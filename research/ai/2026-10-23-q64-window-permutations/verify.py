#!/usr/bin/env python3
"""Exact subspace-intersection replay for matched-window Q(n,4) permutations."""

import argparse
from fractions import Fraction
from itertools import permutations, product
import hashlib
import json
from pathlib import Path
import random


def source_matrix(n, sigma, tau):
    c_dimension = 4 * n
    columns = n * n
    matrix = [[0] * columns for _ in range((4 * n) * c_dimension)]
    for p in range(n):
        for q in range(n):
            column = p * n + q
            for y in range(4):
                for v in range(4):
                    bi = q + v - y
                    ch = p + y - v
                    if 0 <= bi < n and 0 <= ch < n:
                        b_index = sigma[y][bi] * 4 + y
                        c_index = v * n + tau[v][ch]
                        matrix[b_index * c_dimension + c_index][column] += 1
    return matrix


def target_matrix(n):
    c_dimension = 4 * n
    matrix = [[0] * (n * n) for _ in range((4 * n) * c_dimension)]
    for i in range(n):
        for h in range(n):
            column = i * n + h
            for j in range(4):
                b_index = i * 4 + j
                c_index = j * n + h
                matrix[b_index * c_dimension + c_index][column] += 1
    return matrix


def exact_rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0]) if row_count else 0
    pivot_row = 0
    for column in range(column_count):
        pivot = next((r for r in range(pivot_row, row_count) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for r in range(pivot_row + 1, row_count):
            if work[r][column]:
                scale = work[r][column]
                work[r] = [a - scale * b for a, b in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def joined_columns(left, right):
    return [a + b for a, b in zip(left, right)]


def rotate(values, amount):
    amount %= len(values)
    return values[amount:] + values[:amount]


def profiles_for(n, count):
    if n <= 2:
        all_perms = list(permutations(range(n)))
        return list(product(all_perms, repeat=8))

    identity = tuple(range(n))
    reverse = tuple(reversed(range(n)))
    profiles = [
        (identity,) * 8,
        (reverse,) * 8,
        tuple(tuple(rotate(list(identity), j)) for j in range(4))
        + tuple(tuple(rotate(list(reverse), j)) for j in range(4)),
        tuple(tuple(rotate(list(reverse if j % 2 else identity), j)) for j in range(4))
        + tuple(tuple(rotate(list(identity if j % 2 else reverse), j + 1)) for j in range(4)),
    ]
    seen = {tuple(tuple(p) for p in profile) for profile in profiles}
    rng = random.Random(20261023 + n)
    while len(profiles) < count:
        profile = tuple(tuple(rng.sample(range(n), n)) for _ in range(8))
        key = tuple(tuple(p) for p in profile)
        if key not in seen:
            seen.add(key)
            profiles.append(profile)
    return profiles[:count]


def verify(max_n, profile_count):
    if type(max_n) is not int or max_n < 1:
        raise ValueError("max_n must be positive")
    if type(profile_count) is not int or profile_count < 1:
        raise ValueError("profiles must be positive")

    cases = []
    total_profiles = 0
    coverage = {}
    for n in range(1, max_n + 1):
        target = target_matrix(n)
        rank_target = exact_rank(target)
        if rank_target != n * n:
            raise AssertionError(f"target slice rank {rank_target} != n^2 at n={n}")
        profiles = profiles_for(n, profile_count)
        coverage[str(n)] = "exhaustive" if n <= 2 else "deterministic sampled"
        profile_digest = hashlib.sha256()
        minimum_rank = n * n
        maximum_rank = 0
        maximum_intersection = 0
        minimum_source_rank = n * n
        for profile in profiles:
            sigma = profile[:4]
            tau = profile[4:]
            profile_digest.update(json.dumps(profile, separators=(",", ":")).encode())
            profile_digest.update(b"\n")
            source = source_matrix(n, sigma, tau)
            rank_source = exact_rank(source)
            rank_joined = exact_rank(joined_columns(source, target))
            intersection_dimension = rank_source + rank_target - rank_joined
            minimum_correction_rank = rank_target - intersection_dimension
            lower_bound = (n - 1) ** 2
            if minimum_correction_rank < lower_bound:
                raise AssertionError(
                    f"minimum rank {minimum_correction_rank} < {lower_bound} "
                    f"for n={n}, sigma={sigma}, tau={tau}"
                )
            total_profiles += 1
            minimum_rank = min(minimum_rank, minimum_correction_rank)
            maximum_rank = max(maximum_rank, minimum_correction_rank)
            maximum_intersection = max(maximum_intersection, intersection_dimension)
            minimum_source_rank = min(minimum_source_rank, rank_source)
        cases.append({
            "n": n,
            "coverage": coverage[str(n)],
            "profiles_tested": len(profiles),
            "profile_sha256": profile_digest.hexdigest(),
            "minimum_source_subspace_rank": minimum_source_rank,
            "maximum_intersection_dimension": maximum_intersection,
            "minimum_correction_rank": minimum_rank,
            "maximum_correction_rank": maximum_rank,
            "lower_bound": (n - 1) ** 2,
        })
    return {
        "claim": "AI-Q64-WINDOW-PERMUTATIONS-001",
        "exact_rational_replay": True,
        "sizes": list(range(1, max_n + 1)),
        "profiles_tested": total_profiles,
        "coverage_by_size": coverage,
        "requested_sampled_profiles_per_sampled_size": profile_count,
        "first_leg_scope": "all linear maps via exact quotient/intersection minimum-rank identity",
        "lower_bound_checked": "(n-1)^2",
        "general_q_maps_excluded": False,
        "exponent_improvement": False,
        "cases": cases,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=5)
    parser.add_argument("--profiles", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify(args.max_n, args.profiles)
    serialized = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
    print(serialized, end="")

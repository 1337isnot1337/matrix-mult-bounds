#!/usr/bin/env python3
"""Exact subspace-intersection replay for arbitrary Q(n,4) coordinate shifts."""

import argparse
from fractions import Fraction
import json
from pathlib import Path
import random


def source_matrix(n, beta, gamma):
    target_b_dimension = 4 * n
    target_c_dimension = 4 * n
    rows = target_b_dimension * target_c_dimension
    columns = n * n
    matrix = [[0] * columns for _ in range(rows)]
    for p in range(n):
        for q in range(n):
            column = p * n + q
            for y in range(4):
                for v in range(4):
                    i = q + v - beta[y]
                    h = p + y - gamma[v]
                    if 0 <= i < n and 0 <= h < n:
                        b_index = i * 4 + y
                        c_index = v * n + h
                        matrix[b_index * target_c_dimension + c_index][column] += 1
    return matrix


def target_matrix(n):
    target_c_dimension = 4 * n
    rows = (4 * n) * target_c_dimension
    columns = n * n
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(n):
        for h in range(n):
            column = i * n + h
            for j in range(4):
                b_index = i * 4 + j
                c_index = j * n + h
                matrix[b_index * target_c_dimension + c_index][column] += 1
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


def profiles_for(n, count):
    profiles = [
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([0, 1, 2, 3], [0, 1, 2, 3]),
        ([n + 2, -n - 1, 2 * n + 3, -2 * n - 4], [-n, 2 * n + 1, -2 * n - 2, 3 * n + 4]),
        ([3, -2, n + 1, -n - 3], [n + 4, 1, -3, -n - 2]),
        ([n, n - 1, n - 2, n - 3], [-n, -n + 1, -n + 2, -n + 3]),
    ]
    profiles = profiles[:count]
    seen = {(tuple(beta), tuple(gamma)) for beta, gamma in profiles}
    rng = random.Random(20261023 + n)
    while len(profiles) < count:
        bound = 2 * n + 3
        profile = (
            [rng.randint(-bound, bound) for _ in range(4)],
            [rng.randint(-bound, bound) for _ in range(4)],
        )
        key = tuple(profile[0]), tuple(profile[1])
        if key not in seen:
            seen.add(key)
            profiles.append(profile)
    return profiles


def verify(max_n, profile_count):
    if type(max_n) is not int or max_n < 1:
        raise ValueError("max_n must be positive")
    if type(profile_count) is not int or profile_count < 1:
        raise ValueError("profiles must be positive")

    cases = []
    total_profiles = 0
    for n in range(1, max_n + 1):
        target = target_matrix(n)
        rank_target = exact_rank(target)
        if rank_target != n * n:
            raise AssertionError(f"target slice rank {rank_target} != n^2 at n={n}")
        for beta, gamma in profiles_for(n, profile_count):
            source = source_matrix(n, beta, gamma)
            rank_source = exact_rank(source)
            rank_joined = exact_rank(joined_columns(source, target))
            intersection_dimension = rank_source + rank_target - rank_joined
            minimum_correction_rank = rank_target - intersection_dimension
            lower_bound = n * (n - 1) // 2
            if minimum_correction_rank < lower_bound:
                raise AssertionError(
                    f"minimum rank {minimum_correction_rank} < {lower_bound} "
                    f"for n={n}, beta={beta}, gamma={gamma}"
                )
            total_profiles += 1
            cases.append({
                "n": n,
                "beta": beta,
                "gamma": gamma,
                "source_subspace_rank": rank_source,
                "target_subspace_rank": rank_target,
                "intersection_dimension": intersection_dimension,
                "minimum_correction_rank": minimum_correction_rank,
            })
    return {
        "claim": "AI-Q64-ARBITRARY-INNER-SHIFTS-001",
        "exact_rational_replay": True,
        "sizes": list(range(1, max_n + 1)),
        "profiles_requested_per_size": profile_count,
        "profiles_tested": total_profiles,
        "first_leg_scope": "all linear maps via exact quotient/intersection minimum-rank identity",
        "lower_bound_checked": "n*(n-1)//2",
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

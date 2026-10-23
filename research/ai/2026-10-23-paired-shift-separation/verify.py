#!/usr/bin/env python3
"""Exact finite control for the paired-source shift-separation theorem."""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT = ROOT / "results/paired-shift-separation-2026-10-23/verification.json"


def rank_mod(matrix, prime):
    if not matrix or not matrix[0]:
        return 0
    work = [[value % prime for value in row] for row in matrix]
    rows, cols = len(work), len(work[0])
    rank = 0
    for column in range(cols):
        pivot = next((r for r in range(rank, rows) if work[r][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [(value * inverse) % prime for value in work[rank]]
        for row in range(rank + 1, rows):
            factor = work[row][column]
            if factor:
                work[row] = [
                    (left - factor * right) % prime
                    for left, right in zip(work[row], work[rank])
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def build_control():
    prime = 101
    n, m = 9, 4
    interior = list(range(3, 6))

    profiles = [lambda s: 1, lambda s: s]
    profile_matrices = [
        [[profile(q + v) % prime for v in range(m)] for q in interior]
        for profile in profiles
    ]
    profile_ranks = [rank_mod(matrix, prime) for matrix in profile_matrices]
    channel_rank_budget = sum(profile_ranks)

    beta = [
        [
            [((1 + 11 * j + 7 * y + 5 * t + 3 * y * t) % prime)
             for t in range(m)]
            for y in range(m)
        ]
        for j in range(2)
    ]

    first_leg = n * n
    long_dimension = n * m
    residual = []
    for p in range(n):
        for q in range(n):
            target_slice = [0] * (long_dimension * long_dimension)
            source_slice = [0] * (long_dimension * long_dimension)

            for t in range(m):
                row = q * m + t
                column = t * n + p
                target_slice[row * long_dimension + column] = 1

            for y in range(m):
                z = p + y
                if z >= n:
                    continue
                for v in range(m):
                    s = q + v
                    if s >= n:
                        continue
                    for t in range(m):
                        coefficient = (
                            profiles[0](s) * beta[0][y][t]
                            + profiles[1](s) * beta[1][y][t]
                        ) % prime
                        row = s * m + t
                        column = v * n + z
                        index = row * long_dimension + column
                        source_slice[index] = (
                            source_slice[index] + coefficient
                        ) % prime

            residual.append([
                (target - source) % prime
                for target, source in zip(target_slice, source_slice)
            ])

    lower_bound = len(interior) ** 2
    return {
        "field": f"F_{prime}",
        "n": n,
        "m": m,
        "source_first_dimension": first_leg,
        "interior_columns": interior,
        "exceptional_columns": {"B": [], "C": []},
        "bandwidths": {"B": 0, "C": 0},
        "profile_shift_ranks": profile_ranks,
        "channel_rank_budget": channel_rank_budget,
        "target_channel_rank": m,
        "predicted_flattening_lower_bound": lower_bound,
        "observed_residual_flattening_rank": rank_mod(residual, prime),
        "scope": "finite control only; the all-field, all-size claim is proved in proof.md",
    }


def verify():
    report = build_control()
    if report["channel_rank_budget"] >= report["m"]:
        raise ValueError("the finite control must be below the middle width")
    if report["observed_residual_flattening_rank"] < report["predicted_flattening_lower_bound"]:
        raise ValueError("the exact residual rank missed the proved lower bound")
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    report = verify()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

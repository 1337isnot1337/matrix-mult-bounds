#!/usr/bin/env python3
"""Exact controls for the explicit singular shared-map family.

Uses only the Python standard library. A passing run validates these finite
identities and ranks; it does not construct the two missing degeneration maps.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def product(left, right):
    columns = transpose(right)
    return [[sum(a * b for a, b in zip(row, column))
             for column in columns] for row in left]


def identity(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def rank(matrix):
    if not matrix:
        return 0
    reduced = [list(map(Fraction, row)) for row in matrix]
    pivot_row = 0
    for column in range(len(reduced[0])):
        pivot = next((i for i in range(pivot_row, len(reduced))
                      if reduced[i][column]), None)
        if pivot is None:
            continue
        reduced[pivot_row], reduced[pivot] = reduced[pivot], reduced[pivot_row]
        scale = reduced[pivot_row][column]
        reduced[pivot_row] = [x / scale for x in reduced[pivot_row]]
        for i in range(pivot_row + 1, len(reduced)):
            scale = reduced[i][column]
            if scale:
                reduced[i] = [x - scale * y for x, y in
                              zip(reduced[i], reduced[pivot_row])]
        pivot_row += 1
        if pivot_row == len(reduced):
            break
    return pivot_row


def inverse(matrix):
    size = len(matrix)
    augmented = [list(map(Fraction, row)) + list(map(Fraction, unit))
                 for row, unit in zip(matrix, identity(size))]
    for column in range(size):
        pivot = next(i for i in range(column, size) if augmented[i][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [x / scale for x in augmented[column]]
        for i in range(size):
            if i != column:
                scale = augmented[i][column]
                if scale:
                    augmented[i] = [x - scale * y for x, y in
                                    zip(augmented[i], augmented[column])]
    return [row[size:] for row in augmented]


def moment(size, nodes):
    return [[sum(t ** (i + j) for t in nodes) for j in range(size)]
            for i in range(size)]


def block_matrix(shared, q, ell):
    """Assemble from Delta(P X_(a+c)) on a canonical target block."""
    degree = len(shared) - 1
    return [[shared[r + t][a + c]
             for t in range(degree - q + 1)
             for c in range(degree - ell + 1)]
            for r in range(q + 1) for a in range(ell + 1)]


def source_support_rank(m, length, q):
    """Count actual distinct source rows and verify their disjoint support."""
    h = m - 1 - q
    source_rows = {tuple((t, r + t + j) for t in range(h + 1))
                   for r in range(q + 1) for j in range(length)}
    all_positions = [position for row in source_rows for position in row]
    assert len(all_positions) == len(set(all_positions))
    return len(source_rows)


def auxiliary_ranks(shared, q):
    m = len(shared)
    h = m - 1 - q
    first = [[shared[r + t][i] for t in range(h + 1) for i in range(m)]
             for r in range(q + 1)]
    second = [[shared[r + t][i] for r in range(q + 1) for i in range(m)]
              for t in range(h + 1)]
    common = [[shared[r + t][i] for r in range(q + 1) for t in range(h + 1)]
              for i in range(m)]
    return [rank(first), rank(second), rank(common)]


def rational_matrix(matrix):
    return [[str(Fraction(value)) for value in row] for row in matrix]


def exact_shared_coefficients(s):
    m = 2 * s
    vandermonde = [[j ** i for j in range(m)] for i in range(m)]
    inv = inverse(vandermonde)
    regular = [[sum(inv[j][a] * inv[j][b] for j in range(s + 1))
                for b in range(m)] for a in range(m)]
    pole = [[sum(inv[j][a] * inv[j][b] for j in range(s + 1, m))
             for b in range(m)] for a in range(m)]
    p0 = moment(m, range(s + 1))
    p1 = moment(m, range(s + 1, m))
    zero = [[0] * m for _ in range(m)]
    assert product(p0, pole) == zero
    assert product(p1, regular) == zero
    unit = [[x + y for x, y in zip(row1, row2)] for row1, row2 in
            zip(product(p0, regular), product(p1, pole))]
    assert unit == identity(m)
    # Both factors are symmetric, so the transposed coefficient identities
    # also check the reverse-order product.
    return {"P_zero": rational_matrix(p0), "P_linear": rational_matrix(p1),
            "A_regular": rational_matrix(regular), "A_pole": rational_matrix(pole)}


def verify(max_s):
    records = []
    block_rank_count = 0
    source_degree_count = 0
    for s in range(2, max_s + 1):
        m = 2 * s
        degree = m - 1
        n = m * (m + 1) // 2
        p0 = moment(m, range(s + 1))
        pfull = moment(m, range(m))
        fixed = identity(m)
        assert rank(p0) == s + 1
        assert rank(pfull) == m
        assert auxiliary_ranks(p0, s - 1) == [s, s + 1, s + 1]
        degree_records = []
        for q in range(m):
            actual = []
            for ell in range(m):
                observed = rank(block_matrix(p0, q, ell))
                expected = min(s + 1, q + ell + 1, 2 * degree - q - ell + 1)
                assert observed == expected, (s, q, ell, observed, expected)
                actual.append(observed)
                fixed_expected = 1 + min(q + ell, 2 * degree - q - ell)
                assert rank(block_matrix(fixed, q, ell)) == fixed_expected
                assert rank(block_matrix(pfull, q, ell)) == fixed_expected
                block_rank_count += 3
            reflected = min(q, degree - q)
            missing = s - reflected
            expected_sum = 2 * s * (s + 1) - missing * (missing + 1) // 2
            assert sum(actual) == expected_sum
            source_rank = source_support_rank(m, n, q)
            assert source_rank == n + q
            assert sum(actual) <= source_rank
            source_degree_count += 1
            degree_records.append({"q": q, "block_ranks": actual,
                                   "target_rank": sum(actual),
                                   "source_rank": source_rank,
                                   "source_minus_target": source_rank - sum(actual)})
        assert degree_records[s - 1]["source_minus_target"] == 0
        exact_shared_coefficients(s)
        records.append({"s": s, "m": m, "N": n,
                        "auxiliary_and_shared_ranks": [s, s + 1, s + 1],
                        "degrees": degree_records})
    return {
        "status": "exact-finite-controls-passed",
        "claim_scope": "Shared maps and moving rank tests only; missing Y/Z maps.",
        "constructs_tensor_degeneration": False,
        "improves_omega": False,
        "arithmetic": "Python fractions.Fraction and integers",
        "parameters": {"s_min": 2, "s_max": max_s, "nodes": "0,...,2s-1"},
        "coverage": {"block_rank_computations": block_rank_count,
                     "source_degree_support_checks": source_degree_count,
                     "shared_inverse_coefficient_checks": 3 * (max_s - 1)},
        "m4_shared_matrices": exact_shared_coefficients(2),
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-s", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_s < 2:
        parser.error("--max-s must be at least 2")
    report = verify(args.max_s)
    serialized = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
        print(json.dumps({"status": report["status"], "coverage": report["coverage"],
                          "output": str(args.output)}))
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()

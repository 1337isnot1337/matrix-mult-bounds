#!/usr/bin/env python3
"""Exact Segre/Hankel counterexamples outside the proved fixed-scheme range."""

import argparse
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path


def rational_rank(matrix):
    rows = [[Fraction(x) for x in row] for row in matrix]
    if not rows:
        return 0
    pivot = 0
    for column in range(len(rows[0])):
        selected = next((i for i in range(pivot, len(rows)) if rows[i][column]), None)
        if selected is None:
            continue
        rows[pivot], rows[selected] = rows[selected], rows[pivot]
        scale = rows[pivot][column]
        rows[pivot] = [x / scale for x in rows[pivot]]
        for i in range(pivot + 1, len(rows)):
            scale = rows[i][column]
            if scale:
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def determinant_polynomial():
    """Return the exact determinant, with exponents ordered A,B,C,D."""
    positions = {1: 0, 2: 1, 4: 2, 5: 3}
    result = {}
    for permutation in permutations(range(4)):
        if any(i + permutation[i] not in positions for i in range(4)):
            continue
        exponents = [0] * 4
        for i in range(4):
            exponents[positions[i + permutation[i]]] += 1
        inversions = sum(permutation[i] > permutation[j] for i in range(4) for j in range(i + 1, 4))
        key = tuple(exponents)
        result[key] = result.get(key, 0) + (-1) ** inversions
    return {key: value for key, value in result.items() if value}


def family_sequence(a, b, r, u, v):
    m = a + b - 1
    ell, k = m - 2 * r, 3 * r - m
    if not (r < min(a, b) and 2 * r + 1 <= m < 3 * r and len(v) == k):
        raise ValueError("Parameters must satisfy the stated family hypotheses.")
    h = [0] * m
    for j, value in enumerate(v):
        h[ell + j] = u[0] * value
        h[ell + r + j] = u[1] * value
    return h


def recurrence_identity(a, b, r):
    """Compare monomials in u0,u1,v0,...,v(k-1), without sampling."""
    m = a + b - 1
    ell, k = m - 2 * r, 3 * r - m
    h = [None] * m
    for j in range(k):
        for alpha in range(2):
            exponent = [0] * (k + 2)
            exponent[alpha] = exponent[j + 2] = 1
            h[ell + alpha * r + j] = tuple(exponent)

    def times_u(monomial, alpha):
        if monomial is None:
            return None
        exponents = list(monomial)
        exponents[alpha] += 1
        return tuple(exponents)

    return all(times_u(h[s + r], 0) == times_u(h[s], 1) for s in range(m - r))


def family_controls(maximum_r=8):
    records = []
    for r in range(2, maximum_r + 1):
        for m in range(2 * r + 1, 3 * r):
            for a in range(r + 1, (m + 1) // 2 + 1):
                b = m + 1 - a
                k = 3 * r - m
                positions = [m - 2 * r + alpha * r + j for alpha in range(2) for j in range(k)]
                assert len(set(positions)) == 2 * k and min(positions) >= 0 and max(positions) < m
                assert recurrence_identity(a, b, r)
                v = [0] * k
                v[-1] = 1
                h = family_sequence(a, b, r, (1, 1), v)
                rank = rational_rank([[h[p + q] for q in range(b)] for p in range(a)])
                assert rank == r
                boundary = family_sequence(a, b, r, (0, 1), range(1, k + 1))
                boundary_rank = rational_rank([[boundary[p + q] for q in range(b)] for p in range(a)])
                assert boundary_rank <= r
                records.append({
                    "a": a, "b": b, "r": r, "sequence_length": m,
                    "domain_shape": [2, k], "image_dimension": 2 * k,
                    "image_dimension_exceeds_r": 2 * k > r,
                    "formal_recurrence_verified": True,
                    "attained_hankel_rank": rank,
                    "u0_zero_specialization_rank": boundary_rank,
                })
    return records


def report():
    polynomial = determinant_polynomial()
    assert polynomial == {(2, 0, 0, 2): 1, (1, 1, 1, 1): -2, (0, 2, 2, 0): 1}
    h = [0, 1, 2, 0, 3, 6, 0]
    rank = rational_rank([[h[p + q] for q in range(4)] for p in range(4)])
    assert rank == 3
    records = family_controls()
    return {
        "status": "exact_counterexample_to_an_unrestricted_proof_step",
        "determinant_identity": "det H(0,A,B,0,C,D,0) = (A*D-B*C)^2",
        "determinant_monomials": [
            {"exponents_A_B_C_D": list(key), "coefficient": value}
            for key, value in sorted(polynomial.items())
        ],
        "square_domain_counterexample": {
            "a": 4, "b": 4, "r": 3, "domain_shape": [2, 2],
            "image_dimension": 4, "rank_one_input": [[1, 2], [3, 6]],
            "hankel_rank": rank,
        },
        "family_controls": records,
        "family_format_count": len(records),
        "dimension_counterexample_count": sum(row["image_dimension_exceeds_r"] for row in records),
        "proved_frontier_changed": False,
        "new_tensor_restriction_claimed": False,
        "new_exponent_established": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = report()
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "family_controls"}, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact convention controls for the written global RNC obstruction.

The finite controls do not verify the arbitrary-arc geometric theorem.
Only the Python standard library is required.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import comb
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
INPUT_SHA256 = "c53abefde0cb5d5e2e816f96ae6c257ee843f59e6c28d13a6ae1994de9ab88f3"
OUTPUT = ROOT / "results/mixed-longlegs-candidate-2026-10-23/global_rnc_verification.json"


def matrix_product(left, right):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*right)] for row in left]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matrix_inverse(matrix):
    size = len(matrix)
    rows = [[Fraction(x) for x in row]
            + [Fraction(i == j) for j in range(size)]
            for i, row in enumerate(matrix)]
    for col in range(size):
        pivot = next(i for i in range(col, size) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        rows[col] = [x / scale for x in rows[col]]
        for i in range(size):
            if i != col and rows[i][col]:
                scale = rows[i][col]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[col])]
    return [row[size:] for row in rows]


def exact_rank(matrix):
    rows = [[Fraction(x) for x in row] for row in matrix]
    rank = 0
    for col in range(len(rows[0]) if rows else 0):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][col]
        rows[rank] = [x / scale for x in rows[rank]]
        for i in range(rank + 1, len(rows)):
            if rows[i][col]:
                scale = rows[i][col]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def substitution_matrix(degree, frame):
    """R_d(frame) v_d(s,t) = v_d(frame (s,t)), in literal monomial order."""
    alpha, beta = frame[0]
    gamma, delta = frame[1]
    result = []
    for i in range(degree + 1):
        row = []
        for j in range(degree + 1):
            value = sum(
                comb(degree - i, r) * comb(i, j - r)
                * alpha ** (degree - i - r) * beta ** r
                * gamma ** (i - j + r) * delta ** (j - r)
                for r in range(max(0, j - i), min(j, degree - i) + 1)
            )
            row.append(value)
        result.append(row)
    return result


def covariance_controls():
    frames = {
        "shear": [[1, 1], [0, 1]],
        "swap": [[0, 1], [1, 0]],
        "diagonal": [[2, 0], [0, 3]],
        "mixed": [[1, 2], [3, 5]],
    }
    delta = [[int(i + j == ell) for ell in range(14)]
             for i in range(5) for j in range(10)]
    controls = []
    for label, frame in frames.items():
        r4, r9, r13 = [substitution_matrix(d, frame) for d in (4, 9, 13)]
        changed = [[sum(r4[i][u] * r9[j][v]
                        for u in range(5) for v in range(10) if u + v == ell)
                    for ell in range(14)] for i in range(5) for j in range(10)]
        assert changed == matrix_product(delta, r13), label
        q = transpose(matrix_inverse(r13))
        assert matrix_product(changed, transpose(q)) == delta, label
        scalar = Fraction(7, 3)
        scaled = [[scalar * x for x in row] for row in changed]
        q_scaled = [[x / scalar for x in row] for row in q]
        assert matrix_product(scaled, transpose(q_scaled)) == delta, label
        controls.append({
            "frame": label,
            "matrix": frame,
            "degrees": [4, 9, 13],
            "flattening_covariance_equalities": 700,
            "tensor_covariance_equalities": 700,
            "scalar_compensation_equalities": 700,
            "third_action": "R13 inverse transpose",
            "scalar": "7/3",
        })
    return controls


def evaluation(degree, s, t):
    return [s ** (degree - i) * t ** i for i in range(degree + 1)]


def full_slice(width, values):
    assert len(values) == width + 4
    return [[values[i + j] for j in range(width)] for i in range(5)]


def mid_slice(width, values):
    assert len(values) == width
    return [[values[j - i] if 0 <= j - i < width else 0
             for j in range(width + 4)] for i in range(5)]


def output_slice(u, v, values):
    assert u + v == 6 and len(values) == v
    return [[values[i - j] if 0 <= i - j < v else 0
             for j in range(u)] for i in range(5)]


def full_rank_one_controls():
    result = []
    for width in (2, 3, 10):
        for s, t in ((1, 0), (1, 1), (1, -1), (2, 3), (0, 1)):
            literal = full_slice(width, evaluation(width + 3, s, t))
            first = evaluation(4, s, t)
            second = evaluation(width - 1, s, t)
            assert literal == [[x * y for y in second] for x in first]
            rank = exact_rank(literal)
            assert rank == 1
            result.append({"width": width, "parameter": [s, t], "rank": rank})
    return result


def noncurve_full_controls():
    result = []
    for width in (2, 3, 10):
        for prefix in ((0, 1), (1, 1)):
            values = list(prefix) + [0] * (width + 2)
            rank = exact_rank(full_slice(width, values))
            assert rank == 2
            result.append({"width": width, "third_covector": values, "rank": rank})
    return result


def nonfull_controls():
    result = []
    for label, dimension, expected, make in (
        ("Mid(5,2)", 2, 5, lambda x: mid_slice(2, x)),
        ("Out(3,3)", 3, 3, lambda x: output_slice(3, 3, x)),
        ("Out(4,2)", 2, 4, lambda x: output_slice(4, 2, x)),
    ):
        for values in product((-1, 0, 1), repeat=dimension):
            if not any(values):
                continue
            rank = exact_rank(make(values))
            assert rank == expected
            result.append({"block": label, "third_covector": list(values), "rank": rank})
    return result


def third_flattening_rank(dimension, slice_builder):
    slices = [slice_builder([int(i == j) for i in range(dimension)])
              for j in range(dimension)]
    rows = [[matrix[i][j] for matrix in slices]
            for i in range(len(slices[0])) for j in range(len(slices[0][0]))]
    return exact_rank(rows)


def conciseness_controls():
    blocks = [
        ("Full(5,10)", 14, 10, lambda x: full_slice(10, x)),
        ("Full(5,2)", 6, 7, lambda x: full_slice(2, x)),
        ("Full(5,3)", 7, 10, lambda x: full_slice(3, x)),
        ("Out(3,3)", 3, 4, lambda x: output_slice(3, 3, x)),
        ("Out(4,2)", 2, 2, lambda x: output_slice(4, 2, x)),
        ("Mid(5,2)", 2, 6, lambda x: mid_slice(2, x)),
    ]
    result = []
    for label, dimension, copies, make in blocks:
        rank = third_flattening_rank(dimension, make)
        assert rank == dimension
        result.append({"block": label, "copies": copies, "third_rank": rank})
    assert sum(row["copies"] * row["third_rank"] for row in result[1:]) == 140
    return result


def report():
    frozen = (PACKAGE / "discovery_input.json").read_bytes()
    assert sha256(frozen).hexdigest() == INPUT_SHA256
    data = json.loads(frozen)
    assert data["source"]["long_dimensions"] == data["target"]["long_dimensions"] == [100, 140]
    first = [1, 2, 0, 3, 4]
    width_one = full_slice(1, first)
    assert exact_rank(width_one) == 1 and first[0] * first[2] != first[1] ** 2
    return {
        "status": "Exact convention controls accompanying a written global obstruction",
        "field": "Q for controls; C for the geometric theorem",
        "discovery_input_sha256": INPUT_SHA256,
        "arbitrary_arc_theorem_verified_by_finite_controls": False,
        "theorem_proof": "global_rnc_obstruction.md, Sections 2-5",
        "binary_covariance": covariance_controls(),
        "full_rank_one_slices": full_rank_one_controls(),
        "full_noncurve_slices": noncurve_full_controls(),
        "nonfull_slices": nonfull_controls(),
        "third_conciseness": conciseness_controls(),
        "source_third_rank": 140,
        "target_third_rank": 140,
        "width_one_boundary_control": {
            "first_vector": first,
            "rank": 1,
            "rnc_quadratic_value": first[0] * first[2] - first[1] ** 2,
            "meaning": "A Full(5,1) block alone admits rank-one directions outside the RNC",
        },
    }


if __name__ == "__main__":
    result = report()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print("global RNC controls passed: 4 binary frames, 8400 coefficient equalities, "
          "15 rank-one Full slices, 6 noncurve Full slices, 42 other slices, "
          "6 third-flattening ranks, and the width-one boundary control")

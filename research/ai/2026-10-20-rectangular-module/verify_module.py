#!/usr/bin/env python3
"""Exact controls for the rectangular convolution module reformulation."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def rank(matrix):
    rows = [[Fraction(x) for x in row] for row in matrix]
    if not rows:
        return 0
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows))
                      if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        divisor = rows[pivot_row][column]
        rows[pivot_row] = [x / divisor for x in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row and rows[i][column]:
                coefficient = rows[i][column]
                rows[i] = [x - coefficient * y
                           for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def lp(value=0):
    if isinstance(value, dict):
        return {int(e): Fraction(c) for e, c in value.items() if c}
    return {} if not value else {0: Fraction(value)}


def add(left, right):
    result = dict(lp(left))
    for exponent, coefficient in lp(right).items():
        result[exponent] = result.get(exponent, Fraction()) + coefficient
    return lp(result)


def mul(left, right):
    result = {}
    for i, a in lp(left).items():
        for j, b in lp(right).items():
            result[i + j] = result.get(i + j, Fraction()) + a * b
    return lp(result)


def matmul(left, right):
    assert len(left[0]) == len(right)
    result = []
    for row in left:
        output = []
        for j in range(len(right[0])):
            value = {}
            for k in range(len(right)):
                value = add(value, mul(row[k], right[k][j]))
            output.append(value)
        result.append(output)
    return result


def matrix_equal(left, right):
    assert len(left) == len(right)
    assert all(len(a) == len(b) for a, b in zip(left, right))
    return all(lp(a) == lp(b)
               for row_a, row_b in zip(left, right)
               for a, b in zip(row_a, row_b))


def convolution_slice(a, b, i):
    return [[int(k == i + j) for k in range(a + b - 1)]
            for j in range(b)]


def row_reconstruction(slices, row_basis):
    transformed = [matmul(row_basis, h) for h in slices]
    a = len(slices)
    b = len(row_basis)
    n = len(slices[0][0])
    comparisons = 0
    for i in range(a - 1):
        for j in range(b - 1):
            assert transformed[i + 1][j] == transformed[i][j + 1]
            comparisons += n
    output_rows = [None] * (a + b - 1)
    for i, block in enumerate(transformed):
        for j, row in enumerate(block):
            if output_rows[i + j] is not None:
                assert output_rows[i + j] == row
            output_rows[i + j] = row
    assert all(row is not None for row in output_rows)
    return output_rows, comparisons


def laurent_control():
    # The source maps, not the target coefficient formula, are evaluated.
    epsilon = {1: 1}
    inverse_epsilon = {-1: 1}
    y = [[inverse_epsilon, 0, {-1: -1}],
         [0, 1, 0],
         [0, 0, 1]]
    inverse_y = [[epsilon, 0, 1], [0, 1, 0], [0, 0, 1]]
    identity = [[int(i == j) for j in range(3)] for i in range(3)]
    assert matrix_equal(matmul(y, inverse_y), identity)
    z = [[0, epsilon, 0], [1, 0, epsilon], [0, 0, 0], [1, 0, 0]]
    h = [matmul(matmul(y, convolution_slice(2, 3, i)), z)
         for i in range(2)]
    expected = [[[0, 1, 0], [1, 0, epsilon], [0, 0, 0]],
                [[0, 0, 1], [0, 0, 0], [1, 0, 0]]]
    assert all(matrix_equal(left, right)
               for left, right in zip(h, expected))
    assert all(all(e >= 0 for e in coefficient)
               for block in h for row in block for coefficient in row)
    reconstructed, comparisons = row_reconstruction(h, inverse_y)
    assert matrix_equal(reconstructed, z)

    # Add a third source shared coordinate and kill it with A=[I_2 0].
    # This checks the free-slice lift without claiming a new degeneration.
    z_extended = z + [[0, 0, 0]]
    h_extended = [matmul(matmul(y, convolution_slice(3, 3, i)), z_extended)
                  for i in range(3)]
    assert all(matrix_equal(h_extended[i], h[i]) for i in range(2))
    assert matrix_equal(h_extended[2], [[0, 0, 0], [1, 0, 0], [0, 0, 0]])
    reconstructed_extended, comparisons_extended = row_reconstruction(
        h_extended, inverse_y)
    assert matrix_equal(reconstructed_extended, z_extended)
    return {"known_control": "C(2,3) degenerates to T_2",
            "target_coefficient_checks": 18,
            "inverse_identity_entries": 9,
            "row_identity_entries": comparisons,
            "rectangular_control": "C(3,3) followed by [I_2 0]",
            "extra_slice_has_nonzero_limit": True,
            "rectangular_row_identity_entries": comparisons_extended,
            "negative_coefficients": 0}


def shifted(poly, shift, size):
    result = [0] * size
    for j, coefficient in enumerate(poly):
        result[j + shift] = coefficient
    return result


def relation_matrix(quartics):
    # Unknowns are z_x[0..13], z_y[0..13].
    blocks = [(quartics[0], [0] * 5),
              ([0] * 5, quartics[3])]
    blocks += [([-c for c in quartics[i + 1]], quartics[i])
               for i in range(3)]
    result = []
    for first, second in blocks:
        for shift in range(10):
            result.append(shifted(first, shift, 14)
                          + shifted(second, shift, 14))
    return result


def coprime_control():
    quartics = [[1, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [2, 2, 0, 0, 1]]
    assert rank(quartics) == 4
    first_sum = [shifted(u, j, 10)
                 for u in (quartics[0], quartics[3]) for j in range(6)]
    second_sum = [shifted(u, j, 14)
                  for u in (quartics[0], quartics[3]) for j in range(10)]
    first_rank = rank(first_sum)
    second_rank = rank(second_sum)
    total_rank = rank(relation_matrix(quartics))
    assert first_rank == 10
    assert second_rank == 14
    assert total_rank == 28

    # A common factor must not be silently treated as a coprime example.
    common_factor = [[int(j == i + 1) for j in range(5)] for i in range(4)]
    common_rank = rank(relation_matrix(common_factor))
    assert common_rank < 28
    return {"quartics_ascending_t_coefficients": quartics,
            "quartic_span_rank": 4,
            "rank_u0_S5_plus_u3_S5": first_rank,
            "rank_u0_S9_plus_u3_S9": second_rank,
            "relation_system_shape": [50, 28],
            "relation_system_rank": total_rank,
            "common_factor_control_rank": common_rank,
            "common_factor_control_requires_separate_argument": True}


def parity_control(m):
    assert m >= 4 and m % 2 == 0
    s = m // 2
    degree = m - 1
    n = m * (m + 1) // 2
    pairs = [(p, a) for p in range(m) for a in range(p + 1)]
    middle = [(p, r) for p in range(degree) for r in range(-1, p + 1)]
    middle += [(degree, r) for r in range(0, degree, 2)]
    expected_rank = n + s - 1
    assert len(middle) == expected_rank
    left = [[[int(p == q and r == a - alpha) for q, r in middle]
             for p, a in pairs] for alpha in range(2)]
    right = [[[int(v == degree - p and r == 2 * j - c)
               for v, c in pairs] for p, r in middle] for j in range(s)]
    checks = 0
    for alpha in range(2):
        for j in range(s):
            for iy, (p, a) in enumerate(pairs):
                for iz, (v, c) in enumerate(pairs):
                    actual = sum(left[alpha][iy][k] * right[j][k][iz]
                                 for k in range(expected_rank))
                    expected = int(p + v == degree and a + c == 2 * j + alpha)
                    assert actual == expected
                    checks += 1
    stacked_left = left[0] + left[1]
    concatenated_right = [sum((right[j][k] for j in range(s)), [])
                          for k in range(expected_rank)]
    left_rank = rank(stacked_left)
    right_rank = rank(concatenated_right)
    assert left_rank == right_rank == expected_rank
    return {"m": m, "n": n, "middle_dimension": expected_rank,
            "suggested_source_B": expected_rank - 1,
            "left_rank": left_rank, "right_rank": right_rank,
            "coefficient_checks": checks}


def solve_full_column_rank(matrix, rhs):
    width = len(matrix[0])
    output_width = len(rhs[0])
    rows = [[Fraction(x) for x in a + b] for a, b in zip(matrix, rhs)]
    pivot_row = 0
    for column in range(width):
        pivot = next(i for i in range(pivot_row, len(rows)) if rows[i][column])
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        divisor = rows[pivot_row][column]
        rows[pivot_row] = [x / divisor for x in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row and rows[i][column]:
                coefficient = rows[i][column]
                rows[i] = [x - coefficient * y
                           for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
    assert all(not any(row) for row in rows[pivot_row:])
    return [row[width:width + output_width] for row in rows[:width]]


def cubic_syzygy_control():
    b = 10
    degree = 3
    g = [[0, 1, 0, 0], [1, 0, 0, 1]]
    product_matrix = [shifted(poly, h, b + degree + 1)
                      for poly in g for h in range(b + 1)]
    syzygies = []
    for h in range(b - degree + 1):
        syzygies.append(shifted(g[1], h, b + 1)
                        + shifted([-c for c in g[0]], h, b + 1))
    assert rank(product_matrix) == 14
    assert rank(syzygies) == 8
    assert all(not sum(a * product_matrix[k][j] for k, a in enumerate(row))
               for row in syzygies for j in range(14))
    z = [[i * i - 3, 2 * i + 1] for i in range(14)]
    f = [[sum(row[k] * z[k][j] for k in range(14)) for j in range(2)]
         for row in product_matrix]
    assert all(not sum(a * f[k][j] for k, a in enumerate(row))
               for row in syzygies for j in range(2))
    recovered = solve_full_column_rank(product_matrix, f)
    assert recovered == z
    corrupted = [list(row) for row in f]
    corrupted[0][0] += 1
    assert any(sum(a * corrupted[k][0] for k, a in enumerate(row))
               for row in syzygies)
    return {"g_ascending_t_coefficients": g,
            "product_matrix_shape": [22, 14], "product_matrix_rank": 14,
            "syzygy_matrix_shape": [8, 22], "syzygy_matrix_rank": 8,
            "syzygy_product_zero_entries": 112,
            "reconstructed_moment_entries": 28,
            "corrupted_right_factor_rejected": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {"status": "exact-controls-verified",
              "arithmetic": "Python integers and fractions.Fraction",
              "constructs_new_full_target_degeneration": False,
              "improves_omega": False,
              "row_control": laurent_control(),
              "restricted_obstruction_control": coprime_control(),
              "parity_factor_controls": [parity_control(m) for m in (4, 6, 8, 10)],
              "cubic_syzygy_control": cubic_syzygy_control()}
    serialized = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
        print(json.dumps({"status": report["status"],
                          "output": str(args.output),
                          "coprime_relation_rank": report[
                              "restricted_obstruction_control"]["relation_system_rank"]}))
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()

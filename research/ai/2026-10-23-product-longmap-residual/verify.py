"""Exact slice-space checks for two fixed product long maps.

This standard-library verifier does not search for general tensor maps.
All characteristic-zero ranks use Fraction arithmetic. Finite-field ranks
are additional controls; they do not replace the characteristic-zero
proof or certify a new matrix multiplication algorithm.
"""

import argparse
from fractions import Fraction
from itertools import product
import json
from math import isqrt
from pathlib import Path


def _check_characteristic(characteristic):
    if type(characteristic) is not int or characteristic < 0:
        raise ValueError("Characteristic must be zero or a prime.")
    if characteristic == 0:
        return
    if characteristic < 2 or any(
        characteristic % d == 0 for d in range(2, isqrt(characteristic) + 1)
    ):
        raise ValueError("A finite characteristic must be prime.")


def _check_n(n):
    if type(n) is not int or n < 5:
        raise ValueError("The fixed long maps require an integer n >= 5.")


def sparse_rank(rows, characteristic=0):
    """Rank of sparse rows by exact elimination over Q or a prime field."""
    _check_characteristic(characteristic)
    pivots = {}
    for original in rows:
        if characteristic:
            row = {}
            for column, value in original.items():
                value = Fraction(value)
                entry = value.numerator * pow(
                    value.denominator, -1, characteristic
                ) % characteristic
                if entry:
                    row[column] = entry
        else:
            row = {column: Fraction(value) for column, value in original.items()
                   if value}
        while row:
            column = min(row)
            value = row[column]
            if column not in pivots:
                if characteristic:
                    inverse = pow(value, -1, characteristic)
                    pivots[column] = {
                        j: entry * inverse % characteristic
                        for j, entry in row.items()
                    }
                else:
                    pivots[column] = {j: entry / value
                                      for j, entry in row.items()}
                break
            pivot = pivots[column]
            for j, entry in pivot.items():
                updated = row.get(j, 0) - value * entry
                if characteristic:
                    updated %= characteristic
                if updated:
                    row[j] = updated
                else:
                    row.pop(j, None)
    return len(pivots)


def add_rows(first, second, second_scale=1):
    result = dict(first)
    for column, value in second.items():
        updated = result.get(column, 0) + second_scale * value
        if updated:
            result[column] = updated
        else:
            result.pop(column, None)
    return result


def tensor_row(first, second, second_dimension):
    return {i * second_dimension + j: x * y
            for i, x in first.items() for j, y in second.items() if x * y}


def dual_rows_twice(n):
    """Twice the L_(i,a) rows of equations (4)--(5), as sparse integers."""
    _check_n(n)
    r = n - 1
    rows = []
    for t in range(1, n - 1):
        for a in range(2):
            exponent = t + 3 * a
            row = {exponent: 1 if 4 <= exponent <= n - 2 else 2}
            if a == 0 and t == 3:
                row[n + 2] = 2
            if a == 1 and t == n - 4:
                row[0] = 2
            rows.append(row)
    rows.extend([{0: 2}, {n + 2: -2}])
    if len(rows) != 2 * r:
        raise ArithmeticError("Incorrect number of dual rows.")
    return rows


def factor_spaces(n):
    """Return row bases for 2H(V), 2J(U), and 2H(O(U))."""
    _check_n(n)
    r = n - 1
    dual = dual_rows_twice(n)
    source = [{} for _ in range(n)]
    for i, a, b, q in product(range(r), range(2), range(2), range(n)):
        value = dual[2 * i + a].get(q + 3 * b, 0)
        if value:
            source[q][4 * i + 2 * a + b] = value
    target = [{4 * i: 2, 4 * i + 3: 2} for i in range(r)]
    original = [dict(source[t]) for t in range(1, n - 1)]
    original.append(add_rows(source[0], source[n - 1], -1))
    return source, target, original


def good_outer_indices(n):
    _check_n(n)
    return list(range(n - 5, 3)) + [n - 2] if n <= 7 else [n - 2]


def paired_spaces(n):
    """Complete paired slice rows, after the stated coordinate permutation.

    Coefficients are scaled by four: each factor was scaled by two.
    These matrices are assembled directly, without using the tensor-space
    intersection dimension formula.
    """
    source, target, original = factor_spaces(n)
    dimension = 4 * (n - 1)
    paired_source = [tensor_row(x, y, dimension)
                     for x in source for y in source]
    paired_target = [tensor_row(x, y, dimension)
                     for x in target for y in target]
    paired_original = [tensor_row(x, y, dimension)
                       for x in original for y in original]
    residual = [add_rows(t, s, -1)
                for t, s in zip(paired_target, paired_original)]
    return paired_source, paired_target, residual


def check_one_factor_equations(n):
    """Check every coefficient of the displayed H(x) block equations."""
    source, target, original = factor_spaces(n)
    r = n - 1
    for q, t in product(range(n), range(1, n - 1)):
        alpha = 1 if 4 <= t <= n - 2 else 2
        beta = 1 if 4 <= t + 3 <= n - 2 else 2
        expected = [
            alpha * int(q == t),
            alpha * int(q == t - 3) + 2 * int(t == 3 and q == n - 1),
            beta * int(q == t + 3) + 2 * int(t == n - 4 and q == 0),
            beta * int(q == t),
        ]
        actual = [source[q].get(4 * (t - 1) + index, 0)
                  for index in range(4)]
        if actual != expected:
            raise ArithmeticError("A regular H(x) coefficient changed.")
    for q in range(n):
        expected = [2 * int(q == 0), 0, 0, -2 * int(q == n - 1)]
        actual = [source[q].get(4 * (r - 1) + index, 0)
                  for index in range(4)]
        if actual != expected:
            raise ArithmeticError("A boundary H(x) coefficient changed.")
    for i in good_outer_indices(n):
        if original[i] != target[i]:
            raise ArithmeticError("An asserted exact old-map slice changed.")
    return 4 * n * r


def verify_case(n, *, direct=False, characteristic=0):
    _check_n(n)
    _check_characteristic(characteristic)
    if characteristic == 2:
        raise ValueError("The fixed half-coefficient maps exclude characteristic two.")
    r = n - 1
    source, target, original = factor_spaces(n)
    ranks = [sparse_rank(rows, characteristic)
             for rows in (source, target, source + target)]
    d = ranks[0] + ranks[1] - ranks[2]
    expected_d = max(9 - n, 1)
    expected_residual = r * r - expected_d * expected_d
    if ranks[:2] != [n, r] or d != expected_d:
        raise ArithmeticError("The exact one-factor intersection formula failed.")
    row = {
        "n": n,
        "characteristic": characteristic,
        "field": "Q" if characteristic == 0 else f"F_{characteristic}",
        "one_factor_source_rank": ranks[0],
        "one_factor_target_rank": ranks[1],
        "one_factor_union_rank": ranks[2],
        "one_factor_intersection_dimension": d,
        "target_first_dimension": r * r,
        "paired_intersection_dimension": d * d,
        "minimum_first_residual_rank": expected_residual,
        "old_first_map_attains_minimum": True,
        "exact_old_map_outer_indices": good_outer_indices(n),
        "one_factor_coefficients_checked": check_one_factor_equations(n),
        "direct_paired_rank_replay": direct,
    }
    if direct:
        paired_source, paired_target, residual = paired_spaces(n)
        sr = sparse_rank(paired_source, characteristic)
        ur = sparse_rank(paired_source + paired_target, characteristic)
        rr = sparse_rank(residual, characteristic)
        if (sr, ur - sr, rr) != (n * n, expected_residual, expected_residual):
            raise ArithmeticError("The direct paired residual-rank formula failed.")
        if sr + r * r - ur != expected_d * expected_d:
            raise ArithmeticError("The direct paired intersection formula failed.")
        good = good_outer_indices(n)
        if any(residual[r * i + k] for i, k in product(good, repeat=2)):
            raise ArithmeticError("The asserted complete residual kernel changed.")
        row.update({
            "direct_paired_source_rank": sr,
            "direct_paired_union_rank": ur,
            "direct_old_map_residual_rank": rr,
            "paired_ambient_dimension": (4 * r) ** 2,
        })
    return row


def verify():
    rational_cases = [verify_case(n, direct=True)
                      for n in list(range(5, 13)) + [16]]
    larger_factor_cases = [verify_case(n) for n in (32, 64, 200)]
    finite_field_cases = [
        verify_case(n, direct=True, characteristic=prime)
        for prime, n in [(3, 5), (3, 6), (3, 8), (3, 12), (3, 16), (5, 8)]
    ]
    return {
        "claim_id": "AI-PRODUCT-LONGMAP-RESIDUAL-001",
        "statement": "min rank_A(M-(A tensor B_old tensor C_old)Q)=(n-1)^2-max(9-n,1)^2",
        "range": "n >= 5; every field of characteristic different from two",
        "proof_status": "written proof with exact finite replay; not externally reviewed",
        "scope": {
            "arbitrary_first_map": True,
            "two_long_maps_fixed_to_pinned_product_reference": True,
            "excludes_arbitrary_long_maps": False,
            "excludes_general_degenerations": False,
            "improves_omega": False,
        },
        "rational_direct_cases": rational_cases,
        "larger_rational_one_factor_cases": larger_factor_cases,
        "finite_field_direct_controls": finite_field_cases,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, nargs="+")
    parser.add_argument("--direct", action="store_true")
    parser.add_argument("--characteristic", type=int, default=0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = ([verify_case(n, direct=args.direct,
                           characteristic=args.characteristic) for n in args.n]
              if args.n else verify())
    payload = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload)
    print(payload, end="")

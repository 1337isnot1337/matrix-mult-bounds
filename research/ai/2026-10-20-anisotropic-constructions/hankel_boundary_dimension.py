#!/usr/bin/env python3
"""Exact controls for the first-boundary Hankel/Segre dimension argument.

Only the Python standard library is required.  The general proof is
in hankel_boundary_dimension.md; these are finite implementation controls.
"""

import argparse
from fractions import Fraction
import json
from math import comb, gcd, lcm
from pathlib import Path

from hankel_symbol_dimension import jet, rank, gcd as polynomial_gcd


def integer_null_vector(matrix):
    """Return the normalized integer generator of a one-dimensional kernel."""
    rows = [[Fraction(value) for value in row] for row in matrix]
    columns = len(rows[0])
    pivots = []
    active = 0
    for column in range(columns):
        pivot = next((i for i in range(active, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[active], rows[pivot] = rows[pivot], rows[active]
        divisor = rows[active][column]
        rows[active] = [value / divisor for value in rows[active]]
        for i in range(len(rows)):
            if i != active and rows[i][column]:
                multiple = rows[i][column]
                rows[i] = [x - multiple*y for x, y in zip(rows[i], rows[active])]
        pivots.append(column)
        active += 1
        if active == len(rows):
            break
    free = [column for column in range(columns) if column not in pivots]
    if len(free) != 1:
        raise ValueError("Expected a one-dimensional kernel.")
    vector = [Fraction(0)]*columns
    vector[free[0]] = Fraction(1)
    for row, pivot in enumerate(pivots):
        vector[pivot] = -rows[row][free[0]]
    denominator = lcm(*(value.denominator for value in vector))
    answer = [int(value*denominator) for value in vector]
    divisor = gcd(*answer)
    answer = [value // divisor for value in answer]
    if next(value for value in answer if value) < 0:
        answer = [-value for value in answer]
    assert all(sum(x*y for x, y in zip(row, answer)) == 0 for row in matrix)
    return answer


def repeated_endpoint_pencil(r):
    """Endpoints supported to order r at zero and one.

    The normalized formulas come from the top-coefficient Frobenius
    functional on F[z]/(z^r (z-1)^r), divided by the opposite factor.
    They obey h1(q0 p)=h0(q1 p), giving annihilator q0-t*q1.
    """
    m = 3*r - 1
    q0 = [0]*r + [1]
    q1 = [(-1)**(r-j)*comb(r, j) for j in range(r+1)]
    h0 = [comb(3*r-2-j, r-1-j) if j < r else 0 for j in range(m)]
    h1 = [-sum(comb(j, k)*(-1)**(r-1-k)*comb(3*r-2-k, r-1-k)
               for k in range(min(j, r-1)+1)) for j in range(m)]
    for shift in range(m-r):
        assert sum(q0[j]*h0[shift+j] for j in range(r+1)) == 0
        assert sum(q1[j]*h1[shift+j] for j in range(r+1)) == 0
        assert sum(q0[j]*h1[shift+j]-q1[j]*h0[shift+j]
                   for j in range(r+1)) == 0
    return h0, h1, q0, q1


def moving_line_controls():
    records = []
    for r in range(2, 7):
        h0, h1, q0, q1 = repeated_endpoint_pencil(r)
        m = len(h0)
        specializations = []
        for parameter in (0, 1, 2, 3, None):
            h = h1 if parameter is None else [x+parameter*y for x, y in zip(h0, h1)]
            q = q1 if parameter is None else [x-parameter*y for x, y in zip(q0, q1)]
            equations = [[h[shift+j] for j in range(r+1)] for shift in range(m-r)]
            assert all(sum(x*y for x, y in zip(row, q)) == 0 for row in equations)
            assert rank(equations) == r
            recovered = integer_null_vector(equations)
            divisor = gcd(*q)
            normalized = [value // divisor for value in q]
            if next(value for value in normalized if value) < 0:
                normalized = [-value for value in normalized]
            assert recovered == normalized
            hankel_ranks = []
            for a in range(r+1, (m+1)//2+1):
                b = m+1-a
                actual = rank([[h[p+s] for s in range(b)] for p in range(a)])
                assert actual == r
                hankel_ranks.append({"a": a, "b": b, "rank_mod_101": actual})
            specializations.append({
                "parameter": "infinity" if parameter is None else parameter,
                "sequence": h,
                "homogeneous_annihilator_coefficients": normalized,
                "annihilator_equation_rank_mod_101": r,
                "unique_annihilator_recovered_over_Q": True,
                "hankel_formats": hankel_ranks,
            })
        generic_polynomial = [x-2*y for x, y in zip(q0, q1)]
        derivative = [j*generic_polynomial[j] for j in range(1, len(generic_polynomial))]
        assert polynomial_gcd(generic_polynomial, derivative, 101) == [1]
        records.append({
            "r": r, "sequence_length": m,
            "q0": q0, "q1": q1,
            "endpoint_schemes": ["r-fold zero", "r-fold one"],
            "formal_pencil_recurrence_verified": True,
            "parameter_two_annihilator_is_reduced_mod_101": True,
            "specializations": specializations,
        })
    return records


def second_jet_controls():
    records = []
    for r in range(2, 7):
        m, degree = 3*r-1, 3*r-2
        rows = [jet(degree, point, order) for point in range(r) for order in range(3)]
        relation = integer_null_vector([list(column) for column in zip(*rows)])
        tangent = [row for i, row in enumerate(rows) if i % 3 != 2]
        assert rank(rows) == m and rank(tangent) == 2*r
        highest = [relation[3*i+2] for i in range(r)]
        assert all(highest)
        deletion_ranks = []
        for i in range(r):
            deleted = [row for j, row in enumerate(rows) if j != 3*i+2]
            actual = rank(deleted)
            assert actual == m
            deletion_ranks.append(actual)
        records.append({
            "r": r, "points": list(range(r)), "sequence_length": m,
            "jet_row_order": "point first, then orders0,1,2",
            "full_jet_rank_mod_101": m, "tangent_rank_mod_101": 2*r,
            "primitive_integer_jet_relation": relation,
            "highest_jet_relation_coefficients": highest,
            "all_highest_coefficients_nonzero": True,
            "ranks_after_each_highest_jet_deletion_mod_101": deletion_ranks,
        })
    return records


def boundary_dimension_cap(a, b, r):
    if not (r >= 2 and r < min(a, b) and a+b-1 == 3*r-1):
        raise ValueError("The first-boundary theorem hypotheses do not hold.")
    return max(r, 4)


def square_block_test(a, b, r, block_size, total_dimension):
    cap = boundary_dimension_cap(a, b, r)
    source_dimension = a*b*(a+b-1)
    if not (block_size**2 <= total_dimension <= source_dimension):
        raise ValueError("Invalid concise target dimension.")
    loss = source_dimension-total_dimension
    lifted = block_size+2*loss
    coefficient_cap = cap*a*b
    return {
        "a": a, "b": b, "r": r, "symbol_dimension_cap": cap,
        "source_leg_dimension": source_dimension,
        "target_block_size": block_size, "total_target_leg_dimension": total_dimension,
        "projection_loss": loss, "lifted_rank_one_slice_upper_bound": lifted,
        "next_symbol_rank_threshold": (r+1)*a*b,
        "block_dimension": block_size**2, "coefficient_dimension_cap": coefficient_cap,
        "ordinary_restriction_excluded": block_size**2 > coefficient_cap and lifted < (r+1)*a*b,
        "singular_degeneration_excluded": False,
    }


def report():
    return {
        "claim": "First-boundary Hankel Segre image dimension at most max(r,4), for m=3r-1",
        "moving_line_controls": moving_line_controls(),
        "second_jet_controls": second_jet_controls(),
        "ordinary_block_controls": [
            square_block_test(7, 8, 5, 25, 650),
            square_block_test(7, 8, 5, 25, 625),
            square_block_test(7, 8, 5, 25, 628),
            square_block_test(7, 8, 5, 25, 629),
        ],
        "singular_exclusion_claimed": False,
        "new_exponent_established": False,
        "proof_scope_extended_beyond_first_boundary": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = report()
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({
        "claim": result["claim"],
        "moving_line_rank_parameters": len(result["moving_line_controls"]),
        "moving_line_specializations": sum(len(row["specializations"]) for row in result["moving_line_controls"]),
        "second_jet_controls": len(result["second_jet_controls"]),
        "ordinary_block_controls": result["ordinary_block_controls"],
        "new_exponent_established": False,
    }, indent=2))


if __name__ == "__main__":
    main()

"""Exact controls for the cyclic physical-quotient volume bound.

The arbitrary-field proof is in cyclic_quotient_volume.md.  This file
checks the coordinate block formula, sharp projections, and explicit
failed block inclusions above the long dimension.  Standard library only.
"""

from fractions import Fraction
from math import comb
import json
from pathlib import Path


PRIME = 1000003


def rank_mod(rows, prime=PRIME):
    matrix = [[int(x) % prime for x in row] for row in rows]
    if not matrix:
        return 0
    rank = 0
    for col in range(len(matrix[0])):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][col], -1, prime)
        matrix[rank] = [x*inverse % prime for x in matrix[rank]]
        for i in range(rank+1, len(matrix)):
            factor = matrix[i][col]
            if factor:
                matrix[i] = [(x-factor*y) % prime
                             for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def rank_q(rows):
    matrix = [[Fraction(x) for x in row] for row in rows]
    if not matrix:
        return 0
    rank = 0
    for col in range(len(matrix[0])):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        value = matrix[rank][col]
        matrix[rank] = [x/value for x in matrix[rank]]
        for i in range(rank+1, len(matrix)):
            factor = matrix[i][col]
            if factor:
                matrix[i] = [x-factor*y for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def triangular_projection(a, b):
    """pi_t,(i,j)=(-1)^j binom(b-1,j) [t=i+b-1-j]."""
    x = a+b-1
    return [[(-1)**j*comb(b-1, j)*int(t == i+b-1-j)
             for i in range(a) for j in range(b)] for t in range(x)]


def short_row_support(pi, a, b):
    return [[row[i*b+j] for i in range(a)]
            for row in pi for j in range(b)]


def block_generators(pi, a, b):
    """Rows span L: one generator for every free pair (i,k)."""
    return [[pi[t][i*b+k-p] if 0 <= k-p < b else 0
             for t in range(len(pi)) for p in range(a)]
            for i in range(a) for k in range(a+b-1)]


def required_block_generators(output_size, pi_in, a, b):
    """Rows span M_out tensor the sum of input block row spaces."""
    return [[row[p*b+s] if t == out else 0
             for t in range(output_size) for p in range(a)]
            for out in range(output_size) for row in pi_in for s in range(b)]


def block_formula_check(pi, a, b):
    x, m = a+b-1, len(pi)
    coefficients = [[[((i+2)*(k+3)*(s+5) % 17)-8 for s in range(b)]
                     for k in range(x)] for i in range(a)]
    physical = [[coefficients[i][p+j][s] for p in range(a) for s in range(b)]
                for i in range(a) for j in range(b)]
    direct = [[sum(pi[t][r]*physical[r][c] for r in range(a*b))
               for c in range(a*b)] for t in range(m)]
    generators = block_generators(pi, a, b)
    for s in range(b):
        block = [sum(coefficients[i][k][s]*generators[i*x+k][t*a+p]
                     for i in range(a) for k in range(x))
                 for t in range(m) for p in range(a)]
        expected = [direct[t][p*b+s] for t in range(m) for p in range(a)]
        if block != expected:
            raise AssertionError("The physical and fixed-column-block formulas disagree.")
    return m*a*b


def sharp_case(a, b):
    pi = triangular_projection(a, b)
    x = a+b-1
    rho = rank_q(short_row_support(pi, a, b))
    pi_rank = rank_mod(pi)
    block_rank = rank_mod(block_generators(pi, a, b))
    if (pi_rank, rho, block_rank) != (x, a, a*x):
        raise AssertionError("A sharp triangular projection rank control failed.")
    return {"a": a, "b": b, "quotient_dimension": x,
            "short_row_support_dimension_over_Q": rho,
            "projection_rank_mod_prime": pi_rank,
            "block_image_rank_mod_prime": block_rank,
            "proved_rational_block_rank_upper_bound": rho*x,
            "rational_block_rank_certified_exact": True,
            "direct_physical_block_coefficients_checked": block_formula_check(pi, a, b),
            "volume_bound_attained": True}


def oversized_coordinate_case(a, b):
    x, m = a+b-1, a+b
    if m > a*b:
        raise ValueError("This coordinate quotient does not fit.")
    pi = [[int(t == c) for c in range(a*b)] for t in range(m)]
    rho = rank_q(short_row_support(pi, a, b))
    blocks = block_generators(pi, a, b)
    required = required_block_generators(m, pi, a, b)
    block_rank, required_rank = rank_q(blocks), rank_q(required)
    union_rank = rank_q(blocks+required)
    if required_rank != m*rho or not union_rank > block_rank:
        raise AssertionError("An oversized square quotient escaped the block inclusion test.")
    return {"a": a, "b": b, "quotient_dimension": m,
            "short_row_support_dimension_over_Q": rho,
            "source_block_dimension_over_Q": block_rank,
            "required_target_block_dimension_over_Q": required_rank,
            "source_plus_target_block_dimension_over_Q": union_rank,
            "source_block_dimension_upper_bound": x*rho,
            "exact_common_block_inclusion_fails": True,
            "direct_physical_block_coefficients_checked": block_formula_check(pi, a, b)}


def report():
    return {"claim": "Exact cyclic quotient lifts have volume at most (a+b-1)^3.",
            "rank_certificate_prime": PRIME,
            "sharp_triangular_projections": [sharp_case(a, b) for a, b in
                ((2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (5, 6), (8, 8))],
            "oversized_coordinate_quotients": [oversized_coordinate_case(a, b)
                for a, b in ((2, 3), (3, 3), (4, 4))],
            "critical_volume_ratio_at_smallest_source": "729/1250",
            "arbitrary_restrictions_excluded": False,
            "arbitrary_degenerations_excluded": False,
            "new_exponent_established": False}


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[3]
    output = root / "results/anisotropic-constructions-2026-10-20/cyclic-quotient-volume-controls.json"
    output.write_text(json.dumps(report(), indent=2)+"\n")
    print(output)

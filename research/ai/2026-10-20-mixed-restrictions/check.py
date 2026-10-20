"""Exact slice-rank controls for the all-dimension mixed restriction bound."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

import sympy as sp


def coordinates(m):
    return [(a, degree - a) for degree in range(m) for a in range(degree + 1)]


def target_slice(m, vector):
    if m < 1 or len(vector) != m:
        raise ValueError("one coefficient per positive shared dimension required")
    points = coordinates(m)
    return sp.Matrix([[vector[a + c] if a + b + c + d == m - 1 else 0
                       for c, d in points] for a, b in points])


def source_slice(m, B, vector):
    if m < 1 or B < 1 or len(vector) != m or not any(vector):
        raise ValueError("positive dimensions and a nonzero coefficient vector required")
    return sp.Matrix([[vector[k - j] if 0 <= k - j < m else 0
                       for k in range(B + m - 1)] for j in range(B)])


def necessary_length(m, k=1, canonical=True):
    if not isinstance(m, int) or not isinstance(k, int) or m < 1 or k < 1:
        raise ValueError("positive integer dimensions required")
    N = m * (m + 1) // 2
    D = m - 1
    slice_bound = m if canonical else (m + 1)**2 // 4
    return max(k * N, 2 * k * N - D - k * slice_bound)


def run():
    ranks = []
    for m in range(2, 9):
        pure = [1] + [0] * (m - 1)
        central = [int(i == (m - 1)//2) for i in range(m)]
        minimum = int(target_slice(m, pure).rank())
        maximum = int(target_slice(m, central).rank())
        expected_maximum = (m + 1)**2 // 4
        if minimum != m or maximum != expected_maximum:
            raise ArithmeticError("incorrect target slice formula")
        for vector in [pure, central, list(range(1, m + 1))]:
            B = m + 2
            if source_slice(m, B, vector).rank() != B:
                raise ArithmeticError("source polynomial slice not injective")
        ranks.append({"m": m, "minimum_slice_rank": minimum,
                      "maximum_slice_rank": maximum})
    bounds = []
    for m in [2, 3, 4, 8, 16, 32, 53, 64, 128, 512]:
        N = m * (m + 1) // 2
        for k in [1, 3]:
            canonical = necessary_length(m, k)
            arbitrary = necessary_length(m, k, False)
            bounds.append({"m": m, "k": k, "N": N,
                           "canonical_B_lower": canonical,
                           "canonical_overhead_lower": str(Fraction(canonical, k*N)),
                           "independent_identifications_B_lower": arbitrary,
                           "independent_overhead_lower": str(Fraction(arbitrary, k*N)),
                           "per_factor_gorenstein_cover_minimum_length": m*m})
    return {"target_slice_cases": ranks, "large_formula_cases": bounds,
            "ordinary_restriction_limiting_overhead": {"canonical": 2, "independent": "3/2"},
            "does_not_exclude": "Arbitrary Laurent-parameter tensor degenerations",
            "new_exponent_established": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    content = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
    print(content, end="")

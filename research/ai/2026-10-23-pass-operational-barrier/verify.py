"""Exact controls for the Pass packing extension of the operational barrier.

Only standard-library arithmetic is used. The finite controls do not prove
the all-parameter theorem and do not verify a tensor degeneration.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def _positive_integer(name: str, value: int) -> None:
    if type(value) is not int or value < 1:
        raise ValueError(f"{name} must be a positive integer")


def _nonnegative_integer(name: str, value: int) -> None:
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")


def profile_cube_numerator(a: int, b: int) -> int:
    """Return 16*G(a,b)^3, equivalently 16*F_star(C(a,b))^4."""
    _positive_integer("a", a)
    _positive_integer("b", b)
    m, largest = sorted((a, b))
    return (3 * m - 1) * (2 * largest + m - 1) ** 3


def profile_cube(a: int, b: int) -> Fraction:
    return Fraction(profile_cube_numerator(a, b), 16)


def ratio_margin_numerator(a: int, b: int, t: int) -> int:
    """Return an integer with the sign of the cubed ratio inequality."""
    _positive_integer("t", t)
    before = profile_cube_numerator(a, b)
    after = profile_cube_numerator(a, b + t)
    width_before = a + 2 * b - 1
    width_after = width_before + 2 * t
    return after * width_before**3 - before * width_after**3


def pass_margin_numerator(a: int, b: int, c: int, t: int) -> int:
    """Return 16*(c^3*G(a,b+t)^3 - (c+2)^3*G(a,b)^3).

    A negative value rejects operational monotonicity. The caller must
    separately enforce the external construction hypothesis c*t>=a+2*b-1.
    """
    _positive_integer("c", c)
    _positive_integer("t", t)
    return (
        c**3 * profile_cube_numerator(a, b + t)
        - (c + 2) ** 3 * profile_cube_numerator(a, b)
    )


def homogeneous_dimensions(
    a: int, b: int, c: int, t: int, full_count: int, middle_count: int
) -> dict[str, object]:
    """Return literal long-leg dimensions for the homogeneous packing."""
    for name, value in (("a", a), ("b", b), ("c", c), ("t", t)):
        _positive_integer(name, value)
    _nonnegative_integer("full_count", full_count)
    _nonnegative_integer("middle_count", middle_count)
    if full_count + middle_count == 0:
        raise ValueError("at least one target block is required")
    s = a + b - 1
    source = (c * (b + t), c * (s + t))
    target = (full_count * b + middle_count * s,
              full_count * s + middle_count * b)
    deficits = tuple(left - right for left, right in zip(source, target))
    return {
        "source_long_legs": source,
        "target_long_legs": target,
        "dimension_deficits": deficits,
        "dimension_compatible": all(value >= 0 for value in deficits),
    }


def homogeneous_margin_numerator(
    a: int, b: int, c: int, t: int, full_count: int, middle_count: int
) -> int:
    homogeneous_dimensions(a, b, c, t, full_count, middle_count)
    target_count = full_count + middle_count
    return (
        c**3 * profile_cube_numerator(a, b + t)
        - target_count**3 * profile_cube_numerator(a, b)
    )


def _poly_add(*polynomials: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    result: dict[tuple[int, int], int] = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def _poly_multiply(
    first: dict[tuple[int, int], int], second: dict[tuple[int, int], int]
) -> dict[tuple[int, int], int]:
    result: dict[tuple[int, int], int] = {}
    for (i, j), coefficient in first.items():
        for (k, ell), other in second.items():
            exponent = (i + k, j + ell)
            result[exponent] = result.get(exponent, 0) + coefficient * other
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient}


def derivative_identity_residual() -> dict[tuple[int, int], int]:
    """Expand the numerator of the derivative identity as a polynomial."""
    three_b_minus_one = {(0, 1): 3, (0, 0): -1}
    two_a_b_minus_one = {(1, 0): 2, (0, 1): 1, (0, 0): -1}
    a_two_b_minus_one = {(1, 0): 1, (0, 1): 2, (0, 0): -1}
    first = _poly_multiply(
        _poly_add(three_b_minus_one, two_a_b_minus_one),
        a_two_b_minus_one,
    )
    second = {key: -2 * value for key, value in
              _poly_multiply(three_b_minus_one, two_a_b_minus_one).items()}
    negative_square = {(2, 0): -2, (1, 1): 4, (0, 2): -2}
    return _poly_add(first, second, negative_square)


def inspect_pass_case(a: int, b: int, c: int, t: int) -> dict[str, object]:
    margin = pass_margin_numerator(a, b, c, t)
    dimensions = homogeneous_dimensions(a, b, c, t, c + 1, 1)
    admissible = c * t >= a + 2 * b - 1
    equality_expected = admissible and b >= a and c * t == a + 2 * b - 1
    if admissible and margin < 0:
        raise AssertionError("admissible Pass parameters violate the barrier")
    if admissible and (margin == 0) != equality_expected:
        raise AssertionError("the exact equality characterization failed")
    if bool(dimensions["dimension_compatible"]) != admissible:
        raise AssertionError("Pass's cost condition differs from the two flattenings")
    return {
        "parameters": {"a": a, "b": b, "c": c, "t": t},
        "external_cost_condition": admissible,
        "scaled_cubed_margin": margin,
        "margin_scale": 16,
        "barrier_preserved": margin >= 0,
        "equality": margin == 0,
        **dimensions,
    }


def run_controls() -> dict[str, object]:
    if derivative_identity_residual():
        raise AssertionError("the derivative polynomial identity failed")

    ratio_count = 0
    ratio_equalities = 0
    for a in range(1, 25):
        for b in range(1, 25):
            for t in range(1, 25):
                margin = ratio_margin_numerator(a, b, t)
                if margin < 0 or (margin == 0) != (b >= a):
                    raise AssertionError(("ratio", a, b, t, margin))
                ratio_count += 1
                ratio_equalities += margin == 0

    pass_count = 0
    pass_equalities = 0
    for a in range(1, 25):
        for b in range(1, 25):
            for c in range(1, 25):
                minimum_t = (a + 2 * b - 2 + c) // c
                for t in (minimum_t, minimum_t + 1):
                    case = inspect_pass_case(a, b, c, t)
                    if not case["external_cost_condition"]:
                        raise AssertionError("incorrect rounding of the minimum cost")
                    pass_count += 1
                    pass_equalities += bool(case["equality"])

    homogeneous_count = 0
    compatible_count = 0
    for a in range(1, 6):
        for b in range(1, 6):
            for c in range(1, 6):
                for t in range(1, 6):
                    for full in range(6):
                        for middle in range(6):
                            if full + middle == 0:
                                continue
                            dimensions = homogeneous_dimensions(a, b, c, t, full, middle)
                            margin = homogeneous_margin_numerator(a, b, c, t, full, middle)
                            if dimensions["dimension_compatible"]:
                                compatible_count += 1
                                if margin < 0:
                                    raise AssertionError(("homogeneous", a, b, c, t, full, middle))
                            homogeneous_count += 1

    controls = [inspect_pass_case(*parameters) for parameters in
                ((1, 1, 2, 1), (2, 2, 5, 1), (2, 3, 7, 1),
                 (3, 1, 4, 1), (5, 2, 8, 1), (5, 2, 4, 2),
                 (2, 2, 4, 1), (9, 11, 3, 11))]
    return {
        "schema_version": 1,
        "arithmetic": "Python integers and fractions.Fraction; no floating decisions",
        "claim_scope": "finite controls for a written, unreviewed proof; no tensor witness or exponent improvement",
        "derivative_polynomial_identity": "zero residual",
        "ratio_grid": {"a": [1, 24], "b": [1, 24], "t": [1, 24],
                       "count": ratio_count, "equalities": ratio_equalities},
        "pass_boundary_grid": {"a": [1, 24], "b": [1, 24], "c": [1, 24],
                               "t": "ceil((a+2*b-1)/c) and the following integer",
                               "count": pass_count, "equalities": pass_equalities},
        "homogeneous_grid": {"a_b_c_t": [1, 5], "full_middle_counts": [0, 5],
                             "empty_target_excluded": True, "count": homogeneous_count,
                             "dimension_compatible": compatible_count},
        "named_controls": controls,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run_controls()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()

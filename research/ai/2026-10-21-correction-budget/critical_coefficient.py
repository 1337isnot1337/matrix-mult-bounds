"""Exact controls for the conditional critical-power correction allowance."""
import argparse
from fractions import Fraction as F
from math import isqrt
import json
from pathlib import Path


def encode(value):
    return [value.numerator, value.denominator]


def margin_fourth_power(b, h, rho, sigma, cost):
    """For square b, compare positive fourth powers without approximations."""
    root = isqrt(b)
    if root * root != b:
        raise ValueError("This finite control accepts perfect-square source widths.")
    if min(b, h, rho, sigma) <= 0 or cost < 0:
        raise ValueError("Positive dimensions and nonnegative auxiliary cost required.")
    return (rho * sigma * h) ** 3 - (cost + F(4, 3) * root) ** 4


def verify():
    rows = []
    for b, h, rho, sigma, cost, expected in [
        (4, 4, F(1), F(1), F(4, 25), 1),
        (4, 4, F(1), F(1), F(1, 5), -1),
        (16, 16, F(1), F(1), F(5, 2), 1),
        (16, 16, F(1), F(1), F(8, 3), 0),
        (81, 81, F(1), F(1), F(14), 1),
        (4, 4, F(99, 100), F(99, 100), F(1, 10), 1),
    ]:
        gap = margin_fourth_power(b, h, rho, sigma, cost)
        sign = (gap > 0) - (gap < 0)
        assert sign == expected
        root = isqrt(b)
        assert (F(4, 3) * root) ** 3 == F(64, 27) * b * root
        assert (F(4, 3) * root) ** 2 == F(16 * b, 9)
        rows.append({"source_width": b, "target_middle_width": h,
                     "outer_ratios": [encode(rho), encode(sigma)],
                     "auxiliary_coefficient": encode(cost),
                     "exact_fourth_power_margin": encode(gap),
                     "strict_sufficient_budget": sign == 1,
                     "equality_is_not_accepted": sign == 0})
    lower = F(1414213562373095, 10**15)
    upper = F(1414213562373096, 10**15)
    assert lower * lower < 2 < upper * upper
    lower_cost, upper_cost = 2 * lower - F(8, 3), 2 * upper - F(8, 3)
    assert F(4, 25) < lower_cost < upper_cost < F(1, 5)
    squared_margin = F(8) - (F(8, 3) + F(4, 25)) ** 2
    assert squared_margin == F(56, 5625)
    return {
        "status": "conditional implication only",
        "auxiliary_growth_power": [3, 2],
        "strict_coefficient_threshold": "(rho*sigma*h)^(3/4) - (4/3)*sqrt(b)",
        "width_four_squared_margin": encode(squared_margin),
        "width_four_threshold_rational_bracket": [encode(lower_cost), encode(upper_cost)],
        "exact_examples_and_negative_controls": rows,
        "source_constant_cube_identity_checked": True,
        "endpoint_compactness_consequence": "qualitative omega < 9/4 if the entire construction premise is proved",
        "required_unbounded_maps_constructed": False,
        "explicit_smaller_exponent_proved": False,
        "improves_omega": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))

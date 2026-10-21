"""Exact arithmetic certificate for the full-matrix quotient score ceiling."""

import argparse
import json
from math import isqrt
from pathlib import Path


SCALE = 10**6


def fourth_root_bounds(radicand):
    if radicand < 0:
        raise ValueError("the radicand must be nonnegative")
    lower = isqrt(isqrt(radicand))
    upper = lower if lower**4 == radicand else lower + 1
    assert lower**4 <= radicand <= upper**4
    assert upper - lower in (0, 1)
    return lower, upper


def report():
    numerator, denominator = 553, 1000
    root_left = numerator**5 * (denominator + 2*numerator)**4
    root_right = denominator**9
    maximum_left = numerator**5 * (denominator + numerator)**13
    maximum_right = 16 * denominator**18
    assert root_left > root_right
    assert maximum_left < maximum_right
    large_left = 200**4 * 36**9
    large_right = (93*19**3)**4
    assert large_left < large_right
    small = []
    for a, b in ((2, 2), (2, 3), (2, 4), (3, 3)):
        x = a + b - 1
        source = a*b*x
        m = isqrt(source)
        r = a*b - m
        _, upper = fourth_root_bounds(SCALE**4 * (6*m)**9)
        lower, _ = fourth_root_bounds(SCALE**4 * (6*r)**9)
        threshold = (3*x + 1)**3
        assert 100*(upper-lower) < 93*SCALE*threshold
        small.append({
            "a": a, "b": b, "long_dimension": x,
            "source_leg_dimension": source, "largest_quotient_dimension": m,
            "residual_matrix_size": r, "score_scale": SCALE,
            "positive_term_upper": upper, "negative_term_lower": lower,
            "critical_threshold": threshold,
            "strict_below_93_over_100": True,
        })
    return {
        "claim": "Every injective physical quotient with full matrix correction has finite 9/4 score below 93/100 of the source threshold",
        "exponent": [9, 4], "relative_score_ceiling": [93, 100],
        "maximum_control": {
            "rational_upper": [numerator, denominator],
            "critical_root_left": root_left, "critical_root_right": root_right,
            "maximum_fourth_power_left": maximum_left,
            "maximum_fourth_power_right": maximum_right,
        },
        "large_long_dimension_control": {
            "minimum_long_dimension": 6,
            "cleared_left": large_left, "cleared_right": large_right,
        },
        "small_source_controls": small,
        "quotient_existence_claimed": False,
        "joint_inequality_method_excluded": False,
        "new_exponent_established": False,
        "independent_mathematical_review": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[3]/"results/anisotropic-constructions-2026-10-20/quotient-score-barrier.json")
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))

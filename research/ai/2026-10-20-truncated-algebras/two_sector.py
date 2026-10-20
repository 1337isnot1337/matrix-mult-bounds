"""Exact two-sector restrictions and a critical-shape amplitude certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "2026-10-20-affine-direct-sums"))
from verify_filtration import h, profile


def coefficient_certificate(a, b):
    if any(not isinstance(n, int) or n < 1 for n in (a, b)):
        raise ValueError("positive integer lengths required")
    r = a + 2 * b - 1
    retained = [set(), set()]
    discarded = 0
    for i in range(a):
        for j in range(r):
            k = r - 1 - i - j
            if not 0 <= k < r:
                continue
            weight = (-1 if j < b else 0) + (0 if k < b else 1)
            if weight < 0:
                raise ArithmeticError("negative supported weight")
            if weight > 0:
                discarded += 1
            elif j < b <= k:
                retained[0].add((i, j, r - 1 - k))
            elif k < b <= j:
                retained[1].add((i, k, r - 1 - j))
            else:
                raise ArithmeticError("unmatched zero-weight block")
    expected = {(i, j, i + j) for i in range(a) for j in range(b)}
    if retained != [expected, expected]:
        raise ArithmeticError("incorrect convolution coefficient support")
    return {"a": a, "b": b, "source_border_rank": r,
            "shared_first_indices": [0, a - 1],
            "y_left_weights": -1, "y_right_weights": 0,
            "z_left_weights": 0, "z_right_weights": 1,
            "cut_index": b, "retained_terms": [len(v) for v in retained],
            "discarded_positive_terms": discarded}


def run(n=128):
    best = Fraction()
    best_pair = None
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            ratio_cubed = (2 * profile(a, b))**3 / (a + 2 * b - 1)**4
            if ratio_cubed > 1:
                raise ArithmeticError("matching-profile violation", a, b, ratio_cubed)
            if ratio_cubed > best:
                best, best_pair = ratio_cubed, [a, b]
    certificates = [coefficient_certificate(a, b)
                    for a in range(1, 13) for b in range(1, 13)]
    return {"profile_grid": n, "exact_profile_comparisons": n * n,
            "profile_violations": 0, "best_ratio_cubed": str(best),
            "best_pair": best_pair,
            "coefficient_cases": len(certificates),
            "total_retained_terms": sum(sum(c["retained_terms"]) for c in certificates),
            "amplitude_upper_cubed": "16/9",
            "amplitude_lower_cubed_at_grid_endpoint": str(h(n)**3 / n),
            "optimal_aspect_ratio_a_over_b": 4,
            "polynomial_identity": "9(a+2)^4-16(2a+1)^3=(a-4)^2(9a^2+16a+8)",
            "scope": "Exact finite controls for the separate written all-size two-sector theorem; no smaller exponent."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-size", type=int, default=128)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.max_size)
    content = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
    print(content, end="")

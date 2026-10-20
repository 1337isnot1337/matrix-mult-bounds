"""Exact rank covers for constant matrices followed by mixed weights.

These are construction-class obstructions, not exponent improvements.
See intermediate_weights.md for the all-size argument and its hypotheses.
"""
import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path


def nodes(m):
    return [(a, b) for a in range(m) for b in range(m-a)]


def cover(m, alpha, beta, threshold):
    if m < 2 or alpha <= 0:
        raise ValueError("Require m>=2 and alpha>0")
    threshold = Fraction(threshold)
    total = alpha*(m-1)
    points = nodes(m)
    rows = {(a, b) for a, b in points
            if (alpha-beta)*a+alpha*b > threshold}
    cols = {(a, b) for a, b in points
            if (alpha-beta)*a+alpha*b > total-threshold}
    boundary = threshold/alpha
    if boundary.denominator == 1 and 0 <= boundary <= m-1:
        rows.add((0, int(boundary)))
    return rows, cols


def best_cover(m, alpha, beta):
    if m < 2 or alpha <= 0:
        raise ValueError("Require m>=2 and alpha>0")
    weights = sorted((alpha-beta)*a+alpha*b for a, b in nodes(m))
    total = alpha*(m-1)
    # Outside this interval one whole side is needed when alpha>=beta>0.
    # The reported cases use that region. For other beta values, include
    # every weight/reflected weight, so both constant tails are represented.
    breaks = sorted({0, total, *weights, *(total-w for w in weights)})
    thresholds = [Fraction(t) for t in breaks]
    thresholds += [Fraction(a+b, 2) for a, b in zip(breaks, breaks[1:])]
    n = len(weights)
    def size(t):
        boundary = t/alpha
        extra = int(boundary.denominator == 1 and 0 <= boundary <= m-1)
        return 2*n-bisect_right(weights, t)-bisect_right(weights, total-t)+extra
    value, threshold = min((size(t), t) for t in thresholds)
    return {"rank_upper_per_copy": value, "threshold": str(threshold)}


def report():
    records = []
    directions = [(1, 1), (3, 2), (7, 4), (19, 10), (39, 20),
                  (2, 1), (21, 10), (5, 2), (3, 1)]
    for m in (4, 8, 16, 32, 64):
        n = m*(m+1)//2
        for alpha, beta in directions:
            result = best_cover(m, alpha, beta)
            records.append({"m": m, "N": n, "alpha": alpha, "beta": beta,
                            **result,
                            "B_lower_k1": 2*n-result["rank_upper_per_copy"]-(m-1)})
    return {"status": "exact finite covers supporting an unreviewed written proof",
            "new_exponent_established": False,
            "records": records,
            "four_block_replicated_case": {"m": 4, "k": 53, "alpha": 2,
                 "beta": 1, "proposed_B": 530, "necessary_B": 633,
                 "excluded_within_stated_ansatz": True}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+"\n")
    print("Recorded 45 exact covers; no exponent improvement claimed.")

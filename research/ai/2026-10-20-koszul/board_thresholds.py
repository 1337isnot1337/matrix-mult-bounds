"""Exact arithmetic correction to the board's finite exact-rank search window.

External premise: Massarenti-Raviolo, arXiv:1211.6320v2, Remark 3.3,
R(M_n) >= 8 n^2/3 - 7 n over C. This script does not prove that theorem.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path


def strict_rank_ceiling(n):
    if n < 2:
        raise ValueError("n must be at least two")
    low, high = 0, n ** 3
    while low + 1 < high:
        mid = (low + high) // 2
        if mid ** 4 < n ** 9:
            low = mid
        else:
            high = mid
    return low


def exact_rank_floor(n):
    bound = max(Fraction(5 * n * n, 2) - 3 * n,
                Fraction(8 * n * n, 3) - 7 * n)
    return -(-bound.numerator // bound.denominator)


def run():
    rows = [{"n": n, "lower_bound": exact_rank_floor(n),
             "largest_rank_strictly_beating_nine_fourths": strict_rank_ceiling(n),
             "excluded_by_these_bounds": exact_rank_floor(n) > strict_rank_ceiling(n)}
            for n in range(3, 41)]
    return {"status": "exact integer consequences of cited external exact-rank bounds",
            "applies_to_border_rank": False,
            "source": "https://arxiv.org/abs/1211.6320v2",
            "location": "Remark 3.3, pages 9-10; complex matrix multiplication",
            "coverage": "3 <= n <= 40; n=2 not part of this scan",
            "first_size_not_excluded_in_scan": next(r["n"] for r in rows
                                                     if not r["excluded_by_these_bounds"]),
            "rows": rows}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    report = run()
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "rows"}, indent=2))

"""Independent integer-matrix controls for the quantitative capacity bound."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def disjoint_pattern_rank(rows):
    patterns = sorted(set(rows)-{0})
    seen = 0
    for pattern in patterns:
        if seen & pattern:
            raise ArithmeticError("distinct nonzero row patterns overlap")
        seen |= pattern
    return len(patterns)


def projected_target_rank(m, ell, p0, q):
    if not (1 <= ell <= m and 0 <= p0 <= m-ell and 0 <= q < ell):
        raise ValueError("invalid projected target dimensions")
    h = ell-1-q
    total = 0
    for u in range(1, m+1):
        v = m+1-u
        rows = []
        for r in range(q+1):
            for a in range(u):
                pattern = 0
                for s in range(h+1):
                    c = p0+r+s-a
                    if 0 <= c < v:
                        pattern |= 1 << (s*v+c)
                rows.append(pattern)
        total += disjoint_pattern_rank(rows)
    return total


def projected_target_formula(m, ell, p0, q):
    h = ell-1-q
    return (ell+p0)*(m-p0)-(h*(h+1)+q*(q+1))//2


def source_rank(ell, B, q):
    h = ell-1-q
    width = B+ell-1
    rows = [sum(1 << (s*width+r+s+j) for s in range(h+1))
            for r in range(q+1) for j in range(B)]
    return disjoint_pattern_rank(rows)


def longest_constant_run(word):
    longest = current = 0
    previous = None
    for value in word:
        current = current+1 if value == previous else 1
        longest = max(longest, current)
        previous = value
    return longest


def run(max_m=12):
    target_cases = source_cases = 0
    for m in range(1, max_m+1):
        for ell in range(1, m+1):
            for p0 in range(m-ell+1):
                for q in range(ell):
                    actual = projected_target_rank(m, ell, p0, q)
                    formula = projected_target_formula(m, ell, p0, q)
                    if actual != formula:
                        raise ArithmeticError("projected target rank formula mismatch")
                    target_cases += 1
    for ell in range(1, max_m+1):
        for B in [1, 3, 10]:
            for q in range(ell):
                if source_rank(ell, B, q) != B+q:
                    raise ArithmeticError("source rank formula mismatch")
                source_cases += 1
    if not (675 < 676 and (9*15)**3 < 2*(7*16)**3 and 729*4 < 686*5):
        raise ArithmeticError("exact overhead separation failed")
    rational_polynomial = 16*Fraction(16, 15)**2-48*Fraction(16, 15)+33
    if rational_polynomial != Fraction(1, 225):
        raise ArithmeticError("incorrect algebraic lower bound comparison")
    return {"maximum_m": max_m, "explicit_target_matrix_cases": target_cases,
            "explicit_source_matrix_cases": source_cases,
            "asymptotic_overhead_lower": "3/2-sqrt(3)/4",
            "rational_overhead_lower_strict": "16/15",
            "required_overhead_upper_strict": "16/15",
            "maximum_relative_shared_source": "5/4",
            "scope": "Coordinate injections with arbitrary nonzero scalars, constant output matrix, diagonal target weights; arbitrary positive numbers of canonical target copies.",
            "new_matrix_exponent_established": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run(args.max_m)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))

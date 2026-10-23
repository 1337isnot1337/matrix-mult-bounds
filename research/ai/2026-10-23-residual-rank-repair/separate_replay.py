"""Separately implemented exact arithmetic for the October 23 paired residual gate.

This script imports no research acceptance helpers. It checks implications,
not tensor maps or an achieved matrix multiplication exponent.
This same-session check is not independent mathematical review.
"""

from fractions import Fraction as F
from math import isqrt
import json


def full_gate(n, b):
    return 81 * b * n**6 > 4 * (2*n + b - 1)**6


def source_size(n, b):
    return max(n*n, b*(n+b-1))


def root_interval(value, degree, bits=120):
    assert degree in (2, 4) and value >= 0
    scale = 1 << bits
    integer = value.numerator * scale**degree // value.denominator
    low = isqrt(integer) if degree == 2 else isqrt(isqrt(integer))
    lo, hi = F(low, scale), F(low+1, scale)
    assert lo**degree <= value < hi**degree
    return lo, hi


def gate_gap(n, b, d):
    target = root_interval(F((b*n*n)**3), 4)
    residual = root_interval(F(d**3), 4)
    source = root_interval(F(2*b*(2*n+b-1)**3, 9), 2)
    return target[0]-residual[1]-source[1], target[1]-residual[0]-source[0]


def residual_budget(n, b):
    assert gate_gap(n, b, 0)[0] > 0
    low, high = 0, b*n*n
    while high-low > 1:
        middle = (low+high)//2
        if gate_gap(n, b, middle)[0] > 0:
            low = middle
        else:
            high = middle
    accepted, rejected = gate_gap(n, b, low), gate_gap(n, b, high)
    assert accepted[0] > 0 and rejected[1] < 0
    return {
        "n": n, "b": b, "max_source_leg": source_size(n,b),
        "source_format": [n*n,b*(n+b-1),b*(n+b-1)],
        "target_format": [n*n,b*n,b*n],
        "largest_certified_integer_pair_product": low,
        "accepted_gap_interval": [str(x) for x in accepted],
        "next_integer_gap_interval": [str(x) for x in rejected],
    }


def main():
    # Any source size below 441 has n <= 20 and b <= 20 because the
    # source size is at least each of n^2 and b^2. This exhausts all
    # possible smaller sources, not just a heuristic parameter window.
    below = [(n,b) for n in range(1,21) for b in range(1,21)
             if source_size(n,b)<441 and full_gate(n,b)]
    assert below == []
    minimizers = [(n,b) for n in range(1,22) for b in range(1,22)
                  if source_size(n,b)<=441 and full_gate(n,b)]
    assert minimizers == [(21,8),(21,9)]
    # Audit the error-exponent factorization at an exact grid.
    algebra_count = 0
    for g in range(100):
        gamma = F(g,100)
        for k in range(51):
            x = F(k,100)
            delta = x*x
            total = F(9,4)-delta
            maximum = F(3,4)-delta+x
            gap = (1-gamma/2)*total-(2-gamma/2)*maximum
            factored = (x-(1-gamma)/2)*(x-F(3,2))
            assert gap == factored
            if x < (1-gamma)/2:
                assert gap > 0
            algebra_count += 1
    cases = [(21,8),(21,9),(22,7),(22,8),(22,9),(22,10),(22,11),
             (23,6),(24,8),(26,5),(38,4),(40,4),(64,4),(128,4),(256,4)]
    return {
        "scope": "Conditional actual-character gate; no source maps supplied",
        "minimum_max_source_leg": 441,
        "minimum_gate_targets": minimizers,
        "global_minimum_proof": "A smaller objective forces n,b <= 20; all 400 pairs checked",
        "equality_search_pairs": 441,
        "exact_quantitative_algebra_controls": algebra_count,
        "residual_budgets": [residual_budget(n,b) for n,b in cases],
        "improves_omega": False,
    }


if __name__ == "__main__":
    print(json.dumps(main(),indent=2))

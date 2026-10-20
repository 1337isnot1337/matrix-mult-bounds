"""Exact necessary screens and conditional constants for the fat-point route.

No degeneration from a convolution source is supplied by this program.
"""
from fractions import Fraction
import argparse
import json
from math import comb
from pathlib import Path


def target_rank(a, p):
    return sum(min(u*comb(a, p), (a+1-u)*comb(a, p+1))
               for u in range(1, a+1))


def rational_below_root(d, rho=Fraction(1)):
    """Decide rho*d*(d+1)*2**d < 8 by integer powers for positive rationals."""
    p, q = d.numerator, d.denominator
    left = (rho.numerator*p*(p+q))**q * 2**p
    right = (rho.denominator*q*q)**q * 2**(3*q)
    return left < right


def tensor(a):
    monomials = [(i, n-i) for n in range(a) for i in range(n+1)]
    index = {m: i for i, m in enumerate(monomials)}
    terms = [(i+k, index[i, j], index[k, l])
             for i, j in monomials for k, l in monomials
             if i+j+k+l == a-1]
    return [a, len(monomials), len(monomials)], terms


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-a', type=int, default=32)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    count = 0
    for a in range(1, args.max_a+1):
        n = a*(a+1)//2
        for p in range(a):
            if target_rank(a, p) != n*comb(a-1, p):
                raise ValueError(('target rank identity', a, p))
            count += 1
    lower = Fraction(168, 125)
    if not rational_below_root(lower):
        raise ValueError('conditional rational exponent certificate failed')
    if rational_below_root(Fraction(3, 2)):
        raise ValueError('root bracket negative control failed')
    critical_cube = Fraction(729, 686)
    if not critical_cube > 1:
        raise ValueError('critical cost threshold must exceed one')
    report = {
        'status': 'exact screens and conditional constants passed',
        'new_exponent_established': False,
        'construction_status': 'unconstructed from the required convolution source',
        'max_a': args.max_a, 'shared_leg_rank_identities_checked': count,
        'critical_cost_threshold_cube': str(critical_cube),
        'cost_one_root_lower_rational': str(lower),
        'cost_one_conditional_exponent_upper': str(3/lower),
        'scope': 'Finite checks of separately written all-degree formulas and '
                 'a conditional implication. Passing screens is not a degeneration.',
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()

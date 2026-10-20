"""Exact upper certificates for the optimistic full-filtration entropy score.

This bounds an explicitly defined analytic score. It does not silently assert
a weighted tensor extraction theorem or prove a matrix-multiplication bound.
Only the Python standard library is needed. See research_note.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json
from math import isqrt
from pathlib import Path


@lru_cache(None)
def h(n: int) -> Q:
    if n < 1:
        raise ValueError('positive length required')
    value = Q(1)
    for k in range(1, n):
        value *= Q(3*k+1, 3*k)
    return value


def profile(a: int, b: int) -> Q:
    m, n = sorted((a, b))
    return h(m)*Q(2*n+m-1, 2)


def sqrt_interval(value: Q, scale: int) -> tuple[Q, Q]:
    if value < 0 or scale < 1:
        raise ValueError('nonnegative radicand and positive scale required')
    root = isqrt(value.numerator*scale**2//value.denominator)
    lo = Q(root, scale)
    hi = lo if lo*lo == value else Q(root+1, scale)
    if not lo*lo <= value <= hi*hi:
        raise ArithmeticError('invalid root enclosure')
    return lo, hi


@lru_cache(None)
def weight_sum_upper(a: int, c: int, scale: int) -> Q:
    return sum((sqrt_interval(h(a+c-1-2*i)**3, scale)[1]
                for i in range(min(a, c))), Q(0))


def ratio_cube_upper(a: int, b: int, c: int, d: int,
                     scale: int = 10**12) -> Q:
    source = profile(a, b)*profile(c, d)
    A, B = a+c-1, b+d-1
    # A singleton marginal makes the entropy term exactly zero.
    if min(a, c) == 1 or min(b, d) == 1:
        return (profile(A, B)/source)**3
    R = profile(A, B)/(h(A)*h(B))
    HA = weight_sum_upper(a, c, scale)
    HB = weight_sum_upper(b, d, scale)
    return R**3*(HA*HB)**2/source**3


def verify_probability_certificate(values: list[list[Q]], u: list[Q],
                                   v: list[Q], bound: Q) -> bool:
    """Check the pointwise sufficient condition for every distribution q.

    Score(q) = exp(4/3 min_l H(q_l)) prod_ij values[i][j]**q_ij.
    Its output marginal can be any deterministic function of (i,j).
    """
    if (not u or not v or bound <= 0 or sum(u) != 1 or sum(v) != 1
            or any(x <= 0 for x in u+v) or len(values) != len(u)
            or any(len(row) != len(v) for row in values)):
        return False
    return all(value > 0 and value**3 <= bound**3*(u[i]*v[j])**2
               for i, row in enumerate(values) for j, value in enumerate(row))


def polynomial_add(a: list[int], b: list[int]) -> list[int]:
    result = [0]*max(len(a), len(b))
    for i, v in enumerate(a): result[i] += v
    for i, v in enumerate(b): result[i] += v
    return result


def polynomial_mul(a: list[int], b: list[int]) -> list[int]:
    result = [0]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b): result[i+j] += u*v
    return result


def polynomial_power(a: list[int], n: int) -> list[int]:
    result = [1]
    for _ in range(n): result = polynomial_mul(result, a)
    return result


def tail_polynomial(shift: int = 23) -> list[int]:
    """Ascending coefficients after n=x+shift; no symbolic package needed."""
    left = polynomial_mul([shift, 1], polynomial_power([3*shift-1, 3], 7))
    left = polynomial_mul(left, polynomial_power([2*shift-1, 2], 2))
    left = [12*39**3*v for v in left]
    right = polynomial_mul(polynomial_power([6*shift-4, 6], 4),
                           polynomial_power([2*shift+1, 2], 6))
    return polynomial_add(left, [-40**3*v for v in right])


def balanced_certificate(scale: int) -> dict:
    target = Q(39, 40)**3
    small = []
    for n in range(2, 23):
        bound = ratio_cube_upper(n, n, n, n, scale)
        if bound >= target:
            raise ArithmeticError(f'small-size certificate failed at {n}')
        lengths = [2*n-1-2*i for i in range(n)]
        weights = [sqrt_interval(h(k)**3, scale)[0] for k in lengths]
        u = [w/sum(weights) for w in weights]
        values = [[profile(a,b) for b in lengths] for a in lengths]
        if not verify_probability_certificate(values, u, u,
                                               Q(39,40)*profile(n,n)**2):
            raise ArithmeticError(f'independent probability certificate failed at {n}')
        small.append({'n': n, 'ratio_cube_upper': str(bound),
                      'marginal_probabilities': [str(x) for x in u],
                      'pointwise_inequalities_verified': n*n})
    coefficients = tail_polynomial()
    if len(coefficients) != 11 or not all(v > 0 for v in coefficients):
        raise ArithmeticError('tail polynomial has a nonpositive coefficient')
    return {'statement': 'For every integer n>=2 and every distribution q on '
                         'i+j=k, optimistic_score(q) <= (39/40)*P_*(n,n)^2.',
            'status': 'written-proof-unreviewed; exact finite and polynomial certificates',
            'small_sizes': small, 'tail_start': 23,
            'tail_polynomial_coefficients_ascending': coefficients,
            'source_profile_ratio_bound': '39/40',
            'improves_omega': False}


def report(max_size: int = 12, scale: int = 10**12) -> dict:
    balanced = balanced_certificate(scale)
    worst = (Q(-1), None)
    nontrivial = (Q(-1), None)
    count = singleton = 0
    failures = []
    for a, b, c, d in product(range(1, max_size+1), repeat=4):
        value = ratio_cube_upper(a, b, c, d, scale)
        count += 1
        if min(a, c) == 1 or min(b, d) == 1: singleton += 1
        if value > worst[0]: worst = value, [a, b, c, d]
        if min(a,b,c,d) > 1 and value > nontrivial[0]:
            nontrivial = value, [a, b, c, d]
        if value > 1:
            failures.append({'source': [a,b,c,d], 'ratio_cube_upper': str(value)})
    return {'max_size': max_size, 'scale': scale,
            'source_quadruples': count, 'singleton_marginal_cases': singleton,
            'exact_upper_certificates_passed': count-len(failures),
            'failed_upper_certificates': failures,
            'worst': {'source': worst[1], 'ratio_cube_upper': str(worst[0])},
            'worst_nontrivial': {'source': nontrivial[1],
                                'ratio_cube_upper': str(nontrivial[0])},
            'balanced_all_size_certificate': balanced,
            'scope': 'Each passed source certificate bounds every probability '
                     'distribution, using the analytic dual proof. The source '
                     'grid is finite; the balanced theorem is all-size. No '
                     'weighted block-extraction theorem or smaller omega is asserted.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-size', type=int, default=12)
    parser.add_argument('--scale', type=int, default=10**12)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.max_size < 1 or args.scale < 1: parser.error('positive parameters required')
    result = report(args.max_size, args.scale)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()
                      if k != 'balanced_all_size_certificate'}, indent=2))
    if result['failed_upper_certificates']:
        raise SystemExit('Some upper certificates failed; this is not a profile violation.')


if __name__ == '__main__': main()

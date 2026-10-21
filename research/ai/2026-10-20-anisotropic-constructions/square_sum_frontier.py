"""Exact square-direct-sum screen, conditional on the written slice lemmas.

All acceptance comparisons use integer fourth-root enclosures and an exact
integer knapsack. This is an ordinary-restriction screen only. No target
restriction, singular exclusion or smaller exponent is established.
"""

from __future__ import annotations

import argparse
import json
from math import isqrt
from pathlib import Path

SCALE = 10**6


def score_interval(n, scale=SCALE):
    radicand = (6*n)**9 * scale**4
    lower = isqrt(isqrt(radicand))
    assert lower**4 <= radicand < (lower+1)**4
    upper = lower if lower**4 == radicand else lower+1
    return lower, upper


def allowed_blocks(a, b, dimension):
    size = a*b*(a+b-1)
    loss = size-dimension
    if not 1 <= dimension <= size:
        raise ValueError('Target leg dimension is outside the source format.')
    nontrivial = []
    for n in range(2, isqrt(dimension)+1):
        if n+2*loss < 2*a*b:
            continue
        nontrivial.append(n)
    scalar_allowed = 1+2*loss >= a*b
    repeated_scalars_allowed = 2+2*loss >= 2*a*b
    return nontrivial, scalar_allowed, repeated_scalars_allowed


def dimension_frontier(a, b, dimension, scale=SCALE):
    nontrivial, scalar, repeated = allowed_blocks(a, b, dimension)
    values = {n: score_interval(n, scale)[1] for n in [1]+nontrivial}
    unlimited = nontrivial+([1] if scalar and repeated else [])
    scores = [-1]*(dimension+1)
    witness = [None]*(dimension+1)
    scores[0] = 0
    witness[0] = []
    for used in range(1, dimension+1):
        for n in unlimited:
            earlier = used-n*n
            if earlier < 0 or scores[earlier] < 0:
                continue
            candidate = scores[earlier]+values[n]
            if candidate > scores[used]:
                scores[used] = candidate
                witness[used] = witness[earlier]+[n]
    value, shape = scores[dimension], witness[dimension]
    if scalar and not repeated and scores[dimension-1] >= 0:
        candidate = scores[dimension-1]+values[1]
        if candidate > value:
            value, shape = candidate, witness[dimension-1]+[1]
    if shape is not None:
        assert sum(n*n for n in shape) == dimension
        assert sum(values[n] for n in shape) == value
    return {'target_leg_dimension': dimension,
            'upper_score_numerator': value if value >= 0 else None,
            'upper_score_denominator': scale,
            'maximizing_relaxed_partition': shape,
            'allowed_nonscalar_sizes': nontrivial,
            'scalars_allowed': scalar, 'repeated_scalars_allowed': repeated}


def source_frontier(a, b, scale=SCALE, retain_dimensions=False):
    size = a*b*(a+b-1)
    rows = [dimension_frontier(a, b, d, scale) for d in range(1, size+1)]
    best = max((r for r in rows if r['upper_score_numerator'] is not None),
               key=lambda r: r['upper_score_numerator'])
    limit = (3*(a+b)-2)**3
    result = {'a': a, 'b': b, 'source_leg_dimension': size,
              'dimensions_screened': size, 'critical_score_threshold': limit,
              'maximum': best,
              'all_partitions_below_critical_score': best['upper_score_numerator'] < limit*scale}
    if retain_dimensions:
        result['dimension_frontier'] = rows
    return result


def admissible_partition(a, b, shape):
    d = sum(n*n for n in shape)
    allowed, scalar, repeated = allowed_blocks(a, b, d)
    return (all(n in allowed for n in shape if n > 1)
            and (not shape.count(1) or scalar)
            and (shape.count(1) <= 1 or repeated))


def report(maximum_source_dimension=300):
    sources = []
    a = 2
    while a*a*(2*a-1) <= maximum_source_dimension:
        b = a
        while a*b*(a+b-1) <= maximum_source_dimension:
            sources.append(source_frontier(a, b, retain_dimensions=(a == b == 5)))
            b += 1
        a += 1
    sources.sort(key=lambda r: (r['source_leg_dimension'], r['a'], r['b']))
    passing = [r for r in sources if not r['all_partitions_below_critical_score']]
    target = {'source': [5, 6], 'blocks': [16, 4], 'target_leg_dimension': 272,
              'ordinary_screen_passes': admissible_partition(5, 6, [16, 4]),
              'conditional_exponent': ['281', '125'],
              'integer_power_checks': [96**281 > 28585**125, 24**281 > 1266**125],
              'integer_lower_sum': 28585+1266, 'source_threshold': 31**3,
              'target_constructed': False, 'new_exponent_established': False}
    assert all(target['integer_power_checks'])
    assert target['integer_lower_sum'] > target['source_threshold']
    assert target['ordinary_screen_passes']
    if maximum_source_dimension >= 300:
        assert passing[0]['source_leg_dimension'] == 300
        assert (passing[0]['a'], passing[0]['b']) == (5, 6)
    return {'scope': 'ordinary restrictions to square matrix direct sums only; sufficient exclusion tests, not existence tests',
            'maximum_source_dimension': maximum_source_dimension,
            'source_count': len(sources), 'source_frontiers': sources,
            'first_passing_source_dimension': passing[0]['source_leg_dimension'] if passing else None,
            'conditional_surviving_target': target,
            'score': 'sum_j (6*n_j)^(9/4)', 'interval_denominator': SCALE,
            'new_exponent_established': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--maximum-source-dimension', type=int, default=300)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = json.dumps(report(args.maximum_source_dimension), indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
    else:
        print(data, end='')


if __name__ == '__main__':
    main()

"""Exact finite square-sum screen using the written higher-Hankel lemma.

Adapted from anisotropic-constructions/square_sum_frontier.py at
e44aaff22af7863e0a1f5db66d187ae997c82184 in the research repository.
This is a necessary-condition screen for ordinary restrictions. It does
not construct targets or establish any improvement of the exponent.
All score comparisons use integer fourth-root enclosures.
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
    return lower, lower if lower**4 == radicand else lower+1


def allowed_ranks(a, b):
    return range(1, min(min(a, b)-1, (a+b-1)//3)+1)


def block_exclusions(a, b, dimension, n):
    """Return every applicable higher-Hankel obstruction to a block."""
    ab = a*b
    loss = ab*(a+b-1)-dimension
    return [r for r in allowed_ranks(a, b)
            if n*n > r*ab and n+2*loss < (r+1)*ab]


def allowed_blocks(a, b, dimension):
    size = a*b*(a+b-1)
    loss = size-dimension
    if not 1 <= dimension <= size:
        raise ValueError('Target leg dimension is outside the source format.')
    nontrivial = [n for n in range(2, isqrt(dimension)+1)
                  if n+2*loss >= 2*a*b
                  and not block_exclusions(a, b, dimension, n)]
    scalar_allowed = 1+2*loss >= a*b
    repeated_scalars_allowed = 2+2*loss >= 2*a*b
    return nontrivial, scalar_allowed, repeated_scalars_allowed


def dimension_frontier(a, b, dimension, intervals):
    nontrivial, scalar, repeated = allowed_blocks(a, b, dimension)
    unlimited = nontrivial+([1] if scalar and repeated else [])
    scores = [-1]*(dimension+1)
    previous = [None]*(dimension+1)
    scores[0] = 0
    for used in range(1, dimension+1):
        for n in unlimited:
            earlier = used-n*n
            if earlier < 0 or scores[earlier] < 0:
                continue
            candidate = scores[earlier]+intervals[n][1]
            if candidate > scores[used]:
                scores[used] = candidate
                previous[used] = n
    value = scores[dimension]
    final_scalar = False
    if scalar and not repeated and scores[dimension-1] >= 0:
        candidate = scores[dimension-1]+intervals[1][1]
        if candidate > value:
            value = candidate
            final_scalar = True
    if value < 0:
        return None
    remaining = dimension-int(final_scalar)
    shape = [1] if final_scalar else []
    while remaining:
        n = previous[remaining]
        assert n is not None
        shape.append(n)
        remaining -= n*n
    shape.sort(reverse=True)
    assert sum(n*n for n in shape) == dimension
    assert sum(intervals[n][1] for n in shape) == value
    return {'target_leg_dimension': dimension,
            'upper_score_numerator': value,
            'witness_lower_score_numerator': sum(intervals[n][0] for n in shape),
            'maximizing_relaxed_partition': shape}


def source_frontier(a, b, scale=SCALE):
    size = a*b*(a+b-1)
    intervals = {n: score_interval(n, scale) for n in range(1, isqrt(size)+1)}
    best = None
    admissible_dimensions = 0
    for dimension in range(1, size+1):
        row = dimension_frontier(a, b, dimension, intervals)
        if row is not None:
            admissible_dimensions += 1
            if best is None or row['upper_score_numerator'] > best['upper_score_numerator']:
                best = row
    assert best is not None
    threshold = (3*(a+b)-2)**3
    return {'a': a, 'b': b, 'source_leg_dimension': size,
            'higher_hankel_ranks': list(allowed_ranks(a, b)),
            'dimensions_screened': size, 'admissible_dimensions': admissible_dimensions,
            'critical_score_threshold': threshold, 'maximum': best,
            'all_partitions_below_critical_score': best['upper_score_numerator'] < threshold*scale,
            'witness_score_strictly_above_critical': best['witness_lower_score_numerator'] > threshold*scale}


def target_check(a, b, shape):
    dimension = sum(n*n for n in shape)
    allowed, scalar, repeated = allowed_blocks(a, b, dimension)
    obstructions = [{'n': n, 'ranks': block_exclusions(a, b, dimension, n)}
                    for n in shape if block_exclusions(a, b, dimension, n)]
    passes = (all(n in allowed for n in shape if n > 1)
              and (not shape.count(1) or scalar)
              and (shape.count(1) <= 1 or repeated))
    return {'source': [a, b], 'blocks': shape, 'target_leg_dimension': dimension,
            'ordinary_screen_passes': passes, 'higher_hankel_obstructions': obstructions,
            'target_constructed': False}


def report(maximum_source_dimension=600, progress=False):
    sources = []
    a = 2
    while a*a*(2*a-1) <= maximum_source_dimension:
        b = a
        while a*b*(a+b-1) <= maximum_source_dimension:
            row = source_frontier(a, b)
            sources.append(row)
            if progress:
                print(f"A({a},{b}): N={row['source_leg_dimension']}, "
                      f"shape={row['maximum']['maximizing_relaxed_partition']}, "
                      f"excluded={row['all_partitions_below_critical_score']}", flush=True)
            b += 1
        a += 1
    sources.sort(key=lambda r: (r['source_leg_dimension'], r['a'], r['b']))
    passing = [r for r in sources if not r['all_partitions_below_critical_score']]
    known = [target_check(5, 6, [16, 4]), target_check(5, 6, [16])]
    assert all(not t['ordinary_screen_passes'] for t in known)
    if maximum_source_dimension >= 300:
        assert all(s['all_partitions_below_critical_score']
                   for s in sources if s['source_leg_dimension'] <= 300)
    return {'scope': 'ordinary restrictions only; necessary conditions do not imply existence',
            'status': 'conditional on the written geometric lemma and inherited source slice bound',
            'maximum_source_dimension': maximum_source_dimension,
            'source_count': len(sources), 'source_frontiers': sources,
            'first_passing_source_dimension': passing[0]['source_leg_dimension'] if passing else None,
            'passing_sources': [{'a': s['a'], 'b': s['b'],
                                 'source_leg_dimension': s['source_leg_dimension'],
                                 'blocks': s['maximum']['maximizing_relaxed_partition'],
                                 'strict_score_pass': s['witness_score_strictly_above_critical']}
                                for s in passing],
            'selected_target_checks': known,
            'score': 'sum_j (6*n_j)^(9/4)', 'interval_denominator': SCALE,
            'new_exponent_established': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--maximum-source-dimension', type=int, default=600)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--progress', action='store_true')
    args = parser.parse_args()
    result = report(args.maximum_source_dimension, args.progress)
    data = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
        print(json.dumps({k: result[k] for k in ('source_count',
                         'first_passing_source_dimension', 'passing_sources',
                         'selected_target_checks', 'new_exponent_established')}, indent=2))
    else:
        print(data, end='')


if __name__ == '__main__':
    main()

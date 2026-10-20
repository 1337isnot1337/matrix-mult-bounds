"""Exact unit-coefficient monomial controls for the broader Laurent theorem.

This witness format uses one Laurent monomial per nonzero output entry.
The written theorem allows arbitrary Laurent entries and input scalars.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def verify(witness):
    m, B = witness['m'], witness['B']
    A = witness.get('source_A', m)
    if any(not isinstance(v, int) or v < 1 for v in (m, A, B)):
        raise ArithmeticError('invalid source dimensions')
    points = [(a, d-a) for d in range(m) for a in range(d+1)]
    n = len(points)
    xp, yp = witness['source_x_indices'], witness['source_y_indices']
    wx, wy = witness['input_weights']['x'], witness['input_weights']['y']
    rows = witness['output_rows']
    if [len(xp), len(yp), len(wx), len(wy), len(rows)] != [m, n, m, n, n]:
        raise ArithmeticError('incorrect map dimensions')
    if any(not isinstance(v, int) for vector in (xp, yp, wx, wy) for v in vector):
        raise ArithmeticError('integer input indices and valuations required')
    if (len(set(xp)) != m or len(set(yp)) != n or
            any(not 0 <= p < A for p in xp) or any(not 0 <= j < B for j in yp)):
        raise ArithmeticError('invalid input injections')
    maps = []
    for row in rows:
        mapping = dict(row)
        if len(mapping) != len(row):
            raise ArithmeticError('duplicate output source coordinate')
        if any(not isinstance(k, int) or not 0 <= k < A+B-1 or not isinstance(value, int)
               for k, value in row):
            raise ArithmeticError('invalid output Laurent monomial')
        maps.append(mapping)
    count = retained = positive = 0
    active_sets = [set() for _ in rows]
    for p in range(m):
        for y, (a, b) in enumerate(points):
            k = xp[p]+yp[y]
            for z, (c, d) in enumerate(points):
                expected = p == a+c and a+b+c+d == m-1
                if k not in maps[z]:
                    if expected:
                        raise ArithmeticError('missing desired coefficient')
                else:
                    valuation = wx[p]+wy[y]+maps[z][k]
                    if valuation < 0:
                        raise ArithmeticError('negative supported coefficient')
                    if valuation == 0 and not expected:
                        raise ArithmeticError('undesired leading coefficient')
                    if expected and valuation != 0:
                        raise ArithmeticError('wrong desired valuation')
                    retained += valuation == 0
                    positive += valuation > 0
                    if expected:
                        active_sets[z].add(k)
                count += 1
    if sum(map(len, active_sets)) != len(set.union(*active_sets)):
        raise ArithmeticError('active sets for different outputs overlap')
    return {'coefficients_checked': count, 'retained_terms': retained,
            'discarded_positive_terms': positive,
            'active_output_excess': sum(len(row)-1 for row in active_sets),
            'independent_coefficient_verification': True}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('witness', type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(json.loads(args.witness.read_text())), indent=2))

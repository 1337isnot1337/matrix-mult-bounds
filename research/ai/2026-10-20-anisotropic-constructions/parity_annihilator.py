"""Exact finite controls for the written pairwise-annihilator theorem.

This program does not replace the Grassmannian closure proof. No smaller
matrix multiplication exponent is established.
"""

from __future__ import annotations

import argparse
from itertools import product
import json
from pathlib import Path


def capacity_test(shapes, odd):
    """Necessary condition for a direct sum of rectangular matrix tensors."""
    dimensions = [sum(s[i] * s[(i + 1) % 3] for s in shapes) for i in range(3)]
    annihilators = [max(0, d - o) for d, o in zip(dimensions, odd)]
    upper = sum(max(a*b, b*c, c*a) for a, b, c in shapes)
    excluded = sum(annihilators) > upper
    strict_single_square = False
    if len(shapes) == 1 and len(set(shapes[0])) == 1 and min(annihilators) > 0:
        strict_single_square = sum(annihilators) >= upper
        excluded = excluded or strict_single_square
    return {
        'shapes': [list(s) for s in shapes], 'odd_dimensions': list(odd),
        'target_leg_dimensions': dimensions,
        'required_annihilator_dimensions': annihilators,
        'sum_required': sum(annihilators), 'matrix_space_upper_bound': upper,
        'strict_single_square_exclusion': strict_single_square,
        'excluded': excluded,
    }


def source_controls(a, b):
    m = a+b-1
    coords = [list(product(range(a), range(m), range(b))),
              list(product(range(b), range(a), range(m))),
              list(product(range(m), range(b), range(a)))]
    weights = [lambda x: x[1]-x[0]-x[2],
               lambda y: y[2]-y[0]-y[1],
               lambda z: z[0]-z[1]-z[2]]
    shifts = (1, 1, 0)
    odd = [sum((weights[k](c)+shifts[k]) % 2 for c in coords[k]) for k in range(3)]
    terms = 0
    for i, j, p, q, r, s in product(range(a), range(b), range(a), range(b), range(a), range(b)):
        rho = ((p+q-i-s+1) % 2, (r+s-j-p+1) % 2, (i+j-q-r) % 2)
        if sum(rho) != 2:
            assert sum(rho) == 0
            continue
        assert rho.count(0) == 1
        terms += 1
    return {'a': a, 'b': b, 'leg_dimension': a*b*m, 'odd_dimensions': odd,
            'retained_terms': terms, 'no_two_even_terms': True}


def verify():
    corner_checks = 0
    for a, b, c in product(range(1, 9), repeat=3):
        values = []
        for x, y, z in product((0, a), (0, b), (0, c)):
            values.append(x*(b-y)+y*(c-z)+z*(a-x))
            corner_checks += 1
        assert max(values) == max(a*b, b*c, c*a)
    identity_checks = 0
    for n in range(1, 13):
        for x, y, z in product(range(n+1), repeat=3):
            gap = n*n - (x*(n-y)+y*(n-z)+z*(n-x))
            rhs = (n-x)*(n-y)*(n-z)+x*y*z
            assert n*gap == rhs
            assert gap >= 0
            if x*y*z > 0:
                assert gap > 0
            identity_checks += 1
    controls = [source_controls(2, 2), source_controls(4, 4),
                source_controls(4, 5), source_controls(5, 5)]
    assert controls[-1]['odd_dimensions'] == [113, 113, 112]
    assert controls[-1]['retained_terms'] == 11725
    cases = [capacity_test([(14, 14, 14), (4, 4, 4)], (113, 113, 112)),
             capacity_test([(14, 14, 14)], (113, 113, 112)),
             capacity_test([(13, 13, 13)], (113, 113, 112)),
             capacity_test([(3, 3, 3)], (6, 6, 6)),
             capacity_test([(5, 5, 9), (4, 4, 9)], (113, 113, 112)),
             capacity_test([(5, 9, 4), (4, 9, 5)], (113, 113, 112)),
             capacity_test([(5, 5, 5)], (113, 113, 112))]
    assert all(c['excluded'] for c in cases[:4])
    assert not any(c['excluded'] for c in cases[4:])
    return {'claim_status': 'written proof; same-session checks; no independent review',
            'new_exponent_established': False,
            'corner_evaluations': corner_checks, 'integer_deficit_identities': identity_checks,
            'source_controls': controls, 'target_controls': cases,
            'scope': 'arbitrary one-copy degenerations from the specified parity source; no general asymptotic exclusion'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = json.dumps(verify(), indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report)
    else:
        print(report, end='')


if __name__ == '__main__':
    main()

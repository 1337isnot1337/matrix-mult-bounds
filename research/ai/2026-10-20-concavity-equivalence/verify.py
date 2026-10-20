"""Exact checks of the filtration proof chain; not a proof by enumeration."""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import platform

H = [Fraction(0), Fraction(1)]


def profile(a, b):
    if min(a, b) == 0:
        return Fraction(0)
    m, n = sorted((a, b))
    while len(H) <= m:
        k = len(H) - 1
        H.append(H[-1] * Fraction(3*k+1, 3*k))
    return H[m] * Fraction(2*n+m-1, 2)


def lengths(a, c):
    return list(range(a+c-1, abs(a-c), -2))


def check_source(a, b, c, d, value=profile):
    aa, bb = lengths(a, c), lengths(b, d)
    source = value(a, b) * value(c, d)
    x0 = sum(value(aa[0], s) for s in bb)
    xe = min(b*value(aa[0], d), d*value(aa[0], b))
    y0 = sum(value(r, bb[0]) for r in aa)
    ye = min(a*value(bb[0], c), c*value(bb[0], a))
    if not (x0 <= xe <= source and y0 <= ye <= source):
        raise ValueError(('endpoint or Jensen bound', (a, b, c, d)))
    if sum(aa) != a*c or sum(bb) != b*d:
        raise ValueError('block dimension sum')
    for r in aa:
        if sum(value(r, s) for s in bb) > x0:
            raise ValueError('X monotonicity')
    for s in bb:
        if sum(value(r, s) for r in aa) > y0:
            raise ValueError('Y monotonicity')
    for k in range(len(aa)+len(bb)-1):
        diagonal = sum(value(r, bb[k-i]) for i, r in enumerate(aa)
                       if 0 <= k-i < len(bb))
        if diagonal > min(x0, y0):
            raise ValueError('Z domination')
    return {
        'source': [a, b, c, d], 'source_exact': str(source),
        'X0_exact': str(x0), 'X_endpoint_min_exact': str(xe),
        'Y0_exact': str(y0), 'Y_endpoint_min_exact': str(ye),
        'inequalities': 2*(len(aa)+len(bb))-1,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-size', type=int, default=6)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.max_size < 1:
        parser.error('--max-size must be positive')
    count = 0
    for source in product(range(1, args.max_size+1), repeat=4):
        count += check_source(*source)['inequalities']
    stress = [
        (1, 1009, 2, 1013), (1009, 1, 1013, 2),
        (257, 2, 3, 509), (2, 257, 509, 3),
        (17, 257, 19, 509), (64, 65, 64, 65),
    ]
    records = [check_source(*source) for source in stress]
    report = {
        'status': 'passed', 'python': platform.python_version(),
        'arithmetic': 'fractions.Fraction; integer comparisons only',
        'grid_max_size': args.max_size, 'grid_sources': args.max_size**4,
        'grid_filtration_inequalities': count,
        'grid_intermediate_bounds': 4*args.max_size**4,
        'stress_sources': len(stress),
        'stress_filtration_inequalities': sum(r['inequalities'] for r in records),
        'stress_records': records,
        'scope': 'Finite exact checks of a separately written all-size proof. '
                 'No independent review, Lean formalization, or exponent improvement.',
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'stress_records'}, indent=2))


if __name__ == '__main__':
    main()

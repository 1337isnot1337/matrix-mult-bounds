#!/usr/bin/env python3
"""Independent characteristic-zero rank check via SymPy exact rational matrices.

This implementation does not import the finite-field or kernel-basis verifier.
It is optional verification, not an independent mathematical review.
"""
from concurrent.futures import ProcessPoolExecutor
import json
from sympy import Matrix, Rational


def check(pair):
    a, d = pair
    m, q = d + 1, a % (d + 1)
    defect = (q - 1) * (m - q) if q else 0
    c, ratio = Rational(5, 7), Rational(2, 3)
    total = 0
    for ell in range(1, d + 1):
        block = Matrix(a, a, lambda i, j:
                       c * ratio ** (ell+j-i)
                       if 0 <= ell+j-i <= d else 0)
        total += block.rank()
    assert total == a*d - defect, (a,d,total,defect)
    return pair


def main():
    cases = [(a, d) for a in range(3, 13)
             for d in range(1, min(6, a - 1) + 1)]
    with ProcessPoolExecutor(max_workers=4) as pool:
        completed = list(pool.map(check, cases))
    print(json.dumps({'result': 'PASS', 'rational_cases': len(completed),
                      'a_range': [3,12], 'd_max': 6,
                      'method': 'exact SymPy ranks over Q, independent of the finite-field implementation'},
                     sort_keys=True))


if __name__ == '__main__':
    main()

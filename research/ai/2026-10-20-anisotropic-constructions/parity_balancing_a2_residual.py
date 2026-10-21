"""Exact three-shift residual formula for the A(2,b) triangular lift.

The formula itself uses only rational arithmetic. --verify compares every
matrix unit with the independent binomial-block triangular generator.
"""

import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path


def residual_matrix(b, matrix):
    if b < 2 or len(matrix) != b + 1 or any(len(row) != b + 1 for row in matrix):
        raise ValueError('Expected b>=2 and a (b+1)-square matrix')
    return [[Fraction((b-i)*(b-i-1), b) * matrix[i][j]
             + Fraction(2*(i+1)*(b-i-1), b) * matrix[i+1][j+1]
             + Fraction((i+1)*(i+2), b) * matrix[i+2][j+2]
             for j in range(b-1)] for i in range(b-1)]


def verify(b):
    import sympy as sp
    from parity_balancing_triangular import triangular_lift
    lifted = triangular_lift(2, b)
    change = sp.zeros(b-1)
    for v in range(b-1):
        change[b-2-v, v] = (-1)**v * comb(b-2, v)
    inverse = change.inv()
    for index, residual in enumerate(lifted['residual_matrices']):
        unit = [[int(row*(b+1)+col == index) for col in range(b+1)]
                for row in range(b+1)]
        expected = sp.Matrix(residual_matrix(b, unit))
        if change * residual * inverse != expected:
            raise ArithmeticError('The explicit residual formula disagrees with the exact lift')
    identity = residual_matrix(b, [[int(i == j) for j in range(b+1)] for i in range(b+1)])
    if identity != [[(b+1)*int(i == j) for j in range(b-1)] for i in range(b-1)]:
        raise ArithmeticError('The identity action is incorrect')
    for k in range(b+1):
        unit = [[int(i == j == k) for j in range(b+1)] for i in range(b+1)]
        residual = residual_matrix(b, unit)
        if sum(residual[i][i] for i in range(b-1)) != b-1:
            raise ArithmeticError('The trace scaling is incorrect')
    return {'source': [2, b], 'matrix_units_checked': (b+1)**2,
            'residual_formula_exact': True, 'identity_multiplier': b+1,
            'trace_multiplier': b-1, 'residual_retained': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify', type=int, nargs='+', default=[2, 3, 4, 5])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = {'identity': 'A(2,b) -> M_(b+1) plus explicit M_(b-1) residual on the same legs',
              'residual_may_be_discarded': False, 'new_exponent_established': False,
              'records': [verify(b) for b in args.verify]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

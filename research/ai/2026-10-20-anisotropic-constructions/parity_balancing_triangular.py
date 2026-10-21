"""Constructive triangular lifts from full cyclic convolution sources.

For a,b>=2, solve pi W(F(A)) = A pi exactly. The quotient has dimension
a+b-1 and the invariant kernel has dimension (a-1)(b-1). The residual block
is retained explicitly; it may not be discarded from a tensor claim.
"""

import argparse
from itertools import product
import json
from math import comb
from pathlib import Path

import sympy as sp


def projection(a, b=None):
    b = a if b is None else b
    d = b - 1
    result = sp.zeros(a + b - 1, a * b)
    for i, q in product(range(a), range(b)):
        result[i + d - q, b * i + q] = (-1) ** q * comb(d, q)
    return result


def kernel_embedding(a, b=None):
    b = a if b is None else b
    d = b - 1
    result = sp.zeros(a * b, (a - 1) * d)
    for u, v in product(range(a - 1), range(d)):
        result[b * u + v, d * u + v] = sp.Rational(d - v, d)
        result[b * (u + 1) + v + 1, d * u + v] = sp.Rational(v + 1, d)
    return result


def lift_maps(a, b=None):
    b = a if b is None else b
    d, n = b - 1, a + b - 1
    pi = projection(a, b)
    maps = sp.zeros(n * n, a * b * n)
    blocks = []
    for c in range(1 - n, a):
        ks = list(range(max(0, -c), min(n - 1, a - 1 - c) + 1))
        ps = list(range(max(0, -c - d), min(a - 1, a - 1 - c) + 1))
        matrix = sp.Matrix([[(-1) ** (k - p) * comb(d, k - p) if 0 <= k - p <= d else 0
                             for k in ks] for p in ps])
        if len(ks) != len(ps) or not matrix.det():
            raise ArithmeticError('The binomial block is not invertible')
        inverse = matrix.inv()
        blocks.append({'weight_difference': c, 'input_k': ks, 'output_p': ps,
                       'determinant': str(matrix.det())})
        for s in range(b):
            for ik, k in enumerate(ks):
                i = k + c
                column = (i * n + k) * b + s
                for ip, p in enumerate(ps):
                    u = c + d + p
                    for v in range(n):
                        maps[n * u + v, column] += inverse[ik, ip] * pi[v, b * p + s]
    return maps, blocks


def physical_matrix(a, coordinates, b=None):
    b = a if b is None else b
    n = a + b - 1
    return sp.Matrix(a * b, a * b,
                     lambda row, col: coordinates[(row // b * n + row % b + col // b) * b + col % b])


def hankel_coordinates(a, matrix, b=None):
    b = a if b is None else b
    n = a + b - 1
    coordinates = []
    for i, k, s in product(range(a), range(n), range(b)):
        p = min(k, a - 1)
        q = k - p
        coordinates.append(matrix[b * i + q, b * p + s])
    if physical_matrix(a, coordinates, b) != matrix:
        return None
    return coordinates


def triangular_lift(a, b=None):
    b = a if b is None else b
    n, residual_size = a + b - 1, (a - 1) * (b - 1)
    maps, blocks = lift_maps(a, b)
    pi, q = projection(a, b), kernel_embedding(a, b)
    if pi * q != sp.zeros(n, residual_size):
        raise ArithmeticError('The displayed embedding is not in ker pi')
    _, pivot_rows = q.T.rref()
    left = q[list(pivot_rows), :].inv()
    residual = []
    lower_source_maps = []
    all_hankel = True
    for row in range(n * n):
        a_matrix = sp.zeros(n)
        a_matrix[row // n, row % n] = 1
        physical = physical_matrix(a, list(maps.row(row)), b)
        if pi * physical != a_matrix * pi:
            raise ArithmeticError('The quotient-action identity failed')
        k_matrix = left * (physical * q)[list(pivot_rows), :]
        if physical * q != q * k_matrix:
            raise ArithmeticError('The invariant-kernel action identity failed')
        residual.append(k_matrix)
        coordinates = hankel_coordinates(a - 1, k_matrix, b - 1)
        all_hankel &= coordinates is not None
        lower_source_maps.append(coordinates)
    singlet = sum((residual[n * i + i] for i in range(n)), sp.zeros(residual_size))
    next_flag = None
    if a >= 3 and b >= 3:
        lower_pi, lower_q = projection(a - 1, b - 1), kernel_embedding(a - 1, b - 1)
        violations = []
        for row, matrix in enumerate(residual):
            defect = lower_pi * matrix * lower_q
            if any(defect):
                violations.append((row, defect))
        next_flag = {'preserved': not violations, 'violating_matrix_units': len(violations)}
        if violations:
            row, defect = violations[0]
            next_flag.update({'first_target_matrix_unit': [row // n, row % n],
                              'residual_block': encode_matrix(residual[row]),
                              'projected_flag_defect': encode_matrix(defect)})
    return {'a': a, 'b': b, 'source_leg_dimension': a * b * n, 'quotient_size': n,
            'residual_matrix_size': residual_size, 'binomial_blocks': blocks,
            'common_source_maps': maps, 'residual_matrices': residual,
            'residual_in_lower_hankel_space': bool(all_hankel),
            'lower_source_maps': sp.Matrix(lower_source_maps) if all_hankel else None,
            'residual_identity_eigenvalues': {str(k): int(v) for k, v in singlet.eigenvals().items()},
            'next_natural_kernel_flag': next_flag,
            'quotient_and_kernel_identities_exact': True}


def encode_matrix(matrix):
    denominator = int(sp.ilcm(1, *[entry.q for entry in matrix]))
    return {'denominator': denominator,
            'numerators': [[int(denominator * matrix[i, j]) for j in range(matrix.cols)]
                           for i in range(matrix.rows)]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a', type=int, nargs='+', default=[2, 3])
    parser.add_argument('--pair', type=int, nargs=2, action='append',
                        help='An anisotropic pair; repeat to replace the default square cases')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    records = []
    for a, b in (args.pair if args.pair else [(a, a) for a in args.a]):
        if min(a, b) < 2:
            raise ValueError('Use a,b>=2')
        record = triangular_lift(a, b)
        record['common_source_maps'] = encode_matrix(record['common_source_maps'])
        record['residual_matrices'] = [encode_matrix(m) for m in record['residual_matrices']]
        if record['lower_source_maps'] is not None:
            record['lower_source_maps'] = encode_matrix(record['lower_source_maps'])
        records.append(record)
        print('a,b', a, b, 'lower_hankel', record['residual_in_lower_hankel_space'],
              'identity_eigenvalues', record['residual_identity_eigenvalues'], flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({'source_family': 'full A(a,b)',
                                      'identity': 'A(a,b) maps to M_(a+b-1) plus an explicit residual on the same target legs',
                                      'residual_may_be_discarded': False,
                                      'corrected_source': 'A(a,b) direct sum M_((a-1)(b-1))',
                                      'corrected_target': 'M_(a+b-1)', 'records': records,
                                      'new_exponent_established': False}, indent=2) + '\n')


if __name__ == '__main__':
    main()

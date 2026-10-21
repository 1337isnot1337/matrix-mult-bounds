"""Replay triangular quotient and residual identities using Fractions only."""

import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path


def zeros(rows, columns):
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def multiply(left, right):
    if len(left[0]) != len(right):
        raise ValueError('Matrix dimensions do not match')
    result = zeros(len(left), len(right[0]))
    for i, row in enumerate(left):
        for k, value in enumerate(row):
            if value:
                for j, factor in enumerate(right[k]):
                    if factor:
                        result[i][j] += value * factor
    return result


def decode_matrix(record, rows, columns):
    denominator = record['denominator']
    numerator = record['numerators']
    if type(denominator) is not int or denominator <= 0:
        raise ValueError('The common denominator must be a positive integer')
    if len(numerator) != rows or any(len(row) != columns for row in numerator):
        raise ValueError('A saved rational matrix has the wrong shape')
    if any(type(value) is not int for row in numerator for value in row):
        raise ValueError('Rational matrix numerators must be integers')
    return [[Fraction(value, denominator) for value in row] for row in numerator]


def verify_record(record):
    a, b = record['a'], record['b']
    if min(a, b) < 2:
        raise ValueError('The construction requires a,b>=2')
    n, r, physical = a + b - 1, (a - 1) * (b - 1), a * b
    if record['quotient_size'] != n or record['residual_matrix_size'] != r:
        raise ValueError('The declared quotient or residual dimension is incorrect')
    maps = decode_matrix(record['common_source_maps'], n * n, physical * n)
    if len(record['residual_matrices']) != n * n:
        raise ValueError('A residual matrix is missing')
    residual = [decode_matrix(matrix, r, r) for matrix in record['residual_matrices']]
    pi, q = zeros(n, physical), zeros(physical, r)
    for i in range(a):
        for j in range(b):
            pi[i + b - 1 - j][b * i + j] = Fraction((-1) ** j * comb(b - 1, j))
    for u in range(a - 1):
        for v in range(b - 1):
            q[b * u + v][(b - 1) * u + v] = Fraction(b - 1 - v, b - 1)
            q[b * (u + 1) + v + 1][(b - 1) * u + v] = Fraction(v + 1, b - 1)
    if multiply(pi, q) != zeros(n, r):
        raise ArithmeticError('The explicit kernel embedding failed')
    for row, coordinates in enumerate(maps):
        matrix = [[coordinates[((i // b) * n + i % b + j // b) * b + j % b]
                   for j in range(physical)] for i in range(physical)]
        target = zeros(n, physical)
        target[row // n] = list(pi[row % n])
        if multiply(pi, matrix) != target:
            raise ArithmeticError(f'The quotient identity failed at matrix unit {row}')
        if multiply(matrix, q) != multiply(q, residual[row]):
            raise ArithmeticError(f'The retained residual identity failed at matrix unit {row}')
    return {'source_lengths': [a, b], 'source_leg_dimension': physical * n,
            'quotient_size': n, 'residual_matrix_size': r,
            'target_matrix_units_checked': n * n,
            'quotient_identity_exact': True, 'residual_identity_exact': True,
            'arithmetic': 'Python Fraction', 'residual_retained': True}


def verify_report(report):
    if report.get('residual_may_be_discarded') is not False:
        raise ValueError('The report must explicitly retain the residual correction')
    return {'records': [verify_record(record) for record in report['records']],
            'new_exponent_established': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    args = parser.parse_args()
    print(json.dumps(verify_report(json.loads(args.certificate.read_text())), indent=2))


if __name__ == '__main__':
    main()

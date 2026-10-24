"""Exact rational recurrence certificates and bounded full-source controls.

The order-five and order-seven vectors were supplied by the discovery run.
This verifier checks them; it neither repeats discovery nor infers all-size
periodicity from the finite source profiles.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path


WITNESSES = [
    {'order': 2, 'triple': [[0, 0, 1], [], [-1]],
     'kernel_polynomials': [[], [1], []], 'source_sizes': [3, 4]},
    {'order': 3, 'triple': [[0, 0, 1], [0, 1], [1]],
     'kernel_polynomials': [[], [1], [0, -1], []], 'source_sizes': [4, 5, 8]},
    {'order': 5, 'triple': [[1, -1], [-1], [0, 0, 1]],
     'kernel_polynomials': [[-1, -2, 1, 2], [-1, -1, 2, 1], [-1, 0, 2, 0],
                            [-1, 1, 1, 0], [-1, 2, 0, 0], [0, 1, 0, 0]],
     'source_sizes': [4, 5, 9]},
    {'order': 7, 'triple': [[1, -1], [-1, -1], [0, 0, 4]],
     'kernel_polynomials': [[-4, -44, -140, -36, 384, 320],
                            [-4, -36, -76, 68, 240, 64],
                            [-4, -28, -28, 92, 96, 0],
                            [-4, -20, 4, 68, 16, 0],
                            [-4, -12, 20, 28, 0, 0],
                            [-4, -4, 20, 4, 0, 0],
                            [-4, 4, 8, 0, 0, 0], [-3, 6, 1, 0, 0, 0]],
     'source_sizes': [6, 7]},
]


def rank_rational(matrix):
    """Exact elimination, including when every input coefficient is an int."""
    rows = [[Fraction(value) for value in row] for row in matrix]
    position = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(position, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[position], rows[pivot] = rows[pivot], rows[position]
        inverse = 1 / rows[position][column]
        active = [(index, value * inverse) for index, value in enumerate(rows[position]) if value]
        for index, value in active:
            rows[position][index] = value
        for row in rows[position + 1:]:
            factor = row[column]
            if factor:
                for index, value in active:
                    row[index] -= factor * value
        position += 1
        if position == len(rows):
            break
    return position


def recurrence_matrix(n, triple):
    """All n-1 recurrence equations, including coefficients through degree n."""
    if n < 2:
        raise ValueError('auxiliary recurrence requires n>=2')
    return [[triple[L - r][k - j]
             if 0 <= L - r < 3 and 0 <= k - j < len(triple[L - r]) else 0
             for L in range(n + 1) for j in range(n - 1)]
            for r in range(n - 1) for k in range(n + 1)]


def source_matrix(a, triple):
    """Literal full R_(a,a), rows (j,L), columns (H,r); no active crop."""
    if a < 3:
        raise ValueError('degree-two literal source controls require a>=3')
    def coefficient(x_degree, z_degree):
        if 0 <= z_degree < 3 and 0 <= x_degree < len(triple[z_degree]):
            return triple[z_degree][x_degree]
        return 0
    return [[coefficient(H - j, L - r)
             for H in range(2 * a - 1) for r in range(a)]
            for j in range(a) for L in range(2 * a - 1)]


def check_witness(n, triple, polynomials):
    """Independent coefficient convolution; does not call the matrix builder."""
    if len(polynomials) != n + 1 or any(len(poly) > n - 1 for poly in polynomials):
        raise ArithmeticError('witness has invalid coordinate count or degree')
    if not any(any(poly) for poly in polynomials):
        raise ArithmeticError('witness must be nonzero')
    for r in range(n - 1):
        residual = [0] * (n + 1)
        for offset, coefficient in enumerate(triple):
            for i, left in enumerate(coefficient):
                for j, right in enumerate(polynomials[r + offset]):
                    residual[i + j] += left * right
        if any(residual):
            raise ArithmeticError(f'witness fails recurrence equation {r}')


def report():
    records = []
    for witness in WITNESSES:
        n, triple = witness['order'], witness['triple']
        check_witness(n, triple, witness['kernel_polynomials'])
        recurrence = recurrence_matrix(n, triple)
        recurrence_rank = rank_rational(recurrence)
        if len(recurrence) != n * n - 1 or recurrence_rank != n * n - 2:
            raise ArithmeticError('prime-order recurrence does not have nullity one')
        record = {'order': n, 'triple': triple,
                  'kernel_polynomials': witness['kernel_polynomials'],
                  'geometric_order_scope': 'characteristic different from two' if n == 7 else 'every field',
                  'recurrence_size': n * n - 1, 'recurrence_rank': recurrence_rank,
                  'polynomial_equations_checked': n - 1, 'source_controls': []}
        for a in witness['source_sizes']:
            source = source_matrix(a, triple)
            source_rank = rank_rational(source)
            expected = a * a + 2 * a - int((a + 1) % n == 0)
            if source_rank != expected:
                raise ArithmeticError('full source rank disagrees with the written torsion implication')
            record['source_controls'].append({'a': a, 'matrix_size': len(source),
                                              'literal_rank': source_rank,
                                              'multiple_of_order': (a + 1) % n == 0})
        records.append(record)
    return {
        'scope': 'Four exact rational prime-order recurrence certificates and bounded balanced '
                 'source controls. All-size conclusions use the written geometric criterion.',
        'discovery_boundary': 'The order-five and order-seven integer vectors were supplied by '
                              'the discovery run; this package verifies them without rerunning discovery.',
        'integer_identity_scope': 'The convolution identities hold over Z and reduce over every field. '
                                  'Each vector has a unit coefficient, so remains nonzero; the '
                                  'geometric order conclusion additionally needs the stated hypotheses.',
        'coefficient_order': 'triple u,v,w for u+z*v+z^2*w; polynomial coefficients ascending in x',
        'recurrence_matrices_checked': len(records),
        'polynomial_equations_checked': sum(record['polynomial_equations_checked'] for record in records),
        'literal_source_matrices_checked': sum(len(record['source_controls']) for record in records),
        'small_auxiliary_scope': 'Orders2 and3 use T2 andT3 only; no literal source claim at a=1,2',
        'order_seven_characteristic_two_boundary': {
            'reduced_triple': [[1, 1], [1, 1], [0, 0, 0]],
            'common_factor': [1, 1], 'primitive_degree': 0, 'order_claim': False},
        'records': records, 'independent_review': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    payload = json.dumps(report(), indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    else:
        print(payload, end='')

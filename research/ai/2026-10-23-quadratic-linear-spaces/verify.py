"""Exact binary linear-family certificates for the literal R_(3,3) block.

The subspace census tests F2 points. Its exceptional families need not keep
their rank cap after scalar extension; an explicit F4 counterexample is saved.
"""
import argparse
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path


UPPER_BASIS = [84, 174, 311]
LOWER_BASIS = [8, 16, 32, 64, 128, 256]
EXTENSION_BASIS = [1, 4, 56, 64, 128, 256]
EXTENSION_PARAMETERS = [0, 1, 1, 0, 1, 2]


def coefficients(vector):
    return [(vector >> index) & 1 for index in range(9)]


def source_matrix(values):
    """Rows (j,L), columns (H,r): coefficient x^(H-j) z^(L-r)."""
    return [[values[3 * (L - r) + H - j]
             if 0 <= H - j < 3 and 0 <= L - r < 3 else 0
             for H in range(5) for r in range(3)]
            for j in range(3) for L in range(5)]


def binary_rank(rows):
    pivots = {}
    for entries in rows:
        row = sum((entry & 1) << index for index, entry in enumerate(entries))
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def integer_determinant(matrix):
    """Fraction-free elimination, independent of packed binary rank."""
    matrix = [list(row) for row in matrix]
    size, previous, sign = len(matrix), 1, 1
    for k in range(size - 1):
        pivot_row = next((i for i in range(k, size) if matrix[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            matrix[k], matrix[pivot_row] = matrix[pivot_row], matrix[k]
            sign *= -1
        pivot = matrix[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = pivot * matrix[i][j] - matrix[i][k] * matrix[k][j]
                if numerator % previous:
                    raise ArithmeticError('Bareiss division is not exact')
                matrix[i][j] = numerator // previous
            matrix[i][k] = 0
        previous = pivot
    return sign * matrix[-1][-1]


def span(basis):
    vectors = [0]
    for basis_vector in basis:
        vectors += [vector ^ basis_vector for vector in vectors]
    return sorted(vectors)


def kernel_basis(normals):
    basis, generated = [], {0}
    for vector in range(512):
        if vector not in generated and all((vector & normal).bit_count() % 2 == 0
                                           for normal in normals):
            basis.append(vector)
            generated |= {element ^ vector for element in generated}
    return basis


def upper_certificate(basis):
    points = span(basis)
    if len(basis) != 3 or len(set(points)) != 8:
        raise ArithmeticError('upper certificate requires three independent vectors')
    records = []
    for vector in points[1:]:
        determinant = integer_determinant(source_matrix(coefficients(vector)))
        if determinant % 2 == 0:
            raise ArithmeticError('upper certificate contains a singular source matrix')
        records.append({'vector': vector, 'integer_determinant': determinant})
    return {'basis': list(basis), 'nonzero_points': records}


def normal_spaces(dimension):
    """Each normal subspace once, via its unique reduced binary basis."""
    for pivots in combinations(range(9), dimension):
        choices = []
        for pivot in pivots:
            free = [bit for bit in range(pivot) if bit not in pivots]
            choices.append([(1 << pivot) + sum(((mask >> j) & 1) << bit
                                               for j, bit in enumerate(free))
                            for mask in range(1 << len(free))])
        yield from product(*choices)


def subspace_census(ranks):
    masks = {}
    for cap in (12, 14):
        forbidden = [vector for vector in range(1, 512) if ranks[vector] > cap]
        masks[cap] = [sum(1 << index for index, vector in enumerate(forbidden)
                         if (vector & normal).bit_count() % 2 == 0)
                      for normal in range(512)]
    compressions = {}
    for normal in range(1, 8):
        for axis, normals in (
                ('x', [normal << (3 * k) for k in range(3)]),
                ('z', [sum(((normal >> k) & 1) << (3 * k + i) for k in range(3))
                       for i in range(3)])):
            compressions[tuple(span(normals))] = {'axis': axis, 'normal': normal}
    minima = {cap: {'minimum_forbidden_points': 512} for cap in (12, 14)}
    count_seven = 0
    for first, second in normal_spaces(2):
        count_seven += 1
        for cap in (12, 14):
            count = (masks[cap][first] & masks[cap][second]).bit_count()
            if count < minima[cap]['minimum_forbidden_points']:
                minima[cap] = {'minimum_forbidden_points': count,
                               'attaining_normals': [first, second]}
    spaces, count_six = {12: [], 14: []}, 0
    for normals in normal_spaces(3):
        count_six += 1
        for cap in (12, 14):
            if masks[cap][normals[0]] & masks[cap][normals[1]] & masks[cap][normals[2]]:
                continue
            basis = kernel_basis(normals)
            histogram = Counter(ranks[vector] for vector in span(basis) if vector)
            if len(basis) != 6 or max(histogram) > cap:
                raise ArithmeticError('annihilator census produced an invalid subspace')
            spaces[cap].append({'annihilator_basis': list(normals), 'basis': basis,
                               'compression': compressions.get(tuple(span(normals))),
                               'nonzero_rank_histogram': dict(sorted(histogram.items()))})
    if count_seven != 43435 or count_six != 788035:
        raise ArithmeticError('normal-space enumeration is incomplete')
    return {'dimension_seven_spaces_checked': count_seven,
            'dimension_six_spaces_checked': count_six,
            'dimension_seven_minima': minima, 'dimension_six_spaces': spaces}


def gf4_determinant(matrix):
    """F4 = F2[t]/(t^2+t+1), encoded as 0,1,t,t+1 = 0,1,2,3."""
    multiply = ((0, 0, 0, 0), (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2))
    inverse = (0, 1, 3, 2)
    matrix = [list(row) for row in matrix]
    determinant, size = 1, len(matrix)
    for k in range(size):
        pivot_row = next((i for i in range(k, size) if matrix[i][k]), None)
        if pivot_row is None:
            return 0
        matrix[k], matrix[pivot_row] = matrix[pivot_row], matrix[k]
        determinant = multiply[determinant][matrix[k][k]]
        scale = inverse[matrix[k][k]]
        matrix[k] = [multiply[value][scale] for value in matrix[k]]
        for i in range(k + 1, size):
            factor = matrix[i][k]
            if factor:
                matrix[i] = [value ^ multiply[factor][pivot]
                             for value, pivot in zip(matrix[i], matrix[k])]
    return determinant


def extension_coefficients(parameters):
    values = [0] * 9
    for vector, scalar in zip(EXTENSION_BASIS, parameters):
        for index in range(9):
            if vector >> index & 1:
                values[index] ^= scalar
    return values


def report():
    ranks = [binary_rank(source_matrix(coefficients(vector))) for vector in range(512)]
    lower_points = span(LOWER_BASIS)
    if len(set(lower_points)) != 64 or max(ranks[vector] for vector in lower_points) != 12:
        raise ArithmeticError('fixed-factor lower certificate failed')
    cross_tab = Counter((binary_rank([coefficients(vector)[3 * i:3 * i + 3]
                                     for i in range(3)]), ranks[vector])
                        for vector in range(1, 512))
    extension = extension_coefficients(EXTENSION_PARAMETERS)
    determinant = gf4_determinant(source_matrix(extension))
    if determinant != 1:
        raise ArithmeticError('F4 extension witness is no longer invertible')
    return {
        'scope': 'Binary rational-point linear subspaces. The finite classification does not '
                 'assert rank caps after extending scalars.',
        'coefficient_bit_order': ['u0', 'u1', 'u2', 'v0', 'v1', 'v2', 'w0', 'w1', 'w2'],
        'upper_certificate': upper_certificate(UPPER_BASIS),
        'lower_certificate': {'basis': LOWER_BASIS, 'fixed_factor': 'z',
                              'nonzero_rank_histogram': dict(sorted(Counter(
                                  ranks[vector] for vector in lower_points if vector).items()))},
        'literal_source_ranks_including_zero': ranks,
        'nonzero_rank_histogram': dict(sorted(Counter(ranks[1:]).items())),
        'coefficient_rank_source_rank_counts': [
            {'coefficient_rank': first, 'source_rank': second, 'count': count}
            for (first, second), count in sorted(cross_tab.items())],
        'finite_subspace_classification': subspace_census(ranks),
        'extension_counterexample': {
            'field': 'F4=F2[t]/(t^2+t+1); 0,1,2,3 encode 0,1,t,t+1',
            'binary_family_basis': EXTENSION_BASIS, 'parameters': EXTENSION_PARAMETERS,
            'coefficients': extension, 'literal_determinant': determinant},
        'independent_review': False, 'improves_omega': False,
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

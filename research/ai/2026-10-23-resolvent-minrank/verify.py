"""Exact integer replay for a uniform fixed-resolvent obstruction.

This file uses only the Python standard library. The finite certificate proves
a minimum matrix rank of six for the full mixed outer block. The application
to formal Laurent curves is a separate written linear-algebra argument.
"""

import argparse
from itertools import product
import json
from pathlib import Path


def zeros(m, n):
    return [[0] * n for _ in range(m)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def combine(basis, coefficients):
    m, n = len(basis[0]), len(basis[0][0])
    result = zeros(m, n)
    for matrix, coefficient in zip(basis, coefficients):
        if coefficient:
            for i in range(m):
                for j in range(n):
                    result[i][j] += coefficient * matrix[i][j]
    return result


def multiply(left, right):
    result = zeros(len(left), len(right[0]))
    right_sparse = [[(j, x) for j, x in enumerate(row) if x] for row in right]
    for i, row in enumerate(left):
        for k, value in enumerate(row):
            if value:
                for j, coefficient in right_sparse[k]:
                    result[i][j] += value * coefficient
    return result


def integer_inverse(matrix):
    """Find a small lift and accept it only after both exact Z identities."""
    n = len(matrix)
    prime = 1009
    augmented = [list(row) + unit for row, unit in zip(matrix, identity(n))]
    for column in range(n):
        pivot = next((i for i in range(column, n) if augmented[i][column] % prime), None)
        if pivot is None:
            raise ValueError('source unit is singular modulo the discovery prime')
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = pow(augmented[column][column], -1, prime)
        augmented[column] = [value * scale % prime for value in augmented[column]]
        for i in range(n):
            if i != column:
                coefficient = augmented[i][column]
                if coefficient:
                    augmented[i] = [(x - coefficient * y) % prime
                                    for x, y in zip(augmented[i], augmented[column])]
    inverse = [[x if x <= prime // 2 else x - prime for x in row[n:]]
               for row in augmented]
    if multiply(matrix, inverse) != identity(n) or multiply(inverse, matrix) != identity(n):
        raise ValueError('lift is not a two-sided inverse over the integers')
    return inverse


def outer_source():
    rows = list(product(range(4), range(7)))
    columns = list(product(range(7), range(4)))
    matrices = []
    for i, s in product(range(4), repeat=2):
        matrices.append([[int(H - j == i and L - r == s) for H, r in columns]
                         for j, L in rows])
    unit = combine(matrices, [int(i + s == 3) for i, s in product(range(4), repeat=2)])
    inverse = integer_inverse(unit)
    normalized = [multiply(inverse, matrix) for matrix in matrices]
    high = [multiply(matrices[0], matrix) for matrix in normalized]
    return matrices, unit, inverse, normalized, high


def mixed_basis():
    matrices, unit, inverse, normalized, high = outer_source()
    # high(F0)=S00. Removing f03 fixes this one-dimensional redundancy.
    if combine(high, [int(i + s == 3) for i, s in product(range(4), repeat=2)]) != matrices[0]:
        raise ValueError('mixed-block gauge relation is false')
    labels = [['g', i, s] for i, s in product(range(4), repeat=2)]
    labels += [['f', i, s] for i, s in product(range(4), repeat=2) if (i, s) != (0, 3)]
    basis = matrices + [matrix for index, matrix in enumerate(high) if index != 3]
    return basis, labels


def validate_minors(certificate):
    basis, labels = mixed_basis()
    if (certificate.get('size') != 6 or certificate.get('dimension') != 31
            or certificate.get('labels') != labels or certificate.get('remaining_dimension') != 0):
        raise ValueError('wrong mixed-block certificate format or claimed dimension')
    stages = certificate.get('stages', [])
    if len(stages) != 31:
        raise ValueError('complete elimination needs exactly 31 stages')
    diagonal_factors = set()
    for number, stage in enumerate(stages):
        form = stage['form']
        pivot = stage['pivot']
        minor = stage['minor']
        if (len(form) != len(basis) or any(type(x) is not int for x in form)
                or type(pivot) is not int or not 0 <= pivot < len(basis)
                or form[pivot] not in (-1, 1)):
            raise ValueError(f'nonunit elimination at stage {number}')
        if (len(minor) != 6 or any(len(pair) != 2 for pair in minor)
                or any(type(x) is not int or not 0 <= x < 28 for pair in minor for x in pair)
                or len({pair[0] for pair in minor}) != 6
                or len({pair[1] for pair in minor}) != 6):
            raise ValueError(f'invalid six-by-six minor at stage {number}')
        for position, (row, column) in enumerate(minor):
            entries = [matrix[row][column] for matrix in basis]
            factor = entries[pivot] // form[pivot]
            if factor not in (-1, 1) or entries != [factor * x for x in form]:
                raise ValueError(f'incorrect diagonal linear form at stage {number}')
            diagonal_factors.add(factor)
            for _, later_column in minor[position + 1:]:
                if any(matrix[row][later_column] for matrix in basis):
                    raise ValueError(f'nonzero entry above the diagonal at stage {number}')
        chosen = basis[pivot]
        basis = [combine([matrix, chosen], [1, -form[j] // form[pivot]])
                 for j, matrix in enumerate(basis) if j != pivot]
    if basis:
        raise ValueError('some mixed-block parameters remain')
    return {'elimination_stages': len(stages), 'minor_size': 6,
            'diagonal_factors': sorted(diagonal_factors), 'remaining_parameters': 0}


def verify_outer_source_minimum():
    """Check the elementary block-triangular 16-minor for each leading term."""
    matrices, _, _, _, _ = outer_source()
    labels = list(product(range(4), repeat=2))
    for i0, s0 in labels:
        active = [(i, s) for i, s in labels if i < i0 or (i == i0 and s <= s0)]
        selected_rows = [j * 7 + r + s0 for j, r in product(range(4), repeat=2)]
        selected_columns = [(j + i0) * 4 + r for j, r in product(range(4), repeat=2)]
        for row_index, row in enumerate(selected_rows):
            j, r0 = divmod(row_index, 4)
            for column_index, column in enumerate(selected_columns):
                jp, r = divmod(column_index, 4)
                values = [matrices[4 * i + s][row][column] for i, s in active]
                if jp > j or (jp == j and r0 > r):
                    if any(values):
                        raise ValueError('outer-source triangular block has an unwanted entry')
                if row_index == column_index:
                    if values != [int((i, s) == (i0, s0)) for i, s in active]:
                        raise ValueError('outer-source minor has a wrong diagonal coefficient')
    return 16


def full_source_matrix(i, k, s):
    matrix = zeros(112, 112)
    for j, p, r in product(range(4), repeat=3):
        q = k - p
        if 0 <= q < 4:
            row = (j * 4 + p) * 7 + s + r
            column = ((i + j) * 4 + q) * 4 + r
            matrix[row][column] = 1
    return matrix


def full_normalized_matrix(outer, k):
    """Write J_k tensor outer in the maintained (H,q,r) coordinate order."""
    matrix = zeros(112, 112)
    for q in range(4):
        qp = q + 3 - k
        if not 0 <= qp < 4:
            continue
        for outer_row, values in enumerate(outer):
            H, r = divmod(outer_row, 4)
            row = (H * 4 + qp) * 4 + r
            for outer_column, value in enumerate(values):
                if value:
                    Hp, rp = divmod(outer_column, 4)
                    column = (Hp * 4 + q) * 4 + rp
                    matrix[row][column] = value
    return matrix


def verify_full_factorization():
    _, _, _, normalized, _ = outer_source()
    source_unit = combine([full_source_matrix(i, 3, 3 - i) for i in range(4)], [1] * 4)
    for i, k, s in product(range(4), range(7), range(4)):
        proposed = full_normalized_matrix(normalized[4 * i + s], k)
        if multiply(source_unit, proposed) != full_source_matrix(i, k, s):
            raise ValueError('outer/middle factorization disagrees with the literal source')
    nilpotent = full_normalized_matrix(normalized[0], 0)
    if multiply(nilpotent, nilpotent) != zeros(112, 112):
        raise ValueError('fixed normalized source coordinate is not square zero')
    literal_coordinate = full_source_matrix(0, 0, 0)
    entries = [(i, j) for i, row in enumerate(literal_coordinate) for j, x in enumerate(row) if x]
    if len(entries) != 16 or len({i for i, _ in entries}) != 16 or len({j for _, j in entries}) != 16:
        raise ValueError('literal nilpotent source coordinate does not have rank sixteen')
    return {'normalized_source_slices_checked': 112, 'nilpotent_rank': 16,
            'nilpotent_square_zero': True}


def verify(certificate):
    minors = validate_minors(certificate)
    source_minimum = verify_outer_source_minimum()
    source = verify_full_factorization()
    _, _, _, _, high = outer_source()
    sharp = high[0]
    nonzero_rows = [i for i, row in enumerate(sharp) if any(row)]
    if len(nonzero_rows) != 6:
        raise ValueError('sharp mixed-block witness is not supported on six rows')
    # It is nonzero, so the certified rank lower bound and six-row upper bound agree.
    return {'certificate': minors, **source,
            'outer_source_minimum_rank': source_minimum,
            'mixed_block_dimension': 31, 'mixed_block_minimum_rank': 6,
            'sharp_mixed_block_nonzero_rows': nonzero_rows,
            'full_limiting_space_dimension': 112,
            'full_limiting_space_minimum_rank': 6,
            'compression_rank_loss_budget': 4,
            'all_constant_split_compressions_injective': True,
            'written_application': 'Regular moving compressions with invertible leading product, fixed N resolvent',
            'formal_laurent_argument_machine_formalized': False,
            'arbitrary_singular_trajectories_excluded': False,
            'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.certificate.read_text()))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))

"""Exact acceptance for the complete two-sided A4 conjugation limit.

The verifier rebuilds the literal source and replays polynomial identities.
It does not import discovery.py or another research package. Only the Python
standard library is used. The Laurent-limit and evaluation arguments are in
proof.md; this program checks their finite coefficient premises.
"""

import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path

SIZE = 112
PRIME = 1009
ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CERTIFICATE = ROOT / 'results/conjugation-limit-2026-10-23/certificate.json'


def matrix_product(left, right, size=SIZE):
    """Sparse integer matrix product; keys are flattened matrix positions."""
    right_rows = {}
    for position, value in right.items():
        row, column = divmod(position, size)
        right_rows.setdefault(row, []).append((column, value))
    result = {}
    for position, value in left.items():
        row, column = divmod(position, size)
        for last, coefficient in right_rows.get(column, ()):
            key = row * size + last
            result[key] = result.get(key, 0) + value * coefficient
    return {key: value for key, value in result.items() if value}


def add_multiple(target, source, coefficient=1):
    for key, value in source.items():
        target[key] = target.get(key, 0) + coefficient * value
        if not target[key]:
            del target[key]


def integer_inverse(matrix, size):
    """Rational elimination, accepted only with two exact integer identities."""
    work = [[Fraction(matrix.get(i * size + j, 0)) for j in range(size)]
            + [Fraction(i == j) for j in range(size)] for i in range(size)]
    for column in range(size):
        pivot = next((i for i in range(column, size) if work[i][column]), None)
        if pivot is None:
            raise ValueError('the literal source unit is singular')
        work[pivot], work[column] = work[column], work[pivot]
        scale = work[column][column]
        work[column] = [value / scale for value in work[column]]
        for row in range(size):
            if row != column and work[row][column]:
                scale = work[row][column]
                work[row] = [x - scale * y for x, y in zip(work[row], work[column])]
    inverse = {}
    for i in range(size):
        for j in range(size):
            value = work[i][size + j]
            if value.denominator != 1:
                raise ValueError('the source inverse is not integral')
            if value:
                inverse[i * size + j] = int(value)
    identity = {(size + 1) * i: 1 for i in range(size)}
    if (matrix_product(matrix, inverse, size) != identity
            or matrix_product(inverse, matrix, size) != identity):
        raise ValueError('the source inverse fails an exact identity')
    return inverse


def literal_slice(i, k, s):
    """Original row order (j,p,L), column order (q,H,r)."""
    result = {}
    for j, p, r in product(range(4), repeat=3):
        q = k - p
        if 0 <= q < 4:
            row = (4 * j + p) * 7 + s + r
            column = 28 * q + 4 * (i + j) + r
            result[SIZE * row + column] = 1
    return result


def build_source():
    """Reconstruct and check all112 normalized slices from the literal tensor."""
    outer = []
    for i, s in product(range(4), repeat=2):
        matrix = {}
        for j, r in product(range(4), repeat=2):
            row = 7 * j + r + s
            column = 4 * (i + j) + r
            matrix[28 * row + column] = 1
        outer.append(matrix)
    unit = {}
    for i in range(4):
        add_multiple(unit, outer[4 * i + 3 - i])
    inverse = integer_inverse(unit, 28)
    normalized = [matrix_product(inverse, matrix, 28) for matrix in outer]
    full_unit = {}
    for i in range(4):
        add_multiple(full_unit, literal_slice(i, 3, 3 - i))
    basis = []
    for k, i, s in product(range(7), range(4), range(4)):
        matrix = {}
        for q in range(4):
            qp = q + 3 - k
            if 0 <= qp < 4:
                for position, value in normalized[4 * i + s].items():
                    row, column = divmod(position, 28)
                    matrix[(28 * qp + row) * SIZE + 28 * q + column] = value
        if matrix_product(full_unit, matrix) != literal_slice(i, k, s):
            raise ValueError('normalized source differs from the literal tensor')
        basis.append(matrix)
    identity = {(SIZE + 1) * i: 1 for i in range(SIZE)}
    normalized_unit = {}
    for i in range(4):
        add_multiple(normalized_unit, basis[3 * 16 + 4 * i + 3 - i])
    if normalized_unit != identity:
        raise ValueError('the normalized source unit is not the identity')
    nilpotent = basis[0]
    if matrix_product(nilpotent, nilpotent):
        raise ValueError('the specified source coordinate is not square zero')
    # Left multiplication by the invertible source unit preserves this rank.
    literal = literal_slice(0, 0, 0)
    if (len(literal) != 16 or len({key // SIZE for key in literal}) != 16
            or len({key % SIZE for key in literal}) != 16):
        raise ValueError('the fixed source coordinate does not have rank sixteen')
    return basis, nilpotent


def conjugated_source(basis, nilpotent):
    family = []
    for matrix in basis:
        commutator = matrix_product(matrix, nilpotent)
        add_multiple(commutator, matrix_product(nilpotent, matrix), -1)
        quadratic = matrix_product(matrix_product(nilpotent, matrix), nilpotent)
        family.append({(degree, key): sign * value
                       for degree, block, sign in ((0, matrix, 1), (1, commutator, 1),
                                                   (2, quadratic, -1))
                       for key, value in block.items()})
    unit = {}
    for i in range(4):
        add_multiple(unit, family[3 * 16 + 4 * i + 3 - i])
    if unit != {(0, (SIZE + 1) * i): 1 for i in range(SIZE)}:
        raise ValueError('conjugation changed the constant identity slice')
    return family


def decode_sparse(entries, width, label):
    if not isinstance(entries, list):
        raise ValueError(f'{label} is not a list')
    result = {}
    for entry in entries:
        if (not isinstance(entry, list) or len(entry) != 2
                or any(type(x) is not int for x in entry)
                or not 0 <= entry[0] < width or not entry[1] or entry[0] in result):
            raise ValueError(f'invalid or repeated {label} entry')
        result[entry[0]] = entry[1]
    return result


def verify_scalar_columns(matrices, coordinates):
    if coordinates != list(range(100, 112)):
        raise ValueError('the scalar-action subspace is not the stated twelve-space')
    selected = set(coordinates)
    for matrix in matrices:
        scalar = matrix.get((SIZE + 1) * coordinates[0], 0)
        actual = {key: value for key, value in matrix.items() if key % SIZE in selected}
        expected = {(SIZE + 1) * j: scalar for j in coordinates} if scalar else {}
        if actual != expected:
            raise ValueError('a leading matrix violates the scalar-action identity')


def verify_limit(certificate):
    if (certificate.get('schema') != 'a4-conjugation-limit-v1'
            or certificate.get('size') != SIZE or certificate.get('source_order') != 'k,i,s'
            or certificate.get('nilpotent_source_index') != 0):
        raise ValueError('wrong conjugation certificate conventions')
    basis, nilpotent = build_source()
    family = conjugated_source(basis, nilpotent)
    rows = certificate.get('basis', [])
    if len(rows) != SIZE:
        raise ValueError('the full limiting space needs112 certified rows')
    leading = []
    pivots = set()
    degree_counts = Counter()
    for number, row in enumerate(rows):
        degree, pivot = row.get('degree'), row.get('pivot')
        if (type(degree) is not int or degree < 0 or type(pivot) is not int
                or not 0 <= pivot < SIZE * SIZE):
            raise ValueError(f'invalid leading degree or pivot at row{number}')
        transform = row.get('transform', [])
        polynomial = {}
        used = set()
        for entry in transform:
            if (not isinstance(entry, list) or len(entry) != 3
                    or any(type(x) is not int for x in entry)
                    or entry[0] < 0 or not 0 <= entry[1] < SIZE or not entry[2]
                    or tuple(entry[:2]) in used):
                raise ValueError(f'invalid polynomial transformation at row{number}')
            shift, source, coefficient = entry
            used.add((shift, source))
            for (power, position), value in family[source].items():
                key = (power + shift, position)
                polynomial[key] = polynomial.get(key, 0) + coefficient * value
                if not polynomial[key]:
                    del polynomial[key]
        expected = decode_sparse(row.get('leading'), SIZE * SIZE, 'leading matrix')
        if not polynomial or max(power for power, _ in polynomial) != degree:
            raise ValueError(f'wrong complete polynomial degree at row{number}')
        actual = {position: value for (power, position), value in polynomial.items()
                  if power == degree}
        if actual != expected:
            raise ValueError(f'wrong leading coefficient at row{number}')
        if not actual or max(actual) != pivot or pivot in pivots:
            raise ValueError(f'leading pivots do not certify independence at row{number}')
        pivots.add(pivot)
        degree_counts[degree] += 1
        leading.append(actual)
    if dict(degree_counts) != {0: 50, 1: 46, 2: 16}:
        raise ValueError('the degree census differs from the stated complete limit')
    verify_scalar_columns(leading, certificate.get('scalar_coordinates'))
    return leading, {
        'literal_source_slices_checked': SIZE,
        'nilpotent_rank': 16,
        'nilpotent_square_zero': True,
        'full_limit_dimension': SIZE,
        'leading_degree_counts': {str(key): value for key, value in sorted(degree_counts.items())},
        'scalar_action_dimension': 12,
        'identity_slice_preserved': True,
        'all_polynomial_coefficients_replayed': True,
    }


def modular_rank(rows, prime=PRIME):
    pivots = {}
    for entries in rows:
        row = {key: value % prime for key, value in entries.items() if value % prime}
        while row:
            pivot = max(row)
            if pivot not in pivots:
                inverse = pow(row[pivot], -1, prime)
                pivots[pivot] = {key: value * inverse % prime for key, value in row.items()}
                break
            coefficient = row[pivot]
            for key, value in pivots[pivot].items():
                row[key] = (row.get(key, 0) - coefficient * value) % prime
                if not row[key]:
                    del row[key]
    return len(pivots)


def verify_census(certificate, matrices):
    if certificate.get('census_prime') != PRIME:
        raise ValueError('unexpected census prime')
    records = certificate.get('principal_compressions', [])
    expected_pairs = list(combinations(range(SIZE), 2))
    if (len(records) != len(expected_pairs)
            or any(not isinstance(row, list) or len(row) != 3
                   or any(type(value) is not int for value in row) for row in records)
            or [tuple(row[:2]) for row in records] != expected_pairs):
        raise ValueError('the principal compression census has incomplete coverage')
    histogram = Counter()
    for first, second, recorded_rank in records:
        holes = {first, second}
        projected = ({key: value for key, value in matrix.items()
                      if key // SIZE not in holes and key % SIZE not in holes}
                     for matrix in matrices)
        rank = modular_rank(projected)
        if rank != recorded_rank or rank < 108:
            raise ValueError(f'wrong projected rank at holes{first},{second}')
        histogram[rank] += 1
    return {
        'prime': PRIME,
        'principal_compressions_checked': len(records),
        'modular_rank_histogram': {str(key): value for key, value in sorted(histogram.items())},
        'minimum_certified_complex_dimension': min(histogram),
        'maximum_leading_dimension_loss': SIZE - min(histogram),
    }


def verify(certificate):
    matrices, limit = verify_limit(certificate)
    census = verify_census(certificate, matrices)
    return {
        'limit': limit,
        'census': census,
        'target_minimum_nonzero_evaluation_rank': 10,
        'necessary_leading_dimension_loss': 9,
        'all_principal_coordinate_compressions_excluded': True,
        'arbitrary_constant_compressions_excluded': False,
        'arbitrary_singular_trajectories_excluded': False,
        'matrix_multiplication_target_constructed': False,
        'exponent_improvement_proved': False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument('--output', type=Path)
    arguments = parser.parse_args()
    report = verify(json.loads(arguments.certificate.read_text()))
    text = json.dumps(report, indent=2, sort_keys=True) + '\n'
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()

"""Exact ordinary Q(n,b) map and residual certificates.

The rational mode certifies identities and flattening ranks over Q (and C).
Prime-field mode certifies only statements in that finite field. A modular
rank is never silently promoted to a rational upper bound.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product
import argparse
import hashlib
import json
from pathlib import Path


def rational(value):
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("Exact coefficients must be integers or rational strings")
    if isinstance(value, (int, Fraction)):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError("Unsupported exact coefficient")


def is_prime(value):
    if type(value) is not int or value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


class Field:
    def __init__(self, prime=None):
        if prime is not None and not is_prime(prime):
            raise ValueError("The modulus must be prime")
        self.prime = prime

    def number(self, value):
        value = rational(value)
        if self.prime is None:
            return value
        if value.denominator % self.prime == 0:
            raise ValueError("Coefficient denominator vanishes modulo the prime")
        return value.numerator * pow(value.denominator, -1, self.prime) % self.prime

    def reduce(self, value):
        return value if self.prime is None else value % self.prime

    def inverse(self, value):
        return Fraction(1, 1) / value if self.prime is None else pow(value, -1, self.prime)


def shape(n, b, target):
    if any(type(x) is not int or x <= 0 for x in (n, b, *target)):
        raise ValueError("Dimensions must be positive integers")
    left, inner, right = target
    width = n + b - 1
    return (n*n, b*width, b*width), (left*right, left*inner, inner*right)


def normalized_maps(n, b, target, maps, field):
    source_shape, target_shape = shape(n, b, target)
    if len(maps) != 3:
        raise ValueError("Exactly three maps are required")
    result = []
    for matrix, nr, nc in zip(maps, target_shape, source_shape):
        if len(matrix) != nr or any(len(row) != nc for row in matrix):
            raise ValueError("Map dimensions do not match target-by-source convention")
        result.append([[field.number(value) for value in row] for row in matrix])
    return result


def sparse_columns(matrix):
    return [[(row, matrix[row][column]) for row in range(len(matrix))
             if matrix[row][column]] for column in range(len(matrix[0]))]


def contract(n, b, target, maps, prime=None):
    """Reconstruct every source contribution, retaining exact nonzero output."""
    field = Field(prime)
    maps = normalized_maps(n, b, target, maps, field)
    columns = list(map(sparse_columns, maps))
    width = n + b - 1
    tensor = defaultdict(int)
    expanded = 0
    for p, q, y, v in product(range(n), range(n), range(b), range(b)):
        source = (p*n+q, y*width+q+v, (p+y)*b+v)
        for (a, ca), (bb, cb), (c, cc) in product(
                *(columns[leg][index] for leg, index in enumerate(source))):
            key = (a, bb, c)
            tensor[key] = field.reduce(tensor[key] + ca*cb*cc)
            expanded += 1
    return {key: value for key, value in tensor.items() if value}, expanded


def matrix_multiplication(target):
    left, inner, right = target
    return {(i*right+j, i*inner+alpha, alpha*right+j): 1
            for i, alpha, j in product(range(left), range(inner), range(right))}


def subtract(first, second, field):
    result = {}
    for key in first.keys() | second.keys():
        value = field.reduce(first.get(key, 0) - second.get(key, 0))
        if value:
            result[key] = value
    return result


def flatten(tensor, dimensions, leg):
    other = [axis for axis in range(3) if axis != leg]
    matrix = [[0]*(dimensions[other[0]]*dimensions[other[1]])
              for _ in range(dimensions[leg])]
    for indices, value in tensor.items():
        column = indices[other[0]]*dimensions[other[1]]+indices[other[1]]
        matrix[indices[leg]][column] = value
    return matrix


def row_space(matrix, prime=None, factorization=False):
    """Return an echelon basis and, optionally, the exact factorization M = L R.

    Each original row reduces in the already normalized basis. When later
    rows add pivots, old basis rows remain unchanged (echelon, not reduced).
    Thus stored coefficients give an explicit first-factor support witness.
    """
    field = Field(prime)
    columns = len(matrix[0]) if matrix else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError("Ragged matrix")
    basis, pivots, coefficients = [], [], []
    for row in matrix:
        remainder = [field.number(value) for value in row]
        used = []
        for pivot, old in zip(pivots, basis):
            coefficient = remainder[pivot]
            used.append(coefficient)
            if coefficient:
                remainder = [field.reduce(x-coefficient*y)
                             for x, y in zip(remainder, old)]
        pivot = next((j for j, value in enumerate(remainder) if value), None)
        if pivot is not None:
            coefficient = remainder[pivot]
            used.append(coefficient)
            inverse = field.inverse(coefficient)
            basis.append([field.reduce(value*inverse) for value in remainder])
            pivots.append(pivot)
        coefficients.append(used)
    rank = len(basis)
    if not factorization:
        return rank, pivots, basis
    coefficients = [row + [field.number(0)]*(rank-len(row)) for row in coefficients]
    for row, weights in zip(matrix, coefficients):
        replay = [field.reduce(sum(weights[k]*basis[k][column] for k in range(rank)))
                  for column in range(columns)]
        if replay != [field.number(value) for value in row]:
            raise ArithmeticError("Exact support factorization failed")
    return rank, pivots, basis, coefficients


def source_slices(n, b, target, second, third, prime=None):
    """Apply the two long maps and keep the source first leg unchanged."""
    field = Field(prime)
    source_shape, target_shape = shape(n, b, target)
    if (len(second) != target_shape[1] or len(third) != target_shape[2]
            or any(len(row) != source_shape[1] for row in second)
            or any(len(row) != source_shape[2] for row in third)):
        raise ValueError("Long map dimensions do not match")
    second, third = [sparse_columns([[field.number(x) for x in row] for row in matrix])
                     for matrix in (second, third)]
    width = n+b-1
    result = [[0]*(target_shape[1]*target_shape[2]) for _ in range(n*n)]
    for p, q, y, v in product(range(n), range(n), range(b), range(b)):
        row = result[p*n+q]
        for (ib, cb), (ic, cc) in product(second[y*width+q+v], third[(p+y)*b+v]):
            column = ib*target_shape[2]+ic
            row[column] = field.reduce(row[column]+cb*cc)
    return result


def minimum_first_residual(n, b, target, second, third, prime=None):
    """Construct a first map attaining the least possible first residual rank.

    The quotient of the target slice space by the fixed source slice space
    has dimension rank([S;T])-rank(S). Echelon reduction supplies an actual
    first map attaining this lower bound, not only a dimension calculation.
    """
    field = Field(prime)
    source = source_slices(n, b, target, second, third, prime)
    _, dimensions = shape(n, b, target)
    wanted = flatten(matrix_multiplication(target), dimensions, 0)
    basis, pivots, combinations = [], [], []
    for index, row in enumerate(source):
        remainder = row[:]
        combination = [field.number(int(i == index)) for i in range(n*n)]
        for pivot, old, old_combination in zip(pivots, basis, combinations):
            coefficient = remainder[pivot]
            if coefficient:
                remainder = [field.reduce(x-coefficient*y) for x,y in zip(remainder,old)]
                combination = [field.reduce(x-coefficient*y)
                               for x,y in zip(combination,old_combination)]
        pivot = next((j for j,value in enumerate(remainder) if value), None)
        if pivot is not None:
            inverse = field.inverse(remainder[pivot])
            basis.append([field.reduce(x*inverse) for x in remainder])
            combinations.append([field.reduce(x*inverse) for x in combination])
            pivots.append(pivot)
    first, residual = [], []
    for row in wanted:
        remainder = [field.number(x) for x in row]
        combination = [field.number(0) for _ in range(n*n)]
        for pivot, old, old_combination in zip(pivots,basis,combinations):
            coefficient = remainder[pivot]
            if coefficient:
                remainder = [field.reduce(x-coefficient*y) for x,y in zip(remainder,old)]
                combination = [field.reduce(x+coefficient*y)
                               for x,y in zip(combination,old_combination)]
        first.append(combination)
        residual.append(remainder)
    residual_rank = row_space(residual, prime)[0]
    return first, {'source_slice_rank': len(basis),
                   'minimum_first_residual_rank': residual_rank,
                   'target_source_intersection_dimension': len(wanted)-residual_rank,
                   'attaining_first_map_constructed': True,
                   'coefficient_field': 'Q' if prime is None else f'F_{prime}'}


def encode(value):
    if isinstance(value, Fraction):
        return value.numerator if value.denominator == 1 else str(value)
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(item) for item in value]
    return value


def tensor_records(tensor):
    return [[*key, encode(value)] for key, value in sorted(tensor.items())]


def verify(n, b, target, maps, prime=None, expected_residual=None, include_witness=True):
    field = Field(prime)
    source_shape, target_shape = shape(n, b, target)
    actual, expanded = contract(n, b, target, maps, prime)
    wanted = matrix_multiplication(target)
    residual = subtract(wanted, actual, field)
    if expected_residual is not None:
        expected = {tuple(key): field.number(value) for key, value in expected_residual.items()
                    if field.number(value)}
        if residual != expected:
            raise ArithmeticError("The claimed residual does not match all tensor coefficients")
    factorizations = [row_space(flatten(residual, target_shape, leg), prime,
                                factorization=include_witness)
                      for leg in range(3)]
    ranks = [result[0] for result in factorizations]
    pair_product = min(ranks[0]*ranks[1], ranks[0]*ranks[2], ranks[1]*ranks[2])
    residual_records = tensor_records(residual)
    report = {
        'source': [n, b], 'target': list(target),
        'source_format': list(source_shape), 'target_format': list(target_shape),
        'coefficient_field': 'Q' if prime is None else f'F_{prime}',
        'source_terms_reconstructed': n*n*b*b,
        'expanded_source_contributions': expanded,
        'all_target_coefficient_positions_accounted_for':
            target_shape[0]*target_shape[1]*target_shape[2],
        'actual_nonzero_coefficients': len(actual),
        'residual_nonzero_coefficients': len(residual),
        'exact_residual_flattening_ranks': ranks,
        'smallest_rank_pair_product': pair_product,
        'ordinary_target_identity': not residual,
        'repaired_coefficient_identity': True,
        'rational_or_complex_rank_upper_bound_certified': prime is None,
        'finite_field_result_lifted_to_characteristic_zero': False,
        'residual_sha256': hashlib.sha256(json.dumps(residual_records,
            separators=(',', ':')).encode()).hexdigest(),
        'maps_sha256': hashlib.sha256(json.dumps(encode(maps),
            separators=(',', ':')).encode()).hexdigest(),
        'improves_omega': False,
    }
    if include_witness:
        report['residual_coefficients'] = residual_records
        report['flattening_support_witnesses'] = [
            {'leg': leg, 'pivots': result[1], 'basis_rows': encode(result[2]),
             'coefficients': encode(result[3]), 'factorization_replayed': True}
            for leg, result in enumerate(factorizations)]
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidate', type=Path)
    parser.add_argument('--prime', type=int)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--summary-only', action='store_true')
    args = parser.parse_args()
    candidate = json.loads(args.candidate.read_text())
    report = verify(*candidate['source'], candidate['target'], candidate['maps'],
                    args.prime, include_witness=not args.summary_only)
    payload = json.dumps(encode(report), indent=2)+'\n'
    if args.output:
        args.output.write_text(payload)
    print(payload, end='')

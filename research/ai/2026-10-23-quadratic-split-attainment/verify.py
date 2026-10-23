"""Exact split/doubled recurrence and full rectangular source controls.

All matrices are constructed here; no other research verifier is imported.
The finite controls accompany, and do not replace, the all-size written proof.
"""
import argparse
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


class Field:
    def __init__(self, name, characteristic, extension=False):
        self.name = name
        self.characteristic = characteristic
        self.extension = extension

    def integer(self, value):
        return value % self.characteristic if self.characteristic else Fraction(value)

    def element(self, value):
        if self.extension:
            if value not in range(4):
                raise ValueError('F4 elements must use encodings 0,1,2,3')
            return value
        return self.integer(value)

    def add(self, left, right):
        if self.extension:
            return left ^ right
        return self.integer(left + right)

    def neg(self, value):
        return value if self.extension else self.integer(-value)

    def sub(self, left, right):
        return self.add(left, self.neg(right))

    def mul(self, left, right):
        if self.extension:
            return ((0, 0, 0, 0), (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2))[left][right]
        return self.integer(left * right)

    def power(self, value, exponent):
        result = self.integer(1)
        for _ in range(exponent):
            result = self.mul(result, value)
        return result

    def inverse(self, value):
        if not value:
            raise ZeroDivisionError('zero has no field inverse')
        if self.extension:
            return (0, 1, 3, 2)[value]
        if self.characteristic:
            return pow(value, -1, self.characteristic)
        return Fraction(1) / value

    def encode(self, value):
        if isinstance(value, Fraction):
            return value.numerator if value.denominator == 1 else str(value)
        return value


FIELDS = {field.name: field for field in
          (Field('Q', 0), Field('F2', 2), Field('F3', 3), Field('F5', 5), Field('F4', 2, True))}
CASES = {
    'Q': [(-1, 3), (-1, 4), (-1, 5), (1, 3), (1, 4), (2, 3), (2, 4)],
    'F2': [(1, 3), (1, 4), (1, 5), (1, 8)],
    'F3': [(1, 4), (1, 5), (2, 3), (2, 4)],
    'F5': [(1, 3), (1, 4), (2, 3), (2, 4), (4, 4), (4, 5)],
    'F4': [(1, 3), (1, 4), (1, 8), (2, 4), (2, 5), (2, 8), (3, 3), (3, 5)],
}


def nonzero_parameter(field, parameter):
    parameter = field.element(parameter)
    if not parameter:
        raise ValueError('t=0 lowers the primitive degree and is excluded')
    return parameter


def split_triple(field, parameter):
    parameter = nonzero_parameter(field, parameter)
    return [[0, 0, parameter], [0, field.neg(field.add(1, parameter))], [field.integer(1)]]


def source_matrix(a, b, triple):
    """Full rows (j,L), columns (H,r), with every endpoint retained."""
    def coefficient(x_degree, z_degree):
        if 0 <= z_degree < 3 and 0 <= x_degree < len(triple[z_degree]):
            return triple[z_degree][x_degree]
        return 0
    return [[coefficient(H - j, L - r)
             for H in range(a + b - 1) for r in range(a)]
            for j in range(b) for L in range(a + b - 1)]


def recurrence_matrix(a, triple):
    """Degree at most a-1 coordinates, all equations through x-degree a+1."""
    return [[triple[L - r][k - j]
             if 0 <= L - r < 3 and 0 <= k - j < len(triple[L - r]) else 0
             for L in range(a + 2) for j in range(a)]
            for r in range(a) for k in range(a + 2)]


def rank(matrix, field):
    matrix = [list(row) for row in matrix]
    position = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(position, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[position], matrix[pivot] = matrix[pivot], matrix[position]
        inverse = field.inverse(matrix[position][column])
        active = [(index, field.mul(value, inverse))
                  for index, value in enumerate(matrix[position]) if value]
        for index, value in active:
            matrix[position][index] = value
        for row in matrix[position + 1:]:
            factor = row[column]
            if factor:
                for index, value in active:
                    row[index] = field.sub(row[index], field.mul(factor, value))
        position += 1
        if position == len(matrix):
            break
    return position


def predicted_nullity(a, field, parameter):
    if a < 3:
        raise ValueError('degree-two source formulas require a>=3')
    parameter = nonzero_parameter(field, parameter)
    if parameter == 1:
        return int(field.characteristic > 0 and (a + 1) % field.characteristic == 0)
    return int(field.power(parameter, a + 1) == 1)


def predicted_rank(a, b, field, parameter):
    if b < 3:
        raise ValueError('degree-two source formulas require b>=3')
    epsilon = predicted_nullity(a, field, parameter)
    return a * b + 2 * min(a, b) - epsilon * int(a == b)


def geometric_sums(field, parameter, n):
    result, power = [field.integer(0)], field.integer(1)
    for _ in range(n):
        result.append(field.add(result[-1], power))
        power = field.mul(power, parameter)
    return result


def kernel_witness(a, field, parameter):
    if not predicted_nullity(a, field, parameter):
        raise ValueError('this parameter and size have zero recurrence kernel')
    sums = geometric_sums(field, nonzero_parameter(field, parameter), a + 1)
    return [[]] + [[0] * (r - 1) + [sums[r]] if sums[r] else [] for r in range(1, a + 2)]


def check_kernel(a, triple, polynomials, field):
    """Check polynomial convolution directly, without the recurrence constructor."""
    if len(polynomials) != a + 2 or any(len(poly) > a for poly in polynomials):
        raise ArithmeticError('kernel witness has invalid coordinate degrees')
    if not any(any(poly) for poly in polynomials):
        raise ArithmeticError('kernel witness must be nonzero')
    for r in range(a):
        residual = [field.integer(0)] * (a + 2)
        for offset, coefficient in enumerate(triple):
            for i, left in enumerate(coefficient):
                for j, right in enumerate(polynomials[r + offset]):
                    residual[i + j] = field.add(residual[i + j], field.mul(left, right))
        if any(residual):
            raise ArithmeticError('kernel witness fails the polynomial recurrence')


def control(field, parameter, a):
    triple = split_triple(field, parameter)
    epsilon = predicted_nullity(a, field, parameter)
    recurrence_rank = rank(recurrence_matrix(a, triple), field)
    if a * (a + 2) - recurrence_rank != epsilon:
        raise ArithmeticError('exact recurrence nullity disagrees with the formula')
    record = {'field': field.name, 'parameter': parameter, 'a': a, 'n': a + 1,
              'branch': 'doubled' if parameter == 1 else 'distinct',
              'epsilon': epsilon, 'recurrence_size': a * (a + 2),
              'recurrence_rank': recurrence_rank, 'source_controls': []}
    if epsilon:
        witness = kernel_witness(a, field, parameter)
        check_kernel(a, triple, witness, field)
        record['kernel_polynomials'] = [[field.encode(value) for value in poly] for poly in witness]
    for b in (a - 1, a, a + 1):
        if b < 3:
            continue
        matrix = source_matrix(a, b, triple)
        source_rank = rank(matrix, field)
        if source_rank != predicted_rank(a, b, field, parameter):
            raise ArithmeticError('literal source rank disagrees with rectangular formula')
        record['source_controls'].append({'b': b, 'rows': len(matrix), 'columns': len(matrix[0]),
                                          'literal_rank': source_rank})
    return record


def small_auxiliary_control(field, parameter, n):
    """The n=2,3 recurrence lemma only; no literal source claim is made."""
    a = n - 1
    triple = split_triple(field, parameter)
    sums = geometric_sums(field, field.element(parameter), n)
    epsilon = int(not sums[n])
    recurrence_rank = rank(recurrence_matrix(a, triple), field)
    if n * n - 1 - recurrence_rank != epsilon:
        raise ArithmeticError('small auxiliary recurrence disagrees with the lemma')
    record = {'field': field.name, 'parameter': parameter, 'n': n,
              'recurrence_size': n * n - 1, 'recurrence_rank': recurrence_rank,
              'epsilon': epsilon}
    if epsilon:
        witness = [[]] + [[0] * (r - 1) + [sums[r]] if sums[r] else [] for r in range(1, n + 1)]
        check_kernel(a, triple, witness, field)
        record['kernel_polynomials'] = [[field.encode(value) for value in poly] for poly in witness]
    return record


def report():
    controls = [control(FIELDS[name], parameter, a)
                for name, cases in CASES.items() for parameter, a in cases]
    auxiliary = [small_auxiliary_control(FIELDS[name], parameter, n)
                 for name, cases in CASES.items()
                 for parameter in dict.fromkeys(parameter for parameter, _ in cases)
                 for n in (2, 3)]
    zero_controls = []
    for field in FIELDS.values():
        # Construct the excluded lower-degree polynomial directly, without
        # passing t=0 through the theorem's deliberately restricted entry point.
        triple = [[], [0, field.neg(field.integer(1))], [field.integer(1)]]
        source_rank = rank(source_matrix(3, 3, triple), field)
        if source_rank != 12:
            raise ArithmeticError('excluded zero-parameter boundary changed rank stratum')
        zero_controls.append({'field': field.name, 'a': 3, 'b': 3, 'literal_rank': source_rank})
    return {'scope': 'Exact finite controls for the all-size written split/doubled proof; '
                     'literal degree-two source claims require a,b>=3 and t nonzero.',
            'field_extension': 'F4=F2[alpha]/(alpha^2+alpha+1); 0,1,2,3 encode 0,1,alpha,alpha+1',
            'matrix_convention': 'rows (j,L), columns (H,r), entry [x^(H-j)z^(L-r)]f',
            'recurrence_controls': len(controls),
            'source_controls': sum(len(record['source_controls']) for record in controls),
            'kernel_witnesses': sum(record['epsilon'] for record in controls),
            'field_case_counts': dict(Counter(record['field'] for record in controls)),
            'small_auxiliary_scope': 'n=2,3 recurrence lemma only; no source-rank claims at a=1,2',
            'small_auxiliary_controls': auxiliary,
            'small_auxiliary_kernel_witnesses': sum(record['epsilon'] for record in auxiliary),
            'controls': controls, 'excluded_zero_parameter_controls': zero_controls,
            'independent_review': False, 'improves_omega': False}


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

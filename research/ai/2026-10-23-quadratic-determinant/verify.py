"""Bounded exact verification of the universal quadratic determinant identity.

The universal assertion uses the written invariant/normal-form proof. Here the
15x15 determinant is evaluated numerically over Q or finite fields; symbolic
determinants are limited to three-variable Edwards blocks of sizes eight and
seven and the three-by-three invariant matrices.
"""
import argparse
from fractions import Fraction
import json
from math import lcm
from pathlib import Path
import random

import sympy as sp


J = sp.Matrix([[0, 0, -2], [0, 1, 0], [-2, 0, 0]])
B_INVERSE = sp.Matrix([[0, 0, 1], [0, -sp.Rational(1, 2), 0], [1, 0, 0]])
THREE_SPACE_MASKS = (84, 174, 311)


def literal_source(matrix):
    """M rows are x-degrees, columns z-degrees; source rows (j,L), columns (H,r)."""
    return [[matrix[H - j][L - r] if 0 <= H - j <= 2 and 0 <= L - r <= 2 else 0
             for H in range(5) for r in range(3)]
            for j in range(3) for L in range(5)]


def determinant_fraction(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    result = Fraction(1)
    for column in range(len(rows)):
        pivot = next((r for r in range(column, len(rows)) if rows[r][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[pivot], rows[column] = rows[column], rows[pivot]
            result = -result
        value = rows[column][column]
        result *= value
        for row in rows[column + 1:]:
            factor = row[column] / value
            if factor:
                for j in range(column + 1, len(rows)):
                    row[j] -= factor * rows[column][j]
                row[column] = 0
    return result


def determinant_modulo(matrix, prime):
    rows = [[int(value) % prime for value in row] for row in matrix]
    result = 1
    for column in range(len(rows)):
        pivot = next((r for r in range(column, len(rows)) if rows[r][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            rows[pivot], rows[column] = rows[column], rows[pivot]
            result = -result % prime
        value = rows[column][column]
        result = result * value % prime
        inverse = pow(value, -1, prime)
        for row in rows[column + 1:]:
            factor = row[column] * inverse % prime
            if factor:
                for j in range(column + 1, len(rows)):
                    row[j] = (row[j] - factor * rows[column][j]) % prime
                row[column] = 0
    return result


def q_matrix(matrix):
    adjugate = matrix.adjugate()
    return 2 * adjugate - sp.trace(adjugate) * sp.eye(3)


def invariant_values(matrix):
    coefficient = sp.Matrix(matrix)
    h = coefficient.T * J * coefficient * J
    h0 = B_INVERSE * coefficient.T * B_INVERSE * coefficient
    det_m, det_q = coefficient.det(), q_matrix(h).det()
    s1, s2, s3 = sp.trace(h), sp.trace(h.adjugate()), h.det()
    scalar = s2 ** 3 - 4 * s1 * s2 * s3 + 8 * s3 ** 2
    if sp.expand(det_q - scalar) != 0:
        raise ArithmeticError('adjugate determinant disagrees with scalar invariant')
    return {'det_M': det_m, 'cleared_rhs': det_m * det_q,
            'alternate_det_R': 2 * det_m * q_matrix(h0).det()}


def rational_cases():
    cases = [
        ('zero', [[0] * 3 for _ in range(3)]),
        ('identity', [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
        ('edwards', [[3, 0, 1], [0, 2, 0], [1, 0, 3]]),
        ('rank_two', [[1, 2, 3], [4, 5, 6], [5, 7, 9]]),
        ('sparse_full_source', [[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
    ]
    generator = random.Random(20261023)
    for sample in range(24):
        matrix = [[Fraction(generator.randrange(-7, 8), generator.randrange(1, 6))
                   for _ in range(3)] for _ in range(3)]
        cases.append((f'rational_{sample:02}', matrix))
    return cases


def rational_control(label, matrix):
    determinant = determinant_fraction(literal_source(matrix))
    values = invariant_values([[sp.Rational(value) for value in row] for row in matrix])
    if 2048 * sp.Rational(determinant) != values['cleared_rhs']:
        raise ArithmeticError('cleared determinant identity failed')
    if sp.Rational(determinant) != values['alternate_det_R']:
        raise ArithmeticError('alternate normalization failed')
    return {'label': label, 'M': [[str(value) for value in row] for row in matrix],
            'det_R': str(determinant), **{key: str(value) for key, value in values.items()}}


def rational_modulo(value, prime):
    numerator, denominator = sp.fraction(value)
    return int(numerator) * pow(int(denominator), -1, prime) % prime


def prime_control(label, matrix, prime):
    reduced = [[value % prime for value in row] for row in matrix]
    determinant = determinant_modulo(literal_source(reduced), prime)
    values = invariant_values(reduced)
    right = rational_modulo(values['cleared_rhs'], prime)
    if (2048 * determinant - right) % prime:
        raise ArithmeticError('odd-prime cleared identity failed')
    if rational_modulo(values['alternate_det_R'], prime) != determinant:
        raise ArithmeticError('odd-prime alternate normalization failed')
    return {'label': label, 'prime': prime, 'M': reduced, 'det_R_mod_prime': determinant,
            'cleared_rhs_mod_prime': right,
            'alternate_det_R_mod_prime': rational_modulo(values['alternate_det_R'], prime)}


def inversion_count(permutation):
    return sum(left > right for i, left in enumerate(permutation) for right in permutation[i + 1:])


def edwards_symbolic_control():
    a, b, c = sp.symbols('A B C')
    coefficient = [[a, 0, b], [0, c, 0], [b, 0, a]]
    source = sp.Matrix(literal_source(coefficient))
    row_pairs = [(j, L) for j in range(3) for L in range(5)]
    column_pairs = [(H, r) for H in range(5) for r in range(3)]
    rows = [[i for i, pair in enumerate(row_pairs) if sum(pair) % 2 == parity] for parity in (0, 1)]
    columns = [[i for i, pair in enumerate(column_pairs) if sum(pair) % 2 == parity] for parity in (0, 1)]
    if any(source[i, j] for parity in (0, 1) for i in rows[parity] for j in columns[1 - parity]):
        raise ArithmeticError('Edwards source has a nonzero off-parity block')
    inversions = [inversion_count(rows[0] + rows[1]), inversion_count(columns[0] + columns[1])]
    if inversions != [28, 28]:
        raise ArithmeticError('parity permutation sign changed')
    even = sp.expand(source.extract(rows[0], columns[0]).det(method='domain-ge'))
    odd = sp.expand(source.extract(rows[1], columns[1]).det(method='domain-ge'))
    delta = (a * a - b * b) ** 2
    expected_even = -(delta - a * b * c * c) * (delta + a * b * c * c)
    expected_odd = -c * (a * a - b * b) * (2 * delta - (a * a + b * b) * c * c)
    if sp.expand(even - expected_even) != 0 or sp.expand(odd - expected_odd) != 0:
        raise ArithmeticError('symbolic Edwards block determinant changed')
    values = invariant_values(coefficient)
    product = sp.expand(even * odd)
    if sp.expand(2048 * product - values['cleared_rhs']) != 0:
        raise ArithmeticError('symbolic Edwards cleared identity failed')
    if sp.expand(product - values['alternate_det_R']) != 0:
        raise ArithmeticError('symbolic Edwards alternate normalization failed')
    return {'variables': ['A', 'B', 'C'], 'block_sizes': [len(rows[0]), len(rows[1])],
            'row_column_permutation_inversions': inversions,
            'even_block_determinant': str(even), 'odd_block_determinant': str(odd),
            'det_R_from_block_product': str(product),
            'cleared_identity_verified': True, 'alternate_normalization_verified': True}


def characteristic_two_control():
    matrix = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]  # x^2+xz+z^2
    determinant = determinant_modulo(literal_source(matrix), 2)
    right = rational_modulo(invariant_values(matrix)['cleared_rhs'], 2)
    if determinant != 1 or right != 0:
        raise ArithmeticError('characteristic-two degeneration witness changed')
    return {'M': matrix, 'biform': 'x^2+x*z+z^2', 'det_R_mod_two': determinant,
            'literal_rank_mod_two': 15, 'cleared_left_mod_two': (2048 * determinant) % 2,
            'cleared_right_mod_two': right, 'cleared_identity_is_rank_criterion': False}


def rational_three_space_control(parameters):
    parameters = [Fraction(value) for value in parameters]
    if not any(parameters):
        raise ValueError('three-space combination must be nonzero')
    denominator = lcm(*(value.denominator for value in parameters))
    normalized = [int(value * denominator) for value in parameters]
    power_two = 1
    while all(value % 2 == 0 for value in normalized):
        normalized = [value // 2 for value in normalized]
        power_two *= 2
    basis = [[[mask >> (3 * s + i) & 1 for s in range(3)] for i in range(3)]
             for mask in THREE_SPACE_MASKS]
    matrix = [[sum(value * basis[k][i][s] for k, value in enumerate(parameters))
               for s in range(3)] for i in range(3)]
    integer_matrix = [[sum(value * basis[k][i][s] for k, value in enumerate(normalized))
                       for s in range(3)] for i in range(3)]
    control = rational_control('rational_full_rank_three_space', matrix)
    normalized_determinant = Fraction(control['det_R']) * Fraction(denominator, power_two) ** 15
    modular_determinant = determinant_modulo(literal_source(integer_matrix), 2)
    if normalized_determinant.denominator != 1 or normalized_determinant.numerator % 2 != 1:
        raise ArithmeticError('normalized three-space source determinant is not odd')
    if modular_determinant != 1:
        raise ArithmeticError('three-space reduction is not full rank')
    mask = sum((integer_matrix[i][s] % 2) << (3 * s + i) for i in range(3) for s in range(3))
    return {**control, 'parameters': [str(value) for value in parameters],
            'denominator_multiplier': denominator, 'removed_common_power_two': power_two,
            'normalized_parameters': normalized, 'normalized_M': integer_matrix,
            'normalized_det_R': str(normalized_determinant),
            'normalized_det_R_mod_two': modular_determinant, 'reduction_mask': mask}


def cross_matrix(vector):
    x, y, z = vector
    return sp.Matrix([[0, -z, y], [z, 0, -x], [-y, x, 0]])


def determinant_jet(coefficient, direction):
    """Direct numerator expansion of det(2H^-1-tr(H^-1)I), H=N^tN.

    Only a one-variable three-by-three determinant is expanded. No gradient
    or curvature formula is used to obtain these coefficients.
    """
    t = sp.Symbol('t')
    varied = coefficient + t * direction
    h = varied.T * varied
    numerator = sp.Poly(q_matrix(h).det(method='domain-ge'), t)
    return [numerator.nth(degree) for degree in range(3)]


def curvature_control(label, coefficient, prime=None):
    if prime == 2:
        raise ValueError('curvature certificate requires characteristic different from two')
    scalar = (lambda value: rational_modulo(value, prime)) if prime else sp.cancel
    reduce = lambda matrix: matrix.applyfunc(scalar)
    n = reduce(sp.Matrix(coefficient))
    h = reduce(n.T * n)
    q = h.inv_mod(prime) if prime else h.inv()
    s = reduce(2 * q - sp.trace(q) * sp.eye(3))
    u = reduce(s.adjugate())
    tau = scalar(sp.trace(u))
    if scalar(s.det()) != 0 or u == sp.zeros(3) or tau == 0:
        raise ArithmeticError('curvature point must have rank-two S with nonzero adjugate trace')
    if scalar(8 * q.det() - sp.trace(q) * tau) != 0 or reduce(s * u) != sp.zeros(3):
        raise ArithmeticError('rank-two adjugate identity failed')
    g = reduce(-q * (2 * u - tau * sp.eye(3)) * q)
    a = reduce(n * g * n.T)
    if scalar(g.det()) == 0 or scalar(a.det()) == 0 or scalar(sp.trace(h * g)) != 0:
        raise ArithmeticError('curvature gradient must be invertible and trace-orthogonal to H')
    if scalar(sp.trace(a)) != 0:
        raise ArithmeticError('ternary curvature matrix must have trace zero')
    denominator = scalar(h.det() ** 3)
    divide = lambda value: scalar(value / denominator) if prime is None else scalar(value * pow(int(denominator), -1, prime))
    gradient = sp.zeros(3)
    for i in range(3):
        for j in range(3):
            direction = sp.zeros(3)
            direction[i, j] = 1
            constant, first, _ = determinant_jet(n, direction)
            if scalar(constant) != 0:
                raise ArithmeticError('direct determinant numerator is nonzero at curvature point')
            gradient[i, j] = divide(first)
    if gradient != reduce(2 * n * g):
        raise ArithmeticError('direct determinant gradient disagrees with adjugate formula')
    directions = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
    second = []
    for vector in directions:
        _, first, quadratic = determinant_jet(n, cross_matrix(vector) * n)
        if scalar(first) != 0:
            raise ArithmeticError('vertical first derivative must vanish')
        second.append(divide(2 * quadratic))
    hessian = sp.diag(*second[:3])
    half = sp.Rational(1, 2) if prime is None else pow(2, -1, prime)
    for value, (i, j) in zip(second[3:], ((0, 1), (0, 2), (1, 2))):
        hessian[i, j] = hessian[j, i] = scalar((value - second[i] - second[j]) * half)
    if hessian != reduce(-2 * a) or scalar(hessian.det()) == 0:
        raise ArithmeticError('direct vertical Hessian disagrees with nondegenerate negative-two A')
    matrices = {'N': n, 'H': h, 'Q': q, 'S': s, 'adjugate_S': u,
                'gradient_H': g, 'gradient_N': gradient, 'A': a, 'vertical_Hessian': hessian}
    return {'label': label, 'prime': prime, 'adjugate_trace': str(tau),
            'gradient_direction_count': 9, 'vertical_direction_count': 6,
            'det_vertical_Hessian': str(scalar(hessian.det())),
            **{key: [[str(value) for value in row] for row in matrix.tolist()]
               for key, matrix in matrices.items()}}


def curvature_controls():
    diagonal = sp.diag(12, 15, 20)
    left = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5), 0],
                      [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])
    right = sp.Matrix([[1, 0, 0], [0, sp.Rational(3, 5), -sp.Rational(4, 5)],
                       [0, sp.Rational(4, 5), sp.Rational(3, 5)]])
    return [curvature_control('rational_diagonal', diagonal),
            curvature_control('rational_orthogonal_changes', left * diagonal * right),
            curvature_control('F3_irreducible_complement', [[1, 0, 1], [1, 0, -1], [0, 1, 1]], 3),
            curvature_control('F5_nondiagonalizable_Gram', [[1, 0, 0], [0, 1, 0], [0, 2, -2]], 5),
            curvature_control('F7_diagonal', sp.diag(3, 2, 2), 7)]


def report():
    cases = rational_cases()
    rational = [rational_control(label, matrix) for label, matrix in cases]
    prime_cases = cases[:5] + [('invariant_factor_zero_mod_seven', [[1, 0, 0], [0, 3, 0], [0, 0, 1]])]
    primes = [prime_control(label, matrix, prime) for prime in (3, 5, 7) for label, matrix in prime_cases]
    three_space = [rational_three_space_control(parameters) for parameters in
                   ((1, 1, 0), (Fraction(1, 2), Fraction(1, 3), Fraction(1, 5)), (2, 4, 6))]
    curvature = curvature_controls()
    return {'scope': 'Finite exact controls plus a three-variable symbolic Edwards computation. '
                     'The universal integer identity uses the written invariant/normal-form proof.',
            'coefficient_convention': 'M[i,s] is the coefficient of x^i*z^s',
            'literal_source_convention': 'rows (j,L), columns (H,r), entry M[H-j,L-r]',
            'rational_seed': 20261023, 'rational_matrix_count': len(rational),
            'rational_controls': rational, 'odd_prime_matrix_count': len(primes),
            'odd_prime_controls': primes, 'edwards_symbolic': edwards_symbolic_control(),
            'characteristic_two_boundary': characteristic_two_control(),
            'rational_three_space_basis_masks': list(THREE_SPACE_MASKS),
            'rational_three_space_count': len(three_space), 'rational_three_space_controls': three_space,
            'curvature_certificate_count': len(curvature), 'curvature_certificates': curvature,
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

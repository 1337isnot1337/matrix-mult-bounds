"""Exact finite controls for quadratic recurrence kernel indices.

Literal source matrices and polynomial recurrence matrices are constructed
separately. Finite comparisons support, but do not prove, the written theorem.
"""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
import random


def echelon(rows, prime):
    """Sparse exact elimination over Q (prime=None) or a prime field."""
    pivots = {}
    for source in rows:
        row = {i: Fraction(value) if prime is None else value % prime
               for i, value in enumerate(source)
               if value and (prime is None or value % prime)}
        while row:
            column = min(row)
            if column not in pivots:
                inverse = (1 / row[column] if prime is None else
                           pow(row[column], -1, prime))
                pivots[column] = {
                    i: value * inverse if prime is None else value * inverse % prime
                    for i, value in row.items()}
                break
            coefficient = row[column]
            for i, value in pivots[column].items():
                updated = row.get(i, 0) - coefficient * value
                if prime is not None:
                    updated %= prime
                if updated:
                    row[i] = updated
                else:
                    row.pop(i, None)
    return pivots


def rank(rows, prime):
    return len(echelon(rows, prime))


def kernel_vector(rows, prime):
    pivots = echelon(rows, prime)
    width = len(rows[0])
    free = next((i for i in range(width) if i not in pivots), None)
    if free is None:
        raise ArithmeticError('coefficient matrix has no kernel')
    vector = [0] * width
    vector[free] = 1
    for column in sorted(pivots, reverse=True):
        value = -sum(value * vector[i] for i, value in pivots[column].items()
                     if i != column)
        vector[column] = value if prime is None else value % prime
    return vector


def polynomial(coefficients, prime):
    result = [Fraction(value) if prime is None else value % prime
              for value in coefficients]
    while result and not result[-1]:
        result.pop()
    return result


def divide(numerator, denominator, prime):
    remainder = polynomial(numerator, prime)
    denominator = polynomial(denominator, prime)
    if not denominator:
        raise ValueError('polynomial divisor is zero')
    quotient = [0] * max(0, len(remainder) - len(denominator) + 1)
    inverse = (1 / denominator[-1] if prime is None else
               pow(denominator[-1], -1, prime))
    while len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        value = remainder[-1] * inverse
        if prime is not None:
            value %= prime
        quotient[shift] = value
        for i, coefficient in enumerate(denominator):
            remainder[shift + i] -= value * coefficient
        remainder = polynomial(remainder, prime)
    return polynomial(quotient, prime), remainder


def primitive_triple(triple, prime):
    if len(triple) != 3:
        raise ValueError('exactly three polynomials are required')
    triple = [polynomial(item, prime) for item in triple]
    gcd = []
    for item in triple:
        left, right = gcd, item
        while right:
            left, right = right, divide(left, right, prime)[1]
        gcd = left
    if not gcd:
        raise ValueError('the polynomial triple must be nonzero')
    inverse = 1 / gcd[-1] if prime is None else pow(gcd[-1], -1, prime)
    gcd = polynomial([value * inverse for value in gcd], prime)
    primitive = []
    for item in triple:
        quotient, remainder = divide(item, gcd, prime)
        if remainder:
            raise ArithmeticError('gcd does not divide the triple')
        primitive.append(quotient)
    return primitive, gcd


def multiply(left, right, prime):
    if not left or not right:
        return []
    result = [0] * (len(left) + len(right) - 1)
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            result[i + j] += value * other
    return polynomial(result, prime)


def polynomial_matrix_coefficients(matrix, degree):
    """All coefficients of a polynomial matrix times a degree-bounded vector."""
    output_length = max(len(item) for row in matrix for item in row) + degree
    width = len(matrix[0]) * (degree + 1)
    rows = [[0] * width for _ in range(len(matrix) * output_length)]
    for r, row in enumerate(matrix):
        for c, entry in enumerate(row):
            for power, value in enumerate(entry):
                for j in range(degree + 1):
                    rows[r * output_length + power + j][c * (degree + 1) + j] += value
    return rows


def inspect_kernel(a, triple, prime, result=None):
    """Extract a minimum-degree vector and inspect its actual Hankel kernels."""
    if result is None:
        result = minimal_indices(a, triple, prime)
    primitive, _ = primitive_triple(triple, prime)
    degree, delta = result['primitive_degree'], result['minimal_indices'][0]
    if degree == 0:
        raise ValueError('structural inspection requires positive primitive degree')
    matrix = recurrence_matrix(a, primitive, delta)
    vector = kernel_vector(matrix, prime)
    residual = [sum(value * coefficient for value, coefficient in zip(row, vector))
                for row in matrix]
    if any(value if prime is None else value % prime for value in residual):
        raise ArithmeticError('kernel witness fails the recurrence')
    sequence = [polynomial(vector[j * (delta + 1):(j + 1) * (delta + 1)], prime)
                for j in range(a + 2)]
    if max(map(len, sequence)) != delta + 1:
        raise ArithmeticError('kernel witness has the wrong degree')
    hankel = [sequence[r:r + 3] for r in range(a)]
    # The verified nonzero right-kernel triple bounds this rank by two.
    hankel_rank = 1 + any(
        multiply(hankel[r][i], hankel[s][j], prime) !=
        multiply(hankel[r][j], hankel[s][i], prime)
        for r, s in combinations(range(a), 2) for i, j in combinations(range(3), 2))
    threshold = ((a - 1) * degree + 1) // 2
    receipt = {'degree': delta, 'hankel_rank': hankel_rank,
               'rank_two_lower_bound': threshold,
               'sequence': [[str(value) for value in item] if prime is None else item
                            for item in sequence]}
    if hankel_rank == 1:
        if delta % (a + 1):
            raise ArithmeticError('rank-one minimum degree is not a root-height multiple')
        receipt['root_height'] = delta // (a + 1)
    else:
        if delta < threshold:
            raise ArithmeticError('rank-two witness violates the index-sum bound')
        transpose = [list(row) for row in zip(*hankel)]
        receipt['left_nullities'], receipt['right_nullities'] = {}, {}
        for bound in (degree - 1, degree):
            left = a * (bound + 1) - rank(polynomial_matrix_coefficients(transpose, bound), prime)
            right = 3 * (bound + 1) - rank(polynomial_matrix_coefficients(hankel, bound), prime)
            expected = bound + 1 - degree
            if left != (a - 2) * expected or right != expected:
                raise ArithmeticError('Hankel kernel indices do not all equal D')
            receipt['left_nullities'][str(bound)] = left
            receipt['right_nullities'][str(bound)] = right
    return receipt


def recurrence_matrix(a, triple, degree):
    """Coefficients of sum_k c_k(x) lambda_(r+k)(x), for r<a."""
    width = (a + 2) * (degree + 1)
    output_length = max(map(len, triple)) + degree
    rows = [[0] * width for _ in range(a * output_length)]
    for r in range(a):
        for k, coefficients in enumerate(triple):
            for power, value in enumerate(coefficients):
                for j in range(degree + 1):
                    rows[r * output_length + power + j][
                        (r + k) * (degree + 1) + j] += value
    return rows


def minimal_indices(a, triple, prime):
    if a < 2 or any(len(polynomial(item, prime)) > a for item in triple):
        raise ValueError('require a>=2 and coefficient degrees less than a')
    primitive, gcd = primitive_triple(triple, prime)
    degree = max(map(len, primitive)) - 1
    for delta in range(a * degree // 2 + 1):
        matrix = recurrence_matrix(a, primitive, delta)
        if rank(matrix, prime) < (a + 2) * (delta + 1):
            return {'primitive_degree': degree, 'gcd_degree': len(gcd) - 1,
                    'minimal_indices': [delta, a * degree - delta]}
    raise ArithmeticError('no kernel in the proven search range')


def source_matrix(a, b, triple):
    """Literal coefficient [x^(H-j) z^(L-r)](u+zv+z^2w)."""
    size = a + b - 1
    rows = []
    for j in range(b):
        for L in range(size):
            row = []
            for H in range(size):
                for r in range(a):
                    z_power, x_power = L - r, H - j
                    row.append(triple[z_power][x_power]
                               if 0 <= z_power < 3 and
                               0 <= x_power < len(triple[z_power]) else 0)
            rows.append(row)
    return rows


def fixed_roots(triple, prime):
    """K-rational roots of the homogeneous z-quadratic, coefficientwise in x."""
    roots = []
    for s, t in [(1, value) for value in range(prime)] + [(0, 1)]:
        if all(sum((item[k] if k < len(item) else 0) * scalar
                   for item, scalar in zip(triple, (s * s, s * t, t * t))) % prime == 0
               for k in range(max(map(len, triple)))):
            roots.append([s, t])
    return roots


def check_triple(a, triple, prime, b_values=(3, 4, 5)):
    result = minimal_indices(a, triple, prime)
    first, second = result['minimal_indices']
    if prime is not None and result['primitive_degree'] > 0:
        roots = fixed_roots(triple, prime)
        if (first == 0) != bool(roots):
            raise ArithmeticError('zero-index/fixed-root criterion failed')
        result['fixed_roots'] = roots
    result['source_ranks'] = {}
    for b in b_values:
        if b < 3:
            raise ValueError('require b>=3')
        predicted = (a + 2) * b - max(b - first, 0) - max(b - second, 0)
        actual = rank(source_matrix(a, b, triple), prime)
        if actual != predicted:
            raise ArithmeticError(('source rank mismatch', prime, a, b, triple,
                                   actual, predicted, result['minimal_indices']))
        result['source_ranks'][str(b)] = actual
    return result


def census(cases, prime):
    indices, ranks = Counter(), Counter()
    hankel_ranks = Counter()
    low_index_cases = 0
    count = criterion_count = 0
    for a, triple in cases:
        result = check_triple(a, triple, prime)
        first, second = result['minimal_indices']
        indices[f'{a},{result["primitive_degree"]},{first},{second}'] += 1
        for b, value in result['source_ranks'].items():
            ranks[f'{a},{b},{value}'] += 1
        if result['primitive_degree'] > 0:
            witness = inspect_kernel(a, triple, prime, result)
            hankel_ranks[str(witness['hankel_rank'])] += 1
            low_index_cases += witness['degree'] < witness['rank_two_lower_bound']
        criterion_count += result['primitive_degree'] > 0
        count += 1
    return {'triples': count, 'source_maps': 3 * count,
            'fixed_root_criterion_cases': criterion_count,
            'minimum_kernel_hankel_ranks': dict(sorted(hankel_ranks.items())),
            'strictly_low_index_cases': low_index_cases,
            'hankel_left_right_nullity_checks': 4 * hankel_ranks['2'],
            'index_histogram_key': 'a,D,mu1,mu2',
            'index_histogram': dict(sorted(indices.items())),
            'rank_histogram_key': 'a,b,rank',
            'rank_histogram': dict(sorted(ranks.items()))}


def exhaustive_binary_cases():
    for a in (2, 3):
        for values in product(range(2), repeat=3 * a):
            if any(values):
                yield a, [list(values[k * a:(k + 1) * a]) for k in range(3)]


def sampled_cases(prime):
    generator = random.Random(20261023)
    for a in range(2, 6):
        for _ in range(8):
            triple = [[generator.randrange(prime) for _ in range(a)] for _ in range(3)]
            while not any(value for item in triple for value in item):
                triple = [[generator.randrange(prime) for _ in range(a)] for _ in range(3)]
            yield a, triple


NAMED_CASES = [
    ('constant_left', 3, [[1], [], []]),
    ('constant_middle', 3, [[], [1], []]),
    ('missing_left', 3, [[], [0, 1], [1]]),
    ('missing_right', 3, [[1], [0, 1], []]),
    ('common_linear_factor', 4, [[1, 1], [0, 1, 1], [1, 2, 1]]),
    ('common_quadratic_factor', 3, [[0, 0, 1], [0, 0, 2], [0, 0, 1]]),
    ('pr216_unbalanced', 3, [[0, 0, 1], [1, 0, 1], [1, 0, 2]]),
    ('pr216_balanced', 3, [[0, 0, 1], [1, 0, 1], [1, 1, 1]]),
]


def structural_controls():
    controls = []
    for prime in (None, 2, 3, 5):
        for a, degree in ((2, 1), (5, 3)):
            triple = [[0] * degree + [1], [], [1]]
            result = check_triple(a, triple, prime, b_values=(3, 7))
            witness = inspect_kernel(a, triple, prime, result)
            if witness['hankel_rank'] != 2 or witness['degree'] != witness['rank_two_lower_bound']:
                raise ArithmeticError('irreducible saturation control failed')
            controls.append({'name': 'odd_valuation_irreducible', 'a': a,
                             'field': 'Q' if prime is None else f'F{prime}',
                             'coefficients': triple,
                             'irreducibility_reason': 'A rational root would have square of odd x-adic valuation.',
                             **result, 'kernel_witness': witness})
        a = 5
        # (z-x)(z-(x^3+1)); x is a root of height one.
        triple = [[0, 1, 0, 0, 1], [-1, -1, 0, -1], [1]]
        result = check_triple(a, triple, prime, b_values=(3, 7))
        witness = inspect_kernel(a, triple, prime, result)
        root_vector = []
        for j in range(a + 2):
            root_vector.extend([int(power == j) for power in range(a + 2)])
        matrix = recurrence_matrix(a, triple, a + 1)
        residual = [sum(value * entry for value, entry in zip(row, root_vector))
                    for row in matrix]
        if any(value if prime is None else value % prime for value in residual):
            raise ArithmeticError('nonconstant rational-root witness failed')
        coefficient_span = [[item[k] if k < len(item) else 0 for item in triple]
                            for k in range(5)]
        if rank(coefficient_span, prime) != 3:
            raise ArithmeticError('constant-root exclusion control failed')
        if witness['hankel_rank'] != 1 or witness['degree'] != 6 or witness['rank_two_lower_bound'] != 8:
            raise ArithmeticError('nonconstant low-index control failed')
        controls.append({'name': 'nonconstant_rational_root_low_branch', 'a': a,
                         'field': 'Q' if prime is None else f'F{prime}',
                         'coefficients': triple, 'rational_root': {'s': [1], 't': [0, 1]},
                         'constant_coefficient_span_rank': 3,
                         **result, 'kernel_witness': witness})
    return controls


def integer_determinant(rows):
    """Fraction-free determinant; exact division also checks the elimination."""
    matrix = [list(row) for row in rows]
    size, previous, sign = len(matrix), 1, 1
    for k in range(size - 1):
        pivot = next((i for i in range(k, size) if matrix[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            matrix[k], matrix[pivot] = matrix[pivot], matrix[k]
            sign = -sign
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = matrix[k][k] * matrix[i][j] - matrix[i][k] * matrix[k][j]
                matrix[i][j], remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError('nonexact Bareiss division')
            matrix[i][k] = 0
        previous = matrix[k][k]
    return sign * matrix[-1][-1]


def spectrum_controls():
    cases = [('rank_nine', [[1], [], []], 9),
             ('rank_twelve', [[1], [0, 1], []], 12),
             ('rank_fourteen', [[1], [0, 0, 1], [1]], 14),
             ('rank_fifteen', [[0, 0, 1], [0, 1], [1]], 15)]
    records = []
    for name, triple, expected in cases:
        ranks = {}
        for prime in (None, 2, 3, 5):
            value = check_triple(3, triple, prime, b_values=(3,))['source_ranks']['3']
            if value != expected:
                raise ArithmeticError('universal spectrum witness failed')
            ranks['Q' if prime is None else f'F{prime}'] = value
        records.append({'name': name, 'coefficients': triple, 'ranks': ranks})
    matrix = source_matrix(3, 3, cases[-1][1])
    row_labels = [j - L + 2 for j in range(3) for L in range(5)]
    column_labels = [H - r for H in range(5) for r in range(3)]
    if any(value for i, row in enumerate(matrix) for j, value in enumerate(row)
           if row_labels[i] != column_labels[j]):
        raise ArithmeticError('spectrum matrix has an off-block coefficient')
    blocks = []
    for label in range(-2, 5):
        block = [[matrix[i][j] for j in range(15) if column_labels[j] == label]
                 for i in range(15) if row_labels[i] == label]
        determinant = integer_determinant(block)
        if abs(determinant) != 1:
            raise ArithmeticError('spectrum block is not unimodular')
        blocks.append({'label': label, 'matrix': block, 'determinant': determinant})
    determinant = integer_determinant(matrix)
    if determinant != -1:
        raise ArithmeticError('literal spectrum determinant changed')
    return {'witnesses': records, 'source_maps': 16,
            'rank_fifteen_integer_certificate': {
                'zero_off_block': True, 'blocks': blocks, 'determinant': determinant}}


def report():
    controls = []
    for prime in (None, 2, 3, 5):
        for name, a, triple in NAMED_CASES:
            controls.append({'name': name, 'field': 'Q' if prime is None else f'F{prime}',
                             'a': a, 'coefficients': triple,
                             **check_triple(a, triple, prime)})
    binary = census(exhaustive_binary_cases(), 2)
    structure = structural_controls()
    spectra = {'complete_F2': sorted({int(key.split(',')[2])
                                     for key in binary['rank_histogram']
                                     if key.startswith('3,3,')})}
    for field in ('Q', 'F3', 'F5'):
        spectra[f'named_{field}'] = sorted({row['source_ranks']['3'] for row in controls
                                          if row['a'] == 3 and row['field'] == field})
    return {
        'scope': 'Exact finite controls; the all-size result rests on the written proof.',
        'b_values': [3, 4, 5],
        'complete_binary': {'a_values': [2, 3], 'coefficient_degree_bound': 'deg<a',
                            **binary},
        'deterministic_samples': {
            'seed': 20261023, 'a_values': [2, 3, 4, 5], 'samples_per_a': 8,
            'fields': {f'F{prime}': census(sampled_cases(prime), prime) for prime in (3, 5)}},
        'named_controls': controls,
        'named_source_maps': len(controls) * 3,
        'structural_controls': structure,
        'structural_source_maps': len(structure) * 2,
        'a3_b3_observed_rank_spectra': spectra,
        'universal_spectrum_controls': spectrum_controls(),
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

"""Exact finite controls for quadratic recurrence kernel indices.

Literal source matrices and polynomial recurrence matrices are constructed
separately. Finite comparisons support, but do not prove, the written theorem.
"""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import random


def rank(rows, prime):
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
    return len(pivots)


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
    count = criterion_count = 0
    for a, triple in cases:
        result = check_triple(a, triple, prime)
        first, second = result['minimal_indices']
        indices[f'{a},{result["primitive_degree"]},{first},{second}'] += 1
        for b, value in result['source_ranks'].items():
            ranks[f'{a},{b},{value}'] += 1
        criterion_count += result['primitive_degree'] > 0
        count += 1
    return {'triples': count, 'source_maps': 3 * count,
            'fixed_root_criterion_cases': criterion_count,
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


def report():
    controls = []
    for prime in (None, 2, 3, 5):
        for name, a, triple in NAMED_CASES:
            controls.append({'name': name, 'field': 'Q' if prime is None else f'F{prime}',
                             'a': a, 'coefficients': triple,
                             **check_triple(a, triple, prime)})
    return {
        'scope': 'Exact finite controls; the all-size result rests on the written proof.',
        'b_values': [3, 4, 5],
        'complete_binary': {'a_values': [2, 3], 'coefficient_degree_bound': 'deg<a',
                            **census(exhaustive_binary_cases(), 2)},
        'deterministic_samples': {
            'seed': 20261023, 'a_values': [2, 3, 4, 5], 'samples_per_a': 8,
            'fields': {f'F{prime}': census(sampled_cases(prime), prime) for prime in (3, 5)}},
        'named_controls': controls,
        'named_source_maps': len(controls) * 3,
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

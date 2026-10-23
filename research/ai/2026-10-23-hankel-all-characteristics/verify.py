"""Finite prime-field controls for the divided-square Hankel proof.

These checks support the written proof; they do not prove its all-field claim.
"""
import argparse
from itertools import combinations_with_replacement, product
import json
from pathlib import Path


def rank_mod(rows, prime):
    """Exact elimination, retaining sparse rows of the coefficient equations."""
    pivots = {}
    for source in rows:
        row = {i: value % prime for i, value in enumerate(source)
               if value % prime}
        while row:
            column = min(row)
            if column not in pivots:
                inverse = pow(row[column], -1, prime)
                pivots[column] = {i: value * inverse % prime
                                  for i, value in row.items()}
                break
            coefficient = row[column]
            for i, value in pivots[column].items():
                updated = (row.get(i, 0) - coefficient * value) % prime
                if updated:
                    row[i] = updated
                else:
                    row.pop(i, None)
    return len(pivots)


def contraction(evaluation):
    """(id tensor evaluation) on the swap-invariant tensor basis."""
    n = len(evaluation)
    pairs = list(combinations_with_replacement(range(n), 2))
    matrix = [[0] * len(pairs) for _ in range(n)]
    for column, (i, j) in enumerate(pairs):
        matrix[i][column] = evaluation[j]
        if i != j:
            matrix[j][column] = evaluation[i]
    return matrix


def kernel_invariants(evaluation, prime):
    n = len(evaluation)
    pivot = next(i for i, value in enumerate(evaluation) if value % prime)
    inverse = pow(evaluation[pivot], -1, prime)
    kernel = []
    for i in range(n):
        if i != pivot:
            vector = [0] * n
            vector[i] = 1
            vector[pivot] = -evaluation[i] * inverse % prime
            kernel.append(vector)
    rows = []
    for i, j in combinations_with_replacement(range(n - 1), 2):
        u, v = kernel[i], kernel[j]
        rows.append([
            (u[a] * u[b] if i == j else
             u[a] * v[b] + v[a] * u[b]) % prime
            for a, b in combinations_with_replacement(range(n), 2)])
    return rows


def assignment_dimension(r, d, exponents, prime, doubled_diagonal=False):
    """Compare every coefficient of h(w)(w f), keeping diagonal equations."""
    width = len(exponents) * (d + 1)
    rows = []
    for i, j in combinations_with_replacement(range(len(exponents)), 2):
        for shift in range(d - r + 1):
            row = [0] * width
            row[i * (d + 1) + exponents[j] + shift] += 1
            if i != j or doubled_diagonal:
                row[j * (d + 1) + exponents[i] + shift] += 1
            rows.append(row)
    return width - rank_mod(rows, prime)


def report():
    fiber_counts = {}
    assignment_counts = {}
    for prime in (2, 3, 5):
        fibers = 0
        for n in range(2, 5):
            for evaluation in product(range(prime), repeat=n):
                if not any(evaluation):
                    continue
                matrix = contraction(evaluation)
                kernel = kernel_invariants(evaluation, prime)
                if rank_mod(matrix, prime) != n:
                    raise ArithmeticError('contraction is not surjective')
                if rank_mod(kernel, prime) != n * (n - 1) // 2:
                    raise ArithmeticError('kernel embedding lost rank')
                if any(sum(a * b for a, b in zip(row, vector)) % prime
                       for row in matrix for vector in kernel):
                    raise ArithmeticError('invariant kernel does not contract to zero')
                fibers += 1
        fiber_counts[str(prime)] = fibers
        assignments = 0
        for r in range(2, 7):
            for mask in range(1 << (r - 1)):
                exponents = [0] + [i for i in range(1, r)
                                   if mask & (1 << (i - 1))] + [r]
                gaps = [b - a for a, b in zip(exponents, exponents[1:])]
                for d in range(2 * r, 3 * r + 1):
                    if 5 * r >= 2 * (d + 2):
                        continue
                    expected = sum(max(a + b - (d - r) - 1, 0)
                                   for i, a in enumerate(gaps) for b in gaps[i:])
                    actual = assignment_dimension(r, d, exponents, prime)
                    if actual != expected:
                        raise ArithmeticError((prime, r, d, exponents, actual, expected))
                    assignments += 1
        assignment_counts[str(prime)] = assignments
    correct = assignment_dimension(2, 4, [0, 2], 2)
    doubled = assignment_dimension(2, 4, [0, 2], 2, doubled_diagonal=True)
    if correct != 1 or doubled <= correct:
        raise ArithmeticError('characteristic-two negative control failed')
    return {
        'scope': 'Finite exact prime-field controls; the all-field claim rests on the written proof.',
        'primes': [2, 3, 5], 'evaluation_dimensions': [2, 3, 4],
        'nonzero_evaluation_fibers': fiber_counts,
        'assignment_rank_range': [2, 6],
        'assignment_degree_range': '2r <= d <= 3r with 5r < 2(d+2)',
        'monomial_assignment_cases': assignment_counts,
        'diagonal_negative_control': {'prime': 2, 'r': 2, 'd': 4,
                                     'exponents': [0, 2], 'correct_dimension': correct,
                                     'incorrect_doubled_diagonal_dimension': doubled},
        'independent_review': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = json.dumps(report(), indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
    else:
        print(data, end='')

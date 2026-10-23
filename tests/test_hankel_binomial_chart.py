"""Original six-index source replay, identity minors and torus controls."""

from collections import Counter
import importlib.util
import itertools
import json
from math import isqrt
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-hankel-additive-cost'
RESULTS = ROOT/'results/hankel-additive-cost-2026-10-23'
spec = importlib.util.spec_from_file_location('binomial_chart_checks', PACKAGE/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def original_source_slice(a, b, r, seed):
    """Contract the original six-index source sum, not a key factorization."""
    m = a+b-1
    matrix = [[0]*(a*b*m) for _ in range(a*b*m)]
    for i, short_j, p, q, short_t, s in itertools.product(
            range(a), range(b), range(a), range(b), range(a), range(b)):
        if i != s or p+q != seed+r*i:
            continue
        y = (short_j*a+p)*m+s+short_t
        z = ((i+short_j)*b+q)*a+short_t
        matrix[y][z] += 1
    return matrix


def identity_minor(matrix, rows, columns):
    return all(matrix[row][column] == int(i == j)
               for i, row in enumerate(rows) for j, column in enumerate(columns))


class HankelBinomialChartTests(unittest.TestCase):
    def test_complete_key_rectangle_and_saved_literal_reports(self):
        saved = json.loads((RESULTS/'chart-minima.json').read_text())
        self.assertEqual(v.report(), saved)
        self.assertEqual(saved['source_formats_checked'], 140)
        self.assertEqual(saved['feasible_seed_cases_checked'], 426)
        self.assertEqual(saved['balanced_closed_cases_checked'], 1711)
        self.assertEqual(saved['literal_coefficients_checked'], 910075)
        self.assertEqual(len(saved['literal_certificates']), 19)
        self.assertFalse(saved['general_degree_one_additive_conjecture_proved'])
        self.assertFalse(saved['independent_review'])

    def test_identity_minors_from_original_source_and_corruption(self):
        saved = json.loads((RESULTS/'chart-minima.json').read_text())
        for parameters in [(3, 3, 2, 0), (3, 3, 2, 1), (3, 5, 2, 1), (4, 4, 3, 2)]:
            a, b, r, seed = parameters
            record = next(c for c in saved['literal_certificates']
                          if (c['a'], c['b'], c['r'], c['seed']) == parameters)
            matrix = original_source_slice(*parameters)
            self.assertEqual(matrix, v.pilot.literal_matrix(v.basis_sequence(*parameters), a, b))
            rows, columns = record['identity_minor_rows'], record['identity_minor_columns']
            self.assertTrue(identity_minor(matrix, rows, columns))
            corrupt = columns.copy()
            corrupt[0] = corrupt[1]
            self.assertFalse(identity_minor(matrix, rows, corrupt))

    def test_balanced_closed_minimum_by_direct_residue_counts(self):
        for n in range(3, 21):
            for r in range(2, n):
                counts = Counter(p % r for p in range(n))
                correction = min(sum((counts[s]-1)*(counts[(j-s) % r]-1)
                                     for s in range(r)) for j in range(r))
                self.assertEqual(v.balanced_minimum(n, r), r*n*n+2*n*(n-r)+correction)
        self.assertEqual(v.balanced_minimum(4, 2), 50)
        self.assertEqual(v.balanced_minimum(5, 2), 84)
        for n in range(3, 21):
            self.assertEqual(v.balanced_minimum(n, n-1), (n-1)*n*n+2*n)

    def test_feasible_and_empty_source_charts(self):
        self.assertEqual(v.feasible_seeds(3, 5, 2), [1])
        self.assertEqual(v.feasible_seeds(5, 3, 2), [1])
        self.assertEqual(v.feasible_seeds(3, 7, 2), [])
        with self.assertRaises(ValueError):
            v.basis_sequence(3, 5, 2, 0)
        with self.assertRaises(ValueError):
            v.feasible_seeds(2, 3, 2)

    def test_finite_torus_row_column_scaling_on_literal_coefficients(self):
        a = b = 4
        m = a+b-1
        x, z = v.x, v.z
        f = [v.pilot.v.sp.expand((x*z)**(k//2)*(1 if k % 2 == 0 else 1+x+z+x*z))
             for k in range(m)]
        coefficients = v.pilot.v.source.coefficients(f, a, b)
        alpha, gamma, beta, lowest = 3, 1, -5, -4
        changed = [0]*m
        for (i, k, s), c in coefficients.items():
            changed[k] += c*2**(i*alpha+k*gamma+s*beta-lowest)*x**i*z**s
        original = v.pilot.literal_matrix(f, a, b)
        weighted = v.pilot.literal_matrix(changed, a, b)
        prime = 32003
        rows = list(itertools.product(range(b), range(a), range(m)))
        columns = list(itertools.product(range(m), range(b), range(a)))
        for y, (short_j, p, L) in enumerate(rows):
            left = pow(2, -short_j*alpha+p*gamma+L*beta, prime)
            for w, (H, q, short_t) in enumerate(columns):
                right = pow(2, H*alpha+q*gamma-short_t*beta-lowest, prime)
                self.assertEqual(weighted[y][w] % prime, original[y][w]*left*right % prime)

    def test_completed_initial_moment_grid(self):
        self.assertFalse(any(32003 % d == 0 for d in range(2, isqrt(32003)+1)))
        saved = json.loads((RESULTS/'initial-moments.json').read_text())
        self.assertEqual(v.pilot.report(), saved)
        self.assertEqual(len(saved['cases']), 161)
        self.assertEqual(saved['minimum_modular_rank'], 24)
        self.assertEqual(saved['rational_violations'], 0)
        self.assertFalse(saved['general_additive_inequality_proved'])


if __name__ == '__main__':
    unittest.main()

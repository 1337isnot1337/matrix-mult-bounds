"""Coefficient, degeneration, and lower-bound checks for the new basis ansatz."""
import importlib.util
from itertools import product
from pathlib import Path
import random
import sympy as sp
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'chebyshev_search', ROOT/'research/ai/2026-10-20-concavity-equivalence/chebyshev_search.py')
search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)


class ChebyshevSearchTests(unittest.TestCase):
    def test_basis_and_product_coefficients(self):
        t = sp.symbols('t')
        for i in range(1, 12):
            self.assertEqual(sp.degree(sp.chebyshevt(i, t), t), i)
            for j in range(1, 12):
                self.assertEqual(sp.expand(2*sp.chebyshevt(i, t)*sp.chebyshevt(j, t)
                    - sp.chebyshevt(i+j, t)-sp.chebyshevt(abs(i-j), t)), 0)
        for a, b in product(range(2, 6), repeat=2):
            terms = search.support(a, b)
            self.assertEqual(len(terms), len(set(terms)))
            for i in range(a):
                for j in range(1, b):
                    first = sp.Rational(1, 2) if i == 0 else sp.chebyshevt(i, t)
                    actual = sp.expand(2*first*sp.chebyshevt(j, t))
                    expected = sum(sp.chebyshevt(k, t) for x, y, k in terms if (x, y) == (i, j))
                    self.assertEqual(sp.expand(actual-expected), 0)

    def test_zero_terms_and_disjoint_nonshared_spaces(self):
        rng = random.Random(117)
        for a, b in product(range(2, 6), repeat=2):
            wx = tuple(rng.randint(-3, 3) for _ in range(a))
            wy = tuple(rng.randint(-3, 3) for _ in range(b-1))
            groups, wz = search.groups_and_weights(wx, wy)
            expected = set()
            for term in search.support(a, b):
                i, j, k = term
                weight = wx[i]+wy[j-1]+wz[k]
                self.assertGreaterEqual(weight, 0)
                if weight == 0:
                    expected.add(term)
            self.assertEqual(set(term for group in groups for term in group), expected)
            for i, group in enumerate(groups):
                for other in groups[:i]:
                    for axis in (1, 2):
                        self.assertTrue({t[axis] for t in group}.isdisjoint({t[axis] for t in other}))

    def test_slice_bound_against_rational_matrices(self):
        for a, b in product(range(2, 5), repeat=2):
            terms = search.support(a, b)
            best = 0
            for axis in range(3):
                others = [v for v in range(3) if v != axis]
                for label in {term[axis] for term in terms}:
                    selected = [term for term in terms if term[axis] == label]
                    rows = sorted({term[others[0]] for term in selected})
                    cols = sorted({term[others[1]] for term in selected})
                    matrix = sp.zeros(len(rows), len(cols))
                    for term in selected:
                        matrix[rows.index(term[others[0]]), cols.index(term[others[1]])] += 1
                    best = max(best, matrix.rank())
            self.assertLessEqual(search.slice_bound(terms), best)


if __name__ == '__main__':
    unittest.main()

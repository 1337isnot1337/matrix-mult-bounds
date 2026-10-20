"""Independent coefficient ranks and exact calculus for a conditional route."""
from fractions import Fraction
import importlib.util
from pathlib import Path
import sympy as sp
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


route = load('fatpoint_route', ROOT/'research/ai/2026-10-20-concavity-equivalence/fatpoint_route.py')
matrix = load('fatpoint_coefficient_matrices', ROOT/'research/ai/2026-10-20-session2/tensor_checks.py')


class FatpointRouteTests(unittest.TestCase):
    def test_small_target_matrices(self):
        for a in range(1, 6):
            dims, terms = route.tensor(a)
            for p in range(a):
                actual = matrix.koszul_matrix(dims, terms, p).rank()
                self.assertEqual(actual, route.target_rank(a, p))

    def test_integral_of_lower_envelope(self):
        x, d = sp.symbols('x d', positive=True)
        integrand = x**(d-1)*(1-x+(2/d-1)*x)
        actual = 2*sp.integrate(integrand, (x, 0, sp.Rational(1, 2)))
        self.assertEqual(sp.simplify(actual-2**(2-d)/(d*(d+1))), 0)

    def test_root_certificate_and_negative_controls(self):
        self.assertTrue(route.rational_below_root(Fraction(168, 125)))
        self.assertFalse(route.rational_below_root(Fraction(3, 2)))
        self.assertTrue(route.rational_below_root(Fraction(4, 3)))
        self.assertFalse(route.rational_below_root(Fraction(4, 3), Fraction(103, 100)))


if __name__ == '__main__':
    unittest.main()

"""Exact analytic controls for the scaling and rigidity note.

These verify formulas and counterexamples, not the general analytic theorem.
"""
from fractions import Fraction
import sympy as sp
import unittest


class HomogeneousControls(unittest.TestCase):
    def test_actual_flattening_character_scaling(self):
        # For flattening rank, t=2/3 and P(a,b)^2=ab(a+b-1).
        a, b, n = sp.symbols('a b n', positive=True)
        scaled_square = (n*a)*(n*b)*(n*a+n*b-1)/n**3
        self.assertEqual(sp.expand(scaled_square-a*b*(a+b)), -a*b/n)
        self.assertEqual(sp.limit(scaled_square, n, sp.oo), a*b*(a+b))
        r = sp.symbols('r', positive=True)
        f = sp.sqrt(r*(r+1))
        self.assertEqual(sp.simplify(sp.diff(f, r, 2)),
                         -1/(4*r**sp.Rational(3, 2)*(r+1)**sp.Rational(3, 2)))

    def test_flattening_character_curvature_bound(self):
        delta = 2*sp.sqrt(3)-1-sp.sqrt(6)
        self.assertTrue(delta.is_positive)
        # Q at d=3/2 is equivalent to delta<=1/8.
        self.assertTrue((sp.Rational(1, 8)-delta).is_positive)

    def test_critical_shape_and_diagonal_join(self):
        r = sp.symbols('r', positive=True)
        below = r**sp.Rational(1, 3)*(1+r/2)
        above = r+sp.Rational(1, 2)
        self.assertEqual(below.subs(r, 1), above.subs(r, 1))
        self.assertEqual(sp.diff(below, r).subs(r, 1), sp.diff(above, r))
        self.assertEqual(sp.simplify(sp.diff(below, r, 2)
                         - 2*(r-1)/(9*r**sp.Rational(5, 3))), 0)
        self.assertEqual(sp.expand(above.subs(r, 3*r+1)-3*above), 0)
        self.assertEqual(2*above.subs(r, 2)-above.subs(r, 1)-above.subs(r, 3), 0)

    def test_conditional_exponent_example(self):
        delta = Fraction(1, 1000)
        self.assertEqual(9/(4*(1+delta)), Fraction(2250, 1001))
        self.assertLess(Fraction(2250, 1001), Fraction(9, 4))


if __name__ == '__main__':
    unittest.main()

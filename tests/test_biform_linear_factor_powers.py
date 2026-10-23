"""Exact nonlinear-family and univariate-image controls for the corollary."""
import unittest

import sympy as s
from sympy.polys.matrices import DomainMatrix

from test_elementary_biform_gap import independent_matrix, x, z


class BiformLinearFactorPowerTests(unittest.TestCase):
    def test_nonlinear_mixed_factors_and_univariate_decorations(self):
        cases = [
            (3, 4, 1, 1+x, 2+z, x+z+z**2),
            (4, 6, 2, 1+x, 1+z, z**2+x*(1+z)),
            (4, 5, 2, x, z, 1+x*z),
            (3, 5, 2, 1, 1, x+z**2),
            (5, 6, 3, x, 1, x+z),
        ]
        for a, b, e, u, v, h in cases:
            with self.subTest(a=a, b=b, e=e, h=h):
                f = s.Poly(s.expand(u*v*h**e), x, z)
                self.assertLess(f.degree(x), a)
                self.assertLess(f.degree(z), b)
                core = independent_matrix(a, b, h**e)
                decorated = independent_matrix(a, b, f.as_expr())
                self.assertEqual(DomainMatrix.from_Matrix(core).rank(), a*(b+e))
                self.assertEqual(DomainMatrix.from_Matrix(decorated).rank(), a*(b+e))

    def test_exact_multiplication_identity_with_noninvertible_truncations(self):
        a, b = 3, 4
        width = a+b-1
        q, u, v = x+z, x, z*(1+z)
        # Multiplication on coefficients, built independently by polynomial expansion.
        def multiplication(poly, variable):
            return s.Matrix([[s.expand(poly*variable**j).coeff(variable, i)
                              for j in range(width)] for i in range(width)])
        mu, mv = multiplication(u, x), multiplication(v, z)
        self.assertEqual(mu.det(), 0)
        self.assertEqual(mv.det(), 0)
        matrix = independent_matrix(a, b, q)
        actual = independent_matrix(a, b, u*v*q)
        self.assertEqual(actual, s.kronecker_product(s.eye(b), mv)*matrix*
                         s.kronecker_product(mu.T, s.eye(a)))
        self.assertEqual(DomainMatrix.from_Matrix(actual).rank(),
                         DomainMatrix.from_Matrix(matrix).rank())

    def test_distinct_factors_do_not_supply_the_repeated_factor_bound(self):
        repeated = independent_matrix(3, 3, (x+z)**2)
        distinct = independent_matrix(3, 3, (x+z)*(x-z))
        self.assertEqual(DomainMatrix.from_Matrix(repeated).rank(), 15)
        self.assertEqual(DomainMatrix.from_Matrix(distinct).rank(), 14)


if __name__ == '__main__':
    unittest.main()

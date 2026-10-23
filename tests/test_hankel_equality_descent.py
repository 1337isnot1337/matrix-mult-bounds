"""Literal slice ranks and independent homogeneous recurrence controls."""

import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-hankel-equality'
spec = importlib.util.spec_from_file_location('hankel_equality_descent', PACKAGE/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class HankelEqualityDescentTests(unittest.TestCase):
    def test_saved_exact_controls(self):
        saved = json.loads((ROOT/'results/hankel-equality-2026-10-23/controls.json').read_text())
        self.assertEqual(v.report(), saved)
        self.assertEqual(len(saved['saturated_controls']), 18)
        self.assertEqual([x['symbol_rank'] for x in saved['nonsaturated_controls']], list(range(2, 9)))
        self.assertEqual(len(saved['near_equality_controls']), 3)
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_independent_reduced_scheme_and_kernel_gcds(self):
        # Reconstruct the supporting polynomial from each homogeneous kernel,
        # without using the report's stacked coefficient-recurrence routine.
        u, w = sp.symbols('u w')
        a, b = 4, 5
        f = [sum((1+t*v.X)*(1+(t+1)*v.Z)*t**k for t in (1, 2, 3))
             for k in range(a+b-1)]
        H = sp.Matrix(a, b, lambda i, j: f[i+j])
        expected = sp.prod(w-t*u for t in (1, 2, 3))
        for matrix, length in [(H, b), (H.T, a)]:
            domain = sp.QQ.frac_field(v.X, v.Z)
            kernel = DomainMatrix.from_Matrix(matrix).convert_to(domain).nullspace().to_Matrix()
            forms = [sum(c*u**(length-1-j)*w**j for j, c in enumerate(vector))
                     for vector in kernel.tolist()]
            gcd = sp.Poly(forms[0], u, w, domain=domain)
            for form in forms[1:]:
                gcd = sp.gcd(gcd, sp.Poly(form, u, w, domain=domain))
            gcd = gcd.monic().as_expr()
            quotient = sp.cancel(gcd/sp.Poly(expected, u, w).monic().as_expr())
            self.assertFalse(quotient.has(u, w, v.X, v.Z))
            self.assertNotEqual(quotient, 0)

    def test_constant_scheme_containment_is_not_sufficient_for_saturation(self):
        # Only h_0 is nonzero, so q=V is a common annihilator. The biform
        # 1+xz is not separable, and the literal full slice rank exceeds ab.
        a = b = 3
        f = [1+v.X*v.Z, 0, 0, 0, 0]
        row = v.control('nonseparable-fixed-origin', f, a, b, 1, 12)
        self.assertEqual(row['common_annihilator_nullity'], 1)
        self.assertEqual(row['normalized_common_annihilator'], ['0', '1'])
        self.assertFalse(row['saturated'])

    def test_primitive_gcd_and_field_intersection_controls(self):
        u, w, t = sp.symbols('u w t')
        q = w**3-2*u**3
        self.assertEqual(sp.Poly(sp.gcd(q*u, q*w), u, w).monic(),
                         sp.Poly(q, u, w).monic())
        # A moving support is visible in one kernel field, not both.
        moving = w**3-v.X*u**3
        self.assertTrue(moving.has(v.X))
        self.assertFalse(moving.has(v.Z))
        # The shared normalized coefficients of a true constant support do
        # not acquire either variable under a rational scalar change.
        scaled = sp.Poly((v.X+1)/(v.Z+2)*q, u, w)
        leading = scaled.coeff_monomial(w**3)
        normalized = [sp.cancel(c/leading) for c in scaled.coeffs()]
        self.assertTrue(all(not c.has(v.X, v.Z) for c in normalized))
        C = sp.Matrix([[1, t], [0, 0]])
        self.assertEqual(C.rank(), 1)
        # Keeping all outputs detects the nonconstant column dependence.
        coefficient_map = sp.Matrix([[1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1]])
        self.assertEqual(coefficient_map.rank(), 3)

    def test_rejects_wrong_source_dimensions(self):
        with self.assertRaises(ValueError):
            v.coefficients([1, 2], 3, 3)
        with self.assertRaises(ValueError):
            v.coefficients([v.X**3, 0, 0, 0, 0], 3, 3)


if __name__ == '__main__':
    unittest.main()

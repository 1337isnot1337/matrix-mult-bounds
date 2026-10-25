"""Exact invariants, direct determinant curves and trace-only false positives."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-quadratic-invertible-stratum'
SPEC = importlib.util.spec_from_file_location('quadratic_invertible', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class QuadraticInvertibleStratumTests(unittest.TestCase):
    def test_complete_report_and_scope(self):
        saved = json.loads((ROOT / 'results/quadratic-invertible-stratum-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertEqual(saved['dimension_upper_bound'], 4)
        self.assertEqual(saved['excluded_characteristics'], [2, 3])
        self.assertFalse(saved['sharpness_supplied'])
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_source_pins(self):
        sources = verify.check_source_pins()
        self.assertEqual(sources['base_commit'], '07bfe52b8df3112ec3f0762d6ed4e60d4100b7fc')
        self.assertFalse(sources['independent_review'])

    def test_trace_only_candidates_are_excluded_by_second_coefficient(self):
        # Trace alone really does leave these two primes. The nonzero second
        # coefficient, not the trace test, is what excludes them.
        for prime in (5, 151):
            record = verify.modular_trace_only_control(prime)
            self.assertEqual(record['critical_ratio_polynomial'], 0)
            self.assertEqual(record['trace_numerator'], 0)
            self.assertNotEqual(record['second_coefficient_at_p_mu_one'], 0)
        for prime in (2, 3, 7):
            with self.assertRaises(ValueError):
                verify.modular_trace_only_control(prime)

    def test_second_coefficient_omission_is_rejected(self):
        original = verify.determinant_coefficients

        def broken(Q, p, q):
            first, second = original(Q, p, q)
            return first, second-27*p*p/(q*q)

        with patch.object(verify, 'determinant_coefficients', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'literal second coefficient'):
                verify.matrix_checks()

    def test_direct_gradient_curves_in_original_matrix_coordinates(self):
        # These are implementation controls, not claimed bounded-rank families.
        # Differentiate det(N+sA) directly, then compare the full det(N+tV)
        # to det(N)*det(I+tC), without using the report's block normal form.
        s, t = sp.symbols('s t')
        A = sp.Matrix([[1, -2, 3], [0, 2, 1], [-1, 0, 1]])
        matrices = (
            sp.Matrix([[1, 1, 0], [0, 1, 1], [1, 0, 2]]),
            sp.Matrix([[2, 0, 1], [1, -1, 0], [0, 1, 1]]),
            sp.diag(1, 2, 3),
        )
        for N in matrices:
            p, q = N.det(), sp.trace(N.T*N)
            self.assertNotEqual(p*q, 0)
            gradient = N.adjugate().T
            direct_derivative = sp.Poly((N+s*A).det(), s).nth(1)
            self.assertEqual(direct_derivative, sp.trace(gradient.T*A))
            V = gradient-3*p/q*N
            Q = (N.T*N).inv()
            C = p*(Q-3/q*sp.eye(3))
            self.assertEqual(N.inv()*V, C)
            self.assertEqual(sp.expand((N+t*V).det()-p*(sp.eye(3)+t*C).det()), 0)
            direct = sp.Poly((N+t*V).det()/p, t)
            self.assertEqual(direct.nth(1), p*(sp.trace(Q)-9/q))
            self.assertEqual(direct.nth(2), p*p*(sp.trace(Q.adjugate())-6*sp.trace(Q)/q+27/q**2))

    def test_characteristic_seven_is_handled_before_division(self):
        rho = sp.Symbol('rho')
        self.assertEqual(sp.Poly(2-7*rho, rho, modulus=7).as_expr(), 2)
        # A generic rank-seven claim in characteristic three would be false.
        mu, d = sp.symbols('mu d')
        self.assertEqual(sp.Poly(12*mu**2*d*(mu**2-d), mu, d, modulus=3).as_expr(), 0)


if __name__ == '__main__':
    unittest.main()

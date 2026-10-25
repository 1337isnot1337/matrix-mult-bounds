"""Radical/line identities and a basepoint minor valid in every odd field."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-quadratic-char3-stratum'
SPEC = importlib.util.spec_from_file_location('quadratic_char3', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class QuadraticChar3StratumTests(unittest.TestCase):
    def test_exact_report_and_scope(self):
        saved = json.loads((ROOT / 'results/quadratic-char3-stratum-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertEqual(saved['odd_characteristic_upper_bound'], 4)
        self.assertEqual(saved['algebraically_closed_odd_characteristic_lower_bound'], 2)
        self.assertFalse(saved['characteristic_two_resolved'])
        self.assertFalse(saved['sharpness_supplied'])
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_denominators_checked_before_reduction(self):
        x = sp.Symbol('x')
        for expr in (1/(3*x), sp.Rational(1, 3), 1/(3*x+6)):
            with self.assertRaises(ValueError):
                verify.zero_mod_three(expr, (x,), 'invalid denominator')
        verify.zero_mod_three(3/(2*x), (x,), 'valid vanishing')
        with self.assertRaisesRegex(ArithmeticError, 'nonzero'):
            verify.zero_mod_three(1/(2*x), (x,), 'nonzero')

    def test_lost_linear_form_derivative_is_rejected(self):
        data = verify.line_invariants()
        data['hcurve'] = data['p']*data['mu']
        with patch.object(verify, 'line_invariants', return_value=data):
            with self.assertRaisesRegex(ArithmeticError, 'cubic coefficient'):
                verify.cubic_line_check()

    def test_exported_minor_has_integer_determinant_sixteen(self):
        # Rebuild using explicit row/column pairs, independently of the
        # verifier's flattened-index construction. The integer certificate
        # specializes in every odd characteristic, not just tested primes.
        M = [[0, 1, 1], [-1, -2, 1], [1, -1, 0]]
        rows = [(j, L) for j in range(3) for L in range(5) if (j, L) != (0, 1)]
        columns = [(H, r) for H in range(5) for r in range(3) if (H, r) != (1, 0)]
        minor = sp.Matrix([[M[H-j][L-r] if 0 <= H-j <= 2 and 0 <= L-r <= 2 else 0
                            for H, r in columns] for j, L in rows])
        saved = json.loads((ROOT / 'results/quadratic-char3-stratum-2026-10-25/controls.json').read_text())
        self.assertEqual(minor.tolist(), saved['two_plane']['base_minor_matrix'])
        self.assertEqual(minor.det(method='bareiss'), 16)
        self.assertEqual(saved['two_plane']['deleted_row_pair'], [0, 1])
        self.assertEqual(saved['two_plane']['deleted_column_pair'], [1, 0])
        self.assertTrue(saved['two_plane']['field_requires_sqrt_minus_one'])

    def test_corrupted_source_endpoint_is_rejected(self):
        original = verify.literal_source

        def broken(M):
            R = original(M)
            R[0, :] = sp.zeros(1, 15)
            return R

        with patch.object(verify, 'literal_source', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'minor16'):
                verify.two_plane_checks()

    def test_characteristic_two_is_not_admitted_by_the_certificate(self):
        x, y = sp.symbols('x y')
        self.assertTrue(sp.Poly(4*x**3, x, modulus=2).is_zero)
        self.assertEqual(16 % 2, 0)
        self.assertEqual(verify.plane_matrix(x, y)[1, 1], -2*x)

    def test_source_pins(self):
        sources = verify.check_pins()
        self.assertEqual(sources['base_commit'], '2c7854ac8a2e8b65b70c40d0ca16411072916542')
        self.assertFalse(sources['independent_review'])


if __name__ == '__main__':
    unittest.main()

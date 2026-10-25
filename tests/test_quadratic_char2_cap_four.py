"""Exact regressions for the characteristic-two cap-four algebra package."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-quadratic-char2-cap-four'
SPEC = importlib.util.spec_from_file_location('char2_cap_four', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class CharacteristicTwoCapFourTests(unittest.TestCase):
    def test_report_replay_and_evidence_scope(self):
        saved = json.loads((ROOT / 'results/quadratic-char2-cap-four-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertEqual(saved['upper_bound_all_fields_with_pinned_odd_proof'], 4)
        self.assertEqual(saved['lower_bound_all_fields_from_pinned_construction'], 3)
        for key in ('sharpness_supplied', 'independent_review', 'lean_formalized',
                    'improves_omega', 'computer_certifies_geometric_classification'):
            self.assertFalse(saved[key])

    def test_discovery_cubic_error_is_rejected(self):
        original = verify.eta_coefficients
        def broken(p, q, r, s, u, v):
            coefficients = original(p, q, r, s, u, v)
            coefficients[2] = (p+s)*r*v+(p*s+q*r)*u
            return coefficients
        with patch.object(verify, 'eta_coefficients', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'eta Taylor coefficient 3'):
                verify.report()

    def test_missing_mixed_quartic_term_is_rejected(self):
        original = verify.invariants
        def broken(M):
            D, A, T = original(M)
            return D, A, T-M[0, 1]*M[1, 0]*M[1, 2]*M[2, 1]
        with patch.object(verify, 'invariants', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'transverse_compression'):
                verify.report()

    def test_independent_eta_minors(self):
        p, q, r, s, u, v, t = sp.symbols('p q r s u v t')
        rows = [[1+p*t, q*t], [r*t, 1+s*t], [u*t, v*t]]
        m01 = rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0]
        m02 = rows[0][0]*rows[2][1]-rows[0][1]*rows[2][0]
        m12 = rows[1][0]*rows[2][1]-rows[1][1]*rows[2][0]
        direct = sp.Poly(m02*m02+m01*m12, t)
        for j, expected in enumerate(verify.eta_coefficients(p, q, r, s, u, v), 1):
            self.assertTrue(sp.Poly(direct.coeff_monomial(t**j)-expected,
                                    p, q, r, s, u, v, modulus=2).is_zero)

    def test_source_pins_and_corruption(self):
        sources = verify.check_pins()
        self.assertEqual(sources['base_commit'], 'badc9ff77698a34d651594051145f2def46e8c4e')
        self.assertFalse(sources['independent_review'])
        sources['local_dependencies'][0]['sha256'] = '0'*64
        with patch.object(verify.json, 'loads', return_value=sources):
            with self.assertRaisesRegex(ArithmeticError, 'source pin:'):
                verify.check_pins()


if __name__ == '__main__':
    unittest.main()

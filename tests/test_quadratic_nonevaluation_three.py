"""Characteristic-uniform source certificates and dual conic-type regressions."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-quadratic-nonevaluation-three'
SPEC = importlib.util.spec_from_file_location('nonevaluation_three', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class NonevaluationThreeTests(unittest.TestCase):
    def test_saved_certificate_and_scope(self):
        saved = json.loads((ROOT / 'results/quadratic-nonevaluation-three-2026-10-25/certificate.json').read_text())
        self.assertEqual(verify.report(), saved)
        for key in ('computer_certifies_geometric_exhaustion', 'complete_char2_classification',
                    'independent_review', 'lean_formalized', 'improves_omega'):
            self.assertFalse(saved[key])

    def test_independent_pair_indexed_minor(self):
        t, x, y = sp.symbols('t x y')
        coefficients = {(0, 0): x, (1, 0): y, (1, 1): t, (1, 2): x, (2, 2): y}
        rows = [(j, L) for j in range(3) for L in range(5) if (j, L) != (0, 3)]
        cols = [(H, r) for H in range(5) for r in range(3) if (H, r) != (0, 0)]
        minor = sp.Matrix([[coefficients.get((H-j, L-r), 0) for H, r in cols] for j, L in rows])
        self.assertEqual(sp.factor(minor.det(method='domain-ge')), t*t*x**4*y**8)
        saved = json.loads((ROOT / 'results/quadratic-nonevaluation-three-2026-10-25/certificate.json').read_text())
        self.assertEqual(minor.subs({t: 1, x: 1, y: 1}).tolist(), saved['base_minor_matrix'])

    def test_twice_term_is_required_integrally(self):
        t, x, y = sp.symbols('t x y')
        v = verify.kernel(t, x, y); v[1] = 0
        residual = verify.literal_source(verify.family(t, x, y))*v
        self.assertTrue(any(sp.expand(entry) != 0 for entry in residual))
        self.assertTrue(all(sp.Poly(entry, t, x, y, modulus=2).is_zero for entry in residual))
        with patch.object(verify, 'kernel', return_value=v):
            with self.assertRaisesRegex(ArithmeticError, 'integer source kernel'):
                verify.report()

    def test_left_kernel_sign_is_required_integrally(self):
        t, x, y = sp.symbols('t x y')
        w = verify.left_kernel(t, x, y); w[8] = y
        residual = verify.literal_source(verify.family(t, x, y)).T*w
        self.assertTrue(any(sp.expand(entry) != 0 for entry in residual))
        self.assertTrue(all(sp.Poly(entry, t, x, y, modulus=2).is_zero for entry in residual))
        with patch.object(verify, 'left_kernel', return_value=w):
            with self.assertRaisesRegex(ArithmeticError, 'integer left source kernel'):
                verify.report()

    def test_binary_action_must_include_ordinary_middle_coefficients(self):
        original = verify.binary_action
        def broken(a, b, c, d):
            A = original(a, b, c, d); A[1, 0] = 0
            return A
        with patch.object(verify, 'binary_action', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'dual conic covariance'):
                verify.conic_covariance()

    def test_source_endpoint_is_required(self):
        original = verify.literal_source
        def broken(M):
            R = original(M); R[14, 11] = 0
            return R
        with patch.object(verify, 'literal_source', side_effect=broken):
            with self.assertRaises(ArithmeticError):
                verify.report()

    def test_source_pin_corruption_is_rejected(self):
        sources = verify.check_pins(); target = ROOT / sources['local_dependencies'][0]['path']
        original = Path.read_bytes
        def corrupted(path):
            return original(path)+(b'corrupt' if path == target else b'')
        with patch.object(Path, 'read_bytes', new=corrupted):
            with self.assertRaisesRegex(ArithmeticError, 'source pin'):
                verify.check_pins()


if __name__ == '__main__':
    unittest.main()

"""Universal source rank certificates and the actual discovery-error regression."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-quadratic-universal-three-plane'
SPEC = importlib.util.spec_from_file_location('universal_three_plane', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class UniversalThreePlaneTests(unittest.TestCase):
    def test_exact_report_and_scope(self):
        saved = json.loads((ROOT / 'results/quadratic-universal-three-plane-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertEqual(saved['dimension'], 3)
        self.assertEqual(saved['lower_bound_all_fields'], 3)
        self.assertEqual(saved['upper_bound_characteristic_not_two'], 4)
        self.assertEqual(saved['upper_bound_characteristic_two'], 5)
        self.assertFalse(saved['sharpness_supplied'])
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_independent_pair_indexed_symbolic_minor(self):
        x, y, z = sp.symbols('x y z')
        M = [[x, x, 0], [0, y, 0], [0, z, z]]
        rows = [(j, L) for j in range(3) for L in range(5) if (j, L) != (2, 4)]
        cols = [(H, r) for H in range(5) for r in range(3) if (H, r) != (4, 0)]
        minor = sp.Matrix([[M[H-j][L-r] if 0 <= H-j < 3 and 0 <= L-r < 3 else 0
                            for H, r in cols] for j, L in rows])
        self.assertEqual(sp.factor(minor.det(method='domain-ge')), -x**6*y**3*z**5)
        saved = json.loads((ROOT / 'results/quadratic-universal-three-plane-2026-10-25/controls.json').read_text())
        self.assertEqual(minor.subs({x: 1, y: 1, z: 1}).tolist(), saved['base_minor_matrix'])
        self.assertEqual(saved['base_minor_determinant'], -1)

    def test_discovery_omitted_two_ai_is_rejected(self):
        original = verify.integer_invariants
        def broken(M):
            D, A2, T4, P12 = original(M)
            return D, A2-2*M[0, 0]*M[2, 2], T4, P12
        with patch.object(verify, 'integer_invariants', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'integer A2'):
                verify.report()

    def test_missing_kernel_term_is_rejected(self):
        original = verify.kernel_vector
        def broken(x, y, z):
            v = original(x, y, z)
            v[2] = 0
            return v
        with patch.object(verify, 'kernel_vector', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'polynomial source kernel'):
                verify.report()

    def test_corrupted_literal_endpoint_is_rejected(self):
        original = verify.literal_source
        def broken(M):
            R = original(M)
            R[0, 2] += 1
            return R
        with patch.object(verify, 'literal_source', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'polynomial source kernel'):
                verify.report()

    def test_missing_f_determinant_derivative_is_rejected(self):
        original = verify.invariant_coordinates
        def broken(M):
            D, A, T = original(M)
            # Its linear term cancels the historically omitted -xz*f term.
            return D+M[0, 0]*M[2, 2]*M[1, 2], A, T
        with patch.object(verify, 'invariant_coordinates', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'complete determinant differential'):
                verify.extension_checks()

    def test_source_pins(self):
        data = verify.check_pins()
        self.assertEqual(data['base_commit'], '34b794c6f49e212a975397cde1fa916a318d4507')
        self.assertFalse(data['independent_review'])


if __name__ == '__main__':
    unittest.main()

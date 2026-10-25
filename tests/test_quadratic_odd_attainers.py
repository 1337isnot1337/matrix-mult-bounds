"""Exact replay and discovery-error guards for the attainer classification."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-quadratic-odd-attainers'
SPEC = importlib.util.spec_from_file_location('odd_attainers', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class OddAttainerTests(unittest.TestCase):
    def test_exact_report_and_scope(self):
        saved = json.loads((ROOT / 'results/quadratic-odd-attainers-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertFalse(saved['computer_certifies_geometric_classification'])
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_reversed_kernel_normalizer_is_rejected(self):
        with patch.object(verify, 'kernel_normalizer', side_effect=lambda r: sp.Matrix([[1, r], [0, 1]])):
            with self.assertRaisesRegex(ArithmeticError, 'kernel normalizer orientation'):
                verify.report()

    def test_false_zero_mixed_compression_is_rejected(self):
        original = verify.invariants
        def broken(M):
            D, A, T = original(M)
            return D, A, T-M[0, 0]*M[0, 2]*M[2, 1]**2
        with patch.object(verify, 'invariants', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'compression quartic'):
                verify.compression_checks()

    def test_missing_adfi_term_is_rejected(self):
        original = verify.invariants
        def broken(M):
            D, A, T = original(M)
            return D, A, sp.expand(T+M[0, 0]*M[1, 0]*M[1, 2]*M[2, 2])
        with patch.object(verify, 'invariants', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'eta second coefficient'):
                verify.rank_one_eta_checks()

    def test_missing_df_complement_obstruction_is_rejected(self):
        original = verify.invariants
        def broken(M):
            D, A, T = original(M)
            return D, A+M[1, 0]*M[1, 2], T
        with patch.object(verify, 'invariants', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'nonsingular first-column identity'):
                verify.section_checks()

    def test_characteristic_three_normalization_and_surviving_root(self):
        r, t, a = sp.symbols('r t a')
        kernel = sp.Matrix([1, r, r*r])
        column = sp.Matrix([1, 2*r, r*r])
        expected = sp.Matrix([1, 0, 0])
        h = sp.Matrix([[1, 0], [r, 1]])
        g = sp.Matrix([[1, -r], [0, 1]])
        for vector in (verify.binary_action(h).inv().T*kernel-expected,
                       verify.binary_action(g)*column-expected):
            for entry in vector:
                self.assertTrue(sp.Poly(sp.expand(entry), r, modulus=3).is_zero)
        equation = sp.Poly((a-1)**2*(2*a-1), a, modulus=3)
        self.assertEqual([value for value in range(3) if equation.eval(value) % 3 == 0], [1, 2])
        self.assertEqual(sp.Poly(32*t**3, t, modulus=3).as_expr(), -t**3)
        # In characteristic three the two conic equations coincide, but their
        # coefficient actions and correct normalization matrices still differ.
        self.assertTrue(sp.Poly(4*r*r-r*r, r, modulus=3).is_zero)

    def test_source_pins_and_corruption(self):
        data = verify.check_pins()
        self.assertFalse(data['independent_review'])
        target = ROOT / data['local_dependencies'][0]['path']
        original = Path.read_bytes
        def corrupted(path):
            return original(path)+(b'corrupt' if path == target else b'')
        with patch.object(Path, 'read_bytes', new=corrupted):
            with self.assertRaisesRegex(ArithmeticError, 'source pin'):
                verify.check_pins()


if __name__ == '__main__':
    unittest.main()

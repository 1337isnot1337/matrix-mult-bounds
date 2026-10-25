"""Literal-source and characteristic-uniform certificate regressions."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-quadratic-chain-three'
SPEC = importlib.util.spec_from_file_location('chain_three', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class ChainThreeTests(unittest.TestCase):
    def test_saved_exact_certificate_and_scope(self):
        saved = json.loads((ROOT / 'results/quadratic-chain-three-2026-10-25/certificate.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertFalse(saved['complete_char2_classification'])
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_independent_pair_indexed_minor(self):
        t, x, y = sp.symbols('t x y')
        coefficients = {(0, 0): t, (0, 1): x, (1, 1): t, (1, 2): x, (2, 1): y}
        rows = [(j, L) for j in range(3) for L in range(5) if (j, L) != (0, 0)]
        cols = [(H, r) for H in range(5) for r in range(3) if (H, r) != (0, 2)]
        minor = sp.Matrix([[coefficients.get((H-j, L-r), 0) for H, r in cols] for j, L in rows])
        self.assertEqual(sp.factor(minor.det(method='domain-ge')), -t*t*x**7*y**5)
        saved = json.loads((ROOT / 'results/quadratic-chain-three-2026-10-25/certificate.json').read_text())
        self.assertEqual(minor.subs({t: 1, x: 1, y: 1}).tolist(), saved['base_minor_matrix'])

    def test_omitted_twotx_only_works_in_characteristic_two(self):
        t, x, y = sp.symbols('t x y')
        v = verify.kernel(t, x, y); v[13] = 0
        residual = verify.literal_source(verify.family(t, x, y))*v
        self.assertNotEqual(residual, sp.zeros(15, 1))
        self.assertTrue(all(sp.Poly(entry, t, x, y, modulus=2).is_zero for entry in residual))
        with patch.object(verify, 'kernel', return_value=v):
            with self.assertRaisesRegex(ArithmeticError, 'integer source kernel'):
                verify.report()

    def test_full_source_endpoint_is_required(self):
        original = verify.literal_source
        def broken(M):
            R = original(M); R[14, 11] = 0
            return R
        with patch.object(verify, 'literal_source', side_effect=broken):
            with self.assertRaises(ArithmeticError):
                verify.report()

    def test_section_distinction_and_odd_obstruction_small_characteristics(self):
        data = verify.section_checks()
        self.assertNotEqual(sorted(data['new_right_left_kernel_dimensions']), sorted(data['earlier_right_left_kernel_dimensions']))
        t, x, y = sp.symbols('t x y')
        for p in (3, 5, 7):
            self.assertEqual(sp.Poly(t**3+16*t*x*y, t, x, y, modulus=p).coeff_monomial(t**3), 1)
        self.assertEqual(data['section_unit_minors'], [1, 1, 1, 1])

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

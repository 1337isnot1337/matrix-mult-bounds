"""Replay and corruption guards for the odd-characteristic four-space."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-quadratic-odd-sharp-four'
SPEC = importlib.util.spec_from_file_location('odd_sharp_four', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class OddSharpFourTests(unittest.TestCase):
    def test_exact_report_and_scope(self):
        saved = json.loads((ROOT / 'results/quadratic-odd-sharp-four-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertEqual(saved['dimension'], 4)
        self.assertEqual(saved['source_rank_at_every_invertible_coefficient_point'], 14)
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_pair_indexed_minor_and_characteristic_boundary(self):
        t, b, c, f = sp.symbols('t b c f')
        M = [[8*t, b, c], [0, 4*t, f], [0, 0, t]]
        rows = [(j, L) for j in range(3) for L in range(5) if (j, L) != (2, 1)]
        cols = [(H, r) for H in range(5) for r in range(3) if (H, r) != (1, 2)]
        minor = sp.Matrix([[M[H-j][L-r] if 0 <= H-j < 3 and 0 <= L-r < 3 else 0
                            for H, r in cols] for j, L in rows])
        self.assertEqual(sp.factor(minor.det(method='domain-ge')), -2**18*t**14)
        self.assertEqual(sp.Poly(sp.Matrix(M).det(), t, b, c, f, modulus=2).as_expr(), 0)
        self.assertEqual(sp.factorint(abs(int(minor.subs({t: 1, b: 0, c: 0, f: 0}).det()))), {2: 18})

    def test_missing_free_parameter_kernel_terms_are_rejected(self):
        original = verify.kernel_vector
        for index in (8, 10, 11, 12, 13, 14):
            def broken(*args):
                v = original(*args)
                v[index] = 0
                return v
            with self.subTest(index=index), patch.object(verify, 'kernel_vector', side_effect=broken):
                with self.assertRaisesRegex(ArithmeticError, 'polynomial source kernel'):
                    verify.report()

    def test_corrupted_literal_endpoint_is_rejected(self):
        original = verify.literal_source
        def broken(M):
            R = original(M)
            R[0, 5] += 1
            return R
        with patch.object(verify, 'literal_source', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'polynomial source kernel'):
                verify.report()

    def test_source_pins(self):
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

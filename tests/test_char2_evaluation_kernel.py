"""Regression controls for the two characteristic-two chart proofs."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-char2-evaluation-kernel'
SPEC = importlib.util.spec_from_file_location('char2_eval', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class EvaluationKernelTests(unittest.TestCase):
    def test_exact_report_and_scope(self):
        saved = json.loads((ROOT / 'results/char2-evaluation-kernel-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertFalse(saved['complete_char2_attainer_classification'])
        self.assertFalse(saved['arbitrary_ground_field_descent_proved'])
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_omitted_mixed_term_is_rejected(self):
        original = verify.square_divided_C
        def broken(t, b, c, f, i, rho, mu):
            return original(t, b, c, f, i, rho, mu)-rho*b*i
        with patch.object(verify, 'square_divided_C', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'square h-zero mixed term'):
                verify.square_checks()

    def test_missing_cth_is_rejected(self):
        original = verify.chart_equations
        def broken(t, b, c, f, h, i, ell, square):
            Q, C = original(t, b, c, f, h, i, ell, square)
            return Q, C if square else C-c*t*h
        with patch.object(verify, 'chart_equations', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'integral chart C'):
                verify.report()

    def test_binary_action_middle_entry_mutation_is_rejected(self):
        original = verify.binary_action
        def broken(g):
            result = original(g); result[1, 0] = g[1, 0]
            return result
        with patch.object(verify, 'binary_action', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'square shear'):
                verify.action_checks()

    def test_nonunit_denominator_is_rejected(self):
        x = sp.symbols('x')
        with self.assertRaisesRegex(ArithmeticError, 'denominator vanishes'):
            verify.residue(x/2)
        self.assertEqual(verify.residue(2*x), 0)

    def test_pins_and_corruption(self):
        data = verify.check_pins(); target = ROOT / data['local_dependencies'][0]['path']
        original = Path.read_bytes
        def corrupted(path):
            return original(path)+(b'corrupt' if path == target else b'')
        with patch.object(Path, 'read_bytes', new=corrupted):
            with self.assertRaisesRegex(ArithmeticError, 'source pin'):
                verify.check_pins()


if __name__ == '__main__':
    unittest.main()

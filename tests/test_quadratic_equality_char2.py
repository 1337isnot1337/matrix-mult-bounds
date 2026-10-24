"""Characteristic-two equality witnesses and a caught quartic omission."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-24-quadratic-equality'
SPEC = importlib.util.spec_from_file_location('quadratic_equality_char2', PACKAGE / 'verify_char2.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class QuadraticEqualityChar2Tests(unittest.TestCase):
    def test_complete_polynomial_report(self):
        saved = json.loads((ROOT / 'results/quadratic-equality-2026-10-24/char2-controls.json').read_text())
        self.assertEqual(verify.symbolic_checks(), saved)
        self.assertEqual(saved['literal_control_count'], 5)
        self.assertEqual(saved['middle_column_highest_degree'], 12)
        self.assertTrue(saved['middle_column_quartic_includes_adfi'])
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_original_missing_adfi_term_is_rejected(self):
        correct = verify.top_quartic
        def missing(a, c, d, f, g, i):
            return correct(a, c, d, f, g, i)-a*d*f*i
        with patch.object(verify, 'top_quartic', side_effect=missing):
            with self.assertRaisesRegex(ArithmeticError, 'quartic including adfi'):
                verify.symbolic_checks()

    def test_false_literal_source_result_is_rejected(self):
        with patch.object(verify, 'literal_determinant', return_value=sp.Integer(0)):
            with self.assertRaisesRegex(ArithmeticError, 'literal source identity'):
                verify.symbolic_checks()

    def test_escape_polynomial_is_not_a_finite_point_inference(self):
        t, d = sp.symbols('t d')
        M = sp.Matrix([[t, t, 0], [d+1, 1, 0], [0, 0, 1]])
        polynomial = sp.Poly(verify.literal_determinant(M), t)
        # The leading coefficient is d^2, so every nonzero d leaves a
        # nonzero polynomial over any characteristic-two extension field.
        self.assertEqual(polynomial.degree(), 6)
        self.assertEqual(polynomial.LC(), d*d)

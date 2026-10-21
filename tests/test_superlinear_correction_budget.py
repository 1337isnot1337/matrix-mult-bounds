"""Exact controls for the larger conditional auxiliary-rank budget."""
from fractions import Fraction
from pathlib import Path
import importlib.util
import unittest

PATH = Path(__file__).resolve().parents[1] / 'research/ai/2026-10-21-correction-budget/superlinear_budget.py'
SPEC = importlib.util.spec_from_file_location('superlinear_correction_budget', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SuperlinearCorrectionBudgetTests(unittest.TestCase):
    def test_exact_bounds_and_independent_product_expansion(self):
        report = MODULE.certificate()
        self.assertTrue(report['exact_root_comparison_passed'])
        self.assertFalse(report['construction_supplied'])
        self.assertFalse(report['improves_omega'])
        self.assertGreater(report['algebraic_angular_points'], 0)
        for row in report['examples']:
            self.assertGreater(row['parameter_controls'], 0)
            self.assertGreater(Fraction(row['minimum_observed_gap']), 0)
        self.assertEqual([r['retains_strict_30000_over_13433'] for r in report['examples']],
                         [True, True, True, False, False])

    def test_strict_boundary_and_invalid_quantitative_rates(self):
        self.assertEqual(MODULE.correction_gaps([Fraction(3, 4)] * 3, Fraction(3, 2)), [0] * 7)
        for alpha in [Fraction(1, 2), Fraction(3, 2), Fraction(2)]:
            with self.assertRaises(ValueError):
                MODULE.localization_threshold(alpha)


if __name__ == '__main__':
    unittest.main()

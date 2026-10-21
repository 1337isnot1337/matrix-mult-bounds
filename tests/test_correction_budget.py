"""Exact certificate checks, not a test or claim of the missing construction."""
from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'paired_correction_budget', ROOT / 'research/ai/2026-10-21-correction-budget/verify.py')
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class CorrectionBudgetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = module.certificate()

    def test_exact_root_and_conditional_status(self):
        r = self.report
        self.assertTrue(r['root_certificate']['strict_comparison_passes'])
        self.assertLess(Fraction(30000, 13433), Fraction(11167, 5000))
        self.assertGreater(Fraction(30000, 13433), 2)
        self.assertFalse(r['construction_supplied'])
        self.assertFalse(r['improves_omega'])

    def test_width_threshold_and_boundary_restorations(self):
        self.assertEqual(self.report['first_admissible_integer_width'], 4)
        self.assertLess(81 * 3, 256)
        self.assertGreater(81 * 4, 256)
        self.assertGreater(self.report['rational_parameter_controls'], 0)
        rows = self.report['boundary_controls']
        self.assertEqual(len(rows), 80)
        for row in rows:
            self.assertEqual(row['complete_coefficients'], row['b'] * row['n'] ** 2)
            if row['pattern'] == 'diagonal':
                self.assertEqual(row['rank_one_terms'], row['b'] * row['n'])


if __name__ == '__main__':
    unittest.main()

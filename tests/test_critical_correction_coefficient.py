"""Exact positive, negative and equality controls for a conditional budget."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "critical_correction_coefficient",
    ROOT / "research/ai/2026-10-21-correction-budget/critical_coefficient.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CriticalCorrectionCoefficientTests(unittest.TestCase):
    def test_strict_budget_and_rejected_boundaries(self):
        report = MODULE.verify()
        self.assertEqual(report["width_four_squared_margin"], [56, 5625])
        rows = report["exact_examples_and_negative_controls"]
        self.assertEqual([r["strict_sufficient_budget"] for r in rows],
                         [True, False, True, False, True, True])
        self.assertTrue(rows[3]["equality_is_not_accepted"])

    def test_quantified_implication_has_no_constructed_witness(self):
        report = MODULE.verify()
        self.assertTrue(report["source_constant_cube_identity_checked"])
        self.assertFalse(report["required_unbounded_maps_constructed"])
        self.assertFalse(report["explicit_smaller_exponent_proved"])
        self.assertFalse(report["improves_omega"])


if __name__ == "__main__":
    unittest.main()

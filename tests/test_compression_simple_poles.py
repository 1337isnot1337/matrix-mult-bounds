"""Exact fixed-compression defect and simple-pole controls."""

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-anisotropic-constructions"))
import compression_simple_poles as poles


class CompressionSimplePoleTests(unittest.TestCase):
    def test_defect_identity_and_leading_order_contradictions(self):
        actual = poles.report()
        saved = json.loads((ROOT / "results/anisotropic-constructions-2026-10-20/compression-simple-poles-controls.json").read_text())
        self.assertEqual(actual, saved)
        self.assertEqual(actual["defect_formula"]["complete_trilinear_coefficients_checked"], 729)
        self.assertEqual(len(actual["two_normal_forms_and_four_transports"]), 6)
        self.assertTrue(all(row["quadratic_coefficients_checked"] == 729
                            for row in actual["complete_rank_one_leading_controls"]))
        self.assertTrue(all(row["twice_nonzero_linear_obstruction"]
                            for row in actual["complete_rank_one_leading_controls"]))
        self.assertFalse(actual["several_negative_orders_excluded"])
        self.assertFalse(actual["moving_physical_bases_excluded"])
        self.assertFalse(actual["arbitrary_degenerations_excluded"])
        self.assertFalse(actual["new_exponent_established"])


if __name__ == "__main__":
    unittest.main()

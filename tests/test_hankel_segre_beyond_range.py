"""Protect the stated range of the ordinary Hankel/Segre argument."""

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-anisotropic-constructions"))
import hankel_segre_beyond_range as examples


class HankelSegreBeyondRangeTests(unittest.TestCase):
    def test_exact_square_domain_counterexample(self):
        self.assertEqual(examples.determinant_polynomial(), {
            (2, 0, 0, 2): 1, (1, 1, 1, 1): -2, (0, 2, 2, 0): 1,
        })
        result = examples.report()
        square = result["square_domain_counterexample"]
        self.assertGreater(square["image_dimension"], square["r"])
        self.assertEqual(square["hankel_rank"], square["r"])
        self.assertFalse(result["proved_frontier_changed"])
        self.assertFalse(result["new_tensor_restriction_claimed"])

    def test_saved_formal_recurrence_controls(self):
        saved = json.loads((ROOT / "results/anisotropic-constructions-2026-10-20/hankel-segre-beyond-range.json").read_text())
        self.assertEqual(saved, examples.report())
        boundary = [row for row in saved["family_controls"] if (row["a"], row["b"], row["r"]) == (7, 8, 5)]
        self.assertEqual(len(boundary), 1)
        self.assertEqual(boundary[0]["image_dimension"], 2)
        self.assertFalse(boundary[0]["image_dimension_exceeds_r"])
        self.assertTrue(all(row["formal_recurrence_verified"] for row in saved["family_controls"]))


if __name__ == "__main__":
    unittest.main()

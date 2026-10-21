"""Exact tangent/secant controls at twice the minimum slice rank."""

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/"research/ai/2026-10-20-anisotropic-constructions"
sys.path.insert(0, str(PACKAGE))
import hankel_rank_two as geometry


class HankelRankTwoTests(unittest.TestCase):
    def test_integer_factorizations_and_saved_report(self):
        actual = geometry.report()
        saved = json.loads((ROOT/"results/anisotropic-constructions-2026-10-20/hankel-rank-two-controls.json").read_text())
        self.assertEqual(actual, saved)
        self.assertEqual(sum(x["integer_coefficients_compared"] for x in actual["factorization_controls"]), 1296000)
        self.assertFalse(actual["new_exponent_established"])
        self.assertFalse(actual["singular_exclusion_claimed"])

    def test_equality_exclusion_does_not_overextend(self):
        self.assertTrue(geometry.equality_block_screen(5, 6, 4, 272)["ordinary_restriction_excluded"])
        self.assertFalse(geometry.equality_block_screen(5, 6, 3, 271)["ordinary_restriction_excluded"])
        self.assertFalse(geometry.equality_block_screen(5, 6, 2, 271)["ordinary_restriction_excluded"])
        self.assertFalse(geometry.equality_block_screen(3, 3, 3, 45)["lemma_hypotheses_hold"])


if __name__ == "__main__":
    unittest.main()

"""Exact coordinate and scope controls for cyclic quotient volume."""

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-anisotropic-constructions"))
import cyclic_quotient_volume as quotient


class CyclicQuotientVolumeTests(unittest.TestCase):
    def test_sharp_maps_and_failed_oversized_inclusions(self):
        actual = quotient.report()
        saved = json.loads((ROOT / "results/anisotropic-constructions-2026-10-20/cyclic-quotient-volume-controls.json").read_text())
        self.assertEqual(actual, saved)
        self.assertEqual(len(actual["sharp_triangular_projections"]), 7)
        self.assertEqual(len(actual["oversized_coordinate_quotients"]), 3)
        self.assertEqual(actual["sharp_triangular_projections"][-1]["quotient_dimension"], 15)
        self.assertTrue(all(row["rational_block_rank_certified_exact"]
                            for row in actual["sharp_triangular_projections"]))
        self.assertTrue(all(row["exact_common_block_inclusion_fails"]
                            for row in actual["oversized_coordinate_quotients"]))
        self.assertFalse(actual["arbitrary_restrictions_excluded"])
        self.assertFalse(actual["arbitrary_degenerations_excluded"])
        self.assertFalse(actual["new_exponent_established"])


if __name__ == "__main__":
    unittest.main()

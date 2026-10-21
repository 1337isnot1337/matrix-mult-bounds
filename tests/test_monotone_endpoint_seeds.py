"""Full coefficient replay for monotone endpoint source maps."""

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"research/ai/2026-10-20-anisotropic-constructions"))
import monotone_endpoint_seeds as seeds


class MonotoneEndpointSeedTests(unittest.TestCase):
    def test_all_source_terms_and_live_format_embedding(self):
        actual = seeds.report()
        saved = json.loads((ROOT/"results/anisotropic-constructions-2026-10-20/monotone-endpoint-seeds.json").read_text())
        self.assertEqual(actual,saved)
        self.assertEqual([row["target_size"] for row in actual["cases"]],[2,4,4,8])
        self.assertEqual(actual["cases"][-1]["source_terms_checked"],262144)
        self.assertEqual(actual["cases"][-1]["exact_nonzero_target_coefficients"],512)
        self.assertFalse(actual["cases"][-1]["full_target_restriction_established"])
        self.assertFalse(actual["new_exponent_established"])

    def test_invalid_monotonicity_and_coefficient_tamper(self):
        with self.assertRaises(ValueError):
            seeds.build_maps(2,2,[(0,0),(1,1)])
        maps = seeds.build_maps(2,3,[(0,2),(1,0)])
        maps[0][0][2] = 2
        actual,_ = seeds.contract(2,3,maps)
        self.assertNotEqual(actual,seeds.target(2))


if __name__ == "__main__":
    unittest.main()

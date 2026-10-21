"""Exact controls for the proved first-boundary symbol dimension statement."""

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-anisotropic-constructions"))
import hankel_boundary_dimension as boundary


class HankelBoundaryDimensionTests(unittest.TestCase):
    def test_repeated_endpoint_pencils_and_second_jet_relations(self):
        actual = boundary.report()
        saved = json.loads((ROOT / "results/anisotropic-constructions-2026-10-20/hankel-boundary-dimension-controls.json").read_text())
        self.assertEqual(actual, saved)
        self.assertEqual(len(actual["moving_line_controls"]), 5)
        for row in actual["moving_line_controls"]:
            self.assertEqual(row["sequence_length"], 3*row["r"]-1)
            self.assertTrue(row["parameter_two_annihilator_is_reduced_mod_101"])
            self.assertTrue(all(case["unique_annihilator_recovered_over_Q"] for case in row["specializations"]))
        for row in actual["second_jet_controls"]:
            self.assertTrue(all(row["highest_jet_relation_coefficients"]))
        self.assertFalse(actual["singular_exclusion_claimed"])
        self.assertFalse(actual["new_exponent_established"])

    def test_boundary_hypotheses_and_strict_projection_threshold(self):
        self.assertEqual(boundary.boundary_dimension_cap(7, 8, 5), 5)
        self.assertEqual(boundary.boundary_dimension_cap(4, 5, 3), 4)
        for parameters in ((7, 8, 4), (7, 8, 6), (4, 4, 3), (2, 3, 2)):
            with self.assertRaises(ValueError):
                boundary.boundary_dimension_cap(*parameters)
        self.assertTrue(boundary.square_block_test(7, 8, 5, 25, 650)["ordinary_restriction_excluded"])
        self.assertFalse(boundary.square_block_test(7, 8, 5, 25, 625)["ordinary_restriction_excluded"])
        self.assertFalse(boundary.square_block_test(7, 8, 5, 25, 628)["ordinary_restriction_excluded"])
        self.assertTrue(boundary.square_block_test(7, 8, 5, 25, 629)["ordinary_restriction_excluded"])
        self.assertFalse(boundary.square_block_test(7, 8, 5, 24, 628)["ordinary_restriction_excluded"])
        self.assertTrue(boundary.square_block_test(7, 8, 5, 24, 629)["ordinary_restriction_excluded"])


if __name__ == "__main__":
    unittest.main()

"""Replay the exact controls and reject altered boundaries and source pins."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-long-leg-rank-obstruction"
SPEC = importlib.util.spec_from_file_location("long_leg_rank_obstruction", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class LongLegRankObstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_complete_exact_replay(self):
        self.assertEqual(v.verify(self.record), {
            "residual_families": 12,
            "sharp_rank_loss_controls": 15,
            "scalar_valuation_controls": 5,
            "spanning_matrix_units": 100,
            "minimum_slice_factorizations": 3,
            "row_space_intersections": 3,
            "sextic_cubic_divisors": 20,
            "bounded_rank_space_controls": 3,
            "normalized_rank_pairs": 12100,
            "improves_omega": False,
        })

    def test_zero_unit_images_and_raw_laurent_coefficients(self):
        residuals = self.record["residuals"]
        self.assertEqual(sum(row["limiting_unit_image_rank"] == 0 for row in residuals), 6)
        boundary = self.record["boundary_controls"]
        self.assertEqual(boundary["raw_laurent_generic_rank"], 1)
        self.assertEqual(boundary["raw_constant_rank"], 2)
        self.assertEqual(boundary["regularized_limit_rank"], 1)
        self.assertTrue(boundary["without_full_row_target_slice"]["degeneration_exists"])
        self.assertFalse(boundary["without_full_row_target_slice"]["has_full_row_target_slice"])

    def test_corank_one_geometry_and_unclaimed_boundary(self):
        case = self.record["corank_one"]
        self.assertEqual(case["minimum_first_kernel_dimension"], 96)
        self.assertEqual(case["maximum_singular_matrix_space_dimension"], 90)
        self.assertGreater(case["minimum_unit_image_rank"], case["maximum_kernel_residual_rank"])
        self.assertFalse(case["excludes_leading_rank_108"])
        ranks = self.record["normalized_leading_ranks"]
        self.assertEqual(ranks["maximum_remaining_rank_sum"], 208)
        self.assertEqual(ranks["individual_rank_cap_from_corank_one_theorem"], 108)
        self.assertFalse(ranks["boundary_is_construction"])

    def test_reject_corrupted_geometry_or_overstated_scope(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(proof_status="reviewed-proof"),
            lambda x: x["corank_one"].update(excludes_leading_rank_108=True),
            lambda x: x["corank_one"].update(maximum_first_map_rank=16),
            lambda x: x["row_space_intersections"][1].update(common_sextic_space_dimension=1),
            lambda x: x["normalized_leading_ranks"].update(maximum_remaining_rank_sum=207),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_predecessor_changes_and_removed_attribution(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for index in range(len(original["local_dependencies"])):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][index]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        bad = copy.deepcopy(original)
        bad["local_dependencies"].pop()
        with self.assertRaises(ValueError):
            v.check_sources(bad)
        bad = copy.deepcopy(original)
        bad["concurrent_predecessor"]["commit"] = "0"*40
        with self.assertRaises(ValueError):
            v.check_sources(bad)


if __name__ == "__main__":
    unittest.main()

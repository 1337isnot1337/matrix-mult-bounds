"""Shared correction spaces, target rulings and the rank20 source boundary."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-singular-long-ruling"
SPEC = importlib.util.spec_from_file_location("singular_long_ruling", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class SingularLongRulingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_exact_control_replay(self):
        self.assertEqual(v.verify(self.record), {
            "shared_correction_families": 9, "target_rulings": 12,
            "minimum_source_slices": 6, "first_gap_source_rank": 20,
            "a4_long_limit_cases": 7, "minimum_excluded_long_limit_rank": 106,
            "improves_omega": False,
        })

    def test_boundary_does_not_import_the_minimum_cone_at_rank20(self):
        yes, no = v.a4_criterion(106), v.a4_criterion(105)
        self.assertTrue(yes["excluded_by_this_criterion"])
        self.assertEqual(yes["source_rank_cap"], 19)
        self.assertEqual(yes["nonzero_lift_margin"], 8)
        self.assertFalse(no["excluded_by_this_criterion"])
        self.assertEqual(no["source_rank_cap"], 20)
        self.assertIsNone(no["source_ruling_dimension_bound"])
        for rank in (-1, 111, True):
            with self.subTest(rank=rank), self.assertRaises(ValueError):
                v.a4_criterion(rank)

    def test_individual_rank_bounds_do_not_supply_a_shared_space(self):
        negative = self.record["individual_rank_negative_control"]
        self.assertEqual(negative["individual_ranks"], [1, 1])
        self.assertEqual(negative["joint_rank"], 2)
        self.assertFalse(negative["compatible_with_common_rank_one_projector"])
        self.assertEqual({c["unit_image_rank"] for c in self.record["shared_corrections"]},
                         {0, 2, 3})

    def test_reject_false_boundary_shared_rank_and_review_status(self):
        for mutate in (
            lambda x: x.update(independent_review=True),
            lambda x: x["a4_long_limit_cases"][5].update(excluded_by_this_criterion=True),
            lambda x: x["shared_corrections"][0].update(constant_joint_rank=0),
            lambda x: x["first_gap_source_witness"].update(slice_rank=16),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_missing_pins_or_external_attribution(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(2):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        bad = copy.deepcopy(original)
        bad["local_dependencies"].pop()
        with self.assertRaises(ValueError):
            v.check_sources(bad)
        bad = copy.deepcopy(original)
        bad["external_dependency_in_prior_gap_proof"]["theorem"] = "unverified"
        with self.assertRaises(ValueError):
            v.check_sources(bad)


if __name__ == "__main__":
    unittest.main()

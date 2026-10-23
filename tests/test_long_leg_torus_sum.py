"""Reconstruct adopted torus minors and the new normalized sum200 deduction."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-long-leg-rank-obstruction"
SPEC = importlib.util.spec_from_file_location("long_leg_torus_sum", PACKAGE / "verify_torus_sum.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class LongLegTorusSumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_complete_local_replay(self):
        self.assertEqual(v.verify(self.record), {
            "literal_source_terms": 4096,
            "coordinate_ranks": 112,
            "cross_extreme_pairs": 256,
            "determinant_one_matching_minors": 16,
            "source_support_spaces": 2,
            "normalized_rank_pairs": 12100,
            "new_pairs_beyond_pr129_individual_cap": 3,
            "maximum_remaining_rank_sum": 200,
            "improves_omega": False,
        })

    def test_exact_new_scope_and_first_unexcluded_boundary(self):
        ranks = self.record["rank_budgets"]
        self.assertEqual(ranks["new_pairs_beyond_adopted_individual_cap"],
                         [[100, 101], [101, 100], [101, 101]])
        self.assertEqual(ranks["remaining_sum200_boundary_pairs"],
                         [[99, 101], [100, 100], [101, 99]])
        self.assertFalse(ranks["boundary_is_construction"])
        supports = self.record["source_supports"]
        self.assertEqual(supports["linear_spaces"][1]["parameter_dimension"], 12)
        self.assertEqual(supports["twelve_plane_witness_rank"], 24)
        self.assertTrue(supports["rank24_cap_eight_is_false"])

    def test_reject_corrupted_matching_and_overstated_claim(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(proof_status="reviewed-proof"),
            lambda x: x["matching_minors"][0].update(determinant=0),
            lambda x: x["matching_minors"][0]["rows"].pop(),
            lambda x: x["rank_budgets"].update(maximum_remaining_rank_sum=199),
            lambda x: x["source_supports"]["linear_spaces"][1].update(
                source_rank_upper_bound=23),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_missing_or_changed_source_credit(self):
        original = json.loads((PACKAGE / "torus_sources.json").read_text())
        mutations = [
            lambda x: x["adopted_source_cap"].update(commit="0"*40),
            lambda x: x["adopted_source_cap"].update(sha256="0"*64),
            lambda x: x["adopted_source_cap"].update(git_blob_sha="0"*40),
            lambda x: x["regular_kernel_predecessor"].update(commit="0"*40),
            lambda x: x["local_dependencies"].pop(),
            lambda x: x["concurrent_work"].pop(),
            lambda x: x.update(external_theorems_added=True),
        ]
        for mutate in mutations:
            bad = copy.deepcopy(original)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        for index in range(len(original["local_dependencies"])):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][index]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)


if __name__ == "__main__":
    unittest.main()

"""Replay gap-extension controls and reject changed dependencies or boundaries."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-long-leg-rank-obstruction"
SPEC = importlib.util.spec_from_file_location("long_leg_rank_gap", PACKAGE / "verify_gap.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class LongLegRankGapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_complete_exact_replay(self):
        self.assertEqual(v.verify(self.record), {
            "factored_or_transpose_kernel_units": 32,
            "fixed_factor_kernel_units": 2,
            "explicit_source_ranks": [16, 20, 24, 28],
            "negative_boundary_controls": 2,
            "normalized_rank_pairs": 12100,
            "source_pin_count": 5,
            "maximum_remaining_individual_rank": 105,
            "maximum_remaining_rank_sum": 204,
            "improves_omega": False,
        })

    def test_boundaries_reject_two_incorrect_shortcuts(self):
        boundary = self.record["boundaries"]
        self.assertEqual(boundary["rank_one_preserver_image_dimension_can_be"], 16)
        self.assertEqual(boundary["invertible_target_source_image_rank_can_be"], 28)
        large = boundary["oversized_output"]
        self.assertEqual(large["maximum_kernel_matrix_rank"], 8)
        self.assertFalse(large["kernel_contains_invertible"])
        ranks = self.record["rank_budgets"]
        self.assertEqual(ranks["first_unexcluded_individual_source_budget"], 20)
        self.assertEqual(ranks["first_unexcluded_sum_source_budget"], 20)
        self.assertFalse(ranks["boundary_is_construction"])

    def test_reject_overstated_scope_or_altered_algebra(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(proof_status="reviewed-proof"),
            lambda x: x["rank_budgets"].update(maximum_remaining_individual_rank=104),
            lambda x: x["rank_budgets"].update(maximum_remaining_rank_sum=203),
            lambda x: x["factor_kernels"][0].update(kernel_unit_determinant=0),
            lambda x: x["boundaries"]["source_examples"][1].update(
                source_slice_rank_with_coherent_middle=16),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_removed_or_changed_dependencies(self):
        original = json.loads((PACKAGE / "gap_sources.json").read_text())
        for index in range(len(original["local_dependencies"])):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][index]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        for mutate in (
            lambda x: x["local_dependencies"].pop(),
            lambda x: x["inherited_external_dependency"].update(doi="unattributed"),
            lambda x: x["inherited_external_dependency"].update(
                hypotheses="all fields without restriction"),
            lambda x: x["concurrent_kernel_predecessor"].update(commit="0"*40),
        ):
            bad = copy.deepcopy(original)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.check_sources(bad)


if __name__ == "__main__":
    unittest.main()

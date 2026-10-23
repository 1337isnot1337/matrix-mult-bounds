"""Exact controls for two deliberately different repair-obstruction scopes."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research" / "ai" / "2026-10-23-first-support-capacity"
SPEC = importlib.util.spec_from_file_location("first_support_capacity", PACKAGE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class FirstSupportCapacityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = VERIFY.certificate()

    def test_pinned_sources_and_separate_scope(self):
        self.assertEqual(len(VERIFY.verify_local_sources()), 2)
        sources = json.loads((PACKAGE / "sources.json").read_text())
        self.assertEqual(len(sources["claim_ids"]), 2)
        self.assertFalse(sources["independent_mathematical_review"])
        self.assertFalse(sources["improves_omega"])
        self.assertIn("53fed21130a5c46a9c2336a8d196ea0547c2cbfb",
                      sources["pending_pr_sources"][0]["url"])

    def test_full_laurent_identity_with_individual_poles(self):
        result = self.result["pole_cancellation"]
        self.assertEqual(len(result["total_target"]), 4)
        self.assertTrue(any(term[-2] < 0 for term in result["source_image"]))
        self.assertTrue(any(term[-2] < 0 for term in result["auxiliary_image"]))
        self.assertTrue(all(term[-2] == 0 for term in result["total_target"]))
        self.assertEqual(result["regular_basis_unit_minor"], -1)
        self.assertEqual(result["source_first_support"], result["union_support_dimension"])
        with self.assertRaisesRegex(ValueError, "complete target"):
            VERIFY.pole_cancellation_control(leading_coefficient=2)

    def test_native_target_contractions_and_oblique_patterns(self):
        controls = self.result["support_unions"]
        self.assertEqual([case["native_contraction_support_rank"] for case in controls],
                         [10, 0, 9, 48, 11])
        for case in controls:
            self.assertEqual(case["native_contraction_support_rank"], case["union_formula"])
        n9 = controls[3]
        self.assertEqual(n9["coefficient_span_dimensions"], [4, 4])
        self.assertEqual(n9["rank_only_lower_bound"], 28)
        self.assertGreater(n9["union_formula"], n9["rank_only_lower_bound"])

    def test_native_source_slices_and_multiplier_supports(self):
        controls = self.result["source_slices"]
        multipliers = controls["multiplier_controls"]
        self.assertEqual([case["rank_controls"][0]["raw_slice_rank"] for case in multipliers],
                         [16, 20, 24])
        self.assertEqual(multipliers[1]["containing_space_dimensions"], [20, 20])
        for case in multipliers:
            self.assertEqual(len(case["rank_controls"]), 3)
            for control in case["rank_controls"]:
                self.assertGreaterEqual(control["raw_slice_rank"], control["coefficient_rank"] + 15)
        for case in controls["first_map_rank_controls"]:
            f, g = case["factor_ranks"]
            self.assertEqual(case["first_map_rank"], f * g)

    def test_sharp_eleven_and_twelve_rank_loss_controls(self):
        controls = self.result["rank_loss"]
        self.assertEqual([case["compressed_slice_rank"] for case in controls], [5, 4])
        self.assertEqual([case["slice_kernel_intersections"] for case in controls], [[5, 6], [5, 7]])
        for case in controls:
            self.assertEqual(case["long_map_ranks"], [20, 20])
            self.assertEqual(case["raw_slice_rank"], 16)

    def test_width_capacity_and_positive_dimension_choices(self):
        arithmetic = self.result["integer_consequences"]
        self.assertEqual([case["first_support_lower_bound"] for case in arithmetic["width_bounds"]],
                         [37101, 29601, 16800, 0])
        self.assertEqual(arithmetic["positive_dimension_choices_checked"], 6561)
        self.assertTrue(arithmetic["boundary_dimension_choices"])
        for case in arithmetic["boundary_dimension_choices"]:
            self.assertTrue(all(d >= 1 for d in case["good_dimensions"]))

    def test_both_polynomial_bounds_and_exact_threshold(self):
        self.assertEqual(VERIFY.polynomial_first_map_bounds(200, 1),
                         {"n": 200, "c": 1, "r": 199, "capped": 199,
                          "uncapped": 371, "combined": 371})
        self.assertEqual(VERIFY.polynomial_first_map_bounds(22, 1)["combined"], 20)
        self.assertEqual(VERIFY.polynomial_first_map_bounds(23, 1)["combined"], 22)
        self.assertEqual(VERIFY.polynomial_first_map_bounds(6, 1)["combined"], 0)
        with self.assertRaises(ValueError):
            VERIFY.polynomial_first_map_bounds(1, 1)

    def test_complete_saved_certificate_and_tampering(self):
        saved = json.loads((PACKAGE / "certificate.json").read_text())
        self.assertEqual(saved, self.result)
        changed = copy.deepcopy(saved)
        changed["pole_cancellation"]["source_image"][0][-1] += 1
        with self.assertRaisesRegex(ValueError, "complete exact reconstruction"):
            VERIFY.validate_certificate(changed)


if __name__ == "__main__":
    unittest.main()

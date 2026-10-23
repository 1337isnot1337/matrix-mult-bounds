"""Exact controls for the ordinary diagonal-only first-map obstruction."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/"research"/"ai"/"2026-10-23-diagonal-first-support"
SPEC = importlib.util.spec_from_file_location("diagonal_first_support", PACKAGE/"verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class DiagonalFirstSupportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = VERIFY.certificate()

    def test_source_pins_and_changed_hash_rejection(self):
        self.assertEqual(len(VERIFY.verify_local_sources()), 4)
        sources = json.loads((PACKAGE/"sources.json").read_text())
        self.assertEqual(sources["claim_ids"], ["AI-DIAGONAL-FIRST-SUPPORT-001"])
        self.assertFalse(sources["independent_mathematical_review"])
        self.assertFalse(sources["improves_omega"])
        sources["local_sources"][0]["sha256"] = "0"*64
        with self.assertRaisesRegex(ValueError, "Pinned source hash mismatch"):
            VERIFY.verify_local_sources(sources)

    def test_shifted_transpose_unit_minors_and_concision(self):
        rows = VERIFY.shift_transpose_map(4)
        # E_01 maps to E_01 + E_21, not to E_01 + E_12.
        self.assertEqual([i for i, value in enumerate(rows[1]) if value], [1, 11])
        for case in self.result["shift_transpose"]:
            self.assertEqual(case["first_map_rank"], case["r"]**2)
            self.assertEqual(case["unit_minor_determinant"], 1)
            for field in case["fields"]:
                self.assertEqual(field["common_right_kernel_dimension"], 0)
                self.assertEqual(field["common_left_kernel_dimension"], 0)

    def test_complete_diagonal_identity_and_genuine_alternating_change(self):
        for prime in (None, 2, 3):
            original = VERIFY.shift_transpose_map(4)
            altered = VERIFY.shift_transpose_map(4, alternating=True)
            self.assertNotEqual(original, altered)
            VERIFY.check_diagonal_identity(original, 4, prime)
            VERIFY.check_diagonal_identity(altered, 4, prime)
            altered[0][0] += 1
            with self.assertRaisesRegex(ValueError, "diagonal polynomial identity"):
                VERIFY.check_diagonal_identity(altered, 4, prime)
        for case in self.result["shift_transpose"]:
            for field in case["fields"]:
                self.assertEqual(field["perturbed_off_diagonal_rank"], case["n"])

    def test_joint_square_budget_and_common_kernel_cross_space_in_char_two(self):
        controls = self.result["kernel_spaces"]["fields"]
        self.assertEqual([case["field"] for case in controls], ["Q", "F2", "F3"])
        for case in controls:
            self.assertEqual(case["kernel_dimensions"], [2, 1])
            self.assertEqual(case["joint_square_dimension"], 4)
            for cross in case["cross_spaces"]:
                self.assertEqual(cross["cross_space_dimension"], cross["r"])

    def test_native_source_and_target_slices_with_multiplier(self):
        control = self.result["native_source"]
        self.assertFalse(control["actual_target_long_maps_supplied"])
        for field in control["fields"]:
            self.assertEqual(field["coefficient_rank"], 2)
            self.assertEqual(field["native_source_rank"], 20)
            self.assertEqual(field["target_rank"], 4)
            self.assertEqual(field["containing_space_dimensions"], [20, 20])

    def test_all_threshold_splits_and_budget_enumeration(self):
        result = self.result["integer_consequences"]
        self.assertEqual(result["budget_range"], [0, 500])
        self.assertEqual(result["thresholds_per_pair"], 12)
        self.assertGreater(result["deficiency_pairs_checked"], 100000)
        self.assertEqual(VERIFY.optimized_split(20, 0)["F_threshold"], 12)
        self.assertEqual(VERIFY.optimized_split(0, 20)["F_threshold"], 1)
        self.assertEqual(VERIFY.optimized_split(0, 0)["allowance"], 0)
        for e in (0, 1, 2, 3, 153, 170, 171, 175, 176, 500):
            t = VERIFY.tau(e)
            q = VERIFY.paired_deficiency(e)
            self.assertLessEqual(VERIFY.triangular(t), e)
            self.assertGreater(VERIFY.triangular(t+1), e)
            self.assertLessEqual(q*(q+1), e)
            self.assertGreater((q+1)*(q+2), e)

    def test_exact_repair_rounding_and_invalid_parameters(self):
        case = VERIFY.repair_bounds(200, 1)
        self.assertEqual(case["injective_factor_lower_bound"], 188)
        self.assertEqual(case["general_lower_bound"], 176)
        self.assertEqual(175+VERIFY.budget_allowance(175), 187)
        self.assertEqual(176+VERIFY.budget_allowance(176), 188)
        self.assertLess(171+VERIFY.budget_allowance(171), 188)
        self.assertEqual(VERIFY.repair_bounds(12, 1)["general_lower_bound"], 0)
        self.assertEqual(VERIFY.repair_bounds(13, 1)["general_lower_bound"], 1)
        for value in (-1, 0.5, True):
            with self.assertRaises(ValueError):
                VERIFY.tau(value)
        with self.assertRaises(ValueError):
            VERIFY.repair_bounds(1, 1)

    def test_full_certificate_and_changed_or_omitted_evidence(self):
        saved = json.loads((PACKAGE/"certificate.json").read_text())
        self.assertEqual(saved, self.result)
        self.assertTrue(saved["ordinary_maps_only"])
        self.assertTrue(saved["diagonal_identity_is_polynomial"])
        changed = copy.deepcopy(saved)
        changed["integer_consequences"]["target_bounds"][5]["general_lower_bound"] = 175
        with self.assertRaisesRegex(ValueError, "complete exact reconstruction"):
            VERIFY.validate_certificate(changed)
        omitted = copy.deepcopy(saved)
        omitted["local_source_pins"].pop()
        with self.assertRaisesRegex(ValueError, "complete exact reconstruction"):
            VERIFY.validate_certificate(omitted)


if __name__ == "__main__":
    unittest.main()

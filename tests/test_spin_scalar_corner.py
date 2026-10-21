import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/ai/2026-10-20-anisotropic-constructions/spin_scalar_corner.py"
SPEC = importlib.util.spec_from_file_location("spin_scalar_corner_controls", SCRIPT)
CORE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)


class SpinScalarCornerTests(unittest.TestCase):
    def test_all_source_coefficients_mixed_responses_and_exact_ranks(self):
        report = CORE.verify()
        self.assertEqual(report["selected_module"], {
            "source_terms_checked": 262144,
            "all_target_coefficients_checked": 81,
            "nonzero_target_coefficients": 9})
        self.assertEqual([item["rank"] for item in report["response_ranks"]], [15, 9, 9])
        self.assertEqual(report["core_ambient_dimensions"], [192, 180, 180])
        self.assertEqual(len(report["six_mixed_responses"]), 6)
        self.assertTrue(all(item["nonzero_response_coefficients"] == 0
                            for item in report["six_mixed_responses"]))
        self.assertEqual(sum(item["all_response_coefficients_checked"]
                             for item in report["six_mixed_responses"]), 6773760)
        scan = report["complete_coordinate_selection_scan"]
        self.assertEqual(scan["subsets_checked"], 220)
        self.assertEqual(scan["first_response_rank_histogram"],
                         {"15": 10, "16": 16, "17": 38, "18": 78, "19": 40, "20": 38})
        lift = report["nine_copy_reduced_lift"]
        self.assertEqual(lift["all_target_coefficients_checked"], 559872)
        self.assertEqual(lift["nonzero_target_coefficients"], 1296)
        self.assertFalse(report["conditional_correction"]["missing_maps_constructed"])
        self.assertFalse(report["new_exponent_established"])

    def test_small_identity_can_pass_while_mixed_compatibility_fails(self):
        maps = CORE.corner_maps()
        maps[1][0][CORE.coordinate(5, 12, 6)] = 1
        self.assertEqual(CORE.check_module(maps)["nonzero_target_coefficients"], 9)
        mixed = CORE.mixed_responses(maps)
        self.assertTrue(any(item["nonzero_response_coefficients"] for item in mixed))
        with self.assertRaisesRegex(ArithmeticError, "full mixed response is nonzero"):
            CORE.check_mixed(maps)

    def test_changed_nonzero_target_coefficient_is_rejected(self):
        maps = CORE.corner_maps()
        maps[0][0][CORE.coordinate(7, 12, 7)] = 2
        with self.assertRaisesRegex(ArithmeticError, "matrix-tensor coefficient fails"):
            CORE.check_module(maps)

    def test_changed_response_certificate_is_rejected(self):
        certificate = copy.deepcopy(json.loads(CORE.CERTIFICATE.read_text()))
        certificate["evidence"]["response_ranks"][0]["identity_minor_pivots"][0]["output_pair"] = [0, 0]
        with self.assertRaisesRegex(ArithmeticError, "evidence does not match"):
            CORE.verify(certificate)


if __name__ == "__main__":
    unittest.main()

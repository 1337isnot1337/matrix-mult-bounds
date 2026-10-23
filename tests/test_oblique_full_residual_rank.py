"""Check exact inputs to the full one-dependency ordinary-rank proof."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


PACKAGE = (Path(__file__).resolve().parents[1]
           / "research/ai/2026-10-23-oblique-border-repair")
SPEC = importlib.util.spec_from_file_location("oblique_full_residual_rank",
                                            PACKAGE / "full_residual_rank.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ObliqueFullResidualRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = MODULE.build_certificate()

    def test_complete_saved_certificate_and_sources(self):
        self.assertEqual(MODULE.verify_saved(PACKAGE / "full-residual-rank-certificate.json"),
                         self.report)
        self.assertEqual(self.report["source_pin_verification"],
                         {"inherited_sources": 4, "followup_sources": 4, "all_match": True})
        self.assertEqual(self.report["n6_ordinary_rank"], 19)
        self.assertFalse(self.report["independent_mathematical_review"])
        self.assertFalse(self.report["arbitrary_source_map_optimality_claimed"])

    def test_family_basis_splittings_and_rank_costs(self):
        self.assertEqual([case["b"] for case in self.report["controls"]],
                         [2, 3, 4, 5, 6, 7, 8, 12])
        for case in self.report["controls"]:
            r = case["r"]
            self.assertEqual(case["concise_format"], [2 * r - 1, 2 * r + 1, 2 * r + 1])
            self.assertEqual(case["horizontal_peel_dimension"], 2 * (r - 2))
            self.assertEqual(case["vertical_peel_dimension"], 2 * (r - 2))
            self.assertEqual(case["ordinary_rank_lower_bound_from_written_proof"], 4 * r - 1)
            self.assertEqual(case["ordinary_rank_upper_bound"], 4 * r - 1)
            self.assertEqual([minor["determinant"] for minor in case["embedding_unit_minors"]],
                             [1, 1, 1])
            self.assertTrue(case["support_splittings_checked"])

    def test_actual_exported_source_maps_replay(self):
        self.assertEqual(self.report["native_n6_control"],
                         {"source_coefficients_contracted": 576,
                          "target_coordinates_compared": 10000,
                          "nonzero_residual_coefficients": 38,
                          "saved_maps_and_residual_replayed": True,
                          "adapted_core_and_wings_replayed": True})

    def test_changed_residual_or_source_map_is_rejected(self):
        changed = MODULE.inherited_formula(4)
        changed[0, 0, 0] = 1
        with self.assertRaises(ArithmeticError):
            MODULE.check_family(4, expected_residual=changed)
        source = json.loads((MODULE.PREDECESSOR / "witness.json").read_text())
        case = next(case for case in source["cases"] if case["variant"] == "product-oblique")
        changed_case = copy.deepcopy(case)
        changed_case["maps"][0][0][0] = 1
        with self.assertRaises(ArithmeticError):
            MODULE.replay_native_witness(changed_case)

    def test_border_scope_and_koszul_ceiling(self):
        self.assertEqual(self.report["n6_border_rank_interval"], [11, 18])
        self.assertFalse(self.report["whole_residual_border_rank_optimality_claimed"])
        note = self.report["first_leg_Koszul_note"]
        self.assertEqual(note["n6_middle_matrix_shape"], [1386, 1386])
        self.assertEqual(note["n6_middle_rank_ceiling"], 504)
        self.assertEqual(note["n6_rank_one_divisor"], 70)
        self.assertEqual(note["n6_rank_required_to_prove_border_at_least_18"], 1191)
        self.assertFalse(note["exact_Koszul_rank_computation_claimed"])

    def test_wrong_saved_support_dimension_is_rejected(self):
        report = copy.deepcopy(self.report)
        report["controls"][2]["horizontal_peel_dimension"] = 5
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "false-full-rank.json"
            path.write_text(json.dumps(report))
            with self.assertRaises(ArithmeticError):
                MODULE.verify_saved(path)

    def test_invalid_family_parameters(self):
        for b in [0, 1, -2, True, 4.0, "4"]:
            with self.assertRaises(ValueError):
                MODULE.check_family(b)


if __name__ == "__main__":
    unittest.main()

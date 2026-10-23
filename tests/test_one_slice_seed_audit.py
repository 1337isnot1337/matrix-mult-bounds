"""Exact checks of the one-slice theorem's hypotheses and scalar ceiling."""

from copy import deepcopy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/"research/ai/2026-10-23-one-slice-seed-audit"
SPEC = importlib.util.spec_from_file_location("one_slice_seed_audit", PACKAGE/"verify.py")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class OneSliceSeedAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = AUDIT.certificate()

    def test_saved_certificate_replays_exactly(self):
        saved = json.loads((PACKAGE/"certificate.json").read_text())
        self.assertEqual(self.report, saved)
        self.assertFalse(saved["complete_laurent_map_supplied"])
        self.assertTrue(saved["actual_degeneration_via_imported_theorem"])
        self.assertFalse(saved["improves_omega"])

    def test_complete_seed_and_negative_control(self):
        self.assertEqual(self.report["seed_identity"], {
            "source_terms_checked": 400, "target_positions_checked": 4096,
            "target_nonzero_coefficients": 64, "coefficient_failures": 0})
        data = json.loads((AUDIT.reference_root()/AUDIT.SEED_PATH).read_text())
        broken = deepcopy(data["maps_target_by_source"])
        broken[0] = [[0]*25 for _ in range(16)]
        with self.assertRaisesRegex(AssertionError, "Seed coefficient mismatch"):
            AUDIT.seed_coefficient_check(broken)

    def test_all_initial_fixed_seed_kernels_are_zero(self):
        rows = self.report["fixed_seed_initial_slice_kernels"]
        self.assertEqual([row["source_dimension"] for row in rows], [25, 32, 32])
        self.assertEqual([row["two_map_slice_space_rank_over_Q"] for row in rows],
                         [25, 32, 32])
        self.assertEqual([row["kernel_dimension_over_Q"] for row in rows], [0, 0, 0])

    def test_corner_slice_and_exact_appended_cancellation(self):
        row = self.report["corner_slice"]
        self.assertEqual(row["functional_nonzero_coordinates_A_pq"], [[0, 0], [4, 4]])
        self.assertEqual([row[key] for key in (
            "raw_rank_q", "left_compressed_rank", "right_compressed_rank",
            "both_compressed_rank_s", "augmented_raw_slice_rank")], [32, 16, 16, 8, 40])
        self.assertEqual(row["factor_column_ranks"], [8, 8])
        self.assertTrue(all(abs(d) == 1 for d in row["selected_long_map_determinants"]))
        self.assertEqual(len({pair[0] for pair in row["factor_column_pairs_B_C"]}), 8)
        self.assertEqual(len({pair[1] for pair in row["factor_column_pairs_B_C"]}), 8)
        self.assertEqual(row["factorization_entries_checked"], 256)
        self.assertEqual(row["augmented_cancellation_entries_checked"], 256)
        self.assertEqual(row["augmented_cancellation_failures"], 0)

    def test_powered_formula_and_domain(self):
        first, second = self.report["powered_formula_controls"]
        self.assertEqual((first["appended_slice_s"], first["guaranteed_extracted_slice_t"]),
                         (8, 8))
        self.assertEqual((second["raw_rank_q"], second["target_other_leg_dimension"],
                          second["appended_slice_s"], second["guaranteed_extracted_slice_t"]),
                         (1024, 256, 64, 576))
        for k in (1, 2, 5):
            self.assertEqual(AUDIT.powered_parameters(k)["guaranteed_extracted_slice_t"],
                             8**k*(2**k-1)**2)
        for value in (0, -1, True, 1.5):
            with self.assertRaises(ValueError):
                AUDIT.powered_parameters(value)

    def test_integer_ceiling_and_cyclic_scope(self):
        row = self.report["endpoint_comparison"]
        self.assertEqual(Fraction(row["h_4"]), Fraction(140, 81))
        self.assertEqual(Fraction(row["P_star_5_4"]), Fraction(910, 81))
        pairs = [(item["left"], item["right"])
                 for item in row["strict_integer_comparisons"]]
        self.assertEqual(pairs, [(512, 529), (32768, 38416),
                                 (37**2*81**3, 910**3)])
        self.assertTrue(all(left < right for left, right in pairs))
        self.assertFalse(row["individual_character_values_assumed_equal"])
        self.assertFalse(row["actual_endpoint_character_exists_claimed"])
        self.assertTrue(row["equal_cyclic_assignment_survives"])


if __name__ == "__main__":
    unittest.main()

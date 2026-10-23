"""Literal acceptance and focused corruption controls for the sharp84/88 caps."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-rank84-rank88-spaces/verify.py"
SPEC = importlib.util.spec_from_file_location("rank84_rank88_acceptance", PATH)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class Rank84Rank88SpacesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads(verify.CERTIFICATES.read_text())
        cls.bases = verify.literal_bases()

    def test_complete_saved_acceptance_and_sharpness(self):
        report = json.loads(verify.RESULT.read_text())
        verify.replay_saved(report)
        self.assertEqual(report["source_controls"]["source_factorizations_checked"], 112)
        self.assertEqual(report["coherent_controls"]["credited_integer_minors_replayed"], 11)
        self.assertEqual([row["attained_rank"] for row in report["sharpness_controls"]["sharp_spaces"]], [80, 84])

    def test_coherent_inventory_and_credited_bytes_are_checked(self):
        document = copy.deepcopy(self.certificate)
        document["coherent9_ideals"].pop()
        with self.assertRaisesRegex(ArithmeticError, "credited coherent certificates"):
            verify.coherent_controls(document, self.bases[0])
        document = copy.deepcopy(self.certificate)
        document["coherent13_ideals"][1] = copy.deepcopy(document["coherent13_ideals"][0])
        with self.assertRaisesRegex(ArithmeticError, "credited coherent certificates"):
            verify.coherent_controls(document, self.bases[0])
        self.assertEqual(len(verify.short_ideals(9)), 7)
        self.assertEqual(len(verify.short_ideals(13)), 3)

    def test_sharp_space_support_singularity_and_minor_size_are_checked(self):
        records = copy.deepcopy(self.certificate["sharp_spaces"])
        outside = verify.SOURCE.index((2, 0, 0))
        records[0]["coefficient_mask"] = hex(1 << outside)
        with self.assertRaisesRegex(ArithmeticError, "support leaves"):
            verify.sharpness_controls(records, self.certificate["boundary_space"], self.bases[1])
        records[0]["coefficient_mask"] = "0x1"
        with self.assertRaisesRegex(ArithmeticError, "singular modulo two"):
            verify.sharpness_controls(records, self.certificate["boundary_space"], self.bases[1])
        records = copy.deepcopy(self.certificate["sharp_spaces"])
        mask = int(records[1]["minor_rows_mask"], 16)
        records[1]["minor_rows_mask"] = hex(mask & (mask-1))
        with self.assertRaisesRegex(ArithmeticError, "wrong dimensions"):
            verify.sharpness_controls(records, self.certificate["boundary_space"], self.bases[1])

    def test_source_pin_and_source_inventory_are_checked(self):
        source = json.loads((verify.HERE / "sources.json").read_text())
        source["local_dependencies"][0]["sha256"] = "0"*64
        with self.assertRaisesRegex(ArithmeticError, "source digest mismatch"):
            verify.check_sources(source)
        source["local_dependencies"].pop()
        with self.assertRaisesRegex(ArithmeticError, "source inventory"):
            verify.check_sources(source)

    def test_all_profile_counts_and_strict_thresholds_are_enforced(self):
        profiles = verify.profile_controls()
        self.assertEqual(profiles["all_nonincreasing_layer_size_profiles"], 245157)
        for threshold, expected in (("84", (51553, 56, 4)), ("88", (59809, 60, 2))):
            row = profiles["thresholds"][threshold]
            self.assertEqual((row["admissible_profiles"], row["maximum_volume"], row["profiles_at_maximum"]), expected)
        report = json.loads(verify.RESULT.read_text())
        report["profile_controls"]["thresholds"]["88"]["maximum_volume"] = 59
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(report)

    def test_boundary_budget_and_unproved_scope_are_not_inflated(self):
        boundary = copy.deepcopy(self.certificate["boundary_space"])
        boundary["rank_upper"] = 87
        with self.assertRaisesRegex(ArithmeticError, "boundary space"):
            verify.sharpness_controls(self.certificate["sharp_spaces"], boundary, self.bases[1])
        report = json.loads(verify.RESULT.read_text())
        report["claim_scope"]["all_target_leg_pairs_claimed"] = True
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(report)
        document = copy.deepcopy(self.certificate)
        document["verification_modulus"] = 3
        with self.assertRaisesRegex(ArithmeticError, "certificate header"):
            verify.controls(document)

    def test_long_pair_increment_keeps_its_boundary_and_pair_scope(self):
        report = verify.long_pair_controls()
        self.assertEqual(report["integer_long_rank_pairs"], 12321)
        self.assertEqual(report["newly_excluded_pairs"], 644)
        self.assertTrue(report["rank_sum136_boundary_not_excluded"])
        self.assertFalse(report["all_target_leg_pairs_claimed"])


if __name__ == "__main__":
    unittest.main()

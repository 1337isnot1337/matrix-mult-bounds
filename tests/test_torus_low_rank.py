"""Replay the exact source minors and protect the rank-24 stopping boundary."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-torus-low-rank"
SPEC = importlib.util.spec_from_file_location("torus_low_rank", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class TorusLowRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_exact_source_action_and_minor_replay(self):
        self.assertEqual(v.verify(self.record), {
            "literal_source_terms_checked": 4096, "literal_matrix_entries_compared": 12544,
            "coordinate_slices_checked": 112, "cross_extreme_pairs_checked": 256,
            "determinant_one_minors_checked": 16, "sharp_rank23_linear_space_dimension": 8,
            "excluded_defects": list(range(9)), "remaining_balanced_long_rank_upper": 101,
            "improves_omega": False})

    def test_real_boundary_and_echelon_hypotheses(self):
        self.assertTrue(v.threshold(8)["excluded_by_written_torus_ruling_theorem"])
        self.assertEqual(v.threshold(8)["source_rank_upper"], 23)
        self.assertEqual(v.threshold(8)["active_image_rank_lower"], 4)
        self.assertFalse(v.threshold(9)["excluded_by_written_torus_ruling_theorem"])
        boundary = self.record["rank24_boundary_plane"]
        self.assertEqual((boundary["dimension"], boundary["all_slice_rank_upper"]), (12, 24))
        with self.assertRaises(ValueError):
            v.echelon_specialization([{(0, 0, 0): 1}, {(0, 0, 0): 1, (1, 0, 0): 1}])
        with self.assertRaises(ValueError):
            v.threshold(-1)

    def test_reject_corrupted_certificate_and_overclaims(self):
        for change in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(independent_review=True),
            lambda x: x.update(rank101_long_limits_excluded=True),
            lambda x: x["matching_minors"][0]["determinants"][0].update(determinant=0),
            lambda x: x["matching_minors"][7]["row_indices_in_28_by_28_block"].pop(),
            lambda x: x["thresholds"][9].update(excluded_by_written_torus_ruling_theorem=True),
            lambda x: x["action_and_coordinate_controls"].update(source_terms_checked=4095),
            lambda x: x["echelon_specialization_control"]["basis"][0]["normalized_terms"][1].update(
                normalized_exponent=0),
        ):
            bad = copy.deepcopy(self.record)
            change(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_changed_source_pins(self):
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


if __name__ == "__main__":
    unittest.main()

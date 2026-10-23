"""Replay the singular-column controls and protect the exact open boundary."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-singular-long-rank"
SPEC = importlib.util.spec_from_file_location("singular_long_rank", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class SingularLongRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_exact_source_ruling_and_rank_budget_replay(self):
        self.assertEqual(v.verify(self.record), {
            "source_slice_controls": 8, "literal_source_coefficients_checked": 100352,
            "ruling_controls": 6, "isolated_rank_budget_controls": 6,
            "excluded_defects": [0, 1, 2, 3, 4],
            "remaining_balanced_long_rank_upper": 105, "improves_omega": False})

    def test_strict_gap_boundary_and_nonzero_ruling_hypothesis(self):
        self.assertTrue(v.threshold(4)["excluded_by_written_gap_ruling_theorem"])
        self.assertEqual(v.threshold(4)["strict_gap_margin"], 1)
        self.assertFalse(v.threshold(5)["excluded_by_written_gap_ruling_theorem"])
        self.assertEqual(v.threshold(5)["strict_gap_margin"], 0)
        with self.assertRaises(ValueError):
            v.ruling_control(10, 11, 8, [0]*10)
        with self.assertRaises(ValueError):
            v.threshold(-1)

    def test_reject_corrupted_evidence_and_overclaims(self):
        for change in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(independent_review=True),
            lambda x: x.update(rank105_long_limits_excluded=True),
            lambda x: x["source_controls"]["next_rank_case"].update(source_rank=19),
            lambda x: x["thresholds"][5].update(excluded_by_written_gap_ruling_theorem=True),
            lambda x: x["ruling_controls"][1].update(product_rank=7),
        ):
            bad = copy.deepcopy(self.record)
            change(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_changed_source_pins(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(3):
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

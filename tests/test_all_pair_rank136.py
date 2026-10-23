"""Integer endpoint and scope controls for the every-pair136 application."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-all-pair-rank136/verify.py"
SPEC = importlib.util.spec_from_file_location("all_pair_rank136", PATH)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class AllPairRank136Tests(unittest.TestCase):
    def test_frozen_record_and_complete_integer_coverage(self):
        document = json.loads(verify.RESULT.read_text())
        verify.replay_saved(document)
        counts = document["rank_pair_controls"]["pair_counts"]
        self.assertEqual(sum(item["rank_pairs_checked"] for item in counts.values()), 20706)
        self.assertEqual(counts["mixed"]["new_pairs_of_sum137_through144"], 492)
        self.assertEqual(counts["long"]["new_pairs_of_sum137_through144"], 500)

    def test_exact_interval_margins_and_strict_thresholds(self):
        controls = verify.rank_pair_controls()
        margins = {(item["kind"], tuple(item["sum_interval"])):
                   (item["kernel_lower_minimum"], item["kernel_upper"])
                   for item in controls["interval_margins"]}
        self.assertEqual(margins, {("mixed", (141, 144)): (61, 56),
                                   ("mixed", (137, 140)): (61, 60),
                                   ("long", (141, 144)): (58, 56),
                                   ("long", (137, 140)): (64, 60)})
        self.assertEqual([verify.new_source_cap(rank) for rank in (83, 84, 87, 88)],
                         [56, 60, 60, 112])

    def test_prior144_is_retained_and_needed(self):
        prior = verify.pair_screen(100, 100, "mixed")
        alone = verify.pair_screen(100, 100, "mixed", use_prior=False)
        self.assertTrue(prior["excluded_by_prior144"])
        self.assertTrue(prior["excluded"])
        self.assertFalse(alone["excluded"])
        controls = verify.rank_pair_controls()["pair_counts"]
        self.assertEqual(controls["mixed"]["prior_pairs_above144"], 1653)
        self.assertEqual(controls["long"]["prior_pairs_above144"], 1711)

    def test_boundary_pairs_remain_open_and_invalid_ranks_are_rejected(self):
        for a, b, kind in ((68, 68, "mixed"), (68, 68, "long"), (100, 36, "mixed")):
            record = verify.pair_screen(a, b, kind)
            self.assertEqual(record["source_rank_ceiling"], 88)
            self.assertFalse(record["excluded"])
        self.assertTrue(verify.pair_screen(100, 37, "mixed")["excluded"])
        with self.assertRaisesRegex(ArithmeticError, "individual bounds"):
            verify.pair_screen(90, 110, "mixed")
        with self.assertRaisesRegex(ArithmeticError, "invalid source rank"):
            verify.new_source_cap(-1)

    def test_source_pins_and_scope_corruption_are_rejected(self):
        source = json.loads((verify.HERE / "sources.json").read_text())
        wrong = copy.deepcopy(source)
        wrong["local_dependencies"][1]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            verify.check_sources(wrong)
        source["local_dependencies"].pop()
        with self.assertRaisesRegex(ArithmeticError, "source inventory"):
            verify.check_sources(source)
        report = json.loads(verify.RESULT.read_text())
        report["claim_scope"]["leading_rank_bounds_sharp"] = True
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(report)
        report = json.loads(verify.RESULT.read_text())
        report["rank_pair_controls"]["every_pair_sum_upper"] = 135
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(report)


if __name__ == "__main__":
    unittest.main()

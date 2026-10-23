"""Mathematical acceptance and boundary controls for column overlap."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-column-overlap"
SPEC = importlib.util.spec_from_file_location("column_overlap", PACKAGE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class ColumnOverlapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = VERIFY.run()
        cls.cases = {value["name"]: value for value in cls.report["cases"]}

    def test_complete_native_replay_matches_retained_report(self):
        saved = json.loads((ROOT / "results/column-overlap-2026-10-23/controls.json").read_text())
        self.assertEqual(self.report, saved)
        self.assertEqual(self.report["case_count"], 7)

    def test_full_channel_sharp_bound(self):
        value = self.cases["connected-full-channel-sharp"]
        self.assertEqual(value["source_A0_channel_rank_at_t2_X2_Y3"], 3)
        self.assertEqual(value["leading_target_intersection_dimension"], 1)
        self.assertEqual(value["residual_rank_at_t2"], 8)
        self.assertEqual(value["geometry"]["auxiliary_flattening_lower_bound"], 8)

    def test_component_count_and_saturation_are_both_necessary(self):
        for name in ("separated-n6-m2", "separated-n8-m4"):
            value = self.cases[name]
            self.assertTrue(value["exact_target"])
            self.assertEqual(value["leading_target_intersection_dimension"], value["geometry"]["c"])
        moving = self.cases["exact-moving-target-requires-saturation-budget"]
        self.assertTrue(moving["exact_target"])
        self.assertGreater(moving["geometry"]["D"] - moving["geometry"]["c"], 0)
        self.assertLess(moving["leading_source_rank"], moving["source_rank_at_t2"])

    def test_boundary_rank_loss_and_separately_polar_control(self):
        boundary = self.cases["zero-extension-boundary-columns"]
        self.assertEqual(boundary["leading_target_intersection_dimension"], 0)
        self.assertEqual(boundary["residual_rank_at_t2"], 12)
        loss = self.cases["actual-leading-slice-rank-loss"]
        self.assertEqual((loss["leading_source_rank"], loss["source_rank_at_t2"]), (8, 16))
        polar = self.cases["singular-leading-block-with-pole-cancellation"]
        self.assertGreater(polar["source_negative_coefficients"], 0)
        self.assertEqual(polar["residual_rank_at_t2"], 16)

    def test_damaged_integer_construction_is_rejected(self):
        n, m, k = 4, 2, 2
        positions = [1, 3]
        first = {(m*i+m-1-y, m*j+m-1-y): {i*k+j: 1}
                 for i in range(k) for j in range(k) for y in range(m)}
        del first[(0, 0)]
        blocks = VERIFY.constant_blocks([VERIFY.identity(m) for _ in positions])
        with self.assertRaisesRegex(AssertionError, "constructed target identity failed"):
            VERIFY.inspect_case("damaged", n, m, positions, positions, blocks, blocks,
                                VERIFY.constant_first(first), expected_exact=True)

    def test_source_pins_and_written_claim_scope(self):
        sources = json.loads((PACKAGE / "sources.json").read_text())
        for source in sources["local_dependencies"]:
            self.assertEqual(hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest(), source["sha256"])
        claims = json.loads((ROOT / "research/claims.json").read_text())["claims"]
        claim = next(c for c in claims if c["id"] == "AI-PAIRED-COLUMN-OVERLAP-001")
        self.assertEqual(claim["status"], "proof-written-unreviewed")
        self.assertFalse(claim["independent_review"])
        self.assertFalse(claim["improves_omega"])


if __name__ == "__main__":
    unittest.main()

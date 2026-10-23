"""Exact replay and failure controls for the A4 rank-48 frontier."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-torus-rank-frontier/verify.py"
SPEC = importlib.util.spec_from_file_location("torus_rank_frontier", PATH)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class TorusRankFrontierTests(unittest.TestCase):
    def test_frozen_evidence_replays(self):
        document = json.loads(verify.RESULT.read_text())
        verify.replay_saved(document)
        self.assertEqual(document["middle_pair_controls"]["total_short_pairs_checked"], 768)
        self.assertEqual(document["rank48_threshold_controls"]["rank_two_middle_48_minors"], 16)
        self.assertEqual(document["rank48_threshold_controls"]["two_extreme_48_minors"], 64)

    def test_every_source_matrix_entry_agrees_with_literal_six_index_source(self):
        _, entries = verify.literal_source()
        for row in range(112):
            jp, ell = divmod(row, 7)
            j, p = divmod(jp, 4)
            for column in range(112):
                hq, r = divmod(column, 4)
                h, q = divmod(hq, 4)
                expected = (h - j, p + q, ell - r)
                if not (0 <= expected[0] < 4 and 0 <= expected[2] < 4):
                    expected = None
                self.assertEqual(entries.get((row, column)), expected)

    def test_minor_corruption_is_rejected(self):
        records = verify.pair_certificates()
        records[0]["minor_rows"][0] = records[0]["minor_rows"][1]
        with self.assertRaisesRegex(ArithmeticError, "minor dimensions"):
            verify.replay_pairs(records)
        records = verify.pair_certificates()
        records[1]["minor_determinant"] = 2
        with self.assertRaisesRegex(ArithmeticError, "determinant one"):
            verify.replay_pairs(records)

    def test_source_pin_mutation_and_removal_are_rejected(self):
        original = json.loads((verify.HERE / "sources.json").read_text())
        corrupt = copy.deepcopy(original)
        corrupt["local_dependencies"][1]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            verify.check_sources(corrupt)
        original["local_dependencies"].pop()
        with self.assertRaisesRegex(ArithmeticError, "source inventory"):
            verify.check_sources(original)

    def test_all_high_integer_rank_pairs_are_excluded(self):
        records = verify.rank_pair_controls()
        self.assertEqual(records["rank_pairs_checked"], 12321)
        self.assertEqual(records["pairs_above_176"], 990)
        self.assertEqual(records["excluded_pairs_above_176"], 990)
        self.assertEqual(records["new_pairs_of_sum_177_through_192"], 584)
        self.assertEqual(records["new_range_minimum_kernel_lower"], 28)
        self.assertFalse(records["boundary_control"]["excluded"])
        self.assertTrue(records["ordinary_control"]["ordinary_regularity_forced"])

    def test_strict_threshold_is_not_extended_to_rank48(self):
        self.assertEqual(verify.kernel_cap(15), 0)
        self.assertEqual(verify.kernel_cap(31), 16)
        self.assertEqual(verify.kernel_cap(32), 24)
        self.assertEqual(verify.kernel_cap(47), 24)
        self.assertEqual(verify.kernel_cap(48), 112)
        self.assertEqual(verify.screen(88, 88)["source_defect"], 48)

    def test_inflated_scope_and_changed_budget_are_rejected(self):
        document = json.loads(verify.RESULT.read_text())
        document["claim_scope"]["dimension_bound_sharp"] = True
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)
        document = json.loads(verify.RESULT.read_text())
        document["rank_pair_controls"]["new_range_kernel_upper"] = 28
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)

    def test_fraction_free_determinant_covers_pivots_and_singular_matrices(self):
        self.assertEqual(verify.determinant([[0, 1], [1, 0]]), -1)
        self.assertEqual(verify.determinant([[2, 1, 3], [1, 0, 2], [3, 2, 5]]), -1)
        self.assertEqual(verify.determinant([[1, 1], [1, 1]]), 0)


if __name__ == "__main__":
    unittest.main()

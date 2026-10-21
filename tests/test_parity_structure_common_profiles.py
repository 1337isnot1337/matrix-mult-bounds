"""Finite-domain and orientation controls for the complete common-profile screen."""

import copy
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_common_profiles.py"
SPEC = importlib.util.spec_from_file_location("parity_structure_common_profiles", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CommonProfileScreenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = MODULE.verify()

    def test_complete_domain_and_terminal_partition(self):
        report = self.report
        self.assertEqual(report["counts"], {
            "canonical_pairs_considered": 265783,
            "pass_weight_capacity": 38482,
            "pass_saturated_input_lower_rank": 14220,
            "pass_selected_upper_rank": 5604,
        })
        self.assertEqual(report["unclassified_profiles"], 0)
        self.assertEqual(sum(report["terminal_written_proof_classes"].values()), 5604)
        self.assertEqual(report["zero_grade_controls"]["minimum_nonzero_slice_rank_by_torus_proof"], 8)
        self.assertEqual(report["zero_grade_controls"]["zero_grade_source_terms"], 2080)
        self.assertFalse(report["unequal_vertex_profiles_excluded"])
        self.assertFalse(report["arbitrary_singular_degenerations_excluded"])

    def test_ordered_saturated_rank_control(self):
        large = (1,) + (2,) * 13
        small = (1,) * 7
        dimensions, ranks, _ = MODULE.source_tables()
        counts = MODULE.total_counts(large, small)
        self.assertEqual(MODULE.total_block_rank(large, small, -11, 11), 9)
        self.assertEqual(MODULE.total_block_rank(large, small, 11, -11), 12)
        self.assertEqual(ranks[-11, 11], 16)
        self.assertEqual(dimensions[0] - counts[0], 4)
        self.assertIsNotNone(MODULE.saturated_violation(large, small, counts, dimensions, ranks))

    def test_saved_terminal_examples_satisfy_every_written_hypothesis(self):
        for proof_class, record in self.report["terminal_examples"].items():
            large, small = tuple(record["large"]), tuple(record["small"])
            counts = MODULE.total_counts(large, small)
            self.assertEqual(MODULE.terminal_proof_class(large, small, counts), proof_class)
            self.assertEqual([large[i] for i in (0, 1, 13, 14)], [1] * 4)
            self.assertGreaterEqual(large[2], 2)
            self.assertGreaterEqual(large[12], 2)
            if "auxiliary_scalar" in proof_class:
                self.assertEqual(counts[13:15], (3, 1))
                self.assertEqual(large[13], 1)  # target slice rank at large E00
            else:
                self.assertLessEqual(len(small), 13)

    def test_nonzero_count_tamper_is_rejected_by_complete_replay(self):
        changed = copy.deepcopy(self.report)
        changed["counts"]["pass_weight_capacity"] += 1
        with self.assertRaisesRegex(ArithmeticError, "complete exact enumeration"):
            MODULE.verify(changed)


if __name__ == "__main__":
    unittest.main()

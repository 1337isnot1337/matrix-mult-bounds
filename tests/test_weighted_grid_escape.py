"""Exact weighted-grid certificate and construction-search controls."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import unittest

PACKAGE = Path(__file__).resolve().parents[1] / 'research/ai/2026-10-23-grid-escape'
SPEC = importlib.util.spec_from_file_location('weighted_grid_escape', PACKAGE / 'verify.py')
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class WeightedGridEscapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vectors = V.load_vectors()
        cls.report = json.loads(V.REPORT.read_text())
        cls.w_vectors, cls.w_classes = V.load_w_vectors()
        cls.w_report = json.loads(V.W_REPORT.read_text())

    def test_quick_certificate_scope_and_split_seed(self):
        result = V.verify()
        self.assertEqual(result['original_weight'], 251)
        self.assertEqual(result['rank_four_flat_weight_cap'], 24)
        self.assertEqual(result['four_split_seed']['remaining_weight'], 238)
        self.assertTrue(result['four_split_seed']['excluded_by_weight'])
        self.assertEqual(result['unchanged_third_factor']['total_weight'], 149)
        self.assertEqual(result['unchanged_third_factor']['minimum_rank_four_groups_by_weight'], 10)
        self.assertTrue(result['unchanged_third_factor']['all_direction_preserving_termwise_candidates_excluded'])
        self.assertFalse(result['exhaustive_enumeration_rerun_by_this_command'])
        self.assertFalse(result['general_Q64_maps_excluded'])
        self.assertFalse(result['arbitrary_replacement_vectors_excluded'])
        self.assertFalse(result['improves_omega'])

    def test_deletion_threshold_is_necessary_only(self):
        exceptional = sorted(V.EXCEPTIONAL)
        ordinary = [i for i in range(76) if i not in V.EXCEPTIONAL]
        eight = V.deletion_screen(exceptional[:8])
        self.assertEqual(eight['removed_weight'], 32)
        self.assertTrue(eight['excluded_by_weight'])
        wrong_nine = V.deletion_screen(exceptional[:7] + ordinary[:2])
        self.assertEqual(wrong_nine['removed_weight'], 34)
        self.assertTrue(wrong_nine['excluded_by_weight'])
        necessary_nine = V.deletion_screen(exceptional[:8] + ordinary[:1])
        self.assertEqual(necessary_nine['removed_weight'], 35)
        self.assertFalse(necessary_nine['excluded_by_weight'])
        self.assertFalse(necessary_nine['grid_constructed'])
        for bad in ([0, 0], [-1], [76], [True], ['17']):
            with self.assertRaises(ValueError):
                V.deletion_screen(bad)

    def test_report_and_witness_corruption_rejected(self):
        changed = copy.deepcopy(self.report)
        changed['maximum_flat_weight'] = 25
        with self.assertRaises(ArithmeticError):
            V.check_report(changed, self.vectors)
        changed = copy.deepcopy(self.report)
        changed['size_exceptional_histogram'][-1][1] = 1
        with self.assertRaises(ArithmeticError):
            V.check_report(changed, self.vectors)
        changed = copy.deepcopy(self.report)
        changed['weighted_witness_members'].pop()
        with self.assertRaises(ArithmeticError):
            V.check_report(changed, self.vectors)
        changed = copy.deepcopy(self.report)
        changed['four_subsets'] -= 1
        with self.assertRaises(ArithmeticError):
            V.check_report(changed, self.vectors)

    def test_integer_to_modular_rank_direction(self):
        self.assertEqual(V.rank([[101, 0], [0, 1]]), 2)
        self.assertEqual(V.rank([[101, 0], [0, 1]], 101), 1)
        self.assertEqual(V.rank([]), 0)

    def test_third_factor_deduplication_and_cap_controls(self):
        self.assertEqual(sorted(i for group in self.w_classes for i in group), list(range(76)))
        self.assertEqual(len(self.w_classes), 58)
        self.assertEqual(sum(V.W_WEIGHTS), 149)
        changed = copy.deepcopy(self.w_report)
        changed['maximum_flat_weight'] = 15
        with self.assertRaises(ArithmeticError):
            V.check_w_report(changed, self.w_vectors)
        changed = copy.deepcopy(self.w_report)
        changed['flat_weight_histogram']['17'] = 1
        with self.assertRaises(ArithmeticError):
            V.check_w_report(changed, self.w_vectors)
        changed = copy.deepcopy(self.w_report)
        changed['weighted_witness_members'].pop()
        with self.assertRaises(ArithmeticError):
            V.check_w_report(changed, self.w_vectors)

    @unittest.skipUnless(shutil.which('cc') or shutil.which('gcc') or shutil.which('clang'),
                         'A C99 compiler is required for the full enumeration.')
    def test_complete_four_subset_replay(self):
        actual = V.enumerate_flats(self.vectors)
        V.check_report(actual, self.vectors)
        self.assertEqual(actual, self.report)
        actual_w = V.enumerate_flats(self.w_vectors, V.W_WEIGHTS)
        V.check_w_report(actual_w, self.w_vectors)
        self.assertEqual(actual_w, self.w_report)


if __name__ == '__main__':
    unittest.main()

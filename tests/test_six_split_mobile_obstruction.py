"""Complete saturation coverage and exact mobile-span obstruction controls."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import unittest


PACKAGE = Path(__file__).resolve().parents[1] / 'research/ai/2026-10-23-six-split-mobile-obstruction'
SPEC = importlib.util.spec_from_file_location('six_split_mobile', PACKAGE / 'verify.py')
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class SixSplitMobileObstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vectors, cls.mobile, cls.checks, cls.positive_rank = V.configuration()
        cls.report = json.loads((PACKAGE / 'enumeration.json').read_text())

    def test_component_images_and_saturation_hypotheses(self):
        self.assertEqual(self.checks, 3978)
        self.assertEqual(self.positive_rank, 20)
        self.assertEqual(sum(V.S.WEIGHTS), 144)
        self.assertEqual(self.report['maximum_fixed_weight'], 16)
        self.assertEqual(self.report['unique_saturated_flats'], 21649)
        self.assertEqual(self.report['saturated_basis_count'], 25332)
        V.check_report(self.report, self.vectors, self.mobile)
        for index, record in enumerate(self.report['mobile_pairs']):
            basis = [self.vectors[i] for i in record['allowed_line_witness_basis']]
            x, y = self.mobile[2 * index:2 * index + 2]
            self.assertEqual(V.S.C.W.rank([x, y]), 2)
            self.assertEqual(V.S.C.W.rank(basis + [x]), 4)
            self.assertEqual(V.S.C.W.rank(basis + [x, y]), 5)

    def test_bounded_entry_requirement_is_enforced(self):
        V.check_small_entries(self.vectors, self.mobile)
        changed = [list(row) for row in self.vectors]
        changed[0][0] = 2
        with self.assertRaises(ArithmeticError):
            V.check_small_entries(changed, self.mobile)
        changed_mobile = copy.deepcopy(self.mobile)
        changed_mobile[0][0] = 101
        with self.assertRaises(ArithmeticError):
            V.check_small_entries(self.vectors, changed_mobile)
        # Without a bounded-entry hypothesis the modular rank can drop.
        self.assertEqual(V.S.C.W.rank([[1009, 0], [0, 1]]), 2)
        self.assertEqual(V.S.C.W.rank([[1009, 0], [0, 1]], 1009), 1)

    def test_counter_and_intersection_corruption_is_rejected(self):
        changed = copy.deepcopy(self.report)
        changed['unique_saturated_flats'] -= 1
        with self.assertRaises(ArithmeticError):
            V.check_report(changed, self.vectors, self.mobile)
        changed = copy.deepcopy(self.report)
        changed['mobile_pairs'][0]['rank_increment_failures'] = 1
        with self.assertRaises(ArithmeticError):
            V.check_report(changed, self.vectors, self.mobile)
        changed = copy.deepcopy(self.report)
        changed['mobile_pairs'][1]['rank_pair_histogram'][1][2] -= 1
        with self.assertRaises(ArithmeticError):
            V.check_report(changed, self.vectors, self.mobile)
        changed_mobile = copy.deepcopy(self.mobile)
        changed_mobile[1] = changed_mobile[0][:]
        with self.assertRaises(ArithmeticError):
            V.check_report(self.report, self.vectors, changed_mobile)

    def test_scope_and_retained_certificate(self):
        result = V.verify()
        self.assertEqual(result['claim_id'], 'AI-EXTERNAL-SIX-SPLIT-MOBILE-009')
        self.assertTrue(result['saturated_fixed_sets_have_rank_four'])
        self.assertTrue(result['all_finite_standard_flips_full_W_nine_cover_excluded'])
        self.assertTrue(result['full_W_nine_cover_after_minimum_term_component_refactorizations_excluded'])
        self.assertTrue(result['fixed_47_direction_cover_remains_valid'])
        self.assertEqual(result['mobile_W_flattening_ranks'], [2, 2])
        self.assertEqual(result['possible_intersection_span_dimensions'], [1, 1])
        self.assertIn('25-dimensional target leg', result['grid_alignment'])
        self.assertFalse(result['general_Q64_maps_excluded'])
        self.assertFalse(result['further_singular_degenerations_excluded'])
        self.assertFalse(result['other_split_seeds_excluded'])
        self.assertFalse(result['improves_omega'])
        self.assertFalse(result['exhaustive_enumeration_rerun_by_this_command'])
        retained = json.loads((PACKAGE / 'certificate.json').read_text())
        self.assertTrue(retained['exhaustive_enumeration_rerun_by_this_command'])
        retained['exhaustive_enumeration_rerun_by_this_command'] = False
        self.assertEqual(result, retained)

    @unittest.skipUnless(shutil.which('cc') or shutil.which('gcc') or shutil.which('clang'),
                         'A C99 compiler is required for the full enumeration.')
    def test_full_saturation_and_intersection_replay(self):
        actual = V.enumerate_saturated(self.vectors, self.mobile)
        V.check_report(actual, self.vectors, self.mobile)
        self.assertEqual(actual, self.report)


if __name__ == '__main__':
    unittest.main()

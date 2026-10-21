import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions'
RESULTS = ROOT / 'results/anisotropic-constructions-2026-10-20'


def load(name):
    spec = importlib.util.spec_from_file_location(name, RESEARCH / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MIXED = load('parity_balancing_mixed_grading')
SEED = load('parity_balancing_three_weight_seed')


class MixedGradingTests(unittest.TestCase):
    def test_exact_separate_masks_and_760_row_restriction(self):
        actual = MIXED.replay()
        recorded = json.loads((RESULTS / 'parity_balancing_mixed_grading.json').read_text())
        self.assertEqual(actual, recorded)
        self.assertEqual(actual['source_terms_checked'], 262144)
        self.assertEqual([case['final_available_dimensions'] for case in actual['cases']],
                         [[922, 960, 960], [724, 724, 960], [468, 468, 468]])
        counts = actual['selected_row_count_cases']
        self.assertTrue(counts[0]['excluded'])
        self.assertEqual(counts[0]['final_available_dimensions'], [756, 756, 960])
        self.assertFalse(counts[1]['excluded'])
        self.assertEqual(counts[1]['final_available_dimensions'], [922, 922, 960])
        self.assertEqual(actual['at_least_two_legs_each_require_this_many_three_or_more_weight_images'], 19)

    def test_actual_balanced_maps_full_tensor_inverse_and_grade_removal(self):
        data = json.loads((RESULTS / 'parity_balancing_three_weight_seed.json').read_text())
        data['replay_report'] = {'complete_M12_plus_M3_identity_passed': False,
                                 'actual_map_ranks_by_inverse_basis_change': [0, 0, 0]}
        report = SEED.verify(data)
        self.assertEqual(report['actual_nonzero_tensor_coefficients'], 1755)
        self.assertEqual(report['actual_map_ranks_by_inverse_basis_change'], [153] * 3)
        self.assertEqual(report['actual_map_nonzero_counts'], [333] * 3)
        self.assertEqual(report['actual_source_weight_count_histograms'], [{1: 45, 2: 72, 3: 36}] * 3)
        self.assertFalse(report['grade_preserving_parts_alone_reproduce_target'])
        self.assertEqual(report['graded_part_error_nonzero_coefficients'], 648)
        self.assertEqual(report['graded_part_error_squared_norm'], 648)
        self.assertFalse(report['full_A88_to_M27_plus_M7_witness'])

    def test_nonzero_tamper_and_all_zero_maps_rejected(self):
        data = SEED.build()
        changed = copy.deepcopy(data)
        changed['maps'][0][0][2] *= 2
        with self.assertRaisesRegex(ArithmeticError, 'coefficient identity'):
            SEED.verify(changed)
        changed = copy.deepcopy(data)
        changed['maps'] = [[], [], []]
        with self.assertRaisesRegex(ArithmeticError, 'coefficient identity'):
            SEED.verify(changed)

    def test_duplicate_and_out_of_range_actual_entries_rejected(self):
        data = SEED.build()
        changed = copy.deepcopy(data)
        changed['maps'][0].append(changed['maps'][0][0][:])
        with self.assertRaisesRegex(ArithmeticError, 'duplicate'):
            SEED.verify(changed)
        changed = copy.deepcopy(data)
        changed['maps'][0][0][1] = 960
        with self.assertRaisesRegex(ArithmeticError, 'invalid'):
            SEED.verify(changed)


if __name__ == '__main__':
    unittest.main()

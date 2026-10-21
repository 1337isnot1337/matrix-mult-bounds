import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_unequal_profiles.py'
SPEC = importlib.util.spec_from_file_location('parity_balancing_unequal_profiles', SCRIPT)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)
DATA = ROOT / 'results/anisotropic-constructions-2026-10-20/parity_balancing_unequal_profiles.json'
HISTORICAL = DATA.with_name('parity_balancing_unequal_neighbor_hole_partial.json')


class UnequalProfileTests(unittest.TestCase):
    def test_actual_unequal_maps_and_complete_source_replay(self):
        data = json.loads(DATA.read_text())
        data['screen_report'] = {'recorded_screens_pass': False}
        result = MOD.verify(data)
        self.assertEqual(result['complete_source_terms_enumerated'], 262144)
        self.assertEqual(result['nonzero_partial_tensor_coefficients'], 1755)
        self.assertEqual(result['actual_map_ranks'], [153, 153, 153])
        self.assertEqual(result['profile_screens_recomputed']['target_zero_dimensions'], [60, 60, 60])
        self.assertTrue(result['all_three_maps_respect_actual_unequal_vertex_charges'])
        self.assertTrue(result['profile_screens_recomputed']['recorded_screens_pass'])
        self.assertFalse(result['full_target_witness'])

    def test_nonzero_coefficient_and_charge_metadata_tampering_rejected(self):
        data = json.loads(DATA.read_text())
        altered = copy.deepcopy(data)
        altered['partial_maps'][0][0][2] = 2
        with self.assertRaisesRegex(ArithmeticError, 'coefficient identity'):
            MOD.verify(altered)
        altered = copy.deepcopy(data)
        altered['vertex_charges'][0][0][0] = 1
        with self.assertRaisesRegex(ArithmeticError, 'actual profiles'):
            MOD.verify(altered)

    def test_historical_seed_exact_but_full_profile_screen_fails(self):
        result = MOD.verify(json.loads(HISTORICAL.read_text()))
        self.assertEqual(result['nonzero_partial_tensor_coefficients'], 1755)
        self.assertTrue(result['known_recorded_profile_obstruction_detected'])
        failures = result['profile_screens_recomputed']['degree13_endpoint_sylvester_failures']
        self.assertEqual(len(failures), 1)
        self.assertEqual(failures[0]['source_slice_rank_lower_bound'], 2)
        self.assertEqual(failures[0]['required_target_slice_rank'], 1)
        self.assertFalse(result['full_target_witness'])


if __name__ == '__main__':
    unittest.main()

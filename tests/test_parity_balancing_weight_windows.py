import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_weight_windows.py'
SPEC = importlib.util.spec_from_file_location('parity_balancing_weight_windows', SCRIPT)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)
DATA = ROOT / 'results/anisotropic-constructions-2026-10-20/parity_balancing_weight_windows.json'


class WeightWindowTests(unittest.TestCase):
    def test_all_six_exact_window_controls_and_actual_rank_atom(self):
        result = MOD.verify(json.loads(DATA.read_text()))
        self.assertEqual(result['complete_source_terms_enumerated'], 262144)
        cases = {(case['maximum_source_weight_span'], tuple(case['selected_legs'])): case
                 for case in result['cases']}
        self.assertEqual(cases[2, (0, 1, 2)]['final_available_dimensions'], [740] * 3)
        self.assertEqual(cases[3, (0, 1, 2)]['final_available_dimensions'], [622] * 3)
        self.assertEqual(cases[4, (0, 1, 2)]['final_available_dimensions'], [960] * 3)
        self.assertEqual(cases[2, (0, 1)]['final_available_dimensions'], [876, 876, 960])
        self.assertEqual(cases[3, (0, 1)]['final_available_dimensions'], [906, 906, 960])
        atom = result['three_weight_rank_atom']
        self.assertEqual(atom['actual_source_slice_rank'], 384)
        self.assertEqual(atom['middle_component_slice_rank'], 512)
        self.assertEqual(atom['tridiagonal_three_by_three_minor'], 1)
        self.assertFalse(result['arbitrary_ungraded_restrictions_excluded'])

    def test_supporting_plane_that_cuts_a_good_point_is_rejected(self):
        data = json.loads(DATA.read_text())
        first_polytope = data['cases'][0]['rounds'][0]['selected_leg_polytopes'][0]['polytope_indices'][0]
        plane_index = data['window_polytopes'][first_polytope]['plane_indices'][0]
        data['supporting_planes'][plane_index] = [0, 0, 0, -1]
        with self.assertRaisesRegex(ArithmeticError, 'cuts an admissible'):
            MOD.verify(data)

    def test_false_exclusion_of_surviving_window_is_rejected(self):
        data = json.loads(DATA.read_text())
        selected = next(case for case in data['cases'] if case['maximum_source_weight_span'] == 4)
        selected['ordinary_restriction_excluded'] = True
        with self.assertRaisesRegex(ArithmeticError, 'exclusion claim'):
            MOD.verify(data)

    def test_nonzero_rank_atom_coefficient_tamper_is_rejected(self):
        data = json.loads(DATA.read_text())
        atom = copy.deepcopy(data['three_weight_rank_atom'])
        atom['hankel_coefficients'][1][1] = [1, 1]
        with self.assertRaisesRegex(ArithmeticError, 'Hankel rank'):
            MOD.verify_atom(atom, MOD.CORE.source())


if __name__ == '__main__':
    unittest.main()

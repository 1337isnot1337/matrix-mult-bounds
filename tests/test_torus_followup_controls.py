import importlib.util
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / 'research/ai/2026-10-20-anisotropic-constructions'


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(HERE))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(HERE))
    return module


def json_normalized(value):
    return json.loads(json.dumps(value))


class TorusFollowupControlTests(unittest.TestCase):
    def test_affine_builder_has_independent_physical_matrix_control(self):
        module = load('parity_structure_affine_audit')
        actual = module.verify()
        expected = json.loads((HERE / 'parity_structure_affine_audit.json').read_text())
        self.assertEqual(json_normalized(actual), expected)
        self.assertEqual(actual['normalized_equations_reconstructed_by_physical_traces'], 36)
        self.assertTrue(actual['feasible_solution_verified_by_physical_traces'])
        self.assertTrue(actual['nonlinear_free_by_free_slice_rejected'])

    def test_fixed_small_matrix_channels_expose_too_many_source_coordinates(self):
        module = load('parity_structure_free_m7_screen')
        actual = module.verify()
        expected = json.loads((HERE / 'parity_structure_free_m7_screen.json').read_text())
        self.assertEqual(json_normalized(actual), expected)
        for name, legs in actual['screens'].items():
            for leg in legs:
                self.assertFalse(leg['total_dimension_inequality_passes'])
                self.assertEqual(leg['pair_contraction_rank'], 637 if name == 'equal_diagonal_mix' else 343)

    def test_complete_common_vertex_screen_and_balanced_laurent_obstructions(self):
        module = load('parity_structure_m7_vertex_screen')
        actual = module.verify()
        expected = json.loads((HERE / 'parity_structure_m7_vertex_screen.json').read_text())
        self.assertEqual(json_normalized(actual), expected)
        self.assertEqual(actual['complete_choices'], 1290240)
        self.assertEqual(actual['surviving_capacity_choices'], 16)
        for row in actual['near_seeds']:
            self.assertEqual(row['unwanted_terms'], 498)
            self.assertTrue(row['coefficientwise_Laurent_rescaling_obstructed'])
        self.assertEqual(actual['positive_M2_control']['weight_zero_pair_rank'], 2)

    def test_rank_one_transfer_symmetries_on_every_basis_matrix(self):
        module = load('parity_balancing_rankone_13_symmetry')
        actual = module.report()
        expected = json.loads((ROOT / 'results/anisotropic-constructions-2026-10-20/parity_balancing_rankone_13_symmetry.json').read_text())
        self.assertEqual(json_normalized(actual), expected)
        self.assertEqual(actual['source_basis_coordinates_checked'], 960)
        self.assertEqual(actual['target_matrix_unit_pairs_checked_per_identity'], 27**4 + 7**4)


if __name__ == '__main__':
    unittest.main()

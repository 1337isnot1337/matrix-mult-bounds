"""Complete local coefficient identities in the ordinary-kernel obstruction."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-paired-construction/narrow_kernel_controls.py'
SPEC = importlib.util.spec_from_file_location('narrow_kernel_controls', PATH)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class NarrowKernelControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = module.run()

    def test_all_jet_identities_with_both_free_c_coordinates_retained(self):
        self.assertEqual([row['n'] for row in self.report['jets']], list(range(3, 9)))
        for row in self.report['jets']:
            self.assertEqual(abs(row['c_coordinate_change_determinant']), 1)
            self.assertEqual(row['source_monomials_expanded'], 4 * row['n'] ** 2)
            self.assertEqual(row['fibre_slice_equalities'], [True] * row['n'])
            self.assertTrue(row['offending_complete_identity_passes'])
            self.assertTrue(row['offending_free_coordinate_columns_zero'])
            self.assertEqual(row['paired_block_rank'], 1)

    def test_n3_offending_slice_is_exactly_the_stated_six_terms(self):
        row = self.report['jets'][0]
        expected = [[0] * 8 for _ in range(6)]
        for i, j, value in [(0, 1, 1), (0, 2, -1), (2, 3, 1),
                            (1, 3, 1), (1, 4, -1), (3, 5, 1)]:
            expected[i][j] = value
        self.assertEqual(row['offending_full_matrix'], expected)
        self.assertEqual(row['paired_block'], [[0, 1]] + [[0, 0]] * 5)

    def test_uniform_kernels_cannot_supply_the_required_six_dimensional_support(self):
        self.assertEqual(len(self.report['uniforms']), 5)
        for row in self.report['uniforms']:
            self.assertEqual(row['kernel_dimension'], 2)
            self.assertEqual(row['combined_b_span'], 2)
            self.assertEqual(row['combined_c_span'], 4)
            self.assertEqual(row['individual_slice_ranks'], [2, 2, 2])
            self.assertFalse(row['c_quotient_applied'])
        self.assertFalse(self.report['improves_omega'])


if __name__ == '__main__':
    unittest.main()

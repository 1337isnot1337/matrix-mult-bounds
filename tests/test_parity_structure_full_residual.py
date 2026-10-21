"""Exact, standard-library-only coverage of the retained residual and seed limit."""

import importlib
from pathlib import Path
import sys
import unittest


RESEARCH = (Path(__file__).resolve().parents[1]
            / 'research' / 'ai' / '2026-10-20-anisotropic-constructions')
sys.path.insert(0, str(RESEARCH))
try:
    full_residual = importlib.import_module('parity_structure_full_residual_stdlib')
    fixed_core = importlib.import_module('parity_structure_fixed_core')
finally:
    sys.path.remove(str(RESEARCH))


class FullResidualAndFixedCoreTests(unittest.TestCase):
    def test_complete_a78_contraction_and_nonzero_tamper(self):
        result = full_residual.verify()
        self.assertEqual(result['source_terms'], 175616)
        self.assertEqual(result['target_terms'], 2728)
        self.assertEqual(result['target_format'], [204, 204, 204])
        self.assertEqual(result['numerator_nonzero_counts'], [2624, 2624, 2624])
        self.assertTrue(result['all_output_coefficients_exact'])
        self.assertTrue(result['all_mixed_coefficients_zero'])
        self.assertTrue(result['one_entry_tamper_rejected_by_complete_contraction'])
        self.assertFalse(result['new_exponent_established'])

    def test_fixed_core_kernel_from_full_contraction(self):
        result = fixed_core.verify()
        self.assertEqual(result['source_terms_replayed'], 175616)
        self.assertEqual(result['nonzero_two_core_contraction_coefficients'], 13312)
        self.assertEqual(result['local_factor_ranks'], [7, 12, 8])
        self.assertEqual(result['two_core_contraction_ranks'], [672, 672, 672])
        self.assertEqual(result['two_core_kernel_dimensions'], [112, 112, 112])
        self.assertEqual(result['fixed_core_target_leg_dimension_max'], 256)
        self.assertTrue(result['complete_two_core_factorization_exact'])
        self.assertTrue(result['source_and_all_core_cyclic_identifications_exact'])
        self.assertFalse(result['new_exponent_established'])


if __name__ == '__main__':
    unittest.main()

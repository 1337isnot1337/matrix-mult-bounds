import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_crossed_flattening.py'
SPEC = importlib.util.spec_from_file_location('crossed_flattening', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CrossedFlatteningTests(unittest.TestCase):
    def test_all_exact_factors_targets_and_slice_strata(self):
        report = MODULE.verify()
        self.assertEqual([record['rank'] for record in report['source_flattenings']], [45, 32, 90, 64])
        self.assertEqual([record['rank'] for record in report['slice_normal_forms']], [32, 36, 64, 72])
        self.assertEqual(report['target_flattenings'][-1]['rank'], 108)
        self.assertFalse(report['arbitrary_singular_first_map_exclusion_claimed'])
        self.assertFalse(report['full_source_A88_M27_plus_M7_excluded'])
        fixed = report['full_source_fixed_first_control']
        self.assertEqual(fixed['original_A88_terms_checked'], 262144)
        self.assertEqual(fixed['contributing_original_terms'], 2560)
        self.assertEqual(fixed['full_flattening_rank'], 360)
        self.assertEqual(fixed['fixed_first_images_middle_bound'], 22)

    def test_modified_source_coefficient_is_rejected(self):
        terms = MODULE.source_terms(1)
        x, y, z, value = terms[0]
        terms[0] = (x, y, z, value + 1)
        with self.assertRaises(ArithmeticError):
            MODULE.verify_factorization(terms, 1)

    def test_non_product_first_map_is_outside_rank45_scope(self):
        terms = MODULE.source_terms(1)
        terms += [(0, y, z, value) for x, y, z, value in MODULE.source_terms(1) if x == 3]
        self.assertEqual(MODULE.rank_modulo(MODULE.flatten(terms, 40, 36)), 66)
        with self.assertRaises(ArithmeticError):
            MODULE.verify_factorization(terms, 1)


if __name__ == '__main__':
    unittest.main()

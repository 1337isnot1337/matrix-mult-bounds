"""Exact controls for the full-source low-rank slice locus."""
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-20-anisotropic-constructions'
sys.path.insert(0,str(PACKAGE))
import polynomial_rank_locus as locus


class PolynomialRankLocusTests(unittest.TestCase):
    def test_all_binary_slices_and_saved_exact_controls(self):
        actual=json.loads(json.dumps(locus.report()))
        saved=json.loads((ROOT/'results/anisotropic-constructions-2026-10-20/polynomial-rank-locus-controls.json').read_text())
        self.assertEqual(actual,saved)
        binary=actual['binary_exhaustive_control']
        self.assertEqual(binary['nonzero_slices_checked'],4095)
        self.assertEqual(binary['slices_below_2ab'],45)
        self.assertEqual(binary['symbol_rank_slice_histograms']['1'],{'4':27,'6':18})
        self.assertEqual(sum(binary['symbol_rank_slice_histograms']['2'].values()),4050)
        self.assertFalse(actual['new_exponent_established'])
        self.assertFalse(actual['singular_exclusion_claimed'])

    def test_three_leg_factorization_and_strict_threshold(self):
        for row in locus.three_leg_controls():
            self.assertEqual(row['direct_integer_value'],row['separated_integer_value'])
        for row in locus.sharp_threshold_controls():
            self.assertEqual(row['exact_rank'],2*row['a']*row['b'])
            self.assertFalse(row['constant_coherent_factor'])
        source=locus.square_subsum_screen(5,5,(14,3),(1,))
        self.assertEqual(source['maximum_lifted_slice_rank'],49)
        self.assertTrue(source['ordinary_restriction_excluded'])
        self.assertFalse(source['singular_degeneration_excluded'])

    def test_live_targets_are_not_rejected_by_this_screen(self):
        self.assertFalse(locus.rectangular_screen(5,5,(14,14,14))['ordinary_restriction_excluded'])
        self.assertFalse(locus.rectangular_screen(5,6,(15,17,17))['ordinary_restriction_excluded'])
        self.assertFalse(locus.square_subsum_screen(5,6,(16,4),(1,))['ordinary_restriction_excluded'])
        strict=locus.square_block_rank_one_screen(5,6,(16,3,3))
        self.assertTrue(strict['ordinary_restriction_excluded'])
        boundary=locus.square_block_rank_one_screen(5,6,(16,4))
        self.assertFalse(boundary['ordinary_restriction_excluded'])
        self.assertEqual(boundary['non_scalar_block_tests'][1]['lifted_rank_one_slice_upper_bound'],60)
        self.assertTrue(locus.rectangular_screen(5,5,(15,15,15))['ordinary_restriction_excluded'])


if __name__=='__main__':
    unittest.main()

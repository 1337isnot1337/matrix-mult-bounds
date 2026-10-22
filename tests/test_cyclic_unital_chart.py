"""Exact block-rank sharpness and hypothesis controls for the all-order unital proof."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-cyclic-slice-determinants'
spec=importlib.util.spec_from_file_location('cyclic_unital_rank_controls',PACKAGE/'unital_controls.py')
controls=importlib.util.module_from_spec(spec);spec.loader.exec_module(controls)


class CyclicUnitalChartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=json.loads((ROOT/'results/cyclic-slice-determinants-2026-10-21/unital-controls.json').read_text())

    def test_complete_exact_control_replay(self):
        receipt=controls.verify(self.report)
        self.assertEqual([r['actual_rank'] for r in receipt['sharp_rank_controls']],[5,4])
        self.assertTrue(receipt['excluded_all_finite_pole_orders_under_hypotheses'])
        self.assertEqual(receipt['constant_image_control']['principal_image_dimension'],11)
        self.assertEqual(receipt['constant_image_control']['raw_constant_coefficient_rank'],11)
        self.assertEqual(receipt['constant_image_control']['regularized_constant_rank'],1)
        self.assertFalse(receipt['constant_image_control']['full_Laurent_map'])
        self.assertFalse(receipt['all_A4_degenerations_excluded'])
        self.assertEqual(controls.report(),self.report)

    def test_general_block_bound_is_sharp_on_literal_integer_matrices(self):
        for k in [1,2,3]:
            for d in [k]:
                for h in range(1,k+1):
                    witness=controls.sharp_leading_matrix(d,k,h)
                    receipt=controls.verify_leading(witness)
                    self.assertEqual(receipt['actual_rank'],d+2*k-h)

    def test_missing_hypotheses_and_inflated_status_are_rejected(self):
        for key in ['requires_regular_full_rank_long_leg','requires_regular_invertible_source_unit_lift']:
            bad=copy.deepcopy(self.report);bad['A4_budget'][key]=False
            with self.assertRaises(ValueError):controls.verify(bad)
        bad=copy.deepcopy(self.report);bad['A4_budget'].pop('all_finite_pole_orders_excluded_under_hypotheses')
        with self.assertRaises(ValueError):controls.verify(bad)
        bad=copy.deepcopy(self.report);bad['improves_omega']=True
        with self.assertRaises(ValueError):controls.verify(bad)
        bad=copy.deepcopy(self.report)
        bad['A4_budget']['first_pole_source_rank_ceiling']=16
        with self.assertRaises(ValueError):controls.verify(bad)

    def test_false_matrix_rank_and_incomplete_principal_control_are_rejected(self):
        bad=copy.deepcopy(self.report)
        witness=bad['sharp_rank_witnesses'][0]
        witness['source_matrix'][witness['R']][0]=1
        with self.assertRaises(ValueError):controls.verify(bad)
        bad=copy.deepcopy(self.report);bad['constant_image_control']['coefficients'].pop()
        with self.assertRaises(ValueError):controls.verify(bad)


if __name__=='__main__':unittest.main()

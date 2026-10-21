"""Exact replay and scope controls for the graded fixed-core bound."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT=Path(__file__).resolve().parents[1]
FILE=ROOT/'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_fixed_core_weights.py'
SPEC=importlib.util.spec_from_file_location('parity_balancing_fixed_core_weights',FILE)
CORE=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)
DATA=ROOT/'results/anisotropic-constructions-2026-10-20/parity_balancing_fixed_core_weights.json'


class GradedFixedCoreTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(DATA.read_text())

    def test_complete_core_tensors_and_exact_graded_bounds(self):
        expected={'endpoint_M2':(6,62,False),'endpoint_M4':(44,58,True),
                  'monotone_M6':(138,52,True),'repeated_short_index_M6':(192,42,True),
                  'monotone_M8':(312,44,True)}
        for case in self.data['cases']:
            with self.subTest(core=case['name']):
                report=CORE.verify_case(case)
                rank,zero_bound,excluded=expected[case['name']]
                self.assertEqual(report['total_pair_contraction_rank'],rank)
                self.assertEqual(report['weight_blocks'][14]['fixed_core_extension_dimension_upper_bound'],zero_bound)
                self.assertEqual(report['fixed_core_extension_to_current_torus_profile_excluded'],excluded)
                self.assertEqual(report['nonzero_core_coefficients'],case['core_order']**3)
                self.assertEqual(report['full_source_terms_enumerated'],262144)
                self.assertFalse(report['changing_core_maps_excluded'])
                self.assertFalse(report['arbitrary_source_degenerations_excluded'])

    def test_consistent_changed_selector_is_rejected_by_tensor_replay(self):
        case=copy.deepcopy(self.data['cases'][1])
        # Replace E00's selector by another weight-zero coordinate and
        # update every redundant map copy. The tensor identity must fail.
        entry=next(entry for entry in case['common_coordinate_map'] if entry[0]==0)
        entry[1]=0
        a,b=case['source_lengths']
        case['maps']=[[[row,CORE.original_column(a,b,leg,column),value]
                       for row,column,value in case['common_coordinate_map']] for leg in range(3)]
        with self.assertRaisesRegex(ArithmeticError,'core matrix tensor identity'):
            CORE.verify_case(case)

    def test_recorded_rank_metadata_does_not_determine_the_result(self):
        case=copy.deepcopy(self.data['cases'][1])
        case['verification']['total_pair_contraction_rank']=0
        case['verification']['fixed_core_extension_to_current_torus_profile_excluded']=False
        for block in case['verification']['weight_blocks']:
            block['exact_pair_contraction_rank']=0
            block['violated']=False
        report=CORE.verify_case(case,full_source_check=False)
        self.assertEqual(report['total_pair_contraction_rank'],44)
        self.assertEqual(report['violated_weights'],[-12,0,12])


if __name__=='__main__':
    unittest.main()

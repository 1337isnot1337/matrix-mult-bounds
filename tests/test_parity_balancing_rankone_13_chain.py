import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT=Path(__file__).resolve().parents[1]
FILE=ROOT/'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_rankone_13_chain.py'
SPEC=importlib.util.spec_from_file_location('parity_balancing_rankone_13_chain',FILE)
CHAIN=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHAIN)
DATA=ROOT/'results/anisotropic-constructions-2026-10-20/parity_balancing_rankone_13_chain.json'


class RankOneDegree13ChainTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads(DATA.read_text())

    def test_complete_symbolic_slices_shifts_and_independent_forms(self):
        result=CHAIN.verify(self.data)
        self.assertTrue(result['both_symbolic_source_slice_identities_exact'])
        self.assertTrue(result['all_seven_low_coordinate_shifts_exact'])
        self.assertEqual(result['rowspace_dimension_contradiction'],[3,2])
        self.assertEqual(self.data['fixed_rank_one_anchors_needed_on_adjacent_legs'],2)
        self.assertFalse(self.data['negative_extreme_assumptions_used'])
        self.assertFalse(result['arbitrary_degree13_pencils_excluded'])

    def test_changed_source_anchor_does_not_satisfy_the_hypotheses(self):
        altered=copy.deepcopy(self.data)
        altered['rank_one_source_anchor'][1]=1
        with self.assertRaisesRegex(ArithmeticError,'degree-13 source anchor'):
            CHAIN.verify(altered)

    def test_changed_high_shift_is_rejected(self):
        altered=copy.deepcopy(self.data)
        altered['K12'][1][1]+=1
        with self.assertRaisesRegex(ArithmeticError,'stored coordinate'):
            CHAIN.verify(altered)


if __name__=='__main__':
    unittest.main()

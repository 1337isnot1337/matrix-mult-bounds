import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('moving_support_linearity_controls',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/multiple_support_linearity.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class MovingSupportLinearityTests(unittest.TestCase):
 def test_complete_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/multiple-support-linearity.json').read_text()))
 def test_strict_dimension_gaps_and_bad_control(self):
  r=v.report();self.assertLess(r['nongood_family_dimension_bound'],r['rank_two_parameter_dimension']);self.assertLess(r['fixed_scheme_image_dimension_bound'],r['required_injective_leg_dimension'])
  self.assertEqual([x['velocity_square_map_rank'] for x in r['stationarity_controls']],[7,7,6])
if __name__=='__main__':unittest.main()

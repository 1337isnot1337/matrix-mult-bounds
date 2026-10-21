import importlib.util,json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'research/ai/2026-10-21-rectangular-direct-sums/two_ruling_cap.py';spec=importlib.util.spec_from_file_location('two_ruling_test',P);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class TwoRulingTests(unittest.TestCase):
 def test_saved_controls(self):self.assertEqual(e.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/two-ruling-cap.json').read_text()))
 def test_general_equality_cases(self):
  r=e.report();self.assertEqual(sum(x['integer_pairs'] for x in r['general_integer_controls']),2815)
  for x in r['general_integer_controls']:
   self.assertEqual(x['proved_bound'],x['r']**2//4)
   for p,q,core,row in x['exceptional_cases']:self.assertEqual(p,q);self.assertGreaterEqual(row,2);self.assertGreater(2*p,x['r'])
 def test_small_rank_counterexample_preserved(self):self.assertEqual(e.report()['r5_counterexample'],{'two_ruling_rank':5,'full_dimension':7})
 def test_M30_witness(self):
  w=e.exclusion(8,9,[(30,30,30)],[900,900,900]);self.assertEqual((w['lift_upper'],w['next_symbol_threshold'],w['coefficient_cap'],w['target_parameter_dimension']),(564,576,864,900))
 def test_M33_witness_and_scope_guard(self):
  w=e.exclusion(8,10,[(33,33,33)],[1089]*3);self.assertEqual((w['lift_upper'],w['next_symbol_threshold'],w['coefficient_cap']),(608,640,960))
  # A(10,10) now has a replayed cap certificate in the size-2000 scan.
  w=e.exclusion(10,10,[(40,40,40)],[1600]*3)
  self.assertEqual((w['lift_upper'],w['next_symbol_threshold'],w['coefficient_cap']),(720,1000,1300))
  # A(10,11) remains outside the certified format guard.
  self.assertIsNone(e.exclusion(10,11,[(40,40,40)],[1600]*3))

 def test_three_ruling_bound_and_target(self):
  self.assertEqual(e.ruling_bound(8,3),11)
  w=e.exclusion(9,9,[(32,33,33)],[1056,1089,1056]);self.assertEqual((w['input_rank_cap'],w['lift_upper'],w['next_symbol_threshold'],w['coefficient_cap']),(3,708,729,891))

import importlib.util,json
from pathlib import Path
from math import isqrt
import unittest
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'research/ai/2026-10-21-rectangular-direct-sums/single_frontier.py';spec=importlib.util.spec_from_file_location('frontier1500',P);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class Frontier1500Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.actual=e.report(1500)
 def test_saved_complete_report(self):self.assertEqual(self.actual,json.loads((ROOT/'results/rectangular-direct-sums-20261021/single-frontier-1500.json').read_text()))
 def test_only_remaining_target_and_conditional_comparison(self):
  kept=[(s['a'],s['b'],s['source_leg_dimension'],r['shape']) for s in self.actual['sources'] for r in s['records'] if r['gate']=='survives necessary tests'];self.assertEqual(kept,[(8,10,1360,[32,33,33])]);self.assertLess(52**9000,7527168**2246)
 def test_independent_interval_counts(self):
  self.assertEqual(self.actual['source_format_count'],86);self.assertEqual(self.actual['score_eligible_shape_count'],2184)
  for s in self.actual['sources']:
   N=s['source_leg_dimension'];D=3*(s['a']+s['b'])-2;count=sum(max(0,N//v-max(v,D**4//(216*u*v)+1)+1) for v in range(1,isqrt(N)+1) for u in range(1,v+1));self.assertEqual(count,len(s['records']))
 def test_one_step_gap_is_not_rounded(self):
  self.assertEqual(2*33+(1360-1089)+(1360-1056),641);self.assertEqual(8*80,640);self.assertIsNone(e.two.exclusion(8,10,[(32,33,33)],[1056,1089,1056]))

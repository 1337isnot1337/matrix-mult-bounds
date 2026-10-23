import importlib.util,json
from pathlib import Path
from math import isqrt
import unittest
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'research/ai/2026-10-21-rectangular-direct-sums/single_frontier.py';spec=importlib.util.spec_from_file_location('single_frontier_test',P);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class SingleFrontierTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.result=e.report()
 def test_saved_complete_report(self):
  self.assertEqual(self.result,json.loads((ROOT/'results/rectangular-direct-sums-20261021/single-frontier-1152.json').read_text()))
  self.assertEqual(self.result['gate_counts'],{'baseline':1181,'saturation':15,'second_boundary':3,'ruling_dimension':1})
 def test_independent_interval_counts(self):
  for source in self.result['sources']:
   N=source['source_leg_dimension'];D=3*(source['a']+source['b'])-2
   count=sum(max(0,N//v-max(v,D**4//(216*u*v)+1)+1) for v in range(1,isqrt(N)+1) for u in range(1,v+1))
   self.assertEqual(count,source['score_eligible_shapes'])
 def test_all_targets_excluded(self):
  kept=[(s['a'],s['b'],r['shape']) for s in self.result['sources'] for r in s['records'] if r['gate']=='survives necessary tests']
  self.assertEqual(kept,[])
 def test_size_eight_rank_three_witness(self):
  source=next(s for s in self.result['sources'] if (s['a'],s['b'])==(8,8));r=next(r for r in source['records'] if r['shape']==[27,28,28]);self.assertEqual(r['gate'],'saturation');w=r['witness'];self.assertEqual((w['input_rank_cap'],w['lift_upper'],w['next_symbol_threshold'],w['parameter_dimension'],w['symbol_injection_cap']),(3,464,512,756,448));self.assertLess(14,3*(3+2))
 def test_one_short_input_cannot_score(self):
  import sympy as s
  t=s.symbols('t');self.assertEqual(s.expand((3*(t+1)+1)**4-216*(t+1)**3),81*t**4+216*t**3+216*t**2+120*t+40)

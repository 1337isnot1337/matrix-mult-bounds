import importlib.util,json,copy
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'research/ai/2026-10-21-rectangular-direct-sums/ruling_two_sums.py';spec=importlib.util.spec_from_file_location('ruling_sums_test',P);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class RulingTwoSumTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.actual=e.report()
 def test_saved_report(self):self.assertEqual(self.actual,json.loads((e.RESULT/'ruling-refined-two-sums.json').read_text()))
 def test_counts_and_complete_predecessors(self):
  self.assertEqual((self.actual['predecessor_survivors'],self.actual['new_exclusions'],self.actual['remaining']),(4469,3717,752));self.assertEqual([(r['a'],r['b'],r['remaining_count']) for r in self.actual['formats']],[(8,9,0),(8,10,664),(9,9,88)])
 def test_changed_manifest_rejected_even_with_new_hash(self):
  data=json.loads((e.RESULT/'two-sum-ruling-input-a8-b9.json').read_text());previous=next(x for x in json.loads((e.RESULT/'extended-frontier.json').read_text()) if (x['a'],x['b'])==(8,9));data['shapes'][0][0][0]+=1;data['predecessor_sha256']=e.e.digest([e.reconstruct(8,9,s) for s in data['shapes']])
  with self.assertRaises(AssertionError):e.check_manifest(data,previous)
 def test_all_new_witnesses_have_strict_rank_and_dimension_gaps(self):
  for a,b in [(8,9),(8,10),(9,9)]:
   data=json.loads((e.RESULT/f'two-sum-ruling-input-a{a}-b{b}.json').read_text());N=a*b*(a+b-1)
   for shapes in data['shapes']:
    row=e.reconstruct(a,b,shapes);w=e.t.exclusion(a,b,shapes,row['leg_dimensions'])
    if w is None:continue
    shape=shapes[w['block']];leg=w['leg'];rank=e.e.screen.slice_minima(shape)[leg];expected=w['input_rank_cap']*rank+2*N-sum(row['leg_dimensions'])+row['leg_dimensions'][leg];self.assertEqual(w['lift_upper'],expected);self.assertLess(expected,w['next_symbol_threshold']);self.assertGreater(w['target_parameter_dimension'],w['coefficient_cap'])

import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('one_unit_relations',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/one_unit_syzygies.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class OneUnitRelationTests(unittest.TestCase):
 def test_saved_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/one-unit-syzygies.json').read_text()))
 def test_every_small_degree_and_window(self):
  for r in range(2,7):
   for T in range(2,8):
    for d in range(1,10):
     result=v.control(r,T,d)
     self.assertEqual(result['one_unit_equality'],d==1)
 def test_actual_source_relations(self):
  for a,b in [(2,3),(3,4),(8,10)]:
   self.assertEqual(v.source_control(a,b)['shifted_rank_mod_2'],a*a*b+1)
if __name__=='__main__':unittest.main()

import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('critical_states',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/critical_finite_states.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class CriticalStateTests(unittest.TestCase):
 def test_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/critical-finite-states.json').read_text()))
 def test_dimension_gaps(self):
  for rho in range(3,9):
   c=v.incidence(rho)
   self.assertLess(c['eight_state_bad_dimension'],126)
   if rho<=7:self.assertLess(c['nine_state_bad_dimension'],126)
 def test_all_partitions(self):
  p=list(v.partitions(8));self.assertEqual(len(p),22)
  self.assertEqual(sum(len(q)==8 for q in p),1)
if __name__=='__main__':unittest.main()

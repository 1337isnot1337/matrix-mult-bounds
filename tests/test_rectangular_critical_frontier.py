import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('critical_frontier',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/critical_frontier.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class CriticalFrontierTests(unittest.TestCase):
 def test_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/critical-frontier.json').read_text()))
 def test_counts(self):
  r=v.report();self.assertEqual(r['two_block_new_exclusions'],62);self.assertEqual(r['two_block_remaining'],690)
  self.assertEqual(sum(q['predecessor_count'] for q in r['formats']),752)
 def test_small_block_not_overexcluded(self):
  self.assertIsNone(v.witness([[20,20,20],[1,1,1]]))
if __name__=='__main__':unittest.main()

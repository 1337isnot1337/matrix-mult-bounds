import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('flat_realization',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/flat_realization.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class FlatRealizationTests(unittest.TestCase):
 def test_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/flat-realization.json').read_text()))
 def test_failure_is_not_nonexistence(self):
  r=v.report()
  self.assertFalse(r['nonflat_nine_state_control']['flat'])
  self.assertEqual(r['nonflat_nine_state_control']['full_rank'],9)
  self.assertFalse(r['nonflat_implies_no_realization'])
 def test_zero(self):
  self.assertEqual(v.realize([v.s.zeros(2,3) for _ in range(4)],2,3)['state_dimension'],0)
if __name__=='__main__':unittest.main()

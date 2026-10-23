import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('equivariant_frontier',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/equivariant_frontier.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class EquivariantFrontierTests(unittest.TestCase):
 def test_complete_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/equivariant-frontier.json').read_text()))
 def test_both_parity_enumerations(self):
  self.assertEqual(v.parts(6,1),((2,2,2),(2,4),(6,)))
  self.assertFalse(v.parts(5,1))
  self.assertEqual(v.parts(3,0),((1,1,1),(3,)))
if __name__=='__main__':unittest.main()

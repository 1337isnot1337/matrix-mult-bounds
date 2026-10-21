import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('generic_flatness',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/generic_flatness.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class GenericFlatnessTests(unittest.TestCase):
 def test_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/generic-flatness.json').read_text()))
 def test_identity_coordinate_change(self):
  M=[v.s.Matrix([[k]]) for k in range(17)]
  self.assertEqual(v.coordinate_change(M,0),M)
if __name__=='__main__':unittest.main()

import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('moving_support_controls',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/multiple_support_family.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class MovingSupportFamilyTests(unittest.TestCase):
 def test_full_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/multiple-support-family.json').read_text()))
 def test_full_ambient_span(self):
  self.assertEqual(v.span_control(8,10)['certified_linear_span_dimension'],1360)
 def test_support_collision_is_not_invertible(self):
  s=v.s;t=2;M=s.Matrix([[t**p,p*t**(p-1) if p else 0,t**p] for p in range(3)])
  self.assertEqual(M.det(),0)
if __name__=='__main__':unittest.main()

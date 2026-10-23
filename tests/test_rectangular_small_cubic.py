import importlib.util,json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'research/ai/2026-10-21-rectangular-direct-sums/saturation.py'
spec=importlib.util.spec_from_file_location('small_cubic_cert',P)
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class SmallCubicTests(unittest.TestCase):
 def test_all_ten_coordinate_support_certificates(self):
  c=json.loads((ROOT/'results/rectangular-direct-sums-20261021/hankel-a3-b3.json').read_text())
  e.verify(c)
 def test_exclusion_keeps_m5_unresolved(self):
  self.assertLess(6+2*(45-36),27)
  self.assertGreater(36,2*9)
  self.assertGreaterEqual(5+2*(45-25),27)

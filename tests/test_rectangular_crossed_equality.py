import importlib.util
from pathlib import Path
import unittest
P=Path(__file__).resolve().parents[1]/'research/ai/2026-10-21-rectangular-direct-sums/equality_crossed_flattening.py'
spec=importlib.util.spec_from_file_location('crossed_equality',P)
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class CrossedEqualityTests(unittest.TestCase):
 def test_exact_equality_and_strict_controls(self):
  r=e.controls()
  self.assertEqual(r['rational_examples_checked'],96)
  self.assertEqual(r['quantitative_bound_checks'],96)
  self.assertGreater(r['equality_cases'],0)
  self.assertEqual(r['A89_equality_crossed_rank'],8)
  self.assertEqual(r['strict_inequality_control']['crossed_rank'],4)

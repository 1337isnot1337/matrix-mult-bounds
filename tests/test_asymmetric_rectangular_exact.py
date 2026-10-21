import importlib.util
from pathlib import Path
import unittest
P=Path(__file__).resolve().parents[1]/'research/ai/2026-10-21-asymmetric-sl2-seed/rectangular_exact.py'
spec=importlib.util.spec_from_file_location('rectangular_exact',P);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
class ExactRectangularTests(unittest.TestCase):
 def test_all_original_terms(self):
  result=module.verify()
  self.assertEqual(result['source_terms_checked'],729)
  self.assertEqual(result['target_coefficients_checked'],5625)
  self.assertFalse(result['improves_omega'])
 def test_all_maps_injective(self):
  import sympy as s
  self.assertEqual([s.Matrix(M).rank() for M in module.maps()],[25,15,15])

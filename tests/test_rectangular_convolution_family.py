import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'research/ai/2026-10-21-rectangular-direct-sums'
SPEC=importlib.util.spec_from_file_location('one_unit_convolution_controls',FOLDER/'one_unit_convolution_family.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class ConvolutionFamilyTests(unittest.TestCase):
 def test_full_family_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/one-unit-convolution-family.json').read_text()))
 def test_additional_small_seed(self):
  self.assertEqual(v.control(2,2,seed=4)['full_source_rank_over_Q'],9)
 def test_one_factor_dimensions(self):
  spec=importlib.util.spec_from_file_location('one_factor_families',FOLDER/'fixed_pencil_linear_families.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  self.assertEqual(m.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/fixed-pencil-linear-families.json').read_text()))
if __name__=='__main__':unittest.main()

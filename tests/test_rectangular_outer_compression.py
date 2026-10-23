import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('outer_compression',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/outer_compression.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class OuterCompressionTests(unittest.TestCase):
 def test_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/outer-compression.json').read_text()))
 def test_strict_gaps(self):
  for r in v.report()['outer_flattenings']:
   self.assertLess(r['image_dimension_bound'],r['input_dimension'])
 def test_realization_counterexample(self):
  r=v.report()['counterexample']
  self.assertEqual(r['source_partial_permutation_rank'],640)
  self.assertGreater(r['moment_hankel_rank'],r['crossed_rank'])
 def test_embedding_control(self):
  # A real injective zero-padding map must not be excluded by the bound.
  r=v.dimension_bound(3,4,7,6,2)
  self.assertGreaterEqual(r['image_dimension_bound'],r['input_dimension'])
if __name__=='__main__':unittest.main()

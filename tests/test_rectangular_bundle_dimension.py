import importlib.util
from pathlib import Path
import unittest
P=Path(__file__).resolve().parents[1]/'research/ai/2026-10-21-rectangular-direct-sums/bundle_hankel_dimension.py'
spec=importlib.util.spec_from_file_location('bundle_dim',P)
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class BundleDimensionTests(unittest.TestCase):
 def test_splitting_integer_bound_and_parameter_count(self):
  r=e.splitting_controls()
  self.assertGreater(r['splitting_types_checked'],1000)
  self.assertEqual(r['zero_extension_controls'],25)
 def test_cech_cup_product_matches_every_hankel_entry(self):
  self.assertGreater(e.cech_controls(),10000)
 def test_one_unit_excess_is_not_rounded(self):
  r=e.exclusion(8,10,[(32,33,33),(8,3,3)],[1080,1098,1080])
  self.assertIsNotNone(r)
  self.assertEqual(r['lift_upper'],641)
  self.assertEqual(r['crossed_rank_cap'],9)
  self.assertEqual(r['bundle_dimension_cap'],163)

 def test_one_block_column_recovers_a_valid_generic_matrix_bound(self):
  self.assertEqual(e.one_window_controls(),495)

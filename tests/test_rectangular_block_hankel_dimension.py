import importlib.util
from pathlib import Path
import unittest
P=Path(__file__).resolve().parents[1]/'research/ai/2026-10-21-rectangular-direct-sums/block_hankel_dimension.py'
spec=importlib.util.spec_from_file_location('block_hankel_dim',P)
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class BlockHankelDimensionTests(unittest.TestCase):
 def test_all_but_last_chart_can_fail(self):
  self.assertEqual(e.coherent_cover(),[7]*8+[8])
 def test_exceptional_component_is_not_discarded(self):
  r=e.exceptional_control()
  self.assertEqual(r['component_dimension'],136)
  self.assertEqual(r['row_prefix_ranks'],list(range(1,9)))
 def test_exclusion_and_scope_controls(self):
  self.assertIsNotNone(e.exclusion(8,9,[(30,30,30),(3,3,3)],[909]*3))
  self.assertIsNone(e.exclusion(8,10,[(32,33,33),(8,3,3)],[1080,1098,1080]))
  self.assertIsNotNone(e.exclusion(9,9,[(32,33,33),(4,2,2)],[1064,1093,1064]))

 def test_square_common_input_exception(self):
  r=e.square_input_control()
  self.assertEqual(r['chart_ranks'],[8]*10)
  self.assertEqual(r['common_input_component_dimension'],161)

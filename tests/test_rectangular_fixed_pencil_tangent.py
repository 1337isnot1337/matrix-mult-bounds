import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('fixed_pencil_tangent_controls',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/fixed_pencil_tangent.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class FixedPencilTangentTests(unittest.TestCase):
 def test_saved_rational_elimination(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/fixed-pencil-tangent.json').read_text()))
 def test_rank_control(self):
  cols=[{0:2,1:1},{0:4,1:2},{1:3}]
  self.assertEqual(v.rank_sparse(cols),2)
  self.assertEqual(v.rank_sparse(cols,65519),2)
if __name__=='__main__':unittest.main()

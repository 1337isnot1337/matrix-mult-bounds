import importlib.util
from pathlib import Path
import unittest
P=Path(__file__).resolve().parents[1]/'research/ai/2026-10-21-rectangular-direct-sums/equality_counterexample.py'
spec=importlib.util.spec_from_file_location('rectangular_equality_counterexample',P)
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class EqualityCounterexampleTests(unittest.TestCase):
 def test_exact_full_row_rank_counterexample(self):
  r=e.small_report()
  self.assertEqual(r['exact_rational_slice_rank'],12)
  self.assertEqual(r['common_quadratic_annihilator_matrix_rank'],3)

 def test_frontier_format_counterexample(self):
  r=e.family_report()
  self.assertEqual(r['exact_rational_slice_rank'],576)
  self.assertEqual(r['common_degree_a_annihilator_rank'],9)

"""Exact finite controls for a deliberately restricted spectral ansatz."""
import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('distinct_atom_controls',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/distinct_atoms.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class DistinctAtomTests(unittest.TestCase):
 def test_replay(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/distinct-atoms.json').read_text()))
 def test_sharp_gap_and_common_factor(self):
  a,b=2,4
  common=v.control(a,b,'common');changed=v.control(a,b,'one_extra')
  self.assertEqual(common['predicted_slice_rank'],a*a*b)
  self.assertEqual(changed['predicted_slice_rank'],a*a*b+b)
 def test_general_rank641_counterexample_not_removed(self):
  spec=importlib.util.spec_from_file_location('one_step_counterexample',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/equality_one_step.py')
  m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  self.assertEqual(m.certificate(8,10)['rank_mod_2'],641)
if __name__=='__main__':unittest.main()

import importlib.util
from pathlib import Path
import unittest
try:
 import numpy as np
except ImportError:np=None
ROOT=Path(__file__).resolve().parents[1]
@unittest.skipIf(np is None,'optional numerical discovery dependency')
class TargetGaugeTests(unittest.TestCase):
 def test_complex_gauge_balance(self):
  spec=importlib.util.spec_from_file_location('gauge_balance',ROOT/'research/ai/2026-10-21-asymmetric-sl2-seed/target_gauge_balance.py')
  v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
  rng=np.random.default_rng(314159)
  maps=[rng.normal(size=(3,7,d))+1j*rng.normal(size=(3,7,d)) for d in [6,12,8]]
  out,r=v.balance(maps,(2,3,4),sweeps=4)
  self.assertLess(r['target_invariance_relative_error'],1e-10)
  self.assertLessEqual(r['coefficient_norm_history'][-1],r['initial_coefficient_norm'])
  self.assertTrue(r['residual_norms_are_gauge_dependent'])
  self.assertFalse(r['exact_certificate'])
if __name__=='__main__':unittest.main()

import importlib.util
from pathlib import Path
import unittest
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('laurent_scale_balance_test',ROOT/'research/ai/2026-10-21-asymmetric-sl2-seed/laurent_scale_balance.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class LaurentScaleTests(unittest.TestCase):
 def test_gradient_and_gauge(self):
  rng=np.random.default_rng(314159);M=[rng.normal(size=(5,3,2))+1j*rng.normal(size=(5,3,2)) for _ in range(3)]
  D=[rng.normal(size=m.shape)+1j*rng.normal(size=m.shape) for m in M]
  c,g=v.scale_data(M);pred=sum(np.vdot(a,b).real for a,b in zip(g,D));h=1e-5
  actual=(np.log(v.scale_data([m+h*d for m,d in zip(M,D)])[0])-np.log(v.scale_data([m-h*d for m,d in zip(M,D)])[0]))/(2*h)
  self.assertAlmostEqual(pred,actual,places=8)
  B,r=v.balance(M);self.assertLessEqual(r['balanced_coefficient_norm'],r['initial_coefficient_norm'])
  weights=2.3**np.arange(2,-3,-1)
  C,_=v.balance([m*weights[:,None,None] for m in M])
  self.assertTrue(all(np.allclose(b,c,rtol=1e-12,atol=1e-12) for b,c in zip(B,C)))
 def test_constant_scalar_coefficient(self):
  rng=np.random.default_rng(2718);M=[rng.normal(size=(5,1,1))+1j*rng.normal(size=(5,1,1)) for _ in range(3)]
  B,_=v.balance(M)
  def product(A):return np.convolve(np.convolve(A[0].ravel(),A[1].ravel()),A[2].ravel())
  self.assertAlmostEqual(abs(product(M)[6]-product(B)[6]),0,places=10)
if __name__=='__main__':unittest.main()

"""Verify the sharp cyclic family and the necessary cyclicity restriction."""
import importlib.util
import json
from pathlib import Path
import unittest
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('cyclic_state_controls',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/cyclic_state_gap.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class CyclicStateTests(unittest.TestCase):
 def test_saved_certificates(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/cyclic-state-gap.json').read_text()))
 def test_jordan_realization_replays_every_source_coefficient(self):
  for a,b in [(2,3),(3,4),(8,10)]:
   n=a+1;A=s.zeros(n)
   for i in range(n-1):A[i,i+1]=1
   self.assertNotEqual(A**(n-1),s.zeros(n));self.assertEqual(A**n,s.zeros(n))
   power=s.eye(n)
   for k in range(a+b-1):
    for i in range(a):
     for ss in range(b):
      value=(power[0,0] if ss==0 else power[0,a] if ss==1 else 0) if i==0 else 0
      self.assertEqual(value,int((i,k,ss) in [(0,0,0),(0,a,1)]))
    power=power*A
 def test_rank_divisibility_distinguishes_counterexample(self):
  self.assertEqual(v.certificate(8,10)['rank_mod_2']%10,0)
  self.assertEqual(v.old.certificate(8,10)['rank_mod_2']%10,1)
if __name__=='__main__':unittest.main()

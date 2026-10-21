import gzip
import importlib.util
import json
from pathlib import Path
import unittest
try:
 import numpy as np
except ImportError:np=None
ROOT=Path(__file__).resolve().parents[1]
def load(name):
 spec=importlib.util.spec_from_file_location(name,ROOT/f'research/ai/2026-10-21-rectangular-direct-sums/{name}.py')
 v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v);return v
@unittest.skipIf(np is None,'NumPy verification dependency not installed')
class InvariantSliceTests(unittest.TestCase):
 def test_original_source_replay(self):
  v=load('invariant_slice_pairing')
  for a in (2,3,4):
   for l in range(2*a-1):self.assertTrue((v.pairing(a,l)==v.brute_pairing(a,l)).all())
 def test_large_certificate(self):
  v=load('invariant_slice_pairing');r=v.certificate(24)
  self.assertEqual(r,json.loads(gzip.decompress((ROOT/'results/rectangular-direct-sums-20261021/invariant-slice-a24.json.gz').read_bytes())))
  self.assertEqual(r['full_source_rank_lower_bound'],27072)
class InvariantVertexTests(unittest.TestCase):
 def test_complete_graph(self):
  v=load('invariant_vertex_screen');r=v.report()
  self.assertEqual(r,json.loads((ROOT/'results/rectangular-direct-sums-20261021/invariant-slice-a24-target.json').read_text()))
  self.assertFalse(r['survivors']);self.assertTrue(r['does_not_exclude_general_singular_degenerations'])
if __name__=='__main__':unittest.main()

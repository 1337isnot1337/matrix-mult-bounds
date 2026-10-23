import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('large_equivariant',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/equivariant_large_targets.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class LargeEquivariantTests(unittest.TestCase):
 def test_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/equivariant-large-targets.json').read_text()))
 def test_small_source_normalization(self):
  self.assertEqual(dict(v.source_multiplicities(3,3)),{0:1,1:2,2:3,3:2,4:1})
 def test_partition_exhaustion(self):
  for d in (35,37,38):
   P=list(v.odd_partitions(d));self.assertEqual(len(P),len(set(P)))
   self.assertTrue(all(sum(p)==d and all(x%2 for x in p) for p in P))
if __name__=='__main__':unittest.main()

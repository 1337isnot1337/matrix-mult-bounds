import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('physical_subset_frontier',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/physical_subset_frontier.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class PhysicalSubsetTests(unittest.TestCase):
 def test_complete_replay(self):
  F=ROOT/'results/rectangular-direct-sums-20261021';raw=gzip.decompress((F/'physical-subset-frontier.json.gz').read_bytes());summary=json.loads((F/'physical-subset-frontier-summary.json').read_text())
  r=v.report();self.assertEqual(r,json.loads(raw));self.assertEqual(hashlib.sha256(raw).hexdigest(),summary['full_result_uncompressed_sha256'])
  keys=['a','target','source_leg','restricted_vertex_count','counts','rejections']
  digest=hashlib.sha256(json.dumps([{k:a[k] for k in keys} for a in r['sources']],sort_keys=True,separators=(',',':')).encode()).hexdigest()
  self.assertEqual(digest,summary['independent_graph_comparison_sha256'])
  self.assertEqual(r['remaining_count'],0);self.assertEqual(r['capacity_triangle_count'],4070)
 def test_source_multiplicities(self):
  for a in range(24,37):
   self.assertEqual(dict(v.target.eq.v.source_multiplicities(a,a)),{l:min(l+1,2*a-1-l) for l in range(2*a-1)})
if __name__=='__main__':unittest.main()

import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('frontier2000',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/single_frontier.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
F=ROOT/'results/rectangular-direct-sums-20261021'
class Frontier2000Tests(unittest.TestCase):
 def test_complete_scan(self):
  raw=gzip.decompress((F/'single-frontier-2000.json.gz').read_bytes())
  summary=json.loads((F/'single-frontier-2000-summary.json').read_text())
  self.assertEqual(hashlib.sha256(raw).hexdigest(),summary['scan_uncompressed_sha256'])
  self.assertEqual(v.report(2000),json.loads(raw))
  self.assertEqual(summary['remaining_after_written_critical_state_proof'],74)
 def test_all_cap_certificates(self):
  reports=v.verify_caps(2000)
  self.assertEqual(sum(x['coordinate_spaces_certified'] for x in reports),427076)
if __name__=='__main__':unittest.main()

"""Controls for the staged extended necessary-condition screen."""
import importlib.util
from pathlib import Path
import unittest
P=Path(__file__).resolve().parents[1]/'research/ai/2026-10-21-rectangular-direct-sums/extended_search.py'
spec=importlib.util.spec_from_file_location('rectangular_extended',P)
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)

class ExtendedTests(unittest.TestCase):
 def test_boundary_closes_a7b10(self):
  row={'shapes':[(30,30,30),(4,4,5)],'leg_dimensions':[916,920,920]}
  excluded,remaining,counts=e.refine(7,10,[row])
  self.assertEqual(remaining,[])
  self.assertEqual(sum(counts.values()),1)
  self.assertEqual(len(excluded),1)
 def test_equality_now_excluded_by_crossed_dimension(self):
  row={'shapes':[(30,30,30),(3,3,3)],'leg_dimensions':[909]*3}
  excluded,remaining,counts=e.refine(8,9,[row])
  self.assertEqual(len(excluded),1)
  self.assertEqual(remaining,[])
  self.assertEqual(counts['crossed_dimension'],1)
 def test_digest_is_key_order_independent(self):
  self.assertEqual(e.digest([{'a':1,'b':2}]),e.digest([{'b':2,'a':1}]))


class ExtendedReportTests(unittest.TestCase):
 def test_complete_format_coverage_and_retained_samples(self):
  import json
  root=P.parents[3]
  rows=json.loads((root/'results/rectangular-direct-sums-20261021/extended-frontier.json').read_text())
  expected={(a,b) for a in range(2,40) for b in range(a,100)
            if 960<a*b*(a+b-1)<=1500}
  self.assertEqual({(r['a'],r['b']) for r in rows},expected)
  self.assertEqual(len(rows),len(expected))
  for row in rows:
   self.assertEqual(sum(row['excluded_counts'].values())+row['remaining_count'],row['initial_counts']['survivors'])
   excluded,remaining,counts=e.refine(row['a'],row['b'],row['remaining_first_20'])
   self.assertEqual(excluded,[])
   self.assertEqual(len(remaining),min(20,row['remaining_count']))
 def test_replay_all_extended_hankel_certificates(self):
  import json
  root=P.parents[3]
  for a,b in [(7,10),(8,9),(8,10),(9,9)]:
   cert=json.loads((root/f'results/rectangular-direct-sums-20261021/hankel-a{a}-b{b}.json').read_text())
   e.sat.verify(cert)

if __name__=='__main__':unittest.main()

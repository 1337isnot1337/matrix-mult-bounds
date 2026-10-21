import importlib.util
from pathlib import Path
import unittest
P=Path(__file__).resolve().parents[1]/'research/ai/2026-10-21-rectangular-direct-sums/equality_one_step.py'
spec=importlib.util.spec_from_file_location('one_step',P)
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class OneStepTests(unittest.TestCase):
 def test_modular_lower_and_support_upper_match(self):
  for a,b in [(2,2),(2,3),(3,4),(8,9),(8,10),(9,9)]:
   r=e.certificate(a,b)
   self.assertEqual(r['rank_mod_2'],r['baseline']+1)
   self.assertEqual(r['support_cover_size'],r['rank_mod_2'])

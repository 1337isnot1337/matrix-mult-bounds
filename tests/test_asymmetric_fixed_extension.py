import importlib.util,json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'research/ai/2026-10-21-asymmetric-sl2-seed/fixed_extension.py';spec=importlib.util.spec_from_file_location('fixed_extension',P);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class FixedExtensionTests(unittest.TestCase):
 def test_exact_full_rank_witnesses(self):
  actual=e.verify();self.assertEqual(actual,json.loads((ROOT/'results/asymmetric-sl2-seed-20261021/fixed-extension-certificate.json').read_text()))
  for side in 'BC':self.assertEqual(actual[side]['rank'],45)

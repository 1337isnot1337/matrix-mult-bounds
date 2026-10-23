import importlib.util,json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'research/ai/2026-10-21-asymmetric-sl2-seed/pencil_obstruction.py'
spec=importlib.util.spec_from_file_location('asymmetric_pencil',P)
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class AsymmetricPencilTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.actual=e.report()
 def test_every_source_term_and_exact_pencil(self):
  self.assertEqual(self.actual['source_terms_checked'],729)
  self.assertEqual(self.actual['source']['polynomial_invariant'],'0')
  self.assertEqual(self.actual['target']['polynomial_invariant'],'137425/8')
 def test_saved_certificate_matches_reconstruction(self):
  saved=json.loads((ROOT/'results/asymmetric-sl2-seed-20261021/pencil-certificate.json').read_text())
  self.assertEqual(saved,self.actual)

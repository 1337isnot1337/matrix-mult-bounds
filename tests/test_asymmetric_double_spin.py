import json,subprocess,sys
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class DoubleSpinTests(unittest.TestCase):
 def test_saved_exact_pencil(self):
  actual=json.loads(subprocess.check_output([sys.executable,str(ROOT/'research/ai/2026-10-21-asymmetric-sl2-seed/double_spin_pencil.py')],text=True))
  self.assertEqual(actual,json.loads((ROOT/'results/asymmetric-sl2-seed-20261021/double-spin-pencil.json').read_text()))
  self.assertEqual(actual['source']['polynomial_invariant'],'0')
  self.assertEqual(actual['target']['polynomial_invariant'],'-50')

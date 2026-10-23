import importlib.util
import json
from pathlib import Path
import unittest
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('convolution_span_controls',ROOT/'research/ai/2026-10-21-rectangular-direct-sums/convolution_family_span.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
class ConvolutionSpanTests(unittest.TestCase):
 def test_exact_span_report(self):
  self.assertEqual(v.report(),json.loads((ROOT/'results/rectangular-direct-sums-20261021/convolution-family-span.json').read_text()))
 def test_high_multiplicity_pencils(self):
  x=s.Symbol('x')
  def has_root(f):
   f=s.Poly(f,x)
   return 16-f.degree()>=9 or s.gcd_list([f.as_expr()]+[s.diff(f.as_expr(),x,j) for j in range(1,9)]).as_poly(x).degree()>0
  for t in (1,2,3):
   self.assertFalse(has_root(x**9+t*(x-1)**9))
   self.assertTrue(has_root(x**9*(1+x**7)+t*x**9*(2+x**6)))
if __name__=='__main__':unittest.main()

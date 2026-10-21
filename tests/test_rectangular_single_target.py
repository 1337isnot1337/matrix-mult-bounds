import importlib.util
from pathlib import Path
import unittest
P=Path(__file__).resolve().parents[1]/'research/ai/2026-10-21-rectangular-direct-sums/extended_search.py'
spec=importlib.util.spec_from_file_location('single_target_screen',P)
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
class SingleTargetTests(unittest.TestCase):
 def test_only_conditional_arithmetic(self):
  self.assertLess(49**3000,180**2249)
 def test_m30_survives_necessary_tests(self):
  row={'shapes':[(30,30,30)],'leg_dimensions':[900]*3}
  self.assertIsNone(e.screen.rejection(8,9,row['shapes']))
  self.assertEqual(e.refine(8,9,[row])[1],[row])
 def test_integer_width_inequality(self):
  for a in range(2,8):
   for b in range(a,9):
    m=a+b-1
    for x in range(m):
     for y in range(m):
      for z in range(m):
       if x+y<=a-1 and y+z<=b-1 and x+z<=m-1:
        self.assertLessEqual(x+y+z,m-1)

 def test_unique_single_square_candidate_in_this_source(self):
  retained=[]
  for n in range(1,34):
   if e.screen.score_interval(n**3)[1]<=49**3*e.screen.SCALE:continue
   row={'shapes':[(n,n,n)],'leg_dimensions':[n*n]*3}
   if e.screen.rejection(8,9,row['shapes']) is not None:continue
   if e.refine(8,9,[row])[1]:retained.append(n)
  self.assertEqual(retained,[30])

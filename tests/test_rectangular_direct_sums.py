"""Independent finite and arithmetic checks for the two-block screen."""
import importlib.util
from itertools import permutations
from pathlib import Path
import unittest

P=Path(__file__).resolve().parents[1]/'research/ai/2026-10-21-rectangular-direct-sums/screen.py'
spec=importlib.util.spec_from_file_location('rectangular_direct_sums',P)
s=importlib.util.module_from_spec(spec)
spec.loader.exec_module(s)

class RectangularDirectSums(unittest.TestCase):
    def test_integer_enclosures(self):
        for v in range(1,400):
            low,high=s.score_interval(v,100)
            rad=(216*v)**3*100**4
            self.assertLessEqual(low**4,rad)
            self.assertGreaterEqual(high**4,rad)
            self.assertIn(high-low,[0,1])

    def test_known_constructed_controls(self):
        for a,b,blocks in [(2,2,[(2,2,2)]),(2,3,[(4,4,4)]),
                           (5,5,[(8,8,8),(3,3,3)])]:
            self.assertIsNone(s.rejection(a,b,blocks))

    def test_published_frontier_controls(self):
        self.assertIsNone(s.rejection(8,8,[(27,27,27),(7,7,7)]))
        self.assertIsNotNone(s.rejection(7,8,[(25,25,25),(5,5,5)]))
        self.assertIsNotNone(s.rejection(4,4,[(10,10,11),(1,1,1)]))

    def test_conditional_rational_gate(self):
        self.assertGreater(4408992**4499,95972**6000)
        self.assertGreater(15552**4499,1390**6000)
        self.assertGreater(95972+1390,46**3)
        self.assertIsNone(s.rejection(7,9,[(27,27,28),(6,6,2)]))

    def test_leg_and_block_symmetry(self):
        for first in [(1,2,3),(2,3,4),(3,4,5),(4,4,4)]:
            second=(1,2,2)
            base=s.rejection(3,4,[first,second]) is None
            for perm in permutations(range(3)):
                fs=tuple(first[i] for i in perm)
                ss=tuple(second[i] for i in perm)
                self.assertEqual(base,s.rejection(3,4,[fs,ss]) is None)
                self.assertEqual(base,s.rejection(3,4,[ss,fs]) is None)

    def test_score_pruning_against_naive(self):
        for a,b in [(2,2),(2,3),(3,3)]:
            N=a*b*(a+b-1)
            threshold=(3*(a+b)-2)**3*s.SCALE
            score_count=dim_count=survive=0
            shapes=s.sorted_shapes(N)
            for one in shapes:
                for two in shapes:
                    if s.volume(two)>s.volume(one):
                        continue
                    if sum(s.score_interval(s.volume(x))[1] for x in [one,two])<=threshold:
                        continue
                    for oriented in set(permutations(two)):
                        score_count+=1
                        reason=s.rejection(a,b,[one,oriented])
                        dim_count+=reason!='dimension'
                        survive+=reason is None
            actual=s.screen_source(a,b)['counts']
            self.assertEqual(actual['score_eligible_pairs'],dim_count)
            self.assertEqual(actual['survivors'],survive)

if __name__=='__main__': unittest.main()

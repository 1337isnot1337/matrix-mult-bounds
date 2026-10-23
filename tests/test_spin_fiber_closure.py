"""Full source and tamper controls for the weighted spin closure obstruction."""
from collections import Counter
import copy
import importlib.util
from itertools import product
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('fiber_closure',
 ROOT/'research/ai/2026-10-20-anisotropic-constructions/spin_fiber_closure.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)


class SpinFiberClosureTests(unittest.TestCase):
    def test_saved_output_identity_and_induction_controls(self):
        report=c.verify()
        self.assertEqual([q['power'] for q in report['finite_induction_controls']],[2,3,4,5])
        self.assertTrue(report['laurent_limiting_degenerations_excluded'])
        self.assertFalse(report['arbitrary_source_maps_excluded'])

    def test_independent_all_source_terms_at_two_bits(self):
        for point,expected in zip(c.POINTS2,c.POLYS2):
            maps=[]
            for leg,row in enumerate(point):
                I,J=divmod(row,9);image={}
                for first,last,m0,m1 in product(range(4),range(4),range(3),range(3)):
                    a=(first%2*3+m0)*2+last%2;b=(first//2*3+m1)*2+last//2
                    value=c.v.LOCAL[I%3*3+J%3][a]*c.v.LOCAL[I//3*3+J//3][b]
                    if value:
                        variable=leg*144+((first*3+m0)*3+m1)*4+last+1
                        image.setdefault((first,m0+2*m1,last),[]).append((variable,value))
                maps.append(image)
            polynomial=Counter()
            for i,j,p,q,r,s in product(range(4),repeat=6):
                for (x,a),(y,b),(z,d) in product(maps[0].get((i,p+q,s),()),
                     maps[1].get((p,r+s,j),()),maps[2].get((r,i+j,q),())):
                    polynomial[x,y,z]+=a*b*d
            self.assertEqual({m:n for m,n in polynomial.items() if n},expected)

    def test_tampered_linear_relation_is_rejected(self):
        altered=copy.deepcopy(c.report())
        altered['finite_induction_controls'][0]['equations'][1]['output_polynomial'][0]['coefficient']+=1
        with self.assertRaises(ArithmeticError):c.verify(altered)


if __name__=='__main__':unittest.main()

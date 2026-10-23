"""Separate complete-source checks for the weighted ordinary spin certificate."""
from collections import Counter
import copy
import importlib.util
from itertools import product
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('spin_fiber_compression',
 ROOT/'research/ai/2026-10-20-anisotropic-constructions/spin_fiber_compression.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


class SpinFiberCompressionTests(unittest.TestCase):
    def test_saved_certificate_and_integer_identity(self):
        report=v.verify()
        self.assertEqual(len(report['finite_induction_controls']),3)
        self.assertEqual(len(report['normalized_bezout_identity_for_one']),5)
        self.assertTrue(report['ordinary_family_excluded'])
        self.assertFalse(report['laurent_limits_addressed_by_this_certificate'])

    def test_independent_complete_two_bit_source(self):
        for point,expected in zip(v.POINTS,v.BASE):
            maps=[]
            for leg,row in enumerate(point):
                I,J=divmod(row,9);image={}
                for first,last,m0,m1 in product(range(4),range(4),range(3),range(3)):
                    col0=(first%2*3+m0)*2+last%2
                    col1=(first//2*3+m1)*2+last//2
                    value=v.LOCAL[(I%3)*3+J%3][col0]*v.LOCAL[(I//3)*3+J//3][col1]
                    if value:
                        variable=leg*144+((first*3+m0)*3+m1)*4+last+1
                        image.setdefault((first,m0+2*m1,last),[]).append((variable,value))
                maps.append(image)
            polynomial=Counter();visited=0
            for i,j,p,q,r,s in product(range(4),repeat=6):
                visited+=1
                terms=(maps[0].get((i,p+q,s),()),maps[1].get((p,r+s,j),()),maps[2].get((r,i+j,q),()))
                for (x,a),(y,b),(z,c) in product(*terms):polynomial[x,y,z]+=a*b*c
            wanted=int(point[0]%9==point[1]//9 and point[1]%9==point[2]//9 and point[2]%9==point[0]//9)
            polynomial[()]-=64*wanted
            self.assertEqual(visited,4096)
            self.assertEqual({m:c for m,c in polynomial.items() if c},expected)

    def test_modified_saved_coefficient_rejected(self):
        broken=copy.deepcopy(v.report())
        broken['finite_induction_controls'][0]['equations'][0]['residual'][0]['coefficient']+=1
        with self.assertRaises(ArithmeticError):v.verify(broken)


if __name__=='__main__':unittest.main()

"""Reconstruct common tangents from literal seed matrices and their kernels."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-23-hankel-index-sharpness'
RESULTS=ROOT/'results/hankel-index-sharpness-2026-10-23'
spec=importlib.util.spec_from_file_location('hankel_extensions',PACKAGE/'extensions.py')
extensions=importlib.util.module_from_spec(spec); spec.loader.exec_module(extensions)


def exact_rank(matrix):
    return DomainMatrix.from_Matrix(matrix).convert_to(sp.QQ).rank()


def common_tangent_from_points(epsilon,p,q):
    s=p+q; r=epsilon*s; a=r+p; b=r+q; rows=[]
    # Obtain kernels by ordinary elimination, without the proposed P.
    for t in range(2*epsilon+1):
        H=sp.Matrix(a,b,lambda i,j:int(i+j==r-1)+t*int(i+j==r+s-1))
        left=H.T.nullspace(); right=H.nullspace()
        for x in left:
            for y in right:
                row=[sp.Integer(0)]*(a+b-1)
                for i in range(a):
                    for j in range(b):row[i+j]+=x[i]*y[j]
                rows.append(row)
    return sp.Matrix(rows)


class HankelPencilExtensionTests(unittest.TestCase):
    def test_saved_extension_certificates(self):
        report=extensions.report()
        self.assertEqual(report,json.loads((RESULTS/'extensions.json').read_text()))
        self.assertEqual(report['families_checked'],36)
        self.assertFalse(report['arbitrary_quadratic_pencils_classified'])
        self.assertFalse(report['independent_review'])
        self.assertFalse(report['improves_omega'])

    def test_common_tangents_from_independent_pointwise_kernels(self):
        for epsilon,p,q in [(1,2,1),(2,2,2),(2,1,3),(3,1,1)]:
            with self.subTest(epsilon=epsilon,p=p,q=q):
                operator=common_tangent_from_points(epsilon,p,q)
                support=[j*(p+q)-1 for j in range(1,2*epsilon+1)]
                self.assertEqual(operator.cols-exact_rank(operator),2*epsilon)
                self.assertEqual([j for j in range(operator.cols) if not any(operator[:,j])],support)

    def test_entire_a10_four_space_rank_strata(self):
        ranks=set()
        for moments in itertools.product([-1,0,1],repeat=4):
            A,B,C,D=moments
            K=sp.Matrix([[A,B],[B,C],[C,D]])
            h=[0]*19
            for i,value in zip([3,7,11,15],moments):h[i]=value
            H=sp.Matrix(10,10,lambda i,j:h[i+j])
            rank=exact_rank(H); ranks.add(rank)
            self.assertEqual(rank,4*exact_rank(K))
            self.assertEqual(rank<8,all(K.extract(rows,[0,1]).det()==0
                                       for rows in itertools.combinations(range(3),2)))
        self.assertEqual(ranks,{0,4,8})

    def test_quadratic_annihilator_on_the_full_four_space(self):
        A,B,C,D=sp.symbols('A B C D')
        coefficients=sp.Matrix([B*D-C*C,B*C-A*D,A*C-B*B])
        self.assertEqual((sp.Matrix([[A,B,C],[B,C,D]])*coefficients).applyfunc(sp.expand),sp.zeros(2,1))
        for values in [(0,1,2,0),(1,2,3,5),(1,2,4,8)]:
            substitution=dict(zip([A,B,C,D],values))
            h=[0]*19
            for i,value in zip([3,7,11,15],values):h[i]=value
            H=sp.Matrix(10,10,lambda i,j:h[i+j])
            P=[0]*9
            for i,value in zip([0,4,8],coefficients):P[i]=value.subs(substitution)
            for shift in [0,1]:
                vector=sp.Matrix([P[i-shift] if shift<=i<=shift+8 else 0 for i in range(10)])
                self.assertEqual(H*vector,sp.zeros(10,1))


if __name__=='__main__':
    unittest.main()

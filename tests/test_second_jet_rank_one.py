"""Independent coefficient and matrix-space checks for the second-jet bridge."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-second-jet-rank-one'
RESULTS=ROOT/'results/second-jet-rank-one-2026-10-21'
spec=importlib.util.spec_from_file_location('second_jet_verifier',PACKAGE/'verify.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


def coefficient(a,b,c):
    i,s,za=a//28,a//7%4,a%7
    p,j,zb=b//28,b//7%4,b%7
    r,q,zc=c//28,c//7%4,c%7
    return int(za==6-p-q and zb==6-r-s and zc==6-i-j)


def combine(vectors,weights):
    result={}
    for vector,weight in zip(vectors,weights):
        for i,value in vector.items():result[i]=result.get(i,0)+weight*value
    return {i:value for i,value in result.items() if value}


class SecondJetRankOneTests(unittest.TestCase):
    def test_frozen_integer_and_number_field_certificates(self):
        actual=v.report()
        self.assertEqual(actual,json.loads((RESULTS/'certificates.json').read_text()))
        self.assertEqual(actual['leading_tensor']['rank'],12)
        self.assertEqual(actual['canonical_bilinear_tensor']['rank'],25)
        self.assertEqual(actual['necessary_bilinear_first_rank_upper_bound'],0)
        self.assertEqual(actual['necessary_second_partial_space_dimension_upper_bound'],12)
        self.assertEqual(actual['rank_two_spanning']['span']['rank'],25)
        self.assertEqual(len(actual['rank_two_spanning']['slices']),26)
        self.assertEqual(actual['necessary_effective_first_row_rank_sum_upper_bound'],24)

    def test_every_H_coefficient_from_independent_fixed_index_formula(self):
        H=v.tensor()
        for ai,a in enumerate(v.K):
            for b,br in enumerate(v.EB):
                for c,cr in enumerate(v.EC):
                    expected=sum(x*y*coefficient(a,bj,cj) for bj,x in br.items() for cj,y in cr.items())
                    self.assertEqual(H[ai,b*20+c],expected,(a,b,c))

    def test_cross_factorization_is_symbolic_and_first_slices_have_even_rank(self):
        L_ids,_,base=v.block_form();H=v.tensor();rr=[v.K.index(a) for a in L_ids]
        columns=[0,1,2,3,4,5,6,7,12,13,14,15]
        minor=base[:,columns];inverse=minor.inv()
        parameters=sp.symbols('v0:4')
        actual=sum((parameters[i]*H.extract(rr,[b*20+16+i for b in columns]) for i in range(4)),sp.zeros(12))
        X=sp.Matrix([[parameters[3],parameters[1]],[parameters[2],parameters[0]]])
        self.assertEqual(actual,sp.kronecker_product(X,sp.eye(6))*minor)
        # The first-slice normal form is two identical 6-by-2 blocks.
        x=sp.symbols('x0:12');operators=[]
        for i in range(4):operators.append(H.extract(rr,[b*20+16+i for b in columns])*inverse)
        first=sp.Matrix.hstack(*(O.T*sp.Matrix(x) for O in operators))
        U=sp.Matrix(6,2,lambda i,j:x[6+i] if j==0 else x[i])
        self.assertEqual(first[:,[2,3,0,1]],sp.diag(U,U))

    def test_common_column_and_common_row_mixed_spaces_are_different(self):
        # X(e0),X(e2) have the same image; X(e0),X(e1) have different images.
        for chosen,expected in [([0,2],6),([0,1],12)]:
            matrix=v.contract(v.EB[:16],[v.EC[16+i] for i in chosen],v.K)
            self.assertEqual(v.rational_rank(matrix),expected)
        # Any standard mixed vector on each side already gives first rank >=12.
        for b,c in itertools.product(range(4),repeat=2):
            matrix=v.contract(v.EB[:16]+[v.EB[16+b]],v.EC[:16]+[v.EC[16+c]],v.K)
            self.assertGreaterEqual(v.rational_rank(matrix),12)

    def test_low_rank_spanning_slices_have_complete_rational_factorizations(self):
        saved=json.loads((RESULTS/'certificates.json').read_text())
        H=v.tensor()
        for witness in saved['rank_two_spanning']['slices']:
            coefficients=dict(witness['source_first_coefficients'])
            row=sum((value*H[v.K.index(i),:] for i,value in coefficients.items()),sp.zeros(1,400))
            matrix=sp.Matrix(20,20,lambda b,c:row[0,b*20+c])
            rr=witness['matrix_rank']['minor_rows'];cc=witness['matrix_rank']['minor_columns']
            core=matrix.extract(rr,cc)
            self.assertNotEqual(core.det(),0)
            self.assertEqual(matrix,matrix[:,cc]*core.inv()*matrix[rr,:])


if __name__=='__main__':unittest.main()

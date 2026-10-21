"""Independent complete coefficient replay for corrected second-jet witnesses."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-corrected-prolongation'
RESULTS=ROOT/'results/corrected-prolongation-2026-10-21'
spec=importlib.util.spec_from_file_location('corrected_prolongation',PACKAGE/'verify.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


def coefficient(a,b,c):
    i,s,za=a//28,a//7%4,a%7
    p,j,zb=b//28,b//7%4,b%7
    r,q,zc=c//28,c//7%4,c%7
    return int(za==6-p-q and zb==6-r-s and zc==6-i-j)


def decode_maps(data):
    return [[{j:sp.Rational(n,q) for i,j,n,q in level if i==row} for row in range(20)]
            for level in data]


def decode_matrix(data):
    return sp.MutableSparseMatrix(*data['shape'],{(i,j):sp.Rational(n,q) for i,j,n,q in data['entries']})


@lru_cache(None)
def independent_seed(name):
    report=json.loads((RESULTS/(name+'.json')).read_text());P=decode_maps(report['P']);Q=decode_maps(report['Q'])
    matrices=[]
    for degree in range(3):
        entries={}
        for a in range(112):
            for b in range(20):
                for c in range(20):
                    value=sum(x*y*coefficient(a,j,k) for i in range(degree+1)
                              for j,x in P[i][b].items() for k,y in Q[degree-i][c].items())
                    if value:entries[a,20*b+c]=value
        matrices.append(sp.MutableSparseMatrix(112,400,entries))
    return report,matrices


class CorrectedProlongationTests(unittest.TestCase):
    def test_every_saved_rational_and_polynomial_report_replays(self):
        actual=v.reports()
        for name,report in actual.items():self.assertEqual(report,json.loads((RESULTS/(name+'.json')).read_text()))
        self.assertEqual(actual['linear']['prolonged_parameters'],172)
        self.assertEqual(actual['linear']['prolongation_lower_certificate']['rank_lower_bound'],360)
        self.assertEqual(actual['linear']['leading_boundary_departure_rank'],28)
        self.assertEqual(actual['quadratic']['nonzero_equations'],0)
        self.assertEqual(actual['quadratic']['distinct_monomials'],0)

    def test_all_full_seed_coefficients_from_independent_fixed_indices(self):
        for name in ['seed','mixed_seed']:
            report,(S0,S1,S2)=independent_seed(name)
            A0=report['source_first_leading_indices'];K=report['source_first_kernel_indices']
            self.assertEqual(A0,[i for i in range(112) if i//28 in [1,2] and i//7%4 in [1,2] and i%7 in [0,3,6]])
            self.assertEqual(K,[i for i in range(112) if i not in A0])
            Y=decode_matrix(report['first_correction']);Z=decode_matrix(report['second_correction'])
            F0=S0.extract(A0,list(range(400)))
            self.assertEqual(S1.extract(K,list(range(400))),Y*F0)
            self.assertEqual(S2.extract(K,list(range(400)))-Y*S1.extract(A0,list(range(400))),Z*F0)
            for maps in [report['P'],report['Q']]:
                self.assertTrue(all(0<=row<20 for level in maps for row,old,n,q in level))
            self.assertEqual(report['output_dimension'],110)

    def test_first_row_correction_is_essential(self):
        report,(S0,S1,S2)=independent_seed('seed')
        K=report['source_first_kernel_indices']
        self.assertNotEqual(S1.extract(K,list(range(400))),sp.zeros(100,400))
        self.assertTrue(report['first_correction']['entries'])

    def test_mixed_witness_exercises_second_correction(self):
        report,_=independent_seed('mixed_seed')
        self.assertTrue(report['second_correction']['entries'])
        self.assertGreater(sum(row<4 for side in ['P','Q'] for row,old,n,q in report[side][2]),0)


if __name__=='__main__':unittest.main()

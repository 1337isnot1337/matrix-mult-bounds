"""Independent source and certificate replays for the boundary normal lemma."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-third-boundary-trap'
RESULTS=ROOT/'results/third-boundary-trap-2026-10-21'
spec=importlib.util.spec_from_file_location('third_boundary_verifier',PACKAGE/'verify.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


def decode(data):
    return sp.MutableSparseMatrix(*data['shape'],{(i,j):sp.Rational(n,q) for i,j,n,q in data['entries']})


def covectors(data):
    M=decode(data)
    return [{j:value for (i,j),value in M.todok().items() if i==row} for row in range(M.rows)]


def index(i,j,z):return (4*i+j)*7+z


def coefficient(a,b,c):
    i,s,za=a//28,a//7%4,a%7
    p,j,zb=b//28,b//7%4,b%7
    r,q,zc=c//28,c//7%4,c%7
    return int(za==6-p-q and zb==6-r-s and zc==6-i-j)


def contract(a,B,C):
    return sum(x*y*coefficient(a,b,c) for b,x in B.items() for c,y in C.items())


def check_minors(C,records):
    forms=[]
    for record in records:
        form=sp.zeros(1,24)
        for j,value in record['linear_form']:form[0,j]=value
        scales=[];positions=record['positions']
        for k,(row,col) in enumerate(positions):
            diagonal=C[row*256+col,:]
            chosen=next(j for j in range(24) if form[0,j])
            scale=diagonal[0,chosen]/form[0,chosen]
            assert scale and diagonal==scale*form
            scales.append(scale)
            for _,future in positions[k+1:]:assert C[row*256+future,:]==sp.zeros(1,24)
        assert sp.prod(scales)==sp.Rational(*record['determinant_constant'])
        forms.append(form)
    assert sp.Matrix.vstack(*forms).rank()==24


class ThirdBoundaryTrapTests(unittest.TestCase):
    def test_saved_reports_replay(self):
        for name,report in v.reports().items():
            self.assertEqual(report,json.loads((RESULTS/(name+'.json')).read_text()))
        report=v.reports()['normal']
        self.assertEqual(report['boundary_prolonged_parameters'],28)
        self.assertEqual(report['remaining_normal_parameters'],4)
        self.assertEqual(v.reports()['minimum']['minimum_nonzero_first_rank'],8)

    def test_complete_control_from_independent_source_indices(self):
        report=json.loads((RESULTS/'normal.json').read_text());control=report['coefficient_control']
        P=covectors(control['leading_B']);Q=covectors(control['leading_C'])
        BP=covectors(control['B_corrections']);CP=covectors(control['C_corrections'])
        Y=decode(control['source_correction']);K=control['K_inf_indices'];A0=control['A0_indices']
        G=[{index(0,3,z):1,index(3,0,z):-1} for z in [1,2,4,5]]
        DB=[{index(p,j,z):1} for p,j,z in itertools.product((0,3),(0,3),(1,2,4,5))]
        DC=[{index(k//7%4,k//28,k%7):value for k,value in row.items()} for row in DB]
        F=[[[contract(a,G[b],G[c]) for c in range(4)] for b in range(4)] for a in A0]
        needs_correction=False
        for x,a in enumerate(K):
            for b,c in itertools.product(range(4),repeat=2):
                actual=contract(a,P[b],G[c])+contract(a,G[b],Q[c])
                expected=sum(Y[x,k]*F[k][b][c] for k in range(12))
                self.assertEqual(actual,expected)
            for b,c in itertools.product(range(16),range(4)):
                raw=contract(a,BP[b],G[c])+contract(a,DB[b],Q[c])
                correction=sum(Y[x,k]*contract(old,DB[b],G[c]) for k,old in enumerate(A0))
                self.assertEqual(raw,correction)
                needs_correction |= bool(raw)
                raw=contract(a,G[c],CP[b])+contract(a,P[c],DC[b])
                correction=sum(Y[x,k]*contract(old,G[c],DC[b]) for k,old in enumerate(A0))
                self.assertEqual(raw,correction)
        self.assertTrue(needs_correction)
        block=json.loads((RESULTS/'block.json').read_text());E=decode(block)
        for x,a in enumerate(block['source_first_indices']):
            y=K.index(a)
            for b,c in itertools.product(range(16),repeat=2):
                actual=contract(a,BP[b],DC[c])+contract(a,DB[b],CP[c])
                actual-=sum(Y[y,k]*contract(old,DB[b],DC[c]) for k,old in enumerate(A0))
                self.assertEqual(actual,E[x*256+16*b+c,control['parameter']])

    def test_fixed_radicals_and_common_plane_kernel(self):
        normal=json.loads((RESULTS/'normal.json').read_text());E=decode(json.loads((RESULTS/'block.json').read_text()))
        kernel=decode(normal['plane_kernel']);basis=decode(normal['normal_basis']);plane=decode(normal['plane_directions'])
        self.assertEqual(E*kernel,sp.zeros(4096,4))
        self.assertEqual((basis*kernel).row_join(plane).rank(),4)
        for a,b,c in itertools.product(range(16),range(4),range(16)):
            self.assertEqual(E[(a*16+4+b)*16+c,:],E[(a*16+8+b)*16+c,:])
            self.assertEqual(E[(a*16+c)*16+4+b,:],E[(a*16+c)*16+8+b,:])

    def test_eighth_power_minors_without_rerunning_the_search(self):
        E=decode(json.loads((RESULTS/'block.json').read_text()));report=json.loads((RESULTS/'minimum.json').read_text())
        C=E[:,report['coefficient_parameter_columns']]
        check_minors(C,report['minors'])
        sharp=report['sharp_control'];M=sp.Matrix(16,256,lambda i,j:E[i*256+j,sharp['coefficient_parameter']])
        rr=sharp['minor']['minor_rows'];cc=sharp['minor']['minor_columns'];core=M.extract(rr,cc)
        self.assertNotEqual(core.det(),0)
        self.assertEqual(M,M[:,cc]*core.inv()*M[rr,:])
        broken=C.copy();first=report['minors'][0]['positions']
        broken[first[0][0]*256+first[1][1],0]=1
        with self.assertRaises(AssertionError):check_minors(broken,report['minors'])

    def test_target_support_ceiling_has_a_sharp_control(self):
        report=v.reports()['support_control']
        self.assertEqual(report['original_matrix_ranks'],[11,11])
        self.assertEqual(report['projected_matrix_ranks'],[3,7])
        self.assertEqual(report['projected_first_rank'],2)
        self.assertEqual(report['projected_joint_column_dimension'],10)
        self.assertEqual(report['projected_joint_row_dimension'],7)


if __name__=='__main__':unittest.main()

"""Independent source-coordinate and saved polynomial-minor checks."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-integrable-boundary-shears'
RESULTS=ROOT/'results/integrable-boundary-shears-2026-10-21'
spec=importlib.util.spec_from_file_location('integrable_shear_verifier',PACKAGE/'verify.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
DEGREES=[(0,0),(1,0),(0,1)]


def rows(records,count):
    result=[{} for _ in range(count)]
    for i,j,*coefficients in records:result[i][j]=coefficients
    return result


def index(i,j,z):return (4*i+j)*7+z


def coefficient(a,b,c):
    i,s,za=a//28,a//7%4,a%7
    p,j,zb=b//28,b//7%4,b%7
    r,q,zc=c//28,c//7%4,c%7
    return int(za==6-p-q and zb==6-r-s and zc==6-i-j)


def product_at(a,left,right):
    output={}
    for b,P in left.items():
        for c,Q in right.items():
            if not coefficient(a,b,c):continue
            for i,x in enumerate(P):
                for j,y in enumerate(Q):
                    degree=(DEGREES[i][0]+DEGREES[j][0],DEGREES[i][1]+DEGREES[j][1])
                    output[degree]=output.get(degree,0)+x*y
    return {degree:value for degree,value in output.items() if value}


def affine(coefficients):return coefficients[0]+v.A*coefficients[1]+v.B*coefficients[2]


class IntegrableBoundaryShearTests(unittest.TestCase):
    def test_all_saved_reports_replay(self):
        for name,report in v.reports().items():
            self.assertEqual(report,json.loads((RESULTS/(name+'.json')).read_text()))

    def test_full_polynomial_fiber_from_fixed_source_indices(self):
        report=json.loads((RESULTS/'family.json').read_text());B=rows(report['B'],14);C=rows(report['C'],14)
        baseline=sp.zeros(112,196);K=set(report['source_first_kernel_indices'])
        for a,b,c in itertools.product(range(112),range(14),range(14)):
            result=product_at(a,B[b],C[c])
            self.assertTrue(all(degree==(0,0) for degree in result))
            if a in K:self.assertFalse(result)
            baseline[a,14*b+c]=result.get((0,0),0)
        minor=report['first_minor'];self.assertEqual(baseline[report['source_first_leading_indices'],:].extract(minor['rows'],minor['columns']).det(),sp.Rational(minor['determinant']))
        changed=[dict(row) for row in B];raw=report['raw_boundary_indices'].index(8)
        changed[raw][index(1,3,4)]=[0,1,0]
        corrupt=product_at(index(2,2,2),changed[raw],C[raw])
        self.assertEqual(corrupt.get((1,0)),2)

    def test_chart_minors_by_independent_coefficient_formula(self):
        report=json.loads((RESULTS/'family.json').read_text());saved=json.loads((RESULTS/'annihilators.json').read_text())
        B=rows(report['B'],14);C=rows(report['C'],14);K=report['source_first_kernel_indices']
        for side,basis in [('B',B),('C',C)]:
            M=sp.Matrix(14,112,lambda i,j:affine(basis[i].get(j,[0,0,0])))
            self.assertEqual(M[:,report['fixed_pivot_columns'][side]],sp.eye(14))
            for witness in saved[side]['charts']+[saved[side]['origin_minor']]:
                def entry(row,column):
                    a=K[row//14];other=row%14
                    if side=='B':return sum(affine(value)*coefficient(a,column,c) for c,value in C[other].items())
                    return sum(affine(value)*coefficient(a,b,column) for b,value in B[other].items())
                minor=sp.Matrix([[entry(i,j) for j in witness['columns']] for i in witness['rows']])
                if witness is saved[side]['origin_minor']:minor=minor.subs({v.A:0,v.B:0})
                self.assertEqual(sp.factor(minor.det(method='domain-ge')),sp.sympify(witness['determinant']))

    def test_every_polynomial_jet_coefficient_and_normal_rank(self):
        report=json.loads((RESULTS/'polynomial_maps.json').read_text());family=json.loads((RESULTS/'family.json').read_text())
        P=[rows(data,18) for data in report['P']];Q=[rows(data,18) for data in report['Q']]
        for a,b,c in itertools.product(family['source_first_kernel_indices'],range(18),range(18)):
            output={}
            for i,j in itertools.product(range(3),repeat=2):
                for (da,db),value in product_at(a,P[i][b],Q[j][c]).items():
                    key=(i+j,da,db);output[key]=output.get(key,0)+value
            self.assertFalse(any(output.values()))
        t=sp.Symbol('t');kept=family['raw_boundary_indices']
        for data,sign in [(P,1),(Q,-1)]:
            matrix=sum((t**k*sp.Matrix(18,112,lambda i,j:affine(level[i].get(j,[0,0,0]))) for k,level in enumerate(data)),sp.zeros(18,112))
            for i in range(4):
                relation=t*matrix[i,:]-sign*(matrix[4+kept.index(4+i),:]-matrix[4+kept.index(8+i),:])
                self.assertFalse(any(sp.expand(value) for value in relation))
        previous=json.loads((ROOT/'results/third-boundary-trap-2026-10-21/normal.json').read_text());plane=v.decode(previous['plane_directions'])
        normal=[112*b+j for b in range(8) for j in range(112) if (j//28 if b<4 else j//7%4) in [1,2]]
        full=sp.zeros(896,2)
        for leg,data in enumerate([P,Q]):
            for i in range(4):
                for j,value in data[1][i].items():full[448*leg+112*i+j,:]=sp.Matrix(1,2,value[1:])
        combined=plane.row_join(full[normal,:]);minor=report['normal_rank_six_minor']
        self.assertEqual(combined.extract(minor['rows'],minor['columns']).det(),sp.Rational(minor['determinant']))
        self.assertNotEqual(minor['determinant'],'0')


if __name__=='__main__':unittest.main()

"""Independent interval counts, theorem hypotheses and corner determinants."""
import importlib.util
import itertools
import json
from math import isqrt
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-rectangular-ordinary-frontier'
RESULTS=ROOT/'results/rectangular-ordinary-frontier-2026-10-21'


def load(name):
    spec=importlib.util.spec_from_file_location('rectangular_frontier_'+name,PACKAGE/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

v=load('verify');corners=load('corners')


def all_exclusions(a,shape):
    N=a*a*(2*a-1);m=2*a-1;witnesses=[]
    for x,y,z in itertools.permutations(shape):
        bound=z+2*N-z*x-z*y;dimension=x*y
        if bound<a*a:witnesses.append(('minimum',x,y,z))
        if dimension>a*a and bound<2*a*a:witnesses.append(('polynomial',x,y,z))
        for r in range(2,a):
            if 3*r<=m and dimension>r*a*a and bound<(r+1)*a*a:witnesses.append(('symbol',r,x,y,z))
            if m==3*r-1 and dimension>max(r,4)*a*a and bound<(r+1)*a*a:witnesses.append(('boundary',r,x,y,z))
    return witnesses


def check_witness(a,record):
    w=record['witness'];assert w is not None
    x,y=w['matrix_parameter_dimensions'];z=w['slice_rank'];N=a*a*(2*a-1)
    assert sorted([x,y,z])==record['shape']
    assert w['lift_rank_upper_bound']==z+(N-x*z)+(N-y*z)
    assert w['block_parameter_dimension']==x*y
    if w['gate']=='minimum_slice_rank':assert w['required_rank']==a*a
    elif w['gate']=='polynomial_rank_locus':
        assert w['required_rank']==2*a*a and w['dimension_cap']==a*a and x*y>a*a
    else:
        r=w['symbol_rank'];assert 2<=r<a
        assert w['required_rank']==(r+1)*a*a
        if w['gate']=='hankel_symbol':assert 3*r<=2*a-1 and w['dimension_cap']==r*a*a
        else:assert w['gate']=='first_hankel_boundary' and 2*a-1==3*r-1 and w['dimension_cap']==max(r,4)*a*a
        assert x*y>w['dimension_cap']
    assert w['lift_rank_upper_bound']<w['required_rank']


class RectangularOrdinaryFrontierTests(unittest.TestCase):
    def test_all_saved_reports_replay(self):
        self.assertEqual(v.report(),json.loads((RESULTS/'frontier.json').read_text()))
        self.assertEqual(corners.report(),json.loads((RESULTS/'corners.json').read_text()))

    def test_independent_candidate_counts_and_every_gate(self):
        report=json.loads((RESULTS/'frontier.json').read_text());total=excluded=0
        for source in report['sources']:
            a=source['a'];N=a*a*(2*a-1);threshold=(6*a-2)**4
            # Count intervals in n without enumerating n as the maintained driver does.
            count=sum(max(0,N//h-max(h,threshold//(216*l*h)+1)+1)
                      for h in range(1,isqrt(N)+1) for l in range(1,h+1))
            self.assertEqual(count,source['improving_shapes'])
            seen=set()
            for record in source['records']:
                l,h,n=record['shape'];self.assertTrue(1<=l<=h<=n and h*n<=N)
                self.assertEqual(record['volume'],l*h*n)
                self.assertEqual(record['leg_dimensions'],[l*h,h*n,n*l])
                self.assertGreater(216*l*h*n,threshold)
                self.assertNotIn((l,h,n),seen);seen.add((l,h,n))
                self.assertEqual(record['excluded'],bool(all_exclusions(a,[l,h,n])))
                if record['excluded']:check_witness(a,record);excluded+=1
                else:self.assertIsNone(record['witness'])
            self.assertEqual(len(seen),count);total+=count
            if a<=7:self.assertFalse(source['survivors'])
        self.assertEqual((total,excluded),(5139,4192))
        bad=next(r for s in report['sources'] for r in s['records'] if r['excluded'])
        bad=json.loads(json.dumps(bad));bad['witness']['lift_rank_upper_bound']+=1
        with self.assertRaises(AssertionError):check_witness(4,bad)

    def test_unique_first_survivor_and_conditional_integer_comparison(self):
        report=json.loads((RESULTS/'frontier.json').read_text());source=next(s for s in report['sources'] if s['survivors'])
        self.assertEqual(source['a'],8);self.assertEqual(source['survivors'],[[27,28,28]])
        conditional=report['conditional_exponent'];certificate=conditional['integer_certificate']
        self.assertGreater(certificate['left_base']**certificate['left_power'],certificate['right_base']**certificate['right_power'])
        self.assertEqual(certificate,{'left_base':216*27*28*28,'left_power':191,'right_base':46,'right_power':9*85})
        self.assertLess(4*191,9*85);self.assertFalse(conditional['premise_proved'])
        self.assertFalse(report['improves_omega'])

    def test_corner_minor_by_direct_symbolic_determinant(self):
        # Different polynomial values in all off-corner coefficients; only the corner
        # Hankel block controls the nested determinant.
        a=b=2;h=sp.symbols('h0:3');F={(i,k,s):17*i+5*k+3*s+1 for i,k,s in itertools.product(range(2),range(3),range(2))}
        for k in range(3):F[1,k,1]=h[k]
        rows=[(j,p,r+1) for j in range(2) for r in range(2) for p in range(2)]
        columns=[(j+1,q,r) for j in range(2) for r in range(2) for q in range(2)]
        M=sp.Matrix([[F.get((H-j,p+q,L-r),0) for H,q,r in columns] for j,p,L in rows])
        self.assertEqual(sp.factor(M.det(method='domain-ge')),(h[0]*h[2]-h[1]**2)**4)
        corrupt=M.copy();corrupt[0,4]=1
        self.assertNotEqual(sp.factor(corrupt.det(method='domain-ge')),(h[0]*h[2]-h[1]**2)**4)
        with self.assertRaises(ValueError):corners.check(2,2,[0,0],[0,1])


if __name__=='__main__':unittest.main()

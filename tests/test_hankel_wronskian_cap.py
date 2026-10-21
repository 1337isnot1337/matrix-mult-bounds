"""Direct determinants and translation identities for the uniform cap proof."""
import importlib.util
from itertools import product
import json
from math import comb,prod
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-hankel-wronskian-cap'
RESULTS=ROOT/'results/hankel-wronskian-cap-2026-10-21'
spec=importlib.util.spec_from_file_location('wronskian_controls',PACKAGE/'verify.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


class HankelWronskianCapTests(unittest.TestCase):
    def test_saved_controls_replay(self):
        x=json.loads((RESULTS/'controls.json').read_text());self.assertEqual(x,v.report())
        self.assertEqual(x['tail_minors']['complete_case_count'],4356)
        self.assertEqual(x['monomial_wronskians']['case_count'],375)
        self.assertFalse(x['full_segre_image_cap_r_claimed'])
        self.assertFalse(x['independent_review']);self.assertFalse(x['improves_omega'])

    def test_every_antidiagonal_minor_by_direct_exact_determinant(self):
        x=json.loads((RESULTS/'controls.json').read_text())
        for a,b,r,k,i0,j0 in x['tail_minors']['cases']:
            # Direct numerical matrices use nonzero arbitrary later moments, so
            # the test does not implement the zero-pattern check in tail_minor.
            h=[0]*k+[2]+[j*j+3*j+7 for j in range(k+1,a+b-1)]
            M=sp.Matrix(r+1,r+1,lambda i,j:h[i0+i+j0+j])
            self.assertEqual(int(M.to_DM().det()),(-1)**(r*(r+1)//2)*2**(r+1))
        with self.assertRaises(ValueError):v.tail_minor(3,4,3,3)
        with self.assertRaises(ValueError):v.tail_minor(3,4,2,4)

    def test_symbolic_shear_and_polynomial_translation(self):
        lam,t=sp.symbols('lam t')
        for a,b in [(2,3),(3,4),(4,4)]:
            d=a+b-2;h=sp.symbols('h0:'+str(d+1))
            transformed=[sum(comb(d-k,j-k)*lam**(j-k)*h[j] for j in range(k,d+1)) for k in range(d+1)]
            H=sp.Matrix(a,b,lambda i,j:h[i+j]);Hp=sp.Matrix(a,b,lambda i,j:transformed[i+j])
            A=sp.Matrix(a,a,lambda i,j:comb(a-1-i,j-i)*lam**(j-i) if j>=i else 0)
            B=sp.Matrix(b,b,lambda i,j:comb(b-1-i,j-i)*lam**(j-i) if j>=i else 0)
            self.assertEqual((A*H*B.T-Hp).applyfunc(sp.expand),sp.zeros(a,b))
            self.assertEqual(A.det(),1);self.assertEqual(B.det(),1)
            f=sum((-1)**k*comb(d,k)*h[k]*t**k for k in range(d+1))
            fp=sum((-1)**k*comb(d,k)*transformed[k]*t**k for k in range(d+1))
            self.assertEqual(sp.expand(fp-f.subs(t,t-lam)),0)
            self.assertNotEqual(sp.expand(fp-f.subs(t,t+lam)),0)

    def test_exported_polynomial_wronskians_by_point_evaluation(self):
        x=json.loads((RESULTS/'controls.json').read_text())
        for case in x['polynomial_wronskians']:
            polynomials=case['polynomials_low_to_high'];dimension=len(polynomials)
            W=case['wronskian_low_to_high']
            for point in [-2,-1,0,1,3]:
                # Evaluate derivatives directly with integer falling products.
                M=sp.Matrix([[sum(c*prod(range(n-j+1,n+1))*point**(n-j)
                                  for n,c in enumerate(f) if n>=j)
                              for f in polynomials] for j in range(dimension)])
                self.assertEqual(int(M.to_DM().det()),sum(c*point**n for n,c in enumerate(W)))
            degrees=case['degrees'];leading=prod(f[-1] for f in polynomials)*prod(degrees[j]-degrees[i] for i in range(dimension) for j in range(i+1,dimension))
            self.assertEqual(case['leading_coefficient'],leading)

    def test_generated_rank_witnesses_and_invalid_bases(self):
        x=json.loads((RESULTS/'controls.json').read_text())
        for case in x['generated_witnesses']:
            a,b,r=case['a'],case['b'],case['r'];d=a+b-2
            basis=sp.Matrix([[sp.Rational(c) for c in row] for row in case['input_basis']])
            coefficients=sp.Matrix([[sp.Rational(c) for c in case['linear_combination_coefficients']]])
            self.assertEqual(list(coefficients*basis),case['integer_moments'])
            h=case['integer_moments'];minor=case['original_minor']
            H=sp.Matrix(a,b,lambda i,j:h[i+j])
            self.assertEqual(len(minor['rows']),r+1);self.assertEqual(len(minor['columns']),r+1)
            self.assertEqual(int(H.extract(minor['rows'],minor['columns']).to_DM().det()),minor['determinant'])
            self.assertNotEqual(minor['determinant'],0)
            lam=case['shear_lambda'];self.assertTrue(0<=lam<=(r+1)*(d-r))
            shifted=[sum(comb(d-k,j-k)*lam**(j-k)*h[j] for j in range(k,d+1)) for k in range(r+1)]
            self.assertEqual(shifted,[0]*r+[case['sheared_pivot']])
            self.assertEqual(v.witness(a,b,r,case['input_basis']),case)
        self.assertEqual(x['generated_witnesses'][-1]['shear_lambda'],2)
        with self.assertRaises(ValueError):v.witness(3,3,2,[[0]*5]*3)
        with self.assertRaises(ValueError):v.witness(3,3,2,[[1,0]])
        with self.assertRaises(ValueError):v.witness(2,3,2,[[0]*4]*3)

    def test_hypotheses_and_sharp_spaces(self):
        for a,b in product(range(2,8),repeat=2):
            for r in range(1,min(a,b)):
                self.assertEqual(v.linear_space_cap(a,b,r),r)
                h=[0]*(a+b-1);h[r-1]=1
                H=sp.Matrix(a,b,lambda i,j:h[i+j])
                self.assertEqual(H.to_DM().rank(),r)
        self.assertIsNone(v.linear_space_cap(2,3,2))
        t=sp.symbols('t');W=sp.wronskian([1,t**5],t)
        self.assertEqual(W,5*t**4);self.assertTrue(sp.Poly(W,t,modulus=5).is_zero)
        # Independence survives mod5, so the characteristic-zero proof needs
        # its hypothesis; no failure of the finite-field cap is asserted.


if __name__=='__main__':unittest.main()

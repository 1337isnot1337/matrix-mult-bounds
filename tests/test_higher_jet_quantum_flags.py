"""Controls for higher coefficient ranks, moving projections and block minors."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-20-higher-jet-quantum-flags'
RESULTS=ROOT/'results/higher-jet-quantum-flags-2026-10-20'
_spec=importlib.util.spec_from_file_location('higher_jet_controls',PACKAGE/'controls.py')
controls=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(controls)
blocks=controls.blocks;one=controls.one


def dual(poly,root):
    value=derivative=0;p=one.PRIME
    for i in range(poly.degree(),-1,-1):
        c=poly.get((i,),one.qmod.QQ.zero)
        coefficient=int(c.numerator)*pow(int(c.denominator),-1,p)%p
        value,derivative=(value*root+coefficient)%p,(derivative*root+value)%p
    return value,derivative


class HigherJetQuantumTests(unittest.TestCase):
    def test_block_derivatives_against_normalized_dual_numbers(self):
        minima,data=blocks.block_maps();labels,entries=one.local_matrix(4)
        phi=one.qmod.R.from_expr(one.cyclotomic_poly(6,one.Symbol('q')))
        root=pow(10,(one.PRIME-1)//6,one.PRIME)
        for selected,item in data.items():
            for key,value in entries.items():
                block=labels[key[0]][:2]
                if block!=selected and selected!=(0,0):continue
                normalized=value*one.qmod.K(phi)**(int(block!=selected)-minima[block])
                n0,n1=dual(normalized.numer,root);d0,d1=dual(normalized.denom,root)
                self.assertNotEqual(d0,0)
                self.assertEqual(item['leading'].get(key,0),n0*pow(d0,-1,one.PRIME)%one.PRIME)
                self.assertEqual(item['derivative'].get(key,0),(n1*d0-n0*d1)*pow(d0,-2,one.PRIME)%one.PRIME)

    def test_all_256_block_certificates_replay(self):
        saved=json.loads((RESULTS/'block-certificates.json').read_text())
        self.assertEqual(blocks.report(),saved)
        self.assertEqual(saved['counts'],{'leading':131,'first_jet':125})
        self.assertEqual(len(saved['records']),256)
        self.assertTrue(all(r['slice_rank_upper_bound']==97 for r in saved['records']))

    def test_nonzero_rates_preserve_every_block_jet_minor(self):
        _,data=blocks.block_maps()
        saved=json.loads((RESULTS/'block-certificates.json').read_text())
        for record in saved['records']:
            if record['method']!='first_jet':continue
            B=data[tuple(record['left_block'])];C=data[tuple(record['right_block'])]
            witness=record['witness'];rate=one.PRIME-1
            derivative={key:value*rate%one.PRIME for key,value in B['derivative'].items()
                        if key[0] not in B['row_support']}
            rows=one.projected_source(4,{**B['leading'],**derivative},C['leading'])
            determinant=one.determinant_mod([[rows[i].get(j,0) for j in witness['minor_columns']]
                                            for i in witness['minor_rows']])
            self.assertEqual(determinant,witness['minor_determinant_mod_prime']*
                             pow(rate,witness['nonzero_rate_monomial_exponent'],one.PRIME)%one.PRIME)

    def test_explicit_moving_surjections_and_slice_witnesses(self):
        actual=controls.report()
        self.assertEqual(actual,json.loads((RESULTS/'moving-controls.json').read_text()))
        self.assertEqual(len(actual['records']),32)
        self.assertTrue(all(r['minor_determinant_mod_prime'] for r in actual['records']))
        # Columns outside the two killed directions form an identity minor
        # for L0+tL1, while its restriction to E has ranks 2 at zero, 4 generically.
        t=sp.Symbol('t');L=sp.eye(112)
        for j in [70,71]:L[j,j]=0
        L[0,70]=t;L[1,71]=t
        retained=[i for i in range(112) if i not in [70,71]]
        self.assertEqual(L.extract(retained,retained),sp.eye(110))
        self.assertEqual(L[:,[70,71,73,74]].subs(t,0).rank(),2)
        self.assertEqual(L[:,[70,71,73,74]].rank(),4)

    def test_higher_jet_smith_count_and_needed_hypothesis(self):
        t=sp.Symbol('t');I=sp.eye(4)
        def elementary(i,j,power):
            M=I.copy();M[i,j]=t**power;return M
        U=elementary(0,1,1)*elementary(1,2,1)*elementary(3,0,2)
        V=sp.eye(6)
        for i,j,value in [(0,4,t*t),(1,4,t),(2,4,1),(1,5,t),(2,5,1)]:V[i,j]=value
        S=U*sp.diag(1,t,t*t,t**4)*V[:4,:]
        def coefficient(matrix,degree):return matrix.applyfunc(lambda x:sp.expand(x).coeff(t,degree))
        self.assertEqual(coefficient(S[:,4:],0),sp.zeros(4,2))
        self.assertEqual(coefficient(S[:,4:],1),sp.zeros(4,2))
        self.assertEqual(coefficient(S[:,4:],2).rank(),2)
        # The first three primitive rows are in W (column 3 vanishes).
        for degree in range(3):self.assertEqual(coefficient(S[:,3],degree),sp.zeros(4,1))
        cumulative=[]
        for size in range(1,5):
            orders=[]
            for rr in itertools.combinations(range(4),size):
                for cc in itertools.combinations(range(6),size):
                    determinant=sp.Poly(S.extract(rr,cc).det(),t)
                    if not determinant.is_zero:orders.append(min(m[0] for m in determinant.monoms()))
            cumulative.append(min(orders))
        self.assertEqual(cumulative,[0,1,3,7])
        self.assertEqual([cumulative[0]]+[cumulative[i]-cumulative[i-1] for i in range(1,4)],[0,1,2,4])
        bad=sp.Matrix([[1,t],[t,t*t]])
        self.assertEqual(bad.rank(),1)
        self.assertEqual(coefficient(bad,1).rank(),2)
        self.assertNotEqual(coefficient(bad,0),sp.zeros(2))


if __name__=='__main__':unittest.main()

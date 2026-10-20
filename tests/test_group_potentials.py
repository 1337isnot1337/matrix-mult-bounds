"""Exact finite group certificates; no discovery solver is trusted here."""
import copy
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT/'research/ai/2026-10-20-group-potentials'
RESULTS=ROOT/'results/group-potentials-2026-10-20'
sys.path.insert(0,str(RESEARCH))
import group_exact as exact
import fourier_certificate as fourier
import determinant_obstruction as determinant
import verify_reports as verify


class GroupPotentialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.G=exact.group(5)
        cls.control=json.loads((RESULTS/'sl2-5-control3-3-3.json').read_text())

    def test_group_and_affine_orders_inverses(self):
        for G,size in [(self.G,120),(exact.affine_group(5,4),20),
                       (exact.affine_group(7,3),21),(exact.affine_group(13,3),39)]:
            self.assertEqual(len(G['matrices']),size)
            for g in range(size):
                self.assertEqual(G['mul'][g][G['inv'][g]],0)
                self.assertEqual(G['mul'][G['inv'][g]][g],0)
                self.assertEqual(G['mul'][0][g],g)
                self.assertEqual(G['mul'][g][0],g)
        with self.assertRaises(ValueError): exact.affine_group(9,4)
        with self.assertRaises(ValueError): exact.affine_group(7,4)

    def test_control_by_independent_edge_weight_enumeration(self):
        witness=self.control['witness'];S,T,U=witness['sets']
        a=witness['potentials'][:3];b=witness['potentials'][3:6];c=witness['potentials'][6:]
        X={self.G['mul'][self.G['inv'][s]][t]:a[i]-b[j]
           for i,s in enumerate(S) for j,t in enumerate(T)}
        Y={self.G['mul'][self.G['inv'][t]][u]:b[j]-c[k]
           for j,t in enumerate(T) for k,u in enumerate(U)}
        Z={self.G['mul'][self.G['inv'][u]][s]:c[k]-a[i]
           for k,u in enumerate(U) for i,s in enumerate(S)}
        self.assertEqual([len(X),len(Y),len(Z)],[9,9,9])
        weights=[]
        for x,wx in X.items():
            for y,wy in Y.items():
                for z,wz in Z.items():
                    if self.G['mul'][self.G['mul'][x][y]][z]==0:
                        weights.append(wx+wy+wz)
        self.assertEqual(weights.count(0),27)
        self.assertEqual(len(weights),28)
        self.assertEqual(sum(w>0 for w in weights),1)
        self.assertTrue(all(w>=0 for w in weights))
        self.assertTrue(verify.verify_run(self.control)['exact_witness_replayed'])

    def test_bad_witness_and_farkas_tampering_are_rejected(self):
        witness=self.control['witness']
        with self.assertRaises(ValueError):
            exact.verify_witness(self.G,witness['sets'],[0]*9)
        with self.assertRaises(ValueError):
            exact.pair_map(self.G,[0,0],[0])
        report=json.loads((RESULTS/'sl2-5-control6-6-6.json').read_text())
        broken=copy.deepcopy(report)
        broken['cuts'][0]['weights'][0]*=2
        with self.assertRaises(ValueError):verify.verify_run(broken)

    def test_every_saved_farkas_cut_replays(self):
        counts=[]
        for name in ['sl2-5-control6-6-6.json','affine-5-4-shape4-4-5.json']:
            result=verify.verify_run(json.loads((RESULTS/name).read_text()))
            self.assertFalse(result['unsat_proof_checked'])
            self.assertFalse(result['improves_omega'])
            counts.append(result['exact_cuts_replayed'])
        self.assertEqual(counts,[20,459])

    def test_source_idempotents_and_rational_gate_replay(self):
        saved=json.loads((RESULTS/'fourier_and_conditional_gates.json').read_text())
        self.assertEqual(fourier.report(),saved)
        self.assertEqual(saved['source']['irreducible_degrees'],[1,2,2,3,3,4,4,5,6])
        self.assertEqual(saved['source']['pairwise_idempotent_products_verified'],81)
        self.assertEqual(sum(d*d for d in saved['source']['irreducible_degrees']),120)
        for row in saved['conditional_gates']:
            self.assertGreater(Q(row['strict_margin_lower']),0)
            self.assertLess(Q(row['bound']),Q(9,4))
            self.assertFalse(row['actual_improvement_established'])

    def test_block_minor_divisor_independently(self):
        a,b,c,d=sp.symbols('a b c d')
        A=sp.Matrix([[a,b],[c,d]])
        M=sp.diag(A,A)
        determinant2=a*d-b*c
        # Every 3-minor of two repeated 2-blocks must retain one determinant.
        from itertools import combinations
        for rows in combinations(range(4),3):
            for cols in combinations(range(4),3):
                remainder=sp.rem(M.extract(rows,cols).det(),determinant2,a,b,c,d)
                self.assertEqual(remainder,0)
        variables=sp.symbols('x0:9')
        generic_det=sp.Matrix(3,3,variables).det()
        factors=sp.factor_list(generic_det)[1]
        self.assertEqual(len(factors),1)
        self.assertEqual(factors[0][1],1)
        self.assertEqual(sp.total_degree(factors[0][0]),3)

    def test_determinant_screen_has_the_correct_boundary(self):
        self.assertTrue(determinant.obstruction(20,[1]*4+[4],4,5)['excluded'])
        self.assertEqual(determinant.obstruction(21,[1]*3+[3]*2,4,5)[
            'obstructing_irrep_degrees'],[3])
        self.assertTrue(determinant.obstruction(52,[1]*4+[4]*3,7,7)['excluded'])
        self.assertFalse(determinant.obstruction(39,[1]*3+[3]*4,6,6)['excluded'])
        self.assertFalse(determinant.obstruction(120,[1,2,2,3,3,4,4,5,6],10,10)['excluded'])
        with self.assertRaises(ValueError):determinant.obstruction(20,[1,4],4,5)
        self.assertEqual(determinant.report(),json.loads((RESULTS/'determinant_obstruction.json').read_text()))

    def test_abelian_coset_integer_boundaries(self):
        self.assertTrue(determinant.abelian_coset_bounds(19,3,[7,7,7])['excluded'])
        boundary=determinant.abelian_coset_bounds(19,3,[6,7,8])
        self.assertFalse(boundary['excluded'])
        self.assertEqual(boundary['max_coset_size_lower'],[2,3,3])
        self.assertEqual(boundary['max_coset_size_upper'],[2,3,3])
        self.assertFalse(determinant.abelian_coset_bounds(17,4,[8,8,8])['excluded'])
        with self.assertRaises(ValueError):determinant.abelian_coset_bounds(17,0,[8,8,8])


if __name__=='__main__':unittest.main()

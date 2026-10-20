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
import abelian_tables as tables
import rank_locus_obstruction as rank_locus
import symmetry_cnf as symmetry
import ternary_fourier as ternary
import quaternary_group as quaternary


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

    def test_borel_anchor_orbits_by_independent_matrix_conjugation(self):
        report=exact.borel_anchor_certificate(self.G)
        self.assertEqual(len(report['members']),20)
        self.assertEqual(len(report['quotient_orbit_witnesses']),19)
        for row in report['quotient_orbit_witnesses']:
            P=sp.Matrix(2,2,row['conjugator'])
            q=self.G['inv'][row['quotient']] if row['reverse_pair'] else row['quotient']
            Qmat=sp.Matrix(2,2,self.G['matrices'][q])
            conjugated=(P*Qmat*P.inv_mod(5)).applyfunc(lambda x:x%5)
            target=sp.Matrix(2,2,self.G['matrices'][row['anchor']])
            self.assertEqual(conjugated,target)

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

    def test_normal_table_completeness_by_independent_small_bruteforce(self):
        p=11
        expected=set()
        for b in range(1,p):
            for c in range(1,p):
                row=((0,1),(0,b),(0,c))
                if len({(x+y+z)%p for x in row[0] for y in row[1] for z in row[2]})==8:
                    expected.add(row)
        self.assertEqual(set(tables.normal_tables(p,2,2,2)),expected)
        rows=tables.normal_tables(29,3,3,3)
        self.assertEqual(len(rows),162)
        self.assertTrue(all(tables.verify_table_entry(29,row) for row in rows))

    def test_rank_locus_knapsack_matches_exhaustive_choices(self):
        from itertools import product
        degrees=[1,2,3]
        computed=rank_locus.profile(degrees)
        for budget,row in enumerate(computed):
            choices=[ks for ks in product(*(range(d+1) for d in degrees))
                     if sum(d*k for d,k in zip(degrees,ks))<=budget]
            value=max(sum(k*(2*d-k) for d,k in zip(degrees,ks)) for ks in choices)
            self.assertEqual(row['dimension'],value)
            self.assertLessEqual(row['actual_regular_rank'],budget)
            self.assertEqual(sum(k*(2*d-k) for d,k in zip(degrees,row['block_ranks'])),value)

    def test_rank_locus_frontier_and_block_witnesses(self):
        saved=json.loads((RESULTS/'rank_locus_obstruction.json').read_text())
        self.assertEqual(rank_locus.report(),saved)
        self.assertEqual(saved['surviving_shapes'],[[10,10,10]])
        self.assertEqual(len(saved['potential_improvement_shapes']),7)
        degrees=saved['source_degrees']
        for row in saved['potential_improvement_shapes']:
            if row['shape'] in ([9,9,12],[9,10,11]):
                self.assertTrue(row['excluded'])
                self.assertEqual(row['low_rank_locus']['dimension'],14)
                self.assertEqual(row['low_rank_locus']['actual_regular_rank'],8)
            k=row['low_rank_locus']['block_ranks']
            self.assertEqual(sum(d*x for d,x in zip(degrees,k)),row['low_rank_locus']['actual_regular_rank'])
            self.assertEqual(sum(x*(2*d-x) for d,x in zip(degrees,k)),row['low_rank_locus']['dimension'])

    def test_guarded_lex_cnf_against_complete_boolean_enumeration(self):
        from itertools import product
        counter=[5]
        def fresh():counter[0]+=1;return counter[0]
        clauses=symmetry.lex_geq([1,2,3,4],[4,3,2,1],5,fresh)
        for bits in product([False,True],repeat=5):
            expected=(not bits[4]) or bits[:4]>=tuple(reversed(bits[:4]))
            possible=False
            for extra in product([False,True],repeat=counter[0]-5):
                values=(False,)+bits+extra
                if all(any(values[abs(lit)]==(lit>0) for lit in clause) for clause in clauses):
                    possible=True;break
            self.assertEqual(possible,expected)

    def test_ternary_fourier_spectrum_and_scalar_certificates(self):
        from itertools import product
        saved=json.loads((RESULTS/'ternary_fourier_obstruction.json').read_text())
        self.assertEqual(ternary.certificate(),saved)
        # Independent character evaluation in Q(omega), omega^2=-omega-1.
        spectrum={}
        powers=[(1,0),(0,1),(-1,-1)]
        for dual in product(range(3),repeat=4):
            if not any(dual):continue
            u,v=map(sum,zip(*(powers[e] for e in (0,*dual[:3]))))
            norm=u*u-u*v+v*v
            spectrum[norm]=spectrum.get(norm,0)+1
        self.assertEqual(spectrum,{1:36,4:18,7:24,16:2})
        self.assertGreater(saved['elementary_lower_bound'],saved['unique_sum_parseval_required'])
        self.assertEqual(saved['stronger_lower_bound'],1682)

    def test_quaternary_group_and_offset_certificates(self):
        from itertools import product
        G=quaternary.group()
        self.assertEqual(len(G['matrices']),192)
        for g in range(192):
            self.assertEqual(G['mul'][g][G['inv'][g]],0)
            self.assertEqual(G['mul'][G['inv'][g]][g],0)
        for a,b,c in product(range(4),repeat=3):
            self.assertEqual(quaternary.fm(a,quaternary.fm(b,c)),
                             quaternary.fm(quaternary.fm(a,b),c))
            self.assertEqual(quaternary.fm(a,b^c),quaternary.fm(a,b)^quaternary.fm(a,c))
        counts=[]
        for name in ['quaternary-fixed-planes-offsets.json','quaternary-one-shear-offsets.json']:
            report=json.loads((RESULTS/name).read_text())
            result=verify.verify_run(report)
            counts.append(result['exact_cuts_replayed'])
            broken=copy.deepcopy(report)
            broken['cuts'][0]['offset_choice_cut'][0][2]^=1
            with self.assertRaises(ValueError):verify.verify_run(broken)
        self.assertEqual(counts,[167,259])


if __name__=='__main__':unittest.main()

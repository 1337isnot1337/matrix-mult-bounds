"""External finite-domain reflexivity bound and independent sharp controls."""
from fractions import Fraction as Q
import json
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-semisimple-reflexive'
RESULTS=ROOT/'results/semisimple-reflexive-2026-10-21'
sys.path.insert(0,str(PACKAGE))
import reflexive_screen


class SemisimpleReflexiveTests(unittest.TestCase):
    def test_candidate_reports_and_scope(self):
        data=reflexive_screen.report()
        self.assertEqual(data,json.loads((RESULTS/'report.json').read_text()))
        for candidate in data['compact_candidates']:
            self.assertTrue(candidate['ordinary_reflexive_screen']['ordinary_restriction_excluded'])
            self.assertFalse(candidate['ordinary_reflexive_screen']['general_border_degeneration_excluded'])
            self.assertFalse(candidate['square_determinant_screen']['general_border_degeneration_excluded'])
            self.assertEqual(candidate['other_necessary_tests']['Koszul_exclusions'],[])
            self.assertEqual(candidate['other_necessary_tests']['maximum_rank_locus_excess'],0)
            self.assertFalse(candidate['joint_degeneration_constructed'])
        for leg in data['larger_packet_ordinary_screen']['legs']:
            row=next(x for x in leg['budgets'] if x['rank_budget']==7)
            self.assertEqual((row['source_span_lower'],row['target_span_dimension']),(136,49))
        self.assertFalse(data['improves_omega'])

    def test_independent_jordan_sharp_control(self):
        # The evaluation constraints at basis vectors already force a
        #15-dimensional upper triangular5-by5 reflexive hull.
        J=sp.zeros(7)
        for i in range(4):J[i,i+1]=1
        P=sp.diag(1,1,1,1,1,0,0)
        L=[P]+[J**i for i in range(1,5)]
        self.assertEqual(sp.Matrix.hstack(*(sp.Matrix(A).reshape(49,1) for A in L)).rank(),5)
        allowed=sum(sp.Matrix.hstack(*(A[:,j] for A in L)).rank() for j in range(7))
        self.assertEqual(allowed,15)
        rank_one_units=[]
        for i in range(7):
            for j in range(7):
                if i<=j and j<5:continue
                U=sp.zeros(7);U[i,j]=1
                self.assertTrue(all(sum(U[a,b]*A[a,b] for a in range(7) for b in range(7))==0 for A in L))
                rank_one_units.append(U.reshape(49,1))
        self.assertEqual(sp.Matrix.hstack(*rank_one_units).rank(),34)
        self.assertEqual(reflexive_screen.rank_one_span_lower(7,5),34)

    def test_independent_hankel_boundary_control(self):
        constraints=sp.Matrix(10,49,lambda r,c:int(c//7+c%7==r+3))
        self.assertEqual(constraints.rank(),10)
        self.assertEqual(49-constraints.rank(),39)
        units=[]
        for i in range(7):
            for j in range(7):
                if i+j>2:continue
                unit=sp.zeros(49,1);unit[7*i+j]=1
                self.assertEqual(constraints*unit,sp.zeros(10,1))
                self.assertEqual(sp.Matrix(7,7,list(unit)).rank(),1)
                units.append(unit)
        self.assertEqual(sp.Matrix.hstack(*units).rank(),6)
        self.assertEqual(reflexive_screen.rank_one_span_lower(7,10),6)

    def test_exact_interval_gates_and_derivatives(self):
        data=json.loads((RESULTS/'report.json').read_text())
        for candidate in data['compact_candidates']:
            gate=candidate['conditional_gate'];tau=Q(gate['tau']);p,q=tau.numerator,tau.denominator;scale=gate['scale']
            for d,upper in zip(candidate['source_degrees'],gate['source_upper_terms']):
                self.assertLessEqual((upper-1)**q,d**p*scale**q)
                self.assertLess(d**p*scale**q,upper**q)
            for d,lower in zip(candidate['target_sides'],gate['target_lower_terms']):
                self.assertLessEqual(lower**q,d**p*scale**q)
                self.assertLess(d**p*scale**q,(lower+1)**q)
            self.assertGreater(gate['strict_margin_numerator'],0)
        self.assertEqual(Q(4,9)*Q(11,7)**2-Q(3,4)*Q(4,7)**2,Q(376,441))
        self.assertEqual(Q(7,9)**3-Q(1,6),Q(443,1458))

    def test_valid_identity_restrictions_and_edge_cases(self):
        for d in range(1,10):
            self.assertEqual(reflexive_screen.rank_one_span_lower(d,0),d*d)
            self.assertEqual(reflexive_screen.rank_one_span_lower(d,2*d-1),0)
            self.assertFalse(reflexive_screen.screen([d],[(d,d,d)])['ordinary_restriction_excluded'])
        for args in [(0,0),(2,-1),(2,1.0)]:
            with self.assertRaises(ValueError):reflexive_screen.rank_one_span_lower(*args)


if __name__=='__main__':unittest.main()

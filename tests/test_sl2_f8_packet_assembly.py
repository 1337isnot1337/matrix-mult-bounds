"""Conditional multi-target gate and an independent positive-coupling check."""
from fractions import Fraction as Q
from itertools import product
import json
from math import prod
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-sl2-f8-ideals'
RESULTS = ROOT/'results/sl2-f8-ideals-2026-10-21'
sys.path.insert(0,str(PACKAGE))
import packet_assembly


class SL2F8PacketAssemblyTests(unittest.TestCase):
    def test_exact_candidate_report_and_coordinate_barrier(self):
        data = packet_assembly.report()
        self.assertEqual(data,json.loads((RESULTS/'packet-assembly.json').read_text()))
        self.assertEqual(data['target_leg_dimensions'],[499]*3)
        self.assertEqual(data['necessary_tests']['Koszul_exclusion_powers'],[])
        self.assertEqual(data['necessary_tests']['maximum_rank_locus_excess'],0)
        bound = data['dense_coordinate_obstruction']
        self.assertTrue(bound['positive_completion_certified'])
        self.assertEqual(Q(bound['relative_marginal_deviation']),Q(2,27))
        self.assertEqual(Q(bound['positive_edge_mass_factor_lower_bound']),Q(3133,4266))
        self.assertFalse(data['improves_omega'])

    def test_integer_interval_gate_and_derivative_margin(self):
        data = json.loads((RESULTS/'packet-assembly.json').read_text())
        gate = data['conditional_gate']
        tau = Q(gate['tau'])
        p,q = tau.numerator,tau.denominator
        scale = gate['scale']
        for d,upper in zip(data['source_degrees'],gate['source_upper_terms']):
            value = d**p*scale**q
            self.assertLessEqual((upper-1)**q,value)
            self.assertLess(value,upper**q)
        for block,lower in zip(data['target_blocks'],gate['target_lower_terms']):
            value = prod(block)**p*scale**(3*q)
            self.assertLessEqual(lower**(3*q),value)
            self.assertLess(value,(lower+1)**(3*q))
        self.assertEqual(tau,Q(56,25))
        self.assertGreater(gate['strict_margin_numerator'],0)
        self.assertEqual(Q(gate['normalized_difference_derivative_lower_bound']),Q(3)*Q(2,9)*Q(7,9)**3-Q(2)*Q(1,8))

    def test_positive_marginal_completion_by_independent_exact_linear_solve(self):
        # A cyclic Latin tensor with different deleted labels in its three legs.
        # Solve all marginal equations independently, rather than evaluating the
        # bound's formula as a substitute for a real positive completion.
        order = 13
        parts = [[g for g in range(order) if g!=deleted] for deleted in [0,2,4]]
        edges = [(x,y,(-x-y)%order) for x,y in product(parts[0],parts[1])
                 if (-x-y)%order in parts[2]]
        positions = [{g:i for i,g in enumerate(row)} for row in parts]
        A = sp.zeros(36,len(edges))
        for j,edge in enumerate(edges):
            for f,g in enumerate(edge):
                A[12*f+positions[f][g],j] = 1
        target = sp.Matrix([sp.Rational(1,12)+(sp.Rational(1,600) if i==0 else
                             -sp.Rational(1,600) if i==1 else 0)
                            for f in range(3) for i in range(12)])
        uniform = sp.ones(len(edges),1)/len(edges)
        delta = target-A*uniform
        solution,parameters = (A*A.T).gauss_jordan_solve(delta)
        solution = solution.subs({p:0 for p in parameters})
        flow = uniform+A.T*solution
        self.assertEqual(A*flow,target)
        self.assertEqual(sum(flow),1)
        bound = packet_assembly.dense_marginal_bound(order,1,Q(1,50))
        factor = Q(bound['positive_edge_mass_factor_lower_bound'])
        lower = sp.Rational(factor.numerator,factor.denominator*len(edges))
        self.assertGreater(min(flow),0)
        self.assertGreaterEqual(min(flow),lower)

    def test_strict_boundary_and_invalid_parameters(self):
        self.assertFalse(packet_assembly.dense_marginal_bound(9,1,0)['positive_completion_certified'])
        self.assertTrue(packet_assembly.dense_marginal_bound(10,1,0)['positive_completion_certified'])
        for args in [(0,0,0),(3,3,0),(3,-1,0),(3,0,-1)]:
            with self.assertRaises(ValueError):
                packet_assembly.dense_marginal_bound(*args)


if __name__=='__main__':
    unittest.main()

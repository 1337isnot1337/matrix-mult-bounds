"""Ordinary-only span obstruction, exact gates and a full Laurent identity."""
from copy import deepcopy
from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-semisimple-low-slices'
RESULTS = ROOT/'results/semisimple-low-slices-2026-10-21'
sys.path.insert(0,str(PACKAGE))
import low_slice_spans
import mixed_local_packet


class SemisimpleLowSliceTests(unittest.TestCase):
    def test_reports_exclude_only_ordinary_maps(self):
        actual = json.loads(json.dumps(low_slice_spans.report()))
        self.assertEqual(actual,json.loads((RESULTS/'report.json').read_text()))
        for key,right in [('smaller_trade',29),('larger_packet_target',49)]:
            screen = actual[key]['ordinary_span_screen']
            self.assertTrue(screen['ordinary_restriction_excluded'])
            self.assertFalse(screen['general_border_degeneration_excluded'])
            for leg in screen['legs']:
                row = next(row for row in leg['rank_budgets'] if row['slice_rank_budget']==7)
                self.assertEqual(row['source_low_rank_span_lower'],56)
                self.assertEqual(row['target_low_rank_span_dimension'],right)
        self.assertEqual(actual['smaller_trade']['other_necessary_tests']['Koszul_exclusions'],[])
        self.assertEqual(actual['smaller_trade']['other_necessary_tests']['maximum_rank_locus_excess'],0)
        self.assertFalse(actual['improves_omega'])
        self.assertTrue(actual['smaller_trade']['border_factor_screen']['general_border_degeneration_excluded'])
        self.assertFalse(low_slice_spans.square_border_factor_screen([1,7,7,7,7,8,9,9,9],[(8,9,9),(9,8,9),(9,9,8)]*2+[(7,7,7)])['applicable'])

    def test_symbolic_minor_divisibility_and_compression(self):
        x = sp.symbols('x0:4')
        X = sp.Matrix(2,2,x)
        source_slice = sp.diag(X,X)
        determinant = X.det()
        nonzero = 0
        for rows in combinations(range(4),3):
            for cols in combinations(range(4),3):
                minor = sp.expand(source_slice[list(rows),list(cols)].det())
                quotient,remainder = sp.div(minor,determinant,*x)
                self.assertEqual(remainder,0)
                nonzero += int(minor!=0)
        self.assertGreater(nonzero,0)
        U = sp.Matrix([[1,2,0,1],[0,1,1,0],[2,0,1,1]])
        V = sp.Matrix([[1,0,1],[0,1,2],[1,1,0],[2,0,1]])
        compressed = sp.expand((U*source_slice*V).det())
        self.assertNotEqual(compressed,0)
        quotient,remainder = sp.div(compressed,determinant,*x)
        self.assertEqual(remainder,0)

    def test_independent_column_kernel_and_actual_slice_ranks(self):
        # Five global Vandermonde constraints on four Mat7 blocks. Each of
        #28 columns leaves a two-dimensional rank-one matrix subspace.
        C = sp.Matrix(5,196,lambda i,j:sp.Integer(j+1)**i)
        columns = []
        for block in range(4):
            for col in range(7):
                indices = [49*block+7*row+col for row in range(7)]
                kernel = C[:,indices].nullspace()
                self.assertEqual(len(kernel),2)
                for vector in kernel:
                    embedded = sp.zeros(196,1)
                    for i,index in enumerate(indices):
                        embedded[index] = vector[i]
                    self.assertEqual(C*embedded,sp.zeros(5,1))
                    columns.append(embedded)
        self.assertEqual(sp.Matrix.hstack(*columns).rank(),56)
        X = sp.Matrix(7,7,lambda i,j:columns[0][7*i+j])
        self.assertEqual(X.rank(),1)
        # Construct the actual first slice from multiplication indices,
        # separately from the reported rank formula.
        actual_slice = sp.zeros(49,49)
        for i in range(7):
            for j in range(7):
                for k in range(7):
                    actual_slice[7*j+k,7*k+i] = X[i,j]
        self.assertEqual(actual_slice.rank(),7)

    def test_exact_conditional_gate(self):
        data = json.loads((RESULTS/'report.json').read_text())['smaller_trade']
        gate = data['conditional_gate'];tau = Q(gate['tau'])
        p,q = tau.numerator,tau.denominator;scale = gate['scale']
        for degree,upper in zip(data['source_degrees'],gate['source_upper_terms']):
            self.assertLessEqual((upper-1)**q,degree**p*scale**q)
            self.assertLess(degree**p*scale**q,upper**q)
        for block,lower in zip(data['target_blocks'],gate['target_lower_terms']):
            degree = block[0]
            self.assertLessEqual(lower**q,degree**p*scale**q)
            self.assertLess(degree**p*scale**q,(lower+1)**q)
        self.assertEqual(gate['strict_margin_numerator'],5841095151)
        derivative = Q(7,9)**3-Q(4,9)**2-Q(3,2)*Q(1,3)**2-2*Q(2,9)**2
        self.assertEqual(derivative,Q(11,1458))
        self.assertEqual(Q(gate['derivative_lower_bound_on_2_to_9_fourths']),derivative)

    def test_known_restrictions_are_not_rejected(self):
        for degrees,blocks in [([7],[(7,7,7)]),([7],[(6,6,6)]),([2,3],[(2,2,2),(3,3,3)]),([7],[(7,7,6)])]:
            self.assertFalse(low_slice_spans.ordinary_span_screen(degrees,blocks)['ordinary_restriction_excluded'])

    def test_mixed_local_map_complete_replay_and_corruption(self):
        data = json.loads((RESULTS/'mixed-packet.json').read_text())
        self.assertEqual(mixed_local_packet.report(),data)
        result = data['coefficient_replay']
        self.assertEqual(result['negative_exponent_contributions_before_cancellation'],9072)
        self.assertEqual(result['surviving_exponent_counts'],{'0':648,'1':567})
        for key in ['forward_integer_matrix','backward_integer_numerator_matrix']:
            bad = deepcopy(data['map']);bad[key][0][0] += 1
            with self.assertRaises(ValueError):mixed_local_packet.verify(bad)
        bad = deepcopy(data['map']);bad['first_family_potentials'][0] += 1
        with self.assertRaises(ValueError):mixed_local_packet.verify(bad)

    def test_reduced_span_can_drop_at_a_singular_limit(self):
        # The two rank-one directions coalesce; flat scheme length remains2.
        t = sp.Symbol('t')
        two_lines = sp.Matrix([[0,t],[1,1]])
        self.assertEqual(two_lines.det(),-t)
        self.assertEqual(two_lines.subs(t,0).rank(),1)


if __name__=='__main__':unittest.main()

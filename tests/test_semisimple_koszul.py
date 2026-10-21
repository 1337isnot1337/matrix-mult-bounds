"""General semisimple Koszul gates and an exactly derived new group source."""
from fractions import Fraction
from itertools import product
import json
from math import prod
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-semisimple-koszul'
RESULTS = ROOT/'results/semisimple-koszul-2026-10-21'
sys.path.insert(0,str(PACKAGE))
sys.path.insert(0,str(PACKAGE.parent/'2026-10-20-f8-unequal'))
import semisimple_koszul
import sl2_f8_source
import sl2_f8_frames
from koszul_tables import koszul_matrix,rank_mod


def load(name):
    return json.loads((RESULTS/name).read_text())


class SemisimpleKoszulTests(unittest.TestCase):
    def test_small_direct_sum_formula_against_full_integer_matrices(self):
        for degrees in [[1,2],[1,1,2]]:
            N = sum(d*d for d in degrees)
            slices = [[[0]*N for _ in range(N)] for _ in range(N)]
            start = 0
            for d in degrees:
                for i,j,k in product(range(d),repeat=3):
                    slices[start+i*d+j][start+k*d+i][start+k*d+j] = 1
                start += d*d
            expected = semisimple_koszul.source_ranks(degrees)
            for p,rank in enumerate(expected):
                self.assertEqual(rank_mod(koszul_matrix(slices,p),103),rank)

    def test_complete_frontiers_and_retained_general_survivors(self):
        expected = load('frontiers.json')
        for row in expected['sources']:
            self.assertEqual(semisimple_koszul.frontier(row['source'],row['degrees']),row)
        F8,SL8 = expected['sources']
        self.assertEqual([len(r['koszul_surviving_shapes']) for r in [F8,SL8]],[21,16])
        self.assertEqual(sum(r['excluded'] for r in F8['koszul_records']),5)
        self.assertEqual(sum(r['excluded'] for r in SL8['koszul_records']),2)
        self.assertIn([19,19,19],F8['koszul_surviving_shapes'])
        self.assertIn([18,18,25],SL8['koszul_surviving_shapes'])

    def test_exact_group_center_source_and_field_arithmetic(self):
        result = sl2_f8_source.derive()
        self.assertEqual(result,load('sl2-f8-source.json'))
        self.assertEqual(result['complex_degrees'],[1,7,7,7,7,8,9,9,9])
        self.assertEqual(result['group_center_order'],1)
        self.assertEqual(sum(result['class_sizes']),504)
        self.assertEqual(sum(d*d for d in result['complex_degrees']),504)
        fm = sl2_f8_source.fm
        for a,b,c in product(range(8),repeat=3):
            self.assertEqual(fm(fm(a,b),c),fm(a,fm(b,c)))
            self.assertEqual(fm(a,b^c),fm(a,b)^fm(a,c))

    def test_conditional_gate_by_exact_integer_powers(self):
        report = load('sl2-f8-source.json')
        gate = report['conditional_exponent_gate']
        tau = Fraction(gate['tau'])
        m,q = tau.numerator,tau.denominator
        scale = gate['scale']
        for d,upper in zip(report['complex_degrees'],gate['source_term_upper_numerators']):
            value = d**m*scale**q
            self.assertLessEqual((upper-1)**q,value)
            self.assertLess(value,upper**q)
        lower = gate['target_lower_numerator']
        value = prod(gate['shape'])**m*scale**(3*q)
        self.assertLessEqual(lower**(3*q),value)
        self.assertLess(value,(lower+1)**(3*q))
        self.assertEqual(tau,Fraction(449,200))
        self.assertGreater(gate['strict_positive_margin_numerator'],0)
        self.assertFalse(report['improves_omega'])

    def test_rank_seven_control_and_rank_four_obstruction(self):
        self.assertFalse(semisimple_koszul.target_screen([1]*7,[2,2,2])['excluded'])
        cut = semisimple_koszul.target_screen([1]*4,[2,2,2])
        self.assertTrue(cut['excluded'])
        self.assertEqual(cut['witness']['power'],1)
        self.assertEqual([cut['witness']['source_rank'],cut['witness']['target_rank']],[12,16])

    def test_subgroup_control_and_honest_timeout_receipt(self):
        cosets = sl2_f8_frames.right_cosets()
        self.assertEqual(sorted(v for row in cosets for v in row),list(range(504)))
        control = load('sl2-f8-subgroup-control.json')
        receipt = sl2_f8_frames.verify_search(control)
        self.assertTrue(receipt['exact_witness_replayed'])
        self.assertEqual(control['shape'],[18,1,1])
        self.assertEqual(control['witness']['verification']['intended_terms'],18)
        actual = load('sl2-f8-subgroup-180s.json')
        receipt = sl2_f8_frames.verify_search(actual)
        self.assertFalse(receipt['exact_witness_replayed'])
        self.assertFalse(receipt['unsat_proof_checked'])
        self.assertEqual(actual['models'],0)
        self.assertEqual(actual['status'],'time-limit')

    def test_invalid_parameters_and_flattening(self):
        for degrees in [[],[0],[1.0],[-2]]:
            with self.assertRaises(ValueError):
                semisimple_koszul.source_ranks(degrees)
        with self.assertRaises(ValueError):
            semisimple_koszul.padded_basic_ranks(3,3,4)
        self.assertEqual(semisimple_koszul.target_screen([1]*4,[3,3,3])['reason'],'ordinary flattening')


if __name__=='__main__':
    unittest.main()

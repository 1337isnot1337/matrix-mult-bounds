"""Exact controls for the oblique repair, with distinct variant costs."""

from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
import unittest


PACKAGE=Path(__file__).resolve().parents[1]/'research/ai/2026-10-23-oblique-paired-repair'
if not PACKAGE.is_dir():
    PACKAGE=Path(__file__).resolve().parent
sys.path.insert(0,str(PACKAGE))
SPEC=importlib.util.spec_from_file_location('oblique_repair_verify',PACKAGE/'verify.py')
MODULE=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
from exact import Field, contract, matrix_multiplication, subtract, verify
from karatsuba_repair import certificate as karatsuba_certificate, expand_terms, one_dependency_terms


class ObliqueRepairTests(unittest.TestCase):
    def test_product_complete_identity_and_scalar_replay(self):
        case=MODULE.verify_case(6,4)
        saved=json.loads((PACKAGE/'witness.json').read_text())
        self.assertEqual(case,saved['cases'][0])
        self.assertEqual(MODULE.source_pins(PACKAGE.parents[2]),
                         saved['source_pin_verification'])
        self.assertEqual(case['verification']['exact_residual_flattening_ranks'],[9,11,11])
        self.assertEqual([piece['ranks'] for piece in case['residual_pieces']],
                         [[4,2,8],[4,8,2],[1,4,4]])
        self.assertEqual(case['scalar_repair']['scalar_rank_upper_bound'],19)
        self.assertEqual(case['direct_scalar_repair']['scalar_rank_upper_bound'],20)
        self.assertTrue(case['scalar_repair']['complete_decomposition_replayed'])
        self.assertEqual(case['free_first_map_optimum']['minimum_first_residual_rank'],9)
        self.assertFalse(case['improves_omega'])

    def test_nonproduct_cost_is_checked_separately(self):
        case=MODULE.verify_case(6,4,nonproduct=True)
        saved=json.loads((PACKAGE/'witness.json').read_text())
        self.assertEqual(case,saved['cases'][1])
        self.assertEqual(case['verification']['exact_residual_flattening_ranks'],[9,11,11])
        self.assertEqual([piece['ranks'] for piece in case['residual_pieces']],
                         [[4,3,9],[4,8,2],[1,4,4]])
        self.assertEqual(case['scalar_repair']['scalar_rank_upper_bound'],24)

    def test_karatsuba_one_dependency_family_and_corruption(self):
        for b in range(2,8):
            n=b+2
            residual=MODULE.formula_residual(n,b)
            report=karatsuba_certificate(n,b,residual)
            self.assertEqual(report['scalar_rank_upper_bound'],4*(n-1)-1)
        terms=one_dependency_terms(6,4)
        terms[0]['a'][0][1]*=-1
        self.assertNotEqual(expand_terms(terms),MODULE.formula_residual(6,4))

    def test_family_formula_and_boundary_case(self):
        for n,b in [(3,2),(4,2),(5,3),(5,4),(7,4),(8,4),(8,6)]:
            maps=MODULE.product_maps(n,b)
            actual,_=contract(n,b,(n-1,4,n-1),maps)
            residual=subtract(matrix_multiplication((n-1,4,n-1)),actual,Field())
            self.assertEqual(residual,MODULE.formula_residual(n,b))
            r,d=n-1,n-b-1
            expected=[r*r-b*b,2*r+d,2*r+d] if d else [0,0,0]
            report=verify(n,b,(r,4,r),maps,include_witness=False)
            self.assertEqual(report['exact_residual_flattening_ranks'],expected)

    def test_embedded_corner_is_a_different_residual(self):
        baseline=MODULE.embedded_corner()
        self.assertEqual(baseline['residual_ranks'],[9,20,20])
        self.assertEqual(baseline['scalar_rank_upper_bound'],36)

    def test_modular_zero_never_lifts_to_rational(self):
        maps=MODULE.product_maps(5,4)
        maps[0][0][0]+=7
        rational=verify(5,4,(4,4,4),maps,include_witness=False)
        modular=verify(5,4,(4,4,4),maps,7,include_witness=False)
        self.assertEqual(rational['exact_residual_flattening_ranks'],[1,4,4])
        self.assertEqual(modular['exact_residual_flattening_ranks'],[0,0,0])
        self.assertFalse(modular['rational_or_complex_rank_upper_bound_certified'])
        self.assertFalse(modular['finite_field_result_lifted_to_characteristic_zero'])

    def test_false_residual_and_invalid_coefficients_are_rejected(self):
        maps=MODULE.product_maps(6,4)
        with self.assertRaises(ArithmeticError):
            verify(6,4,(5,4,5),maps,expected_residual={})
        maps[0][0][0]=0.5
        with self.assertRaises(ValueError):
            verify(6,4,(5,4,5),maps)
        maps[0][0][0]=Fraction(1,7)
        with self.assertRaises(ValueError):
            verify(6,4,(5,4,5),maps,7)
        with self.assertRaises(ValueError):
            verify(6,4,(5,4,5),MODULE.product_maps(6,4),9)


if __name__=='__main__':
    unittest.main()

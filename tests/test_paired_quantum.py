"""Exact coverage of the prescribed paired quantum calibration."""
import importlib.util
from pathlib import Path
import unittest

from sympy import Matrix, Rational

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location(
    'paired_quantum_screens',
    ROOT/'research/ai/2026-10-21-paired-quantum/screens.py')
screens=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(screens)


class PairedQuantumTests(unittest.TestCase):
    def test_source_diagonal_identity(self):
        self.assertEqual(screens.source_controls(),353)

    def test_small_local_maps(self):
        for a,order,expected in ((2,3,[4,4,4]),(2,4,[3,6,6]),
                                 (3,10,[9,12,12]),(4,14,[16,18,18])):
            actual=[screens.regular_initial(screens.paired_local_map(a,leg),order)
                    ['regular_initial_rank'] for leg in range(3)]
            self.assertEqual(actual,expected)

    def test_small_tensor_is_not_matrix_multiplication(self):
        result=screens.algebra_screen(2,3)
        self.assertEqual(result['flattening_ranks'],[4,4,4])
        self.assertEqual(result['nonzero_coefficients'],36)
        self.assertEqual(result['invertible_slice_determinant_coefficients'],['-7/16','-7/16'])
        witness=result['first_product_failure']
        self.assertEqual(witness['product_indices'],[0,0])
        self.assertEqual(witness['product_span_rank'],5)
        self.assertEqual(witness['minor_columns'],[0,1,2,4,5])
        self.assertEqual(witness['minor_determinant_coefficients'],['1/343','19/343'])

    def test_size_ten_first_leg(self):
        result=screens.regular_initial(screens.paired_local_map(10,0),14)
        self.assertEqual(result['regular_initial_rank'],91)
        deficits=[(b['weight_index'],b['dimension']-b['rank'])
                  for b in result['weight_blocks'] if b['dimension']!=b['rank']]
        self.assertEqual(deficits,[(7,1),(8,2),(9,3),(10,2),(11,1)])

    def test_field_determinant_independent_control(self):
        field,_=screens.residue_field(3)
        z=field.unit
        matrix=[[z,field.one,field.convert(2)],
                [field.convert(3),z+field.one,field.convert(-1)],
                [field.convert(4),field.convert(Rational(1,2)),z**2]]
        expected=Matrix([[field.to_sympy(x) for x in row] for row in matrix]).det()
        self.assertEqual(screens.determinant_field(matrix,field),field.from_sympy(expected))


if __name__=='__main__':
    unittest.main()

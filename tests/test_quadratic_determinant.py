"""Exact determinant identity, source conventions, and field boundaries."""
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-quadratic-determinant'
SPEC = importlib.util.spec_from_file_location('quadratic_determinant', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class QuadraticDeterminantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads((ROOT / 'results/quadratic-determinant-2026-10-23/controls.json').read_text())

    def test_complete_saved_report(self):
        self.assertEqual(verify.report(), self.saved)
        self.assertEqual(self.saved['rational_matrix_count'], 29)
        self.assertEqual(self.saved['odd_prime_matrix_count'], 18)
        self.assertEqual(self.saved['rational_three_space_count'], 3)
        self.assertEqual(self.saved['edwards_symbolic']['block_sizes'], [8, 7])
        self.assertEqual(self.saved['edwards_symbolic']['row_column_permutation_inversions'], [28, 28])
        integral = self.saved['characteristic_two_integral']
        self.assertEqual(integral['T_term_count'], 15)
        self.assertEqual(integral['integer_factor_term_count'], 776)
        self.assertEqual(integral['reduced_factor_term_count'], 174)
        self.assertEqual(integral['triangular_variables'], ['a', 'b', 'h', 'i'])
        self.assertEqual(integral['triangular_source_size'], 15)
        self.assertFalse(self.saved['independent_review'])
        self.assertFalse(self.saved['improves_omega'])

    def test_literal_matrix_agrees_with_contraction_and_multiplication(self):
        coefficient = [[2, -1, 3], [4, 0, -2], [1, 5, 7]]
        vector = [Fraction(i - 7, i + 1) for i in range(15)]
        # Independent natural action: contract the x monomial against the
        # literal dual coordinate H, and multiply the z monomial by z^r.
        expected = [Fraction(0)] * 15
        for H in range(5):
            for r in range(3):
                for i in range(3):
                    for s in range(3):
                        if 0 <= H - i < 3:
                            expected[5 * (H - i) + r + s] += coefficient[i][s] * vector[3 * H + r]
        actual = [sum(entry * value for entry, value in zip(row, vector))
                  for row in verify.literal_source(coefficient)]
        transposed = [list(row) for row in zip(*coefficient)]
        wrong = [sum(entry * value for entry, value in zip(row, vector))
                 for row in verify.literal_source(transposed)]
        self.assertEqual(actual, expected)
        self.assertNotEqual(wrong, expected)

    def test_odd_source_row_permutation_is_rejected(self):
        coefficient = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        source = verify.literal_source(coefficient)
        self.assertEqual(verify.determinant_fraction(source), 1)
        source[0], source[1] = source[1], source[0]
        self.assertEqual(verify.determinant_fraction(source), -1)
        with patch.object(verify, 'literal_source', return_value=source):
            with self.assertRaisesRegex(ArithmeticError, 'cleared determinant identity'):
                verify.rational_control('wrong_row_order', coefficient)

    def test_corrupt_discriminant_sign_is_rejected(self):
        broken = verify.J.copy()
        broken[0, 2] = 2
        with patch.object(verify, 'J', broken):
            with self.assertRaisesRegex(ArithmeticError, 'cleared determinant identity'):
                verify.rational_control('wrong_J_sign', [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    def test_alternate_normalization_similarity_and_fraction_guard(self):
        coefficient = sp.Matrix([[2, -1, 3], [4, 0, -2], [1, 5, 7]])
        h = coefficient.T * verify.J * coefficient * verify.J
        h0 = verify.B_INVERSE * coefficient.T * verify.B_INVERSE * coefficient
        self.assertEqual(verify.J, -2 * verify.B_INVERSE)
        self.assertEqual(verify.B_INVERSE * h * verify.B_INVERSE.inv(), 4 * h0)
        large = 10 ** 30
        self.assertEqual(verify.determinant_fraction([[large, large + 1], [large + 1, large + 2]]), -1)
        self.assertEqual(verify.determinant_fraction([[large, large + 1], [2 * large, 2 * large + 2]]), 0)

    def test_odd_prime_controls_include_invariant_only_rank_loss(self):
        controls = self.saved['odd_prime_controls']
        self.assertEqual(Counter(record['prime'] for record in controls), {3: 6, 5: 6, 7: 6})
        for record in controls:
            prime = record['prime']
            self.assertEqual(record['cleared_rhs_mod_prime'] * pow(2048, -1, prime) % prime,
                             record['det_R_mod_prime'])
            self.assertEqual(record['alternate_det_R_mod_prime'], record['det_R_mod_prime'])
        special = next(record for record in controls
                       if record['prime'] == 7 and record['label'] == 'invariant_factor_zero_mod_seven')
        self.assertEqual(verify.determinant_modulo(special['M'], 7), 3)
        self.assertEqual(special['det_R_mod_prime'], 0)

    def test_characteristic_two_cleared_identity_is_not_rank_criterion(self):
        boundary = self.saved['characteristic_two_boundary']
        self.assertEqual(verify.determinant_fraction(verify.literal_source(boundary['M'])), -1)
        self.assertEqual(boundary['det_R_mod_two'], 1)
        self.assertEqual(boundary['literal_rank_mod_two'], 15)
        self.assertEqual(boundary['cleared_left_mod_two'], 0)
        self.assertEqual(boundary['cleared_right_mod_two'], 0)
        self.assertFalse(boundary['cleared_identity_is_rank_criterion'])

    def test_source_pins(self):
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        self.assertTrue(sources['local_dependencies'])
        for item in sources['local_dependencies']:
            with self.subTest(path=item['path']):
                self.assertEqual(hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest(),
                                 item['sha256'])

    def test_rational_three_space_normalization_preserves_integer_sums(self):
        controls = self.saved['rational_three_space_controls']
        self.assertEqual([item['denominator_multiplier'] for item in controls], [1, 30, 1])
        self.assertEqual([item['removed_common_power_two'] for item in controls], [1, 1, 2])
        self.assertEqual([item['normalized_parameters'] for item in controls], [[1, 1, 0], [15, 10, 6], [1, 2, 3]])
        self.assertEqual([item['reduction_mask'] for item in controls], [250, 84, 355])
        self.assertEqual(controls[0]['normalized_M'][2][0], 2)  # Integer sum, not binary XOR.
        for item in controls:
            determinant = verify.determinant_fraction(verify.literal_source(item['normalized_M']))
            self.assertEqual(str(determinant), item['normalized_det_R'])
            self.assertEqual(determinant.denominator, 1)
            self.assertEqual(determinant.numerator % 2, 1)
            self.assertNotEqual(Fraction(item['det_R']), 0)
        with self.assertRaisesRegex(ValueError, 'must be nonzero'):
            verify.rational_three_space_control((0, 0, 0))

    def test_curvature_certificates_cover_gradient_and_ternary_hessian(self):
        certificates = self.saved['curvature_certificates']
        self.assertEqual(self.saved['curvature_certificate_count'], 5)
        self.assertEqual([item['prime'] for item in certificates], [None, None, 3, 5, 7])
        self.assertEqual(sum(item['gradient_direction_count'] for item in certificates), 45)
        self.assertEqual(sum(item['vertical_direction_count'] for item in certificates), 30)
        for item in certificates:
            prime = item['prime']
            scalar = (lambda value: verify.rational_modulo(value, prime)) if prime else sp.cancel
            a = sp.Matrix(item['A'])
            hessian = sp.Matrix(item['vertical_Hessian'])
            self.assertEqual(hessian, (-2 * a).applyfunc(scalar))
            self.assertNotEqual(hessian, (2 * a).applyfunc(scalar))
            self.assertNotEqual(scalar(hessian.det()), 0)
            self.assertEqual(scalar(sp.trace(a)), 0)
        with self.assertRaisesRegex(ValueError, 'characteristic different from two'):
            verify.curvature_control('excluded_characteristic', sp.eye(3), 2)

    def test_curvature_nonsemisimple_gram_requires_no_diagonalization(self):
        item = next(record for record in self.saved['curvature_certificates'] if record['prime'] == 5)
        h = sp.Matrix(item['H'])
        reduce = lambda matrix: matrix.applyfunc(lambda value: value % 5)
        # Characteristic polynomial (t-1)(t-2)^2; the eigenvalue two has
        # a one-dimensional eigenspace and a genuine size-two Jordan block.
        self.assertEqual([value % 5 for value in h.charpoly().all_coeffs()], [1, 0, 3, 1])
        repeated = h - 2 * sp.eye(3)
        self.assertEqual(repeated.det() % 5, 0)
        self.assertNotEqual(reduce(repeated.adjugate()), sp.zeros(3))
        self.assertNotEqual(reduce((h - sp.eye(3)) * repeated), sp.zeros(3))
        self.assertEqual(reduce((h - sp.eye(3)) * repeated ** 2), sp.zeros(3))

    def test_corrupt_skew_direction_is_rejected(self):
        original = verify.cross_matrix

        def corrupt(vector):
            matrix = original(vector)
            matrix[1, 0] = -matrix[1, 0]
            return matrix

        with patch.object(verify, 'cross_matrix', side_effect=corrupt):
            with self.assertRaisesRegex(ArithmeticError, 'vertical (first derivative|Hessian)'):
                verify.curvature_control('broken_skew_sign', [[1, 0, 1], [1, 0, -1], [0, 1, 1]], 3)

    def test_integer_T_sign_error_is_detected_before_mod_two_reduction(self):
        original = verify.degree_four_T

        def corrupt(entries):
            a, b, _, _, _, _, _, h, i = entries
            return original(entries) + 2*a*b*h*i  # Flip the sign of -abhi.

        entries = sp.symbols('a b c d e f g h i')
        self.assertTrue(sp.Poly(corrupt(entries)-original(entries), *entries, modulus=2).is_zero)
        with patch.object(verify, 'degree_four_T', side_effect=corrupt):
            with self.assertRaisesRegex(ArithmeticError, 'degree-four T identity'):
                verify.characteristic_two_symbolic()

    def test_characteristic_two_affine_boundary_over_F4(self):
        # Check the table independently by polynomial multiplication modulo
        # alpha^2+alpha+1, including elements outside the prime field.
        for a in range(4):
            for b in range(4):
                product = (a if b & 1 else 0) ^ (a << 1 if b & 2 else 0)
                if product & 4:
                    product ^= 7
                self.assertEqual(verify.GF4_PRODUCT[a][b], product)
        controls = self.saved['characteristic_two_field_controls']
        self.assertEqual(len(controls['binary_affine_controls']), 4)
        self.assertEqual([record['det_R'] for record in controls['binary_affine_controls']], [0, 0, 0, 0])
        self.assertEqual([record['det_R'] for record in controls['gf4_controls']], [3, 3, 0, 0])
        self.assertEqual([record['transpose'] for record in controls['gf4_controls']], [False, True, False, True])
        self.assertEqual(controls['gf4_controls'][0]['M'], [[2, 1, 0], [0, 1, 0], [0, 1, 1]])
        self.assertEqual(verify.determinant_gf4([[2, 1], [1, 3]]), 0)
        self.assertEqual(verify.determinant_gf4([[2, 1], [0, 3]]), 1)


if __name__ == '__main__':
    unittest.main()

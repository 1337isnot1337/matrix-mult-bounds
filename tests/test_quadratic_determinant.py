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


if __name__ == '__main__':
    unittest.main()

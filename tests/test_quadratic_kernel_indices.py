"""Exact source-rank checks for the quadratic recurrence kernel theorem."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-quadratic-kernel-indices'
SPEC = importlib.util.spec_from_file_location('quadratic_kernel_indices', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class QuadraticKernelIndicesTests(unittest.TestCase):
    def test_complete_finite_report(self):
        saved = json.loads((ROOT / 'results/quadratic-kernel-indices-2026-10-23/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        binary = saved['complete_binary']
        self.assertEqual(binary['triples'], 574)
        self.assertEqual(binary['source_maps'], 1722)
        self.assertEqual(binary['fixed_root_criterion_cases'], 504)
        self.assertEqual(sum(binary['index_histogram'].values()), 574)
        self.assertEqual(binary['minimum_kernel_hankel_ranks'], {'1': 144, '2': 360})
        self.assertEqual(binary['strictly_low_index_cases'], 144)
        self.assertEqual(binary['hankel_left_right_nullity_checks'], 1440)
        for field in ('F3', 'F5'):
            self.assertEqual(saved['deterministic_samples']['fields'][field]['source_maps'], 96)
        self.assertEqual(saved['named_source_maps'], 96)
        self.assertEqual(saved['structural_source_maps'], 24)
        self.assertEqual(saved['universal_spectrum_controls']['source_maps'], 16)
        for spectrum in saved['a3_b3_observed_rank_spectra'].values():
            self.assertEqual(spectrum, [9, 12, 14, 15])
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_common_factor_does_not_change_indices_or_source_rank(self):
        primitive = [[1], [0, 1], [1, 1]]
        multiple = [[1, 1], [0, 1, 1], [1, 2, 1]]
        for prime in (None, 2, 3, 5):
            with self.subTest(prime=prime):
                left = verify.check_triple(4, primitive, prime)
                right = verify.check_triple(4, multiple, prime)
                self.assertEqual(left['minimal_indices'], right['minimal_indices'])
                self.assertEqual(left['source_ranks'], right['source_ranks'])
                self.assertEqual(right['primitive_degree'], 1)
                self.assertEqual(right['gcd_degree'], 1)
                constant = verify.check_triple(3, [[0, 0, 1], [0, 0, 2], [0, 0, 1]], prime)
                self.assertEqual(constant['minimal_indices'], [0, 0])
                self.assertEqual(constant['primitive_degree'], 0)
                self.assertEqual(constant['gcd_degree'], 2)
                self.assertEqual(constant['source_ranks'], {'3': 9, '4': 12, '5': 15})

    def test_missing_endpoints_and_constant_triples(self):
        for triple in ([[], [0, 1], [1]], [[1], [0, 1], []]):
            result = verify.check_triple(3, triple, 2)
            self.assertEqual(result['minimal_indices'], [0, 3])
            self.assertEqual(result['source_ranks'], {'3': 12, '4': 15, '5': 18})
            self.assertTrue(result['fixed_roots'])
        for triple in ([[1], [], []], [[], [1], []], [[], [], [1]]):
            result = verify.check_triple(3, triple, 2)
            self.assertEqual(result['minimal_indices'], [0, 0])
            self.assertEqual(result['source_ranks'], {'3': 9, '4': 12, '5': 15})
        with self.assertRaisesRegex(ValueError, 'must be nonzero'):
            verify.minimal_indices(3, [[0], [], [0, 0]], 2)

    def test_pr216_splittings_and_full_kernel_dimensions(self):
        unbalanced = [[0, 0, 1], [1, 0, 1], [1, 0, 2]]
        balanced = [[0, 0, 1], [1, 0, 1], [1, 1, 1]]
        for prime in (None, 3, 5):
            for triple, indices, source_rank in (
                    (unbalanced, [2, 4], 14), (balanced, [3, 3], 15)):
                with self.subTest(prime=prime, indices=indices):
                    result = verify.check_triple(3, triple, prime, b_values=(3,))
                    self.assertEqual(result['minimal_indices'], indices)
                    self.assertEqual(result['source_ranks']['3'], source_rank)
                    primitive, _ = verify.primitive_triple(triple, prime)
                    for degree in range(6):
                        nullity = 5 * (degree + 1) - verify.rank(
                            verify.recurrence_matrix(3, primitive, degree), prime)
                        expected = sum(max(degree + 1 - index, 0) for index in indices)
                        self.assertEqual(nullity, expected)
        result = verify.check_triple(3, unbalanced, 2, b_values=(3, 7))
        self.assertEqual(result['minimal_indices'], [0, 6])
        self.assertEqual(result['source_ranks'], {'3': 12, '7': 27})
        self.assertEqual(result['fixed_roots'], [[1, 1]])
        self.assertEqual(verify.minimal_indices(3, balanced, 2)['minimal_indices'], [3, 3])

    def test_literal_source_coefficient_corruption_is_detected(self):
        triple = [[1], [], []]
        matrix = verify.source_matrix(2, 3, triple)
        self.assertEqual(verify.rank(matrix, 2), 6)
        # [j=0,L=2; H=3,r=0] is outside the constant polynomial's support.
        # Both its row and column are zero, so this adds an independent pivot.
        self.assertEqual(matrix[2][6], 0)
        matrix[2][6] = 1
        with patch.object(verify, 'source_matrix', return_value=matrix):
            with self.assertRaisesRegex(ArithmeticError, 'source rank mismatch'):
                verify.check_triple(2, triple, 2, b_values=(3,))

    def test_hankel_left_and_right_kernel_indices(self):
        # An explicit rank-two minimum vector for x^3 + z^2 at a=5.
        sequence = [[], [1], [], [0, 0, 0, -1], [], [0] * 6 + [1], []]
        hankel = [sequence[r:r + 3] for r in range(5)]
        transpose = [list(row) for row in zip(*hankel)]
        for prime in (None, 2, 3, 5):
            for bound, left_expected, right_expected in ((2, 0, 0), (3, 3, 1), (4, 6, 2)):
                with self.subTest(prime=prime, bound=bound):
                    left = 5 * (bound + 1) - verify.rank(
                        verify.polynomial_matrix_coefficients(transpose, bound), prime)
                    right = 3 * (bound + 1) - verify.rank(
                        verify.polynomial_matrix_coefficients(hankel, bound), prime)
                    self.assertEqual(left, left_expected)
                    self.assertEqual(right, right_expected)

    def test_irreducible_saturation_and_nonconstant_low_branch(self):
        records = verify.structural_controls()
        self.assertEqual(len(records), 12)
        for record in records:
            witness = record['kernel_witness']
            if record['name'] == 'odd_valuation_irreducible':
                self.assertEqual(witness['hankel_rank'], 2)
                self.assertEqual(witness['degree'], witness['rank_two_lower_bound'])
                if record['a'] == 2:
                    self.assertEqual(witness['left_nullities'], {'0': 0, '1': 0})
            else:
                self.assertEqual(record['minimal_indices'], [6, 14])
                self.assertEqual(witness['hankel_rank'], 1)
                self.assertEqual(witness['root_height'], 1)
                self.assertEqual(witness['rank_two_lower_bound'], 8)
                self.assertEqual(record['constant_coefficient_span_rank'], 3)
                self.assertEqual(record['source_ranks'], {'3': 21, '7': 48})

    def test_corrupt_minimum_kernel_witness_is_rejected(self):
        triple = [[0, 0, 0, 1], [], [1]]
        matrix = verify.recurrence_matrix(5, triple, 6)
        vector = verify.kernel_vector(matrix, 2)
        vector[0] ^= 1
        with patch.object(verify, 'kernel_vector', return_value=vector):
            with self.assertRaisesRegex(ArithmeticError, 'fails the recurrence'):
                verify.inspect_kernel(5, triple, 2)

    def test_universal_three_by_three_spectrum_and_integer_blocks(self):
        controls = verify.spectrum_controls()
        self.assertEqual(controls['source_maps'], 16)
        for field in ('Q', 'F2', 'F3', 'F5'):
            self.assertEqual([row['ranks'][field] for row in controls['witnesses']],
                             [9, 12, 14, 15])
        certificate = controls['rank_fifteen_integer_certificate']
        self.assertTrue(certificate['zero_off_block'])
        self.assertEqual(certificate['determinant'], -1)
        self.assertEqual([block['determinant'] for block in certificate['blocks']],
                         [1, 1, 1, -1, 1, 1, 1])
        self.assertEqual([len(block['matrix']) for block in certificate['blocks']],
                         [1, 2, 3, 3, 3, 2, 1])

    def test_pinned_source_bytes(self):
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        self.assertTrue(sources['local_dependencies'])
        for item in sources['local_dependencies']:
            with self.subTest(path=item['path']):
                self.assertEqual(hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest(),
                                 item['sha256'])


if __name__ == '__main__':
    unittest.main()

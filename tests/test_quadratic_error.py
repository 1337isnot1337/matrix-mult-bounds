"""Exact full-error invariants, polynomial families, and Laurent-pole controls."""
import copy
from fractions import Fraction as Q
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest


PACKAGE = Path(__file__).resolve().parents[1] / 'research/ai/2026-10-23-quadratic-error'
SPEC = importlib.util.spec_from_file_location('quadratic_error_replay', PACKAGE / 'verify.py')
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)
I = V.I


class QuadraticErrorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((PACKAGE / 'certificate.json').read_text())
        cls.sources = V.load_sources()

    def test_all_coordinates_and_target_reshape(self):
        dims = (4, 5, 5)
        for coordinate in product(range(20), range(25), range(20)):
            self.assertEqual(I.involution(I.involution(coordinate, dims), dims), coordinate)
        target = I.target(dims)
        self.assertEqual(I.reshape(target, dims), {(i, i): Q(1) for i in range(100)})
        self.assertEqual(I.quadratic(target, dims), 100)
        self.assertEqual(I.trace_power(target, 3, dims), 100)
        tensor = {(0, 0, 0): Q(7, 3), (3, 12, 4): Q(-2), (19, 24, 19): Q(5)}
        self.assertEqual(I.pairing(target, tensor, dims), I.trace_tensor(tensor, dims))
        self.assertEqual(I.pairing(tensor, target, dims), I.trace_tensor(tensor, dims))
        self.assertEqual(I.quadratic(tensor, dims), I.trace_power(tensor, 2, dims))

    def test_quadratic_zero_does_not_imply_contraction(self):
        # Reshape to a three-cycle permutation matrix.  Its first two power
        # traces vanish, but the cubic is three, so quadratic zero is not enough.
        dims = (1, 1, 3)
        tensor = {(0, j, i): Q(1) for i, j in ((0, 1), (1, 2), (2, 0))}
        self.assertEqual(I.trace_tensor(tensor, dims), 0)
        self.assertEqual(I.quadratic(tensor, dims), 0)
        self.assertEqual(I.trace_power(tensor, 3, dims), 3)

    def test_physical_action_is_exact_conjugation(self):
        dims = (2, 2, 2)
        physical = [[[Q(2), Q(1)], [Q(0), Q(1)]],
                    [[Q(1), Q(0)], [Q(1), Q(3)]],
                    [[Q(1), Q(2)], [Q(0), Q(-1)]]]
        inverses = [V.inverse(matrix) for matrix in physical]
        terms = [[[Q(1), Q(-2), Q(3), Q(1)], [Q(0), Q(1), Q(2), Q(-1)],
                  [Q(1), Q(1), Q(0), Q(2)]],
                 [[Q(2), Q(0), Q(-1), Q(1)], [Q(1), Q(3), Q(0), Q(2)],
                  [Q(-1), Q(0), Q(4), Q(1)]]]
        transformed = []
        for term in terms:
            output = []
            for leg, row in enumerate(term):
                matrix = I.matrix_product(I.matrix_product(inverses[leg], I.matrix(row, 2, 2)),
                                          physical[(leg+1) % 3])
                output.append([entry for values in matrix for entry in values])
            transformed.append(output)
        original = I.tensor_from_factors(terms, dims)
        moved = I.tensor_from_factors(transformed, dims)
        self.assertEqual(I.quadratic(original, dims), I.quadratic(moved, dims))
        self.assertEqual(I.trace_power(original, 3, dims), I.trace_power(moved, 3, dims))
        self.assertEqual(I.quadratic(original, dims),
                         sum(I.factor_pairing(a, b, dims) for a in terms for b in terms))
        indices = list(product(range(2), repeat=3))
        def kron(matrices):
            return [[matrices[0][i[0]][j[0]] * matrices[1][i[1]][j[1]]
                     * matrices[2][i[2]][j[2]] for j in indices] for i in indices]
        sparse = I.reshape(original, dims)
        dense = [[sparse.get((i, j), Q(0)) for j in range(8)] for i in range(8)]
        conjugate = I.matrix_product(I.matrix_product(kron(inverses), dense), kron(physical))
        self.assertEqual(I.reshape(moved, dims),
                         {(i, j): value for i, row in enumerate(conjugate)
                          for j, value in enumerate(row) if value})
        # Each term gauge has product one and leaves the tensor unchanged.
        gauged = [[V.scale(term[0], Q(-2)), V.scale(term[1], Q(3)),
                   V.scale(term[2], Q(-1, 6))] for term in terms]
        self.assertEqual(I.tensor_from_factors(gauged, dims), original)

    def test_complete_uniform_family_and_block_replay(self):
        result = V.verify(self.certificate)
        self.assertEqual(result['full_error_quadratics'], ['2', '2', '2'])
        self.assertEqual(result['full_family_coefficient_positions_checked'], 90000)
        self.assertTrue(result['arbitrary_Laurent_parameters_included'])
        self.assertFalse(result['all_refactorizations_excluded'])
        block = self.certificate['ten_block']
        self.assertEqual(block['V_flattening_rank'], 5)
        self.assertEqual(block['full_error_quadratic_in_tau'], ['2', '-2', '1'])
        for family in self.certificate['families']:
            checks = family['checks']
            self.assertEqual(checks['surviving_terms'], 75)
            self.assertEqual(checks['deleted_term_quadratic'], '0')
            self.assertEqual(checks['full_error_quadratic'], '2')
            self.assertTrue(checks['deleted_cyclic_product_square_zero'])

    def test_full_old_error_is_essential(self):
        for name in V.FAMILIES:
            data = V.family_data(name, self.sources)
            old = I.polynomial_tensor([V.constant_family(term) for term in data['discarded']], V.DIMS)
            deleted = I.polynomial_tensor([data['deleted']], V.DIMS)
            self.assertEqual(I.polynomial_pairing(deleted, deleted, V.DIMS), {})
            self.assertEqual(I.polynomial_pairing(old, deleted, V.DIMS), {0: Q(1)})
            error = V.polynomial_sum(old, deleted)
            self.assertEqual(I.polynomial_pairing(error, error, V.DIMS), {0: Q(2)})

    def test_minimum_block_control_with_laurent_poles(self):
        data = V.family_data(V.FAMILIES[0], self.sources)
        u, v, w = data['surviving'][61]
        other_u, other_v, _ = data['surviving'][62]
        # A two-term refactorization with s=epsilon^-1, q=-1/3+epsilon.
        # The selected term has trace 3epsilon, although factors have poles.
        deleted_factors = ({0: u, -1: V.scale(other_u, -1)},
                           {-1: V.scale(v, Q(1, 3)), 0: V.scale(other_v, Q(-1, 3)), 1: other_v},
                           {0: w})
        kept_factors = ({-1: V.scale(other_u, Q(1, 3)), 0: V.scale(u, Q(-1, 3)), 1: u},
                        {-1: v, 0: V.scale(other_v, -1)}, {0: w})
        def expand(factors):
            output = {}
            for choices in product(*(factor.items() for factor in factors)):
                degree = sum(i for i, _ in choices)
                tensor = I.tensor_from_factors([[row for _, row in choices]], V.DIMS)
                output[degree] = I.add_tensors(output.get(degree, {}), tensor)
            return {degree: tensor for degree, tensor in output.items() if tensor}
        deleted, kept = expand(deleted_factors), expand(kept_factors)
        pair = I.tensor_from_factors([data['surviving'][i] for i in (61, 62)], V.DIMS)
        self.assertEqual(V.polynomial_sum(deleted, kept), {0: pair})
        old = I.polynomial_tensor([V.constant_family(term) for term in data['discarded']], V.DIMS)
        error = V.polynomial_sum(old, deleted)
        linear = {degree: value for degree, tensor in error.items()
                  if (value := I.trace_tensor(tensor, V.DIMS))}
        self.assertEqual(linear, {1: Q(3)})
        self.assertEqual(I.polynomial_pairing(error, error, V.DIMS),
                         {0: Q(2), 1: Q(-6), 2: Q(9)})
        self.assertTrue(any(degree < 0 for degree in deleted))

    def test_certificate_scope_factor_and_block_mutations(self):
        for key in ('schema', 'claim_id', 'scope', 'source_pins'):
            changed = copy.deepcopy(self.certificate)
            changed[key] = 'changed'
            with self.subTest(field=key), self.assertRaises(ValueError):
                V.verify(changed)
        changed = copy.deepcopy(self.certificate)
        changed['families'][0]['deleted_factor_coefficients'][0][0][0] = '7'
        with self.assertRaisesRegex(ValueError, 'certificate differs'):
            V.verify(changed)
        changed = copy.deepcopy(self.certificate)
        changed['ten_block']['J_full_old_error_pairing'][2][3] = '-2'
        with self.assertRaisesRegex(ValueError, 'certificate differs'):
            V.verify(changed)
        changed = copy.deepcopy(self.certificate)
        changed['families'][1]['checks']['full_error_quadratic'] = '0'
        with self.assertRaisesRegex(ValueError, 'certificate differs'):
            V.verify(changed)

    def test_strict_exact_coefficient_and_shape_controls(self):
        for value in ('0.5', '1/0', '2/2', '-0', '1e6', '__import__("os")', 1, True):
            with self.subTest(value=value), self.assertRaises(ValueError):
                V.parse_rational(value)
        for dims in ((True, 5, 5), (4.0, 5, 5), (4, 0, 5), (4, 5)):
            with self.subTest(dimensions=dims), self.assertRaises(ValueError):
                I.target(dims)
        for tensor in ({(20, 0, 0): Q(1)}, {(0, 0, 0): .5}, {(0, 0, 0): True}):
            with self.assertRaises(ValueError):
                I.quadratic(tensor, V.DIMS)
        changed = copy.deepcopy(self.certificate)
        changed['families'][0]['deleted_factor_coefficients'][0][0].pop()
        with self.assertRaisesRegex(ValueError, 'shape'):
            V.verify(changed)
        with self.assertRaises(ValueError):
            I.trace_power({}, 0, V.DIMS)
        with self.assertRaises(ValueError):
            I.polynomial_pairing({'1': {}}, {}, V.DIMS)


if __name__ == '__main__':
    unittest.main()

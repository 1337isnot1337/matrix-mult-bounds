"""Exact checks of supplied rational witnesses, with all source endpoints."""
from copy import deepcopy
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-quadratic-rational-attainment'
RESULTS = ROOT / 'results/quadratic-rational-attainment-2026-10-23'
SPEC = importlib.util.spec_from_file_location('quadratic_rational_attainment', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class QuadraticRationalAttainmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads((RESULTS / 'controls.json').read_text())

    def test_complete_saved_report_and_bounded_source_controls(self):
        self.assertEqual(verify.report(), self.saved)
        self.assertEqual(self.saved['recurrence_matrices_checked'], 4)
        self.assertEqual(self.saved['polynomial_equations_checked'], 13)
        self.assertEqual(self.saved['literal_source_matrices_checked'], 10)
        expected = {2: [(3, 14), (4, 24)], 3: [(4, 24), (5, 34), (8, 79)],
                    5: [(4, 23), (5, 35), (9, 98)], 7: [(6, 47), (7, 63)]}
        for record in self.saved['records']:
            self.assertEqual(record['recurrence_size'] - record['recurrence_rank'], 1)
            self.assertEqual([(item['a'], item['literal_rank']) for item in record['source_controls']],
                             expected[record['order']])
            self.assertTrue(any(item['multiple_of_order'] for item in record['source_controls']))
            self.assertTrue(any(not item['multiple_of_order'] for item in record['source_controls']))
            for item in record['source_controls']:
                self.assertEqual(item['matrix_size'], item['a'] * (2 * item['a'] - 1))
        self.assertFalse(self.saved['independent_review'])
        self.assertFalse(self.saved['improves_omega'])

    def test_supplied_integer_witnesses_preserved(self):
        original = json.loads((RESULTS / 'discovery-prime-witnesses.json').read_text())
        original_five = next(record for record in original['records'] if record['n'] == 5)
        original_seven = json.loads((RESULTS / 'discovery-order7-small.json').read_text())
        current = {record['order']: record for record in self.saved['records']}
        self.assertEqual(current[5]['triple'], original_five['triple'])
        self.assertEqual(current[5]['kernel_polynomials'],
                         [[int(value) for value in poly] for poly in original_five['kernel_polynomials']])
        self.assertEqual(current[7]['triple'], original_seven['triple'])
        self.assertEqual(current[7]['kernel_polynomials'], original_seven['integer_kernel_polynomials'])
        self.assertTrue(all(isinstance(value, int) for record in current.values()
                            for poly in record['kernel_polynomials'] for value in poly))

    def test_convolution_and_matrix_coordinates_agree_at_every_endpoint(self):
        for record in self.saved['records']:
            n, triple, polynomials = record['order'], record['triple'], record['kernel_polynomials']
            verify.check_witness(n, triple, polynomials)
            vector = [value for poly in polynomials for value in poly + [0] * (n - 1 - len(poly))]
            matrix = verify.recurrence_matrix(n, triple)
            self.assertEqual(len(matrix), n * n - 1)
            self.assertEqual(len(vector), n * n - 1)
            self.assertTrue(all(len(row) == len(vector) for row in matrix))
            self.assertEqual([sum(entry * value for entry, value in zip(row, vector)) for row in matrix],
                             [0] * (n * n - 1))

    def test_first_and_last_recurrence_corruptions_rejected(self):
        record = next(item for item in self.saved['records'] if item['order'] == 7)
        for coordinate, equation in ((0, 0), (7, 5)):
            broken = deepcopy(record['kernel_polynomials'])
            broken[coordinate][0] += 1
            with self.assertRaisesRegex(ArithmeticError, f'equation {equation}'):
                verify.check_witness(7, record['triple'], broken)
        with self.assertRaisesRegex(ArithmeticError, 'coordinate count or degree'):
            verify.check_witness(7, record['triple'], record['kernel_polynomials'][:-1])
        with self.assertRaisesRegex(ArithmeticError, 'must be nonzero'):
            verify.check_witness(7, record['triple'], [[] for _ in range(8)])

    def test_small_auxiliary_certificates_are_not_invalid_source_claims(self):
        for record in self.saved['records'][:2]:
            self.assertEqual(record['recurrence_size'], {2: 3, 3: 8}[record['order']])
            with self.assertRaisesRegex(ValueError, 'a>=3'):
                verify.source_matrix(record['order'] - 1, record['triple'])
        self.assertEqual(self.saved['records'][1]['kernel_polynomials'], [[], [1], [0, -1], []])

    def test_fraction_elimination_guards_integer_inputs(self):
        large = 10 ** 30
        self.assertEqual(verify.rank_rational([[large, large + 1], [large + 1, large + 2]]), 2)
        self.assertEqual(verify.rank_rational([[large, large + 1], [2 * large, 2 * large + 2]]), 1)
        self.assertEqual(verify.rank_rational([[Fraction(1, 3), Fraction(1, 2)],
                                              [Fraction(2, 3), 1]]), 1)

    def test_integer_identity_survives_but_order_seven_hypotheses_fail_mod_two(self):
        for record in self.saved['records']:
            self.assertTrue(any(abs(value) == 1 for poly in record['kernel_polynomials'] for value in poly))
        seven = next(record for record in self.saved['records'] if record['order'] == 7)
        reduced = [[value % 2 for value in poly] for poly in seven['triple']]
        witness = [[value % 2 for value in poly] for poly in seven['kernel_polynomials']]
        self.assertEqual(reduced, [[1, 1], [1, 1], [0, 0, 0]])
        self.assertEqual(witness[-1], [1, 0, 1, 0, 0, 0])
        verify.check_witness(7, reduced, witness)
        # q7 mod2=(1+x)(1+z); after removing 1+x its primitive degree is zero.
        boundary = self.saved['order_seven_characteristic_two_boundary']
        self.assertEqual(boundary['reduced_triple'], reduced)
        self.assertEqual(boundary['common_factor'], [1, 1])
        self.assertEqual(boundary['primitive_degree'], 0)
        self.assertFalse(boundary['order_claim'])
        # One small actual binary source also distinguishes this rank-nine
        # stratum from the invalid order-seven/full-active-rank prediction.
        pivots = {}
        for entries in verify.source_matrix(3, reduced):
            row = sum(value << index for index, value in enumerate(entries))
            while row:
                pivot = row.bit_length() - 1
                if pivot not in pivots:
                    pivots[pivot] = row
                    break
                row ^= pivots[pivot]
        self.assertEqual(len(pivots), 9)

    def test_source_pins(self):
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        self.assertTrue(sources['local_dependencies'])
        for item in sources['local_dependencies']:
            with self.subTest(path=item['path']):
                self.assertEqual(hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest(),
                                 item['sha256'])


if __name__ == '__main__':
    unittest.main()

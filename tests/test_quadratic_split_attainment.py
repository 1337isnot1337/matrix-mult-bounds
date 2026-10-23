"""Finite exact checks for split/doubled quadratic source attainment."""
from collections import Counter
from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-quadratic-split-attainment'
SPEC = importlib.util.spec_from_file_location('quadratic_split_attainment', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


def restrict_f4(matrix):
    """Multiplication by a+b*alpha on the independent binary basis (1,alpha)."""
    result = []
    for row in matrix:
        result.append([entry for value in row for entry in (value & 1, value >> 1)])
        result.append([entry for value in row
                       for entry in (value >> 1, (value & 1) ^ (value >> 1))])
    return result


class QuadraticSplitAttainmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads((ROOT / 'results/quadratic-split-attainment-2026-10-23/controls.json').read_text())

    def test_complete_finite_report_and_rectangular_clipping(self):
        self.assertEqual(verify.report(), self.saved)
        self.assertEqual(self.saved['recurrence_controls'], 29)
        self.assertEqual(self.saved['source_controls'], 78)
        self.assertEqual(self.saved['kernel_witnesses'], 13)
        self.assertEqual(self.saved['field_case_counts'], {'Q': 7, 'F2': 4, 'F3': 4, 'F5': 6, 'F4': 8})
        comparisons = Counter()
        for control in self.saved['controls']:
            a = control['a']
            for source in control['source_controls']:
                b = source['b']
                comparisons[(b > a) - (b < a)] += 1
                self.assertEqual(source['rows'], b * (a + b - 1))
                self.assertEqual(source['columns'], a * (a + b - 1))
                self.assertEqual(a * b + 2 * min(a, b) - source['literal_rank'],
                                 control['epsilon'] if a == b else 0)
        self.assertEqual(comparisons, {-1: 20, 0: 29, 1: 29})
        self.assertEqual(len(self.saved['excluded_zero_parameter_controls']), 5)
        self.assertTrue(all(item['literal_rank'] == 12
                            for item in self.saved['excluded_zero_parameter_controls']))
        self.assertFalse(self.saved['independent_review'])
        self.assertFalse(self.saved['improves_omega'])

    def test_exact_witnesses_and_geometric_sum_identity(self):
        for name, cases in verify.CASES.items():
            field = verify.FIELDS[name]
            for parameter, a in cases:
                t = field.element(parameter)
                sums = verify.geometric_sums(field, t, a + 1)
                for r in range(2, a + 2):
                    self.assertEqual(field.sub(field.mul(sums[r - 1], sums[r - 1]),
                                               field.mul(sums[r], sums[r - 2])), field.power(t, r - 2))
                if verify.predicted_nullity(a, field, parameter):
                    witness = verify.kernel_witness(a, field, parameter)
                    verify.check_kernel(a, verify.split_triple(field, parameter), witness, field)
                    self.assertEqual(max(map(len, witness)), a)
        self.assertEqual(verify.kernel_witness(3, verify.FIELDS['Q'], -1),
                         [[], [1], [], [0, 0, 1], []])
        self.assertEqual(verify.kernel_witness(5, verify.FIELDS['F4'], 2),
                         [[], [1], [0, 3], [], [0, 0, 0, 1], [0, 0, 0, 0, 3], []])

    def test_auxiliary_n2_n3_are_separate_from_source_parameters(self):
        controls = self.saved['small_auxiliary_controls']
        self.assertEqual(len(controls), 24)
        self.assertEqual(Counter(record['n'] for record in controls), {2: 12, 3: 12})
        self.assertEqual(self.saved['small_auxiliary_kernel_witnesses'], 8)
        for record in controls:
            self.assertNotIn('source_controls', record)
            self.assertEqual(record['recurrence_size'], record['n'] ** 2 - 1)
            self.assertEqual(record['recurrence_size'] - record['recurrence_rank'], record['epsilon'])
        for name, parameter, n, expected in [
                ('F2', 1, 2, [[], [1], []]),
                ('F3', 1, 3, [[], [1], [0, 2], []]),
                ('F4', 2, 3, [[], [1], [0, 3], []])]:
            self.assertEqual(verify.small_auxiliary_control(verify.FIELDS[name], parameter, n)
                             ['kernel_polynomials'], expected)
        with self.assertRaisesRegex(ValueError, 'a>=3'):
            verify.kernel_witness(2, verify.FIELDS['F4'], 2)

    def test_corrupt_witness_rejected_by_polynomial_convolution(self):
        field = verify.FIELDS['F4']
        triple = verify.split_triple(field, 2)
        witness = verify.kernel_witness(8, field, 2)
        broken = deepcopy(witness)
        broken[1][0] = 0
        with self.assertRaisesRegex(ArithmeticError, 'fails the polynomial recurrence'):
            verify.check_kernel(8, triple, broken, field)
        with self.assertRaisesRegex(ArithmeticError, 'invalid coordinate degrees'):
            verify.check_kernel(8, triple, witness[:-1], field)
        with self.assertRaisesRegex(ArithmeticError, 'must be nonzero'):
            verify.check_kernel(8, triple, [[] for _ in range(10)], field)

    def test_zero_parameter_and_invalid_source_sizes_rejected(self):
        for field in verify.FIELDS.values():
            with self.assertRaisesRegex(ValueError, 't=0'):
                verify.split_triple(field, 0)
            with self.assertRaisesRegex(ValueError, 't=0'):
                verify.predicted_rank(3, 3, field, 0)
        with self.assertRaisesRegex(ValueError, 'a>=3'):
            verify.predicted_rank(2, 3, verify.FIELDS['Q'], -1)
        with self.assertRaisesRegex(ValueError, 'b>=3'):
            verify.predicted_rank(3, 2, verify.FIELDS['Q'], -1)

    def test_repeated_parameter_is_not_the_distinct_root_condition(self):
        for name, a, expected in [('Q', 3, 0), ('Q', 4, 0), ('F2', 3, 1),
                                  ('F2', 4, 0), ('F3', 4, 0), ('F3', 5, 1),
                                  ('F5', 3, 0), ('F5', 4, 1)]:
            field = verify.FIELDS[name]
            self.assertEqual(field.power(field.element(1), a + 1), 1)
            self.assertEqual(verify.predicted_nullity(a, field, 1), expected)
        with self.assertRaisesRegex(ValueError, 'zero recurrence kernel'):
            verify.kernel_witness(4, verify.FIELDS['Q'], 1)

    def test_extension_rank_by_independent_restriction_of_scalars(self):
        extension, binary = verify.FIELDS['F4'], verify.FIELDS['F2']
        self.assertEqual(verify.predicted_nullity(8, binary, 1), 0)
        self.assertEqual(verify.predicted_nullity(8, extension, 2), 1)
        for parameter, epsilon in ((1, 0), (2, 1)):
            triple = verify.split_triple(extension, parameter)
            recurrence = verify.recurrence_matrix(8, triple)
            source = verify.source_matrix(8, 8, triple)
            self.assertEqual(verify.rank(restrict_f4(recurrence), binary), 2 * (80 - epsilon))
            self.assertEqual(verify.rank(restrict_f4(source), binary), 2 * (80 - epsilon))

    def test_rational_elimination_preserves_large_integer_differences(self):
        large = 10 ** 30
        self.assertEqual(verify.rank([[large, large + 1], [large + 1, large + 2]], verify.FIELDS['Q']), 2)
        self.assertEqual(verify.rank([[large, large + 1], [2 * large, 2 * large + 2]], verify.FIELDS['Q']), 1)

    def test_source_pins(self):
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        self.assertTrue(sources['local_dependencies'])
        for item in sources['local_dependencies']:
            with self.subTest(path=item['path']):
                self.assertEqual(hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest(),
                                 item['sha256'])


if __name__ == '__main__':
    unittest.main()

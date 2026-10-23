"""Exact finite orbit and cohomology controls for binary quadratic torsion."""
from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-quadratic-torsion'
SPEC = importlib.util.spec_from_file_location('quadratic_torsion', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


def evaluate(coefficients, x, z):
    return sum(coefficients[3 * k + i] * x[0] ** (2 - i) * x[1] ** i *
               z[0] ** (2 - k) * z[1] ** k for k in range(3) for i in range(3)) % 2


def apply_matrix(matrix, point):
    a, b, c, d = matrix
    return ((a * point[0] + b * point[1]) % 2,
            (c * point[0] + d * point[1]) % 2)


class QuadraticTorsionTests(unittest.TestCase):
    def test_complete_saved_orbits_and_profiles(self):
        saved = json.loads((ROOT / 'results/quadratic-torsion-2026-10-23/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertEqual(saved['candidate_count'], 264)
        self.assertEqual(saved['orbit_count'], 16)
        self.assertEqual(saved['representative_transforms_checked'], 576)
        self.assertEqual(saved['literal_source_comparisons'], 176)
        self.assertEqual(saved['additional_small_cohomology_matrices'], 32)
        self.assertEqual(saved['first_nonzero_power_counts']['orbits'], {'2': 9, '3': 4, '4': 2, '5': 1})
        self.assertEqual(saved['first_nonzero_power_counts']['candidate_triples'],
                         {'2': 96, '3': 96, '4': 36, '5': 36})
        self.assertEqual(saved['previous_sizes_not_recomputed'], [6, 10])
        self.assertFalse({6, 10} & set(saved['source_sizes']))
        members = [tuple(member) for orbit in saved['orbits'] for member in orbit['members']]
        self.assertEqual(len(members), len(set(members)))
        self.assertEqual(set(members), verify.candidates())
        self.assertFalse(saved['independent_review'])
        self.assertFalse(saved['improves_omega'])

    def test_bihomogeneous_substitution_on_every_basis_element(self):
        points = [(1, 0), (0, 1), (1, 1)]
        group = verify.projective_group()
        self.assertEqual(len(group), 6)
        # Evaluation at these three points determines a binary homogeneous quadric;
        # their nine products therefore determine every bidegree-(2,2) form.
        for monomial in range(9):
            coefficients = tuple(int(i == monomial) for i in range(9))
            for x_matrix in group:
                for z_matrix in group:
                    transformed = verify.transform(coefficients, x_matrix, z_matrix)
                    for x in points:
                        for z in points:
                            self.assertEqual(evaluate(transformed, x, z), evaluate(
                                coefficients, apply_matrix(x_matrix, x), apply_matrix(z_matrix, z)))
        with self.assertRaisesRegex(ValueError, 'invertible'):
            verify.transform((1,) + (0,) * 8, (1, 0, 0, 0), (1, 0, 0, 1))

    def test_small_powers_are_cohomology_not_invalid_source_parameters(self):
        cases = [(2, (0, 0, 1, 0, 0, 0, 1, 0, 0), [[], [1], []]),
                 (3, (0, 0, 1, 0, 1, 0, 1, 0, 0), [[], [1], [0, 1], []]),
                 (5, (0, 0, 1, 1, 0, 0, 0, 1, 1),
                  [[1, 0, 1, 1], [0, 0, 1], [0, 0, 0, 1], [0, 0, 1],
                   [0, 1, 1, 1], [1, 0, 1]])]
        for power, coefficients, expected in cases:
            with self.subTest(power=power):
                record = verify.kernel_record(power - 1, coefficients)
                self.assertEqual(record['nullity'], 1)
                self.assertEqual(record['kernel_polynomials'], expected)
                for smaller in range(2, power):
                    self.assertEqual(verify.kernel_record(smaller - 1, coefficients)['nullity'], 0)
        with self.assertRaisesRegex(ValueError, 'a>=3'):
            verify.source_control(1, cases[0][1])

    def test_corrupt_power_five_witness_is_rejected(self):
        coefficients = (0, 0, 1, 1, 0, 0, 0, 1, 1)
        record = verify.kernel_record(4, coefficients)
        matrix = verify.base.recurrence_matrix(4, verify.triple(coefficients), 3)
        broken = deepcopy(record['kernel_polynomials'])
        broken[0][0] ^= 1
        with self.assertRaisesRegex(ArithmeticError, 'does not satisfy'):
            verify.check_kernel_polynomials(matrix, 4, broken)
        with self.assertRaisesRegex(ArithmeticError, 'invalid coordinate degrees'):
            verify.check_kernel_polynomials(matrix, 4, record['kernel_polynomials'][:-1])

    def test_source_pins(self):
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        self.assertTrue(sources['local_dependencies'])
        for item in sources['local_dependencies']:
            with self.subTest(path=item['path']):
                self.assertEqual(hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest(),
                                 item['sha256'])


if __name__ == '__main__':
    unittest.main()

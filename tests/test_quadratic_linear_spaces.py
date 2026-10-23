"""Literal-matrix certificates and finite binary subspace classification."""
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-quadratic-linear-spaces'
SPEC = importlib.util.spec_from_file_location('quadratic_linear_spaces', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class QuadraticLinearSpacesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads((ROOT / 'results/quadratic-linear-spaces-2026-10-23/controls.json').read_text())

    def test_compact_upper_and_lower_certificates(self):
        certificate = verify.upper_certificate([84, 174, 311])
        self.assertEqual([item['vector'] for item in certificate['nonzero_points']],
                         [84, 174, 250, 311, 355, 409, 461])
        self.assertEqual([item['integer_determinant'] for item in certificate['nonzero_points']],
                         [-1, 7, 3, 1, 43, 1, 1])
        for point in certificate['nonzero_points']:
            self.assertEqual(verify.binary_rank(verify.source_matrix(
                verify.coefficients(point['vector']))), 15)
        points = verify.span(verify.LOWER_BASIS)
        self.assertEqual(len(set(points)), 64)
        self.assertTrue(all(vector & 7 == 0 for vector in points))
        self.assertEqual(Counter(verify.binary_rank(verify.source_matrix(verify.coefficients(vector)))
                                 for vector in points if vector), {9: 21, 12: 42})

    def test_corrupt_upper_certificate_rejected(self):
        with self.assertRaisesRegex(ArithmeticError, 'singular source'):
            verify.upper_certificate([84, 174, 1])
        with self.assertRaisesRegex(ArithmeticError, 'independent'):
            verify.upper_certificate([84, 174, 84 ^ 174])

    def test_complete_finite_classification(self):
        self.assertEqual(json.loads(json.dumps(verify.report())), self.saved)
        self.assertEqual(self.saved['nonzero_rank_histogram'], {'9': 49, '12': 198, '14': 132, '15': 132})
        census = self.saved['finite_subspace_classification']
        self.assertEqual(census['dimension_seven_spaces_checked'], 43435)
        self.assertEqual(census['dimension_six_spaces_checked'], 788035)
        cap12, cap14 = census['dimension_six_spaces']['12'], census['dimension_six_spaces']['14']
        self.assertEqual(len(cap12), 6)
        self.assertEqual(len(cap14), 20)
        self.assertTrue(all(item['compression']['normal'] in (1, 4, 7) for item in cap12))
        self.assertEqual(sum(item['compression'] is not None for item in cap14), 14)
        exceptional = [item for item in cap14 if item['compression'] is None]
        self.assertEqual(len(exceptional), 6)
        self.assertTrue(all(item['nonzero_rank_histogram'] == {'9': 15, '12': 18, '14': 30}
                            for item in exceptional))
        self.assertFalse(self.saved['independent_review'])
        self.assertFalse(self.saved['improves_omega'])

    def test_independent_walsh_dimension_seven_bounds(self):
        ranks = self.saved['literal_source_ranks_including_zero']
        for cap, expected in ((12, 32), (14, 6)):
            forbidden = [vector for vector in range(1, 512) if ranks[vector] > cap]
            transform = [sum(1 if (normal & vector).bit_count() % 2 == 0 else -1
                             for vector in forbidden) for normal in range(512)]
            checked, minimum = 0, 512
            # Each pair here is the two smallest nonzero vectors of one normal plane.
            # This enumerator is independent of the verifier's reduced-basis routine.
            for first in range(1, 512):
                for second in range(first + 1, 512):
                    if first ^ second <= second:
                        continue
                    checked += 1
                    numerator = (transform[0] + transform[first] + transform[second]
                                 + transform[first ^ second])
                    self.assertEqual(numerator % 4, 0)
                    minimum = min(minimum, numerator // 4)
            self.assertEqual(checked, 43435)
            self.assertEqual(minimum, expected)

    def test_extension_counterexample_and_binary_membership(self):
        witness = self.saved['extension_counterexample']
        values = verify.extension_coefficients(witness['parameters'])
        self.assertEqual(values, [0, 0, 1, 1, 1, 1, 0, 1, 2])
        matrix = verify.source_matrix(values)
        self.assertEqual(verify.gf4_determinant(matrix), 1)
        # Independently embed multiplication by a+b*t as [[a,b],[b,a+b]].
        # A full-rank 30x30 binary map proves the original F4 map is invertible.
        restriction = []
        for row in matrix:
            restriction.append([entry for value in row for entry in (value & 1, value >> 1)])
            restriction.append([entry for value in row
                                for entry in (value >> 1, (value & 1) ^ (value >> 1))])
        self.assertEqual(verify.binary_rank(restriction), 30)
        binary_points = verify.span(witness['binary_family_basis'])
        ranks = self.saved['literal_source_ranks_including_zero']
        self.assertEqual(Counter(ranks[vector] for vector in binary_points if vector),
                         {9: 15, 12: 18, 14: 30})
        for scalar in (0, 1):
            parameters = witness['parameters'][:-1] + [scalar]
            self.assertEqual(verify.gf4_determinant(verify.source_matrix(
                verify.extension_coefficients(parameters))), 0)

    def test_source_pins(self):
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        self.assertTrue(sources['local_dependencies'])
        for item in sources['local_dependencies']:
            with self.subTest(path=item['path']):
                self.assertEqual(hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest(),
                                 item['sha256'])


if __name__ == '__main__':
    unittest.main()

import copy
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-sl2-finite-slices'
RESULTS = ROOT/'results/sl2-finite-slices-2026-10-21'
spec = importlib.util.spec_from_file_location('nonsplit_finite_cover', PACKAGE/'verify_cover.py')
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class NonsplitFiniteCoversTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS/'cover-certificate.json').read_text())

    def test_original_source_and_cube_replay(self):
        report = verifier.verify(self.certificate)
        self.assertEqual(report, json.loads((RESULTS/'verification.json').read_text()))
        self.assertEqual(report['original_group_coefficients_checked'], 1728000)
        self.assertEqual(report['covers'][0]['slice_upper_bound'], 98)
        self.assertEqual(report['extra_C2_cube']['slice_upper_bound'], 6155844)
        self.assertEqual(report['extra_C2_cube']['strict_gap'], 270381)

    def test_field_laws_and_source_format(self):
        T = verifier.TABLE
        for a, b, c in product(range(4), repeat=3):
            self.assertEqual(T[T[a][b]][c], T[a][T[b][c]])
            self.assertEqual(T[a][b ^ c], T[a][b] ^ T[a][c])
        bad = copy.deepcopy(self.certificate)
        bad['coefficient_field'] = 'F5'
        with self.assertRaisesRegex(ValueError, 'field'):
            verifier.verify(bad)
        bad = copy.deepcopy(self.certificate)
        bad['basis'][0] = bad['basis'][1]
        with self.assertRaisesRegex(ValueError, 'singular'):
            verifier.verify(bad)
        bad = copy.deepcopy(self.certificate)
        high, low = bad['basis_degrees'].index(8), bad['basis_degrees'].index(0)
        bad['basis_degrees'][high], bad['basis_degrees'][low] = bad['basis_degrees'][low], bad['basis_degrees'][high]
        with self.assertRaisesRegex(ValueError, 'block degree'):
            verifier.verify(bad)

    def test_uncovered_original_coefficients_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['covers'][0]['selected_coordinates'] = [[], [], []]
        bad['covers'][0]['slice_upper_bound'] = 0
        with self.assertRaisesRegex(ValueError, 'uncovered original'):
            verifier.verify(bad)

    def test_cube_count_and_volume_corruption_are_rejected(self):
        for key in ('word_multiplicity', 'per_word_slices'):
            cube = copy.deepcopy(self.certificate['cube'])
            cube['rows'][0][key] += 1
            with self.assertRaisesRegex(ValueError, 'multiplicity|slice count'):
                verifier.verify_cube(cube, self.certificate['basis_degrees'])
        cube = copy.deepcopy(self.certificate['cube'])
        cube['rows'][0]['degree_counts'][0] += 1
        with self.assertRaisesRegex(ValueError, 'degree counts'):
            verifier.verify_cube(cube, self.certificate['basis_degrees'])
        cube = copy.deepcopy(self.certificate['cube'])
        cube['rectangular_volume_upper_bound'] = 2482
        with self.assertRaisesRegex(ValueError, 'volume comparison'):
            verifier.verify_cube(cube, self.certificate['basis_degrees'])

    def test_uncovered_cube_degree_triples_are_rejected(self):
        cube = copy.deepcopy(self.certificate['cube'])
        cube['rows'][0]['cutoffs'] = [-1, -1, -1]
        with self.assertRaisesRegex(ValueError, 'uncovered'):
            verifier.verify_cube(cube, self.certificate['basis_degrees'])


if __name__ == '__main__':
    unittest.main()

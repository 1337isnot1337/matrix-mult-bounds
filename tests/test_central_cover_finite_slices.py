import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-central-cover-finite-slices'
RESULTS = ROOT/'results/central-cover-finite-slices-2026-10-21'
spec = importlib.util.spec_from_file_location('central_finite_slices', PACKAGE/'verify_cover.py')
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class CentralCoverFiniteSlicesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS/'cover-certificate.json').read_text())

    def test_complete_source_and_coordinate_replay(self):
        report = verifier.verify(self.certificate)
        self.assertEqual(report, json.loads((RESULTS/'verification.json').read_text()))
        self.assertEqual([x['slice_upper_bound'] for x in report['finite_covers']],
                         [110, 10120, 973422])
        self.assertEqual(report['cube_gap'], 26578)
        self.assertEqual(report['rectangular_volume_upper_bound'], 986)
        self.assertLess(973422, (9*10*11)**2)

    def test_uncovered_degree_triples_are_rejected(self):
        rows = copy.deepcopy(self.certificate['covers'][0]['rows'])
        rows[1]['cutoffs'] = [0, 0, 0]
        with self.assertRaisesRegex(ValueError, 'uncovered'):
            verifier.count_cover(self.certificate['degrees'], 1, rows)

    def test_count_and_polynomial_tampering_are_rejected(self):
        for key in ('word_multiplicity', 'selected_slices', 'whole_leg_slices'):
            rows = copy.deepcopy(self.certificate['covers'][0]['rows'])
            rows[0][key] += 1
            with self.assertRaisesRegex(ValueError, 'multiplicity|slice count'):
                verifier.count_cover(self.certificate['degrees'], 1, rows)
        rows = copy.deepcopy(self.certificate['covers'][0]['rows'])
        rows[0]['degree_counts_without_matrix'][0] += 1
        with self.assertRaisesRegex(ValueError, 'polynomial'):
            verifier.count_cover(self.certificate['degrees'], 1, rows)

    def test_field_source_and_dimension_tampering_are_rejected(self):
        for key, value, message in (
                ('coefficient_field', 'F5', 'field'),
                ('group', 'SL(2,5)', 'source'),
                ('degrees', [0]*60, 'degree dimensions'),
                ('rectangular_volume_upper_bound', 987, 'volume bound')):
            bad = copy.deepcopy(self.certificate)
            bad[key] = value
            with self.assertRaisesRegex(ValueError, message):
                verifier.verify(bad)
        bad = copy.deepcopy(self.certificate)
        bad['basis_source']['sha256'] = '0'*64
        with self.assertRaisesRegex(ValueError, 'pinned basis'):
            verifier.verify(bad)

    def test_histogram_preserving_false_degree_assignment_is_rejected(self):
        bad = copy.deepcopy(self.certificate)
        high = bad['degrees'].index(4)
        low = bad['degrees'].index(0)
        bad['degrees'][high], bad['degrees'][low] = bad['degrees'][low], bad['degrees'][high]
        with self.assertRaisesRegex(ValueError, 'degree four'):
            verifier.verify(bad)


if __name__ == '__main__':
    unittest.main()

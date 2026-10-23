"""Actual full-source replay, independent finite counts and false-claim controls."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-s5-peirce-covers'
RESULTS = ROOT/'results/s5-peirce-covers-2026-10-23'


def load(name):
    spec = importlib.util.spec_from_file_location('s5_peirce_'+name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


source, exporter, verifier = load('source'), load('export_covers'), load('verify_covers')


class S5PeirceCoverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads((RESULTS/'source.json').read_text())
        cls.certificate = json.loads((RESULTS/'certificate.json').read_text())

    def test_full_source_and_separate_grouped_coordinate_replay(self):
        receipt = verifier.verify(self.source, self.certificate)
        self.assertEqual(receipt, json.loads((RESULTS/'verification.json').read_text()))
        self.assertEqual(receipt['source_replay']['original_coefficients_checked'], 120**3)
        self.assertEqual(receipt['source_replay']['basis_rank'], 120)
        self.assertEqual(receipt['source_replay']['principal_terms'], 1198)
        self.assertEqual(receipt['source_replay']['small_terms'], 6964)
        self.assertEqual(receipt['source_replay']['common_cover_coordinate_count'], 26)
        self.assertEqual([r['coordinate_multiplicity_checked'] for r in receipt['sources']],
                         [240**3, 480**3])

    def test_source_and_polynomial_exports_reproduce(self):
        self.assertEqual(source.construct(), self.source)
        self.assertEqual(exporter.export(), self.certificate)

    def test_new_target_exclusions_and_still_open_target(self):
        first, second = self.certificate['sources']
        self.assertEqual([first['slice_upper_bound'], second['slice_upper_bound']],
                         [6638912, 41159136])
        self.assertEqual(first['additional_coordinate_exclusions'], [])
        self.assertEqual(second['additional_coordinate_exclusions'],
                         [[18, 18, 20], [17, 18, 21], [15, 18, 24], [18, 19, 19], [17, 19, 20]])
        self.assertEqual(len(second['remaining_shapes']), 4)
        self.assertGreater(first['slice_upper_bound'], (13*14*14)**2)
        for row in self.certificate['sources']:
            v = row['single_target_volume_upper_bound']
            self.assertLessEqual(v*v, row['slice_upper_bound'])
            self.assertLess(row['slice_upper_bound'], (v+1)**2)

    def test_rejects_changed_basis_common_cover_field_and_pins(self):
        mutations = [
            lambda r: r['basis'].__setitem__(1, r['basis'][0]),
            lambda r: r.__setitem__('field', 'C'),
            lambda r: r.__setitem__('common_cover_types', [7, 10, 11, 18]),
            lambda r: r.__setitem__('source_pins', {}),
        ]
        for mutation in mutations:
            report = copy.deepcopy(self.source)
            mutation(report)
            with self.assertRaises(ValueError):
                source.replay(report)

    def test_rejects_wrong_budget_cut_count_or_scope(self):
        mutations = [
            lambda r: r['sources'][0]['rows'][1].__setitem__('source_degree_bound', 11),
            lambda r: r['sources'][0]['rows'][1]['cutoffs'].__setitem__(0, 8),
            lambda r: r['sources'][0]['rows'][1].__setitem__('selected_slices', 387327),
            lambda r: r['sources'][0]['additional_coordinate_exclusions'].append([13, 14, 14]),
            lambda r: r.__setitem__('arbitrary_complex_exclusion', True),
            lambda r: r.__setitem__('improves_omega', True),
        ]
        for mutation in mutations:
            report = copy.deepcopy(self.certificate)
            mutation(report)
            with self.assertRaises(ValueError):
                verifier.verify(self.source, report)


if __name__ == '__main__':
    unittest.main()

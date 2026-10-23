"""Independent source/cover replay, exhaustive cutoff controls, and tampering."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-s5-finite-covers'
RESULTS = ROOT/'results/s5-finite-covers-2026-10-23'


def load(name):
    spec = importlib.util.spec_from_file_location('s5_finite_'+name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


covers, verifier = load('covers'), load('verify')


class S5FiniteCoverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((RESULTS/'certificate.json').read_text())

    def test_independent_source_and_coordinate_replay(self):
        receipt = verifier.verify(self.report)
        self.assertEqual(receipt, json.loads((RESULTS/'verification.json').read_text()))
        self.assertEqual([s['coordinate_multiplicity_checked'] for s in receipt['sources']],
                         [240**3, 480**3])
        self.assertEqual([s['degree_triples_checked'] for s in receipt['sources']], [47313, 180400])

    def test_export_reproducible_and_new_target_boundary(self):
        self.assertEqual(covers.export(), self.report)
        first, second = self.report['sources']
        self.assertLess(second['slice_upper_bound'], 19**6)
        self.assertGreater(first['slice_upper_bound'], (13*14*14)**2)
        self.assertIn([19, 19, 19], second['new_coordinate_exclusions'])
        self.assertEqual([len(s['new_coordinate_exclusions']) for s in (first, second)], [4, 34])
        self.assertEqual([len(s['remaining_shapes']) for s in (first, second)], [2, 9])

    def test_cutoff_search_against_all_integer_triples(self):
        # Sparse degree polynomials exercise the plateau endpoint reduction.
        for counts in ([1, 0, 0, 2, 0, 1], [2, 1, 3, 1, 2], [1, 0, 0, 0, 1], [4]):
            maximum = len(counts)-1
            exact = sum(counts)
            for a in range(-1, maximum+1):
                for b in range(-1, maximum+1):
                    for c in range(-1, maximum+1):
                        if a+b+c >= maximum-2:
                            exact = min(exact, sum(sum(counts[:v+1]) for v in (a, b, c)))
            self.assertEqual(covers.choose_cutoffs(counts)[0], exact)

    def test_rejects_undercoverage_wrong_counts_and_false_frontier(self):
        mutations = [
            lambda r: r['sources'][0]['rows'][1]['cutoffs'].__setitem__(0, 8),
            lambda r: r['sources'][0]['rows'][1]['degree_counts_without_matrix'].__setitem__(0, 0),
            lambda r: r['sources'][0]['rows'][1].__setitem__('word_multiplicity', 2),
            lambda r: r['sources'][1].__setitem__('slice_upper_bound', 1),
            lambda r: r['sources'][0]['new_coordinate_exclusions'].append([13, 14, 14]),
        ]
        for mutation in mutations:
            report = copy.deepcopy(self.report)
            mutation(report)
            with self.assertRaises(ValueError):
                verifier.verify(report)

    def test_rejects_changed_sources_or_inflated_evidence(self):
        for key, value in [('scope', 'all complex degenerations'),
                           ('proof_status', 'reviewed'), ('improves_omega', True),
                           ('optimal_cover_claimed', True), ('source_pins', {})]:
            report = copy.deepcopy(self.report)
            report[key] = value
            with self.assertRaises(ValueError):
                verifier.verify(report)
        report = copy.deepcopy(self.report)
        report['source_pins'][next(iter(report['source_pins']))] = '0'*64
        with self.assertRaises(ValueError):
            verifier.verify(report)


if __name__ == '__main__':
    unittest.main()

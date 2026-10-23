"""Exact induction gates, literal coordinate controls, and corruption rejection."""

import copy
import importlib.util
from itertools import product
import json
from math import prod
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-s5-higher-powers'
RESULTS = ROOT / 'results/s5-higher-powers-2026-10-23'


def load(name):
    spec = importlib.util.spec_from_file_location('s5_high_' + name, PACKAGE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


bounds, verifier = load('bounds'), load('verify')


def selected(n, r):
    """Literal small model with one coordinate per principal degree."""
    result = set()
    for word in product((0, 1), repeat=n):
        j, k = sum(word), n*(r+1)-sum(word)
        for principal in product(range(7), repeat=j):
            if sum(principal) > 2*j:
                continue
            for central in product((0, 1), repeat=k):
                if sum(central) <= k//3:
                    result.add((word, principal, central))
    return result


class S5HigherPowerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((RESULTS / 'certificate.json').read_text())

    def test_complete_source_and_induction_acceptance(self):
        receipt = verifier.verify(self.report)
        self.assertEqual(receipt, json.loads((RESULTS / 'verification.json').read_text()))
        self.assertEqual([s['induction_seeds_checked'] for s in receipt['sources']], [36, 36])
        self.assertEqual([s['power35_passes'] for s in receipt['sources']], [False, True])
        self.assertFalse(receipt['actual_source_lower_bound_claimed'])

    def test_reproducible_export_and_target_inventory(self):
        self.assertEqual(bounds.export(), self.report)
        self.assertEqual([len(s['remaining_shapes']) for s in self.report['sources']], [2, 9])
        self.assertEqual([s['maximum_target_volume'] for s in self.report['sources']], [2548, 6498])

    def test_literal_weighted_coordinate_counts(self):
        layers = [17, 9, 9, 18, 9, 9, 17]
        for j in range(5):
            literal = sum(prod(layers[d] for d in coordinate)
                          for coordinate in product(range(7), repeat=j)
                          if sum(coordinate) <= 2*j)
            self.assertEqual(verifier.principal_count(layers, j), literal)
        for k in range(13):
            self.assertEqual(verifier.binary_count(k),
                             sum(sum(bits) <= k//3 for bits in product((0, 1), repeat=k)))

    def test_literal_diagonal_and_concatenation(self):
        for r in (1, 2):
            first, second, third = selected(1, r), selected(2, r), selected(3, r)
            for word, principal, central in third:
                self.assertLessEqual(3*sum(principal), 6*sum(word))
                self.assertLessEqual(3*sum(central), 3*(r+1)-sum(word))
            for a, b, target in ((first, first, second), (first, second, third)):
                images = {(u[0]+v[0], u[1]+v[1], u[2]+v[2]) for u in a for v in b}
                self.assertEqual(len(images), len(a)*len(b))
                self.assertLessEqual(images, target)

    def test_rejects_incomplete_or_corrupted_induction(self):
        mutations = [
            lambda r: r['sources'][0]['seed_counts'].pop(),
            lambda r: r['sources'][0]['seed_counts'].__setitem__(1, r['sources'][0]['seed_counts'][0]),
            lambda r: r['sources'][1]['seed_counts'][0].__setitem__('count', 1),
            lambda r: r.__setitem__('induction_step', 37),
            lambda r: r['sources'][0].__setitem__('maximum_target_volume', 2535),
            lambda r: r['sources'][1]['remaining_shapes'].pop(),
        ]
        for mutation in mutations:
            report = copy.deepcopy(self.report)
            mutation(report)
            with self.assertRaises(ValueError):
                verifier.verify(report)

    def test_rejects_source_changes_and_actual_tensor_claims(self):
        for key, value in [('scope', 'actual tensor slice rank'),
                           ('actual_source_lower_bound_claimed', True),
                           ('improves_omega', True), ('proof_status', 'reviewed'),
                           ('source_pins', {})]:
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

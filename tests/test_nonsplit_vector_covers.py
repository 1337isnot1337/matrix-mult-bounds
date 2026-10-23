import importlib.util
from itertools import product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-nonsplit-vector-covers'
RESULTS = ROOT/'results/nonsplit-vector-covers-2026-10-23'
sys.path.insert(0, str(PACKAGE))
spec = importlib.util.spec_from_file_location('nonsplit_vector_verify', PACKAGE/'verify.py')
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)
from cover_model import classes, verify_block
from weighted_discovery import cutoffs


class NonsplitVectorCoverTests(unittest.TestCase):
    def test_full_source_covers_and_exact_weight_census(self):
        report = verifier.verify()
        self.assertEqual(report, json.loads((RESULTS/'verification.json').read_text()))
        self.assertEqual(report['source']['principal_degree_triples'], 95)
        self.assertEqual(report['weight_vectors_checked'], 3372)
        self.assertEqual(report['best_cube_slice_upper_bound'], 6155844)
        self.assertFalse(report['class_cover_optimality_certified'])

    def test_parity_only_cover_requires_the_verified_source_condition(self):
        labels = list(classes(1))
        selected = [[label for label in labels if label[0] % 2 == parity]
                    for parity in (0, 1, 1)]
        report = verify_block(1, selected, True)
        self.assertEqual(report['admissible_triples_checked'], 19000)
        with self.assertRaisesRegex(ValueError, 'uncovered'):
            verify_block(1, selected, False)

    def test_missing_and_duplicate_classes_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'uncovered'):
            verify_block(0, [[], [], []])
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            verify_block(0, [[(0, 0, 0), (0, 0, 0)], [], []])

    def test_cutoff_search_agrees_with_independent_small_enumeration(self):
        for counts in ([1, 2, 3, 1], [3, 0, 1, 4, 2], [1, 4, 6, 4, 1]):
            for maximum in range(3, 9):
                expected = min(sum(sum(counts[:cut+1]) for cut in cuts)
                               for cuts in product(range(-1, maximum+1), repeat=3)
                               if sum(cuts) == maximum-2)
                self.assertEqual(cutoffs(counts, maximum)[0], expected)


if __name__ == '__main__':
    unittest.main()

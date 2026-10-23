"""Exact certificate rejection and independent rank controls for the locus."""
import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-resolvent-rank-six-finite'
RESULTS = ROOT / 'results/resolvent-rank-six-finite-2026-10-23'
spec = importlib.util.spec_from_file_location('rank_six_locus', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


def rational_rank(matrix):
    work = [[Fraction(x) for x in row] for row in matrix]
    rank = 0
    for c in range(len(work[0])):
        pivot = next((r for r in range(rank, len(work)) if work[r][c]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][c]
        work[rank] = [x / scale for x in work[rank]]
        for r in range(rank + 1, len(work)):
            scale = work[r][c]
            work[r] = [x - scale * y for x, y in zip(work[r], work[rank])]
        rank += 1
        if rank == len(work):
            break
    return rank


class ResolventRankSixLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / 'certificate.json').read_text())
        cls.raw, cls.unit, cls.high, cls.labels, cls.basis = verify.source()

    def test_complete_certificate_matches_report(self):
        report = verify.verify(self.certificate)
        self.assertEqual(report, json.loads((RESULTS / 'verification.json').read_text()))
        self.assertEqual(report['full_rank_six_locus_dimension'], 17)
        self.assertEqual(report['explicit_rank109_compression']['image_dimension'], 111)
        self.assertFalse(report['exponent_improvement'])

    def test_rejects_missing_and_repeated_minor_stages(self):
        for key in ('seven_minors', 'six_minors'):
            for extra in (False, True):
                bad = copy.deepcopy(self.certificate)
                if extra:
                    bad[key].append(bad[key][0])
                else:
                    bad[key].pop()
                with self.assertRaisesRegex(ValueError, 'incomplete'):
                    verify.verify(bad)

    def test_rejects_corrupted_diagonal_and_nonunit_substitution(self):
        bad = copy.deepcopy(self.certificate['seven_minors'])
        bad[0]['form'][bad[0]['pivot']] = 2
        with self.assertRaisesRegex(ValueError, 'unit'):
            verify.eliminate(self.basis, self.labels, bad, 7)
        bad = copy.deepcopy(self.certificate['seven_minors'])
        j = next(i for i, x in enumerate(bad[0]['form']) if not x)
        bad[0]['form'][j] = 1
        with self.assertRaisesRegex(ValueError, 'diagonal'):
            verify.eliminate(self.basis, self.labels, bad, 7)

    def test_rejects_repeated_rows_and_broken_six_minors(self):
        bad = copy.deepcopy(self.certificate['seven_minors'])
        bad[0]['minor'][1][0] = bad[0]['minor'][0][0]
        with self.assertRaisesRegex(ValueError, 'minor'):
            verify.eliminate(self.basis, self.labels, bad, 7)
        reduced, labels = verify.eliminate(self.basis, self.labels,
                                          self.certificate['seven_minors'], 7)
        bad = copy.deepcopy(self.certificate['six_minors'])
        bad[0]['minor'][0][1] = 27
        with self.assertRaises(ValueError):
            verify.eliminate(reduced, labels, bad, 6)

    def test_independent_rational_locus_and_outside_controls(self):
        reduced, _ = verify.eliminate(self.basis, self.labels,
                                     self.certificate['seven_minors'], 7)
        for weights in ([1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, -2, 3, -4, 5]):
            self.assertEqual(rational_rank(verify.add(reduced, weights)), 6)
        # Keeping only the high part of T_4 does not remain on the locus.
        high_part = verify.add([self.high[7], self.high[10], self.high[13]], [1, 1, 1])
        self.assertGreater(rational_rank(high_part), 6)
        self.assertEqual(rational_rank(self.high[1]), 8)
        self.assertEqual(rational_rank(self.raw[0]), 16)

    def test_sharp_compression_kills_the_stated_matrix(self):
        sharp = self.high[0]
        survivors = [[sharp[r][c] for c in range(28) if c not in (3, 7, 11)]
                     for r in range(28) if r not in (21, 22, 23)]
        self.assertTrue(all(not x for row in survivors for x in row))
        self.assertEqual(rational_rank(sharp), 6)


if __name__ == '__main__':
    unittest.main()

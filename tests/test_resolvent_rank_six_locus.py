"""Replay, malformed-certificate, and exceptional-direction controls."""

import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-resolvent-rank-six-locus'
RESULTS = ROOT / 'results/resolvent-rank-six-locus-2026-10-23'
spec = importlib.util.spec_from_file_location('rank_six_locus', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


def rational_rank(matrix):
    work = [[Fraction(x) for x in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [x / scale for x in work[rank]]
        for i in range(rank + 1, len(work)):
            scale = work[i][column]
            if scale:
                work[i] = [x - scale * y for x, y in zip(work[i], work[rank])]
        rank += 1
    return rank


class ResolventRankSixLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / 'certificate.json').read_text())
        cls.raw, cls.unit, cls.high, cls.mixed, cls.labels = verify.source()

    def test_complete_certificate_and_compression_report(self):
        report = verify.verify(self.certificate)
        self.assertEqual(report, json.loads((RESULTS / 'verification.json').read_text()))
        self.assertEqual(report['full_rank_at_most_six_dimension'], 17)
        self.assertEqual(len(report['compression_controls']), 4)
        self.assertFalse(report['independent_review'])
        self.assertFalse(report['improves_omega'])

    def test_hidden_mixed_direction_and_pure_Q_are_distinct(self):
        hidden = verify.combine(
            [self.raw[4], self.high[7], self.high[10], self.high[13]], [-1, 1, 1, 1])
        self.assertEqual(rational_rank(hidden), 6)
        self.assertEqual(rational_rank(self.high[13]), 8)
        self.assertEqual(verify.shear(hidden),
                         [[-x for x in row] for row in verify.normal_block(4)])
        combination = verify.combine(
            [self.high[0], self.high[4], self.high[8], self.high[12], hidden],
            [3, -2, 1, 4, -5])
        self.assertEqual(rational_rank(combination), 6)

    def test_missing_duplicate_and_corrupt_minors_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['stages'].pop()
        with self.assertRaisesRegex(ValueError, '26 stages'):
            verify.validate_certificate(bad, self.mixed, self.labels)
        bad = copy.deepcopy(self.certificate)
        bad['stages'][0]['minor'][1] = bad['stages'][0]['minor'][0][:]
        with self.assertRaisesRegex(ValueError, 'invalid minor'):
            verify.validate_certificate(bad, self.mixed, self.labels)
        bad = copy.deepcopy(self.certificate)
        stage = bad['stages'][0]
        stage['form'][stage['pivot']] = 2
        with self.assertRaisesRegex(ValueError, 'nonunit'):
            verify.validate_certificate(bad, self.mixed, self.labels)
        bad = copy.deepcopy(self.certificate)
        stage = bad['stages'][0]
        stage['form'][(stage['pivot'] + 1) % len(stage['form'])] += 1
        with self.assertRaisesRegex(ValueError, 'diagonal'):
            verify.validate_certificate(bad, self.mixed, self.labels)
        bad = copy.deepcopy(self.certificate)
        bad['remaining_labels'][-1] = ['f', 3, 0]
        with self.assertRaisesRegex(ValueError, 'remaining labels'):
            verify.validate_certificate(bad, self.mixed, self.labels)

    def test_product_dimension_lower_bound_is_sharp(self):
        # A=<1,x>, B=<1,x,x^2> in one component; their product has dimension4.
        products = [{i + j: 1} for i in range(2) for j in range(3)]
        for prime in [None, 2, 3]:
            self.assertEqual(verify.sparse_rank(products, prime), 4)

    def test_artifact_hashes_source_pins_and_claim_registration(self):
        manifest = json.loads((PACKAGE / 'manifest.json').read_text())
        for path, digest in manifest['sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), digest)
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for source in sources['local_dependencies']:
            self.assertEqual(hashlib.sha256((ROOT / source['path']).read_bytes()).hexdigest(),
                             source['sha256'])
        claims = json.loads((PACKAGE / 'claims.json').read_text())
        ledger = json.loads((ROOT / 'research/claims.json').read_text())['claims']
        for claim in claims:
            self.assertEqual([entry for entry in ledger if entry['id'] == claim['id']], [claim])


if __name__ == '__main__':
    unittest.main()

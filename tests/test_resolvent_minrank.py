"""Exact coefficient, source-convention, and corruption controls."""
import copy
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-resolvent-minrank'
RESULTS = ROOT / 'results/resolvent-minrank-2026-10-23'
spec = importlib.util.spec_from_file_location('resolvent_minrank_verify', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


def rational_rank(matrix):
    """Independent dense rational row reduction for the sharpness control."""
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
        if rank == len(work):
            break
    return rank


class ResolventMinrankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / 'certificate.json').read_text())

    def test_complete_integer_certificate_and_recorded_report(self):
        report = verify.verify(self.certificate)
        self.assertEqual(report, json.loads((RESULTS / 'verification.json').read_text()))
        self.assertEqual(report['certificate']['elimination_stages'], 31)
        self.assertEqual(report['certificate']['diagonal_factors'], [-1, 1])
        self.assertEqual(report['full_limiting_space_minimum_rank'], 6)
        self.assertFalse(report['arbitrary_singular_trajectories_excluded'])

    def test_literal_source_matches_independent_six_index_tensor_expansion(self):
        slices = [verify.zeros(112, 112) for _ in range(112)]
        for i, j, p, q, r, s in product(range(4), repeat=6):
            first = (i * 7 + p + q) * 4 + s
            row = (j * 4 + p) * 7 + r + s
            column = ((i + j) * 4 + q) * 4 + r
            slices[first][row][column] += 1
        for i, k, s in product(range(4), range(7), range(4)):
            self.assertEqual(slices[(i * 7 + k) * 4 + s], verify.full_source_matrix(i, k, s))

    def test_sharp_mixed_block_has_exact_rational_rank_six(self):
        _, unit, inverse, normalized, high = verify.outer_source()
        self.assertEqual(rational_rank(high[0]), 6)
        self.assertEqual(rational_rank(verify.multiply(inverse, high[0])), 6)
        self.assertEqual(verify.multiply(unit, inverse), verify.identity(28))
        self.assertEqual(verify.multiply(inverse, unit), verify.identity(28))
        self.assertEqual(rational_rank(normalized[0]), 16)

    def test_corrupted_eliminations_and_omitted_cases_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['stages'].pop()
        with self.assertRaisesRegex(ValueError, '31 stages'):
            verify.validate_minors(bad)
        bad = copy.deepcopy(self.certificate)
        bad['stages'][0]['minor'][1][1] = bad['stages'][0]['minor'][0][1]
        with self.assertRaisesRegex(ValueError, 'minor'):
            verify.validate_minors(bad)
        bad = copy.deepcopy(self.certificate)
        bad['stages'][0]['form'][0] = 1
        with self.assertRaisesRegex(ValueError, 'diagonal'):
            verify.validate_minors(bad)
        bad = copy.deepcopy(self.certificate)
        bad['stages'][0]['form'][bad['stages'][0]['pivot']] = 2
        with self.assertRaisesRegex(ValueError, 'nonunit'):
            verify.validate_minors(bad)
        bad = copy.deepcopy(self.certificate)
        bad['labels'][0][1] = 3
        with self.assertRaisesRegex(ValueError, 'format'):
            verify.validate_minors(bad)

    def test_artifact_hashes_and_source_pins(self):
        manifest = json.loads((PACKAGE / 'manifest.json').read_text())
        for path, expected in manifest['sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), expected)
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for source in sources['local_dependencies']:
            self.assertEqual(hashlib.sha256((ROOT / source['path']).read_bytes()).hexdigest(), source['sha256'])


if __name__ == '__main__':
    unittest.main()

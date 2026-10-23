"""Acceptance tampering, literal coefficients, and compression controls."""

import copy
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-resolvent-rank-six-locus'
RESULTS = ROOT / 'results/resolvent-rank-six-locus-2026-10-23'
spec = importlib.util.spec_from_file_location('resolvent_rank_six_locus', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class ResolventRankSixLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / 'certificate.json').read_text())

    def test_complete_replay_and_recorded_report(self):
        self.assertEqual(verify.verify(self.certificate),
                         json.loads((RESULTS / 'verification.json').read_text()))

    def test_source_matches_independent_index_expansion(self):
        raw, unit, inverse, high, mixed, labels, terminal = verify.source()
        expected = [[[0] * 28 for _ in range(28)] for _ in range(16)]
        for i, s, j, r in product(range(4), repeat=4):
            expected[4 * i + s][7 * j + r + s][4 * (i + j) + r] += 1
        self.assertEqual(raw, expected)
        self.assertEqual(verify.multiply(unit, inverse), verify.identity(28))
        self.assertEqual(verify.multiply(inverse, unit), verify.identity(28))

    def test_corrupt_minors_substitutions_and_terminal_space_are_rejected(self):
        bad_cases = []
        bad = copy.deepcopy(self.certificate)
        bad['stages'].pop()
        bad_cases.append(bad)
        bad = copy.deepcopy(self.certificate)
        bad['stages'][0]['minor'][1][0] = bad['stages'][0]['minor'][0][0]
        bad_cases.append(bad)
        bad = copy.deepcopy(self.certificate)
        bad['stages'][0]['form'][bad['stages'][0]['pivot']] = 2
        bad_cases.append(bad)
        bad = copy.deepcopy(self.certificate)
        bad['remaining_basis_coefficients'][-1][4] = 1
        bad_cases.append(bad)
        bad = copy.deepcopy(self.certificate)
        bad['terminal_six_minor_stages'].pop()
        bad_cases.append(bad)
        bad = copy.deepcopy(self.certificate)
        bad['terminal_six_minor_stages'][0]['form'][0] += 1
        bad_cases.append(bad)
        for i, bad in enumerate(bad_cases):
            with self.subTest(corruption=i), self.assertRaises(ValueError):
                verify.validate_certificate(bad)

    def test_misaligned_compression_is_injective(self):
        basis = verify.full_transformed_basis()
        # These lost output coordinates are outside the common final image.
        compressed = [{(r, c): x for (r, c), x in b.items()
                       if r not in (0, 1, 2) and c not in (31, 35, 39)} for b in basis]
        self.assertEqual(verify.sparse_rank(compressed), 112)

    def test_artifact_hashes_and_source_pins(self):
        manifest = json.loads((PACKAGE / 'manifest.json').read_text())
        for path, expected in manifest['sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), expected)
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for entry in sources['local_dependencies']:
            self.assertEqual(hashlib.sha256((ROOT / entry['path']).read_bytes()).hexdigest(),
                             entry['sha256'])


if __name__ == '__main__':
    unittest.main()

"""Exact support and source-certificate tests for the rank-six family."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-resolvent-rank6-family'
REPORT = ROOT / 'results/resolvent-rank6-family-2026-10-23/verification.json'
spec = importlib.util.spec_from_file_location('resolvent_rank6_family_verify', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class ResolventRank6FamilyTests(unittest.TestCase):
    def test_exact_common_six_row_support_and_inherited_lower_bound(self):
        report = verify.verify()
        self.assertEqual(report['family_dimension'], 16)
        self.assertEqual(report['block_positions'], [[3, column] for column in range(4)])
        self.assertEqual(report['common_row_support'], [0, 7, 14, 21, 22, 23])
        self.assertEqual(len(report['generator_supports']), 16)
        self.assertEqual(report['full_source_embeddings_checked'], 16)
        self.assertEqual(report['minimum_nonzero_rank'], 6)
        self.assertFalse(report['full_rank_six_locus_classified'])
        self.assertFalse(report['tensor_degeneration_constructed'])

    def test_recorded_report_and_hashes(self):
        self.assertEqual(verify.verify(), json.loads(REPORT.read_text()))
        manifest = json.loads((PACKAGE / 'manifest.json').read_text())
        for path, expected in manifest['sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), expected)


if __name__ == '__main__':
    unittest.main()

"""Preserved discovery stdout must match the repaired sampled histories."""
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT/'research/ai/2026-10-20-paired-direct-sums/q64_history_metadata_check.py'
SPEC = importlib.util.spec_from_file_location('q64_history_metadata_checked', MODULE)
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class HistoryMetadataTests(unittest.TestCase):
    def test_all_preserved_sampled_records(self):
        report = CHECK.verify()
        self.assertEqual(report['histories_checked'], 8)
        self.assertEqual(report['retained_snapshots_checked'], 223)
        self.assertTrue(report['all_non_ridge_published_payloads_unchanged'])


if __name__ == '__main__':
    unittest.main()

"""Separately implemented integer controls for the reduced-corner search."""
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT/'research/ai/2026-10-20-paired-direct-sums/reduced_corner_replay.py'
SPEC = importlib.util.spec_from_file_location('reduced_corner_replay_tested', MODULE)
REPLAY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPLAY)


class ReducedCornerReplayTests(unittest.TestCase):
    def test_integer_M343_control_and_detected_sign_error(self):
        result = REPLAY.positive_control()
        self.assertEqual(result['all_coefficient_positions_checked'], 1296)
        self.assertTrue(result['integer_control_passes'])
        self.assertEqual(result['deliberate_A_sign_error_positions'], 4)

    def test_retained_histories_match_original_emitted_records(self):
        results = ROOT/'results/paired-direct-sums-2026-10-20'
        audit = json.loads((results/'q64-m1-corner-pilot-audit.json').read_text())
        count = 0
        for pilot in audit['pilots']:
            saved = json.loads((results/pilot['artifact']).read_text())
            self.assertEqual(saved['completed_run']['history'], pilot['original_emitted_records'])
            self.assertEqual(saved['completed_run']['iterations_completed'], 1500)
            self.assertEqual(saved['completed_run']['actual_stop_reason'], 'iteration_budget')
            self.assertEqual(saved['discovery_checkpoint_sha256'],
                             pilot['original_discovery_checkpoint_sha256'])
            count += len(pilot['original_emitted_records'])
        self.assertEqual(count, 62)


if __name__ == '__main__':
    unittest.main()

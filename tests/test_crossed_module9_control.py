"""Replay the separately reconstructed rational nine-channel control."""

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results/anisotropic-constructions-2026-10-20"
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_balancing_cross_module_replay.py"
SPEC = importlib.util.spec_from_file_location("crossed_module9_replay", PATH)
REPLAY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPLAY)


class CrossedModule9ControlTests(unittest.TestCase):
    def test_complete_rational_control_and_full_source_lifts(self):
        witness = json.loads((RESULTS / "crossed-module9-control.json").read_text())
        actual = REPLAY.verify(witness)
        expected = json.loads((RESULTS / "parity_balancing_cross_module9_full_replay.json").read_text())
        self.assertEqual(actual, expected)
        self.assertEqual([item["target_shape"] for item in actual["full_sources"]],
                         [[4, 4, 9], [4, 4, 18]])


if __name__ == "__main__":
    unittest.main()

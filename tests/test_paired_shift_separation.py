import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-paired-shift-separation"
RESULT = ROOT / "results/paired-shift-separation-2026-10-23/verification.json"
SPEC = importlib.util.spec_from_file_location(
    "paired_shift_separation_verify", PACKAGE / "verify.py"
)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class PairedShiftSeparationTests(unittest.TestCase):
    def test_exact_finite_control_and_report(self):
        report = VERIFY.verify()
        self.assertEqual(report, json.loads(RESULT.read_text()))
        self.assertEqual(report["profile_shift_ranks"], [1, 2])
        self.assertEqual(report["channel_rank_budget"], 3)
        self.assertEqual(report["target_channel_rank"], 4)
        self.assertGreaterEqual(
            report["observed_residual_flattening_rank"],
            report["predicted_flattening_lower_bound"],
        )

    def test_rank_routine_on_rectangular_and_zero_matrices(self):
        self.assertEqual(VERIFY.rank_mod([[1, 2, 3], [2, 4, 6]], 101), 1)
        self.assertEqual(VERIFY.rank_mod([[0, 0], [0, 0]], 101), 0)


if __name__ == "__main__":
    unittest.main()

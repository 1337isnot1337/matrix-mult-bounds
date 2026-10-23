import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/ai/2026-10-23-paired-long-leg-target-screen/verify.py"
CERTIFICATE = ROOT / "results/paired-long-leg-target-screen-2026-10-23/certificate.json"
SPEC = importlib.util.spec_from_file_location("paired_long_leg_target_screen", SCRIPT)
SCREEN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCREEN)


class PairedLongLegTargetScreenTests(unittest.TestCase):
    def test_pinned_target_screen_regenerates_exactly(self):
        report = json.loads(CERTIFICATE.read_text())
        result = SCREEN.verify_report(report)
        self.assertEqual(result["saved_targets"], 28)
        self.assertEqual(result["all_target_safe_windows"], {
            14: [[183, 209]],
            15: [[211, 241]],
            16: [[241, 274]],
        })
        self.assertTrue(result["conditional_on_unreviewed_upstream_proof"])
        self.assertFalse(result["improves_omega"])


if __name__ == "__main__":
    unittest.main()

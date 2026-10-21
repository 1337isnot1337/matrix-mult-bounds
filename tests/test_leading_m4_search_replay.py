"""Controls for the independently contracted numerical search archive."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "leading_m4_replay",
    ROOT / "research/ai/2026-10-21-leading-m4-search/replay.py",
)
REPLAY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPLAY)


class LeadingM4SearchReplayTests(unittest.TestCase):
    def test_archive_and_complete_coefficients(self):
        result = REPLAY.verify_all()
        self.assertEqual(result["terminal_points_replayed"], 39)
        self.assertTrue(result["integer_positive_control_passed"])
        self.assertGreater(result["deliberate_sign_error_positions"], 0)
        self.assertFalse(result["exact_low_rank_certificate_found"])
        self.assertFalse(result["improves_omega"])
        self.assertFalse(result["svd_diagnostics_recomputed"])
        self.assertEqual(result["coefficient_verification_dependencies"],
                         "Python standard library only")

    def test_active_norm_penalty_gradient(self):
        check = REPLAY.active_penalty_control()
        self.assertTrue(check["penalty_is_active"])
        self.assertLess(check["corrected_gradient_error"], 1e-7)
        self.assertGreater(check["historical_gradient_error"], 1.0)


if __name__ == "__main__":
    unittest.main()

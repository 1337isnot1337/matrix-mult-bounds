"""Exact controls for the arbitrary-A two-Toeplitz long-leg obstruction."""
import importlib.util
from pathlib import Path
import unittest

PATH = (Path(__file__).resolve().parents[1] / "research" / "ai" /
        "2026-10-23-toeplitz-long-legs" / "verify.py")
SPEC = importlib.util.spec_from_file_location("toeplitz_long_legs_verifier", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ToeplitzLongLegControls(unittest.TestCase):
    def test_complete_source_tensor_and_symbol_replay(self):
        result = MODULE.run()
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["field_for_rank"], "F_101")
        self.assertEqual(len(result["cases"]), 5)
        self.assertTrue(result["m_equals_one_sharpness_control"])
        self.assertEqual(
            [x["observed_flattening_rank_mod_101"] for x in result["cases"]],
            [36, 36, 64, 81, 100])
        for case in result["cases"]:
            self.assertGreaterEqual(
                case["observed_flattening_rank_mod_101"],
                case["predicted_lower_bound"])
            self.assertTrue(case["symbol_coefficient_identity_checked"])

    def test_nonlocal_exceptions_and_unrestricted_first_map(self):
        c = MODULE.check(10, 2, 0, True, (4,), (5,))
        self.assertEqual(c["predicted_lower_bound"], 36)
        self.assertEqual(c["observed_flattening_rank_mod_101"], 100)
        self.assertEqual(c["exceptional_b_columns"], [4])
        self.assertEqual(c["exceptional_c_columns"], [5])

    def test_width_one_is_not_excluded(self):
        self.assertTrue(MODULE.sharp_m1_control())
        # In the width-one case Q is exactly the width-one matrix tensor.
        self.assertEqual(MODULE.multiply({(0,0):1}, {(0,0):1}), {(0,0):1})


if __name__ == "__main__":
    unittest.main()

"""Exact positive control and optional full-coefficient compression controls."""

import importlib.util
from pathlib import Path
import sys
import unittest


HERE = Path(__file__).resolve().parents[1] / "research/ai/2026-10-20-anisotropic-constructions"


def load(name):
    original = list(sys.path)
    try:
        sys.path.insert(0, str(HERE))
        spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path[:] = original


EXACT = load("parity_structure_compression_control")
HAS_NUMERICS = (importlib.util.find_spec("numpy") is not None
                and importlib.util.find_spec("scipy") is not None)


class ExactCompressionControl(unittest.TestCase):
    def test_complete_integer_M2_identity_and_top_blocks(self):
        report = EXACT.verify()
        self.assertEqual(report["source_terms_checked"], 64)
        self.assertEqual(report["target_nonzero_coefficients"], 8)
        self.assertTrue(report["all_three_physical_top_blocks_exact"])

    def test_nonzero_to_nonzero_coefficient_tamper_is_rejected(self):
        maps = EXACT.maps()
        row, col, value = maps[0][0]
        maps[0][0] = (row, col, 2 * value)
        with self.assertRaises(ValueError):
            EXACT.verify(maps)


@unittest.skipUnless(HAS_NUMERICS, "Optional compression discovery controls require NumPy and SciPy")
class NumericalCompressionControl(unittest.TestCase):
    def test_fixed_frame_complete_objective_gradient_and_alternating_solve(self):
        report = load("parity_structure_rectangular_compression").controls()
        self.assertEqual(report["complete_source_terms_checked"], 216)
        self.assertEqual(report["complete_target_coefficients_checked"], 144)
        self.assertTrue(report["other_two_leg_parameter_blocks_unchanged"])
        self.assertLess(report["loss_after_leg_update"], report["loss_before_leg_update"])

    def test_moving_splitting_gradients_normalization_and_positive_control(self):
        report = load("parity_structure_moving_compression").controls()
        self.assertEqual(len(report["gradient_checks"]), 6)
        self.assertLess(max(x["relative_error"] for x in report["gradient_checks"]), 1e-7)
        self.assertLess(report["positive_target_normalization_error"], 1e-10)
        self.assertLess(report["known_M2_control_loss"], 1e-20)


if __name__ == "__main__":
    unittest.main()

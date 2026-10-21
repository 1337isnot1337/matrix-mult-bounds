"""Optional numerical controls; importing this test does not require NumPy."""

import importlib.util
from pathlib import Path
import sys
import unittest


HAS_NUMPY = importlib.util.find_spec("numpy") is not None
MODULE = None
if HAS_NUMPY:
    HERE = Path(__file__).resolve().parents[1] / "research/ai/2026-10-20-anisotropic-constructions"
    original_path = list(sys.path)
    try:
        sys.path.insert(0, str(HERE))
        SPEC = importlib.util.spec_from_file_location("parity_structure_unequal_objective", HERE / "parity_structure_unequal_objective.py")
        MODULE = importlib.util.module_from_spec(SPEC)
        SPEC.loader.exec_module(MODULE)
    finally:
        sys.path[:] = original_path


@unittest.skipUnless(HAS_NUMPY, "Optional unequal-objective discovery control requires NumPy")
class UnequalObjectiveControls(unittest.TestCase):
    def test_full_nonsymmetric_coefficient_gradient_and_affine_controls(self):
        report = MODULE.controls()
        self.assertEqual(report["problem"]["target_leg_dimensions"], [5, 7, 7])
        self.assertEqual(report["exact_rectangular_partial_target_terms"], 12)
        self.assertEqual(report["exact_partial_squared_residual"], 1)
        self.assertEqual(len(report["single_block_controls_all_three_legs"]), 3)
        self.assertTrue(report["all_leg_specific_fixed_coefficients_unchanged"])
        self.assertTrue(report["all_three_regularized_leg_updates_monotone"])


if __name__ == "__main__":
    unittest.main()

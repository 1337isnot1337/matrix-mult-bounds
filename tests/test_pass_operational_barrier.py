"""Independent finite controls for the operational packing extension."""

from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-pass-operational-barrier/verify.py"
SPEC = importlib.util.spec_from_file_location("pass_operational_barrier", PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PassOperationalBarrierTests(unittest.TestCase):
    def test_literal_profile_values_and_normalization(self):
        self.assertEqual(MODULE.profile_cube(1, 7), 7**3)
        self.assertEqual(MODULE.profile_cube(2, 2), Fraction(625, 16))
        self.assertEqual(MODULE.profile_cube(3, 4), 500)
        self.assertEqual(MODULE.profile_cube(4, 3), 500)

    def test_exact_equality_strictness_and_forbidden_shortening(self):
        for parameters in ((1, 1, 2, 1), (2, 2, 5, 1), (2, 3, 7, 1)):
            case = MODULE.inspect_pass_case(*parameters)
            self.assertTrue(case["external_cost_condition"])
            self.assertEqual(case["scaled_cubed_margin"], 0)
            self.assertEqual(case["dimension_deficits"], (0, 0))
        for parameters in ((3, 1, 4, 1), (5, 2, 8, 1), (5, 2, 4, 2)):
            case = MODULE.inspect_pass_case(*parameters)
            self.assertTrue(case["external_cost_condition"])
            self.assertGreater(case["scaled_cubed_margin"], 0)
            self.assertEqual(case["dimension_deficits"], (0, 0))
        shortened = MODULE.inspect_pass_case(2, 2, 4, 1)
        self.assertFalse(shortened["external_cost_condition"])
        self.assertEqual(shortened["source_long_legs"], (12, 16))
        self.assertEqual(shortened["target_long_legs"], (13, 17))
        self.assertLess(shortened["scaled_cubed_margin"], 0)

    def test_derivative_identity_and_join(self):
        self.assertEqual(MODULE.derivative_identity_residual(), {})
        for a in range(1, 15):
            at_join = MODULE.profile_cube(a, a)
            expected_join = Fraction(3 * a - 1, 2) ** 4
            self.assertEqual(at_join, expected_join)
            for b in range(1, 15):
                # An independent cleared-denominator expansion of the
                # logarithmic derivative, including the positive denominator.
                denominator = (3 * b - 1) * (2 * a + b - 1) * (a + 2 * b - 1)
                derivative = (Fraction(1, 3 * b - 1)
                              + Fraction(1, 2 * a + b - 1)
                              - Fraction(2, a + 2 * b - 1))
                self.assertEqual(derivative * denominator, 2 * (a - b) ** 2)

    def test_dimension_control_uses_both_legs(self):
        # All full targets pass the first leg of dimensions here, but fail
        # the other one. The average condition alone is insufficient.
        dimensions = MODULE.homogeneous_dimensions(3, 2, 1, 3, 2, 0)
        self.assertEqual(dimensions["source_long_legs"], (5, 7))
        self.assertEqual(dimensions["target_long_legs"], (4, 8))
        self.assertFalse(dimensions["dimension_compatible"])
        self.assertEqual(sum(dimensions["dimension_deficits"]), 0)

    def test_exact_parameter_domains(self):
        for invalid in (0, -1, True, 2.5, "2"):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    MODULE.profile_cube(invalid, 2)
                with self.assertRaises(ValueError):
                    MODULE.pass_margin_numerator(2, 2, invalid, 1)
        with self.assertRaises(ValueError):
            MODULE.homogeneous_dimensions(2, 2, 5, 1, 0, 0)
        with self.assertRaises(ValueError):
            MODULE.homogeneous_dimensions(2, 2, 5, 1, -1, 1)

    def test_complete_recorded_finite_controls(self):
        report = MODULE.run_controls()
        self.assertEqual(report["ratio_grid"]["count"], 24**3)
        self.assertEqual(report["pass_boundary_grid"]["count"], 2 * 24**3)
        self.assertEqual(report["homogeneous_grid"]["count"], 5**4 * 35)
        self.assertGreater(report["homogeneous_grid"]["dimension_compatible"], 0)


if __name__ == "__main__":
    unittest.main()

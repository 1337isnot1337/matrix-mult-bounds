"""Exact acceptance controls for a formal calculus, not tensor-map tests."""

from fractions import Fraction as F
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "operational_repair_barrier",
    ROOT / "research/ai/2026-10-23-operational-repair-barrier/barrier.py",
)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class OperationalRepairBarrierTests(unittest.TestCase):
    def test_leg_convention_and_external_exponents(self):
        for p in (F(3, 2), F(8, 5), F(15, 8)):
            theta, exponents = module.dot_exponents(p)
            self.assertEqual(sum(theta), 1)
            for i in range(3):
                j, k = [s for s in range(3) if s != i]
                self.assertEqual(exponents[i], theta[i] / ((1 - theta[j]) * (1 - theta[k])))
            degree, target, _ = module.formal_powers(20, 4, 3, 5, 7, p)
            # Paper <r,l,h>: the h exponent is p1, not p3.
            expected = 7 ** int(degree * exponents[1])
            expected *= 3 ** int(degree * exponents[2])
            expected *= 5 ** int(degree * exponents[0])
            self.assertEqual(target, expected)

    def test_literal_parameter_branch_and_wrong_branch_rejection(self):
        self.assertTrue(module.source_branch(6, 4, F(7, 4)))
        self.assertFalse(module.source_branch(6, 4, F(19, 10)))
        module.formal_powers(6, 4, 5, 4, 5, F(7, 4))
        with self.assertRaises(ValueError):
            module.formal_powers(6, 4, 5, 4, 5, F(19, 10))
        for bad in (1, 2, F(5, 2), 1.5):
            with self.assertRaises(ValueError):
                module.parameter(bad)
        with self.assertRaises(ValueError):
            module.formal_powers(0, 4, 5, 4, 5, F(7, 4))

    def test_source_formula_from_generator_definition(self):
        # Directly evaluate the paper's generator formula to a clearing
        # power.  This independently checks the paired-source simplification.
        for n, b, p in ((6, 4, F(7, 4)), (20, 4, F(8, 5)), (9, 3, F(15, 8))):
            theta, exponents = module.dot_exponents(p)
            a_n = (n - theta[0]) / (1 - theta[0])
            a_b = (b - theta[1]) / (1 - theta[1])
            self.assertLessEqual(a_b, a_n)
            degree, _, source = module.formal_powers(n, b, n, b, n, p)
            generator_base = theta[0] * a_b + (1 - theta[0]) * a_n
            direct = a_b ** int(2 * degree * (1 - exponents[1]))
            direct *= generator_base ** int(2 * degree * exponents[1])
            self.assertEqual(source, direct)

    def test_exact_finite_witnesses_and_integer_repairs(self):
        for n, c, p in ((8, 0, F(15, 8)), (20, 1, F(8, 5)), (29, 2, F(3, 2))):
            row = module.finite_certificate(n, 4, n - c, 4, n - c, p)
            self.assertGreater(int(row["cleared_target_power"]), int(row["cleared_source_power"]))
            self.assertTrue(row["no_scalar_repair_ruled_out"])
            self.assertTrue(row["tested_formal_relation_ruled_out"])
        row = module.finite_certificate(20, 4, 19, 4, 19, F(8, 5), scalar_repair=2)
        self.assertEqual(row["certified_integer_scalar_repair_lower_bound"], 3)
        self.assertTrue(row["tested_formal_relation_ruled_out"])
        row = module.finite_certificate(20, 4, 19, 4, 19, F(8, 5), scalar_repair=3)
        self.assertFalse(row["tested_formal_relation_ruled_out"])
        # A simpler independent cleared-power witness, without helper algebra.
        self.assertGreater(2 ** 774, 53 ** 8 * 67 ** 120)
        self.assertGreater(2 ** 8 * 27 ** 6 * 4 ** 3, 11 ** 2 * 61 ** 6)

    def test_negative_and_equality_controls(self):
        active = module.finite_certificate(6, 4, 5, 4, 5, F(7, 4))
        self.assertFalse(active["no_scalar_repair_ruled_out"])
        equality = module.finite_certificate(8, 1, 8, 1, 8, F(15, 8))
        self.assertEqual(equality["target_power"], equality["source_power"])
        self.assertEqual(equality["gap_interval"], ["0", "0"])
        self.assertFalse(equality["tested_formal_relation_ruled_out"])
        self.assertFalse(module.coefficient_positive(1, F(3, 2)))

    def test_root_enclosures_against_exact_powers(self):
        for radicand, degree in ((F(0), 3), (F(81, 16), 4), (F(2), 7), (F(97, 5), 13)):
            lower, upper = module.root_interval(radicand, degree, bits=24)
            self.assertLessEqual(lower ** degree, radicand)
            self.assertGreaterEqual(upper ** degree, radicand)
            self.assertLessEqual(upper - lower, F(1, 2 ** 24))
        self.assertEqual(module.root_interval(F(81, 16), 4), (F(3, 2), F(3, 2)))

    def test_natural_log_constant_certificate_and_scope(self):
        report = module.certificate()
        self.assertEqual(report["logarithm_convention"], "natural logarithm")
        self.assertEqual(report["width_four_constant_rational_bracket"],
                         ["304118051531/1000000000000", "76029512883/250000000000"])
        self.assertGreater(report["finite_positivity_controls"], 1000)
        self.assertTrue(report["formal_preorder_only"])
        self.assertFalse(report["actual_tensor_degeneration_excluded"])
        self.assertFalse(report["improves_omega"])
        lo, hi = module.log_interval(F(7, 16))
        other_lo, other_hi = module.log_interval(F(16, 7))
        self.assertEqual((lo, hi), (-other_hi, -other_lo))
        self.assertEqual(module.logarithmic_constant_interval(1), (0, 0))


if __name__ == "__main__":
    unittest.main()

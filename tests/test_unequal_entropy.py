"""Exact controls for the all-size unequal-filtration certificate."""
from fractions import Fraction as Q
from itertools import product
import unittest

import importlib.util
from pathlib import Path

_PATH = Path(__file__).resolve().parents[1] / 'research/ai/2026-10-20-unequal-entropy/unequal_entropy.py'
_SPEC = importlib.util.spec_from_file_location('unequal_entropy', _PATH)
ue = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(ue)


class UnequalEntropyTests(unittest.TestCase):
    def test_complete_certificate_and_residual_partition(self):
        result = ue.report()
        self.assertEqual(len(result["all_large_cones"]), 8)
        self.assertEqual(len(result["small_minimum_tails"]), 72)
        self.assertEqual(sum(len(row["certificates"])
                             for row in result["small_minimum_tails"]), 216)
        self.assertEqual(result["finite_residual_count"], 37)
        self.assertEqual(max(max(row["source"])
                             for row in result["finite_residuals"]), 10)
        self.assertFalse(result["improves_omega"])
        for row in result["all_large_cones"]:
            self.assertGreater(row["minimum_normalized_coefficient"], 0)
        exceptional = [row["source"] for row in result["finite_residuals"]
                       if row["exceptional"]]
        self.assertEqual(exceptional, [[2, 2, 2, 2]])

    def test_cone_cover_and_scalar_polynomial_values(self):
        # Independently recover cone coordinates from all four-variable integer
        # tuples in this box after making a a minimum.  This checks both sides
        # of the two sum comparisons and all tie boundaries.
        checked = 0
        polynomials = {}
        for a in range(2, 6):
            for b, c, d in product(range(a, 10), repeat=3):
                sizes = {"a": a, "b": b, "c": c, "d": d}
                order = "".join(sorted("bcd", key=lambda label: (sizes[label], label)))
                ordered = [sizes[label] for label in order]
                x, y, z = ordered[0]-a, ordered[1]-ordered[0], ordered[2]-ordered[1]
                side = "auto"
                if order[-1] == "c":
                    if z <= x:
                        side, x = "lo", x-z
                    else:
                        side, z = "hi", z-x
                recovered = ue.cone_sizes(a, (x, y, z), order, side)
                self.assertEqual(recovered, sizes)
                key = (a, order, side)
                if key not in polynomials:
                    polynomials[key] = ue.inequality_polynomial(a, order, side, False)
                polynomial = polynomials[key]
                self.assertEqual(ue.evaluate(polynomial, (x, y, z)),
                                 ue.direct_inequality_value(sizes, a, False))
                checked += 1
        self.assertEqual(checked, 1196)

    def test_large_polynomial_against_independent_scalar_formula(self):
        for order, side in ue.cones():
            polynomial = ue.inequality_polynomial(11, order, side, True)
            for point in product((0, 1, 3), repeat=4):
                s, x, y, z = point
                sizes = ue.cone_sizes(11+s, (x, y, z), order, side)
                self.assertEqual(ue.evaluate(polynomial, point),
                                 ue.direct_inequality_value(sizes, 11, True))

    def test_sharp_constant_from_independent_radical_arithmetic(self):
        # B^3=(81/350)^3*(1+14sqrt(14)/27)^4.  Evaluate the fourth
        # power in Q[sqrt(14)] independently of the weight-sum formula.
        real, radical = Q(1), Q(0)
        for _ in range(4):
            real, radical = real+14*radical*Q(14,27), radical+real*Q(14,27)
        factor = Q(81,350)**3
        root_lo, root_hi = ue.sqrt_interval(Q(14))
        exact_lo = factor*(real+radical*root_lo)
        exact_hi = factor*(real+radical*root_hi)
        lo, hi = ue.ratio_cube_interval(2, 2, 2, 2)
        self.assertLessEqual(max(lo, exact_lo), min(hi, exact_hi))
        self.assertLess(Q(974772906,10**9)**3, exact_lo)
        self.assertLess(exact_hi, Q(974772907,10**9)**3)
        self.assertLess(Q(97,100)**3, lo)
        self.assertLess(hi, Q(39,40)**3)

    def test_shift_identity_and_negative_coefficient_control(self):
        polynomial = {(2, 1): Q(3,7), (1, 0): Q(-5,9), (0, 0): Q(2)}
        shifted = ue.shift(polynomial, 0, 3)
        for x, y in product(range(5), repeat=2):
            self.assertEqual(ue.evaluate(shifted, (x,y)),
                             ue.evaluate(polynomial, (x+3,y)))
        valid = ue.inequality_polynomial(11, "bdc", "hi", True)
        self.assertGreater(ue.coefficient_certificate(valid)["monomials"], 0)
        corrupted = dict(valid)
        corrupted[(0,0,0,0)] = Q(-1)
        with self.assertRaises(ArithmeticError):
            ue.coefficient_certificate(corrupted)


if __name__ == "__main__":
    unittest.main()

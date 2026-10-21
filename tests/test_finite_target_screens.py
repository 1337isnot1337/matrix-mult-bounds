"""Finite independent checks of the screening proof's ingredients and report."""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-koszul"))
import finite_target_screens as screens


class FiniteTargetScreenTests(unittest.TestCase):
    def test_binomial_normalization_small_matrix(self):
        self.assertEqual(screens.normalized_coefficients(2, 3), [
            [Fraction(1, 4), Fraction(1, 6), Fraction(1, 12)],
            [Fraction(1, 12), Fraction(1, 6), Fraction(1, 4)]])

    def test_off_diagonal_reduced_densities_vanish(self):
        for a, b in ((1, 1), (2, 3), (4, 4), (5, 9)):
            support = [(i, j, i+j) for i in range(a) for j in range(b)]
            for excluded_axis in range(3):
                pairs = [tuple(t[k] for k in range(3) if k != excluded_axis)
                         for t in support]
                self.assertEqual(len(set(pairs)), len(pairs))

    def test_entropy_ingredient_equality_and_strict_cases(self):
        # Endpoints with no other mass make the AM-GM coefficient bound exact.
        p = [Fraction(1, 2), Fraction(0), Fraction(1, 2)]
        self.assertEqual(screens.convolution(p, p),
                         [Fraction(1, 4), 0, Fraction(1, 2), 0, Fraction(1, 4)])
        r = screens.convolution([Fraction(1, 3)]*3, [Fraction(1, 3)]*3)
        self.assertGreater(r[2]**2, 4*r[0]*r[-1])

    def test_integer_width_cases(self):
        # All two-point potential ranges of width <=D, including permuted roles.
        for degree in range(1, 7):
            for u, v, w in product(range(degree+1), repeat=3):
                for common, first, second in ((v, u, w), (u, v, w), (w, u, v)):
                    if first+common <= degree and second+common <= degree:
                        if common:
                            self.assertLessEqual(u+v+w+1, 2*degree)
                        else:
                            self.assertLessEqual(first, degree)
                            self.assertLessEqual(second, degree)

    def test_a5_exact_improvement_and_scope(self):
        self.assertGreater(6**9*5**8*9**5, 28**12)
        self.assertLess(6**9*5**8*9**5*6561**9, 28**12*6563**9)
        # This particular rational entropy correction does not close a=6.
        d = 81*11**2
        self.assertGreater(6**9*6**8*11**5*d**9, 34**12*(d+2)**9)

    def test_laurent_output_boundary(self):
        self.assertEqual(screens.square_capacity(93, 12544), 79887)
        self.assertEqual(screens.square_capacity(94, 12544), 133480)
        self.assertEqual(screens.square_capacity(106, 12544), 913720)
        for n in range(94, 113):
            self.assertGreater(9*n*n+9*n+3-25088, 0)
            self.assertGreater(screens.square_capacity(n, 12544), 117649)

    def test_all_four_type_graphs_and_saved_report(self):
        result = screens.report()
        self.assertEqual(result["component_controls"]["count_vector_pairs"], 43681)
        self.assertEqual(result["convolution_controls"]["ordered_distribution_pairs"], 4877)
        self.assertEqual(len(result["uniform_marginal_records"]), 256)
        saved = json.loads((ROOT / "results/koszul-2026-10-20/finite_target_screens.json").read_text())
        self.assertEqual(result, saved)
        self.assertFalse(result["new_exponent_established"])


if __name__ == "__main__":
    unittest.main()

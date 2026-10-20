"""Controls for the low-border-rank algebra source and its extraction score."""
from fractions import Fraction
from pathlib import Path
import sys
import unittest

AI = Path(__file__).resolve().parents[1] / "research/ai"
sys.path.insert(0, str(AI / "2026-10-20-truncated-algebras"))
import truncated_search as truncated
import product_search as product_source
import source_certificates as certificates
import two_sector


class TruncatedAlgebraTests(unittest.TestCase):
    def test_cyclic_tensor_leading_support(self):
        for r in range(2, 9):
            cyclic = [(i, j, k) for i in range(r) for j in range(r) for k in range(r)
                      if (i + j + k) % r == r - 1]
            minimum = min(sum(point) for point in cyclic)
            self.assertEqual(minimum, r - 1)
            self.assertEqual([p for p in cyclic if sum(p) == minimum],
                             [(i, j, r - 1 - i - j) for i in range(r) for j in range(r - i)])

    def test_source_three_known_score(self):
        result = truncated.search_size(3)
        self.assertEqual(result["candidate_cases"], 49)
        self.assertEqual(result["distinct_supports"], 21)
        self.assertEqual(Fraction(result["best"]["score_lower"]), 4)
        self.assertEqual(result["strict_critical_parameter_violations"], [])

    def test_output_restriction_recovers_strassen_sector(self):
        weak = truncated.search_size(4)
        strong = truncated.search_size(4, delete_outputs=True)
        self.assertEqual(Fraction(weak["best"]["score_lower"]), 5)
        self.assertEqual(Fraction(strong["best"]["score_lower"]), 6)
        self.assertEqual(strong["strict_critical_parameter_violations"], [])

    def test_digit_product_degeneration(self):
        for a, b in [(2, 2), (2, 3), (3, 3), (4, 5)]:
            report = certificates.verify_digit_product(a, b)
            self.assertEqual(report["source_rank_bound"], a * b)

    def test_standard_cw_border_coefficients(self):
        for q in range(1, 9):
            report = certificates.verify_cw(q)
            self.assertEqual(report["rank_one_terms"], q + 2)
            self.assertEqual(report["leading_tensor_terms"], 3 * q + 3)
            self.assertEqual(report["negative_powers"], 0)

    def test_coupled_weight_sampling_reproducible(self):
        actual = list(product_source.weights(9, 20, 123456))
        self.assertEqual(actual, list(product_source.weights(9, 20, 123456)))
        self.assertTrue(all(min(x) == min(y) == 0 for x, y in actual))
        self.assertTrue(any(any(x[i * 3 + j] - x[i * 3] - x[j] + x[0] != 0
                                for i in range(3) for j in range(3)) for x, y in actual))

    def test_nonfree_slice_count_rejected(self):
        with self.assertRaises(ValueError):
            truncated.search_size(2, terms=[(0, 0, 0), (0, 0, 1)])

    def test_two_sector_coefficients(self):
        for a, b in [(1, 1), (4, 1), (7, 3), (3, 9)]:
            result = two_sector.coefficient_certificate(a, b)
            self.assertEqual(result["retained_terms"], [a * b, a * b])

    def test_amplitude_polynomials(self):
        import sympy as sp
        x = sp.symbols("x")
        self.assertEqual(sp.expand(9 * (x + 2)**4 - 16 * (2*x + 1)**3
                                   - (x - 4)**2 * (9*x*x + 16*x + 8)), 0)
        self.assertEqual(sp.expand(27*x**4 - 16*(2*x - 1)**3
                                   - (x - 2)**2 * (27*x*x - 20*x + 4)), 0)

    def test_small_two_sector_profile_control(self):
        result = two_sector.run(8)
        self.assertEqual(result["best_ratio_cubed"], "27/32")
        self.assertEqual(result["amplitude_upper_cubed"], "16/9")


if __name__ == "__main__":
    unittest.main()

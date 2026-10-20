"""Controls for the low-border-rank algebra source and its extraction score."""
from fractions import Fraction
from pathlib import Path
import sys
import unittest

AI = Path(__file__).resolve().parents[1] / "research/ai"
sys.path.insert(0, str(AI / "2026-10-20-truncated-algebras"))
import truncated_search as truncated


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


if __name__ == "__main__":
    unittest.main()

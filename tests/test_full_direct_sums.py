"""Independent assignment, root, and tensor-coefficient checks."""
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-affine-direct-sums"))
import full_direct_sums as full
import tensor_certificate as tensor


class FullDirectSumTests(unittest.TestCase):
    def test_interval_fourth_power_certificate(self):
        for value in [Fraction(1), Fraction(81, 16), Fraction(56, 9),
                      Fraction(17, 31), Fraction(10**70 + 3, 7**23)]:
            lower, upper = full.power_interval(value, 96)
            target = value.numerator**3 * 2**384
            denominator = value.denominator**3
            self.assertLessEqual(lower**4 * denominator, target)
            self.assertGreaterEqual(upper**4 * denominator, target)
            self.assertLessEqual(upper - lower, 1)
        self.assertEqual(full.power_interval(Fraction(81, 16), 8), (864, 864))

    def test_assignment_against_independent_enumeration(self):
        for table in [[[100, 99], [98, 1]], [[4, 9], [8, 1], [6, 7]],
                      [[1, 7, 3], [8, 1, 4]], [[7]]]:
            rows = list(zip(*table)) if len(table) > len(table[0]) else table
            brute = max(sum(rows[i][j] for i, j in enumerate(choice))
                        for choice in permutations(range(len(rows[0])), len(rows)))
            value, pairs = full.maximum_matching(table)
            self.assertEqual(value, brute)
            self.assertEqual(value, sum(table[i][j] for i, j in pairs))
            self.assertEqual(len(set(i for i, j in pairs)), len(pairs))
            self.assertEqual(len(set(j for i, j in pairs)), len(pairs))

    def test_degenerate_lines_rejected(self):
        for line in [(0, 1, 0), (1, 0, 0), (1, 1, 0), (1.5, -1, 0)]:
            with self.assertRaises(ValueError):
                full.line_certificate(3, 3, 3, 3, *line)

    def test_actual_coefficients_in_independent_bases(self):
        for dims, line in [((2, 2, 2, 2), (1, -1, 0)),
                           ((3, 2, 2, 3), (1, -1, 0)),
                           ((3, 3, 3, 3), (2, -1, 0)),
                           ((3, 3, 3, 3), (2, 1, -2))]:
            with self.subTest(dims=dims, line=line):
                result = tensor.verify_tensor(*dims, *line)
                self.assertGreater(result["coefficients_checked"], 0)
                self.assertGreater(result["surviving_coefficients"], 0)

    def test_small_exhaustive_matching_bound(self):
        result = full.run(4)
        self.assertEqual(result["source_quadruples"], 256)
        self.assertEqual(result["violations"], 0)
        best = result["best_nontrivial_upper_bound"]
        self.assertEqual(best["source"], [2, 2, 2, 2])
        self.assertLess(Fraction(best["ratio_upper_bound"]), Fraction(82, 100))

    def test_recorded_report_and_weights(self):
        report = json.loads((ROOT / "results/affine-direct-sums-2026-10-20/full_direct_sums.json").read_text())
        self.assertEqual(report["source_quadruples"], 6561)
        self.assertEqual(report["single_block_cases_exact_rational"]
                         + report["nontrivial_matching_cases_certified"], 6561)
        self.assertEqual(report["maximal_relaxed_matchings_covered"], 9600473)
        self.assertEqual(report["smallest_diagonal_extraction"],
                         full.line_certificate(2, 2, 2, 2))


if __name__ == "__main__":
    unittest.main()

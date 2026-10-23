"""Exact conditional search gates and residual-rank corruption controls."""

from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "residual_rank_repair",
    ROOT / "research/ai/2026-10-23-residual-rank-repair/verify.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ResidualRankRepairTests(unittest.TestCase):
    def test_exact_gate_budgets_and_missing_construction(self):
        report = MODULE.verify()
        self.assertEqual(report["first_no_residual_thresholds"], [
            {"outer_deficit": 0, "first_source_n": 38},
            {"outer_deficit": 1, "first_source_n": 64},
        ])
        self.assertEqual([row["largest_single_residual_pair_product"]
                          for row in report["single_residual_product_budgets"]],
                         [0, 230, 2121, 18393, 80775, 8739465])
        self.assertFalse(report["successful_paired_map_constructed"])
        self.assertFalse(report["improves_omega"])

    def test_single_finite_dense_output_defect(self):
        good = MODULE.finite_gate(200, 4, 199, 4, 199, [(2, 796, 796)])
        bad = MODULE.finite_gate(200, 4, 199, 4, 199, [(3, 796, 796)])
        self.assertEqual(good["residual_pair_products"], [1592])
        self.assertEqual(good["outcome"], "strict-gate-certified")
        self.assertEqual(bad["outcome"], "gate-not-satisfied")
        # Rank dimensions alone never certify the required tensor identity.
        self.assertFalse(good["construction_certified"])

    def test_radical_equality_and_no_false_strict_decision(self):
        self.assertEqual(MODULE.root_interval(Fraction(81, 16), 4),
                         (Fraction(3, 2), Fraction(3, 2)))
        lo, hi = MODULE.root_interval(2, 2, 20)
        self.assertLess(lo * lo, 2)
        self.assertGreater(hi * hi, 2)
        # An algebraic equality between nonrational radicals must never pass.
        # n=1,b=36 gives source^4=4*37^6=(4*37^2)^3.
        volume = 4 * 37**2
        self.assertEqual(Fraction(2 * 36 * 37**3, 9)**2, volume**3)
        equality = MODULE.finite_gate(1, 36, volume, 1, 1)
        self.assertNotEqual(equality["outcome"], "strict-gate-certified")
        self.assertLessEqual(Fraction(*equality["gap_interval"][0]), 0)
        self.assertGreaterEqual(Fraction(*equality["gap_interval"][1]), 0)
        with self.assertRaises(ValueError):
            MODULE.finite_gate(0, 4, 5, 4, 5)
        with self.assertRaises(ValueError):
            MODULE.pair_product([1, -2, 3])

    def test_dense_rank_one_and_damaged_support_certificate(self):
        a, b, c = [1, 2, -1], [2, -3], [1, 4, 2]
        tensor = {(i, j, k): x * y * z
                  for i, x in enumerate(a)
                  for j, y in enumerate(b)
                  for k, z in enumerate(c)}
        self.assertEqual(MODULE.flattening_ranks(tensor, [3, 2, 3]), [1, 1, 1])
        damaged = dict(tensor)
        damaged[(0, 0, 0)] += 1
        self.assertEqual(MODULE.flattening_ranks(damaged, [3, 2, 3]), [2, 2, 2])
        self.assertEqual(MODULE.pair_product([2, 2, 2]), 4)
        self.assertEqual(MODULE.flattening_ranks({}, [3, 2, 3]), [0, 0, 0])

    def test_corner_control_and_broken_scalar_product(self):
        tensor, shape = MODULE.missing_corner_residual(5, 4)
        self.assertEqual(len(tensor), 36)
        self.assertEqual(MODULE.flattening_ranks(tensor, shape), [9, 20, 20])
        # Deleting every contribution of one missing output changes its A rank.
        damaged = {index: value for index, value in tensor.items() if index[0] != 24}
        self.assertEqual(MODULE.flattening_ranks(damaged, shape)[0], 8)
        self.assertNotEqual(tensor, damaged)

    def test_minimum_paired_source_format_census(self):
        passing = []
        for n in range(1, 22):
            for b in range(1, 22):
                if max(n*n, b*(n+b-1)) <= 441:
                    integer_gate = 81*b*n**6 > 4*(2*n+b-1)**6
                    if integer_gate:
                        passing.append((n, b))
        self.assertEqual(passing, [(21, 8), (21, 9)])
        for n, b, d in [(22, 7, 4), (22, 8, 9), (22, 9, 10)]:
            self.assertEqual(MODULE.largest_single_product(n, b, n, b, n), d)


if __name__ == "__main__":
    unittest.main()

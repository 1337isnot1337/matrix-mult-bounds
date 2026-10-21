"""Check cyclic-source indices and exact minimum-rank proof controls."""
from itertools import product
import json
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-koszul"))
import cyclic_finite_target as cyclic


class CyclicFiniteTargetTests(unittest.TestCase):
    def test_three_factor_index_formula(self):
        a = 3
        direct = {}
        for i, j, p, q, r, s in product(range(a), repeat=6):
            direct[((j, p, r+s), (i+j, q, r))] = (i, p+q, s)
        f = list(range(1, a*a*(2*a-1)+1))
        for row in product(range(a), range(a), range(2*a-1)):
            for col in product(range(2*a-1), range(a), range(a)):
                index = direct.get((row, col))
                expected = cyclic.coefficient(f, a, *index) if index is not None else 0
                self.assertEqual(cyclic.slice_entry(f, a, row, col), expected)

    def test_minimum_is_attained_in_characteristic_zero(self):
        for a in range(1, 5):
            f = [1]+[0]*(a*a*(2*a-1)-1)
            rows = list(product(range(a), range(a), range(2*a-1)))
            cols = list(product(range(2*a-1), range(a), range(a)))
            support = [(i, j) for i, row in enumerate(rows) for j, col in enumerate(cols)
                       if cyclic.slice_entry(f, a, row, col)]
            self.assertEqual(len(support), a*a)
            self.assertEqual(len({i for i, _ in support}), a*a)
            self.assertEqual(len({j for _, j in support}), a*a)

    def test_triangular_minor_determinants(self):
        # Vary the last nonzero indices, not just dense slices with maximal pivots.
        for a in (2, 3):
            for i, k, s in product(range(a), range(2*a-1), range(a)):
                f = [0]*(a*a*(2*a-1))
                for ii in range(i+1):
                    for ss in range(a if ii < i else s+1):
                        f[(ii*(2*a-1)+k)*a+ss] = ii+2*ss+1
                minor = cyclic.triangular_minor(f, a)
                self.assertEqual(sp.Matrix(minor["matrix"]).det(), minor["pivot"]**(a*a))

    def test_integer_target_certificate_and_frontier(self):
        self.assertGreater(237600**281, 22**1125)
        for a in (1, 2, 3):
            self.assertEqual(cyclic.improving_frontier(a)["improving_sorted_shapes"], [])
        records = cyclic.improving_frontier(4)["improving_sorted_shapes"]
        self.assertEqual([x["shape"] for x in records], [[10, 10, 11]])
        self.assertEqual(records[0]["constant_restriction_slacks"], [8, 8, -1])
        a5 = cyclic.improving_frontier(5)["improving_sorted_shapes"]
        self.assertEqual(len(a5), 7)
        self.assertEqual(sum(not x["minimum_slice_rank_excluded"] for x in a5), 5)
        self.assertEqual(sum(not x["constant_restriction_excluded"] for x in a5), 4)
        self.assertTrue(a5[0]["minimum_rank_locus_excluded"])

    def test_complete_binary_control_and_report(self):
        result = cyclic.report()
        self.assertEqual(result["binary_slice_controls"]["nonzero_slices"], 4095)
        self.assertEqual(result["binary_slice_controls"]["minimum_rank"], 4)
        self.assertEqual(len(result["binary_slice_controls"]["minimum_rank_encoded_slices"]), 27)
        self.assertTrue(result["binary_slice_controls"]["minimum_rank_classification_matches"])
        saved = json.loads((ROOT / "results/koszul-2026-10-20/cyclic_finite_target.json").read_text())
        self.assertEqual(result, saved)
        self.assertFalse(result["new_exponent_established"])
        self.assertFalse(result["finite_target"]["general_degeneration_excluded"])


if __name__ == "__main__":
    unittest.main()

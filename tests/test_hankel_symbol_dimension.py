"""Exact finite checks of the ordinary symbol-dimension obstruction."""

import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/"research/ai/2026-10-20-anisotropic-constructions"
sys.path.insert(0, str(PACKAGE))
import hankel_symbol_dimension as symbol


class HankelSymbolDimensionTests(unittest.TestCase):
    def test_saved_exact_controls(self):
        actual = json.loads(json.dumps(symbol.report()))
        saved = json.loads((ROOT/"results/anisotropic-constructions-2026-10-20/hankel-symbol-dimension-controls.json").read_text())
        self.assertEqual(actual, saved)
        self.assertEqual(sum(x["nonzero_sequences"] for x in actual["binary_hankel_controls"]), 1341)
        self.assertEqual(actual["hermite_interpolation_controls"]["total_schemes"], 1000)
        self.assertFalse(actual["singular_exclusion_claimed"])
        self.assertFalse(actual["new_exponent_established"])

    def test_strict_threshold_and_first_larger_candidate(self):
        self.assertEqual(symbol.allowed_ranks(5, 6), [1, 2, 3])
        self.assertEqual(symbol.allowed_ranks(3, 3), [1])
        for sizes in ((16,), (16, 4), (16, 3, 2, 1, 1)):
            self.assertTrue(symbol.square_block_tests(5, 6, sizes)["ordinary_restriction_excluded"])
        self.assertFalse(symbol.square_block_tests(5, 6, (15, 4, 2, 1, 1))["ordinary_restriction_excluded"])
        self.assertFalse(symbol.square_block_tests(7, 8, (25, 5))["ordinary_restriction_excluded"])

    def test_variable_scheme_projection_counts_coefficients(self):
        result = symbol.variable_scheme_projection_control()
        self.assertEqual(result["coefficient_space_dimension"], 12)
        self.assertEqual(result["projected_coefficient_rank_mod_101"], 12)
        self.assertEqual(result["coefficient_dimension_bound"], 60)
        self.assertFalse(result["constant_scheme_claimed"])
        for row in symbol.scheme_line_boundary_controls():
            self.assertEqual(row["sequence_length"], row["three_r"]-1)
            self.assertEqual(row["hankel_ranks_mod_101"], [row["rank"]]*4)
            self.assertNotIn(row["rank"], symbol.allowed_ranks(row["a"], row["b"]))


if __name__ == "__main__":
    unittest.main()

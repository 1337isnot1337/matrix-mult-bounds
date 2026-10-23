"""Controls for the border-rank margin, not only first-flattening rank."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "laurent_rank_margin",
    ROOT / "research/ai/2026-10-23-laurent-channel-barrier/rank_margin.py")
margin = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(margin)


def rational_rank(matrix):
    rows = [[sum(Fraction(coefficient)*Fraction(2)**t
                 for (_, _, t), coefficient in entry.items())
             for entry in row] for row in matrix]
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        lead = rows[rank][col]
        rows[rank] = [x/lead for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col]:
                factor = rows[i][col]
                rows[i] = [x-factor*y for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


class LaurentRankMarginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = margin.certificate()

    def test_complete_saved_control_replay(self):
        saved = json.loads((ROOT / "results/laurent-channel-barrier-2026-10-23/rank-margin-controls.json").read_text())
        self.assertEqual(self.report, saved)

    def test_zero_good_subspace_does_not_create_a_spurious_bound(self):
        for h in range(2, 7):
            for rho in range(h):
                self.assertEqual(margin.lower_bound(0, h, rho), 0)
        for args in [(-1, 4, 1), (1, 1, 0), (1, 4, 4), (1, 4, -1)]:
            with self.assertRaises(ValueError):
                margin.lower_bound(*args)

    def test_auxiliary_border_rank_really_exceeds_its_first_flattening(self):
        case = self.report["sharp_projector_cases"][0]
        self.assertEqual(case["auxiliary_first_flattening_rank"], 1)
        self.assertEqual(case["auxiliary_border_rank"], 3)
        for h, rho in [(4, 1), (5, 2), (5, 4)]:
            s_terms, e_terms = margin.projector_data(h, rho)
            self.assertEqual(rational_rank(margin.matrix_sum(s_terms, h)), rho)
            self.assertEqual(rational_rank(margin.matrix_sum(e_terms, h)), h-rho)
            for k in range(len(e_terms)):
                self.assertEqual(rational_rank(margin.matrix_sum(
                    s_terms+e_terms[:k]+e_terms[k+1:], h)), h-1)

    def test_rank_one_channel_encoding_retains_every_pole(self):
        row = self.report["rank_one_channel_encoding"]
        self.assertEqual(row["native_rank_one_coefficient_positions"], 54)
        self.assertEqual(row["zero_two_by_two_minors"], 9)
        self.assertGreater(row["negative_coefficients_retained"], 0)

    def test_substitution_must_exceed_the_full_local_pole_budget(self):
        rows = {row["N"]: row for row in self.report["auxiliary_border_substitution"]}
        self.assertTrue(rows[4]["total_has_poles"])
        self.assertTrue(rows[4]["raw_constant_matches_target"])
        self.assertFalse(rows[4]["regular_with_correct_target"])
        self.assertFalse(rows[5]["raw_constant_matches_target"])
        self.assertFalse(rows[5]["regular_with_correct_target"])
        self.assertTrue(rows[6]["regular_with_correct_target"])
        self.assertEqual(rows[6]["mapped_error_order"], 1)

    def test_paired_corollary_keeps_the_two_rank_statements_separate(self):
        row = self.report["paired_control"]
        self.assertEqual(row["kernel_dimension_lower_bound"], 16)
        self.assertEqual(row["strengthened_auxiliary_border_rank_lower_bound"], 18)
        self.assertEqual(row["generic_channel_rank_cap"], 1)


if __name__ == "__main__":
    unittest.main()

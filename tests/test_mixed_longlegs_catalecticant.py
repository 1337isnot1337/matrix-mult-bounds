"""Literal convention and covariance checks for the regular first-map chart."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-mixed-longlegs-candidate"
SPEC = importlib.util.spec_from_file_location("mixed_longlegs_catalecticant", PACKAGE / "verify_catalecticant.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def transform_long_coefficients(tensor, left, right):
    b, c, entries = tensor
    result = {}
    for i, j, k in entries:
        for new_j in range(b):
            for new_k in range(c):
                value = left[new_j][j] * right[new_k][k]
                if value:
                    VERIFY.BASE.add(result, (i, new_j, new_k), value)
    return b, c, [(i, j, k, value) for (i, j, k), value in result.items()]


def explicit_kronecker_action(tensor, left, right):
    b, c, _ = tensor
    _, original = VERIFY.rows_for_tensor(*tensor)
    result = [{} for _ in range(3 * c)]
    for row, values in enumerate(original):
        r, old_k = divmod(row, c)
        for column, coefficient in values.items():
            s, old_j = divmod(column, b)
            for new_k in range(c):
                for new_j in range(b):
                    value = right[new_k][old_k] * coefficient * left[new_j][old_j]
                    if value:
                        VERIFY.BASE.add(result[r * c + new_k], s * b + new_j, value)
    return 3 * b, result


class MixedLonglegsCatalecticantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = VERIFY.report()

    def test_saved_report_and_chart_scope(self):
        saved = json.loads((ROOT / "results/mixed-longlegs-candidate-2026-10-23/catalecticant_verification.json").read_text())
        self.assertEqual(saved, self.report)
        self.assertEqual((self.report["source_rank"], self.report["target_universal_lower_bound"]), (120, 130))
        self.assertEqual(self.report["necessary_leading_first_rank_range"], [1, 4])
        self.assertFalse(self.report["arbitrary_singular_first_maps_excluded"])
        self.assertEqual(self.report["singular_first_projection_diagnostic"]["target_rank"], 62)

    def test_canonical_and_changed_first_basis_controls(self):
        self.assertEqual(len(self.report["width_and_output_controls"]), 25)
        self.assertEqual(len(self.report["first_frame_controls"]), 6)
        for frame in self.report["first_frame_controls"]:
            self.assertGreaterEqual(frame["target_rank"], 130)
        self.assertEqual(len(self.report["quadratic_contraction_controls"]), 26)
        self.assertTrue(all(row["rank"] == 3 for row in self.report["quadratic_contraction_controls"]))

    def test_long_factor_covariance_from_separate_literal_constructions(self):
        for tensor in (VERIFY.full(2), VERIFY.output_block(3, 3), VERIFY.full(2, True)):
            b, c, _ = tensor
            left = [[int(i == j) + (i + 1 if j == i + 1 else 0)
                     for j in range(b)] for i in range(b)]
            right = [[int(i == j) + (j + 2 if i == j + 1 else 0)
                      for j in range(c)] for i in range(c)]
            changed = VERIFY.rows_for_tensor(*transform_long_coefficients(tensor, left, right))
            expected = explicit_kronecker_action(tensor, left, right)
            self.assertEqual(changed, expected)
            self.assertEqual(VERIFY.BASE.rational_rank(changed[1]), VERIFY.rank_for_tensor(tensor))

    def test_mid_transpose_after_nontrivial_first_change(self):
        frame = VERIFY.first_frames()["upper_unipotent"]
        for width in (1, 2, 5):
            original = VERIFY.rows_for_tensor(*VERIFY.full(width), first=frame)
            swapped = VERIFY.rows_for_tensor(*VERIFY.full(width, True), first=frame)
            self.assertEqual(VERIFY.transpose_rows(*original), swapped)


if __name__ == "__main__":
    unittest.main()

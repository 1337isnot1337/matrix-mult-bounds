"""Exact checks for the single-copy interpolation-factor incidence result."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-mixed-family-single-copy"
RESULT = ROOT / "results/mixed-family-single-copy-2026-10-23/rank10-shared-points.json"
SPEC = importlib.util.spec_from_file_location(
    "mixed_family_shared_points", PACKAGE / "verify_rank10_shared_points.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def independent_rank(matrix):
    """Rational row reduction, independent of the package Bareiss determinant."""
    a = [[Fraction(value) for value in row] for row in matrix]
    rows, columns = len(a), len(a[0])
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if a[row][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][column]
        a[rank] = [value / scale for value in a[rank]]
        for row in range(rows):
            if row != rank and a[row][column]:
                scale = a[row][column]
                a[row] = [x - scale * y for x, y in zip(a[row], a[rank])]
        rank += 1
    return rank


class MixedFamilySingleCopyTests(unittest.TestCase):
    def test_saved_exact_certificate(self):
        self.assertEqual(json.loads(RESULT.read_text()), VERIFY.report())

    def test_quadratic_conditions_are_independent(self):
        labels, points = VERIFY.nodes_and_points()
        monomials, matrix = VERIFY.quadratic_evaluation_matrix(points)
        self.assertEqual(len(labels), 10)
        self.assertEqual(len(monomials), 10)
        self.assertEqual(independent_rank(matrix), 10)
        self.assertEqual(VERIFY.determinant_bareiss(matrix), 1)
        self.assertTrue(VERIFY.projectively_distinct(points))

    def test_standard_source_evaluation_factors_lie_on_three_quadrics(self):
        for t in range(-3, 8):
            point = (1, t, t * t, t * t * t)
            self.assertEqual(point[0] * point[2] - point[1] ** 2, 0)
            self.assertEqual(point[0] * point[3] - point[1] * point[2], 0)
            self.assertEqual(point[1] * point[3] - point[2] ** 2, 0)


if __name__ == "__main__":
    unittest.main()

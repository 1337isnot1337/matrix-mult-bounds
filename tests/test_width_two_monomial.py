"""All-support checks and controls for the width-two score theorem."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-width-two-monomial'
spec = importlib.util.spec_from_file_location('width_two_verify', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class WidthTwoMonomialTests(unittest.TestCase):
    def test_every_support_in_both_orientations_replays_recorded_census(self):
        report = verify.census(10)
        recorded = json.loads((ROOT / 'results/width-two-monomial-2026-10-23/census.json').read_text())
        self.assertEqual(report, recorded)
        self.assertEqual(report['orientation_support_checks'], 59046)

    def test_huge_affine_gauge_preserves_the_literal_support_and_score(self):
        scorer = verify.load_scorer()
        b = 97
        values = verify.weights_for_signs(tuple((-1, 0, 1, 0) * 24))
        slope, x_shift, y_shift = 10 ** 80, -(10 ** 100), 10 ** 120
        wx = (x_shift, x_shift + slope)
        wy = tuple(y_shift + slope * j + value for j, value in enumerate(values))
        self.assertEqual(scorer.components(wx, wy)[0], scorer.components((0, 0), values)[0])
        expected = verify.short_shared_prediction((0, 0), values)
        self.assertEqual(verify.short_shared_prediction(wx, wy), expected)
        score, _ = verify.original_score(scorer, wx, wy, scorer.slopes(b + 1))
        self.assertEqual(score, expected['score'])
        score, _ = verify.original_score(scorer, wy, wx, scorer.slopes(b + 1))
        self.assertEqual(score, verify.short_second_prediction(wy, wx))

    def test_isolated_vertex_orientation_and_sharp_gaps(self):
        isolated = verify.short_shared_prediction((0, 0), (0, 1, 0))
        self.assertEqual(isolated['inactive_y'], 1)
        self.assertEqual(isolated['deficit'], Fraction(2, 3))
        equality_weights = (0, 1, 1, 0)
        self.assertEqual(verify.short_shared_prediction((0, 0), equality_weights)['deficit'], 0)
        self.assertEqual(verify.short_second_prediction(equality_weights, (0, 0)), 3)
        for b in (2, 3, 10, 97):
            self.assertEqual(verify.short_shared_prediction((0, 0), (0,) * (b - 1) + (1,))['deficit'], Fraction(1, 3))
            self.assertEqual(verify.short_second_prediction(tuple(range(b)), (0, 0)), b + 1)

    def test_equality_count_recurrence_and_exponential_census_counts(self):
        counts = [0] + [verify.equality_count(b) for b in range(1, 101)]
        self.assertEqual(counts[1:11], [1, 1, 1, 2, 4, 7, 12, 21, 37, 65])
        for b in range(4, 101):
            self.assertEqual(counts[b], 2 * counts[b - 1] - counts[b - 2] + counts[b - 3])
            self.assertLessEqual(counts[b], 3 ** (b - 1))

    def test_invalid_dimensions_are_rejected(self):
        with self.assertRaises(ValueError):
            verify.short_shared_prediction((0,), (0, 0))
        with self.assertRaises(ValueError):
            verify.short_second_prediction((0, 0), (0, 0, 0))
        with self.assertRaises(ValueError):
            verify.weights_for_signs((2,))


if __name__ == '__main__':
    unittest.main()

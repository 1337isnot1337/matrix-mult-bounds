"""Exact finite regressions for the higher-Hankel necessary-condition screen."""

import importlib.util
from pathlib import Path
import unittest


PACKAGE = Path(__file__).resolve().parents[1]/'research/ai/2026-10-20-hankel-segre'


def load_module(name):
    spec = importlib.util.spec_from_file_location(name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


frontier = load_module('higher_hankel_frontier')
controls = load_module('hankel_segre_controls')


class HigherHankelTests(unittest.TestCase):
    def test_selected_targets_are_excluded(self):
        self.assertEqual(frontier.block_exclusions(5, 6, 272, 16), [2, 3])
        self.assertEqual(frontier.block_exclusions(5, 6, 256, 16), [3])
        self.assertFalse(frontier.target_check(5, 6, [16, 4])['ordinary_screen_passes'])

    def test_frontier_survivor_has_certified_score(self):
        shape = [25, 5, 2, 1, 1]
        self.assertTrue(frontier.target_check(7, 8, shape)['ordinary_screen_passes'])
        lower = sum(frontier.score_interval(n)[0] for n in shape)
        self.assertGreater(lower, 43**3*frontier.SCALE)
        self.assertEqual(sum(n*n for n in shape), 656)

    def test_repeated_points_and_infinity(self):
        report = controls.report()
        self.assertEqual(report['hermite_intersections']['ordered_intersection_checks'], 1225)
        self.assertEqual([r['source_slice_rank'] for r in report['coherent_source_controls']],
                         [24, 24, 24, 72])
        self.assertFalse(report['new_exponent_established'])

    def test_line_hypothesis_cannot_be_removed(self):
        # For degree 4, r=2, this whole line has Hankel rank <=2,
        # although its endpoint minimal divisors have union length 4.
        # The line lemma explicitly requires degree >=5 in this case.
        f = controls.jet_vector(4, 0, 1)
        g = controls.jet_vector(4, None, 1)
        self.assertEqual(controls.rank_mod(controls.hankel(f, 3, 3)), 2)
        self.assertEqual(controls.rank_mod(controls.hankel(g, 3, 3)), 2)
        for scalar in range(controls.PRIME):
            sequence = [x+scalar*y for x, y in zip(f, g)]
            self.assertEqual(controls.rank_mod(controls.hankel(sequence, 3, 3)), 2)


if __name__ == '__main__':
    unittest.main()

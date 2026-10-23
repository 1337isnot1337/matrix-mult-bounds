"""Proof-specific controls for the unequal paired-source continuation."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-20-unequal-paired'
RESULTS = ROOT / 'results/unequal-paired-2026-10-20'
SPEC = importlib.util.spec_from_file_location('unequal_paired_test_subject', PACKAGE / 'unequal_paired.py')
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)
EDGE_SPEC = importlib.util.spec_from_file_location(
    'unequal_paired_edge_test_subject', PACKAGE / 'edge_ordinary.py')
edge_module = importlib.util.module_from_spec(EDGE_SPEC)
EDGE_SPEC.loader.exec_module(edge_module)


class UnequalPairedTests(unittest.TestCase):
    def test_independent_coefficient_maps(self):
        expected = json.loads((RESULTS / 'coefficient-controls.json').read_text())
        self.assertEqual(module.coefficient_controls(), expected)
        self.assertEqual(len(expected['mod2_records']), 437)
        self.assertEqual(len(expected['odd_prime_records']), 12)

    def test_full_stated_frontier(self):
        expected = json.loads((RESULTS / 'frontier.json').read_text())
        self.assertEqual(module.finite_frontier(), expected)
        self.assertEqual(expected['source_count'], 15327)
        self.assertEqual(expected['surviving_source_count'], 121)
        self.assertEqual(expected['records'][0]['source'], [10, 9, 12, 12])

    def test_selected_target_and_conditional_certificate(self):
        expected = json.loads((RESULTS / 'selected-target.json').read_text())
        self.assertEqual(module.selected_target_certificate(), expected)
        self.assertEqual(len(expected['first_leg_Koszul']), 120)
        self.assertTrue(all(row['source_rank'] > row['target_rank']
                            for row in expected['first_leg_Koszul']))
        self.assertFalse(expected['constructed'])
        self.assertFalse(expected['improves_omega'])

    def test_equal_source_specialization_and_transpose(self):
        for a in range(2, 13):
            for power in range(a * a):
                self.assertEqual(module.source_rank(a, a, a, a, power),
                                 module.matrix_reference.source_rank(a, power))
        for source in [(2, 1, 3, 7), (4, 3, 6, 9), (10, 9, 12, 12)]:
            a, b, c, d = source
            v = a * c
            for power in range(v):
                self.assertEqual(module.source_rank(a, b, c, d, power),
                                 module.source_rank(c, d, a, b, v - power - 1))

    def test_hypotheses_and_outside_range_counterexample(self):
        for source in [(3, 1, 2, 2), (2, 2, 4, 1), (1, 2, 3, 3)]:
            with self.assertRaises(ValueError):
                module.source_rank(*source, 1)
        # Without the a<=b+1 hypothesis, the displayed polynomial can exceed
        # the entire domain. A source tensor still exists, but formula (1) is
        # not its rank formula in that region.
        source = (4, 1, 2, 2)
        v, y, z = module.source_format(*source)
        unchecked = y * (v - 2) + z + 2 * (source[0] - 1) * (source[2] - 1)
        self.assertGreater(unchecked, v * y)
        self.assertEqual(module.coefficient_rank_mod2(*source, 1), v * y)

    def test_universal_upper_bound_controls(self):
        expected = json.loads((RESULTS / 'upper-bound-controls.json').read_text())
        self.assertEqual(module.upper_bound_controls(), expected)
        self.assertTrue(all(row['rank_mod2'] <= row['upper_bound']
                            for row in expected['mod2_records']))
        self.assertTrue(all(row['rank'] <= row['upper_bound']
                            for row in expected['odd_prime_records']))
        for source in [(2, 1, 3, 7), (4, 3, 6, 9), (10, 9, 12, 12)]:
            for power in range(source[0] * source[2]):
                self.assertEqual(module.source_rank(*source, power),
                                 module.source_rank_upper(*source, power))

    def test_edge_exclusion_on_other_leg(self):
        expected = json.loads((RESULTS / 'edge-exclusion.json').read_text())
        self.assertEqual(module.excluded_edge_certificate(), expected)
        self.assertEqual(expected['gap'], 366737896009212)
        self.assertTrue(expected['excluded_under_arbitrary_degeneration'])
        self.assertFalse(expected['improves_omega'])

    def test_actual_edge_restrictions_are_preserved(self):
        expected = json.loads((RESULTS / 'edge-positive-controls.json').read_text())
        self.assertEqual(edge_module.positive_controls(), expected)
        self.assertEqual(expected['fixture_count'], 27)

    def test_complete_stated_ordinary_edge_frontier(self):
        expected = json.loads((RESULTS / 'edge-ordinary-frontier.json').read_text())
        self.assertEqual(edge_module.finite_ordinary_frontier(), expected)
        self.assertEqual(expected['source_count'], 2867)
        self.assertEqual(expected['improving_target_count'], 10418)
        self.assertEqual(expected['excluded_target_counts_by_witness'], {
            'Koszul upper bound': 9756, 'minimum slice': 386,
            'gcd factor dimensions': 171, 'factor product space': 105})
        self.assertEqual(expected['survivors'], [])
        self.assertEqual(expected['overall_exclusion_scope'],
                         'ordinary linear restriction only')
        self.assertFalse(expected['improves_omega'])


if __name__ == '__main__':
    unittest.main()

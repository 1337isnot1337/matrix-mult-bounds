"""Exact minimum-rank and crossed-jet coefficient certificates."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-paired-construction/narrow_rank_locus.py'
SPEC = importlib.util.spec_from_file_location('narrow_rank_locus', PATH)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class NarrowRankLocusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = module.run()

    def test_all_nonzero_binary_q3_parameters(self):
        self.assertEqual(self.report['binary_q3_a_parameters_checked'], 511)
        expected = {(1, 4): 49, (2, 6): 160, (2, 8): 128,
                    (3, 7): 66, (3, 8): 108}
        actual = {(r['a_rank'], r['slice_rank']): r['count']
                  for r in self.report['binary_q3_rank_histogram']}
        self.assertEqual(actual, expected)

    def test_each_preceding_b_row_block_adds_at_least_m(self):
        self.assertEqual(len(self.report['triangular_block_controls']), 42)
        for record in self.report['triangular_block_controls']:
            n, m, r = record['n'], record['m'], record['a_rank']
            ranks = record['successive_descending_b_block_ranks']
            self.assertGreaterEqual(ranks[0], r + m - 1)
            self.assertTrue(all(b - a >= m for a, b in zip(ranks, ranks[1:])))
            self.assertGreaterEqual(ranks[-1], r + m * m - 1)
            self.assertEqual(ranks[-1] == m * m, r == 1)

    def test_crossed_jets_lose_one_a_direction_but_have_an_odd_slice(self):
        for record in self.report['crossed_jet_controls']:
            n = record['n']
            self.assertEqual(record['a_flattening_rank'], n * n - 1)
            self.assertEqual(record['a_kernel_parameter'], [0, 0])
            self.assertEqual(record['offending_rank'], 5)
            self.assertEqual(record['nonzero_columns'], 5)
            self.assertEqual(record['minor_determinant'], 1)
        self.assertEqual(self.report['crossed_jet_controls'][0]['basis_slice_ranks'],
                         [0, 2, 2, 2, 4, 4, 2, 4, 4])
        self.assertFalse(self.report['improves_omega'])


if __name__ == '__main__':
    unittest.main()

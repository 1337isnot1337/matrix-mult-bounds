"""Check the complete coefficients of the wider regular-nilpotent quotient."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-paired-construction/wider_jet_obstruction.py'
SPEC = importlib.util.spec_from_file_location('wider_jet_obstruction', PATH)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class WiderJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = module.run()

    def test_complete_identities_at_inner_dimensions_two_three_four(self):
        self.assertEqual([(r['n'], r['m']) for r in self.report['records']],
                         [(3, 2), (4, 3), (5, 4), (13, 4)])
        for record in self.report['records']:
            n, m = record['n'], record['m']
            self.assertEqual(abs(record['c_coordinate_change_determinant']), 1)
            self.assertEqual(record['all_source_monomials_expanded'], n * n * m * m)
            self.assertEqual(record['fixed_q_zero_fibre_identities'], n)
            self.assertTrue(record['full_offending_identity_passes'])
            self.assertTrue(record['offending_has_no_free_c_coordinates'])
            self.assertEqual(record['first_paired_block_rank'], 1)
            self.assertEqual(record['first_paired_block_nonzeros'], [[0, m - 1, 1]])

    def test_small_m4_certificate_retains_all_twelve_free_c_coordinates(self):
        record = self.report['records'][2]
        self.assertEqual(record['source_dimensions'], [25, 32, 32])
        self.assertEqual(record['target_dimensions'], [25, 20, 20])
        self.assertEqual(record['b_kernel_dimension'], 12)
        matrix = record['offending_full_matrix']
        self.assertEqual(len(matrix), 20)
        self.assertTrue(all(len(row) == 32 and row[20:] == [0] * 12 for row in matrix))
        self.assertEqual(record['first_paired_block'], [[0, 0, 0, 1]] + [[0] * 4] * 19)
        self.assertFalse(self.report['improves_omega'])


if __name__ == '__main__':
    unittest.main()

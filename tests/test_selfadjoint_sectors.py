"""Exact replay and adversarial checks for the self-adjoint five-sector maps."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from fractions import Fraction


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'selfadjoint_sector_replay',
    ROOT/'research/ai/2026-10-21-selfadjoint-sectors/verify_witness.py')
REPLAY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPLAY)
RESULTS = ROOT/'results/selfadjoint-sectors-2026-10-21'


class SelfadjointSectorTests(unittest.TestCase):
    def setUp(self):
        self.witness = json.loads((RESULTS/'m5-witness.json').read_text())

    def test_all_source_coefficients_and_invertible_sector_maps(self):
        expected = json.loads((RESULTS/'m5-verification.json').read_text())
        expected.pop('witness_sha256')
        self.assertEqual(REPLAY.verify(self.witness), expected)

    def test_nonzero_negative_coefficient_is_rejected(self):
        corrupted = copy.deepcopy(self.witness)
        corrupted['z'][0][14] = '1'
        with self.assertRaises(AssertionError):
            REPLAY.verify(corrupted)

    def test_singular_shared_identification_is_rejected(self):
        corrupted = copy.deepcopy(self.witness)
        corrupted['shared_sector_maps'][2][0] = ['0']*5
        with self.assertRaises(AssertionError):
            REPLAY.verify(corrupted)

    def test_all_six_sector_coefficients_and_maps(self):
        witness = json.loads((RESULTS/'m6-witness.json').read_text())
        expected = json.loads((RESULTS/'m6-verification.json').read_text())
        expected.pop('witness_sha256')
        self.assertEqual(REPLAY.verify(witness), expected)

    def test_common_ideal_finite_bounds(self):
        controls = json.loads((RESULTS/'common-ideal-controls.json').read_text())
        self.assertEqual([row['m'] for row in controls['small_checks']], list(range(4, 13)))
        for row in controls['small_checks']:
            m = row['m']
            s, size = m//2, m*(m+1)//2
            required = sum(m-p for p in range(s))
            necessary = 2*required-m
            self.assertEqual(row['strictly_low_degree_count'], s)
            self.assertEqual(row['N'], size)
            self.assertEqual(row['shared_source_dimension'], m+1)
            self.assertEqual(row['required_opposite_flattening_rank'], required)
            self.assertEqual(row['necessary_B'], necessary)
            self.assertEqual(row['B_equals_N_plus_m'], size+m)
            self.assertEqual(row['N_plus_m_survives_this_necessary_test'], size+m >= necessary)
            self.assertEqual(Fraction(row['necessary_cost_ratio']), Fraction(necessary, size))


if __name__ == '__main__':
    unittest.main()

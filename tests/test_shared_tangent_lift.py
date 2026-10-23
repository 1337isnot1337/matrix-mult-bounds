"""Exact coefficient controls for the specified shared-map tangent obstruction."""

import importlib.util
from pathlib import Path
import unittest


PATH = (Path(__file__).resolve().parents[1]/'research/ai/'
        '2026-10-20-shared-tangent-lift/verify_tangent_obstruction.py')
SPEC = importlib.util.spec_from_file_location('shared_tangent_verifier', PATH)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class SharedTangentLiftTests(unittest.TestCase):
    def test_degree_three_normal_forcing(self):
        case = VERIFY.verify(2)
        self.assertEqual(case['total_target_rank'], 11)
        self.assertEqual(case['nonzero_normal_forcing'], 36)
        self.assertTrue(case['all_perturbation_coefficients_annihilated'])

    def test_two_dropped_nodes_and_scope(self):
        case = VERIFY.verify(3)
        self.assertEqual(case['total_target_rank'], 23)
        self.assertEqual(case['nonzero_normal_forcing'], 14976)
        report = VERIFY.report(3)
        self.assertFalse(report['higher_ramification_excluded'])
        self.assertFalse(report['new_exponent_established'])


if __name__ == '__main__':
    unittest.main()

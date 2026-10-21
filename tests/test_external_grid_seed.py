"""Exact controls for the fixed external grid-seed investigation."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

PACKAGE = Path(__file__).resolve().parents[1] / 'research/ai/2026-10-21-external-grid-seed'
SPEC = importlib.util.spec_from_file_location('external_grid_seed', PACKAGE / 'verify.py')
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class ExternalGridSeedTests(unittest.TestCase):
    def test_complete_integer_identity_and_mutation(self):
        factors = json.loads((PACKAGE / 'factors.json').read_text())
        actual, expected = V.integer_tensor(factors)
        self.assertEqual(actual, expected)
        self.assertEqual(sum(expected), 100)
        broken = copy.deepcopy(factors)
        first = next(i for i, x in enumerate(broken['u'][0]) if x)
        broken['u'][0][first] *= -1
        altered, _ = V.integer_tensor(broken)
        self.assertNotEqual(altered, expected)
        self.assertEqual(sum(V.term_traces(factors)), 100)
        self.assertGreater(min(V.term_traces(factors)), 0)

    def test_extremal_flat_and_stored_run_controls(self):
        result = V.verify()
        self.assertTrue(result['extremal_flat_verified_over_rationals'])
        self.assertEqual(result['nine_vector_negative_control_rank'], 5)
        self.assertFalse(result['exhaustive_enumeration_rerun_by_this_command'])
        self.assertFalse(result['general_Q64_maps_excluded'])
        self.assertFalse(result['improves_omega'])
        # A bad prime can only lower rank; the proof uses the safe direction.
        self.assertEqual(V.rank([[101, 0], [0, 1]]), 2)
        self.assertEqual(V.rank([[101, 0], [0, 1]], 101), 1)


if __name__ == '__main__':
    unittest.main()

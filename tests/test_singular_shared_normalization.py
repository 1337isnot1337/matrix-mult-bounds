"""Replay the explicit shared maps and every projected tensor coefficient."""

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'research/ai/2026-10-20-singular-shared-normalization'
RESULTS = ROOT / 'results/singular-shared-normalization-2026-10-20'


def load_module(name):
    spec = importlib.util.spec_from_file_location(name, SOURCE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SingularSharedNormalizationTests(unittest.TestCase):
    def test_shared_laurent_matrices_and_moving_ranks(self):
        expected = json.loads((RESULTS / 'family.json').read_text())
        actual = load_module('verify_family').verify(5)
        self.assertEqual(actual, expected)
        self.assertFalse(actual['constructs_tensor_degeneration'])
        self.assertFalse(actual['improves_omega'])

    def test_all_projected_coefficients_and_negative_powers(self):
        expected = json.loads((RESULTS / 'projection.json').read_text())
        verifier = load_module('verify_projection')
        actual = [verifier.verify_size(s) for s in range(2, 6)]
        self.assertEqual(actual, expected['records'])
        self.assertEqual(sum(row['coefficient_checks'] for row in actual), 26694)
        self.assertEqual(sum(row['negative_exponent_zero_checks'] for row in actual), 4345)
        self.assertFalse(expected['constructs_full_fatpoint_target'])
        self.assertFalse(expected['improves_omega'])

    def test_explicit_algebra_smoothing_and_window_diagnostics(self):
        expected = json.loads((RESULTS / 'smoothing.json').read_text())
        actual = load_module('verify_smoothing').verify(6)
        self.assertEqual(actual, expected)
        self.assertEqual(actual['coverage']['ordered_pair_products'], 811)
        self.assertEqual(actual['coverage']['transported_structure_coefficients'], 13879)
        self.assertTrue(actual['constructs_algebra_smoothing'])
        self.assertFalse(actual['constructs_required_tensor_degeneration'])
        self.assertFalse(actual['improves_omega'])


if __name__ == '__main__':
    unittest.main()

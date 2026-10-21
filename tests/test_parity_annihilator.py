"""Exact acceptance controls for the pairwise-annihilator obstruction."""

import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-anisotropic-constructions'
SPEC = importlib.util.spec_from_file_location('parity_annihilator', PACKAGE/'parity_annihilator.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ParityAnnihilatorTests(unittest.TestCase):
    def test_saved_source_and_target_certificate(self):
        actual = MODULE.verify()
        saved = json.loads((ROOT/'results/anisotropic-constructions-2026-10-20/parity-annihilator-controls.json').read_text())
        self.assertEqual(actual, saved)
        first = actual['target_controls'][0]
        self.assertEqual(first['required_annihilator_dimensions'], [99, 99, 100])
        self.assertEqual(first['matrix_space_upper_bound'], 212)
        self.assertTrue(first['excluded'])

    def test_strict_boundary_and_direct_sum_scope(self):
        boundary = MODULE.capacity_test([(13, 13, 13)], (113, 113, 112))
        self.assertEqual(boundary['sum_required'], 169)
        self.assertTrue(boundary['strict_single_square_exclusion'])
        separate = MODULE.capacity_test([(1, 1, 1)]*3, (2, 2, 2))
        self.assertEqual(separate['sum_required'], 3)
        self.assertFalse(separate['excluded'])
        self.assertFalse(separate['strict_single_square_exclusion'])

    def test_rectangular_constructed_controls_survive(self):
        for shapes in ([(5, 5, 9), (4, 4, 9)], [(5, 9, 4), (4, 9, 5)]):
            self.assertFalse(MODULE.capacity_test(shapes, (113, 113, 112))['excluded'])


if __name__ == '__main__':
    unittest.main()

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/torus_saturated_pencil.py'
SPEC = importlib.util.spec_from_file_location('torus_saturated_pencil', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SaturatedPencilTests(unittest.TestCase):
    def test_exact_saved_cube_and_target_slice_report(self):
        expected = json.loads((ROOT / 'results/anisotropic-constructions-2026-10-20/torus-saturated-pencil.json').read_text())
        self.assertEqual(MODULE.report(), expected)
        self.assertEqual(expected['source_test_slice_rank'], 3)
        self.assertEqual(expected['target_test_slice_rank'], 2)
        self.assertFalse(expected['extreme_scalars_normalized'])

    def test_cube_identity_changes_if_forced_corner_is_removed(self):
        v = MODULE.POLY.variable
        a, h, z, w = [v(name) for name in ('a', 'h', 'z', 'w')]
        matrix = [[z, h, a], [a, {}, {}], [w, a, {}]]
        self.assertEqual(MODULE.determinant(matrix), {('a', 'a', 'a'): 1})
        matrix[0][2] = {}
        self.assertEqual(MODULE.determinant(matrix), {})


if __name__ == '__main__':
    unittest.main()

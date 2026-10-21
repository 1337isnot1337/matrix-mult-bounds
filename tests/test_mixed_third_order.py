"""Replay the two universal rank covers and independently contract the source."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-21-mixed-first-jets'
RESULTS = ROOT / 'results/mixed-first-jets-2026-10-21'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


third = load('mixed_third_certificate', PACKAGE / 'third_order.py')
original = load('mixed_third_original_control', ROOT / 'tests/test_mixed_first_jets.py')


class MixedThirdOrderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / 'twojet-family.json').read_text())
        cls.maps = third.third_coefficients(cls.certificate)

    def test_complete_finite_normal_lemma(self):
        self.assertEqual(third.report(), json.loads((RESULTS / 'third-order-report.json').read_text()))

    def test_independent_projected_third_coefficient(self):
        parameters = (1, -1, 2, 1, 0, -2, 1, 1, -1, 2, 1, 0, 1, -1, 1, 2)
        ps, qs, y, z = original.evaluate(self.certificate, parameters)
        residue = original.corrected_coefficients(ps, qs, y, z)[3]
        for a, matrix in self.maps.items():
            expected = sp.Matrix([residue.get((a, b+4, c+4), 0)
                                  for b in range(14) for c in range(6)])
            self.assertEqual(matrix*sp.Matrix(parameters), expected)

    def test_all_boundary_second_row_freedoms_vanish(self):
        index = third.verify.index
        boundary_b = [{index(p, j, z): 1}
                      for p in (0, 3) for j in range(4) for z in range(7)]
        boundary_c = [{index(r, q, z): 1}
                      for r in range(4) for q in (0, 3) for z in range(7)]
        left = third.verify.rows(self.certificate['first_constant_B_new'])
        right = third.verify.rows(self.certificate['first_constant_C_new'])
        for tensor in (third.verify.contract(boundary_b, right),
                       third.verify.contract(left, boundary_c)):
            self.assertFalse(any(a in self.maps for a, b, c in tensor))

    def test_rank_cover_rejects_an_extra_output_row(self):
        maps = copy.deepcopy(self.maps)
        maps[36][0, 0] = 1
        with self.assertRaisesRegex(ArithmeticError, 'exceeds its universal row cover'):
            third.force_stage(maps, sp.SparseMatrix.eye(16), third.STAGES[0], 1)


if __name__ == '__main__':
    unittest.main()

"""Uniform polynomial normal lemma, source coordinates and certificate controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load('seven_frame_verifier', ROOT / 'research/ai/2026-10-21-rankone-seven-frames/verify.py')
original = load('seven_frame_original_source', ROOT / 'tests/test_mixed_first_jets.py')


class RankOneSevenFrameTests(unittest.TestCase):
    def test_complete_polynomial_certificate_and_endpoint(self):
        self.assertEqual(verify.report(), json.loads((ROOT / 'results/rankone-seven-frames-2026-10-21/report.json').read_text()))

    def test_polynomial_pair_in_original_cyclic_source_coordinates(self):
        data = verify.chart_data()
        tensor = original.original_contract(data['left_rows'], data['right_rows'])
        self.assertFalse(any(sp.expand(value) for (a, b, c), value in tensor.items()
                             if a in verify.extension.OUTSIDE))

    def test_reversed_triangular_order_is_rejected(self):
        data = verify.chart_data()
        with self.assertRaisesRegex(ArithmeticError, 'not above the diagonal'):
            verify.verify_triangular_order(data['normalized'], data['order'][::-1])

    def test_removing_the_mixed_rows_changes_the_normal_problem(self):
        left, right = verify.chart_frames()
        matrix = verify.constraints(left[:, :6], right[:, :6]).subs({verify.A: 0, verify.B: 0})
        self.assertLess(verify.third.matrix_rank(matrix), 224)


if __name__ == '__main__':
    unittest.main()

"""Polynomial certificates and their independently constructed point limit."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('uniform_mixed_five_verifier', ROOT / 'research/ai/2026-10-21-mixed-five-space-uniform/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class UniformMixedFiveTests(unittest.TestCase):
    def test_complete_polynomial_report(self):
        saved = ROOT / 'results/mixed-five-space-uniform-2026-10-21/report.json'
        self.assertEqual(verify.report(), json.loads(saved.read_text()))
        self.assertTrue(verify.data()['low'].todok())
        self.assertEqual({i % 7 for i, _ in verify.data()['low'].todok()}, {6})

    def test_uniform_virtual_tensor_specializes_to_point_construction(self):
        substitution = {verify.A: 0, verify.B: 0}
        uniform = verify.data()['virtual']
        point = verify.point.source_data()
        self.assertEqual(uniform['parameters'].subs(substitution), point['parameters'])
        self.assertEqual(uniform['third'].subs(substitution), point['third'])
        self.assertEqual(uniform['psi'].subs(substitution), point['psi'])

    def test_a_vanishing_minor_is_not_accepted_as_uniform(self):
        matrix = verify.sp.SparseMatrix([[1+verify.A, 0], [0, 1]])
        with self.assertRaisesRegex(ArithmeticError, 'not acyclic'):
            verify.polynomial_row_basis(matrix)


if __name__ == '__main__':
    unittest.main()

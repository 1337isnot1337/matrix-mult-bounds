"""Uniform Laurent reduction and rejection of hidden exceptional factors."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('mixed_axis_verifier', ROOT / 'research/ai/2026-10-21-mixed-axis-family/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class MixedAxisTests(unittest.TestCase):
    def test_complete_uniform_replay(self):
        saved = ROOT / 'results/mixed-axis-family-2026-10-21/report.json'
        self.assertEqual(verify.report(), json.loads(saved.read_text()))
        self.assertEqual(verify.report()['remaining_quotient_dimension'], 10)
        self.assertFalse(verify.report()['target_excluded_on_this_axis'])

    def test_hidden_parameter_division_is_rejected(self):
        matrix = verify.sp.SparseMatrix([[verify.A-1]])
        with self.assertRaisesRegex(ArithmeticError, 'not a Laurent unit'):
            verify.linear.replay(matrix, [[0, 0, 'a-1']], verify.A, verify.T)

    def test_column_operation_has_the_correct_orientation(self):
        matrix = verify.sp.SparseMatrix([[verify.A, verify.A+1]])
        steps = [['column', 1, 0, '1'], [0, 1, '1']]
        kernel = verify.linear.replay(matrix, steps, verify.A, verify.T)
        self.assertEqual(kernel, verify.sp.Matrix([verify.A+1, -verify.A]))
        basis, projection = verify.linear.replay(matrix, steps, verify.A, verify.T, row_basis=True)
        self.assertEqual(basis, matrix)
        self.assertEqual(basis*projection, verify.sp.eye(1))

    def test_changed_square_scale_is_rejected(self):
        matrix, rows, witness = verify.split_data()['square_checks'][0]
        changed = copy.deepcopy(witness)
        changed['scales'][0] = str(2*verify.sp.sympify(changed['scales'][0]))
        with self.assertRaisesRegex(ArithmeticError, 'Incorrect square minor diagonal'):
            verify.check_square(matrix, rows, changed)


if __name__ == '__main__':
    unittest.main()

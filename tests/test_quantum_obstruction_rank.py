"""Replay the all-parameter rank certificate without the minor search."""
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-21-moving-boundary-flags/minimum_rank.py'
SPEC = importlib.util.spec_from_file_location('quantum_obstruction_minimum_rank', PATH)
rank = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rank)
REPORT = ROOT / 'results/moving-boundary-flags-2026-10-21/minimum-rank-certificates.json'


def check_saved_minor(matrix, record):
    positions = record['positions']
    if len(positions) != 4 or len({i for i, _ in positions}) != 4 or len({j for _, j in positions}) != 4:
        raise ArithmeticError('Invalid minor coordinates')
    form = sp.Matrix(1, matrix.cols, lambda i, j: dict(record['form']).get(j, 0))
    pivot = next(j for j in range(matrix.cols) if form[j])
    for a, (i, j) in enumerate(positions):
        diagonal = matrix[200*j+i, :]
        if not diagonal[pivot] or diagonal*form[pivot] != form*diagonal[pivot]:
            raise ArithmeticError('Invalid diagonal polynomial identity')
        for _, other in positions[a+1:]:
            if matrix[200*other+i, :] != sp.zeros(1, matrix.cols):
                raise ArithmeticError('Invalid upper triangular zero')


class QuantumObstructionRankTests(unittest.TestCase):
    def test_regenerated_report_matches_saved_certificate(self):
        self.assertEqual(json.loads(json.dumps(rank.report())), json.loads(REPORT.read_text()))

    def test_saved_minors_and_full_kernels_without_search(self):
        saved = json.loads(REPORT.read_text())
        data = rank.normal.data()
        for side, key in (('B', 'left_obstruction'), ('C', 'right_obstruction')):
            matrix = data[key]
            for step in saved['chains'][side]['rounds']:
                self.assertEqual(matrix.cols, step['parameter_dimension'])
                for minor in step['minors']:
                    check_saved_minor(matrix, minor)
                equations = sp.Matrix(len(step['minors']), matrix.cols,
                                      lambda i, j: dict(step['minors'][i]['form']).get(j, 0))
                basis = sp.Matrix.hstack(*equations.nullspace())
                self.assertEqual(equations.cols-basis.cols, step['forced_linear_rank'])
                self.assertEqual(equations*basis, sp.zeros(equations.rows, basis.cols))
                matrix = matrix*sp.MutableSparseMatrix(basis)
            self.assertEqual(matrix, sp.zeros(3200, 88))

    def test_corrupted_triangular_zero_is_rejected(self):
        saved = json.loads(REPORT.read_text())
        matrix = sp.MutableSparseMatrix(rank.normal.data()['left_obstruction'])
        minor = saved['chains']['B']['rounds'][0]['minors'][0]
        i = minor['positions'][0][0]
        j = minor['positions'][1][1]
        self.assertEqual(matrix[200*j+i, :], sp.zeros(1, matrix.cols))
        matrix[200*j+i, 0] = 1
        with self.assertRaisesRegex(ArithmeticError, 'upper triangular zero'):
            check_saved_minor(matrix, minor)
        with self.assertRaisesRegex(ArithmeticError, 'triangular zero'):
            rank.verify_minor(matrix, minor['positions'], minor['form'])


if __name__ == '__main__':
    unittest.main()

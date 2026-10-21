"""Exact normal filtering and direct positive/negative lifting controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-21-invertible-line-lifts'
RESULTS = ROOT / 'results/invertible-line-lifts-2026-10-21'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


quadratic = load('invertible_quadratic_test', PACKAGE / 'quadratic.py')
normal = quadratic.normal_filter
extension = quadratic.extension


def control(first, second):
    data = quadratic.data()
    direction = data['directions'][:, first]+data['directions'][:, second]
    rows = [{j: direction[112*b+j] for j in range(112) if direction[112*b+j]}
            for b in range(8)]
    tensor = extension.contract(rows[:4], rows[4:], extension.OUTSIDE)
    return data, tensor, -data['forcing']*sp.Matrix(list(tensor))


class InvertibleLineLiftTests(unittest.TestCase):
    def test_complete_normal_filter(self):
        self.assertEqual(normal.report(), json.loads((RESULTS / 'normal-space.json').read_text()))

    def test_complete_quadratic_coefficient_report(self):
        self.assertEqual(quadratic.report(), json.loads((RESULTS / 'quadratic-compatibility.json').read_text()))

    def test_positive_control_replays_actual_source_corrections(self):
        data, residual, rhs = control(0, 22)
        reduced, pivots = data['system'].row_join(rhs).to_DM().rref()
        reduced = reduced.to_Matrix()
        self.assertTrue(all(j < 896 for j in pivots))
        solution = sp.zeros(896, 1)
        for i, j in enumerate(pivots):
            solution[j] = reduced[i, 896]
        self.assertEqual(data['system']*solution, rhs)
        rows = [{j: solution[112*b+j] for j in range(112) if solution[112*b+j]}
                for b in range(8)]
        first, cb, cc, _, _, annihilator = extension.matrices()
        core = first[extension.A0, :]
        second = (residual+extension.contract(rows[:4], extension.G, extension.OUTSIDE)
                  + extension.contract(extension.G, rows[4:], extension.OUTSIDE))
        self.assertFalse(any(second*annihilator.T))
        _, columns = core.to_DM().rref()
        y2 = second[:, list(columns)]*core[:, list(columns)].inv()
        self.assertEqual(second, y2*core)
        left, right = data['left'], data['right']
        for matrix, tensor in (
                (cb, extension.contract(left, rows[4:], extension.OUTSIDE)
                 - y2*extension.contract(left, extension.G, extension.A0)),
                (cc, extension.contract(rows[:4], right, extension.OUTSIDE)
                 - y2*extension.contract(extension.G, right, extension.A0))):
            answer = normal.constructor.solver(matrix)(-sp.Matrix(list(tensor)))
            self.assertEqual(matrix*answer, -sp.Matrix(list(tensor)))

    def test_incompatible_control_has_an_augmented_rank_obstruction(self):
        data, _, rhs = control(2, 30)
        self.assertEqual(quadratic.third.matrix_rank(data['system'].row_join(rhs)), 633)


if __name__ == '__main__':
    unittest.main()

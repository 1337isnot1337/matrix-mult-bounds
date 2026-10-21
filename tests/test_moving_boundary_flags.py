"""Independent coefficients and constructive controls for the normal lemma."""
import importlib.util
import json
from pathlib import Path
import random
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-21-moving-boundary-flags/normal_directions.py'
SPEC = importlib.util.spec_from_file_location('moving_boundary_normal_test', PATH)
normal = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(normal)
ext = normal.extension


def solve_columns(matrix, rhs):
    """Solve all right sides through one independently selected square minor."""
    _, columns = matrix.to_DM().rref()
    _, rows = matrix[:, list(columns)].T.to_DM().rref()
    coefficients = matrix[list(rows), list(columns)].inv()*rhs[list(rows), :]
    solution = sp.zeros(matrix.cols, rhs.cols)
    for i, col in enumerate(columns):
        solution[col, :] = coefficients[i, :]
    if matrix*solution != rhs:
        raise ArithmeticError('The direct coefficient equations have no solution')
    return solution


class MovingBoundaryTests(unittest.TestCase):
    def test_exact_normal_certificate_replay(self):
        saved = json.loads((ROOT / 'results/moving-boundary-flags-2026-10-21/normal-certificates.json').read_text())
        self.assertEqual(json.loads(json.dumps(normal.report())), saved)

    def test_first_operator_against_direct_source_contraction(self):
        rng = random.Random(202610771)
        rows = [{j: rng.choice((-2, -1, 1, 2)) for j in rng.sample(range(112), 16)}
                for _ in range(8)]
        vector = sp.Matrix([row.get(j, 0) for row in rows for j in range(112)])
        actual = (ext.contract(rows[:4], ext.G, normal.KERNEL)
                  + ext.contract(ext.G, rows[4:], normal.KERNEL))
        self.assertEqual(normal.data()['operator']*vector, sp.Matrix(list(actual)))

    def test_plane_directions_admit_direct_cross_lifts_and_detect_tamper(self):
        data = normal.data()
        directions = normal.plane_directions()
        coefficients = (1, -2, 3, -1)
        leading_rows = []
        for i in range(8):
            row = {}
            for direction, coefficient in zip(directions, coefficients):
                for j, value in direction[i].items():
                    row[j] = row.get(j, 0)+coefficient*value
            leading_rows.append({j: value for j, value in row.items() if value})
        p1 = leading_rows[:4]+data['E_B_complement']
        q1 = leading_rows[4:]+data['E_C_complement']
        leading = ext.G+[{} for _ in range(16)]
        first = (ext.contract(p1, leading, normal.KERNEL)
                 + ext.contract(leading, q1, normal.KERNEL))
        old = [20*b+c for b in range(4) for c in range(4)]
        y = first[:, old]*data['recover'].T
        first_a0 = ext.contract(p1, leading, ext.A0)+ext.contract(leading, q1, ext.A0)
        residual = ext.contract(p1, q1, normal.KERNEL)-y*first_a0
        rhs_b = sp.Matrix(256, 16, lambda r, j: -residual[r//4, 20*(j+4)+r % 4])
        rhs_c = sp.Matrix(256, 16, lambda r, j: -residual[r//4, 20*(r % 4)+j+4])
        b = solve_columns(data['left_constraints'], rhs_b)
        c = solve_columns(data['right_constraints'], rhs_c)
        p2 = [{} for _ in range(4)]+[{i: b[i, j] for i in range(112) if b[i, j]}
                                      for j in range(16)]
        q2 = [{} for _ in range(4)]+[{i: c[i, j] for i in range(112) if c[i, j]}
                                      for j in range(16)]
        cross = ([20*b+c for b in range(4, 20) for c in range(4)]
                 + [20*b+c for b in range(4) for c in range(4, 20)])
        lifted = (residual+ext.contract(p2, leading, normal.KERNEL)
                  + ext.contract(leading, q2, normal.KERNEL))
        self.assertEqual(lifted[:, cross], sp.zeros(64, 128))
        p2[4][ext.index(1, 0, 0)] = p2[4].get(ext.index(1, 0, 0), 0)+1
        corrupted = (residual+ext.contract(p2, leading, normal.KERNEL)
                     + ext.contract(leading, q2, normal.KERNEL))
        self.assertNotEqual(corrupted[:, cross], sp.zeros(64, 128))

    def test_moving_polynomial_boundary_identity(self):
        for t in (0, 1, 2):
            u = [(1, t, 2*t*t, 0), (0, t*t, -t, 1)]
            products = []
            for a, b in ((0, 0), (0, 1), (1, 1)):
                row = [0]*7
                for p in range(4):
                    for q in range(4):
                        row[6-p-q] += u[a][p]*u[b][q]
                products.append(row)
            kernel = sp.Matrix.hstack(*sp.Matrix(products).nullspace()).T
            self.assertEqual(kernel.rows, 4)
            first_rows = sp.zeros(64, 112)
            for i in range(4):
                for s in range(4):
                    for a in range(4):
                        for z in range(7):
                            first_rows[16*i+4*s+a, ext.index(i, s, z)] = kernel[a, z]
            b_rows = [{ext.index(p, j, z): row[p] for p in range(4) if row[p]}
                      for row in u for j in range(4) for z in range(7)]
            c_rows = [{ext.index(r, q, z): row[q] for q in range(4) if row[q]}
                      for row in u for r in range(4) for z in range(7)]
            self.assertEqual(first_rows*ext.contract(b_rows, c_rows, range(112)), sp.zeros(64, 56*56))


if __name__ == '__main__':
    unittest.main()

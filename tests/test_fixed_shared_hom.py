"""Coefficient-kernel checks for the fixed-shared-coordinate obstruction."""
import importlib.util
from pathlib import Path
import sympy as sp
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'fatpoint_hom', ROOT/'research/ai/2026-10-20-concavity-equivalence/fatpoint_route.py')
target = importlib.util.module_from_spec(spec)
spec.loader.exec_module(target)


def hom_dimension(a, matrices):
    z, y = matrices[0].shape
    equations = []
    for i, matrix in enumerate(matrices):
        u = sp.zeros(a+1, 2)
        u[i, 0] = 1
        u[i+1, 1] = 1
        equations.append((-sp.kronecker_product(sp.eye(2), matrix)).row_join(
            sp.kronecker_product(u.T, sp.eye(z))))
    eq = sp.Matrix.vstack(*equations)
    return 2*y+(a+1)*z-eq.rank()


class FixedSharedHomTests(unittest.TestCase):
    def test_source_formula(self):
        for a in range(2, 6):
            b = a*(a+1)//2+max(a-3, 0)
            matrices = [sp.zeros(b+a-1, b) for _ in range(a)]
            for i in range(a):
                for j in range(b):
                    matrices[i][i+j, j] = 1
            self.assertEqual(hom_dimension(a, matrices), b-1)

    def test_padded_target_and_cost_one_rejection(self):
        for a, extra in [(2, 0), (3, 0), (4, 0), (4, 1), (5, 2)]:
            n = a*(a+1)//2
            b = n+extra
            _, terms = target.tensor(a)
            matrices = [sp.zeros(b+a-1, b) for _ in range(a)]
            for i, y, z in terms:
                matrices[i][z, y] += 1
            actual = hom_dimension(a, matrices)
            self.assertEqual(actual, 2*b-(n+a-2))
            if (a, extra) == (4, 0):
                self.assertLess(actual, b-1)


if __name__ == '__main__':
    unittest.main()

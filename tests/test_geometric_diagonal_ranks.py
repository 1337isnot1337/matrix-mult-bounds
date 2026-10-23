"""Regression controls for geometric diagonal-polynomial source slices."""
from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest

MODULE = (Path(__file__).resolve().parents[1] / 'research' / 'ai' /
          '2026-10-23-geometric-diagonal-ranks' / 'verify.py')
spec = importlib.util.spec_from_file_location('geometric_diagonal_verify', MODULE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def rational_rank(A):
    """Independent Fraction elimination, with no finite-field backend."""
    A = [list(map(Fraction, row)) for row in A]
    row = 0
    for col in range(len(A[0])):
        k = next((k for k in range(row, len(A)) if A[k][col]), None)
        if k is None:
            continue
        A[row], A[k] = A[k], A[row]
        inv = 1 / A[row][col]
        for j in range(col, len(A[0])):
            A[row][j] *= inv
        for k in range(row + 1, len(A)):
            factor = A[k][col]
            if factor:
                for j in range(col, len(A[0])):
                    A[k][j] -= factor * A[row][j]
        row += 1
        if row == len(A):
            break
    return row


class GeometricDiagonalRankTests(unittest.TestCase):
    def test_finite_field_source_and_kernel_replay(self):
        report = module.verify()
        self.assertEqual(report['result'], 'PASS')
        self.assertEqual(report['counts']['toeplitz_ranks'], 3276)
        self.assertEqual(report['counts']['literal_full_matrices'], 75)

    def test_independent_characteristic_zero_toeplitz_ranks(self):
        ratio, scalar = Fraction(2, 3), Fraction(5, 7)
        for a, d in ((4,3), (5,3), (6,4), (7,3), (8,5), (10,6)):
            m, q = d+1, a % (d+1)
            e = (q-1)*(m-q) if q else 0
            ranks = []
            for ell in range(1,d+1):
                mat = [[scalar * ratio**(ell+v-u)
                        if 0 <= ell+v-u <= d else Fraction(0)
                        for v in range(a)] for u in range(a)]
                ranks.append(rational_rank(mat))
            self.assertEqual(sum(ranks), a*d-e, (a,d,ranks))

    def test_wrong_kernel_is_rejected(self):
        a,d,ell,p = 7,3,1,101
        basis = module.kernel_basis(a,d,ell,1,p)
        self.assertGreater(len(basis), 0)
        bad = basis[0].copy()
        bad[0] = (bad[0] + 1) % p
        T = module.toeplitz(a,d,ell,1,1,p)
        self.assertTrue(any(sum(x*y for x,y in zip(row,bad)) % p
                            for row in T))


if __name__ == '__main__':
    unittest.main()

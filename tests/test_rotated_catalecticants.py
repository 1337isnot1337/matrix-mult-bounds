"""Exact controls for the biform proof and its tensor identification."""
import json
from math import factorial
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-koszul"))
import rotated_catalecticants as rotated
import all_dimension_targets as family


class RotatedCatalecticantTests(unittest.TestCase):
    def test_replay_rank_report(self):
        saved = json.loads((ROOT / "results/koszul-2026-10-20" /
                            "rotated_catalecticants.json").read_text())
        self.assertEqual(rotated.report(), saved)
        self.assertEqual(saved["block_rank_cases"], 360)

    def test_identity_is_sharp_in_every_tested_degree(self):
        for m in range(2, 7):
            for q in range(m):
                ranks = [rotated.block_matrix(sp.eye(m), q, j).rank() for j in range(m)]
                self.assertEqual(ranks, [rotated.lower_bound(m - 1, q, j) for j in range(m)])
                self.assertEqual(sum(ranks), m * (m + 1) // 2 + q * (m - 1 - q))

    def test_derivative_convention(self):
        d, q, j = 3, 1, 2
        p = rotated.bases(d + 1)["vandermonde"]
        s, t, u, v = sp.symbols("s t u v")
        form = sum(p[i, l] * s**i * t**(d-i) * u**l * v**(d-l) /
                   (factorial(i)*factorial(d-i)*factorial(l)*factorial(d-l))
                   for i in range(d + 1) for l in range(d + 1))
        rows = []
        for r in range(q + 1):
            for a in range(j + 1):
                derivative = sp.Poly(sp.diff(form, s, r, t, q-r, u, a, v, j-a), s,t,u,v)
                rows.append([derivative.coeff_monomial(s**b*t**(d-q-b)*u**c*v**(d-j-c)) *
                             factorial(b)*factorial(d-q-b)*factorial(c)*factorial(d-j-c)
                             for b in range(d-q+1) for c in range(d-j+1)])
        self.assertEqual(sp.Matrix(rows), rotated.block_matrix(p, q, j))

    def test_independent_tensor_assembly(self):
        for m in range(2, 6):
            nodes, _, terms = family.target(m)
            n = len(nodes)
            p = rotated.bases(m)["swap_0_1"]
            for q in range(m):
                matrix = sp.zeros((q + 1) * n, (m - q) * n)
                for x, y, z in terms:
                    for r in range(q + 1):
                        for s in range(m - q):
                            matrix[r*n+y, s*n+z] += p[r+s, x]
                self.assertEqual(matrix.rank(), sum(rotated.block_matrix(p, q, j).rank()
                                                     for j in range(m)))

    def test_singular_basis_is_outside_the_lemma(self):
        for m in range(3, 8):
            p = sp.zeros(m)
            p[0, 0] = 1
            ranks = [rotated.block_matrix(p, 1, j).rank() for j in range(m)]
            self.assertEqual(ranks, [1] * m)
            self.assertLess(sum(ranks), m * (m + 1) // 2 + m - 2)

    def test_triangular_nonsingular_blocks(self):
        for m in range(2, 6):
            p = rotated.bases(m)["vandermonde"]
            for j in range(m):
                # Nonzero entries above the leading convolution degree.
                def coefficient(i, a, c):
                    if i < a + c:
                        return 0
                    if i == a + c:
                        return 1
                    return (17 * i + 5 * a - 3 * c) % 7 - 3

                for q in range(m):
                    matrix = sp.Matrix([
                        [sum(p[r+s, i] * coefficient(i, a, c) for i in range(m))
                         for s in range(m-q) for c in range(m-j)]
                        for r in range(q+1) for a in range(j+1)])
                    self.assertGreaterEqual(matrix.rank(), rotated.lower_bound(m-1, q, j))

    def test_small_slope_support_cover(self):
        for m in range(2, 16):
            d = m - 1
            t = d // 2
            nodes, _, _ = family.target(m)
            rows = {(a, b) for a, b in nodes if b > t or (a, b) == (0, t)}
            cols = {(c, e) for c, e in nodes if e > d - t}
            self.assertEqual(len(rows) + len(cols), m * m // 4 + 1)
            for a, b in nodes:
                for c, e in nodes:
                    if b + e > d or (a == c == 0 and b + e == d):
                        self.assertTrue((a, b) in rows or (c, e) in cols)


if __name__ == "__main__":
    unittest.main()

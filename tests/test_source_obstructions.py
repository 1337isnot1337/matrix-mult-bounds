"""Finite matrix checks of the source-construction obstructions."""
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/ai/2026-10-20-koszul"))
import all_dimension_targets as family


def catalecticant(m, ysize, zsize, terms, q):
    h = m - 1 - q
    matrix = sp.zeros((q + 1) * ysize, (h + 1) * zsize)
    for x, y, z in terms:
        for r in range(q + 1):
            s = x - r
            if 0 <= s <= h:
                matrix[r * ysize + y, s * zsize + z] += 1
    return matrix


def polynomial_matrix_flattening(coefficients, length):
    rows, cols = coefficients[0].shape
    result = sp.zeros(rows * (length + len(coefficients) - 1), cols * length)
    for i, matrix in enumerate(coefficients):
        for j in range(length):
            result[(i + j) * rows:(i + j + 1) * rows, j * cols:(j + 1) * cols] += matrix
    return result


def monomial_control(m, k, lengths, weights):
    """Build the source map explicitly and check every surviving coefficient."""
    nodes, _, target = family.target(m)
    lookup = {monomial: index for index, monomial in enumerate(nodes)}
    n = len(nodes)
    ymap, zmap, yw, zw = {}, {}, {}, {}
    ystart = 0
    multiplicities = {u: 0 for u in range(1, m + 1)}
    for u, weight in zip(lengths, weights):
        copy = multiplicities[u]
        multiplicities[u] += 1
        for a in range(u):
            j = ystart + u - 1 - a
            ymap[j] = copy * n + lookup[a, u - 1 - a]
            yw[j] = weight
        for c in range(m + 1 - u):
            j = ystart + u - 1 + c
            if j in zmap:
                raise AssertionError("overlapping output sectors")
            zmap[j] = copy * n + lookup[c, m - u - c]
            zw[j] = -weight
        ystart += u
    assert ystart == k * n
    assert all(count == k for count in multiplicities.values())
    actual = set()
    for x in range(m):
        for y in range(k * n):
            z = x + y
            if z not in zmap:
                continue  # Explicitly project unused output coordinates to zero.
            exponent = yw[y] + zw[z]
            assert exponent >= 0
            if exponent == 0:
                actual.add((x, ymap[y], zmap[z]))
    expected = {(x, copy * n + y, copy * n + z)
                for copy in range(k) for x, y, z in target}
    assert actual == expected
    return len(actual)


class SourceObstructionTests(unittest.TestCase):
    def test_source_catalecticants(self):
        for m in range(2, 6):
            size = m * (m + 1) // 2
            terms = [(x, y, x + y) for x in range(m) for y in range(size)]
            for q in range(m):
                matrix = catalecticant(m, size, size + m - 1, terms, q)
                self.assertEqual(matrix.rank(), size + q)

    def test_target_catalecticants(self):
        for m in range(2, 6):
            nodes, _, terms = family.target(m)
            for q in range(m):
                matrix = catalecticant(m, len(nodes), len(nodes), terms, q)
                self.assertEqual(matrix.rank(), len(nodes) + q * (m - 1 - q))

    def test_maximum_target_slice_rank(self):
        for m in range(2, 9):
            nodes, _, terms = family.target(m)
            matrix = sp.zeros(len(nodes), len(nodes))
            for x, y, z in terms:
                matrix[y, z] = sp.Rational(1, x + 1)
            self.assertEqual(matrix.rank(), (m + 1) ** 2 // 4)

    def test_minimum_target_slice_rank(self):
        for m in range(2, 9):
            nodes, _, terms = family.target(m)
            matrix = sp.zeros(len(nodes), len(nodes))
            for x, y, z in terms:
                if x == 0:
                    matrix[y, z] = 1
            self.assertEqual(matrix.rank(), m)

    def test_optimized_catalecticant_bound(self):
        for m in range(2, 101):
            for k in (1, 2, 7, 53):
                lower_gap = max(k * q * (m - 1 - q) - q for q in range(m))
                self.assertEqual(lower_gap, family.coordinate_gap(m, k))

    def test_known_small_degeneration_controls(self):
        for k in range(1, 5):
            self.assertEqual(monomial_control(2, k, [1, 2] * k, [0, 1] * k), 4 * k)
        self.assertEqual(monomial_control(3, 1, [2, 3, 1], [0, 1, 0]), 10)

    def test_projected_shared_koszul_barrier(self):
        projection = sp.Matrix([[1, 0, 1, 2], [0, 1, 1, -1], [1, 1, 0, 1]])
        coefficients = []
        for i in range(4):
            a, b, c = projection[:, i]
            coefficients.append(sp.Matrix([[0, -c, b], [c, 0, -a], [-b, a, 0]]))
        matrix = polynomial_matrix_flattening(coefficients, 10)
        self.assertGreaterEqual(matrix.rank(), 20)

    def test_polynomial_curve_rank_hypothesis_is_essential(self):
        length = 10
        generic = [sp.eye(2), sp.Matrix([[0, 1], [0, 0]]),
                   sp.Matrix([[0, 0], [1, 0]]), sp.zeros(2)]
        self.assertEqual(polynomial_matrix_flattening(generic, length).rank(), 2 * length)
        # M(z)=[[1,z],[z^2,z^3]] has rank one, although L(x) generically has rank two.
        exceptional = [sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 1], [0, 0]]),
                       sp.Matrix([[0, 0], [1, 0]]), sp.Matrix([[0, 0], [0, 1]])]
        self.assertEqual(polynomial_matrix_flattening(exceptional, length).rank(), length + 1)


if __name__ == "__main__":
    unittest.main()

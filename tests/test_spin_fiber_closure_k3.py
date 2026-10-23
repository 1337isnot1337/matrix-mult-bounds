"""Independent six-index replay of the separate three-bit induction base."""

from collections import Counter
import importlib.util
from itertools import product
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/spin_fiber_closure.py'
SPEC = importlib.util.spec_from_file_location('spin_fiber_closure_three_bit_audit', SCRIPT)
CORE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)


def independent_three_bit_replay():
    power, side, matrix_side = 3, 8, 27
    polynomials, counts = [], []
    for point in CORE.POINTS3:
        images = []
        for leg, row in enumerate(point):
            first_vertex, second_vertex = divmod(row, matrix_side)
            image = {}
            for first, last in product(range(side), repeat=2):
                for middles in product(range(3), repeat=power):
                    value = 1
                    for bit in range(power):
                        local_row = (3 * (first_vertex // 3 ** bit % 3)
                                     + second_vertex // 3 ** bit % 3)
                        column = ((first // 2 ** bit % 2) * 3 + middles[bit]) * 2
                        column += last // 2 ** bit % 2
                        value *= CORE.v.LOCAL[local_row][column]
                    if not value:
                        continue
                    trits = sum(middles[bit] * 3 ** (power - 1 - bit) for bit in range(power))
                    variable = leg * 12 ** power + (first * 3 ** power + trits) * side + last + 1
                    middle = sum(middles[bit] * 2 ** bit for bit in range(power))
                    image.setdefault((first, middle, last), []).append((variable, value))
            images.append(image)
        polynomial, source_terms = Counter(), 0
        # Enumerate all six original indices.  Do not solve for either hidden
        # index, and do not call row_image or selected_equation from acceptance.
        for i, p, r, j, q, s in product(range(side), repeat=6):
            source_terms += 1
            for (vx, x), (vy, y), (vz, z) in product(
                    images[0].get((i, p + q, s), ()),
                    images[1].get((p, r + s, j), ()),
                    images[2].get((r, i + j, q), ())):
                polynomial[vx, vy, vz] += x * y * z
        polynomials.append({monomial: value for monomial, value in polynomial.items() if value})
        counts.append(source_terms)
    return polynomials, counts


class SpinFiberClosureThreeBitTests(unittest.TestCase):
    def test_full_three_bit_source_and_shared_polynomials(self):
        polynomials, counts = independent_three_bit_replay()
        self.assertEqual(counts, [262144, 262144, 262144])
        self.assertEqual(tuple(polynomials), CORE.POLYS3)
        combined = Counter()
        for sign, polynomial in zip((1, -1, 1), polynomials):
            for monomial, coefficient in polynomial.items():
                combined[monomial] += sign * coefficient
        self.assertFalse(any(combined.values()))
        self.assertEqual(sum(sign * CORE.v.matrix_coefficient(3, point)
                             for sign, point in zip((1, -1, 1), CORE.POINTS3)), -1)


if __name__ == '__main__':
    unittest.main()

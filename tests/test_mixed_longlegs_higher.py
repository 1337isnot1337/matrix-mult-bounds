"""Exact replay and independent coefficient controls for higher Koszul degrees."""
from collections import Counter
from fractions import Fraction
import importlib.util
from itertools import combinations
import json
from math import comb, prod
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-mixed-longlegs-candidate/verify_higher.py"
SPEC = importlib.util.spec_from_file_location("mixed_longlegs_higher", PATH)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def literal_unsplit_matrix(names, degree):
    blocks = [VERIFY.oriented(name, "B") for name in names]
    xdim = sum(block[0] for block in blocks)
    ydim = sum(block[1] for block in blocks)
    wedges = list(combinations(range(xdim), degree))
    rows = {(a, wedge): i for i, (a, wedge) in enumerate(
        (a, wedge) for a in range(5) for wedge in combinations(range(xdim), degree + 1))}
    columns = {(y, wedge): i for i, (y, wedge) in enumerate(
        (y, wedge) for y in range(ydim) for wedge in wedges)}
    matrix = [[0] * len(columns) for _ in rows]
    xoffset = yoffset = 0
    for x, y, entries, _, _ in blocks:
        for a, j, k in entries:
            j += xoffset
            k += yoffset
            for wedge in wedges:
                if j not in wedge:
                    output = tuple(sorted(wedge + (j,)))
                    matrix[rows[a, output]][columns[k, wedge]] += (-1) ** sum(i < j for i in wedge)
        xoffset += x
        yoffset += y
    return matrix


def fraction_rank(matrix):
    """Independent rational algorithm, without primitive-integer normalization."""
    a = [[Fraction(value) for value in row] for row in matrix]
    rank = 0
    for column in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for row in range(rank + 1, len(a)):
            if a[row][column]:
                scale = a[row][column] / a[rank][column]
                for col in range(column, len(a[0])):
                    a[row][col] -= scale * a[rank][col]
        rank += 1
        if rank == len(a):
            break
    return rank


class MixedLonglegsHigherTests(unittest.TestCase):
    def test_saved_exact_report(self):
        saved = json.loads((ROOT / "results/mixed-longlegs-candidate-2026-10-23/higher_verification.json").read_text())
        self.assertEqual(VERIFY.report(), saved)
        self.assertEqual([saved["degrees"][str(p)]["slack"] for p in (1, 2, 3)], [148, 14302, 734943])

    def test_occupancy_domain_and_codomain_coverage(self):
        for profile in (VERIFY.SOURCE, VERIFY.TARGET):
            xdim = sum(VERIFY.tensor(name)[0] * count for name, count in profile.items())
            ydim = sum(VERIFY.tensor(name)[1] * count for name, count in profile.items())
            for degree in (1, 2, 3):
                rows = columns = 0
                for names, occupancy, count in VERIFY.components(profile, degree):
                    dims = [VERIFY.tensor(name)[:2] for name in names]
                    rows += count * 5 * prod(choose(x, q) for (x, _), q in zip(dims, occupancy))
                    for selected, (_, y) in enumerate(dims):
                        columns += count * y * prod(
                            choose(x, q - int(j == selected))
                            for j, ((x, _), q) in enumerate(zip(dims, occupancy)))
                with self.subTest(profile=profile, degree=degree):
                    self.assertEqual(rows, 5 * comb(xdim, degree + 1))
                    self.assertEqual(columns, ydim * comb(xdim, degree))

    def test_unsplit_literal_coefficients_and_independent_rank(self):
        cases = [(["F2", "F3"], 2), (["F2", "O33"], 2),
                 (["O33", "M2"], 2), (["F2", "F2", "O33"], 2),
                 (["F2", "F3"], 3), (["F2", "O33"], 3),
                 (["F2", "F2", "O33"], 3)]
        for names, degree in cases:
            with self.subTest(names=names, degree=degree):
                direct = fraction_rank(literal_unsplit_matrix(names, degree))
                split = VERIFY.calculate(dict(Counter(names)), degree)["rank"]
                self.assertEqual(direct, split)


if __name__ == "__main__":
    unittest.main()

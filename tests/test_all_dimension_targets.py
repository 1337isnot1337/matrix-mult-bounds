"""Independent finite checks of the general mixed-target argument."""
from fractions import Fraction
import importlib.util
import itertools
import json
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "research/ai/2026-10-20-koszul"
sys.path.insert(0, str(CODE))
import all_dimension_targets as family


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


tensor = load("tensor_all_dimension", ROOT / "research/ai/2026-10-20-session2/tensor_checks.py")


class AllDimensionTests(unittest.TestCase):
    def test_report_replay(self):
        saved = ROOT / "results/koszul-2026-10-20/all_dimension_targets.json"
        self.assertEqual(family.run(), json.loads(saved.read_text()))

    def test_weights_against_evaluation_inverse(self):
        for m in range(2, 7):
            nodes, weights, _ = family.target(m)
            matrix = sp.Matrix([[s ** i * t ** j for i, j in nodes] for s, t in nodes])
            inverse_rows = matrix.inv()[-m:, :].tolist()
            self.assertEqual(weights, [[Fraction(value) for value in row] for row in inverse_rows])

    def test_shared_koszul_matrices(self):
        for m in (2, 3, 5):
            nodes, _, terms = family.target(m)
            for p in range(m):
                matrix = tensor.koszul_matrix([m, len(nodes), len(nodes)], terms, p)
                self.assertEqual(matrix.rank(), len(nodes) * sp.binomial(m - 1, p))

    def test_minimum_interval_gap_by_all_orderings(self):
        # This checks the combinatorial minimum, not sufficiency for degeneration.
        for m, k in ((2, 3), (3, 2), (4, 1), (5, 1), (6, 1)):
            labels = tuple(u for u in range(1, m + 1) for _ in range(k))
            minimum = min(sum(m - max(a, b) for a, b in zip(order, order[1:]))
                          for order in set(itertools.permutations(labels)))
            self.assertEqual(minimum, family.coordinate_gap(m, k))

    def test_integral_and_threshold(self):
        x, d = sp.symbols("x d", positive=True)
        integral = 2 * sp.integrate(x ** (d - 1) * (1 - x / 2), (x, 0, sp.Rational(1, 2)))
        expected = 2 ** (-d - 1) * (3 * d + 4) / (d * (d + 1))
        self.assertEqual(sp.simplify(integral - expected), 0)
        q = 8 * expected / (3 * d)
        self.assertEqual(sp.simplify(q.subs(d, sp.Rational(4, 3)) ** 3), sp.Rational(729, 686))
        self.assertGreater(Fraction(3, 1) / Fraction(13423, 10000), Fraction(2))
        self.assertLess(Fraction(3, 1) / Fraction(13423, 10000), Fraction(9, 4))


if __name__ == "__main__":
    unittest.main()

"""Finite controls, not a replacement for the invariant-theory proof."""
from collections import defaultdict
import importlib.util
from itertools import product
import json
from pathlib import Path
import random
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-20-cyclic-mixed-map"
spec = importlib.util.spec_from_file_location("cyclic_full_capacity", PACKAGE / "full_capacity.py")
capacity = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capacity)


class CyclicFullCapacityTests(unittest.TestCase):
    def test_seeded_minors_corners_and_marginals(self):
        actual = capacity.report()
        path = ROOT / "results/cyclic-mixed-map-2026-10-20/full-capacity.json"
        self.assertEqual(actual, json.loads(path.read_text()))
        self.assertEqual(actual["integer_slices_checked"], 112)

    def test_minor_against_independent_tensor_product_expansion(self):
        rng = random.Random(202610361)
        grid = list(product(range(2), repeat=2))
        longs = list(product(range(3), repeat=2))
        f = {(i, k, s): rng.choice((-1, 0, 1)) for i, k, s in product(grid, longs, grid)}
        terms = []
        for i, j, p, q, t, s in product(range(2), repeat=6):
            terms.append(((i, p+q, s), (j, p, t+s), (i+j, q, t)))
        matrix = defaultdict(int)
        for left, right in product(terms, repeat=2):
            x, y, z = [tuple(zip(left[axis], right[axis])) for axis in range(3)]
            matrix[y, z] += f[x]
        minor = capacity.triangular_minor(2, 2, f)
        actual = [[matrix[row, col] for col in minor["columns"]] for row in minor["rows"]]
        self.assertEqual(actual, minor["matrix"])


if __name__ == "__main__":
    unittest.main()

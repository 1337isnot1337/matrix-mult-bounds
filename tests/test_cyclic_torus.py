import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "cyclic_torus", ROOT / "research/ai/2026-10-20-cyclic-equivariant/torus.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class CyclicTorusTests(unittest.TestCase):
    def test_complete_character_frontier(self):
        path = ROOT / "results/cyclic-equivariant-2026-10-20/torus-character-frontier.json"
        self.assertEqual(v.report(), json.loads(path.read_text()))

    def test_positive_factor_search_against_independent_small_enumeration(self):
        vectors = [tuple(c) for length in range(1, 4) for c in product(range(5), repeat=length)
                   if c[0] and c[-1] and sum(c) <= 4]
        cases = {}
        for f, g in product(vectors, repeat=2):
            if len(f)+len(g) > 5:
                continue
            key = (tuple(v.multiply(f, g)), sum(f), sum(g))
            cases.setdefault(key, set()).add((f, g))
        # A product of degree at most two cannot have a factor of larger degree.
        checked = 0
        for (q, fs, gs), expected in cases.items():
            if len(q) > 3:
                continue
            actual, _ = v.positive_factors(list(q), fs, gs)
            self.assertEqual({(tuple(f), tuple(g)) for f, g in actual}, expected)
            checked += 1
        self.assertGreater(checked, 100)


if __name__ == "__main__":
    unittest.main()

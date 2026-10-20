"""Independent checks of the target certificate and its tensor interpretation."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "results/koszul-2026-10-20/fatpoint.json"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


fatpoint = load("fatpoint", ROOT / "research/ai/2026-10-20-koszul/fatpoint.py")
tensor = load("tensor_for_fatpoint", ROOT / "research/ai/2026-10-20-session2/tensor_checks.py")


class FatpointTests(unittest.TestCase):
    def test_coefficient_replay(self):
        self.assertEqual(json.loads(json.dumps(fatpoint.run())), json.loads(REPORT.read_text()))

    def test_exported_weights_without_matrix_inversion(self):
        data = json.loads(REPORT.read_text())
        weights = [[Fraction(x) for x in row] for row in data["output_weights_rows"]]
        for a, b in data["monomials_st_exponents"]:
            for x in range(4):
                value = sum(weights[x][h] * s ** a * t ** b
                            for h, (s, t) in enumerate(data["evaluation_nodes"]))
                self.assertEqual(value, int(a + b == 3 and a == x))

    def test_explicit_target_koszul_matrices(self):
        data = json.loads(REPORT.read_text())
        ranks = [int(tensor.koszul_matrix([4, 10, 10], data["constant_support"], p).rank())
                 for p in range(4)]
        self.assertEqual(ranks, [10, 30, 30, 10])
        self.assertEqual(len(data["constant_support"]), 20)


if __name__ == "__main__":
    unittest.main()

"""Replay exact cyclic recoupling and finite-search witnesses."""
from collections import defaultdict
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-20-cyclic-recoupling"
sys.path.insert(0, str(PACKAGE))
import coefficients as cyclic_coefficients
spec = importlib.util.spec_from_file_location("cyclic_recoupling_search", PACKAGE / "search.py")
cyclic_search = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cyclic_search)
RESULTS = ROOT / "results/cyclic-recoupling-2026-10-20"


class CyclicRecouplingTests(unittest.TestCase):
    def test_exact_full_coefficient_replay(self):
        for a, blocks, terms in ((2, 36, 239), (3, 429, 7897), (4, 2539, 91620)):
            actual = cyclic_coefficients.recouple(a)
            self.assertEqual(actual, cyclic_coefficients.read_json(RESULTS/f"coefficients-a{a}.json.gz"))
            self.assertEqual(len(actual["blocks"]), blocks)
            self.assertEqual(sum(len(b["terms"]) for b in actual["blocks"]), terms)

    def test_equivariant_raising_operator(self):
        for degree in range(1, 4):
            basis = cyclic_coefficients.triple_basis(degree)
            lookup = {(i, j, e): p for i, j, e, _, p in basis}
            for i, j, e, _, poly in basis:
                raised = defaultdict(Fraction)
                for point, coefficient in poly.items():
                    for axis in range(3):
                        if point[axis]:
                            target = point[:axis]+(point[axis]-1,)+point[axis+1:]
                            raised[target] += coefficient*point[axis]
                actual = {k: v for k, v in raised.items() if v}
                expected = {k: e*v for k, v in lookup[i, j, e-1].items() if v} if e else {}
                self.assertEqual(actual, expected)

    def test_uniform_marginals_and_multiplicity_factorizations(self):
        for a, blocks in ((2, 15), (3, 65), (4, 175)):
            data = cyclic_coefficients.read_json(RESULTS/f"coefficients-a{a}.json.gz")
            actual = cyclic_coefficients.group_multiplicities(data)
            self.assertEqual(actual, cyclic_coefficients.read_json(RESULTS/f"grouped-a{a}.json.gz"))
            self.assertEqual(len(actual["blocks"]), blocks)

    def test_saved_best_supports_and_exact_scores(self):
        for path in sorted(RESULTS.glob("*-a*.json")):
            result = json.loads(path.read_text())
            mode, a = result["mode"], result["a"]
            stem = "coefficients" if mode == "scalar-sampled" else "grouped"
            data = cyclic_coefficients.read_json(RESULTS/f"{stem}-a{a}.json.gz")
            labels, blocks, leaves = cyclic_search.prepare(data, stem == "grouped")
            weights = result["best"]["weights"]
            actual = []
            for i, block in enumerate(blocks):
                x, y, z = block["labels"]
                degree = weights["x"][x]+weights["y"][y]+weights["z"][z]
                self.assertGreaterEqual(degree, 0)
                if degree == 0 and weights["output_mask"] & (1 << z):
                    actual.append(i)
            self.assertEqual(actual, result["best"]["retained_blocks"])
            score, expression = cyclic_search.score_functions(blocks, leaves)
            mask = sum(1 << i for i in actual)
            interval = [str(Fraction(v, cyclic_search.SCALE)) for v in score(mask)]
            self.assertEqual(interval, result["best"]["score_interval"])
            # JSON normalizes tuple-valued axis labels into lists.
            self.assertEqual(json.loads(json.dumps(expression(mask))), result["best"]["expression"])
            self.assertEqual(result["violations"], [])
            self.assertEqual(result["unresolved_interval_comparisons"], [])
            self.assertLess(Fraction(result["global_ratio_upper"]), 1)
            self.assertFalse(result["new_exponent_established"])

    def test_central_multiplicity_determinant_certificate(self):
        import central_screen
        data = cyclic_coefficients.read_json(RESULTS/"grouped-a4.json.gz")
        saved = json.loads((RESULTS/"central-multiplicity-screen.json").read_text())
        self.assertEqual(central_screen.report(data), saved)
        x = sp.Symbol("x")
        f = sp.Poly.from_list(saved["primitive_quartic_coefficients_high_to_low"], x)
        u = sp.Poly.from_list(list(map(sp.Rational, saved["bezout_u_high_to_low"])), x)
        v = sp.Poly.from_list(list(map(sp.Rational, saved["bezout_v_high_to_low"])), x)
        self.assertEqual(sp.expand((u*f+v*f.diff()).as_expr()), 1)
        self.assertEqual(f.as_expr(), 192*x**4+352*x**2-765)
        self.assertFalse(saved["arbitrary_degeneration_to_M2_excluded"])

    def test_complete_small_binary_search(self):
        data = cyclic_coefficients.read_json(RESULTS/"grouped-a2.json.gz")
        actual = cyclic_search.search(data, "grouped-binary")
        saved = json.loads((RESULTS/"grouped-binary-a2.json").read_text())
        self.assertEqual(json.loads(json.dumps(actual)), saved)


if __name__ == "__main__":
    unittest.main()

"""Finite controls and independent historical-score comparisons."""
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import random
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-width-two-support"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load("width_two_support", PACKAGE / "verify.py")
historical = load("archived_monomial_score", ROOT / "research/ai/2026-10-20/search_degenerations.py")


class WidthTwoSupportTests(unittest.TestCase):
    def test_every_small_support_matches_the_historical_recognizer(self):
        h = historical.slopes(7)
        for b in range(2, 6):
            for reverse in (False, True):
                for terms in verify.all_supports(b, reverse):
                    groups = verify.components(terms)
                    expected = sum((historical.profile(q["a"], q["b"], h)
                                    for q in map(historical.recognize, groups)), Fraction(0))
                    actual = verify.score(terms)
                    self.assertEqual(actual, expected, (b, reverse, terms))
                    self.assertLessEqual(actual, verify.profile(2, b))
                    if reverse:
                        self.assertEqual(actual == verify.profile(2, b), len(terms) == 2 * b)
                    else:
                        self.assertEqual(verify.profile(2, b) - actual,
                                         verify.path_gap(b, terms))

    def test_asymmetric_equality_example_is_an_actual_weight_support(self):
        wx, wy = (0, 0), (0, 1, 1, 0)
        groups, _ = historical.components(wx, wy)
        terms = tuple(sorted(t for group in groups for t in group))
        self.assertEqual(len(terms), 6)
        self.assertEqual(verify.score(terms), 6)
        self.assertEqual(verify.path_gap(4, terms), 0)
        self.assertEqual(verify.score(tuple((j, i, k) for i, j, k in terms)), 3)

    def test_long_sparse_and_dense_supports_obey_the_deficit_identity(self):
        rng = random.Random(20261023)
        for b in (9, 17, 40, 101):
            for denominator in (1, 2, 5):
                for _ in range(8):
                    terms = tuple((i, j, i + j) for i in range(2) for j in range(b)
                                  if rng.randrange(denominator) == 0)
                    self.assertEqual(verify.profile(2, b) - verify.score(terms),
                                     verify.path_gap(b, terms))
                    swapped = tuple((j, i, k) for i, j, k in terms)
                    self.assertLessEqual(verify.score(swapped), verify.profile(2, b))
                    self.assertEqual(verify.score(swapped) == verify.profile(2, b),
                                     len(terms) == 2 * b)

    def test_source_pins_and_report_scope(self):
        sources = json.loads((PACKAGE / "sources.json").read_text())
        for source in sources["local_sources"]:
            self.assertEqual(hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest(),
                             source["sha256"])
        report = json.loads((ROOT / "results/width-two-support-2026-10-23/exhaustive.json").read_text())
        self.assertEqual(report["supports_checked"],
                         2 * sum(4 ** b for b in range(2, report["max_b"] + 1)))
        self.assertEqual(len(report["rows"]), 2 * (report["max_b"] - 1))
        for row in report["rows"]:
            self.assertEqual(row["supports"], 4 ** row["b"])
            self.assertEqual(Fraction(row["maximum_exact"]), verify.profile(2, row["b"]))
            if row["shared_axis"] == "large":
                self.assertEqual(row["equality_supports"], 1)
        self.assertFalse(report["improves_omega"])


if __name__ == "__main__":
    unittest.main()

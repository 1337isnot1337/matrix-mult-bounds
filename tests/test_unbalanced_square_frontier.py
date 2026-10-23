"""Independent gates and item-first integer knapsack for every saved dimension."""
import hashlib
import importlib.util
import json
from math import isqrt
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-unbalanced-square-frontier"
RESULT = ROOT / "results/unbalanced-square-frontier-2026-10-23/frontier.json"
SPEC = importlib.util.spec_from_file_location("test_unbalanced_frontier", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


def independent_sizes(a, b, dimension):
    loss = a*b*(a+b-1)-dimension
    allowed = []
    for n in range(2, isqrt(dimension)+1):
        lift = n+2*loss
        if lift < 2*a*b:
            continue
        if a >= 3 and a+b-1 >= 6 and n >= 3 and lift == 2*a*b:
            continue
        excluded = False
        for r in range(1, a):
            caps = []
            if 3*r <= a+b-1:
                caps.append(r)
            if r >= 2 and 3*r == a+b:
                caps.append(max(r, 4))
            if 5*r < 2*(a+b):
                caps.append(max(r, max(1, (3*r-a-b+4)//2)**2))
            if any(n*n > cap*a*b and lift < (r+1)*a*b for cap in caps):
                excluded = True
                break
        if not excluded:
            allowed.append(n)
    scalar = 1+2*loss >= a*b
    repeated = 2+2*loss >= 2*a*b
    if scalar and repeated:
        allowed.append(1)
    return tuple(allowed), scalar and not repeated


def item_first_scores(sizes, dimension, values):
    scores = [-1]*(dimension+1)
    scores[0] = 0
    for n in sizes:
        for used in range(n*n, dimension+1):
            if scores[used-n*n] >= 0:
                scores[used] = max(scores[used], scores[used-n*n]+values[n])
    return scores


class UnbalancedSquareFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads(RESULT.read_text())

    def test_complete_source_rectangle_and_scope(self):
        expected = {(a, b) for a in range(2, 40) for b in range(a, 40)
                    if a*b*(a+b-1) <= 1377}
        # a>=10 has minimal size1900, b>=26 has minimal size1404.
        self.assertGreater(10*10*19, 1377)
        self.assertGreater(2*26*27, 1377)
        actual = [(r["a"], r["b"]) for r in self.saved["source_frontiers"]]
        self.assertEqual(set(actual), expected)
        self.assertEqual(set(v.source_formats(1377)), expected)
        self.assertEqual(len(actual), 82)
        self.assertEqual(self.saved["dimensions_screened"], 52310)
        self.assertEqual(self.saved["first_surviving_source"], [8, 9])
        self.assertEqual(self.saved["surviving_source_formats"], [[8, 9], [9, 9]])
        self.assertEqual(sum(r["source_leg_dimension"] < 1152
                             for r in self.saved["source_frontiers"]), 70)
        self.assertFalse(self.saved["singular_degenerations_excluded"])
        self.assertFalse(self.saved["independent_review"])
        self.assertFalse(self.saved["improves_omega"])

    def test_every_dimension_by_independent_gates_and_item_first_recurrence(self):
        for source in self.saved["source_frontiers"]:
            a, b = source["a"], source["b"]
            size = a*b*(a+b-1)
            groups = {}
            for dimension in range(1, size+1):
                key = independent_sizes(a, b, dimension)
                groups.setdefault(key, []).append(dimension)
            values = {}
            for n in range(1, isqrt(size)+1):
                lower = isqrt(isqrt((6*n)**9*10**24))
                upper = lower+int(lower**4 != (6*n)**9*10**24)
                self.assertEqual(v.prior.squares.score_interval(n), (lower, upper))
                values[n] = upper
            actual = [None]*size
            for (sizes, one_scalar), dimensions in groups.items():
                scores = item_first_scores(sizes, max(dimensions), values)
                for dimension in dimensions:
                    score = scores[dimension]
                    if one_scalar and scores[dimension-1] >= 0:
                        score = max(score, scores[dimension-1]+values[1])
                    actual[dimension-1] = score if score >= 0 else None
            self.assertEqual(actual, source["dimension_score_upper_numerators"], (a, b))
            maximum = source["maximum"]
            self.assertEqual(max(x for x in actual if x is not None), maximum["upper_score_numerator"])
            shape = maximum["maximizing_relaxed_partition"]
            D = sum(n*n for n in shape)
            self.assertEqual(D, maximum["target_leg_dimension"])
            sizes, one_scalar = independent_sizes(a, b, D)
            self.assertTrue(all(n in sizes or n == 1 and one_scalar for n in shape))
            if one_scalar:
                self.assertLessEqual(shape.count(1), 1)
            self.assertEqual(sum(values[n] for n in shape), maximum["upper_score_numerator"])
            self.assertEqual(source["all_partitions_below_critical_score"],
                             maximum["upper_score_numerator"] < (3*(a+b)-2)**3*10**6)
            lower = sum(v.prior.squares.score_interval(n)[0] for n in shape)
            self.assertEqual(lower, maximum["lower_score_numerator"])
            if not source["all_partitions_below_critical_score"]:
                self.assertGreater(lower, (3*(a+b)-2)**3*10**6)

    def test_new_single_target_and_strict_rank_boundary(self):
        target = self.saved["unconstructed_single_target"]
        self.assertEqual(target, v.single_target())
        self.assertEqual(target["lift_rank_upper_bound"], 534)
        self.assertIn(30, independent_sizes(8, 9, 900)[0])
        self.assertNotIn(31, independent_sizes(8, 9, 961)[0])
        self.assertGreater(180**5621, 49**7500)
        self.assertLess(4*5621, 9*2500)
        self.assertGreater(target["score_interval_numerators"][0], 117649*10**6)
        self.assertFalse(target["target_constructed"])

    def test_source_pins_and_package_manifest(self):
        for name in ["sources.json", "manifest.json"]:
            data = json.loads((PACKAGE / name).read_text())
            entries = data["local_dependencies"] if name == "sources.json" else [
                {"path": path, "sha256": digest} for path, digest in data["sha256"].items()
            ]
            for row in entries:
                self.assertEqual(hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest(),
                                 row["sha256"], row["path"])


if __name__ == "__main__":
    unittest.main()

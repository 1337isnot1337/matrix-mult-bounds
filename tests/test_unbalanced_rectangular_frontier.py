"""Complete format enumeration and independent exclusion-witness replay."""
import hashlib
import importlib.util
import itertools
import json
from math import isqrt
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-unbalanced-rectangular-frontier"
RESULT = ROOT / "results/unbalanced-rectangular-frontier-2026-10-23/frontier.json"
SPEC = importlib.util.spec_from_file_location("test_unbalanced_rectangular", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


def valid_witness(a, b, shape, witness):
    x, y = witness["matrix_parameter_dimensions"]
    z = witness["slice_rank"]
    if sorted([x, y, z]) != shape:
        return False
    lift = z+2*a*b*(a+b-1)-z*(x+y)
    if witness["lift_rank_upper_bound"] != lift or witness["block_parameter_dimension"] != x*y:
        return False
    if witness["gate"] == "minimum_slice_rank":
        return witness["required_rank"] == a*b and lift < a*b
    if witness["gate"] == "polynomial_rank_locus":
        return (witness["required_rank"] == 2*a*b and witness["dimension_cap"] == a*b
                and lift < 2*a*b and x*y > a*b)
    if witness["gate"] != "hankel_linear_annihilator":
        return False
    r = witness["symbol_rank"]
    cap = max(r, max(1, (3*r-a-b+4)//2)**2)
    return (1 <= r < min(a, b) and 5*r < 2*(a+b)
            and witness["symbol_image_cap"] == cap
            and witness["required_rank"] == (r+1)*a*b
            and witness["dimension_cap"] == cap*a*b
            and lift < (r+1)*a*b and x*y > cap*a*b)


class UnbalancedRectangularFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads(RESULT.read_text())

    def test_complete_source_and_shape_enumeration(self):
        expected_sources = {(a, b) for a in range(2, 10) for b in range(a, 26)
                            if a*b*(a+b-1) <= 1377}
        self.assertGreater(10*10*19, 1377)
        self.assertGreater(2*26*27, 1377)
        self.assertEqual({tuple(row["source"]) for row in self.saved["sources"]}, expected_sources)
        self.assertEqual(len(self.saved["sources"]), 82)
        total = 0
        for source in self.saved["sources"]:
            a, b = source["source"]
            N = a*b*(a+b-1)
            self.assertEqual(source["source_leg_dimension"], N)
            # Direct full interval enumeration, independent of the generator's
            # lower endpoint derived by integer division of the score threshold.
            expected = {(l, h, n) for l in range(1, isqrt(N)+1)
                        for h in range(l, isqrt(N)+1) for n in range(h, N//h+1)
                        if 216*l*h*n > (3*(a+b)-2)**4}
            actual = [tuple(row["shape"]) for row in source["records"]]
            self.assertEqual(set(actual), expected, (a, b))
            self.assertEqual(len(actual), len(expected))
            total += len(actual)
        self.assertEqual(total, 2113)
        self.assertEqual(self.saved, v.report())

    def test_all_2110_exclusion_certificates_and_corruptions(self):
        count = 0
        for source in self.saved["sources"]:
            a, b = source["source"]
            for row in source["records"]:
                l, h, n = row["shape"]
                self.assertEqual(row["leg_dimensions"], [l*h, h*n, n*l])
                self.assertEqual(row["volume"], l*h*n)
                if not row["excluded"]:
                    self.assertIsNone(row["witness"])
                    continue
                count += 1
                self.assertTrue(valid_witness(a, b, row["shape"], row["witness"]))
                broken = dict(row["witness"])
                broken["lift_rank_upper_bound"] -= 1
                self.assertFalse(valid_witness(a, b, row["shape"], broken))
        self.assertEqual(count, 2110)
        self.assertEqual(self.saved["excluded_shapes"], count)

    def test_three_survivors_in_every_orientation_and_strict_boundary(self):
        self.assertEqual(self.saved["surviving_sources"], [[8, 9]])
        source = next(row for row in self.saved["sources"] if row["source"] == [8, 9])
        self.assertEqual(source["survivors"], [[28, 31, 31], [29, 30, 31], [30, 30, 30]])
        self.assertEqual(source["improving_shapes"], 222)
        for shape in source["survivors"]:
            for x, y, z in itertools.permutations(shape):
                lift = z+2304-z*(x+y)
                self.assertGreaterEqual(lift, 72)
                self.assertFalse(lift < 144 and x*y > 72)
                for r in range(1, 8):
                    if 5*r >= 34:
                        continue
                    cap = max(r, max(1, (3*r-13)//2)**2)
                    self.assertFalse(lift < (r+1)*72 and x*y > cap*72)
        self.assertIsNone(v.controls.symbol_cap(8, 9, 7))
        for key in ["survivors_are_constructions", "singular_degenerations_excluded",
                    "independent_review", "improves_omega"]:
            self.assertFalse(self.saved[key])

    def test_pinned_sources_and_package(self):
        for name in ["sources.json", "manifest.json"]:
            data = json.loads((PACKAGE / name).read_text())
            rows = data["local_dependencies"] if name == "sources.json" else [
                {"path": p, "sha256": h} for p, h in data["sha256"].items()
            ]
            for row in rows:
                self.assertEqual(hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest(),
                                 row["sha256"], row["path"])

    def test_higher_rank_input_constraints_and_exact_thresholds(self):
        source = next(row for row in self.saved["sources"] if row["source"] == [8, 9])
        self.assertEqual([row["orientations"][0]["maximum_parameter_rank"]
                          for row in source["survivor_higher_rank_constraints"]], [3, 3, 2])
        for constraint in source["survivor_higher_rank_constraints"]:
            self.assertFalse(constraint["stronger_global_dimension_bound_proved"])
            for orientation in constraint["orientations"]:
                x, y = orientation["matrix_parameter_dimensions"]
                z = orientation["slice_rank_multiplier"]
                k = orientation["maximum_parameter_rank"]
                loss = 2304-z*(x+y)
                self.assertEqual(loss, orientation["long_leg_loss"])
                self.assertEqual(orientation["lift_rank_upper_bound"], z*k+loss)
                self.assertLess(z*k+loss, 576)
                self.assertGreaterEqual(z*(k+1)+loss, 576)
                self.assertEqual(orientation["hankel_rank_upper_bound"], 7)


if __name__ == "__main__":
    unittest.main()

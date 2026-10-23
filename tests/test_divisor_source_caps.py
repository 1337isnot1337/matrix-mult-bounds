"""Independent determinants, literal block ranks and divisor-cap boundaries."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-divisor-source-caps"
SPEC = importlib.util.spec_from_file_location("divisor_source_caps", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class DivisorSourceCapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_complete_saved_control_replay(self):
        self.assertEqual(v.verify(self.record), {
            "base_minors": 110, "residue_blocks": 330, "divisor_strips": 60,
            "a4_cases": 10, "nondivisor_boundaries": 1, "improves_omega": False})

    def test_sharp_intervals_at_divisors_of_composite_sizes(self):
        cases = {(r["a"], r["d"]): r for r in self.record["divisor_strips"]}
        for key, expected in (((4, 2), (8, 20, 23)), ((6, 2), (12, 42, 47)),
                              ((6, 3), (18, 48, 53)), ((9, 3), (27, 99, 107))):
            record = cases[key]
            self.assertEqual((record["dimension_cap"], record["sharp_ceiling_min"],
                              record["strict_ceiling_max"]), expected)
        self.assertNotIn((6, 4), cases)

    def test_literal_dense_ranks_include_crossed_and_wrapped_pairs(self):
        for a, d, positions in ((4, 2, [(0, 0), (2, 2)]),
                                (6, 2, [(4, 0), (0, 2)]),
                                (6, 3, [(3, 0), (0, 3)])):
            middle = 2*a-1
            coefficients = {point: 1 for point in positions}
            literal = s.Matrix([[coefficients.get((height-j, ell-r), 0)
                                 for height in range(middle) for r in range(a)]
                                for j in range(a) for ell in range(middle)])
            self.assertGreaterEqual(literal.to_DM().rank(), a*(a+d))

    def test_bareiss_against_a_separate_exact_backend(self):
        examples = [[], [[0]], [[0, 1], [1, 0]], [[2, 3], [5, 7]],
                    [[0, 2, 1], [3, -1, 4], [5, 0, 2]],
                    [[1, 2, 3], [2, 4, 6], [7, 8, 9]]]
        for values in examples:
            self.assertEqual(v.bareiss_determinant(values), s.Matrix(values).det())
        for entry in self.record["base_minors"][::27]:
            values = v.matrix(entry["p"], v.coordinates(entry["alpha"], entry["beta"],
                                                        entry["orientation"]))
            minor = s.Matrix([[values[i][j] for j in entry["columns"]] for i in entry["rows"]])
            self.assertEqual(minor.to_DM().det(), entry["determinant"])

    def test_nondivisor_pair_does_not_meet_the_divisor_threshold(self):
        boundary = self.record["nondivisor_boundary"]
        self.assertNotEqual(boundary["a"] % boundary["d"], 0)
        literal = s.Matrix(v.matrix(5, [(0, 0), (2, 2)]))
        self.assertEqual(literal.to_DM().rank(), 34)
        self.assertLess(boundary["exact_rank"], boundary["naive_divisor_threshold"])
        bad = copy.deepcopy(boundary)
        bad["active_determinant"] = 1
        with self.assertRaises(ValueError):
            v.verify_nondivisor_control(bad)

    def test_corrupt_minor_scope_and_divisor_witness_are_rejected(self):
        for mutate in (
            lambda record: record["base_minors"][0].update(determinant=2),
            lambda record: record["base_minors"][0]["rows"].__setitem__(0, -1),
            lambda record: record["residue_blocks"][0].update(blocks=9),
            lambda record: record["divisor_strips"][0].update(dimension_cap=99),
            lambda record: record.update(improves_omega=True),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_dependencies_and_inherited_a4_boundary(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(len(original["local_dependencies"])):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        self.assertTrue(self.record["a4_corollary"][8]["excluded"])
        self.assertFalse(self.record["a4_corollary"][9]["excluded"])
        self.assertEqual(self.record["a4_corollary"][9]["first_rank_margin"], 0)


if __name__ == "__main__":
    unittest.main()

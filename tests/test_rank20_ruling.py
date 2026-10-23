"""Rank20 factor families, generic-pencil hypotheses and the rank105 chart."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-rank20-ruling"
SPEC = importlib.util.spec_from_file_location("rank20_ruling", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class Rank20RulingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_exact_rank20_controls(self):
        self.assertEqual(v.verify(self.record), {
            "fixed_divisor_spaces": 8, "actual_source_ranks": 24,
            "independent_pencils": 4, "splitting_degree_cases": 22,
            "a4_long_limit_cases": 8, "sharp_linear_space_dimension": 8,
            "minimum_excluded_long_limit_rank": 105, "improves_omega": False,
            "selected_size_splitting_cases": 331, "additional_source_sizes": 3,
            "all_size_target_examples": 4,
        })

    def test_rank105_is_included_but_rank104_is_not(self):
        yes, no = v.a4_criterion(105), v.a4_criterion(104)
        self.assertTrue(yes["excluded_by_this_criterion"])
        self.assertEqual(yes["source_rank_cap"], 20)
        self.assertEqual(yes["nonzero_lift_margin"], 7)
        self.assertFalse(no["excluded_by_this_criterion"])
        self.assertEqual(no["source_rank_cap"], 21)
        self.assertIsNone(no["source_space_dimension_bound"])
        for rank in (-1, 111, True):
            with self.subTest(rank=rank), self.assertRaises(ValueError):
                v.a4_criterion(rank)

    def test_independence_is_required_for_the_pencil_gcd_lemma(self):
        records, independent, dependent = v.pencil_controls()
        self.assertEqual(len(records), 4)
        self.assertEqual(independent, {"rational_function_rank": 2,
                                      "joint_gcd_degree": 0, "generic_gcd_degree": 0})
        self.assertEqual(dependent, {"rational_function_rank": 1,
                                    "joint_gcd_degree": 0, "generic_gcd_degree": 2})
        for record in self.record["fixed_divisor_spaces"]:
            self.assertEqual(record["space_dimension"], 8)
            self.assertEqual(record["actual_source_ranks"], [16, 20, 20])

    def test_exhaustive_splitting_budget_forces_two_constant_kernel_vectors(self):
        records = v.splitting_controls()
        self.assertEqual([len(c["admissible_degrees"]) for c in records], [1, 15, 3, 3])
        for record in records[2:]:
            for degrees in record["admissible_degrees"]:
                self.assertEqual(degrees.count(0), 2)
                self.assertEqual(sum(degrees), 4*record["primitive_degree"])

    def test_all_size_source_bounds_and_target_thresholds(self):
        controls = self.record["all_size_controls"]
        self.assertEqual([c["total_cases"] for c in controls["splitting_degrees"]],
                         [2, 7, 22, 69, 231])
        for space in controls["fixed_divisor_spaces"]:
            a = space["source_size"]
            self.assertEqual(space["space_dimension"], 2*a)
            self.assertEqual(space["actual_source_ranks"], [a*a, a*a+a])
        self.assertEqual([c["long_rank_threshold"] for c in controls["target_examples"]],
                         [105, 216, 212, 210])
        with self.assertRaises(ValueError):
            v.general_threshold(4, 8, 11)

    def test_reject_false_next_boundary_and_changed_source_pins(self):
        bad = copy.deepcopy(self.record)
        bad["a4_long_limit_cases"][6]["excluded_by_this_criterion"] = True
        with self.assertRaises(ValueError):
            v.verify(bad)
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(4):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        bad = copy.deepcopy(original)
        bad["local_dependencies"].pop()
        with self.assertRaises(ValueError):
            v.check_sources(bad)


if __name__ == "__main__":
    unittest.main()

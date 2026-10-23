"""Retraction witnesses, strict source-rank boundaries and evidence integrity."""
import copy
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-unit-image-rank-gap"
SPEC = importlib.util.spec_from_file_location("unit_image_rank_gap", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class UnitImageRankGapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_saved_controls_replay(self):
        self.assertEqual(v.verify(self.record), {
            "retractions": 56, "source_matrices": 9, "a4_rank_cases": 5,
            "lowest_excluded_unit_image_rank": 107, "improves_omega": False})

    def test_retraction_against_exhaustive_small_integer_search(self):
        h = s.eye(3)[:, :2]
        projections = [s.eye(2).row_join(s.Matrix(2, 1, z))
                       for z in product(range(3), repeat=2)]
        for bits in product((0, 1), repeat=6):
            y = s.Matrix(3, 2, bits)
            expected = max((p*y).rank() for p in projections)
            self.assertEqual(expected, y.rank())
            p = v.rank_preserving_retraction(h, y)
            self.assertEqual(p*h, s.eye(2))
            self.assertEqual((p*y).rank(), expected)

    def test_rank107_and_unresolved_rank106(self):
        by_rank = {case["retained"]: case for case in self.record["a4_rank_margins"]}
        self.assertEqual(by_rank[107]["strict_margins"], {
            "first_pole": 1, "injectivity": 3,
            "rank_locus": 6, "parameter_dimension": 84})
        self.assertTrue(by_rank[107]["excludes_target"])
        self.assertFalse(by_rank[106]["forces_regularity"])
        self.assertEqual(by_rank[106]["strict_margins"]["first_pole"], -2)
        self.assertEqual(by_rank[107]["ordinary_rank_floor"], 12)

    def test_actual_source_ranks_and_fixed_projection_loss(self):
        a4 = [c["exact_rank"] for c in self.record["source_controls"] if c["a"] == 4]
        self.assertEqual(a4, [16, 28, 32])
        example = v.hidden_rank_control()
        self.assertEqual(example["fixed_projection_rank"], 5)
        self.assertEqual(example["constructed_retraction_rank"], 8)

    def test_reject_corrupted_scope_or_rank_claim(self):
        for field, value in (("improves_omega", True),
                             ("proof_status", "reviewed-proof")):
            bad = copy.deepcopy(self.record)
            bad[field] = value
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_corrupted_dependency_or_invalid_retraction(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(len(original["local_dependencies"])):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        bad = copy.deepcopy(original)
        bad["local_dependencies"].pop()
        with self.assertRaises(ValueError):
            v.check_sources(bad)
        with self.assertRaises(ValueError):
            v.rank_preserving_retraction(s.zeros(3, 2), s.zeros(3, 2))
        with self.assertRaises(ValueError):
            v.margins(4, 10, 11, 111)


if __name__ == "__main__":
    unittest.main()

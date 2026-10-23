"""Exact stacked-product controls and the strict A4 rank104 boundary."""
import copy
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import unittest

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-unit-image-stacked-rank"
SPEC = importlib.util.spec_from_file_location("unit_image_stacked_rank", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class UnitImageStackedRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_saved_controls_replay(self):
        self.assertEqual(v.verify(self.record), {
            "stacked_products": 48, "rank_one_kernel_spaces": 3,
            "a4_rank_cases": 7, "lowest_excluded_unit_image_rank": 105,
            "improves_omega": False})

    def test_rank105_margins_and_noninjective_kernel_budget(self):
        cases = {c["retained"]: c for c in self.record["a4_rank_margins"]}
        self.assertEqual(cases[105]["strict_margins"], {
            "first_pole": 2, "kernel_rank_two": 10,
            "source_rank_locus": 7, "image_dimension": 74})
        self.assertEqual(cases[105]["kernel_rank_bound"], 1)
        self.assertEqual(cases[105]["first_image_dimension_floor"], 90)
        self.assertTrue(cases[105]["excludes_target"])
        self.assertFalse(cases[104]["forces_regularity"])
        self.assertEqual(cases[104]["strict_margins"]["first_pole"], 0)

    def test_sharp_block_boundary_does_not_claim_a_cyclic_witness(self):
        boundary = [c for c in self.record["stacked_products"] if c["inner_dimension"] == 8]
        self.assertEqual(len(boundary), 6)
        self.assertTrue(all(c["source_leading_rank"] == 16 for c in boundary))
        self.assertIn("not cyclic degenerations", self.record["scope"])

    def test_rank_one_pencils_against_complete_binary_pair_inventory(self):
        matrices = [s.Matrix(2, 2, values) for values in product((0, 1), repeat=4)]
        rank_one = [matrix for matrix in matrices if matrix.rank() == 1]
        for left, right in combinations(rank_one, 2):
            if (left+right).rank() > 1 or (left-right).rank() > 1:
                continue
            column_span = left.row_join(right).rank()
            row_span = left.col_join(right).rank()
            self.assertTrue(column_span == 1 or row_span == 1)

    def test_reject_corrupted_scope(self):
        bad = copy.deepcopy(self.record)
        bad["improves_omega"] = True
        with self.assertRaises(ValueError):
            v.verify(bad)

    def test_dependency_integrity_and_invalid_dimensions(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(len(original["local_dependencies"])):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        with self.assertRaises(ValueError):
            v.margins(4, 10, 11, 111)


if __name__ == "__main__":
    unittest.main()

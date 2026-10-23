"""Literal source replay and highest-pole evidence boundaries."""
import copy
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-unit-image-pole-flags"
SPEC = importlib.util.spec_from_file_location("unit_image_pole_flags", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class UnitImagePoleFlagTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_literal_source_agrees_with_maintained_formula(self):
        spec = importlib.util.spec_from_file_location(
            "pole_flag_literal_source", ROOT / "research/ai/2026-10-20-koszul/cyclic_finite_target.py")
        literal = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(literal)
        for a in (2, 3, 4):
            f = [(j*7+2)%11-5 for j in range(a*a*(2*a-1))]
            actual = v.source_matrix(f, a)
            rows = list(product(range(a), range(a), range(2*a-1)))
            columns = list(product(range(2*a-1), range(a), range(a)))
            expected = [[literal.slice_entry(f, a, row, column) for column in columns]
                        for row in rows]
            self.assertEqual(actual.tolist(), expected)

    def test_all_exact_source_controls(self):
        self.assertEqual(v.verify(self.record), {
            "unit_image_rank_cases": 5, "ruling_families": 8,
            "literal_minimum_source_ranks": 24, "source_countercontrols": 3,
            "improves_omega": False})
        survivor = self.record["source_controls"]["rank106_block_budget_survivor"]
        self.assertEqual(survivor["block_ranks"], [4, 10, 16])
        self.assertFalse(survivor["target_constructed"])
        self.assertFalse(survivor["unit_frame_compatibility_claimed"])

    def test_reject_false_exclusion_and_changed_ruling(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x["ruling_controls"][0].update(dimension=5),
            lambda x: x["source_controls"]["rank106_block_budget_survivor"].update(
                target_constructed=True),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_changed_dependencies(self):
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

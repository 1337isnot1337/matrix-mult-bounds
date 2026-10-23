"""Partial-frame algebra, independent targets and non-strict boundary controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-partial-regular-frames"
SPEC = importlib.util.spec_from_file_location("partial_regular_frames", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class PartialRegularFramesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_every_exact_control_and_predecessor_replay(self):
        self.assertEqual(v.verify(self.record),
                         {"independent_frame_examples": 4, "polar_unit_examples": 12,
                          "column_kernel_examples": 12, "a4_rank_cases": 3,
                          "improves_omega": False})

    def test_polar_examples_do_not_assert_source_rank_hypotheses(self):
        examples = self.record["polar_unit_and_long_map_examples"]
        self.assertEqual({x["unit_pole_order"] for x in examples}, {1, 2, 3})
        self.assertTrue(all(not x["source_rank_hypotheses_asserted"] for x in examples))
        cases = self.record["a4_rank_cases"]
        self.assertEqual(cases[1]["strict_margins"]["column_kernel_dimension"], 1)
        self.assertEqual(cases[2]["strict_margins"]["column_kernel_dimension"], 0)

    def test_false_equality_exclusion_and_erased_poles_are_rejected(self):
        for mutation in (
            lambda x: x.update(improves_omega=True),
            lambda x: x["a4_rank_cases"][2].update(forces_all_maps_regular=True),
            lambda x: x["polar_unit_and_long_map_examples"][0].update(unit_pole_order=0),
            lambda x: x["independent_target_frames"][0].update(target_frames_distinct=False),
        ):
            bad = copy.deepcopy(self.record)
            mutation(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_corrupted_and_missing_predecessor_is_rejected(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(3):
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

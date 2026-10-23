"""Exact Laurent correction replay and rejection of corrupted certificates."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-one-regular-leg"
SPEC = importlib.util.spec_from_file_location("one_regular_leg", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class OneRegularLegTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_exact_replay(self):
        self.assertEqual(v.verify(self.record), {
            "polar_projection_controls": 36, "vanishing_unit_controls": 6,
            "scalar_balancing_controls": 5, "rank_budget_controls": 9,
            "target_generators": 100, "strict_a4_rank_margin": 1, "improves_omega": False})

    def test_reject_changed_ranks_and_overstated_scope(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(independent_review=True),
            lambda x: x["a4"].update(strict_rank_margin=2),
            lambda x: x["a4"].update(both_balanced_long_maps_singular_excluded=True),
            lambda x: x["a4"]["target_generators"][0].update(slice_rank=10),
            lambda x: x["vanishing_units"][0].update(unit_limit_rank=1),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_changed_pins_and_removed_dependency(self):
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

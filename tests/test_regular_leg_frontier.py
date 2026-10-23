"""Independent source-coordinate controls and rejection of inflated rank claims."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-regular-leg-frontier"
SPEC = importlib.util.spec_from_file_location("regular_leg_frontier", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class RegularLegFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_full_original_source_and_rank_pair_replay(self):
        self.assertEqual(v.verify(self.record), {
            "coordinate_compressions": 10, "twice_minimum_controls": 5,
            "rank_pairs_checked": 23532, "improves_omega": False})

    def test_a4_attained_coherent_kernel_and_single_hidden_slice(self):
        controls = [r for r in self.record["coordinate_compressions"] if r["a"] == 4]
        self.assertEqual(controls[0]["regular_ranks"], [84, 110])
        self.assertEqual(controls[0]["projected_rank"], 96)
        self.assertEqual(controls[0]["kernel_dimension"], 16)
        self.assertEqual(controls[1]["regular_ranks"], [104, 104])
        self.assertEqual(controls[1]["projected_rank"], 111)

    def test_strict_threshold_and_surviving_pairs_are_preserved(self):
        self.assertEqual(v.projected_lower_bound(96, 96), 0)
        self.assertEqual(v.projected_lower_bound(96, 97), 96)
        self.assertFalse(v.screen(100, 107, "short_long")["excluded"])
        self.assertTrue(v.screen(100, 108, "short_long")["excluded"])
        self.assertTrue(v.screen(110, 110, "long_long")["ordinary_regularity_forced"])

    def test_reject_inflated_scope_and_corrupted_coordinate_evidence(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(independent_review=True),
            lambda x: x.update(target_constructed=True),
            lambda x: x["twice_minimum_boundary"][0].update(below_twice_minimum=True),
            lambda x: x["coordinate_compressions"][0].update(projected_rank=12),
            lambda x: x["rank_pair_screen"]["short_long"].update(surviving_high_pairs=[]),
        ):
            changed = copy.deepcopy(self.record)
            mutate(changed)
            with self.assertRaises(ValueError):
                v.verify(changed)

    def test_reject_changed_source_pins_or_removed_dependency(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for index in range(3):
            changed = copy.deepcopy(original)
            changed["local_dependencies"][index]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(changed)
        changed = copy.deepcopy(original)
        changed["local_dependencies"].pop()
        with self.assertRaises(ValueError):
            v.check_sources(changed)


if __name__ == "__main__":
    unittest.main()

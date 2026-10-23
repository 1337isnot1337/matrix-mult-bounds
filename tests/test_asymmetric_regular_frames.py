"""Complete frame-budget frontier, rank upgrades and corruption controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-asymmetric-regular-frames"
SPEC = importlib.util.spec_from_file_location("asymmetric_regular_frames", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class AsymmetricRegularFramesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_complete_finite_frontier_and_all_matrix_controls(self):
        receipt = v.verify(self.record)
        self.assertEqual(receipt, {"examined_pairs": 12100, "sufficient_pairs": 9,
                                  "minimal_pairs": [[106, 110], [107, 109]],
                                  "unit_upgrade_controls": 4, "unit_corank_controls": 11,
                                  "improves_omega": False})

    def test_weakest_frame_pairs_and_exact_failure_margins(self):
        self.assertEqual(v.a4_margins(106, 110)["strict_margins"], [2, 1, 2, 2])
        self.assertEqual(v.a4_margins(107, 109)["strict_margins"], [3, 2, 1, 1])
        self.assertEqual(v.a4_margins(106, 109)["strict_margins"][1], 0)
        self.assertEqual(v.a4_margins(110, 108)["strict_margins"][2:], [0, 0])
        self.assertFalse(v.a4_margins(105, 110)["sufficient"])

    def test_forged_threshold_missing_pair_and_erased_pole_are_rejected(self):
        for mutate in (
            lambda x: x.update(regular_unit_image_threshold=105),
            lambda x: x["a4_scan"]["sufficient_pairs"].pop(),
            lambda x: x["a4_scan"]["boundary_controls"][0].update(sufficient=True),
            lambda x: x["unit_rank_upgrade_examples"][0].update(unselected_column_pole=False),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_changed_or_removed_dependency_rejected(self):
        record = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(3):
            bad = copy.deepcopy(record)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        record["local_dependencies"].pop()
        with self.assertRaises(ValueError):
            v.check_sources(record)


if __name__ == "__main__":
    unittest.main()

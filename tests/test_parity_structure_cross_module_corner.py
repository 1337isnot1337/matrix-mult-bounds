"""Complete integer replay and meaningful map-tamper controls."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_cross_module_corner.py"
SPEC = importlib.util.spec_from_file_location("parity_structure_cross_module_corner", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CrossModuleCornerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(MODULE.MAPS.read_text())

    def test_complete_replay_and_both_exact_ranks(self):
        report = MODULE.verify(self.data)
        self.assertEqual(report["source_terms_checked"], 262144)
        self.assertEqual(report["all_target_coefficients_checked"], 36864)
        self.assertEqual(report["nonzero_target_coefficients"], 192)
        self.assertEqual(report["full_response_rank_exact"], 186)
        self.assertEqual(report["changed_first_core_flattening"]["exact_rational_rank"], 481)
        self.assertFalse(report["new_exponent_established"])

    def test_nonzero_to_nonzero_tamper_is_rejected(self):
        for leg in (0, 1):
            changed = copy.deepcopy(self.data)
            if leg == 0:
                selected = next(entry for entry in changed["maps"][0]["entries"]
                                if MODULE.decode(entry[1])[1] == 14)
            else:
                selected = next(entry for entry in changed["maps"][1]["entries"]
                                if entry[0] % 12 == 11)
            selected[2] *= 2
            with self.subTest(leg=leg):
                with self.assertRaises(ArithmeticError):
                    MODULE.verify(changed)


if __name__ == "__main__":
    unittest.main()

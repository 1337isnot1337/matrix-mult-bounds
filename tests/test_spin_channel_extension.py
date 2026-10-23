"""Exact acceptance of the private-channel attachment, using no dependencies."""

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/spin_channel_extension.py"
SPEC = importlib.util.spec_from_file_location("spin_channel_extension", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SpinChannelExtensionTests(unittest.TestCase):
    def test_complete_integer_replay(self):
        report, exported = MODULE.verify(exported=json.loads(MODULE.MAPS.read_text()))
        self.assertEqual(report["coefficient_replay"]["source_terms_checked"], 262144)
        self.assertEqual(report["coefficient_replay"]["target_coefficients_checked"], 237897)
        self.assertEqual(report["coefficient_replay"]["nonzero_target_coefficients"], 267)
        self.assertEqual(report["additional_response_rank_exact"], 24)
        self.assertEqual(report["full_response_rank_exact"], 216)
        self.assertEqual(report["first_preimage_dimension_after_extension"], 777)
        self.assertFalse(report["full_square_target_constructed"])
        self.assertFalse(exported["new_exponent_established"])

    def test_changed_attached_coefficient_is_rejected(self):
        maps, denominators, _ = MODULE.build_maps()
        maps[0][9][MODULE.coordinate(2, 4, 0)] += denominators[0]
        with self.assertRaisesRegex(ArithmeticError, "glued coefficient identity"):
            MODULE.coefficient_replay(maps, denominators)


if __name__ == "__main__":
    unittest.main()

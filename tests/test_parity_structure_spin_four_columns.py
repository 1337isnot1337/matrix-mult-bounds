"""Exact full-channel extension and complete response checks, without NumPy."""

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_four_columns.py"
SPEC = importlib.util.spec_from_file_location("parity_structure_spin_four_columns", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FullChannelExtensionTests(unittest.TestCase):
    def test_complete_source_and_response_replay(self):
        self.assertEqual(json.loads(MODULE.MAPS.read_text()), MODULE.build())
        report = MODULE.verify()
        self.assertEqual(report["source_terms_checked"], 262144)
        self.assertEqual(report["nonzero_target_coefficients"], 567)
        self.assertEqual(report["full_first_response_rank_exact"], 576)
        self.assertEqual(report["first_response_preimage_dimension"], 405)
        self.assertEqual([block["rank_exact"] for block in report["response_blocks"]], [192]*3)
        self.assertFalse(report["new_exponent_established"])

    def test_nonzero_added_channel_tamper_is_rejected(self):
        data = json.loads(MODULE.MAPS.read_text())
        for entry in data["maps"]["Z"]["entries"]:
            if (entry[1]//8) % 15 >= 9:
                entry[2] *= 2
                break
        else:
            self.fail("The construction has no added high-long-coordinate channel")
        with self.assertRaisesRegex(ArithmeticError, "complete M\\(3,7,27\\) coefficient"):
            MODULE.verify(data)

    def test_false_response_minor_is_rejected(self):
        specification = json.loads(MODULE.MINORS.read_text())
        specification["blocks"][1]["determinant_mod65521"] += 1
        with self.assertRaisesRegex(ArithmeticError, "regenerated response minor"):
            MODULE.verify(specification=specification)


if __name__ == "__main__":
    unittest.main()

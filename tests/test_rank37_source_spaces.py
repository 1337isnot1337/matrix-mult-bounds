"""Exact acceptance and corruption controls for the rank37 source-space theorem."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-rank37-source-spaces/verify.py"
SPEC = importlib.util.spec_from_file_location("rank37_source_spaces", PATH)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class Rank37SourceSpacesTests(unittest.TestCase):
    def test_complete_frozen_replay_and_sharpness(self):
        document = json.loads(verify.RESULT.read_text())
        verify.replay_saved(document)
        self.assertEqual(document["minor_controls"]["integer_minors_checked"], 14)
        self.assertEqual(document["minor_controls"]["axis_length_inventory"], {"1": 1, "2": 2, "3": 4, "4": 6})
        self.assertEqual(document["source_controls"]["sharpness_dimension"], 16)
        self.assertEqual(document["source_controls"]["sharpness_uniform_rank_upper"], 28)

    def test_missing_and_duplicate_ideals_are_rejected(self):
        document = json.loads(verify.CERTIFICATES.read_text())
        document["source17_ideals"].pop()
        with self.assertRaisesRegex(ArithmeticError, "incomplete source17"):
            verify.replay_certificates(document)
        document = json.loads(verify.CERTIFICATES.read_text())
        document["source17_ideals"][1] = copy.deepcopy(document["source17_ideals"][0])
        with self.assertRaisesRegex(ArithmeticError, "duplicate source17"):
            verify.replay_certificates(document)

    def test_outside_layer_and_singular_minor_are_rejected(self):
        document = json.loads(verify.CERTIFICATES.read_text())
        document["source17_ideals"][0]["coefficient_mask"] = hex(1 << verify.SOURCE.index((0, 2, 0)))
        with self.assertRaisesRegex(ArithmeticError, "support leaves"):
            verify.replay_certificates(document)
        document = json.loads(verify.CERTIFICATES.read_text())
        document["source17_ideals"][0]["coefficient_mask"] = "0x1"
        with self.assertRaisesRegex(ArithmeticError, "singular modulo two"):
            verify.replay_certificates(document)

    def test_wrong_minor_dimensions_and_modulus_are_rejected(self):
        document = json.loads(verify.CERTIFICATES.read_text())
        first = document["source17_ideals"][0]
        mask = int(first["minor_rows_mask"], 16)
        first["minor_rows_mask"] = hex(mask & (mask - 1))
        with self.assertRaisesRegex(ArithmeticError, "wrong dimensions"):
            verify.replay_certificates(document)
        document = json.loads(verify.CERTIFICATES.read_text())
        document["verification_modulus"] = 3
        with self.assertRaisesRegex(ArithmeticError, "certificate header"):
            verify.replay_certificates(document)

    def test_source_pin_and_inventory_are_checked(self):
        document = json.loads((verify.HERE / "sources.json").read_text())
        changed = copy.deepcopy(document)
        changed["local_dependencies"][1]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            verify.check_sources(changed)
        document["local_dependencies"].pop()
        with self.assertRaisesRegex(ArithmeticError, "source inventory"):
            verify.check_sources(document)

    def test_strict_threshold_and_unproved_mixed_consequence_are_not_inflated(self):
        document = json.loads(verify.RESULT.read_text())
        document["claim_scope"]["source_rank_strict_upper"] = 40
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)
        document = json.loads(verify.RESULT.read_text())
        document["claim_scope"]["mixed_leg_rank_consequence_claimed"] = True
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)


if __name__ == "__main__":
    unittest.main()

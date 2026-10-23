"""Independent replay and certificate-integrity controls for the cactus result."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/ai/2026-10-23-mixed-longlegs-candidate/verify_cactus.py"
SPEC = importlib.util.spec_from_file_location("mixed_longlegs_cactus_verifier", SCRIPT)
VERIFIER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFIER)


class MixedLonglegsCactusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads(VERIFIER.OUTPUT.read_text())

    def test_complete_exact_replay(self):
        self.assertEqual(VERIFIER.build_report(), self.saved)
        self.assertEqual(self.saved["target"]["flattening_ranks"], [5, 100, 140])
        self.assertEqual(self.saved["target"]["curve_slice_ranks"], [62] * 6)
        self.assertEqual(self.saved["target"]["cactus_rank"], 178)
        self.assertFalse(self.saved["scope"]["target_border_rank_determined"])

    def test_saved_interpolation_witnesses_and_tamper_rejection(self):
        for witness in self.saved["interpolation_witnesses"]:
            name = witness["block"]
            self.assertEqual(VERIFIER.verify_interpolation_witness(name, witness), witness["verification"])
        corrupted = copy.deepcopy(self.saved["interpolation_witnesses"][0])
        corrupted["lagrange_coefficient_rows"][0][0] = "2"
        with self.assertRaisesRegex(ValueError, "Lagrange"):
            VERIFIER.verify_interpolation_witness(corrupted["block"], corrupted)

    def test_discovery_pin_rejects_changed_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            changed = Path(directory) / "changed.json"
            changed.write_bytes(VERIFIER.INPUT.read_bytes() + b"\n")
            with self.assertRaisesRegex(ValueError, "byte pin"):
                VERIFIER.check_discovery_input(changed)

    def test_small_wild_tensor_literal_controls(self):
        toy = VERIFIER.wild_toy_controls()
        self.assertEqual(toy, self.saved["small_wild_tensor"])
        self.assertEqual(toy["flattening_ranks"], [2, 3, 3])
        self.assertEqual(toy["first_slice_ranks"], [2] * 4)
        self.assertEqual((toy["border_rank"], toy["cactus_rank"]), (3, 4))


if __name__ == "__main__":
    unittest.main()

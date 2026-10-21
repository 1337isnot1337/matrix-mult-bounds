import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin22_fourth_vertex.py"
SPEC = importlib.util.spec_from_file_location("fourth_vertex", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FourthVertexTests(unittest.TestCase):
    def test_complete_coefficients_and_three_leg_responses(self):
        report = MODULE.verify()
        self.assertEqual(report["tiny"]["all_target_coefficients_checked"],576)
        self.assertEqual(report["tiny"]["nonzero_target_coefficients"],24)
        self.assertEqual(report["targets"]["32"]["full_response_ranks_exact"],[192,288,288])
        self.assertEqual(report["targets"]["28"]["full_response_ranks_exact"],[192,252,252])
        self.assertEqual(report["targets"]["28"]["exact_core_preimage_dimensions"],[780,820,792])
        self.assertFalse(report["new_exponent_established"])

    def test_nonzero_to_nonzero_tiny_y_tamper_is_rejected(self):
        witness = json.loads(MODULE.WITNESS.read_text())
        witness["maps"]["Y"]["entries"][0][2] *= 2
        with self.assertRaises(ArithmeticError):
            MODULE.verify(witness=witness)

    def test_third_leg_minor_tamper_is_rejected(self):
        data = json.loads(MODULE.MINORS.read_text())
        data["targets"]["28"]["Z"]["determinant_mod_prime"] += 1
        with self.assertRaises(ArithmeticError):
            MODULE.verify(minors=data)


if __name__ == "__main__":
    unittest.main()

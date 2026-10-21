"""Exact full-source replay of the Laurent core and both retained arms."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_jet_extension.py"
SPEC = importlib.util.spec_from_file_location("parity_structure_jet_extension", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class MatrixCoreJetExtensionTests(unittest.TestCase):
    def test_all_a88_source_terms_and_nonzero_arm_tamper(self):
        report = MODULE.verify()
        self.assertEqual(report["source_terms_examined"], 262144)
        self.assertEqual(report["source_terms_meeting_all_three_maps"], 902)
        self.assertEqual(report["target_leg_dimension"], 134)
        self.assertEqual(report["constant_target_flattening_ranks"], [134, 134, 134])
        self.assertEqual(report["selected_original_source_columns_per_leg"], [134, 134, 134])
        self.assertEqual(report["map_nonzero_monomials"], [278, 278, 278])
        self.assertEqual(report["nonzero_coefficients_by_power"],
                         {"0": 1514, "2": 36, "3": 216, "6": 1512, "12": 216})
        self.assertTrue(report["nonzero_to_nonzero_arm_tamper_rejected"])
        self.assertFalse(report["new_exponent_established"])

    def test_smallest_extension_retains_all_directions(self):
        report = MODULE.verify(MODULE.build(3))
        self.assertEqual(report["source_terms_examined"], 729)
        self.assertEqual(report["target_leg_dimension"], 9)
        self.assertEqual(report["constant_target_terms"], 14)
        self.assertEqual(report["constant_target_flattening_ranks"], [9, 9, 9])


if __name__ == "__main__":
    unittest.main()

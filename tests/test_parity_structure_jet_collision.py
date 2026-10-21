"""Complete exact Laurent identities, including coefficient cancellation."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_jet_collision.py"
SPEC = importlib.util.spec_from_file_location("parity_structure_jet_collision", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class MatrixCoreJetCollisionTests(unittest.TestCase):
    def test_complete_a88_laurent_identity_and_nonzero_tamper(self):
        report = MODULE.verify()
        self.assertEqual(report["source_terms_examined"], 262144)
        self.assertEqual(report["target_leg_dimension"], 110)
        self.assertEqual(report["nonzero_coefficients_by_power"], {"0": 1298, "2": 1296, "4": 216})
        self.assertTrue(report["all_negative_powers_cancel_exactly"])
        self.assertTrue(report["nonzero_to_nonzero_tamper_rejected"])
        self.assertFalse(report["full_target_27_plus_7_witness"])

    def test_smallest_composed_source_and_scalar_slice_invariant(self):
        report = MODULE.verify(MODULE.build(3))
        self.assertEqual(report["source_terms_examined"], 729)
        self.assertEqual(report["target_leg_dimension"], 5)
        self.assertEqual(report["constant_target_terms"], 8)
        scalar = report["scalar_genuinely_singular_control"]
        self.assertEqual(scalar["constant_target_terms"], 6)
        self.assertEqual(scalar["nilpotence_index"], 3)
        self.assertEqual(scalar["normalized_nonzero_nilpotent_slice"], [[0, 1, 0], [0, 0, 1], [0, 0, 0]])


if __name__ == "__main__":
    unittest.main()

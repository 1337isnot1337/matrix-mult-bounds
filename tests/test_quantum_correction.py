"""Exact controls for the scoped quantum correction screens."""
import importlib.util
from pathlib import Path
import unittest


class QuantumCorrectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[1]
        spec = importlib.util.spec_from_file_location(
            "quantum_correction_test_verifier",
            root/"research/ai/2026-10-21-quantum-correction/verify.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.result = module.verify()

    def test_full_exact_source_composition(self):
        self.assertEqual(self.result["exact_source_control_coefficients"], 576)
        self.assertEqual(self.result["exact_regular_tensor_nonzero_coefficients"], 416)
        self.assertTrue(self.result["full_tensor_composition_matches_stored"])

    def test_extreme_and_adjacent_rank_deficits(self):
        witnesses = {row["weight"]: row for row in self.result["slice_rank_witnesses"]}
        for weight in (-8, 8):
            self.assertEqual(witnesses[weight]["exact_rank"], 6)
            self.assertEqual(witnesses[weight]["target_weight_space_maximum_rank"], 4)
        for weight in (-6, 6):
            self.assertEqual(witnesses[weight]["exact_rank"], 9)
            self.assertEqual(witnesses[weight]["target_weight_space_maximum_rank"], 8)

    def test_central_obstruction_scope(self):
        self.assertEqual(self.result["central_anchor_rank"], 20)
        self.assertEqual(self.result["central_commutator_exact_rank"], 14)
        self.assertEqual(len(self.result["excluded_D6_weight_assignments"]), 3)
        self.assertFalse(self.result["excludes_unrestricted_corrections"])
        self.assertFalse(self.result["improves_omega"])


if __name__ == "__main__":
    unittest.main()

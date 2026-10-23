"""Exact checks of the fixed-seed pencil reduction and rank contradiction."""
import importlib.util
from pathlib import Path
import unittest


class BulkPartialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[1]
        spec = importlib.util.spec_from_file_location("bulk_partial_verifier", root/"research/ai/2026-10-21-bulk-partial/verify.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.result = module.verify()

    def test_exact_seed_and_free_directions(self):
        for seed in self.result["exact_seed_controls"]:
            self.assertEqual(seed["exact_target_terms"], 8)
            self.assertEqual(seed["pre_A_rank"], 16)
            self.assertEqual(len(seed["kernel_A_coordinates"]), 20)

    def test_cross_reduction_and_both_units(self):
        cross = self.result["first_cross"]
        self.assertEqual(cross["exact_nonzero_cross_coefficients"], 40)
        self.assertEqual(cross["ambient_cross_coefficient_positions"], 768)
        self.assertTrue(cross["both_unit_cases_symbolically_verified"])
        self.assertTrue(cross["generic_unit_inverse_verified"])
        self.assertEqual(cross["sharp_source_rank_control"], 2)
        self.assertEqual(cross["required_target_edge_rank"], 4)

    def test_scope(self):
        self.assertFalse(self.result["excludes_arbitrary_Laurent_families"])
        self.assertFalse(self.result["improves_omega"])


if __name__ == "__main__":
    unittest.main()

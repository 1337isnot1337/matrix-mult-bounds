"""Exact coefficient and structural controls for controlled transposes."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "research/ai/2026-10-21-centered-orientations/verify.py"
SPEC = importlib.util.spec_from_file_location("centered_orientations_verify", FILE)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class CenteredOrientationTests(unittest.TestCase):
    def test_all_correction_coefficients(self):
        for s in (2, 3, 4):
            result = VERIFY.aggregate_and_corrections(s)
            self.assertEqual(result["correction_rank_one_terms"], 12*s**4)
            self.assertEqual(result["surviving_nonzero_coefficients"], 4*s**6)

    def test_exact_grams_and_algebra_witness(self):
        for s in (2, 3, 4):
            self.assertEqual(VERIFY.gram_certificate(s)["gram_scalars"], [4, s**3, s**3])
            self.assertEqual(VERIFY.multiplication_witness(s)["nonzero_residual_entries"], 2*s*s)

    def test_repair_rank_and_separate_source(self):
        for s in (2, 3, 4):
            self.assertEqual(VERIFY.orbit_repair_rank(s)["first_flattening_rank"],
                             3*(s**6-s**4)//4)
        for s in (2, 3):
            self.assertEqual(VERIFY.factor_source_certificate(s)["selected_nonzero_coefficients"],
                             4*s**6)


if __name__ == "__main__":
    unittest.main()

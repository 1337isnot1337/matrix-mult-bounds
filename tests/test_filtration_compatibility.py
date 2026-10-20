"""Regression checks for the concavity proof and its asymmetric cases."""
import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "filtration_compatibility",
    ROOT / "research/ai/2026-10-20-affine-direct-sums/verify_filtration.py",
)
filtration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(filtration)


class FiltrationTests(unittest.TestCase):
    def test_asymmetric_proof_chains(self):
        for dims in [(1, 9, 11, 1), (2, 97, 53, 3), (15, 2, 1, 131),
                     (1, 1, 1, 1), (3, 5, 7, 11)]:
            with self.subTest(dims=dims):
                self.assertGreater(filtration.verify_case(*dims), 8)

    def test_source_pair_exchange(self):
        self.assertEqual(filtration.row_certificate(3, 11, 7, 5),
                         filtration.row_certificate(7, 5, 3, 11))

    def test_jensen_equality_and_strictness(self):
        linear = filtration.row_certificate(1, 3, 2, 5)
        curved = filtration.row_certificate(9, 3, 8, 5)
        self.assertEqual(linear[0], linear[1])
        self.assertLess(curved[0], curved[1])

    def test_known_profile(self):
        self.assertEqual(filtration.profile(2, 2), Fraction(10, 3))
        self.assertEqual(filtration.profile(3, 3), Fraction(56, 9))

    def test_invalid_dimensions(self):
        for dims in [(0, 2, 3, 4), (1, -2, 3, 4), (1, 2, 3, 1.5)]:
            with self.assertRaises(ValueError):
                filtration.row_certificate(*dims)

    def test_small_exhaustive_proof_certificates(self):
        result = filtration.run(4)
        self.assertEqual(result["source_quadruples"], 256)
        self.assertEqual(result["violations"], 0)


if __name__ == "__main__":
    unittest.main()

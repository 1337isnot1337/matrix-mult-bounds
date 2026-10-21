import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "cyclic_singular", ROOT / "research/ai/2026-10-20-cyclic-singular-search/verify.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class CyclicSingularTests(unittest.TestCase):
    def test_complete_fixed_kernel_certificates(self):
        self.assertEqual(v.report(), json.loads((v.RESULTS / "exact-verification.json").read_text()))

    def test_corrupt_kernel_and_minor_are_rejected(self):
        certificate = json.loads((v.RESULTS / "fixed-extension-certificate.json").read_text())
        for field in ("kernel_basis", "determinant"):
            changed = copy.deepcopy(certificate)
            item = changed["integer-derived"]["new-C"]
            if field == "kernel_basis":
                item[field][0][0] = "0"
            else:
                item[field] = "999"
            with self.assertRaises(AssertionError):
                v.verify_certificate(changed)

    def test_masked_residual_can_hide_growing_full_error(self):
        residual, omitted, squared = v.mask_escape(100)
        self.assertEqual(residual, Fraction(1, 100))
        self.assertEqual(omitted, 100)
        self.assertGreater(squared, 10000)


if __name__ == "__main__":
    unittest.main()

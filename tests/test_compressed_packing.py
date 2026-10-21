"""Coefficient-level controls for the compressed packing identities."""

import importlib.util
from pathlib import Path
import unittest


PATH = Path(__file__).resolve().parents[1] / "research/ai/2026-10-21-compressed-packing/verify_compressed.py"
SPEC = importlib.util.spec_from_file_location("compressed_packing", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CompressedPackingTests(unittest.TestCase):
    def test_all_coefficients_and_alternate_limit(self):
        for m in range(2, 17, 2):
            with self.subTest(m=m):
                MODULE.check(m)

    def test_m4_has_the_stated_single_negative_term(self):
        tensor, _ = MODULE.transform(4)
        self.assertEqual(dict(MODULE.coefficient(tensor, -1)),
                         {(3, 0, 1, 0, 1): 1})

    def test_source_lengths_and_domain(self):
        for m in (0, 1, 3):
            with self.assertRaises(ValueError):
                MODULE.source_maps(m)
        y, z = MODULE.source_maps(10)
        self.assertEqual(len(y), 55)
        self.assertEqual(len(z), 55)
        self.assertEqual(max(z), 58)


if __name__ == "__main__":
    unittest.main()

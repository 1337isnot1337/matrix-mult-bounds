"""Exact support regression for the alternating-sector degeneration."""
from __future__ import annotations

from itertools import product
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'research' / 'ai' / '2026-10-23-alternating-sector-separation' / 'verify.py'
SPEC = importlib.util.spec_from_file_location('alternating_sector_verify', SCRIPT)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class AlternatingSectorTests(unittest.TestCase):
    def test_small_exhaustive_support_grid(self):
        for a in range(1, 5):
            for k in range(1, 6):
                for widths in product((1, 2), repeat=k):
                    VERIFY.verify_case(a, widths)

    def test_output_tail_and_sector_lengths(self):
        for a in range(1, 8):
            d = a - 1
            for k in range(1, 8):
                widths = tuple(range(1, k + 1))
                B, y_blocks, z_blocks = VERIFY.layout(a, widths)
                self.assertEqual(B, sum(widths) + (k // 2) * d)
                self.assertEqual(sum(hi - lo for lo, hi in y_blocks), B)
                self.assertEqual(
                    sum(hi - lo for lo, hi in z_blocks),
                    sum(widths) + ((k + 1) // 2) * d)
                self.assertEqual(
                    B + d - sum(hi - lo for lo, hi in z_blocks),
                    d if k % 2 == 0 else 0)
                VERIFY.verify_case(a, widths)


if __name__ == '__main__':
    unittest.main()

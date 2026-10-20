"""Finite exact source calculation and interval checks for the SL(2,7) lane."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('sl2_seven_source',
    ROOT/'research/ai/2026-10-20-sl2-seven/source_certificate.py')
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)


class SL2SevenTests(unittest.TestCase):
    def test_source_blocks_and_conditional_gate(self):
        report = source.derive()
        self.assertEqual(report['complex_degrees'], [1, 3, 3, 4, 4, 6, 6, 6, 7, 8, 8])
        self.assertEqual(sum(report['class_sizes']), 336)
        gate = source.exponent_gate(report['complex_degrees'])
        self.assertGreater(gate['strict_positive_margin_numerator'], 0)

    def test_integer_root_intervals(self):
        for n in range(1, 10):
            for a in (0, 1, 2, 15, 16, 17, 1000, 2**123+7):
                root = source.root_floor(a, n)
                self.assertLessEqual(root**n, a)
                self.assertGreater((root+1)**n, a)

    def test_bad_source_cost_rejected(self):
        with self.assertRaises(ArithmeticError):
            source.exponent_gate([20]*11)


if __name__ == '__main__':
    unittest.main()

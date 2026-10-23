import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'conic_d0_exact_curve_verifier',
    ROOT/'research/ai/2026-10-23-conic-d0-cubic/verify.py')
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class ConicD0ExactCurveTests(unittest.TestCase):
    def test_all_parameter_curve_replays_from_literal_source(self):
        record = json.loads(VERIFY.DEFAULT.read_text())
        report = VERIFY.verify(record)
        self.assertEqual(report['parameter_scope'], 'all complex a,b at c=0,d=0')
        self.assertEqual(report['kernel_coefficients_checked'], 78400)
        self.assertEqual(report['leading_minor_determinants'], ['1', '1', '-1'])
        self.assertTrue(report['all_order_source_curve'])
        self.assertFalse(report['exponent_improvement'])


if __name__ == '__main__':
    unittest.main()

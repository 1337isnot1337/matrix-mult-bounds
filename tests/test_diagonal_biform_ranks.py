"""Finite independently assembled acceptance for the diagonal rank claims."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'research/ai/2026-10-23-diagonal-biform-ranks/verify.py'

class DiagonalBiformTests(unittest.TestCase):
    def test_literal_matrix_blocks_and_quadratic_determinants(self):
        spec = importlib.util.spec_from_file_location('diagonal_biform_verify', SOURCE)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        report = module.verify()
        self.assertEqual(report['result'], 'pass')
        self.assertEqual(report['block_rank_cases'], 312)
        self.assertEqual(report['full_literal_matrix_cases'], 112)
        self.assertEqual(report['quadratic_closed_rank_cases'], 144)
        self.assertEqual(report['triangular_block_cases'], 5016)
        self.assertEqual(report['cyclotomic_recurrence_cases'], 290)

if __name__ == '__main__':
    unittest.main()

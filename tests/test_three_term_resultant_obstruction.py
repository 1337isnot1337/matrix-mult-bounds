"""Regression entrypoint for the exact three-term biform determinant."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'research/ai/2026-10-23-three-term-resultant-obstruction/verify.py'

class ThreeTermBiformObstructionTests(unittest.TestCase):
    def test_exact_certificate(self):
        spec = importlib.util.spec_from_file_location('three_term_biform', SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        report = module.verify()
        self.assertEqual(report['status'], 'pass')
        self.assertEqual(report['integer_grid_points'], 256)
        self.assertEqual(report['rank14_minor'], -4)

if __name__ == '__main__':
    unittest.main()

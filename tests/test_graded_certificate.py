"""Explicit exact controls for the graded degeneration certificate."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'graded_certificate', ROOT/'research/ai/2026-10-20-concavity-equivalence/graded_certificate.py')
certificate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(certificate)


class GradedCertificateTests(unittest.TestCase):
    def test_explicit_small_degenerations(self):
        for a in (2, 3):
            p, q = certificate.small_control(a)
            self.assertTrue(certificate.verify(a, p.rows, p, q)['exact'])

    def test_wrong_coefficient_is_rejected(self):
        p, q = certificate.small_control(3)
        p[0, 0] = 2
        report = certificate.verify(3, p.rows, p, q)
        self.assertFalse(report['exact'])
        self.assertTrue(report['constant_coefficient_failures'])

    def test_float_entries_are_rejected(self):
        p, q = certificate.small_control(2)
        p[0, 0] = 1.0
        with self.assertRaises(ValueError):
            certificate.verify(2, p.rows, p, q)


if __name__ == '__main__':
    unittest.main()

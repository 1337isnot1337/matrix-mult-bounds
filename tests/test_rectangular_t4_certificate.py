"""Exact acceptance and tampering controls for the finite T4 certificate."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-21-rectangular-t4-certificate/verify_certificate.py'
SPEC = importlib.util.spec_from_file_location('rectangular_t4_certificate', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
CERTIFICATE = ROOT / 'results/rectangular-t4-certificate-2026-10-21/certificate.json'


class RectangularT4CertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(CERTIFICATE.read_text())

    def test_exact_contraction_and_natural_grading(self):
        report = MODULE.verify(self.data)
        self.assertTrue(report['all_172_equations_have_a_common_exact_real_zero'])
        self.assertEqual(report['natural_grading_equations_also_certified'], 140)
        self.assertEqual(report['negative_weight_equations'], 48)
        self.assertEqual(report['zero_weight_equations'], 124)
        self.assertFalse(report['new_exponent_established'])

    def test_zero_approximate_inverse_is_rejected(self):
        altered = copy.deepcopy(self.data)
        altered['inverse_numerators'] = [[0]*172 for _ in range(172)]
        with self.assertRaisesRegex(AssertionError, 'not certified invertible'):
            MODULE.verify(altered)

    def test_large_radius_is_rejected(self):
        altered = copy.deepcopy(self.data)
        altered['radius_denominator'] = 1
        with self.assertRaisesRegex(AssertionError, 'not certified contractive'):
            MODULE.verify(altered)

    def test_independent_source_expansion_and_finite_difference_replay(self):
        path = PATH.with_name('independent_replay.py')
        spec = importlib.util.spec_from_file_location('t4_independent_replay', path)
        independent = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(independent)
        actual = independent.replay(CERTIFICATE)
        saved = json.loads((ROOT / 'results/rectangular-t4-certificate-2026-10-21/independent-verification.json').read_text())
        self.assertEqual(actual, saved)


if __name__ == '__main__':
    unittest.main()

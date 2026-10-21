import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin1_verify.py'
SPEC = importlib.util.spec_from_file_location('parity_balancing_spin1_verify', MODULE_PATH)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)
CERTIFICATE_PATH = ROOT / 'results/anisotropic-constructions-2026-10-20/parity_balancing_spin1/scalar_witness.json'


class SpinOneScalarConstructionTests(unittest.TestCase):
    def setUp(self):
        self.certificate = json.loads(CERTIFICATE_PATH.read_text())

    def test_complete_exact_identities(self):
        report = VERIFY.verify_certificate(self.certificate)
        self.assertTrue(report['extended_source_exact_M3_identity'])
        self.assertTrue(report['base_source_exact_M3_plus_trace_cube_identity'])
        self.assertEqual(report['target_coefficients_checked'], 729)
        self.assertEqual(report['nonzero_target_coefficients'], 27)

    def test_corrupted_coefficient_rejected(self):
        altered = copy.deepcopy(self.certificate)
        altered['map_numerators']['A'][0][0] += 1
        with self.assertRaises(ArithmeticError):
            VERIFY.verify_certificate(altered)

    def test_wrong_scalar_sign_rejected(self):
        altered = copy.deepcopy(self.certificate)
        for row in altered['map_numerators']['B']:
            row[12] *= -1
        with self.assertRaises(ArithmeticError):
            VERIFY.verify_certificate(altered)

    def test_omitted_scalar_source_declaration_rejected(self):
        altered = copy.deepcopy(self.certificate)
        altered['source'] = 'A(2,2)'
        with self.assertRaises(ValueError):
            VERIFY.verify_certificate(altered)


if __name__ == '__main__':
    unittest.main()

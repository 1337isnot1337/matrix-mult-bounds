import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_triangular_verify.py'
SPEC = importlib.util.spec_from_file_location('parity_balancing_triangular_verify', MODULE_PATH)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)
CERTIFICATE_PATH = ROOT / 'results/anisotropic-constructions-2026-10-20/parity_balancing_triangular.json'


class TriangularConstructionTests(unittest.TestCase):
    def setUp(self):
        self.certificate = json.loads(CERTIFICATE_PATH.read_text())

    def test_all_saved_quotient_and_residual_identities(self):
        report = VERIFY.verify_report(self.certificate)
        self.assertEqual([r['source_lengths'] for r in report['records']],
                         [[2, 2], [2, 3], [3, 3], [4, 4]])
        self.assertTrue(all(r['quotient_identity_exact'] and r['residual_identity_exact']
                            for r in report['records']))

    def test_modified_residual_rejected(self):
        altered = copy.deepcopy(self.certificate)
        altered['records'][2]['residual_matrices'][0]['numerators'][0][0] += 1
        with self.assertRaises(ArithmeticError):
            VERIFY.verify_report(altered)

    def test_discarding_residual_rejected(self):
        altered = copy.deepcopy(self.certificate)
        altered['residual_may_be_discarded'] = True
        with self.assertRaises(ValueError):
            VERIFY.verify_report(altered)


if __name__ == '__main__':
    unittest.main()

"""Exact block coordinates, transpose transport, and certificate corruption."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-conjugation-limit'
RESULTS = ROOT / 'results/conjugation-limit-2026-10-23'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load('conjugation_block_parent_test', PACKAGE / 'verify.py')
block = load('conjugation_block_reduction_test', PACKAGE / 'block_reduction.py')


class ConjugationBlockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent = json.loads((RESULTS / 'certificate.json').read_text())
        cls.parent_hash = hashlib.sha256((RESULTS / 'certificate.json').read_bytes()).hexdigest()
        cls.certificate = json.loads((RESULTS / 'block-certificate.json').read_text())

    def accept(self, certificate):
        return block.accept(certificate, self.parent, verify, self.parent_hash)

    def test_complete_exact_block_identities_and_saved_report(self):
        report = self.accept(self.certificate)
        self.assertEqual(report, json.loads((RESULTS / 'block-verification.json').read_text()))
        self.assertEqual(report['reduced_space_dimension'], 46)
        self.assertFalse(report['remaining_dimension_bound_proved'])
        self.assertFalse(report['arbitrary_constant_compressions_excluded'])

    def test_wrong_coordinate_omitted_row_and_parent_pin_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['coordinate_rows'][0]['coefficients'][0][1] += 1
        with self.assertRaises(ValueError):
            self.accept(bad)
        bad = copy.deepcopy(self.certificate)
        bad['coordinate_rows'].pop()
        with self.assertRaisesRegex(ValueError, 'row coverage'):
            self.accept(bad)
        bad = copy.deepcopy(self.certificate)
        bad['parent_certificate_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'parent pin'):
            self.accept(bad)

    def test_transpose_transport_detects_corrupted_outer_matrix(self):
        _, _, outer = block.build_blocks(verify)
        self.assertEqual(block.verify_transpose_identity(outer, verify)
                         ['outer_transpose_identities_checked'], 16)
        bad = copy.deepcopy(outer)
        bad[1][1] = bad[1].get(1, 0) + 1
        with self.assertRaisesRegex(ValueError, 'transpose-conjugation'):
            block.verify_transpose_identity(bad, verify)


if __name__ == '__main__':
    unittest.main()

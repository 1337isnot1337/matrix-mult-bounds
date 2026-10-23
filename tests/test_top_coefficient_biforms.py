"""Exact acceptance controls for AI-TOP-COEFFICIENT-BIFORM-RANK-001."""
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research' / 'ai' / '2026-10-23-top-coefficient-biforms'
RECEIPT = ROOT / 'results' / 'top-coefficient-biforms-2026-10-23' / 'verification.json'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class TopCoefficientBiformTests(unittest.TestCase):
    def test_modular_acceptance_and_frozen_receipt(self):
        verifier = load('top_coeff_verify', PACKAGE / 'verify.py')
        actual = verifier.run()
        frozen = json.loads(RECEIPT.read_text())
        self.assertEqual(actual, frozen)
        self.assertEqual(actual['total'], 3372)
        self.assertEqual(actual['result'], 'PASS')

    def test_exact_rational_backend(self):
        oracle = load('top_coeff_qq', PACKAGE / 'verify_charzero.py')
        actual = oracle.run()
        self.assertEqual(actual['result'], 'PASS')
        self.assertEqual(actual['charzero_QQ_cases'], 24)

    def test_off_by_one_mutation_control(self):
        verifier = load('top_coeff_mutation', PACKAGE / 'verify.py')
        # f=1+z+(1+x^2)z^2, a=3, b=7 over F_101.
        c = (1, 1)
        w = (1, 0, 1)
        actual = verifier.exact_rank_modp(
            verifier.coefficient_matrix(3, 7, 2, c, w, 101), 101)
        self.assertEqual(actual, 27)
        self.assertEqual(actual, verifier.predicted_rank(3, 7, 2, w, 101))
        self.assertNotEqual(actual, 26)


if __name__ == '__main__':
    unittest.main()

"""Exact complete source replay with the full credited first jet fixed."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-conic-fixed-first-curve'
RESULTS = ROOT / 'results/conic-fixed-first-curve-2026-10-23'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load('conic_fixed_first_acceptance', PACKAGE / 'verify.py')


class ConicFixedFirstCurveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness = json.loads((RESULTS / 'polynomial-curve.json').read_text())

    def test_complete_source_identity_and_fixed_first_coefficients(self):
        report = v.verify(self.witness)
        self.assertEqual(report, json.loads((RESULTS / 'verification.json').read_text()))
        self.assertEqual(report['complete_product_orders_checked'], list(range(7)))
        self.assertEqual(report['leading_minor_determinants'], ['1', '1', '-1'])
        self.assertTrue(report['full_first_jet_preserved'])
        self.assertTrue(report['all_order_lift_established'])

    def test_explicit_polynomial_formulas_regenerate_witness(self):
        construction = load('conic_fixed_first_construction', PACKAGE / 'construct.py')
        self.assertEqual(construction.construct(), self.witness)

    def test_boundary_first_velocity_is_fixed(self):
        bad = copy.deepcopy(self.witness)
        entry = next(e for e in bad['B'][1]['entries'] if e[:2] == [0, 1])
        entry[2] = f'({entry[2]})+1'
        with self.assertRaisesRegex(ValueError, 'credited full coefficient B1'):
            v.verify(bad)

    def test_higher_coefficient_corruption_rejected(self):
        bad = copy.deepcopy(self.witness)
        entry = bad['C'][3]['entries'][0]
        entry[2] = f'({entry[2]})+1'
        with self.assertRaisesRegex(ValueError, 'kernel coefficient at order 4'):
            v.verify(bad)

    def test_complete_degree_and_parameter_denominator_controls(self):
        bad = copy.deepcopy(self.witness)
        bad['B'].pop()
        with self.assertRaisesRegex(ValueError, 'complete polynomial degrees'):
            v.verify(bad)
        bad = copy.deepcopy(self.witness)
        bad['B'][3]['entries'][0][2] = '1/d'
        with self.assertRaisesRegex(ValueError, 'polynomial arithmetic'):
            v.verify(bad)

    def test_exact_credited_source_pins(self):
        record = json.loads((PACKAGE / 'sources.json').read_text())
        for source in record['local']:
            for path, digest in source['sha256'].items():
                self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), digest)


if __name__ == '__main__':
    unittest.main()

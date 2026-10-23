"""Complete polynomial source replay and controls for the all-order conic curve."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-conic-polynomial-curve'
RESULTS = ROOT / 'results/conic-polynomial-curve-2026-10-23'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load('conic_polynomial_acceptance', PACKAGE / 'verify.py')


class ConicPolynomialCurveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness = json.loads((RESULTS / 'polynomial-curve.json').read_text())

    def test_complete_source_product_and_unit_minors(self):
        report = v.verify(self.witness)
        self.assertEqual(report, json.loads((RESULTS / 'verification.json').read_text()))
        self.assertEqual(report['complete_product_orders_checked'], [0, 1, 2, 3, 4])
        self.assertEqual(report['leading_minor_determinants'], ['1', '1', '-1'])
        self.assertEqual(report['normal_class'], '[1:d]')
        self.assertTrue(report['all_order_lift_established'])
        self.assertFalse(report['full_first_jet_preserved'])

    def test_explicit_formula_regenerates_exported_coefficients(self):
        construction = load('conic_polynomial_construction', PACKAGE / 'construct.py')
        self.assertEqual(construction.construct(), self.witness)

    def test_highest_product_coefficient_is_essential(self):
        bad = copy.deepcopy(self.witness)
        entry = bad['C'][3]['entries'][0]
        entry[2] = f'({entry[2]})+1'
        # This edit survives every kernel equation through t^3. Checking the
        # complete t^4 coefficient distinguishes a curve from a three-jet.
        with self.assertRaisesRegex(ValueError, 'kernel coefficient at order 4'):
            v.verify(bad)

    def test_changed_boundary_velocity_is_rejected_by_source(self):
        bad = copy.deepcopy(self.witness)
        entry = bad['B'][1]['entries'][0]
        entry[2] = f'({entry[2]})+1'
        with self.assertRaisesRegex(ValueError, 'kernel coefficient at order 2'):
            v.verify(bad)

    def test_credited_constant_and_normal_coefficients_are_enforced(self):
        bad = copy.deepcopy(self.witness)
        bad['B'][0]['entries'][0][2] = '2'
        with self.assertRaisesRegex(ValueError, 'credited constant'):
            v.verify(bad)
        bad = copy.deepcopy(self.witness)
        entry = next(e for e in bad['C'][1]['entries'] if e[:2] == [0, 102])
        entry[2] = '-2'
        with self.assertRaisesRegex(ValueError, 'credited first normal'):
            v.verify(bad)

    def test_polynomial_ring_and_complete_degree_controls(self):
        for text in ('1/d', '1/(a+1)', 'd**-1', 'd**(1/2)',
                     "__import__('os')", '1/0', '1.0'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                v.expression(text)
        self.assertEqual(v.expression('(a+b*d)/3').as_expr(), (v.A+v.B*v.D)/3)
        bad = copy.deepcopy(self.witness)
        bad['C'].pop()
        with self.assertRaisesRegex(ValueError, 'complete polynomial degrees'):
            v.verify(bad)

    def test_credited_source_identity_and_byte_pins(self):
        source = load('conic_polynomial_credited_source', ROOT /
            'research/ai/2026-10-21-quantum-extension-spaces/extensions.py')
        self.assertEqual(set(v.source_terms()), set(source.TERMS))
        self.assertEqual(len(v.source_terms()), 4096)
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for record in sources['local']:
            for path, digest in record.get('sha256', {}).items():
                self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), digest)


if __name__ == '__main__':
    unittest.main()

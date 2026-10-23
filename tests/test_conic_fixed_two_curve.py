"""One complete replay, with inexpensive preflight and selected-order controls."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-conic-fixed-two-curve'
RESULTS = ROOT / 'results/conic-fixed-two-curve-2026-10-23'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load('conic_fixed_two_acceptance', PACKAGE / 'verify.py')


class ConicFixedTwoCurveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness = json.loads((RESULTS / 'polynomial-curve.json').read_text())
        started = time.monotonic()
        cls.report = v.verify(cls.witness)
        cls.acceptance_seconds = time.monotonic()-started

    def test_complete_product_two_jet_and_unit_minors(self):
        self.assertEqual(self.report, json.loads((RESULTS / 'verification.json').read_text()))
        self.assertEqual(self.report['complete_product_orders_checked'], list(range(18)))
        self.assertEqual(self.report['map_parameter_pole_orders'], [5, 6])
        self.assertEqual(self.report['leading_minor_determinants'], ['1', '1', '-1'])
        self.assertEqual(self.report['prescribed_map_orders_preserved'], [0, 1, 2])
        self.assertEqual(self.report['prescribed_kernel_corrections_preserved'], ['Y1=0', 'Y2=0'])

    def test_explicit_projection_formula_regenerates_all_coefficients(self):
        construction = load('conic_fixed_two_construction', PACKAGE / 'construct.py')
        self.assertEqual(construction.construct(), self.witness)

    def test_changed_second_coefficient_and_kernel_parametrization_rejected(self):
        bad = copy.deepcopy(self.witness)
        entry = bad['B'][2]['entries'][0]
        entry[2] = f'({entry[2]})+1'
        with self.assertRaisesRegex(ValueError, 'prescribed full coefficient B2'):
            v.prepare(bad)
        bad = copy.deepcopy(self.witness)
        bad['source_row_corrections_through_two'][1]['entries'] = [[0, 0, '1']]
        with self.assertRaisesRegex(ValueError, 'kernel parametrization'):
            v.prepare(bad)

    def test_changed_last_coefficient_has_a_late_source_residual(self):
        bad = copy.deepcopy(self.witness)
        entry = bad['C'][9]['entries'][0]
        entry[2] = f'({entry[2]})+1'
        bs, cs = v.prepare(bad)
        terms = [z for z in v.source_terms() if z[0] in v.OUTSIDE]
        # The changed boundary entry first meets a nonboundary B coefficient
        # at t^10. These selected-order controls avoid another full replay.
        self.assertFalse(v.coefficient(bs, cs, 9, terms))
        self.assertTrue(v.coefficient(bs, cs, 10, terms))

    def test_laurent_parser_degree_and_chart_controls(self):
        self.assertEqual(v.expression('(a+b*d)/d**2', 2), v.A+v.B*v.D)
        self.assertEqual(v.expression('d**-6', 6), v.R.one)
        for text in ('1/a', '1/(d+1)', 'd**-7', 'd**(1/2)',
                     "__import__('os')", '1.0', '1/0'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                v.expression(text, 6)
        bad = copy.deepcopy(self.witness)
        bad['chart'] = 'all d'
        with self.assertRaisesRegex(ValueError, 'd chart'):
            v.prepare(bad)
        bad = copy.deepcopy(self.witness)
        bad['C'].pop()
        with self.assertRaisesRegex(ValueError, 'complete polynomial degrees'):
            v.prepare(bad)

    def test_literal_source_and_exact_byte_pins(self):
        source = load('conic_fixed_two_original_source', ROOT /
            'research/ai/2026-10-21-quantum-extension-spaces/extensions.py')
        self.assertEqual(set(v.source_terms()), set(source.TERMS))
        self.assertEqual(len(v.source_terms()), 4096)
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for source in sources['local']:
            for path, digest in source['sha256'].items():
                self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), digest)


if __name__ == '__main__':
    unittest.main()

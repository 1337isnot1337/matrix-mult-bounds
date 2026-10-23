"""Literal-source acceptance and corruption controls for higher conic jets."""
import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-conic-higher-jets'
RESULTS = ROOT/'results/conic-higher-jets-2026-10-23'


def load(name):
    spec = importlib.util.spec_from_file_location('conic_higher_'+name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ConicHigherJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rational = json.loads((RESULTS/'rational-ten-jet.json').read_text())
        cls.symbolic = json.loads((RESULTS/'mixed-fourth-family.json').read_text())
        cls.r = load('verify')
        cls.s = load('verify_symbolic')

    def test_rational_ten_jet_replays_all_coefficients(self):
        report = self.r.verify(self.rational)
        self.assertEqual(report, json.loads((RESULTS/'rational-verification.json').read_text()))
        self.assertEqual(report['jet_order'], 10)
        self.assertEqual(report['first_nonboundary_entries'], 128)

    def test_symbolic_four_jet_replays_every_parameter(self):
        report = self.s.verify(self.symbolic)
        self.assertEqual(report, json.loads((RESULTS/'mixed-verification.json').read_text()))
        self.assertEqual(report['leading_minor_determinants'], ['1', '1', '-1'])
        self.assertEqual(report['maximum_d_pole_order'], 3)

    def test_source_is_the_maintained_literal_source(self):
        path = ROOT/'research/ai/2026-10-21-quantum-extension-spaces/extensions.py'
        spec = importlib.util.spec_from_file_location('higher_jet_source_control', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(len(self.r.source_terms()), 4096)
        self.assertEqual(set(self.r.source_terms()), set(module.TERMS))

    def test_last_map_and_last_kernel_corruptions_are_rejected(self):
        for key in ('B', 'source_row_corrections'):
            bad = copy.deepcopy(self.rational)
            entry = bad['witness'][key][-1]['entries'][0]
            entry[2] = str(Fraction(entry[2])+1)
            with self.assertRaisesRegex(ValueError, 'order 10'):
                self.r.verify(bad)

    def test_changed_credited_coefficients_and_point_are_rejected(self):
        bad = copy.deepcopy(self.rational)
        bad['witness']['B'][2]['entries'][0][2] = '99'
        with self.assertRaisesRegex(ValueError, 'credited coefficient'):
            self.r.verify(bad)
        bad = copy.deepcopy(self.rational)
        bad['parameters']['d'] = '2'
        with self.assertRaisesRegex(ValueError, 'rational point'):
            self.r.verify(bad)

    def test_symbolic_chart_and_third_formula_are_enforced(self):
        for text in ('1/(a+1)', '1/d**4', '__import__("os")'):
            with self.assertRaises(ValueError):
                self.s.expression(text)
        bad = copy.deepcopy(self.symbolic)
        bad['witness']['B'][3]['entries'][0][2] = '99'
        with self.assertRaisesRegex(ValueError, 'five-field third correction'):
            self.s.verify(bad)

    def test_symbolic_last_map_corruption_is_rejected(self):
        bad = copy.deepcopy(self.symbolic)
        entry = bad['witness']['B'][4]['entries'][0]
        entry[2] = '('+entry[2]+')+1'
        with self.assertRaisesRegex(ValueError, 'order 4'):
            self.s.verify(bad)


if __name__ == '__main__':
    unittest.main()

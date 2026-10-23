"""All projective strata, literal all-order curves, and meaningful corruptions."""
import copy
import importlib.util
import json
from pathlib import Path
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-conic-projective-criterion'
RESULTS = ROOT/'results/conic-projective-criterion-2026-10-23'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load('conic_projective_acceptance', PACKAGE/'verify.py')


class ConicProjectiveCriterionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curves = v.read('curves')
        cls.certificates = v.read('certificates')
        started = time.monotonic()
        # One complete source/operator replay is shared by all focused controls.
        cls.report = v.verify(cls.curves, cls.certificates)
        cls.acceptance_seconds = time.monotonic()-started

    def test_complete_projective_tangent_and_curvature_cover(self):
        self.assertEqual(self.report, json.loads((RESULTS/'verification.json').read_text()))
        self.assertEqual([row['stratum'] for row in self.report['missing_strata']],
                         ['a_infinity', 'b_infinity', 'both_infinity'])
        for row in self.report['missing_strata']:
            self.assertEqual(row['tangent_dimensions'], [64, 3, 3])
            self.assertEqual(row['mixed_unit_pivots'], 49)
        self.assertTrue(self.report['all_projective_base_points'])
        self.assertFalse(self.report['prescribed_full_first_jet_claimed'])

    def test_exact_curves_cover_the_cubic_and_both_linear_factors(self):
        self.assertEqual(len(self.report['curves']), 8)
        self.assertEqual(sum(len(row['checked_product_orders']) for row in self.report['curves']), 29)
        self.assertEqual(len(self.report['exact_linear_components']), 7)
        for row in self.report['curves']:
            self.assertEqual(row['leading_minor_determinants'], ['1', '1', '-1'])
            self.assertTrue(row['fixed_kernel'])
        construction = load('conic_projective_construction', PACKAGE/'construct.py')
        self.assertEqual(construction.construct(), self.curves)

    def test_literal_reversal_transports_normals_without_a_rank_guard(self):
        reversal = self.report['reversal']
        self.assertEqual(reversal['source_terms_permuted'], 4096)
        self.assertEqual(reversal['projective_normal_transition'], '[lambda:mu] -> [mu:lambda]')
        for row in reversal['strata']:
            self.assertEqual(row['row_change_determinants'], ['1', '1'])
        # The conic-infinity discriminant has precisely the stated strata.
        for stratum in v.m.STRATA:
            data = v.m.base(stratum, 'infinity')
            self.assertEqual(data['delta'], -1 if stratum == 'finite' else 0)

    def test_late_changes_distinguish_boundary_motion_from_source_residual(self):
        allowed = copy.deepcopy(self.curves['families'][3])
        entry = allowed['C'][2]['entries'][0]
        entry[2] = '('+entry[2]+')+1'
        self.assertTrue(v.check_curve(allowed)['fixed_kernel'])
        curve = copy.deepcopy(self.curves['families'][3])
        entry = next(row for row in curve['C'][2]['entries'] if row[1]//7 % 4 == 1)
        entry[2] = '('+entry[2]+')+1'
        with self.assertRaisesRegex(ValueError, 'source product has a kernel residual'):
            v.check_curve(curve)

    def test_changed_normal_and_incomplete_degree_data_are_rejected(self):
        curve = copy.deepcopy(self.curves['families'][0])
        entry = next(row for row in curve['B'][1]['entries'] if row[1]//28 == 2)
        entry[2] = '('+entry[2]+')+1'
        with self.assertRaisesRegex(ValueError, 'required normal class'):
            v.check_curve(curve)
        curve = copy.deepcopy(self.curves['families'][0])
        curve['C'].append({'shape': [14, 112], 'entries': []})
        with self.assertRaisesRegex(ValueError, 'polynomial degree bounds'):
            v.check_curve(curve)

    def test_missing_stratum_and_wrong_residual_generator_are_rejected(self):
        certificates = copy.deepcopy(self.certificates)
        certificates['strata'].pop()
        with self.assertRaisesRegex(ValueError, 'Complete curvature stratum cover'):
            v.certificate_headers(certificates)
        certificates = copy.deepcopy(self.certificates)
        certificates['strata'][2]['compatibility']['residual_generator'] = '1'
        with self.assertRaisesRegex(ValueError, 'curvature residual generator'):
            v.certificate_headers(certificates)

    def test_source_pins_and_polynomial_only_parser(self):
        self.assertEqual(v.source_pins(), 11)
        previous = v.m.load('research/ai/2026-10-21-quantum-extension-spaces/extensions.py',
                            'projective_test_literal_source')
        self.assertEqual(set(v.source_terms()), set(previous.TERMS))
        self.assertEqual(len(v.source_terms()), 4096)
        self.assertEqual(v.expression('(a+b*d)/3'), (v.a+v.b*v.d)/3)
        for text in ('1/a', '1/d', 'd**-1', 'd**21', 'd**(1/2)',
                     "__import__('os')", '1.0', '1/0'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                v.expression(text)


if __name__ == '__main__':
    unittest.main()

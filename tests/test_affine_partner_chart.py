"""Boundary source closure and certificate corruption controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('affine_partner_chart_test', ROOT / 'research/ai/2026-10-21-affine-partner-chart/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class AffinePartnerChartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = verify.report()

    def test_report_and_scope(self):
        expected = json.loads((ROOT / 'results/affine-partner-chart-2026-10-21/report.json').read_text())
        self.assertEqual(self.report, expected)
        self.assertEqual(self.report['boundary_point']['final_nonplane_dimension'], 0)
        self.assertTrue(self.report['all_finite_a_b_excluded_under_adopted_claims'])
        self.assertFalse(self.report['b_nonzero_verifier_replayed_here'])
        self.assertFalse(self.report['projective_endpoints_classified'])
        self.assertFalse(self.report['improves_omega'])

    def test_missing_terminal_family_is_rejected(self):
        bad = copy.deepcopy(verify.certificate())
        bad['terminal_source_cases'].pop()
        with self.assertRaises(ArithmeticError):
            verify.BoundaryProof(verify.common, bad).report()

    def test_false_cubic_span_is_rejected(self):
        proof = verify.proof
        with self.assertRaises(ArithmeticError):
            proof.span(verify.sp.Matrix([[1, 0]]), verify.sp.Matrix([[0, 1]]))

    def test_wrong_source_identity_is_rejected(self):
        proof = verify.proof
        records = copy.deepcopy(proof.cert['initial_source_cases'][0]['records'])
        next(r for r in records if r['kind'] == 'low_sources')['sources'][0]['source_index'] += 1
        with self.assertRaises(ArithmeticError):
            proof.replay(proof.data()['families'][0], set(), records)

    def test_wrong_torus_column_weight_is_rejected(self):
        weights = list(verify.generic.certificate()['torus_boundary_weights'])
        weights[0] += 1
        with self.assertRaises(ArithmeticError):
            verify.torus_report(weights)


if __name__ == '__main__':
    unittest.main()

"""Open-set certificate, symbolic block structure and modular lifting gates."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('generic_graph_verifier', ROOT / 'research/ai/2026-10-21-generic-mixed-graphs/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class GenericMixedGraphTests(unittest.TestCase):
    def test_complete_source_and_open_set_certificate(self):
        saved = ROOT / 'results/generic-mixed-graphs-2026-10-21/report.json'
        self.assertEqual(verify.report(), json.loads(saved.read_text()))
        self.assertEqual([s['quartic_rank_mod_prime'] for s in verify.report()['spans']], [2380, 2380])
        self.assertTrue(verify.report()['nonempty_open_set_proved'])
        self.assertFalse(verify.report()['all_graphs_classified'])

    def test_hidden_parameter_cross_term_is_rejected(self):
        data, cert = verify.source_data(), verify.certificate()
        changed = data['base'].copy()
        row = next(i for i, group in enumerate(cert['source_row_groups']) if group == 0)
        column = cert['normal_components'][1][0]
        # This change is invisible at the rational witness a=1.
        changed[row, column] += verify.A-1
        with self.assertRaisesRegex(ArithmeticError, 'cross-block source coefficient'):
            verify.check_source_blocks(changed, cert['normal_components'], cert['source_row_groups'])

    def test_missing_sparse_cube_witness_is_rejected(self):
        case = copy.deepcopy(verify.certificate()['span_cases'][0])
        case['witnesses'].pop()
        with self.assertRaisesRegex(ArithmeticError, 'Degree-four span is incomplete'):
            verify.macaulay.span_report(verify.point_data()['parts'], case, verify.certificate()['prime'])

    def test_nonunit_rational_denominator_is_rejected(self):
        prime = verify.certificate()['prime']
        with self.assertRaisesRegex(ArithmeticError, 'not a modular unit'):
            verify.macaulay.field_value(verify.sp.Rational(1, prime), prime)

    def test_changed_graph_torus_weight_is_rejected(self):
        changed = list(verify.certificate()['torus_boundary_weights'])
        changed[0] += 1
        with self.assertRaisesRegex(ArithmeticError, 'torus covariance'):
            verify.check_torus(changed)


if __name__ == '__main__':
    unittest.main()

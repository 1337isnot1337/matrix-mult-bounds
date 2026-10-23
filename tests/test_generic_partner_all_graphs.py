"""Generic rank guards must certify the claimed nonempty parameter set."""
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('generic_partner_test', ROOT / 'research/ai/2026-10-21-generic-partner-all-graphs/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class GenericPartnerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = verify.report()
        record = verify.certificate()['initial_source_cases'][0]
        parameters, selected, _ = verify.replay(verify.data()['families'][0], set(), record['records'], 'test/stable')
        basis, _, _ = verify.source_rows(parameters, selected, 'test/cubic_source')
        record = next(r for r in verify.certificate()['linear_cube_cases'] if r['case'] == 'stable' and r['group'] == 0)
        columns, rows = verify.previous.partition(parameters, basis, record)
        cls.minors = verify.previous.cubic_coefficients(basis, columns, rows, record['witnesses'])
        cls.forms = verify.decode(record['forms'])

    def test_report_and_all_graph_quantifier(self):
        expected = json.loads((ROOT / 'results/generic-partner-all-graphs-2026-10-21/report.json').read_text())
        self.assertEqual(self.report, expected)
        self.assertEqual(len(self.report['rank_guards']), 79)
        self.assertTrue(all(r['generic_rank'] == r['reference_rank'] for r in self.report['rank_guards']))
        self.assertTrue(self.report['all_graphs_for_every_good_partner'])
        self.assertTrue(self.report['partner_complement_finite'])
        self.assertFalse(self.report['exceptional_partners_classified'])
        self.assertFalse(self.report['improves_omega'])

    def test_reference_pole_is_rejected(self):
        # Scaling a valid constraint preserves a generic implication but loses the stated witness.
        with self.assertRaises(ArithmeticError):
            verify.reference(self.forms/(verify.A-2))

    def test_rank_loss_hidden_by_field_row_reduction_is_rejected(self):
        # Its generic rowspace is unchanged, while every minor vanishes at a=2.
        with self.assertRaises(ArithmeticError):
            verify.row_basis((verify.A-2)*self.minors, 'test/lost_reference_rank')

    def test_false_cubic_span_is_rejected(self):
        _, pivots = self.minors.to_DM().rref()
        missing = next(j for j in range(self.minors.cols) if j not in pivots)
        target = sp.SparseMatrix(1, self.minors.cols, {(0, missing): 1})
        with self.assertRaises(ArithmeticError):
            verify.span(self.minors, target, 'test/false_cubic')


if __name__ == '__main__':
    unittest.main()

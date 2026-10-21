"""All-graph source-stage replay with damaged certificate controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('all_graphs_test', ROOT / 'research/ai/2026-10-21-all-mixed-graphs-a1/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class AllMixedGraphsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = verify.report()
        first = verify.certificate()['initial_source_cases'][0]
        cls.parameters, cls.selected, _ = verify.replay(verify.data()['families'][0], set(), first['records'])
        cls.cubes = [r for r in verify.certificate()['linear_cube_cases'] if r['case'] == 'stable']

    def test_report_and_complete_scope(self):
        expected = json.loads((ROOT / 'results/all-mixed-graphs-a1-2026-10-21/report.json').read_text())
        self.assertEqual(self.report, expected)
        self.assertTrue(self.report['all_six_graph_parameters_covered'])
        self.assertTrue(self.report['extends_to_a_equals_b_nonzero'])
        self.assertEqual(self.report['final_nonplane_dimension'], 0)
        self.assertEqual([r['dimensions'] for r in self.report['stable_terminal_traces']], [[4, 0], [3, 2, 0], [3, 2, 0], [2, 0]])
        self.assertFalse(self.report['all_partners_classified'])
        self.assertFalse(self.report['improves_omega'])

    def test_corrupt_source_identity_is_rejected(self):
        records = copy.deepcopy(verify.certificate()['initial_source_cases'][0]['records'])
        record = next(r for r in records if r['kind'] == 'low_sources')
        record['sources'][0]['source_index'] += 1
        with self.assertRaises(ArithmeticError):
            verify.replay(verify.data()['families'][0], set(), records)

    def test_corrupt_cube_span_is_rejected(self):
        records = copy.deepcopy(self.cubes)
        entry = records[0]['cube_coefficients']['entries'][0]
        entry[2] = str(sp.Rational(entry[2])+1)
        with self.assertRaises(ArithmeticError):
            verify.linear_cubes(self.parameters, self.selected, records)

    def test_corrupt_branch_product_is_rejected(self):
        parameters = verify.linear_cubes(self.parameters, self.selected, self.cubes)
        basis, _, _ = verify.source_rows(parameters, self.selected)
        record = verify.certificate()['stable_branch_certificates'][0]
        columns, rows = verify.partition(parameters, basis, record)
        minors = verify.cubic_coefficients(basis, columns, rows, record['witnesses'])
        coefficients = verify.decode(record['coefficients']).copy()
        coefficients[0, 0] += 1
        u, v, w = sp.symbols('u v w')
        targets = verify.polynomial_rows([(v-w)**2*(v+w), (v-w)**2*(u-w)], (u, v, w))
        with self.assertRaises(ArithmeticError):
            verify.check_span(coefficients, minors, targets)


if __name__ == '__main__':
    unittest.main()

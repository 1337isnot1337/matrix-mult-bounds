"""All-graph polynomial identities and damaged-certificate rejection."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('global_dichotomy_test', ROOT / 'research/ai/2026-10-21-global-mixed-normal-dichotomy/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class GlobalDichotomyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = verify.report()
        cls.reduced = verify.rank_one_data()
        original = verify.data()
        embedding = original['quotient']*cls.reduced['parameters']
        base = original['base']
        mixed = base[1872:, :]*embedding+sum((h*base[312*j:312*(j+1), :]*embedding
            for j, h in enumerate(verify.H)), sp.zeros(312, 40))
        cls.record = verify.certificate()['mixed_projection_identities'][0]
        columns = cls.record['normal_columns']
        cls.matrix = mixed[cls.record['source_rows'], columns]
        cls.target, _ = verify.point.row_basis(cls.reduced['projection'][:, columns])

    def test_report_and_precise_scope(self):
        expected = json.loads((ROOT / 'results/global-mixed-normal-dichotomy-2026-10-21/report.json').read_text())
        self.assertEqual(self.report, expected)
        self.assertTrue(self.report['all_six_graph_parameters_covered'])
        self.assertEqual(self.report['remaining_linear_families'], [54, 36])
        self.assertFalse(self.report['target_excluded'])
        self.assertFalse(self.report['improves_omega'])

    def test_square_identity_corruption_is_rejected(self):
        coefficients = self.reduced['square_coefficients'].copy()
        coefficients[0, 0] += 1
        with self.assertRaises(ArithmeticError):
            verify.check_square_identities(self.reduced['quadratic_coefficients'], self.reduced['forms'], coefficients)

    def test_invalid_minor_position_is_rejected(self):
        with self.assertRaises(ArithmeticError):
            verify.quadratic_coefficients(sp.zeros(138, 12), 46, [[0, 0, 0, 1]])

    def test_source_polynomial_identity_corruption_is_rejected(self):
        bad = copy.deepcopy(self.record)
        bad['row_identity']['entries'][0][2] = str(sp.sympify(bad['row_identity']['entries'][0][2], locals=verify.LOCALS)+1)
        with self.assertRaises(ArithmeticError):
            verify.check_mixed_identity(self.matrix, self.target, bad)


if __name__ == '__main__':
    unittest.main()

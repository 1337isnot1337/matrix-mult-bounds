"""Exact exceptional fibers, polynomial identities and target-stage replay."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('exceptional_affine_test', ROOT / 'research/ai/2026-10-21-mixed-exceptional-affine/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class ExceptionalAffineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = verify.report()
        cls.data = verify.point_data()
        cls.record = verify.certificate()['left_certificates'][0]
        cert = verify.generic.certificate()
        columns = cert['normal_components'][0]
        base = verify.source_data()['base']
        rows = cls.record['selected_rows']
        parts = [base[[312*c+i for i in rows], columns] for c in range(7)]
        cls.matrix = parts[6]+sum((h*part for h, part in zip(verify.GRAPH, parts[:6])), sp.zeros(28, 44))

    def test_complete_report_and_exact_scope(self):
        expected = json.loads((ROOT / 'results/mixed-exceptional-affine-2026-10-21/report.json').read_text())
        self.assertEqual(self.report, expected)
        self.assertEqual(self.report['generic_normal_dimension'], 38)
        self.assertTrue(self.report['base_target_excluded'])
        self.assertFalse(self.report['whole_affine_family_target_excluded'])
        self.assertFalse(self.report['improves_omega'])

    def test_complete_base_kernel_and_both_terminal_families(self):
        self.assertEqual(self.report['square_dimensions'], [34, 26, 20, 18, 14])
        self.assertEqual(self.report['terminal_dimensions'], [[6, 0], [14, 10, 4, 2, 0]])
        self.assertEqual(self.report['base_joint_rows'], 44)

    def test_corrupt_polynomial_relation_is_rejected(self):
        bad = copy.deepcopy(self.record)
        bad['left']['entries'][0][2] = str(sp.sympify(bad['left']['entries'][0][2], locals=verify.LOCALS)+1)
        with self.assertRaises(ArithmeticError):
            verify.check_left(self.matrix, bad)

    def test_corrupt_independence_minor_is_rejected(self):
        bad = copy.deepcopy(self.record)
        bad['point_columns'] = [0, 0, 0]
        with self.assertRaises(ArithmeticError):
            verify.check_left(self.matrix, bad)

    def test_incomplete_terminal_certificate_is_rejected(self):
        records = verify.certificate()['terminal_cases'][1]['result']
        with self.assertRaises(ArithmeticError):
            verify.replay_case(self.data, self.data['families'][1], records[:-1])


if __name__ == '__main__':
    unittest.main()

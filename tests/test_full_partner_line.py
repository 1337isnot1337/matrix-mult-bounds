"""Explicit exceptional-fiber cover and source-level phase controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('full_partner_line_test', ROOT / 'research/ai/2026-10-21-full-partner-line/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class FullPartnerLineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = verify.report()

    def test_complete_report_and_boundary_scope(self):
        expected = json.loads((ROOT / 'results/full-partner-line-2026-10-21/report.json').read_text())
        self.assertEqual(self.report, expected)
        self.assertEqual(self.report['rank_minors_verified'], 79)
        self.assertTrue(self.report['all_complex_a_at_b_one_excluded'])
        self.assertTrue(self.report['extends_to_all_b_nonzero'])
        self.assertEqual(self.report['phase']['source_terms_checked'], 4096)
        self.assertEqual(self.report['a_zero']['final_nonplane_dimension'], 0)
        self.assertFalse(self.report['b_zero_boundary_classified'])
        self.assertFalse(self.report['improves_omega'])

    def test_wrong_physical_phase_is_rejected(self):
        bad = copy.deepcopy(verify.certificate('phase-certificate.json'))
        bad['leg_coordinate_weights'][1][1] = 1
        with self.assertRaises(ArithmeticError):
            verify.phase_report(bad)

    def test_omitted_rank_guard_is_rejected(self):
        records = verify.certificate('rank-minor-cover.json')['minors']
        with self.assertRaises(ArithmeticError):
            verify.check_cover_labels(verify.common.report()['rank_guards'], records[:-1])

    def test_corrupted_actual_minor_determinant_is_rejected(self):
        common = verify.common
        matrix = common.point.joint(common.multiply(common.data()['obstruction'], common.data()['families'][0]), 56)
        record = copy.deepcopy(verify.certificate('rank-minor-cover.json')['minors'][0])
        record['determinant'] = '2*('+record['determinant']+')'
        with self.assertRaises(ArithmeticError):
            verify.check_minor(matrix, record)

    def test_zero_partner_source_corruption_is_rejected(self):
        zero = verify.zero_proof
        records = copy.deepcopy(zero.cert['initial_source_cases'][0]['records'])
        record = next(r for r in records if r['kind'] == 'low_sources')
        record['sources'][0]['source_index'] += 1
        with self.assertRaises(ArithmeticError):
            zero.replay(zero.data()['families'][0], set(), records)


if __name__ == '__main__':
    unittest.main()

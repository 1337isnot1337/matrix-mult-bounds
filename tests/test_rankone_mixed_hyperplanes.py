"""Polynomial hyperplane certificates with boundary and smaller-space controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('mixed_hyperplane_verifier', ROOT / 'research/ai/2026-10-21-rankone-mixed-hyperplanes/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class RankOneMixedHyperplaneTests(unittest.TestCase):
    def test_complete_chart_endpoint_and_saved_certificate(self):
        saved = ROOT / 'results/rankone-mixed-hyperplanes-2026-10-21/report.json'
        self.assertEqual(verify.report(), json.loads(saved.read_text()))

    def test_nonzero_rank_one_obstructions_are_retained(self):
        for key in ('chart', 'endpoint'):
            case = verify.data()[key]
            self.assertEqual(case['report']['remaining_obstruction_columns'], [6])
            self.assertEqual(case['report']['boundary_only_normal_dimension'], 16)
            self.assertTrue(case['report']['rank_one_boundary_control']['matrix']['entries'])

    def test_unconditioned_boundary_hyperplanes_retain_more_freedom(self):
        for key in ('unconditioned_chart', 'unconditioned_endpoint'):
            record = verify.data()[key]['report']
            self.assertEqual(record['remaining_obstruction_columns'], [6])
            self.assertEqual(record['boundary_only_normal_dimension'], 106)
            self.assertEqual(record['complete_seven_frame_normal_dimension'], 88)
            self.assertTrue(record['rank_one_boundary_control']['matrix']['entries'])

    def test_mixed_five_space_has_extra_normal_freedom(self):
        self.assertEqual(verify.report()['seven_by_five_control']['normal_dimension'], 12)

    def test_changed_nonzero_minor_scale_is_rejected(self):
        case = verify.data()['chart']
        record = copy.deepcopy(case['report']['rounds'][0]['minors'][0])
        record['diagonal_scales'][0] = str(2*verify.sp.Rational(record['diagonal_scales'][0]))
        with self.assertRaisesRegex(ArithmeticError, 'Incorrect repeated diagonal form'):
            verify.check_minor(case['round_matrices'][0], record)


if __name__ == '__main__':
    unittest.main()

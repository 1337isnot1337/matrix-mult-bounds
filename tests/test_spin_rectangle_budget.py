import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/spin_rectangle_budget.py'
SPEC = importlib.util.spec_from_file_location('spin_rectangle_budget_controls', SCRIPT)
CORE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)


class SpinRectangleBudgetTests(unittest.TestCase):
    def test_saved_maps_all_coefficients_and_three_leg_ranks(self):
        report = CORE.verify(exported=json.loads(CORE.FULL_MAPS.read_text()))
        self.assertEqual([row['response_rank'] for row in report['three_leg_budgets']], [192, 236, 216])
        self.assertEqual([row['preimage_dimension'] for row in report['three_leg_budgets']], [777, 808, 828])
        self.assertEqual([row['remaining_excess_rank_budget'] for row in report['three_leg_budgets']], [21, 24, 72])
        self.assertEqual(report['complete_source_replay']['source_terms_checked'], 262144)
        self.assertEqual(report['complete_source_replay']['nonzero_target_coefficients'], 252)
        self.assertEqual(len(report['known_necessary_hankel_tests']), 15)
        self.assertTrue(report['conditional_exponent']['inequality_passes'])
        self.assertFalse(report['full_rectangular_target_constructed'])
        self.assertFalse(report['new_exponent_established'])

    def test_nonzero_kernel_tamper_is_rejected(self):
        certificate = json.loads(CORE.CERTIFICATE.read_text())
        certificate['Y']['integer_kernel_vectors'][0][0][1] *= 2
        with self.assertRaisesRegex(ArithmeticError, 'integer kernel vector has a nonzero exact coefficient'):
            CORE.verify(certificate=certificate)

    def test_growing_the_first_core_updates_the_budget(self):
        at_cap = CORE.budgets((216, 236, 216), core=(3, 4, 28))[0]
        above_cap = CORE.budgets((217, 236, 216), core=(3, 4, 28))[0]
        self.assertEqual(at_cap['retained_leg_dimension'], 12)
        self.assertEqual(at_cap['excess_response_rank'], 204)
        self.assertTrue(at_cap['necessary_preimage_test_passes'])
        self.assertFalse(above_cap['necessary_preimage_test_passes'])


if __name__ == '__main__':
    unittest.main()

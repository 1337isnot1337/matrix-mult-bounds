"""Exact regression for the variable-coefficient shift-window obstruction."""
import importlib.util
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SCRIPT = HERE / 'research' / 'ai' / '2026-10-23-shift-window-long-legs' / 'verify.py'
spec = importlib.util.spec_from_file_location('shift_window_long_legs_verify', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ShiftWindowLongLegTests(unittest.TestCase):
    def test_five_finite_coefficient_and_flattening_controls(self):
        outcome = module.run()
        self.assertEqual(outcome['status'], 'pass')
        self.assertEqual([x['observed_residual_flattening_rank_F101']
                          for x in outcome['cases']], [64,100,100,144,144])
        self.assertEqual([x['predicted_lower_bound']
                          for x in outcome['cases']], [16,16,16,25,36])

    def test_recurrence_window_expansion_is_sensitive_to_tampering(self):
        with self.assertRaises(AssertionError):
            module.check(8,3,0,'polynomial',1,tamper_phi=True)

    def test_unrestricted_bulk_can_have_full_window_span(self):
        self.assertTrue(module.full_window_rank_control(3))
        self.assertTrue(module.full_window_rank_control(4))

    def test_genuinely_variable_bulk(self):
        b = module.bcoef
        self.assertNotEqual(b('polynomial',2,1,0,0,1),b('polynomial',2,1,0,0,2))
        self.assertNotEqual(b('exp_linear',0,1,0,0,1),b('exp_linear',0,1,0,0,2))


if __name__ == '__main__':
    unittest.main()

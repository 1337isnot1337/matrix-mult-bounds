import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin44.py'
SPEC = importlib.util.spec_from_file_location('balanced_spin44', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class BalancedSpinTests(unittest.TestCase):
    def test_full_rational_witness_and_four_parity_lift(self):
        report, exported = MODULE.verify(exported=json.loads(MODULE.MAPS.read_text()))
        self.assertEqual(report['construction_checks']['join_determinant'], '21/128')
        self.assertEqual(report['map_denominators'], [2, 42, 2])
        self.assertEqual(exported['restrictions'][1]['target'], [3, 3, 32])
        self.assertEqual(report['original_source_replays'][1]['target_coefficients_checked'], 82944)
        self.assertFalse(report['new_exponent_established'])

    def test_changed_rational_map_is_rejected(self):
        witness = json.loads(MODULE.WITNESS.read_text())
        witness['Y']['entries'][0][2] += 1
        with self.assertRaises(ArithmeticError):
            MODULE.verify(witness=witness)

    def test_changed_parity_coordinate_is_rejected(self):
        exported = json.loads(MODULE.MAPS.read_text())
        entry = exported['restrictions'][1]['maps']['Y']['entries'][0]
        entry[1] += 1
        with self.assertRaises(ArithmeticError):
            MODULE.verify(exported=exported)


if __name__ == '__main__':
    unittest.main()

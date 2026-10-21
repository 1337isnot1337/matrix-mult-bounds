"""Standard-library replay of the exact seed used for the live A88 target."""

import importlib.util
from pathlib import Path
import unittest


PATH = (Path(__file__).resolve().parents[1] / 'research' / 'ai' /
        '2026-10-20-anisotropic-constructions' / 'parity_structure_torus_seed.py')
SPEC = importlib.util.spec_from_file_location('parity_structure_torus_seed', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TorusSeedTest(unittest.TestCase):
    def test_complete_seed_partial_target_anchors_and_tamper(self):
        report = MODULE.verify()
        self.assertEqual(report['source_terms_checked'], 262144)
        self.assertEqual(report['seed_target_terms'], 1755)
        self.assertEqual(report['extreme_charge_M2_control_terms'], 8)
        self.assertTrue(report['nonzero_to_nonzero_tamper_rejected'])
        self.assertTrue(report['full_target_charge_profile_fits'])
        self.assertEqual(report['full_target_charge_slack'],
                         [4, 7, 8, 10, 11, 11, 12, 10, 8, 5, 3, 2, 1, 1, 0])
        self.assertFalse(report['full_target_witness'])


if __name__ == '__main__':
    unittest.main()

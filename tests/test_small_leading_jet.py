import importlib.util
from pathlib import Path
import unittest

PATH=Path(__file__).resolve().parents[1]/'research/ai/2026-10-20-paired-construction/small_leading_jet.py'
SPEC=importlib.util.spec_from_file_location('small_leading_jet_control',PATH)
MODULE=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(MODULE)

class SmallLeadingJetTests(unittest.TestCase):
    def test_complete_first_jet_gate(self):
        report=MODULE.certificate(include_linear_systems=False)
        self.assertEqual(report['leading_source_A_rank'],16)
        self.assertNotEqual(report['old_rank_minor_determinant'],0)
        self.assertEqual(len(report['K0_sparse_basis']),21)
        self.assertEqual(report['joint_possible_action_row_rank'],0)
        for leg in ['B','C']:
            self.assertEqual(report['first_jet_data'][leg]['nullity'],96)
            self.assertEqual(len(report['first_jet_data'][leg]['pivot_columns']),52)
            self.assertTrue(report['first_jet_data'][leg]['canonical_kernel_conditions_checked'])
        self.assertFalse(report['different_leading_maps_excluded'])

if __name__=='__main__':unittest.main()

"""Exact coefficient and support checks for the fixed enriched leading point."""
import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT/'research/ai/2026-10-20-paired-direct-sums'
sys.path.insert(0, str(DIRECTORY))
SPEC = importlib.util.spec_from_file_location('enriched_lead_checked', DIRECTORY/'r_enriched_lead_obstruction.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class EnrichedLeadTests(unittest.TestCase):
    def test_all_leading_coefficients_and_both_first_edge_supports(self):
        result = CHECK.report()
        self.assertEqual(result['leading_integer_rational_positions_checked'], 4096)
        self.assertEqual(result['native_leading_rank'], 4)
        self.assertEqual(len(result['native_K0_basis_indices']), 12)
        self.assertEqual(len(result['endpoint_first_edge_native_B_support']), 6)
        self.assertEqual(len(result['endpoint_first_edge_native_C_support']), 6)
        self.assertEqual(result['interior_first_edge_old_C_support'], [1])
        self.assertEqual(result['interior_first_edge_old_B_support'], [4])
        self.assertTrue(result['target_functional_slice_identity_checked_on_all_basis_coefficients'])
        self.assertFalse(result['arbitrary_border_D2_repair_excluded'])


if __name__ == '__main__':
    unittest.main()

"""Exact leading-point gates, with no optional numerical dependencies."""
import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-paired-direct-sums'
sys.path.insert(0, str(PACKAGE))
SPEC = importlib.util.spec_from_file_location('q64_m1_leading_exact_tested', PACKAGE/'q64_m1_leading_exact.py')
EXACT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXACT)


class LeadingPointTests(unittest.TestCase):
    def test_sparse_obstruction_and_distinct_endpoint_gate(self):
        report = EXACT.exact_report()
        self.assertEqual(report['sparse_fixed_point']['first_edge_source_ranks'], [10, 10])
        self.assertEqual(report['endpoint_product_point']['first_edge_source_ranks'], [32, 32])
        self.assertTrue(report['sparse_fixed_point_excluded_in_stated_chart'])
        self.assertFalse(report['moving_leading_maps_excluded'])

    def test_sparse_support_formula_at_other_sizes(self):
        for n in [3, 4, 5]:
            report = EXACT.leading_data(*EXACT.sparse_maps(n), n=n)
            self.assertEqual(report['pre_A_rank'], 4)
            self.assertEqual(report['first_edge_source_ranks'], [2*(n-1)]*2)
            if n >= 4:
                self.assertLess(2*(n-1), 4*(n-2))


if __name__ == '__main__':
    unittest.main()

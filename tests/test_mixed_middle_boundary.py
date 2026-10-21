import importlib.util
from pathlib import Path
import unittest

PATH=Path(__file__).resolve().parents[1]/'research/ai/2026-10-20-paired-construction/mixed_middle_boundary.py'
SPEC=importlib.util.spec_from_file_location('mixed_middle_boundary_control',PATH)
MODULE=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class MixedMiddleBoundaryTests(unittest.TestCase):
    def test_complete_integer_identity_and_projected_rank(self):
        report=MODULE.certificate()
        self.assertEqual(report['coefficient_failures'],0)
        self.assertEqual(report['all_target_coefficients_checked'],4096)
        self.assertEqual(report['projected_source_A_rank'],36)
        self.assertNotEqual(report['rank_minor_determinant'],0)
        self.assertEqual(report['projected_slices_changed'],[35])
        self.assertTrue(report['corner_outer_product_update_checked'])
        self.assertLess(report['singular_middle_product_rank'],16)

    def test_nonproduct_middle_space(self):
        h=MODULE.middle_space()
        # The collective polynomial support has dimension three, whereas
        # a four-dimensional Y2 tensor W2 would have support dimension two.
        rows=[[h[j][y][b] for y in range(4)] for j in range(4) for b in range(2)]
        self.assertEqual(len(MODULE.BASE.pivots(rows)),3)

if __name__=='__main__':
    unittest.main()

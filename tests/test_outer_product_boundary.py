"""Exact checks of the specified boundary-column Laurent obstruction."""

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-20-paired-construction"
SPEC = importlib.util.spec_from_file_location("outer_product_boundary", PACKAGE / "outer_product_boundary.py")
B = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(B)


class OuterProductBoundaryTests(unittest.TestCase):
    def test_saved_exact_corner_and_rank(self):
        saved = json.loads((PACKAGE / "q64-boundary-chart.json").read_text())
        self.assertEqual(saved, B.certificate(4))
        b, c = saved["long_maps_target_by_source"]
        # Directly verify the rank-one corner cancellation from the saved maps.
        for ib in range(16):
            for ic in range(16):
                actual = sum(b[ib][9*y+5+v]*c[ic][4*(5+y)+v]
                             for y in range(4) for v in range(4))
                self.assertEqual(actual, 0)
        self.assertEqual(saved["crossed_boundary_pre_A_rank"], 35)
        self.assertEqual(abs(saved["rank_minor_determinant"]), 1)
        self.assertEqual(saved["required_A_kernel_dimension_for_stated_M_extension"], 9)
        self.assertFalse(saved["general_degeneration_excluded"])

    def test_integer_family_and_symbolic_update_controls(self):
        for k in range(2, 7):
            report = B.certificate(k, include_maps=False)
            self.assertEqual(report["crossed_boundary_pre_A_rank"], (k+2)**2-1)
            self.assertEqual(report["zero_boundary_pre_A_rank"], (k+2)**2)
            self.assertTrue(report["arbitrary_boundary_control"]["corner_update_is_specified_outer_product"])

    def test_old_source_columns_are_exactly_preserved(self):
        _, old_b, old_c = B.SEED.maps(4)
        new_b, new_c = B.boundary_maps(4, crossed=True)
        for row in range(16):
            for y in range(4):
                for s in range(8):
                    self.assertEqual(new_b[row][9*y+s], old_b[row][8*y+s])
            for z in range(8):
                for v in range(4):
                    self.assertEqual(new_c[row][4*z+v], old_c[row][4*z+v])


if __name__ == "__main__":
    unittest.main()

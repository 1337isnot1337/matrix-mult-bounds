"""Exact controls for the independent-map module reformulation."""

import importlib.util
from pathlib import Path
import unittest


PATH = Path(__file__).resolve().parents[1] / "research/ai/2026-10-20-rectangular-module/verify_module.py"
SPEC = importlib.util.spec_from_file_location("rectangular_module", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RectangularModuleTests(unittest.TestCase):
    def test_laurent_reconstruction_and_free_slice(self):
        report = MODULE.laurent_control()
        self.assertEqual(report["negative_coefficients"], 0)
        self.assertTrue(report["extra_slice_has_nonzero_limit"])

    def test_parity_factors_all_coefficients(self):
        for m in (4, 6):
            with self.subTest(m=m):
                report = MODULE.parity_control(m)
                self.assertEqual(report["middle_dimension"], m * (m + 1) // 2 + m // 2 - 1)

    def test_syzygies_reconstruct_and_reject_corruption(self):
        report = MODULE.cubic_syzygy_control()
        self.assertEqual(report["syzygy_matrix_rank"], 8)
        self.assertTrue(report["corrupted_right_factor_rejected"])

    def test_coprime_and_common_factor_cases_differ(self):
        report = MODULE.coprime_control()
        self.assertEqual(report["relation_system_rank"], 28)
        self.assertLess(report["common_factor_control_rank"], 28)


if __name__ == "__main__":
    unittest.main()

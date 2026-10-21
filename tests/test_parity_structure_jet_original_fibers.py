"""Replay original-source Laurent cancellations and the exact slice cover."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_jet_original_fibers.py"
SPEC = importlib.util.spec_from_file_location("parity_structure_jet_original_fibers", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OriginalSourceJetFiberTests(unittest.TestCase):
    def test_complete_source_identity_new_fiber_tamper_and_cover(self):
        report = MODULE.verify()
        self.assertEqual(report["source_terms_examined"], 262144)
        self.assertEqual(report["exact_negative_system_ranks"], [598, 598, 597])
        self.assertEqual(report["new_original_source_kernel_dimensions"], [228, 228, 229])
        self.assertEqual(report["full_coefficient_map_ranks_mod1009"], [960, 960, 960])
        self.assertEqual(report["constant_nonzero_coefficients"], 28316)
        self.assertEqual(report["concise_coordinate_projection_dimensions"], [936, 936, 935])
        self.assertEqual(report["concise_projection_flattening_ranks_mod1009"], [936, 936, 935])
        self.assertEqual(report["slice_cover_sizes_per_leg"], [42, 42, 42])
        self.assertEqual(report["slice_rank_upper_bound"], 126)
        self.assertTrue(report["all_negative_powers_cancel_exactly"])
        self.assertTrue(report["nonzero_to_nonzero_original_fiber_tamper_rejected"])
        self.assertFalse(report["full_target_27_plus_7_witness"])
        self.assertFalse(report["new_exponent_established"])


if __name__ == "__main__":
    unittest.main()

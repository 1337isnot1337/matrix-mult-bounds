import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "m1_corner_one_scalar",
    ROOT / "research/ai/2026-10-20-paired-construction/m1_corner_one_scalar.py",
)
SCALAR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCALAR)


class M1CornerOneScalarTests(unittest.TestCase):
    def test_both_source_map_cases(self):
        result = SCALAR.verify()
        control = result["invertible_A_R_control"]
        self.assertEqual(control["basis_slice_ranks"], [5, 4, 4, 4])
        self.assertEqual(control["aggregate_long_support_dimensions"], [15, 5])
        self.assertEqual(result["singular_A_R_control"]["target_A15_slice_rank"], 1)
        self.assertTrue(result["one_scalar_degeneration_excluded"])
        self.assertFalse(result["two_scalar_degeneration_excluded"])
        self.assertFalse(result["general_Q64_degeneration_excluded"])


if __name__ == "__main__":
    unittest.main()

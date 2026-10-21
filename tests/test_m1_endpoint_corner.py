import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "m1_endpoint_corner",
    ROOT / "research/ai/2026-10-20-paired-construction/m1_endpoint_corner.py",
)
CORNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORNER)


class M1EndpointCornerTests(unittest.TestCase):
    def test_native_coefficients_and_low_rank_subspace(self):
        result = CORNER.verify()
        self.assertEqual(result["coefficient_positions_checked"], 5184)
        self.assertEqual(result["coefficient_failures"], 0)
        self.assertEqual(result["corner_flattening_ranks"], [16, 18, 18])
        self.assertEqual(result["rank_three_witness_rank"], 3)
        self.assertEqual(result["pure_t5_tensor_t5_slice_rank"], 4)
        self.assertEqual(result["t5_tensor_P_fibre_support_dimensions"], [14, 4])
        self.assertFalse(result["Q64_general_degeneration_excluded"])
        self.assertFalse(result["improves_omega"])


if __name__ == "__main__":
    unittest.main()

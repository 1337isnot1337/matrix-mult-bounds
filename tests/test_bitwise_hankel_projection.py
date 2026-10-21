import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "research/ai/2026-10-20-anisotropic-constructions/bitwise_hankel_projection.py"
SPEC = importlib.util.spec_from_file_location("bitwise_hankel_projection", MODULE)
PROJECTION = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PROJECTION)


class BitwiseHankelProjectionTests(unittest.TestCase):
    def test_exact_carry_coefficients_and_saved_scope(self):
        actual = PROJECTION.carry_control()
        stored = json.loads(PROJECTION.OUTPUT.read_text())
        self.assertEqual(actual, stored["uncompressed_spin1_square_carry_control"])
        self.assertEqual([item["forced_alpha_x"] for item in actual["witnesses"]], ["0", "1"])
        self.assertFalse(actual["general_source_compression_excluded"])
        self.assertFalse(stored["new_exponent_established"])

    def test_average_projection_remains_injective(self):
        self.assertEqual(PROJECTION.map_rank(), 81)
        polys = PROJECTION.coefficient_polynomials()
        for point in [(9, 0, 61), (12, 50, 39)]:
            self.assertEqual(PROJECTION.selected_coefficient(point), polys[point])


if __name__ == "__main__":
    unittest.main()

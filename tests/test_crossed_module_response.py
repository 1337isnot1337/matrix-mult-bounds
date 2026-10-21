"""Standard-library replay of the saved module's full ambient response."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/crossed_module_response.py"
SPEC = importlib.util.spec_from_file_location("crossed_module_response", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CrossedModuleResponseTests(unittest.TestCase):
    def test_exact_response_rank_and_scope(self):
        report = MODULE.verify()
        self.assertEqual(report["full_response_rank"], 256)
        self.assertEqual(report["full_response_kernel_dimension"], 704)
        self.assertEqual(report["maximum_leg_dimension_of_an_extension_preserving_the_saved_other_maps"], 720)
        self.assertFalse(report["other_module_maps_excluded"])
        self.assertFalse(report["arbitrary_degenerations_excluded"])

    def test_modular_determinant_control(self):
        self.assertEqual(MODULE.determinant_mod([[0, 2], [3, 4]], 65521), 65515)
        self.assertEqual(MODULE.determinant_mod([[2, 4], [3, 6]], 65521), 0)


if __name__ == "__main__":
    unittest.main()

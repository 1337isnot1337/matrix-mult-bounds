import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_cross_module_corner_shifted.py"
SPEC = importlib.util.spec_from_file_location("parity_structure_cross_module_corner_shifted", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ShiftedCornerTests(unittest.TestCase):
    def test_complete_identity_and_response164(self):
        data = json.loads(MODULE.MAPS.read_text())
        report = MODULE.verify(data)
        self.assertEqual(report["full_response_rank_exact"], 164)
        self.assertEqual(report["nonzero_target_coefficients"], 192)
        self.assertEqual(report["changed_first_core_flattening"]["exact_rational_rank"], 481)

    def test_actual_corner_coefficient_tamper(self):
        data = copy.deepcopy(json.loads(MODULE.MAPS.read_text()))
        selected = next(entry for entry in data["maps"][2]["entries"] if entry[0] // 4 == 11)
        selected[2] *= 2
        with self.assertRaises(ArithmeticError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()

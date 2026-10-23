"""Exact source-basis escape and tamper controls, with no optional imports."""

import copy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "spin_basis_escape",
    ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_basis_escape.py",
)
control = importlib.util.module_from_spec(spec)
spec.loader.exec_module(control)


class SpinBasisEscapeTests(unittest.TestCase):
    def test_complete_local_identity_and_original_source_escape(self):
        report = control.verify()
        self.assertEqual(report["local_output_coefficients_checked"], 729)
        self.assertEqual(report["selected_numerators_over64"], [64, 128, 448])
        self.assertEqual(report["linear_combination"], "6")
        self.assertFalse(report["M9_constructed"])

    def test_nonzero_to_nonzero_map_tamper_is_rejected(self):
        data = copy.deepcopy(control.witness())
        entry = data["compressed"]["maps"][1][0]
        entry[2] *= 2
        with self.assertRaises(ArithmeticError):
            control.verify(data)

    def test_false_zero_hyperplane_report_is_rejected(self):
        data = copy.deepcopy(control.witness())
        data["linear_combination_numerator_over64"] = 0
        with self.assertRaises(ArithmeticError):
            control.verify(data)


if __name__ == "__main__":
    unittest.main()

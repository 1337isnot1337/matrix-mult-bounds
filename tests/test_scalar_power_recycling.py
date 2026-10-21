"""Exact controls for the explicitly charged scalar-defect powers."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/scalar_power_recycling.py"
SPEC = importlib.util.spec_from_file_location("scalar_power_recycling", PATH)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)
REPORT = ROOT / "results/anisotropic-constructions-2026-10-20/scalar-power-recycling.json"


class ScalarPowerRecyclingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads(REPORT.read_text())

    def test_complete_saved_witness_without_regeneration(self):
        with patch.object(MOD, "construct_square", side_effect=AssertionError("regeneration forbidden")):
            result = MOD.verify_square(self.saved["square_witness"])
        self.assertEqual(result, self.saved["square_verification"])
        self.assertEqual(result["source_terms_checked"], 4187)
        self.assertEqual(result["target_coefficients_checked"], 531441)

    def test_auxiliary_sign_cannot_be_omitted(self):
        altered = copy.deepcopy(self.saved["square_witness"])
        for row in altered["sparse_map_numerators"][2]:
            for entry in row:
                if entry[0] >= 144:
                    entry[1] = -entry[1]
        with self.assertRaises(ArithmeticError):
            MOD.verify_square(altered)

    def test_independently_eliminated_residual_slice_ranks(self):
        self.assertEqual(MOD.controls(), self.saved["residual_rank_controls"])
        self.assertEqual(MOD.exact_rank(MOD.residual_identity_slice(3, 2)), 17)

    def test_exact_costs_and_retained_scope(self):
        costs = MOD.cost_report()
        self.assertEqual(costs, self.saved["costs"])
        self.assertTrue(costs["finite_gate_for_A22_powers"]["strict_inequality"])
        self.assertTrue(costs["telescoping_gate_comparison"]["strict_inequality"])
        self.assertEqual(costs["powers"][2]["residual_flattening_rank"], 217)
        self.assertEqual(costs["powers"][2]["independent_matrix_correction_size_lower_bound"], 15)
        self.assertFalse(costs["new_exponent_established"])
        self.assertFalse(costs["finite_gate_for_A22_powers"]["general_tensor_power_constructions_excluded"])


if __name__ == "__main__":
    unittest.main()

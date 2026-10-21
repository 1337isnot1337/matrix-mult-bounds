import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "research/ai/2026-10-20-anisotropic-constructions/two_source_budget.py"
SPEC = importlib.util.spec_from_file_location("two_source_budget", MODULE)
BUDGET = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUDGET)


class TwoSourceBudgetTests(unittest.TestCase):
    def test_sharp_capacity_and_complete_majority_coefficients(self):
        for n in range(2, 35):
            minimum = BUDGET.equal_source_minimum(n)
            self.assertTrue(BUDGET.capacity_passes(n, minimum, minimum))
            self.assertFalse(BUDGET.capacity_passes(n, minimum-1, minimum-1))
        for r, s in [(1, 1), (2, 2), (2, 3), (3, 4)]:
            result = BUDGET.majority_control(r, s)
            self.assertTrue(result["complete_coefficient_identity"])
            self.assertEqual(result["checked_target_terms"], (r+s)**3)
            first, second = result["source_leg_dimensions"]
            self.assertFalse(BUDGET.capacity_passes(r+s, first-1, second))

    def test_exact_frontiers_and_conditional_scope(self):
        stored = json.loads(BUDGET.OUTPUT.read_text())
        self.assertEqual(BUDGET.build_report(), stored)
        first = stored["two_equal_source_frontier"]["first_relaxed_survivor"]
        self.assertEqual((first["a"], first["b"], first["largest_capacity_admissible_square"]), (11, 12, 62))
        self.assertFalse(stored["new_exponent_established"])
        self.assertFalse(stored["conditional_pair_target"]["map_constructed"])

    def test_ordinary_minimum_rank_gate_and_old_pair_rejections(self):
        self.assertFalse(BUDGET.capacity_passes(35, 784, 784))
        self.assertFalse(BUDGET.capacity_passes(38, 960, 960))
        reasons = BUDGET.majority_obstructions(11, 12, 31)
        minimum = next(item for item in reasons if item["kind"] == "minimum_source_slice_rank")
        self.assertEqual((minimum["lift_upper"], minimum["source_lower"]), (73, 132))
        self.assertTrue(BUDGET.majority_obstructions(12, 13, 35))
        self.assertFalse(BUDGET.majority_obstructions(18, 21, 64))


if __name__ == "__main__":
    unittest.main()

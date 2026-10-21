"""Controls of full contractions in the correction-capacity argument."""

import importlib.util
from pathlib import Path
import unittest


PATH = (Path(__file__).resolve().parents[1] / "research" / "ai" /
        "2026-10-21-correction-budget" / "source_capacity.py")
SPEC = importlib.util.spec_from_file_location("source_capacity_controls", PATH)
CAPACITY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CAPACITY)


class SourceCapacityControls(unittest.TestCase):
    def test_complete_rational_contractions_and_mutation(self):
        result = CAPACITY.report()
        self.assertEqual(result["status"], "passed")
        self.assertEqual(len(result["cases"]), 10)
        self.assertTrue(result["negative_control"]["rejected"])
        strict = result["cases"][-1]
        self.assertGreater(strict["restricted_a_rank"], strict["ceiling_lower_bound"])
        self.assertEqual(result["positive_width_margin"], list(range(4, 21)))

    def test_dependent_subspace_is_rejected(self):
        forms = CAPACITY.coordinate_subspace(2, 2, 1)
        with self.assertRaises(ValueError):
            CAPACITY.check_case(2, 2, 3, forms + forms, "dependent")


if __name__ == "__main__":
    unittest.main()

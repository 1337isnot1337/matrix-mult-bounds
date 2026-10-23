"""Exact support and corruption controls for staircase source spaces."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-source-staircase-spaces/verify.py"
SPEC = importlib.util.spec_from_file_location("source_staircase_spaces", PATH)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class SourceStaircaseSpacesTests(unittest.TestCase):
    def test_frozen_all_case_support_replay(self):
        document = json.loads(verify.RESULT.read_text())
        verify.replay_saved(document)
        self.assertEqual(document["coverage"]["parameter_triples"], 140)
        self.assertEqual(document["coverage"]["literal_terms_reconstructed"], 67170)
        self.assertEqual([(r["dimension"], r["uniform_rank_upper"]) for r in document["a4_table"]],
                         [(56, 80), (60, 84), (64, 88), (68, 92)])

    def test_same_dimension_outside_mask_breaks_column_budget(self):
        record = json.loads(verify.RESULT.read_text())["a4_counterexample"]
        # Move one selected coordinate to middle k3 in the next i-layer.
        # Dimension stays68, but the newly allowed q3 adds four columns.
        mask = int(record["coordinate_mask"], 16)
        record["coordinate_mask"] = hex((mask ^ (1 << 67)) | (1 << 68))
        with self.assertRaisesRegex(ArithmeticError, "column support"):
            verify.replay_counterexample(record)

    def test_dimension_and_rank_budget_corruptions_are_rejected(self):
        record = json.loads(verify.RESULT.read_text())["a4_counterexample"]
        record["dimension"] = 69
        with self.assertRaisesRegex(ArithmeticError, "dimension changed"):
            verify.replay_counterexample(record)
        record = json.loads(verify.RESULT.read_text())["a4_counterexample"]
        record["uniform_rank_upper"] = 91
        with self.assertRaisesRegex(ArithmeticError, "column support"):
            verify.replay_counterexample(record)

    def test_source_pin_and_inventory_corruption_are_rejected(self):
        original = json.loads((verify.HERE / "sources.json").read_text())
        changed = copy.deepcopy(original)
        changed["local_dependencies"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            verify.check_sources(changed)
        original["local_dependencies"].pop()
        with self.assertRaisesRegex(ArithmeticError, "source inventory"):
            verify.check_sources(original)

    def test_strict_threshold_and_unproved_attainment_stay_distinct(self):
        document = json.loads(verify.RESULT.read_text())
        self.assertEqual(document["boundary_control"]["uniform_rank_upper"], 96)
        self.assertFalse(document["boundary_control"]["column_count_proves_rank_below_96"])
        document["claim_scope"]["blocks_every_source_cap_refinement"] = True
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)

    def test_parameter_endpoints_and_invalid_inputs(self):
        self.assertEqual(verify.family(2, 1, 0)["dimension"], 6)
        self.assertEqual(verify.family(4, 3, 7)["dimension"], 112)
        self.assertEqual(verify.family(4, 3, 7)["supported_columns"], 112)
        for args in ((4, 0, 2), (4, 4, 0), (4, 2, 8), (4, 2, -1)):
            with self.assertRaisesRegex(ArithmeticError, "invalid staircase"):
                verify.family(*args)


if __name__ == "__main__":
    unittest.main()

"""Exact matrix controls, strict-boundary checks and corrupted evidence rejection."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-regular-unit-image"
SPEC = importlib.util.spec_from_file_location("regular_unit_image", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class RegularUnitImageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_full_control_replay(self):
        receipt = v.verify(self.record)
        self.assertEqual(receipt, {"projection_families": 16, "rank_budget_controls": 8,
                                  "regularized_product_controls": 4, "singular_unit_controls": 4,
                                  "a4_rank_cases": 3, "improves_omega": False})

    def test_equality_is_not_a_strict_dimension_contradiction(self):
        cases = self.record["a4_rank_margins"]
        self.assertEqual([x["forces_regularity"] for x in cases], [True, True, False])
        self.assertEqual(cases[1]["strict_margins"],
                         {"first_pole": 7, "first_injectivity": 6, "row_kernel_dimension": 1})
        self.assertEqual(cases[2]["strict_margins"]["row_kernel_dimension"], 0)

    def test_reject_changed_scope_false_boundary_and_raw_coefficient_rank(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(proof_status="reviewed-proof"),
            lambda x: x["a4_rank_margins"][2].update(forces_regularity=True),
            lambda x: x["regularized_products"][0].update(raw_constant_rank=1),
            lambda x: x["projection_recovery"][0].update(hidden_pole_rows_recovered=0),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_changed_predecessor_pins_and_dependency_removal(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(3):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        bad = copy.deepcopy(original)
        bad["local_dependencies"].pop()
        with self.assertRaises(ValueError):
            v.check_sources(bad)


if __name__ == "__main__":
    unittest.main()

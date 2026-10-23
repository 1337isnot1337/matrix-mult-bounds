"""One-sided rank budgets, unresolved boundary and rejection of changed evidence."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-one-sided-unit-image"
SPEC = importlib.util.spec_from_file_location("one_sided_unit_image", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class OneSidedUnitImageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_exact_control_replay(self):
        self.assertEqual(v.verify(self.record), {
            "a4_rank_cases": 5, "one_sided_target_controls": 5,
            "full_column_kernel_controls": 5, "first_pole_controls": 6,
            "regularized_product_controls": 6, "improves_omega": False})

    def test_new_boundary_and_original_column_count(self):
        cases = self.record["a4_rank_margins"]
        self.assertEqual([c["forces_regularity"] for c in cases], [True]*4+[False])
        self.assertEqual(cases[3]["strict_margins"], {
            "first_pole": 1, "first_injectivity": 3, "full_row_kernel_dimension": 2})
        control = next(c for c in self.record["full_column_kernel_controls"]
                       if c["retained"] == 107)
        self.assertEqual(control["full_kernel_dimension"], 98)
        self.assertEqual(control["compressed_kernel_dimension"], 101)

    def test_strict_inequalities_and_invalid_dimensions(self):
        base = dict(source_dimension=112, matrix_dimension=112,
                    target_dimension=110, parameter_dimension=100,
                    source_minimum=16, row_minimum=16,
                    target_minimum=11, retained=107)
        for key, value in (("source_minimum", 15), ("target_minimum", 8),
                           ("parameter_dimension", 98)):
            self.assertFalse(v.margins(**dict(base, **{key: value}))["forces_regularity"])
        for key, value in (("retained", 111), ("retained", 0),
                           ("target_dimension", 113), ("row_minimum", True)):
            with self.assertRaises(ValueError):
                v.margins(**dict(base, **{key: value}))

    def test_reject_changed_boundary_rank_loss_and_proof_status(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(proof_status="reviewed-proof"),
            lambda x: x["a4_rank_margins"][-1].update(forces_regularity=True),
            lambda x: x["one_sided_target_controls"][3].update(rank_loss=6),
            lambda x: x["full_column_kernel_controls"][1].update(full_kernel_dimension=101),
            lambda x: x["regularized_product_controls"][0].update(raw_constant_rank=1),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_source_pins_and_inventory(self):
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

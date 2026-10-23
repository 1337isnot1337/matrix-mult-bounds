"""Polar right-inverse controls and strict Laurent-regularity boundaries."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-regular-unit-projector"
SPEC = importlib.util.spec_from_file_location("regular_unit_projector", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class RegularUnitProjectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_polar_projector_replay(self):
        self.assertEqual(v.verify(self.record), {
            "polar_projectors": 9, "source_rank_budgets": 5,
            "target_boundary_controls": 4, "row_contraction_budgets": 5,
            "a4_rank_cases": 11, "minimum_sufficient_unit_image_rank": 102,
            "improves_omega": False,
        })

    def test_rank102_and_exact_rank101_injectivity_boundary(self):
        cases = {c["retained"]: c for c in self.record["a4_rank_margins"]}
        self.assertTrue(cases[102]["forces_all_regularity"])
        self.assertEqual(cases[102]["strict_margins"], {
            "first_pole": 12, "first_injectivity": 1, "row_kernel_dimension": 2})
        self.assertFalse(cases[101]["forces_all_regularity"])
        self.assertTrue(cases[101]["forces_first_regularity"])
        self.assertEqual(cases[101]["strict_margins"]["first_injectivity"], 0)
        boundary = self.record["target_injectivity_boundary"]
        self.assertEqual([c["product_rank"] for c in boundary], [4, 3, 2, 1])

    def test_each_strict_hypothesis_and_invalid_dimensions(self):
        common = dict(source_dimension=112, matrix_dimension=112, target_dimension=110,
                      parameter_dimension=100, source_minimum=16, row_minimum=16,
                      target_minimum=11, retained=102)
        for changed in ({"source_minimum": 4}, {"target_minimum": 10},
                        {"parameter_dimension": 98}):
            with self.subTest(changed=changed):
                self.assertFalse(v.margins(**(common | changed))["forces_all_regularity"])
        for changed in ({"retained": 111}, {"retained": 0},
                        {"matrix_dimension": True}, {"row_minimum": 113}):
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                v.margins(**(common | changed))

    def test_reject_corrupted_scope_boundary_and_rank_evidence(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(independent_review=True),
            lambda x: x["a4_rank_margins"][9].update(forces_all_regularity=True),
            lambda x: x["raw_coefficient_negative_control"].update(raw_constant_rank=1),
            lambda x: x["polar_projectors"][0].update(projector_rank=0),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_changed_predecessor_pins_or_inventory(self):
        sources = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(2):
            bad = copy.deepcopy(sources)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        bad = copy.deepcopy(sources)
        bad["local_dependencies"].pop()
        with self.assertRaises(ValueError):
            v.check_sources(bad)


if __name__ == "__main__":
    unittest.main()

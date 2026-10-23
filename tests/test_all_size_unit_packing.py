"""All-size proof-data controls, independent determinants and scope corruption."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-all-size-unit-packing"
SPEC = importlib.util.spec_from_file_location("all_size_unit_packing", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class AllSizeUnitPackingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_exact_integer_modular_and_recurrence_controls(self):
        receipt = v.verify(self.record)
        self.assertEqual(receipt, {"short_integer_determinants": 21,
                                  "independent_modular_checks": 63,
                                  "formal_successive_identities": 70,
                                  "packing_sizes": 12, "improves_omega": False})

    def test_base_case_a1_and_a4_agree_with_sharp_source_cap(self):
        cases = self.record["packing_and_sharp_kernel_controls"]
        self.assertEqual(cases[0]["all_singular_subspace_cap"], 0)
        self.assertEqual(cases[3]["source_dimension"], 112)
        self.assertEqual(cases[3]["all_singular_subspace_cap"], 96)
        self.assertEqual(cases[3]["disjoint_unit_count"], 16)
        for row in self.record["short_matrices"]:
            self.assertEqual(abs(row["integer_determinant"]), 1)
            self.assertEqual(row["independent_modular_determinants"]["2"], 1)

    def test_bad_characteristic_boundary_and_false_all_size_cap_are_rejected(self):
        for mutate in (
            lambda x: x.update(all_size_cap_formula="a^2*(2*a-2)-1"),
            lambda x: x["short_matrices"][0]["independent_modular_determinants"].update({"2": 0}),
            lambda x: x["formal_recurrence_controls"][0].update(terminal_unit_coefficient=0),
            lambda x: x.update(improves_omega=True),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_changed_or_missing_dependency_is_rejected(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(3):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        original["local_dependencies"].pop()
        with self.assertRaises(ValueError):
            v.check_sources(original)


if __name__ == "__main__":
    unittest.main()

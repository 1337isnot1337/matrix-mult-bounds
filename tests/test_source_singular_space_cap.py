"""Independent source assembly, exact unit packing and corrupted-cap controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-source-singular-space-cap"
SPEC = importlib.util.spec_from_file_location("source_singular_space_cap", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)
OLD_SPEC = importlib.util.spec_from_file_location(
    "singular_cap_literal_source", ROOT / "research/ai/2026-10-21-cyclic-slice-determinants/certify.py")
old = importlib.util.module_from_spec(OLD_SPEC)
OLD_SPEC.loader.exec_module(old)


class SourceSingularSpaceCapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_every_unit_and_all_entries_match_the_pinned_literal_source(self):
        receipt = v.verify(self.record)
        self.assertEqual(receipt["unit_witnesses"], 16)
        self.assertEqual(receipt["literal_factorization_entries_checked"], 200704)
        self.assertEqual(receipt["source_weight_entries_checked"], 4096)
        for witness in self.record["unit_witnesses"]:
            support = set(witness["coefficient_one_support"])
            f = [int(i in support) for i in range(112)]
            self.assertEqual(v.source_matrix(f), old.source_matrix(4, f))

    def test_sharp_kernel_has_exactly96_independent_coordinate_directions(self):
        constraints = set(self.record["sharp_kernel_constraints"])
        free = [i for i in range(112) if i not in constraints]
        self.assertEqual((len(constraints), len(free)), (16, 96))
        for i in free:
            f = [int(j == i) for j in range(112)]
            self.assertEqual(old.source_matrix(4, f)[0], [0]*112)
        for witness in self.record["unit_witnesses"]:
            self.assertEqual(len(constraints.intersection(witness["coefficient_one_support"])), 1)

    def test_lost_unit_wrong_weight_forged_determinant_and_overstated_cap_rejected(self):
        for mutate in (
            lambda x: x["unit_witnesses"].pop(),
            lambda x: x["unit_witnesses"][0].update(determinant_mod1009=0),
            lambda x: x["source_weights"].__setitem__(0, 1),
            lambda x: x.update(all_singular_subspace_dimension_cap=95),
            lambda x: x.update(improves_omega=True),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_changed_or_missing_source_pin_is_rejected(self):
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

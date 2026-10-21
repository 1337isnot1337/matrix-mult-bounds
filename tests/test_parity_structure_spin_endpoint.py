import copy
import importlib.util
import json
from math import lcm
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_endpoint.py"
SPEC = importlib.util.spec_from_file_location("parity_structure_spin_endpoint", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SpinEndpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(MODULE.MAPS.read_text())
        cls.minor = json.loads(MODULE.MINOR.read_text())

    def test_complete_core_and_endpoint_replay(self):
        report = MODULE.verify(self.data, self.minor)
        self.assertEqual(report["source_terms_checked"], 262144)
        self.assertEqual(report["all_target_coefficients_checked"], 59049)
        self.assertEqual(report["nonzero_target_coefficients"], 243)
        self.assertEqual(report["full_response_rank_exact"], 191)
        self.assertEqual(report["fixed_core_first_preimage_dimension_exact"], 778)
        self.assertFalse(report["full_M27_plus_M7_constructed"])

    def test_kernel_correction_tamper_breaks_endpoint_cancellation(self):
        data = copy.deepcopy(self.data)
        old_path = ROOT / "results/anisotropic-constructions-2026-10-20/spin-module14-full-maps.json"
        old = json.loads(old_path.read_text())["restrictions"][1]["maps"]["Y"]
        current = data["maps"]["Y"]
        denominator = lcm(current["denominator"], old["denominator"])
        scale = denominator//current["denominator"]
        for entry in current["entries"]:
            entry[2] *= scale
        current["denominator"] = denominator
        old_row = {column: denominator//old["denominator"]*value
                   for row, column, value in old["entries"] if row == 0}
        new_row = {column: value for row, column, value in current["entries"] if row == 0}
        self.assertNotEqual(old_row, new_row)
        doubled = {column: 2*new_row.get(column, 0)-old_row.get(column, 0)
                   for column in old_row.keys() | new_row.keys()}
        current["entries"] = [entry for entry in current["entries"] if entry[0] != 0]
        current["entries"].extend([0, column, value] for column, value in doubled.items() if value)
        with self.assertRaisesRegex(ArithmeticError, "support and endpoint cancellation"):
            MODULE.verify(data, self.minor)

    def test_changed_first_coefficient_breaks_core_identity(self):
        data = copy.deepcopy(self.data)
        data["maps"]["X"]["entries"][0][2] *= 2
        with self.assertRaisesRegex(ArithmeticError, "module identity"):
            MODULE.verify(data, self.minor)


if __name__ == "__main__":
    unittest.main()

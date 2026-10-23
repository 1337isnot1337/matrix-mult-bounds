"""Witness replay, singular long-leg boundaries and preserver degeneracies."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-singular-long-gap"
SPEC = importlib.util.spec_from_file_location("singular_long_gap", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class SingularLongGapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_all_exported_kernel_units_and_source_controls(self):
        self.assertEqual(v.verify(self.record), {
            "compression_kernel_units": 53, "degenerate_kernel_units": 3,
            "source_gap_matrices": 2, "lowest_excluded_long_limit_rank": 106,
            "improves_omega": False})

    def test_singular_rank106_and_unresolved_rank105(self):
        cases = {entry["long_limit_rank"]: entry for entry in self.record["a4_margins"]}
        self.assertTrue(cases[106]["excludes_target"])
        self.assertEqual(cases[106]["rank_one_source_budget"], 19)
        self.assertEqual(cases[106]["unit_image_margin"], 8)
        self.assertFalse(cases[105]["excludes_target"])
        self.assertEqual(cases[105]["minimum_gap_margin"], 0)
        self.assertEqual([entry["exact_rank"] for entry in self.record["source_gap"]], [16, 20])

    def test_both_rank_deficient_and_transposed_preserver_cases(self):
        selected = [entry for entry in self.record["compression_kernel_units"]
                    if entry["m"] == 10]
        self.assertEqual({(entry["p_rank"], entry["q_rank"]) for entry in selected},
                         {(4, 4), (1, 4), (4, 1)})
        for entry in selected:
            p, q, x = (s.Matrix(entry[name]) for name in ("P", "Q", "kernel_unit"))
            self.assertNotEqual(x.det(), 0)
            transposed_witness = x.T
            self.assertEqual(p*transposed_witness.T*q, s.zeros(4))

    def test_degenerate_images_have_large_kernels_with_exact_units(self):
        for entry in self.record["degenerate_kernel_units"]:
            self.assertGreater(entry["kernel_dimension"], entry["singular_dimension_cap"])
            x = s.Matrix(entry["kernel_unit"])
            values = s.Matrix(entry["linear_forms"])*s.Matrix(list(x))
            self.assertEqual(values, s.zeros(entry["a"], 1))
            fixed = s.eye(entry["a"])[:, 0]
            self.assertEqual(fixed*values.T, s.zeros(entry["a"]))

    def test_reject_corrupt_kernel_unit_scope_and_missing_case(self):
        for mutate in (
            lambda record: record["compression_kernel_units"][-1].update(kernel_unit=[["0"]*10]*10),
            lambda record: record.update(improves_omega=True),
            lambda record: record["compression_kernel_units"].pop(),
            lambda record: record["a4_margins"][-1].update(excludes_target=True),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_dependency_version_and_dimension_gate(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(len(original["local_dependencies"])):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        bad = copy.deepcopy(original)
        bad["external_dependencies"][0]["field"] = "unspecified"
        with self.assertRaises(ValueError):
            v.check_sources(bad)
        with self.assertRaises(ValueError):
            v.invertible_compression_kernel(s.eye(2), s.eye(2))


if __name__ == "__main__":
    unittest.main()

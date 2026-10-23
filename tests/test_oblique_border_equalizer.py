"""Replay the fixed residual's minimal-border-rank obstruction."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-oblique-border-equalizer"
SPEC = importlib.util.spec_from_file_location("oblique_border_equalizer", PACKAGE / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ObliqueBorderEqualizerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = MODULE.build_certificate()
        cls.n6 = next(case for case in cls.report["controls"] if case["b"] == 4)

    def test_complete_saved_certificate_and_native_identity(self):
        self.assertEqual(MODULE.verify_saved(PACKAGE / "certificate.json"), self.report)
        self.assertEqual(self.report["source_pin_verification"], {"count": 4, "all_match": True})
        native = self.report["native_n6_control"]
        self.assertEqual(native["source_coefficients_contracted"], 576)
        self.assertEqual(native["target_coordinates_compared"], 10000)
        self.assertEqual(native["native_residual_nonzero_coefficients"], 38)
        self.assertEqual(native["concise_tensor_sha256"], self.n6["concise_tensor_sha256"])
        self.assertTrue(native["literal_tensor_and_native_source_equal"])
        self.assertEqual(self.report["n6_border_rank_interval"], [12, 18])
        self.assertEqual(self.report["inherited_n6_ordinary_rank"], 19)

    def test_n6_unit_minor_and_two_kernel_generators(self):
        shape, tensor = MODULE.canonical_residual(4)
        rows = MODULE.equalizer_rows(shape, tensor)
        self.assertTrue(MODULE.check_minor(rows, self.n6["unit_minor"]))
        self.assertEqual(self.n6["matrix_format_with_zero_rows"], [1089, 242])
        self.assertEqual(self.n6["matrix_nonzero_rows"], 392)
        self.assertEqual(self.n6["unit_minor_order"], 240)
        self.assertEqual(self.n6["unit_minor_determinant"], -1)
        self.assertEqual(self.n6["rank_ceiling_for_border_rank_at_most_m"], 231)
        self.assertEqual(set(self.n6["unit_minor"]["unit_pivots"]), {-1, 1})
        identity, nilpotent = MODULE.kernel_generators(11)
        self.assertEqual(nilpotent, {15: 1, 158: 1})
        for vector in (identity, nilpotent):
            self.assertTrue(all(sum(value * vector.get(column, 0)
                                    for column, value in row.items()) == 0
                                for row in rows.values()))

    def test_all_family_controls_and_scope(self):
        self.assertEqual([case["b"] for case in self.report["controls"]], [2, 3, 4, 5, 6, 7, 8, 12])
        self.assertEqual(self.report["predecessor_control_comparison"],
                         {"complete_adapted_controls_compared": 8, "all_match": True})
        for case in self.report["controls"]:
            r, m = case["r"], 2 * case["r"] + 1
            self.assertEqual(case["concise_format"], [2 * r - 1, m, m])
            self.assertEqual(case["unit_minor_order"], 2 * m * m - 2)
            self.assertEqual(case["equalizer_kernel_dimension"], 2)
            self.assertEqual(case["border_rank_lower_bound"], m + 1)
            self.assertEqual(case["inherited_border_rank_upper_bound"], 4 * r - 2)
        self.assertFalse(self.report["independent_mathematical_review"])
        self.assertFalse(self.report["whole_residual_border_rank_optimality_claimed"])
        self.assertFalse(self.report["arbitrary_source_map_optimality_claimed"])
        self.assertFalse(self.report["improves_omega"])

    def test_known_minimal_rank_tensors_pass_the_equalizer_condition(self):
        for m in (2, 3, 5):
            diagonal = {(i, i, i): 1 for i in range(m)}
            rank = MODULE.unit_reduce(MODULE.equalizer_rows([m, m, m], diagonal))["order"]
            self.assertEqual(2 * m * m - rank, m)
            # A rectangular first factor: a single identity-matrix slice.
            one_slice = {(0, i, i): 1 for i in range(m)}
            rank = MODULE.unit_reduce(MODULE.equalizer_rows([1, m, m], one_slice))["order"]
            self.assertEqual(2 * m * m - rank, m * m)

    def test_removed_core_coupling_and_false_minor_are_rejected(self):
        shape, tensor = MODULE.canonical_residual(4)
        del tensor[2, 0, 2]
        with self.assertRaises(ArithmeticError):
            MODULE.check_minor(MODULE.equalizer_rows(shape, tensor), self.n6["unit_minor"])
        shape, tensor = MODULE.canonical_residual(4)
        minor = copy.deepcopy(self.n6["unit_minor"])
        minor["columns"][1] = minor["columns"][0]
        with self.assertRaises(ArithmeticError):
            MODULE.check_minor(MODULE.equalizer_rows(shape, tensor), minor)

    def test_changed_family_record_source_hash_and_native_map_are_rejected(self):
        changed = copy.deepcopy(self.report)
        changed["controls"][-1]["equalizer_kernel_dimension"] = 3
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "false-equalizer.json"
            path.write_text(json.dumps(changed))
            with self.assertRaises(ArithmeticError):
                MODULE.verify_saved(path)
        pins = json.loads((PACKAGE / "sources.json").read_text())
        pins["local_sources"][-1]["sha256"] = "0" * 64
        with self.assertRaises(ArithmeticError):
            MODULE.source_pins(ROOT, pins)
        source = json.loads((ROOT / MODULE.PAIRED / "witness.json").read_text())
        case = copy.deepcopy(next(case for case in source["cases"] if case["variant"] == "product-oblique"))
        case["maps"][0][0][0] = 1
        with self.assertRaises(ArithmeticError):
            MODULE.replay_native(ROOT, case)

    def test_invalid_parameters_and_noninteger_coefficients(self):
        for b in (0, 1, -2, True, 4.0, "4"):
            with self.assertRaises(ValueError):
                MODULE.canonical_residual(b)
        for value in (True, 1.0, "1/2"):
            with self.assertRaises(ArithmeticError):
                MODULE.integer(value)


if __name__ == "__main__":
    unittest.main()

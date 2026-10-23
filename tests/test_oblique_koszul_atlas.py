"""Exact all-field ranks and screening scope for the fixed repair tensor."""

import copy
import importlib.util
import json
from math import comb
from pathlib import Path
import tempfile
import unittest

from sympy import Matrix


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-oblique-koszul-atlas"
SPEC = importlib.util.spec_from_file_location("oblique_koszul_atlas", PACKAGE / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ObliqueKoszulAtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = MODULE.verify_saved(PACKAGE / "certificate.json")

    def test_all_degrees_legs_and_native_source(self):
        self.assertEqual(self.report["matrices_reduced"], 75)
        for case in self.report["controls"]:
            shape = case["concise_shape"]
            atlas = case["all_degrees_and_legs"]
            expected = {(leg, p) for leg in range(3) for p in range(shape[leg])}
            self.assertEqual({(r["leg"], r["degree"]) for r in atlas}, expected)
            self.assertEqual(len(atlas), len(expected))
            self.assertTrue(all(r["nonunit_pivots"] == 0 for r in atlas))
        self.assertEqual([c["strongest_full_space_koszul_bound"]
                          for c in self.report["controls"]], [8, 9, 11])
        self.assertEqual([c["inherited_equalizer_lower_bound"]
                          for c in self.report["controls"]], [8, 10, 12])
        native = self.report["native_n6_control"]
        self.assertTrue(native["literal_tensor_and_native_source_equal"])
        self.assertEqual(native["target_coordinates_compared"], 10000)

    def test_unit_rank_agrees_with_independent_small_matrix_rank(self):
        shape, tensor = MODULE.SOURCE.canonical_residual(2)
        for leg in range(3):
            rows, matrix_shape = MODULE.koszul_rows(shape, tensor, leg, 1)
            dense = Matrix(matrix_shape[0], matrix_shape[1],
                           lambda i, j: rows.get(i, {}).get(j, 0))
            self.assertEqual(MODULE.unit_rank(rows)["rank"], dense.rank())

    def test_simple_tensor_divisor_and_direct_diagonal_sums(self):
        for d in range(1, 6):
            for p in range(d):
                tensor = {(0, 0, 0): 1}
                rows, _ = MODULE.koszul_rows([d, 3, 3], tensor, 0, p)
                self.assertEqual(MODULE.unit_rank(rows)["rank"], comb(d - 1, p))
                tensor = {(i % d, i, i): 1 for i in range(3)}
                rows, _ = MODULE.koszul_rows([d, 3, 3], tensor, 0, p)
                self.assertEqual(MODULE.unit_rank(rows)["rank"], 3 * comb(d - 1, p))

    def test_transpose_orientation_at_complementary_degrees(self):
        shape, tensor = MODULE.SOURCE.canonical_residual(2)
        for leg in range(3):
            first, last = [i for i in range(3) if i != leg]
            swapped = {}
            for key, value in tensor.items():
                out = list(key)
                out[first], out[last] = out[last], out[first]
                swapped[tuple(out)] = value
            new_shape = list(shape)
            new_shape[first], new_shape[last] = new_shape[last], new_shape[first]
            for p in range(shape[leg]):
                left, _ = MODULE.koszul_rows(shape, tensor, leg, p)
                right, _ = MODULE.koszul_rows(new_shape, swapped, leg, shape[leg] - 1 - p)
                self.assertEqual(MODULE.unit_rank(left)["rank"],
                                 MODULE.unit_rank(right)["rank"])

    def test_changed_certificate_or_source_is_rejected(self):
        changed = copy.deepcopy(self.report)
        changed["controls"][-1]["all_degrees_and_legs"][4]["rank"] += 1
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "false-atlas.json"
            path.write_text(json.dumps(changed))
            with self.assertRaises(ArithmeticError):
                MODULE.verify_saved(path)
        pins = json.loads((PACKAGE / "sources.json").read_text())
        pins["local_sources"][0]["sha256"] = "0" * 64
        with self.assertRaises(ArithmeticError):
            MODULE.source_pins(pins)

    def test_nonunit_pivot_does_not_claim_an_all_field_rank(self):
        with self.assertRaises(ArithmeticError):
            MODULE.unit_rank({0: {0: 2}})
        self.assertEqual(MODULE.unit_rank({0: {0: -1}, 1: {0: 2}})["rank"], 1)


if __name__ == "__main__":
    unittest.main()

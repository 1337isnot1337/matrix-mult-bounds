"""Exact acceptance and independent characteristic-two controls."""

import copy
import importlib.util
import json
from math import comb
from pathlib import Path
import unittest


PACKAGE = Path(__file__).resolve().parents[1] / "research/ai/2026-10-23-oblique-koszul-atlas"
SPEC = importlib.util.spec_from_file_location("oblique_koszul_atlas", PACKAGE / "verify.py")
ATLAS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ATLAS)


def binary_rank(rows):
    basis = {}
    for row in rows:
        value = sum(1 << column for column, coefficient in row.items() if coefficient % 2)
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return len(basis)


class ObliqueKoszulAtlasTests(unittest.TestCase):
    def test_complete_exact_certificate_and_binary_crosscheck(self):
        saved = json.loads((PACKAGE / "certificate.json").read_text())
        self.assertEqual(ATLAS.certificate(), saved)
        self.assertEqual(len(saved["matrices"]), 112)
        self.assertEqual(saved["best_bounds"], {"3": 8, "4": 9, "5": 11, "6": 13})
        for record in saved["matrices"]:
            tensor, dimensions = ATLAS.residual(record["r"])
            rows, _ = ATLAS.koszul_rows(tensor, dimensions, record["leg"], record["degree"])
            self.assertEqual(binary_rank(rows), record["rank_over_every_field"])

    def test_native_source_identity_and_map_tampering(self):
        witness = json.loads((PACKAGE / "native-witness.json").read_text())
        self.assertEqual(ATLAS.native_residual(witness), ATLAS.embedded_residual(5))
        changed = copy.deepcopy(witness)
        changed["maps"][0][0][2] += 1
        self.assertNotEqual(ATLAS.native_residual(changed), ATLAS.embedded_residual(5))
        witness["maps"].append([])
        with self.assertRaises(ValueError):
            ATLAS.native_residual(witness)

    def test_rank_one_cost_including_both_endpoint_degrees(self):
        dimensions = (4, 3, 5)
        tensor = {(2, 1, 3): 1}
        for leg in range(3):
            for degree in range(dimensions[leg]):
                rows, _ = ATLAS.koszul_rows(tensor, dimensions, leg, degree)
                self.assertEqual(ATLAS.unit_rank(rows)[0], comb(dimensions[leg] - 1, degree))

    def test_signed_wedges_and_external_leg_transpose_duality(self):
        tensor, dimensions = ATLAS.residual(3)
        for leg in range(3):
            other = [i for i in range(3) if i != leg]
            order = list(range(3))
            order[other[0]], order[other[1]] = order[other[1]], order[other[0]]
            swapped = {tuple(indices[k] for k in order): value
                       for indices, value in tensor.items()}
            new_dimensions = tuple(dimensions[k] for k in order)
            for degree in range(dimensions[leg]):
                rows, _ = ATLAS.koszul_rows(tensor, dimensions, leg, degree)
                dual, _ = ATLAS.koszul_rows(swapped, new_dimensions, leg,
                                           dimensions[leg] - degree - 1)
                self.assertEqual(ATLAS.unit_rank(rows)[0], ATLAS.unit_rank(dual)[0])
        # Wedge signs over Z are not replaced by characteristic-two coefficients.
        rows, _ = ATLAS.koszul_rows({(0, 0, 0): 1, (1, 0, 0): 1}, (2, 1, 1), 0, 1)
        self.assertEqual(rows, [{1: 1, 0: -1}])

    def test_nonunit_pivots_are_rejected(self):
        with self.assertRaises(ArithmeticError):
            ATLAS.unit_rank([{0: 2}])
        for r in (2, 3.0, True):
            with self.assertRaises(ValueError):
                ATLAS.residual(r)


if __name__ == "__main__":
    unittest.main()

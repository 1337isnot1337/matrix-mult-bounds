"""Exact lower/upper witnesses and independent weighted/finite-field ranks."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-binomial-biform-ranks"
SPEC = importlib.util.spec_from_file_location("binomial_biform_ranks", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


def modular_rank(matrix, prime):
    data = [[int(value) % prime for value in row] for row in matrix.tolist()]
    rank = 0
    for column in range(matrix.cols):
        pivot = next((i for i in range(rank, matrix.rows) if data[i][column]), None)
        if pivot is None:
            continue
        data[rank], data[pivot] = data[pivot], data[rank]
        inverse = pow(data[rank][column], -1, prime)
        data[rank] = [value*inverse % prime for value in data[rank]]
        for i in range(rank+1, matrix.rows):
            coefficient = data[i][column]
            if coefficient:
                data[i] = [(x-coefficient*y) % prime for x, y in zip(data[i], data[rank])]
        rank += 1
    return rank


class BinomialBiformRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_exported_minor_cover_certificates_and_arithmetic_scope(self):
        self.assertEqual(v.verify(self.record), {
            "exact_minor_cover_cases": 114, "lower_gap_cases": 8555,
            "quotient_remainder_cases": 435, "improves_omega": False})

    def test_independent_weighted_rational_ranks(self):
        for a, u, offset in ((2, 1, 1), (4, 1, 3), (5, 2, 2), (7, 3, 3)):
            for orientation in (0, 1):
                matrix = v.literal_matrix(a, u, offset, orientation, 2, -3)
                self.assertEqual(matrix.to_DM().rank(), v.rank_formula(a, u, offset))

    def test_independent_small_characteristic_ranks(self):
        for prime in (2, 3, 5):
            for a, u, offset in ((2, 1, 1), (4, 1, 3), (5, 2, 2), (6, 2, 3), (7, 3, 3)):
                for orientation in (0, 1):
                    matrix = v.literal_matrix(a, u, offset, orientation, 1, prime-1)
                    self.assertEqual(modular_rank(matrix, prime), v.rank_formula(a, u, offset))

    def test_weighted_selected_minors_are_single_monomials(self):
        alpha, beta = s.symbols("alpha beta")
        for a, u, offset, orientation in ((2, 1, 1, 0), (3, 1, 2, 1)):
            record = next(case for case in self.record["cases"]
                          if (case["a"], case["u"], case["v"], case["orientation"]) ==
                          (a, u, offset, orientation))
            matrix = v.literal_matrix(a, u, offset, orientation, alpha, beta)
            determinant = matrix.extract(record["minor_rows"], record["minor_columns"]).to_DM().det()
            if hasattr(determinant, "as_expr"):
                determinant = determinant.as_expr()
            polynomial = s.Poly(determinant, alpha, beta)
            self.assertEqual(len(polynomial.terms()), 1)
            self.assertIn(polynomial.terms()[0][1], (-1, 1))

    def test_equal_offset_deficits_and_divisor_threshold(self):
        for a, d, rank, deficit in ((4, 2, 24, 0), (5, 2, 34, 1),
                                     (5, 3, 38, 2), (7, 2, 62, 1), (7, 3, 68, 2)):
            self.assertEqual(v.rank_formula(a, d, d), rank)
            self.assertEqual(a*(a+d)-rank, deficit)

    def test_corrupted_covers_minors_scope_and_coverage_are_rejected(self):
        for mutate in (
            lambda case: case["cover_rows"].pop(),
            lambda case: case.update(minor_determinant=2),
            lambda case: case.update(exact_rank=99),
        ):
            bad = copy.deepcopy(self.record["cases"][0])
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify_case(bad)
        for mutate in (
            lambda record: record.update(improves_omega=True),
            lambda record: record.update(theorem_field_scope="C only"),
            lambda record: record["cases"].pop(),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_source_pins_elementary_scope_and_invalid_offsets(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(len(original["source_references"])):
            bad = copy.deepcopy(original)
            bad["source_references"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        bad = copy.deepcopy(original)
        bad["imported_theorems"] = ["unstated classification"]
        with self.assertRaises(ValueError):
            v.check_sources(bad)
        for arguments in ((4, 0, 1), (4, 1, 4)):
            with self.assertRaises(ValueError):
                v.rank_formula(*arguments)


if __name__ == "__main__":
    unittest.main()

"""Exact graded-source, smaller-support and count-budget controls."""
import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-aggregation-families/pruned"
spec = importlib.util.spec_from_file_location("aggregation_pruned", PACKAGE / "verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class AggregationPrunedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = verify.read_source("general22")
        cls.witness = json.loads((PACKAGE / "witness.json").read_text())

    def test_complete_saved_exact_acceptance(self):
        report = verify.build_report()
        self.assertEqual(report, json.loads((PACKAGE / "report.json").read_text()))
        self.assertEqual(sum(row["ordered_mixed_triples"] for row in report["source_acceptance"].values()), 13845)
        self.assertEqual(report["source_acceptance"]["general22"]["class_counts"],
                         {"centered": 8770, "corrected": 884, "diagonal": 22, "positive_grade": 972})
        self.assertTrue(all(row["budget_strictly_above_critical_mass"] for row in report["restricted_profile_samples"]))

    def test_external_source_hash_and_scalar_grades_are_enforced(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "altered.txt"
            path.write_bytes((PACKAGE / "sources/general22.txt").read_bytes() + b"\n")
            with self.assertRaisesRegex(ValueError, "SHA256"):
                verify.read_source("general22", path)
        changed = copy.deepcopy(self.data)
        for row in changed["products"]:
            row["grades"] = [0, 0, 0]
        with self.assertRaisesRegex(ValueError, "nonpositive"):
            verify.verify_grades(changed)
        changed = copy.deepcopy(self.data)
        changed["correction_subsets"].remove([0, 2])
        with self.assertRaisesRegex(ValueError, "nonpositive"):
            verify.verify_grades(changed)

    def test_independent_direct_grid_count(self):
        profiles = self.witness["profiles"]
        polynomial = verify.position_polynomials(self.data, profiles)
        for n in (2, 3):
            direct = verify.direct_grid_count(self.data, profiles, n)
            self.assertEqual(direct["total_positions"], verify.value(polynomial["total_coefficients_in_n_minus_one"], n))
            self.assertEqual(direct["main_positions"], 4*n*(n+1)**4)
            self.assertEqual(direct["correction_positions"],
                             [verify.value(row["coefficients_in_n_minus_one"], n) for row in polynomial["corrections"]])

    def test_featured_all_n_budget_and_classical_threshold(self):
        result = verify.featured_construction(self.data, self.witness)
        self.assertEqual(result["rank_polynomial_coefficients_n"], {"5":4,"4":32,"3":102,"2":158,"1":118,"0":34})
        self.assertEqual(result["classical_minus_pruned_coefficients_after_n_equals_4_plus_u"],
                         {"5":18,"4":328,"3":2266,"2":7066,"1":8570,"0":678})
        self.assertEqual(sum(row["products"] for row in result["matrix_shape_exponent_counts"]), 22)
        self.assertTrue(all(sum(row["A_B_C_exponents"]) == 5 for row in result["matrix_shape_exponent_counts"]))
        changed = copy.deepcopy(self.witness)
        changed["rank_polynomial_coefficients_n"]["0"] -= 1
        with self.assertRaisesRegex(ValueError, "multiplication count"):
            verify.featured_construction(self.data, changed)

    def test_common_support_floor_and_integer_boundary(self):
        for p,d in ((10,6),(13,6),(22,6),(29,9),(106,12),(29,6)):
            self.assertTrue(verify.pruning_floor(p,d)["excluded_for_all_dimensions_with_common_support_condition"])
        self.assertFalse(verify.pruning_floor(30,6)["excluded_for_all_dimensions_with_common_support_condition"])
        interval = verify.mass_interval(self.witness["profiles"], 16)
        self.assertEqual(Fraction(*interval["lower"]), 22*8**5)
        self.assertEqual(interval["lower"], interval["upper"])

    def test_separate_centering_rows_really_escape_the_support_premise(self):
        for n in range(1, 5):
            e = [[int(i == j) for j in range(n)] for i in range(n)] + [[-1]*n, [0]*n]
            d = [[int(i == j) for j in range(n)] for i in range(n)] + [[0]*n, [-1]*n]
            self.assertTrue(all(sum(row[j] for row in matrix) == 0 for matrix in (e,d) for j in range(n)))
            self.assertTrue(all(sum(e[i][j]*d[i][k] for i in range(n+2)) == int(j == k)
                                for j in range(n) for k in range(n)))
            self.assertEqual(sum(bool(any(x)) and bool(any(y)) for x,y in zip(e,d)), n)


if __name__ == "__main__":
    unittest.main()

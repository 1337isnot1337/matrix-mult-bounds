"""Acceptance and tamper controls for the exact 29-product construction."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from tempfile import TemporaryDirectory
from math import comb

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-aggregation-families"


def load_module(stem):
    spec = importlib.util.spec_from_file_location(f"aggregation_{stem}", PACKAGE / f"{stem}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load_module("verify")
evaluate = load_module("evaluate")
evaluate_binary = load_module("evaluate_binary")


class AggregationFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness = json.loads((PACKAGE / "witness_29.json").read_text())
        cls.witness_106 = json.loads((PACKAGE / "witness_106.json").read_text())

    def test_complete_exact_certificate(self):
        result = verify.check_family(self.witness)
        self.assertEqual(result["products"], 29)
        self.assertEqual(result["ordered_mixed_triples"], 24389)
        self.assertEqual(result["off_diagonal_terms_killed_by_centering"], 23072)
        self.assertEqual(result["off_diagonal_terms_killed_by_corrections"], 1288)
        self.assertEqual(result["correction_counts_by_size"], {1: 9, 2: 36, 3: 3})

    def test_external_baseline_and_uniform_cost_improvement(self):
        old = verify.baseline_data(PACKAGE / "baseline_ex28.txt")
        self.assertEqual(verify.check_family(old)["products"], 28)
        result = verify.comparison(self.witness, old)
        self.assertEqual(result["positive_coefficients"], {"9": 1, "8": 9, "7": 7, "6": 32})
        scope = verify.direct_exponent_cost_scope(self.witness)
        self.assertEqual(scope["strict_integer_margin"], 4716973042654866123349)
        self.assertTrue(scope["displayed_budget_cannot_reach_omega_nine_fourths_by_direct_sum_bound"])

    def test_external_source_hash_is_enforced(self):
        self.assertTrue(verify.check_source_hash(PACKAGE / "baseline_ex28.txt")["verified"])
        with TemporaryDirectory() as directory:
            altered = Path(directory) / "changed_baseline.txt"
            altered.write_bytes((PACKAGE / "baseline_ex28.txt").read_bytes() + b"\n# changed\n")
            with self.assertRaisesRegex(ValueError, "SHA256"):
                verify.baseline_data(altered)

    def test_repeated_product_is_rejected(self):
        malformed = copy.deepcopy(self.witness)
        malformed["products"][1] = copy.deepcopy(malformed["products"][0])
        with self.assertRaisesRegex(ValueError, "Repeated coordinate part"):
            verify.check_family(malformed)

    def test_missing_required_correction_is_rejected(self):
        malformed = copy.deepcopy(self.witness)
        malformed["correction_subsets"].remove([1, 3, 4])
        with self.assertRaisesRegex(ValueError, "Uncancelled replicated triple"):
            verify.check_family(malformed)

    def test_understated_cost_is_rejected(self):
        malformed = copy.deepcopy(self.witness)
        malformed["rank_polynomial_coefficients"]["7"] = 35
        with self.assertRaisesRegex(ValueError, "multiplication count"):
            verify.check_family(malformed)

    def test_actual_rank_one_realization_over_prime_field(self):
        result = evaluate.evaluate(self.witness, n=2, modulus=101, seed=20261023)
        self.assertEqual(result["rank_one_contributions_enumerated"], 159651)
        self.assertEqual(result["aggregate_value"], 15)
        self.assertEqual(result["aggregate_value"], result["target_value"])


    def test_106_product_complete_exact_certificate(self):
        result = verify.check_family(self.witness_106)
        self.assertEqual(result["products"], 106)
        self.assertEqual(result["ordered_mixed_triples"], 1191016)
        self.assertEqual(result["off_diagonal_terms_killed_by_centering"], 1166235)
        self.assertEqual(result["off_diagonal_terms_killed_by_corrections"], 24675)
        self.assertEqual(result["correction_counts_by_size"], {1: 12, 2: 66, 3: 139, 4: 5})
        self.assertEqual(len(self.witness_106["correction_subsets"]), 222)

    def test_106_exact_shifted_cost_comparison(self):
        old = verify.baseline_data(PACKAGE / "baseline_ex105.txt", "ex105")
        self.assertEqual(verify.check_family(old)["products"], 105)
        result = verify.comparison(self.witness_106, old)
        self.assertEqual(result["difference_coefficients"], {"12": 1, "11": 12, "10": 66, "9": -1451, "8": -207})
        self.assertEqual(result["shift_x"], 8)
        self.assertEqual(result["shifted_polynomial_coefficients"], {"4": 1, "3": 44, "2": 738, "1": 3957, "0": 2649})
        self.assertEqual(result["strictly_lower_cost_per_output_for_integer_n_at_least"], 7)
        self.assertEqual(7**4 + 12*7**3 + 66*7**2 - 1451*7 - 207, -613)
        self.assertTrue(verify.direct_exponent_cost_scope(self.witness_106)["displayed_budget_cannot_reach_omega_nine_fourths_by_direct_sum_bound"])

    def test_106_full_rank_one_positions_over_f2(self):
        result = evaluate_binary.evaluate(self.witness_106)
        self.assertEqual(result["matrix_dimension"], 16)
        self.assertEqual(result["rank_one_positions_evaluated"], 9323181)
        self.assertEqual(result["nonzero_correction_aggregate_values"], 117)
        self.assertEqual(result["aggregate_value"], result["target_value"])

    def test_all_size_cost_floor_integer_receipt(self):
        report = json.loads((PACKAGE / "cost_floor.json").read_text())
        self.assertEqual([row["N"] for row in report["rows"]], list(range(1, 9)))
        for row in report["rows"]:
            n = row["N"]
            cap = comb(3*n, n)
            left, right = cap**4 * 3**(9*n), 4**(12*n)
            self.assertEqual(row["distinct_part_product_cap"], cap)
            self.assertEqual(row["strict_cost_floor_margin"], right-left)
            self.assertEqual(row["excluded_by_this_cost_floor"], n <= 7)
            threshold = row["minimum_integer_products_above_cost_floor"]
            self.assertLess((threshold-1)**4 * 3**(9*n), right)
            self.assertGreater(threshold**4 * 3**(9*n), right)


if __name__ == "__main__":
    unittest.main()

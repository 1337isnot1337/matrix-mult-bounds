"""Acceptance and tamper controls for the exact 29-product construction."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-aggregation-families"


def load_module(stem):
    spec = importlib.util.spec_from_file_location(f"aggregation_{stem}", PACKAGE / f"{stem}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load_module("verify")
evaluate = load_module("evaluate")


class AggregationFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness = json.loads((PACKAGE / "witness_29.json").read_text())

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


if __name__ == "__main__":
    unittest.main()

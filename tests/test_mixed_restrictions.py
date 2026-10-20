"""Independent exact controls for mixed-target restrictions and degenerations."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from itertools import product

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-20-mixed-restrictions"
RESULTS = ROOT / "results/mixed-restrictions-2026-10-20"


def load(name):
    spec = importlib.util.spec_from_file_location(name, PACKAGE / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


checks = load("check")
collision = load("collision_search")
combinatorics = load("collision_combinatorics")


class MixedRestrictionTests(unittest.TestCase):
    def test_minimum_and_maximum_target_slices(self):
        for m in range(2, 7):
            self.assertEqual(checks.target_slice(m, [1] + [0]*(m-1)).rank(), m)
            center = [int(i == (m-1)//2) for i in range(m)]
            self.assertEqual(checks.target_slice(m, center).rank(), (m+1)**2//4)

    def test_source_slices_and_canonical_cost(self):
        for m in range(2, 7):
            for vector in ([1] + [0]*(m-1), [0]*(m-1) + [1], list(range(1, m+1))):
                self.assertEqual(checks.source_slice(m, 9, vector).rank(), 9)
        self.assertEqual(checks.necessary_length(4), 13)
        self.assertEqual(checks.necessary_length(4, canonical=False), 11)
        self.assertEqual(checks.necessary_length(53), 2757)

    def test_saved_sat_witnesses_without_solver(self):
        for name, count in [("collision-m2-control", 18),
                            ("collision-m3-control", 108), ("collision-m4-B11", 400)]:
            report = json.loads((RESULTS / (name + ".json")).read_text())
            actual = collision.verify_witness(report["witness"])
            self.assertEqual(actual, report["verification"])
            self.assertEqual(actual["coefficients_checked"], count)

    def test_m2_control_requires_a_real_output_collision(self):
        report = json.loads((RESULTS / "collision-m2-control.json").read_text())
        witness = copy.deepcopy(report["witness"])
        self.assertEqual(witness["output_source_indices"][0], [0, 3])
        witness["output_source_indices"][0] = [0]
        with self.assertRaisesRegex(ArithmeticError, "leading coefficient"):
            collision.verify_witness(witness)

    def test_negative_supported_weight_is_rejected(self):
        report = json.loads((RESULTS / "collision-m2-control.json").read_text())
        witness = copy.deepcopy(report["witness"])
        witness["weights"]["x"][0] -= 100
        with self.assertRaises(ArithmeticError):
            collision.verify_witness(witness)

    def test_duplicate_output_coefficient_is_rejected(self):
        report = json.loads((RESULTS / "collision-m2-control.json").read_text())
        witness = copy.deepcopy(report["witness"])
        witness["output_source_indices"][0].append(0)
        with self.assertRaisesRegex(ArithmeticError, "duplicate"):
            collision.verify_witness(witness)

    def test_saved_queries_match_report_hashes(self):
        for path in RESULTS.glob("collision*.json"):
            report = json.loads(path.read_text())
            self.assertEqual(hashlib.sha256(path.with_suffix(".smt2").read_bytes()).hexdigest(),
                             report["query_sha256"])
            self.assertFalse(report["unrestricted_nonexistence_claim"])

    def test_word_gap_lemma_exact_controls(self):
        for alphabet, maximum in [(2, 9), (3, 7)]:
            for n in range(5, maximum+1):
                for word in product(range(alphabet), repeat=n):
                    if not combinatorics.end_exception_word(word):
                        self.assertGreaterEqual(combinatorics.word_defect(word), 2*n-4)

    def test_permutation_classification(self):
        for m in range(6, 9):
            actual = combinatorics.normalized_permutations(m, m-1)
            expected = combinatorics.endpoint_candidates(m)
            self.assertEqual(sorted(actual), sorted(expected))

    def test_witness_output_capacity(self):
        for name in ["collision-m2-control", "collision-m3-control", "collision-m4-B11"]:
            witness = json.loads((RESULTS / (name + ".json")).read_text())["witness"]
            m, B = witness["m"], witness["B"]
            rows = [set(row) for row in witness["output_source_indices"]]
            self.assertEqual(sum(map(len, rows)), len(set.union(*rows)))
            excess = sum(len(row)-1 for row in rows)
            self.assertGreaterEqual(excess, combinatorics.repetition_defect(witness["source_x_indices"]))
            self.assertLessEqual(excess, B+m-1-m*(m+1)//2)

    def test_all_size_endpoint_capacity(self):
        for m in range(10, 300):
            self.assertGreater((m-5)*(m+1)+2, m*(m+1)//2)


if __name__ == "__main__":
    unittest.main()

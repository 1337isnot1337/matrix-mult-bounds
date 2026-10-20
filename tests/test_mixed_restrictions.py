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
quantitative = load("quantitative_capacity")


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
                    defect = combinatorics.word_defect(word)
                    longest = quantitative.longest_constant_run(word)
                    self.assertGreaterEqual(defect, (n-longest)**2//4)
                    if not combinatorics.end_exception_word(word):
                        self.assertGreaterEqual(defect, 2*n-4)

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

    def test_projected_target_integer_matrices(self):
        report = quantitative.run(6)
        self.assertEqual(report["explicit_target_matrix_cases"], 126)
        self.assertEqual(report["explicit_source_matrix_cases"], 63)

    def test_projected_minimum_rank_and_balanced_choice(self):
        for m in range(2, 40):
            for ell in range(1, m+1):
                q = (ell-1)//2
                for p0 in [0, (m-ell)//2, m-ell]:
                    rank = quantitative.projected_target_formula(m, ell, p0, q)
                    self.assertGreaterEqual(rank, ell*m-ell*ell//4)

    def test_exact_overhead_separation(self):
        self.assertLess(675, 676)  # sqrt(3)<26/15, hence kappa>16/15.
        self.assertLess((9*15)**3, 2*(7*16)**3)  # rho_c<16/15.
        self.assertLess(729*4, 686*5)  # rho_c^3<5/4.
        self.assertLess(3*16, 7*7)  # 3-sqrt(3)>5/4.

    def test_nonzero_shared_rescaling_keeps_rank_lower_bound(self):
        import sympy as sp
        for m, ell, p0, q in [(4, 3, 0, 1), (6, 4, 1, 1), (6, 6, 0, 2)]:
            h = ell-1-q
            coefficients = [(-1)**r*(r+2) for r in range(ell)]
            actual = 0
            for u in range(1, m+1):
                v = m+1-u
                matrix = sp.Matrix([
                    [coefficients[r+s] if p0+r+s == a+c else 0
                     for s in range(h+1) for c in range(v)]
                    for r in range(q+1) for a in range(u)])
                actual += matrix.rank()
            self.assertGreaterEqual(actual, quantitative.projected_target_formula(m, ell, p0, q))


if __name__ == "__main__":
    unittest.main()

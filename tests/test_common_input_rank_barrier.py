"""Regression controls for the common-input symmetric-power barrier."""
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "research/ai/2026-10-23-common-input-rank-barrier/verify.py"
spec = importlib.util.spec_from_file_location("common_input_rank_barrier", MODULE)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def block_diagonal(*matrices):
    rows = sum(len(m) for m in matrices)
    cols = sum(len(m[0]) for m in matrices)
    result = [[0] * cols for _ in range(rows)]
    row_offset = col_offset = 0
    for matrix in matrices:
        for i, row in enumerate(matrix):
            result[row_offset+i][col_offset:col_offset+len(row)] = row
        row_offset += len(matrix)
        col_offset += len(matrix[0])
    return result


class CommonInputRankBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = v.report()

    def test_recorded_report_replays_exactly(self):
        recorded = json.loads((ROOT / "results/common-input-rank-barrier-2026-10-23/verification.json").read_text())
        self.assertEqual(self.report, recorded)
        self.assertEqual(self.report["coefficient_matrices"]["matrices"], 160)
        self.assertEqual(self.report["symmetric_curvature"]["rank_decomposition_identities"], 1400)
        self.assertEqual(self.report["heterogeneous_dimension_formats"]["formats_checked"], 6225)

    def test_literal_boundary_and_one_dimensional_maps(self):
        self.assertEqual(v.full_matrix(2, 1, 0), [[0, 1], [1, 0]])
        self.assertEqual(v.determinant(v.full_matrix(2, 1, 0)), -1)
        for b in range(1, 6):
            identity = [[int(i == j) for j in range(b)] for i in range(b)]
            for q in (0, 1, 4):
                self.assertEqual(v.full_matrix(1, b, q), identity)
                self.assertEqual(v.full_matrix(1, b, q, True), identity)
                self.assertEqual(v.block_ranks(1, b, q), (b, b))

    def test_balancing_rejection_uses_literal_integer_matrices(self):
        source = block_diagonal(v.full_matrix(2, 1, 1), v.full_matrix(2, 3, 1))
        target = block_diagonal(v.full_matrix(2, 2, 1), v.full_matrix(2, 2, 1))
        self.assertEqual((len(source), len(source[0])), (12, 12))
        self.assertEqual((len(target), len(target[0])), (12, 12))
        self.assertEqual(v.modular_rank(source), 11)
        self.assertEqual(v.modular_rank(target), 12)
        self.assertEqual(v.balancing_control(2)["phi_rank_gap"], 1)
        self.assertEqual(v.balancing_control(3)["phi_rank_gap"], 4)

    def test_mutated_critical_map_is_not_accepted_as_full_rank(self):
        matrix = v.full_matrix(3, 2, 1)
        self.assertEqual(v.modular_rank(matrix), 12)
        for row in matrix:
            row[0] = 0
        self.assertLess(v.modular_rank(matrix), 12)
        self.assertEqual(v.determinant(matrix), 0)

    def test_exact_radical_normalization_and_certified_signs(self):
        self.assertEqual(v.radical_term(128), v.radical_term(2, 4))
        self.assertEqual(v.radical_term(8), {1: 2})
        for n in range(300):
            root = v.integer_cube_root(n)
            self.assertLessEqual(root**3, n)
            self.assertGreater((root+1)**3, n)
        self.assertEqual(v.radical_sign(v.radical_add(v.radical_term(2),
                                                    v.radical_term(2, -1))), 0)
        self.assertEqual(v.radical_sign(v.radical_add(v.radical_term(5, 3),
                                                    v.radical_term(2, -4))), 1)

    def test_orientation_and_nontrivial_degree_domains(self):
        for a, b, q in ((2, 1, 0), (3, 2, 1), (4, 3, 4)):
            self.assertEqual(v.block_ranks(a, b, q, "mid"),
                             tuple(reversed(v.block_ranks(a, b, q))))
        for bad in (0, -1, True, 1.5, "2"):
            with self.assertRaises(ValueError):
                v.block_ranks(bad, 2, 0)
            with self.assertRaises(ValueError):
                v.block_ranks(2, bad, 0)
        for bad in (-1, True, 1.5, "0"):
            with self.assertRaises(ValueError):
                v.block_ranks(2, 2, bad)
        with self.assertRaises(ValueError):
            v.block_ranks(2, 2, 0, "output")
        with self.assertRaises(ValueError):
            v.balancing_control(1)


if __name__ == "__main__":
    unittest.main()


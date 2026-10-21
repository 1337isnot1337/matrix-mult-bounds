"""Exact checks of a grading allocation; no numerical fit is accepted here."""

import importlib.util
import json
from collections import Counter
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-20-paired-construction"
SPEC = importlib.util.spec_from_file_location("paired_construction_grading", PACKAGE / "graded_search.py")
G = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G)
EXACT_SPEC = importlib.util.spec_from_file_location("paired_construction_exact_p2", PACKAGE / "exact_p2.py")
E = importlib.util.module_from_spec(EXACT_SPEC)
EXACT_SPEC.loader.exec_module(E)
CHAIN_SPEC = importlib.util.spec_from_file_location("paired_construction_chain", PACKAGE / "chain_family.py")
H = importlib.util.module_from_spec(CHAIN_SPEC)
CHAIN_SPEC.loader.exec_module(H)
QUOTIENT_SPEC = importlib.util.spec_from_file_location("paired_construction_quotient", PACKAGE / "quotient_search.py")
Q = importlib.util.module_from_spec(QUOTIENT_SPEC)
QUOTIENT_SPEC.loader.exec_module(Q)


class PairedConstructionTests(unittest.TestCase):
    def test_saved_integer_certificate(self):
        saved = json.loads((PACKAGE / "grading.json").read_text())
        self.assertEqual(G.grade_certificate(), saved)
        self.assertEqual(saved["graded_map_parameter_count"], 3628)
        self.assertFalse(saved["degeneration_constructed"])
        self.assertFalse(saved["improves_omega"])

    def test_source_support_and_target_blocks_independently(self):
        source, sw, st, target, tw, tt = G.coordinates(10, G.example())
        self.assertEqual(list(map(len, source)), [100, 190, 190])
        self.assertEqual(list(map(len, target)), [100, 164, 182])
        self.assertEqual(len(set(st)), 10000)
        self.assertEqual(len(set(tt)), 1160)
        for ia, ib, ic in st:
            p, q = source[0][ia]
            y, j = source[1][ib]
            z, v = source[2][ic]
            self.assertEqual(j, q+v)
            self.assertEqual(z, p+y)
            self.assertEqual(sw[0][ia]+sw[1][ib]+sw[2][ic], 36)
        counts = Counter()
        for ia, ib, ic in tt:
            ba, i, k = target[0][ia]
            bb, ii, j = target[1][ib]
            bc, jj, kk = target[2][ic]
            self.assertEqual((ba, i, j, k), (bb, ii, jj, kk))
            self.assertEqual(ba, bc)
            self.assertEqual(tw[0][ia]+tw[1][ib]+tw[2][ic], 36)
            counts[ba] += 1
        self.assertEqual(counts, {0: 440, 1: 720})

    def test_exact_p2_complete_coefficient_identity(self):
        saved = json.loads((PACKAGE / "exact-p2.json").read_text())
        self.assertEqual(E.certificate(), saved)
        # Rebuild the target coefficient tensor independently, rather than
        # accepting a residual or testing just its eight nonzero entries.
        actual = Counter()
        source_indices = set()
        for contribution in saved["all_source_contributions"]:
            source_indices.add(tuple(contribution["source_indices"]))
            key = tuple(tuple(x) for x in contribution["target_indices"])
            actual[key] += contribution["coefficient"]
        self.assertEqual(len(source_indices), 16)
        for ia in range(4):
            for ib in range(4):
                for ic in range(4):
                    i, k = divmod(ia, 2)
                    ii, j = divmod(ib, 2)
                    jj, kk = divmod(ic, 2)
                    self.assertEqual(actual[((i, k), (ii, j), (jj, kk))],
                                     int(i == ii and j == jj and k == kk))
        self.assertEqual(len(saved["off_support_cancellations"]), 4)
        self.assertTrue(saved["restriction_constructed"])
        self.assertFalse(saved["improves_omega"])

    def test_exact_p2_conventional_product_on_all_basis_pairs(self):
        # Sixteen independent bilinear input pairs determine the full map.
        # The expected answer is ordinary row-by-column multiplication.
        for left_entry in range(4):
            for right_entry in range(4):
                left = [[int(2*i+j == left_entry) for j in range(2)] for i in range(2)]
                right = [[int(2*j+k == right_entry) for k in range(2)] for j in range(2)]
                expected = [[sum(left[i][j]*right[j][k] for j in range(2))
                             for k in range(2)] for i in range(2)]
                self.assertEqual(E.multiply(left, right), expected)
        left, right = [[-7, 13], [4, 9]], [[5, -11], [2, 17]]
        expected = [[-9, 298], [38, 109]]
        self.assertEqual(E.multiply(left, right), expected)
        # The integer identity also survives in characteristic two.
        self.assertEqual([[x % 2 for x in row] for row in E.multiply(left, right)],
                         [[x % 2 for x in row] for row in expected])

    def test_chain_family_all_integer_coefficients(self):
        saved = json.loads((PACKAGE / "chain-family.json").read_text())
        self.assertEqual([H.certificate(a) for a in range(2, 9)], saved)
        self.assertEqual(H.maps(2), E.maps())
        for report in saved:
            a = report["a"]
            self.assertEqual(report["all_target_coefficient_positions_checked"], 4*a**4)
            self.assertTrue(report["restriction_constructed"])
            self.assertFalse(report["improves_omega"])

    def test_chain_family_ordinary_multiplication(self):
        for a in range(2, 9):
            # Independently test the bilinear basis, including transposition.
            for left_entry in range(2*a):
                for right_entry in range(2*a):
                    left = [[int(2*i+j == left_entry) for j in range(2)] for i in range(a)]
                    right = [[int(a*j+k == right_entry) for k in range(a)] for j in range(2)]
                    expected = [[sum(left[i][j]*right[j][k] for j in range(2))
                                 for k in range(a)] for i in range(a)]
                    self.assertEqual(H.multiply(left, right), expected)

    def test_exact_quotient_continuation(self):
        saved = json.loads((PACKAGE / "quotient-continuation.json").read_text())
        actual = [Q.analyze(a) for a in [2, 3, 4, 5]]
        self.assertEqual(actual, saved)
        self.assertEqual([r["middle_mode_dimension"] for r in actual], [3, 2, 2, 2])
        self.assertEqual([r["combined_output_span_rank"] for r in actual], [4, 6, 8, 10])


if __name__ == "__main__":
    unittest.main()

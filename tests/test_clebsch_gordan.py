"""Exact coefficient and interval tests for off-leading recoupling blocks."""
from fractions import Fraction
from pathlib import Path
import sys
import unittest

AI = Path(__file__).resolve().parents[1] / "research/ai"
sys.path.insert(0, str(AI / "2026-10-20-clebsch-gordan"))
import cg_blocks as cg
import cg_search as search


class ClebschGordanTests(unittest.TestCase):
    def test_polarization_quotient(self):
        for p, q in [(1, 1), (2, 3), (4, 2)]:
            basis = cg.equivariant_basis(p, q)
            self.assertEqual(len(basis), (p + 1) * (q + 1))
            for order, degree, poly in basis:
                self.assertEqual(sum(poly.values()), 0 if order else 1)
                self.assertTrue(all(v + w == order + degree for v, w in poly))

    def test_actual_off_leading_square_blocks(self):
        blocks = cg.full_blocks(2, 2, 2, 2)
        self.assertEqual([b["labels"] for b in blocks],
                         [(0, 0, 0), (0, 0, 2), (0, 1, 1), (1, 0, 1), (1, 1, 2)])
        self.assertTrue(all(cg.convolution_isomorphism(b) for b in blocks))

    def test_balanced_parity_selection(self):
        blocks = cg.full_blocks(3, 3, 3, 3)
        self.assertEqual(len(blocks), 14)
        self.assertTrue(all((b["labels"][2] - sum(b["labels"][:2])) % 2 == 0
                            for b in blocks))

    def test_exact_factorization_rejects_corruption(self):
        terms = [(i, j, i + j, Fraction(1)) for i in range(3) for j in range(3)]
        self.assertIsNotNone(cg.convolution_isomorphism({"dims": (3, 3, 5), "terms": terms}))
        bad = [(i, j, k, Fraction(2) if (i, j) == (1, 2) else value)
               for i, j, k, value in terms]
        self.assertIsNone(cg.convolution_isomorphism({"dims": (3, 3, 5), "terms": bad}))

    def test_interior_block_contains_larger_convolution_restriction(self):
        block = next(b for b in cg.full_blocks(3, 3, 3, 3) if b["labels"] == (0, 0, 2))
        self.assertIsNone(cg.convolution_isomorphism(block))
        self.assertEqual(cg.dot_slice_bound(block), 5)
        value, witness = search.coordinate_convolution_bound(tuple(block["dims"]), tuple(block["terms"]))
        self.assertEqual(value, Fraction(56, 9))
        self.assertIsNotNone(witness)

    def test_integer_cube_roots(self):
        for n in [0, 1, 2, 7, 8, 9, 10**80 + 1, (2**123 + 5)**3 - 1]:
            r = search.cuberoot(n)
            self.assertLessEqual(r**3, n)
            self.assertGreater((r + 1)**3, n)

    def test_direct_sum_interval_contains_exact_power(self):
        bits = 80
        q = 1 << bits
        lower, upper = search.direct_sum_interval([(q, q), (q, q)], bits)
        self.assertLessEqual(lower**3, 16 * q**3)
        self.assertGreaterEqual(upper**3, 16 * q**3)

    def test_small_completed_search(self):
        result = search.search_source((2, 2, 2, 2))
        self.assertEqual(result["distinct_scored_supports"], 31)
        self.assertEqual(result["violations"], [])
        self.assertEqual(result["unresolved_interval_comparisons"], [])

    def test_uniform_scalar_tight_certificates(self):
        for dims in [(2, 2, 2, 2), (3, 3, 3, 3), (2, 3, 3, 2)]:
            for block in cg.full_blocks(*dims):
                certificate = cg.tight_uniform_certificate(block)
                self.assertEqual(sum(map(Fraction, certificate["probabilities"])), 1)
                self.assertEqual(certificate["asymptotic_subrank"], min(block["dims"]))

    def test_uniform_certificate_rejects_corruption(self):
        block = next(b for b in cg.full_blocks(3, 3, 3, 3) if b["labels"] == (0, 0, 2))
        bad = dict(block)
        bad["terms"] = list(block["terms"])
        i, j, k, value = bad["terms"][0]
        bad["terms"][0] = (i, j, k, 2 * value)
        with self.assertRaises(ArithmeticError):
            cg.tight_uniform_certificate(bad)


if __name__ == "__main__":
    unittest.main()

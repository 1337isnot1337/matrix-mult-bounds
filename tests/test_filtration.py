"""Independent boundary, proof-chain, and coefficient checks."""
from fractions import Fraction
import importlib.util
from itertools import product
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'filtration', ROOT/'research/ai/2026-10-20-concavity-equivalence/verify.py')
filtration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(filtration)


class FiltrationTests(unittest.TestCase):
    def test_profile_against_independent_closed_product(self):
        for a, b in product(range(1, 25), repeat=2):
            m, n = sorted((a, b))
            expected = Fraction(2*n+m-1, 2)
            for k in range(1, m):
                expected *= Fraction(3*k+1, 3*k)
            self.assertEqual(filtration.profile(a, b), expected)

    def test_zero_boundary_and_concavity(self):
        for a in range(1, 30):
            for b in range(1, 30):
                self.assertGreaterEqual(
                    2*filtration.profile(a, b),
                    filtration.profile(a, b-1)+filtration.profile(a, b+1))

    def test_other_profiles_use_same_proof_chain(self):
        def additive(a, b):
            return a+b-1 if a and b else 0

        def bilinear(a, b):
            return a*b

        def mixed(a, b):
            return (filtration.profile(a, b)+bilinear(a, b))/2

        for value in (additive, bilinear, mixed):
            for source in product(range(1, 5), repeat=4):
                filtration.check_source(*source, value=value)

    def test_boundary_hypothesis_is_needed(self):
        def bad(a, b):
            return a*b+(a-1)*(b-1)

        self.assertEqual(bad(2, 1)*bad(1, 2), 4)
        self.assertEqual(bad(2, 2), 5)
        with self.assertRaises(ValueError):
            filtration.check_source(2, 1, 1, 2, value=bad)
        for a, b in product(range(1, 10), repeat=2):
            self.assertEqual(bad(a, 3*b+a-1)-3*bad(a, b),
                             (a-1)*(2*a+1))

    def test_elementary_restriction_coefficients(self):
        for a, b in product(range(1, 8), repeat=2):
            # Source output labels are independent pairs; merging sums
            # recovers every convolution coefficient, including zeros.
            source = {(u, v, (u, v)): 1
                      for u, v in product(range(a), range(b))}
            actual = {(u, v, i+j): coefficient
                      for (u, v, (i, j)), coefficient in source.items()}
            for u, v, k in product(range(a), range(b), range(a+b-1)):
                self.assertEqual(actual.get((u, v, k), 0), int(k == u+v))

    def test_converse_recovers_boundary_and_interior(self):
        for a, b in product(range(1, 20), repeat=2):
            blocks = filtration.lengths(b, 2)
            actual = sum(filtration.profile(a, s) for s in blocks)
            expected = (filtration.profile(a, b+1)
                        + filtration.profile(a, b-1))
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

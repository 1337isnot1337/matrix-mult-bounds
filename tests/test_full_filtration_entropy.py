"""Independent checks of rational all-distribution and all-size certificates."""
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT/'research/ai/2026-10-20-full-filtration/entropy_certificate.py'
spec = importlib.util.spec_from_file_location('full_filtration_entropy', PATH)
entropy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(entropy)


class FullFiltrationEntropyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT/'results/full-filtration-2026-10-20/'
                                'entropy_certificate.json').read_text())

    def test_square_root_enclosures_and_domains(self):
        for value in [Q(0),Q(1),Q(4,9),Q(2),Q(7,13),entropy.h(43)**3]:
            lo, hi = entropy.sqrt_interval(value, 10**12)
            self.assertLessEqual(lo*lo, value)
            self.assertGreaterEqual(hi*hi, value)
            self.assertLessEqual(hi-lo, Q(1,10**12))
        self.assertEqual(entropy.sqrt_interval(Q(9,4), 100), (Q(3,2),Q(3,2)))
        with self.assertRaises(ValueError): entropy.sqrt_interval(Q(-1), 100)
        with self.assertRaises(ValueError): entropy.sqrt_interval(Q(2), 0)
        with self.assertRaises(ValueError): entropy.h(0)

    def test_generic_certificate_rejects_false_or_malformed_inputs(self):
        check = entropy.verify_probability_certificate
        values = [[Q(1),Q(1)],[Q(1),Q(1)]]
        u = [Q(1,2),Q(1,2)]
        self.assertTrue(check(values, u, u, Q(3)))
        # Uniform q gives score 2**(4/3)>2, so C=2 must fail.
        self.assertFalse(check(values, u, u, Q(2)))
        self.assertFalse(check(values, [Q(1),Q(1)], u, Q(10)))
        self.assertFalse(check(values, [Q(0),Q(1)], u, Q(10)))
        self.assertFalse(check(values[:-1], u, u, Q(10)))
        self.assertFalse(check(values, u, u, Q(0)))

    def test_small_size_probability_certificates_directly(self):
        # This uses the exported probability witnesses and individual block
        # values, bypassing the R-monotonicity and summed-root upper bound.
        entries = self.report['balanced_all_size_certificate']['small_sizes']
        self.assertEqual([r['n'] for r in entries], list(range(2,23)))
        count = 0
        for row in entries:
            n = row['n']
            u = list(map(Q, row['marginal_probabilities']))
            self.assertEqual(sum(u), 1)
            self.assertTrue(all(v>0 for v in u))
            C = Q(39,40)*entropy.profile(n,n)**2
            for i in range(n):
                for j in range(n):
                    value = entropy.profile(2*n-1-2*i,2*n-1-2*j)
                    self.assertLessEqual(value**3, C**3*(u[i]*u[j])**2)
                    count += 1
        self.assertEqual(count, 3794)

    def test_tail_identity_independently_expanded(self):
        x = sp.symbols('x')
        n = x+23
        polynomial = sp.Poly(sp.expand(
            39**3*12*n*(3*n-1)**7*(2*n-1)**2
            -40**3*(6*n-4)**4*(2*n+1)**6),x)
        independent = [int(polynomial.nth(k)) for k in range(11)]
        saved = self.report['balanced_all_size_certificate'][
            'tail_polynomial_coefficients_ascending']
        self.assertEqual(independent, saved)
        self.assertEqual(independent, entropy.tail_polynomial())
        self.assertTrue(all(c>0 for c in independent))

    def test_recurrence_identities_symbolically(self):
        r = sp.symbols('r', positive=True)
        self.assertEqual(sp.factor((1+1/(3*r))**3-(1+1/r)),
                         (9*r+1)/(27*r**3))
        self.assertEqual(sp.expand(27*r**3*(3*r+2)-(3*r+1)**3*(3*r-1)),6*r+1)

    def test_exact_report_replays_entire_source_grid(self):
        regenerated = entropy.report(self.report['max_size'], self.report['scale'])
        self.assertEqual(regenerated, self.report)
        self.assertEqual(regenerated['source_quadruples'], 20736)
        self.assertEqual(regenerated['exact_upper_certificates_passed'], 20736)
        self.assertEqual(regenerated['failed_upper_certificates'], [])
        self.assertEqual(regenerated['singleton_marginal_cases'],6095)
        self.assertEqual(regenerated['worst_nontrivial']['source'],[2,2,2,2])


if __name__ == '__main__': unittest.main()

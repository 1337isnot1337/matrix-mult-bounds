"""Independent exact ranks, polynomial covariance, and rejection controls."""
import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as s
from sympy.polys.domains import GF
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-elementary-biform-gap'
RESULTS = ROOT / 'results/elementary-biform-gap-2026-10-23'
spec = importlib.util.spec_from_file_location('elementary_biform_verify', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)
x, z = s.symbols('x z')


def coefficients(polynomial):
    return dict(s.Poly(s.expand(polynomial), x, z).terms())


def independent_matrix(a, b, polynomial):
    """Build columns by multiplying f by Laurent monomials, then extracting."""
    width = a+b-1
    # The coefficient of x^H z^(-r) in f*x^j*z^(-L) is the crossed entry.
    rows = []
    for j in range(b):
        for ell in range(width):
            shifted = s.Poly(s.expand(polynomial*x**j), x, z)
            rows.append([shifted.coeff_monomial(x**h*z**(ell-r)) if ell >= r else 0
                         for h in range(width) for r in range(a)])
    return s.Matrix(rows)


class ElementaryBiformGapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / 'certificate.json').read_text())

    def test_complete_acceptance_and_saved_report(self):
        report = verify.verify(self.certificate)
        self.assertEqual(report, json.loads((RESULTS / 'verification.json').read_text()))
        self.assertEqual(report['power_cases'], 45)
        self.assertEqual(report['positive_integer_minors'], 525)
        self.assertFalse(report['independent_review'])
        self.assertFalse(report['improves_omega'])

    def test_every_exported_minor_with_separate_symbolic_backend(self):
        count = 0
        for case in self.certificate['cases']:
            a, b, e = case['a'], case['b'], case['e']
            matrix = independent_matrix(a, b, (x+z)**e)
            for block in case['blocks']:
                minor = matrix.extract(block['rows'], block['columns'])
                self.assertEqual(minor.det(method='domain-ge'), block['determinant'])
                count += 1
        self.assertEqual(count, 525)

    def test_literal_full_ranks_and_weighted_powers(self):
        for a in range(2, 5):
            for b in [a, a+1]:
                for e in range(1, a):
                    matrix = independent_matrix(a, b, (2*x-3*z)**e)
                    self.assertEqual(matrix, s.Matrix(verify.literal_matrix(
                        a, b, verify.power_coefficients(e, 2, -3))))
                    self.assertEqual(DomainMatrix.from_Matrix(matrix).rank(), a*(b+e))

    def test_covariance_with_symbolic_arbitrary_coefficients(self):
        a, b = 2, 3
        width = a+b-1
        fs = s.symbols('f0:6')
        polynomial = sum(fs[i*b+j]*x**i*z**j for i in range(a) for j in range(b))
        c, d = Fraction(2, 3), Fraction(-3, 2)
        left = s.kronecker_product(s.Matrix(verify.translation(b, -c)).T,
                                   s.Matrix(verify.translation(width, d)))
        right = s.kronecker_product(s.Matrix(verify.translation(width, c)).T,
                                    s.Matrix(verify.translation(a, -d)))
        shifted = s.expand(polynomial.subs({x: x+c, z: z+d}, simultaneous=True))
        difference = independent_matrix(a, b, shifted)-left*independent_matrix(a, b, polynomial)*right
        self.assertTrue(all(s.expand(value) == 0 for value in difference))

    def test_repeated_mixed_factor_limits_and_rank_bounds(self):
        for e in range(1, 4):
            a, b = e+2, e+3
            polynomial = s.expand((x+z+x*z)**e*(1+2*x)*(1+3*z))
            lowest = sum(value*x**i*z**j for (i, j), value in coefficients(polynomial).items()
                         if i+j == e)
            self.assertEqual(s.expand(lowest-(x+z)**e), 0)
            matrix = independent_matrix(a, b, polynomial)
            self.assertGreaterEqual(DomainMatrix.from_Matrix(matrix).rank(), a*(b+e))
        for e in [1, 2]:
            a = b = e+2
            polynomial = (x*z-1)**e*(x+2)*(z+3)
            shifted = s.expand(polynomial.subs({x: x+1, z: z+1}, simultaneous=True))
            lowest = sum(value*x**i*z**j for (i, j), value in coefficients(shifted).items()
                         if i+j == e)
            self.assertEqual(s.expand(lowest-12*(x+z)**e), 0)
            self.assertGreaterEqual(DomainMatrix.from_Matrix(
                independent_matrix(a, b, polynomial)).rank(), a*(b+e))

    def test_sharp_gap_separable_cases_and_characteristic_boundary(self):
        for a, b in [(2, 2), (2, 4), (3, 3), (3, 5), (4, 4)]:
            polynomial = sum((i+1)*x**i for i in range(a))*sum((-2)**j*z**j for j in range(b))
            self.assertEqual(DomainMatrix.from_Matrix(independent_matrix(a, b, polynomial)).rank(), a*b)
            self.assertEqual(DomainMatrix.from_Matrix(independent_matrix(a, b, x+z)).rank(), a*b+a)
        matrix = independent_matrix(3, 3, (x+z)**2)
        self.assertEqual(DomainMatrix.from_Matrix(matrix).rank(), 15)
        self.assertEqual(DomainMatrix.from_Matrix(matrix).convert_to(GF(2)).rank(), 14)

    def test_corrupted_inventory_minors_and_source_scope_are_rejected(self):
        for mutation in ['missing', 'duplicate', 'determinant', 'row', 'field']:
            bad = copy.deepcopy(self.certificate)
            if mutation == 'missing':
                bad['cases'].pop()
            elif mutation == 'duplicate':
                bad['cases'].append(copy.deepcopy(bad['cases'][0]))
            elif mutation == 'determinant':
                bad['cases'][0]['blocks'][0]['determinant'] += 1
            elif mutation == 'row':
                bad['cases'][0]['blocks'][0]['rows'][0] += 1
            else:
                bad['field'] = 'every field'
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                verify.check_certificate(bad)
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for mutation in ['digest', 'inventory', 'scope', 'attribution']:
            bad = copy.deepcopy(sources)
            if mutation == 'digest':
                bad['source_references'][0]['sha256'] = '0'*64
            elif mutation == 'inventory':
                bad['source_references'].pop()
            elif mutation == 'scope':
                bad['field'] = 'every field'
            else:
                bad['external_references'][0]['sha256'] = '0'*64
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                verify.check_sources(bad)


if __name__ == '__main__':
    unittest.main()

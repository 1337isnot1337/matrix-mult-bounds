"""Exact full-tangent identities and exceptional-characteristic boundaries."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-24-quadratic-equality'
SPEC = importlib.util.spec_from_file_location('quadratic_equality', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class QuadraticEqualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved = json.loads((ROOT / 'results/quadratic-equality-2026-10-24/controls.json').read_text())
        cls.forms, cls.tracefree, _ = verify.symbolic_checks()

    def test_complete_report_and_retained_characteristic_boundaries(self):
        self.assertEqual(verify.report(), self.saved)
        self.assertEqual(self.saved['finite_control_count'], 5)
        self.assertFalse(self.saved['independent_review'])
        self.assertFalse(self.saved['improves_omega'])
        records = self.saved['odd_prime_controls']
        self.assertEqual([(r['prime'], r['tangent_rank']) for r in records],
                         [(3, 5), (5, 7), (5, 7), (7, 5), (13, 6)])
        self.assertEqual([(r['four_block_rank'], r['C_block_rank'])
                          for r in records if r['prime'] in (3, 7)], [(4, 1), (2, 3)])

    def test_exact_inverse_curve_matches_quadratic_coefficient(self):
        # Direct rational inversion of one complete curve, independent of the
        # verifier's truncated inverse and column-coefficient extraction.
        t = sp.Symbol('t')
        Q = sp.diag(2, 1, 1)
        F = sp.Matrix([[1, 1, 2], [0, 2, 0], [0, 0, 0]])
        inverse = (sp.eye(3)+t*F).inv()
        Qt = inverse.T*Q*inverse
        phi = sp.cancel((2*Qt-sp.trace(Qt)*sp.eye(3)).det())
        numerator, denominator = sp.fraction(phi)
        n = sp.Poly(numerator, t)
        self.assertEqual(n.nth(0), 0)
        self.assertEqual(n.nth(1), 0)
        actual = n.nth(2)/denominator.subs(t, 0)
        f = self.forms
        sub = {f['u']: 1, f['v']: 0, f['w']: 1}
        sub.update(dict(zip(f['F'], F)))
        expected = (4*f['d']*(f['qc']+f['q4'])).subs(sub)
        self.assertEqual(actual, expected)

    def test_wrong_off_diagonal_coefficient_is_rejected(self):
        broken = verify.tangent_forms()
        broken['q4'] += 2*(broken['p'].T*broken['B']*broken['q'])[0]
        with patch.object(verify, 'tangent_forms', return_value=broken):
            with self.assertRaisesRegex(ArithmeticError, 'tangent quadratic coefficient'):
                verify.symbolic_checks()

    def test_nonsemisimple_control_is_not_diagonalized(self):
        B = sp.Matrix([[1, 1], [1, 0]])
        nilpotent = B-3*sp.eye(2)
        self.assertNotEqual(nilpotent.applyfunc(lambda x: x % 5), sp.zeros(2))
        self.assertEqual((nilpotent**2).applyfunc(lambda x: x % 5), sp.zeros(2))
        record = verify.finite_control(self.forms, self.tracefree, 5, (1, 1, 0))
        self.assertEqual(record['tangent_rank'], 7)

    def test_excluded_denominators_and_characteristic_two_rejected(self):
        for values in ((1, 0, -1), (1, 1, 1)):
            with self.assertRaisesRegex(ValueError, 'mu and d'):
                verify.finite_control(self.forms, self.tracefree, 5, values)
        with self.assertRaisesRegex(ValueError, 'odd prime'):
            verify.rank_mod(sp.eye(2), 2)
        with self.assertRaisesRegex(ValueError, 'denominators'):
            verify.rank_mod(sp.Matrix([[sp.Rational(1, 3)]]), 3)

    def test_exact_rank_does_not_truncate_large_integers(self):
        large = 10**30
        matrix = sp.Matrix([[large, large+1], [large+1, large+2]])
        self.assertEqual(verify.rank_mod(matrix, 7), 2)
        self.assertEqual(verify.rank_mod(sp.Matrix([[large, large+1],
                                                  [2*large, 2*(large+1)]]), 7), 1)

    def test_source_pins(self):
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for entry in sources['local_dependencies']:
            self.assertEqual(hashlib.sha256((ROOT / entry['path']).read_bytes()).hexdigest(),
                             entry['sha256'])
        self.assertEqual(sources['base_commit'], '4c34716c94c52d8bc2886d49ea8edab4fab91463')
        self.assertFalse(sources['independent_review'])

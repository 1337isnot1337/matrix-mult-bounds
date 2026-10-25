"""Certificate regressions for the sharp characteristic-two bound."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-quadratic-char2-sharp-three'
SPEC = importlib.util.spec_from_file_location('char2_sharp_three', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class CharacteristicTwoSharpThreeTests(unittest.TestCase):
    def test_report_replay_and_scope(self):
        saved = json.loads((ROOT / 'results/quadratic-char2-sharp-three-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(), saved)
        self.assertEqual(saved['upper_bound_characteristic_two'], 3)
        self.assertEqual(saved['lower_bound_from_pinned_construction'], 3)
        self.assertTrue(saved['middle_rank_one_case_checked'])
        for key in ('classifies_attaining_three_spaces', 'computer_certifies_geometric_proof',
                    'independent_review', 'lean_formalized', 'improves_omega'):
            self.assertFalse(saved[key])

    def test_rank_one_three_space_requires_separate_case(self):
        a, d, g = sp.symbols('a d g')
        M = sp.Matrix([[a, 0, 0], [d, 0, 0], [g, 0, 0]])
        basis = [M.diff(x) for x in (a, d, g)]
        self.assertEqual(sp.Matrix.hstack(*[B.reshape(9, 1) for B in basis]).rank(), 3)
        for rows in itertools.combinations(range(3), 2):
            for cols in itertools.combinations(range(3), 2):
                self.assertEqual(M.extract(rows, cols).det(), 0)
        self.assertEqual(M.subs({a: 1, d: 0, g: 0}).rank(), 1)

    def test_rank_one_obstruction_dropped_f0_is_rejected(self):
        original = verify.middle_rank_one_residuals
        def broken(b0, c0, f0, h0, i0):
            residuals = original(b0, c0, f0, h0, i0)
            residuals[1] -= f0
            return residuals
        with patch.object(verify, 'middle_rank_one_residuals', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'middle rank-one coefficient comparison'):
                verify.report()

    def test_missing_adjugate_term_is_rejected(self):
        original = verify.adjugate_form
        with patch.object(verify, 'adjugate_form', side_effect=lambda N: original(N)-N[0, 0]*N[2, 2]):
            with self.assertRaisesRegex(ArithmeticError, 'full adjugate identity'):
                verify.report()

    def test_missing_free_c_quartic_term_is_rejected(self):
        original = verify.invariants
        def broken(M):
            D, A, T = original(M)
            return D, A, T-M[0, 0]*M[0, 2]*M[2, 1]**2
        with patch.object(verify, 'invariants', side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError, 'full adjugate identity'):
                verify.report()

    def test_primitive_identity_with_independent_cofactors(self):
        x, y, z = sp.symbols('x y z')
        Alt = sp.Matrix([[0, z, y], [z, 0, x], [y, x, 0]])
        P = sp.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]])
        Q = sp.Matrix([[1, 0, 0], [1, 1, 0], [0, 1, 1]])
        M = P*Alt*Q
        cofactors = sp.Matrix(3, 3, lambda i, j: (-1)**(i+j)*M.minor_submatrix(j, i).det())
        lhs = verify.adjugate_form(cofactors)
        expected = verify.conic(Q.inv()*sp.Matrix([x, y, z]))*verify.conic(P.inv().T*sp.Matrix([x, y, z]))
        self.assertEqual(verify.mod2(lhs-expected), 0)
        self.assertNotEqual(verify.mod2(lhs), 0)

    def test_source_pins_and_corruption(self):
        sources = verify.check_pins()
        self.assertEqual(sources['base_commit'], '0290bdc043b028f58b638c70183dfa52fc82fe2f')
        sources['local_dependencies'][0]['sha256'] = '0'*64
        with patch.object(verify.json, 'loads', return_value=sources):
            with self.assertRaisesRegex(ArithmeticError, 'source pin:'):
                verify.check_pins()


if __name__ == '__main__':
    unittest.main()

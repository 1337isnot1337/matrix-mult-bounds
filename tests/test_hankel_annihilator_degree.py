"""Independent finite kernel counts and literal degree-bound controls."""

import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-hankel-annihilator-degree'
spec = importlib.util.spec_from_file_location('hankel_degree', PACKAGE/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class HankelAnnihilatorDegreeTests(unittest.TestCase):
    def test_saved_literal_reports(self):
        expected = json.loads((ROOT/'results/hankel-annihilator-degree-2026-10-23/controls.json').read_text())
        self.assertEqual(v.report(), expected)
        self.assertEqual(len(expected['balanced_sharpness_controls']), 15)
        self.assertEqual(len(expected['unbalanced_and_higher_degree_controls']), 7)
        self.assertEqual(len(expected['two_variable_controls']), 2)
        self.assertFalse(expected['independent_review'])
        self.assertFalse(expected['improves_omega'])

    def test_kernel_cutoff_at_the_primitive_degree(self):
        # A 5-by-5 rank-four symbol with primitive kernel (-t^2,0,0,0,1).
        # Count bounded-degree polynomial kernel vectors via direct rational
        # coefficient systems, including input lengths at/below degree two.
        t = sp.symbols('t')
        f = [1, 0, 0, 0, t**2, 0, 0, 0, t**4]
        H = sp.Matrix(5, 5, lambda i, j: f[i+j])
        self.assertEqual(H.rank(), 4)
        for T in range(1, 5):
            blocks = sp.zeros(5*(T+4), 5*T)
            for k in range(T):
                for i in range(5):
                    for j in range(5):
                        for e in range(5):
                            blocks[5*(k+e)+i, 5*k+j] = sp.Poly(H[i, j], t).nth(e)
            self.assertEqual(5*T-blocks.rank(), max(T-2, 0))

    def test_primitive_degree_ignores_rational_scalar_and_denominators(self):
        x, z = v.X, v.Z
        q = [-x**2, 0, 0, 1]
        for factor in [1, (x+1)*(z+1), (z+2)/(x**3+1)]:
            scaled = [c*factor for c in q]
            self.assertEqual(v.primitive_degree(scaled, x, z), 2)
            self.assertEqual(v.primitive_degree(scaled, z, x), 0)
        self.assertEqual(v.primitive_degree([-(1+z), 0, 1+x], x, z), 1)
        self.assertEqual(v.primitive_degree([-(1+z), 0, 1+x], z, x), 1)

    def test_rejects_invalid_source_degree_or_declared_support_degree(self):
        with self.assertRaises(ValueError):
            v.monomial_sequence(3, 3, 2, v.X, 2)
        with self.assertRaises(ArithmeticError):
            v.control('incorrect-degree', [1, 0, v.X, 0, v.X**2], 3, 3, 2, 0, 0)


if __name__ == '__main__':
    unittest.main()

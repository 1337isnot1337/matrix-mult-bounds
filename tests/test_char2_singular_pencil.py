"""Exact polynomial pencil conditions and proof-boundary regression checks."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-25-char2-singular-pencil'
SPEC = importlib.util.spec_from_file_location('singular_pencil', PACKAGE / 'verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class SingularPencilTests(unittest.TestCase):
    def test_complete_census_and_saved_report(self):
        saved=json.loads((ROOT/'results/char2-singular-pencil-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(),saved)
        self.assertEqual(saved['census']['all_two_spaces'],43435)
        self.assertEqual(saved['census']['singular_T4_zero'],3623)
        self.assertEqual(sum(saved['census']['common_kernel_dimensions'].values()),3623)
        for key in ('finite_census_is_arbitrary_field_proof',
                    'computer_certifies_UFD_factorization_or_degree_argument',
                    'complete_char2_attainer_classification','independent_review',
                    'lean_formalized','improves_omega'):
            self.assertFalse(saved[key])

    def test_polynomial_product_matches_coefficient_convolution(self):
        for a in range(32):
            for b in range(32):
                out=[0]*9
                for i in range(5):
                    for j in range(5):
                        out[i+j]^=((a>>i)&1)*((b>>j)&1)
                self.assertEqual(verify.mul(a,b),sum(v<<i for i,v in enumerate(out)))

    def test_pointwise_hypothesis_does_not_suffice(self):
        trap=verify.pointwise_trap()
        self.assertTrue(trap['vanishes_at_all_GF2_projective_points'])
        self.assertFalse(trap['polynomial_T4_zero'])
        self.assertEqual(trap['common_kernel_dimensions'],[0,0])
        s,t=sp.symbols('s t')
        M=sp.Matrix([[0,s+t,0],[s,0,t],[0,t,0]])
        A=M.subs({s:1,t:0});B=M.subs({s:0,t:1})
        # Unit minors certify both stacked systems have rank three over GF2.
        right=sp.Matrix.vstack(A,B);left=sp.Matrix.vstack(A.T,B.T)
        self.assertEqual(abs(right.extract([0,1,4],[0,1,2]).det()),1)
        self.assertEqual(abs(left.extract([0,1,4],[0,1,2]).det()),1)

    def test_omitted_adjugate_term_is_rejected(self):
        original=verify.adjugate_form
        with patch.object(verify,'adjugate_form',side_effect=lambda N: original(N)-N[1,1]**2):
            with self.assertRaisesRegex(ArithmeticError,'literal adjugate identity'):
                verify.adjugate_controls()

    def test_wrong_conic_is_rejected(self):
        with patch.object(verify,'conic',side_effect=lambda u:u[1]**2):
            with self.assertRaisesRegex(ArithmeticError,'rank-one conic factorization'):
                verify.adjugate_controls()

    def test_polynomial_encoding_corruption_is_rejected(self):
        original=verify.inv
        def broken(entries):
            D,T=original(entries)
            return D,T^1
        with patch.object(verify,'inv',side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError,'literal polynomial encoding'):
                verify.symbolic_controls()

    def test_source_pin_corruption_is_rejected(self):
        sources=verify.check_pins();target=ROOT/sources['local_dependencies'][0]['path']
        original=Path.read_bytes
        def corrupted(path):
            return original(path)+(b'corrupt' if path==target else b'')
        with patch.object(Path,'read_bytes',new=corrupted):
            with self.assertRaisesRegex(ArithmeticError,'source pin'):
                verify.check_pins()


if __name__=='__main__':
    unittest.main()

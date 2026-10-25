"""Regression guards for the characteristic-two geometric classification."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-25-char2-attainer-classification'
SPEC=importlib.util.spec_from_file_location('char2_attainers',PACKAGE/'verify.py')
verify=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class Char2AttainerClassificationTests(unittest.TestCase):
    def test_saved_report_and_geometric_scope(self):
        saved=json.loads((ROOT/'results/char2-attainer-classification-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(),saved)
        self.assertEqual(saved['written_geometric_representatives'],['P','N','V'])
        for key in ('computer_certifies_geometric_exhaustion','arbitrary_ground_field_forms_classified',
                    'independent_review','lean_formalized','improves_omega'):
            self.assertFalse(saved[key])

    def test_quartic_term_omission_is_rejected(self):
        original=verify.quartic
        with patch.object(verify,'quartic',side_effect=lambda e:original(e)-e[0]*e[5]**2*e[6]):
            with self.assertRaisesRegex(ArithmeticError,'quartic extension coefficient'):
                verify.extension_controls()

    def test_family_coefficient_error_is_rejected(self):
        original=verify.family
        def broken(L,J):
            F=original(L,J);F[0,2]+=verify.t
            return F
        with patch.object(verify,'family',side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError,'normalized family invariant identities'):
                verify.extension_controls()

    def test_wrong_action_transpose_is_rejected(self):
        original=verify.binary_action
        with patch.object(verify,'binary_action',side_effect=lambda *a:original(*a).T):
            with self.assertRaisesRegex(ArithmeticError,'stabilizer orientation'):
                verify.stabilizer_controls()

    def test_wrong_syzygy_is_rejected(self):
        original=verify.pencil
        def broken(x,y):
            K=original(x,y);K[2,0]=x
            return K
        with patch.object(verify,'pencil',side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError,'moving pencil syzygies'):
                verify.syzygy_controls()

    def test_eta_locus_and_ground_field_are_not_collapsed(self):
        controls=verify.branch_and_field_controls()
        self.assertTrue(controls['fixed_eta_witness_is_P_transpose'])
        self.assertEqual(controls['section_kernel_dimensions_right_left']['P'],[1,1])
        self.assertEqual(controls['section_kernel_dimensions_right_left']['V'],[1,0])
        self.assertEqual(controls['GF2_invertible_matrix_counts'],{'0,0':1,'1,1':3})
        # A nonunit symbolic determinant exposes the missing action scalar.
        w=sp.symbols('w',nonzero=True);x,y=verify.x,verify.y
        transformed_q=(x/w)*y
        self.assertNotEqual(sp.expand(transformed_q-x*y),0)
        self.assertEqual(sp.expand(w*transformed_q-x*y),0)

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

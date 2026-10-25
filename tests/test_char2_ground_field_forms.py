"""Scope and corruption guards for the ground-field forms package."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-25-char2-ground-field-forms'
SPEC=importlib.util.spec_from_file_location('ground_field_forms',PACKAGE/'verify.py')
verify=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class GroundFieldFormsTests(unittest.TestCase):
    def test_complete_saved_report_and_scope(self):
        saved=json.loads((ROOT/'results/char2-ground-field-forms-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(),saved)
        self.assertEqual(sum(r['all_action_invariance_checks'] for r in saved['finite_fields']),228696)
        self.assertEqual(sum(r['all_family_matrix_determinants'] for r in saved['finite_fields']),33824)
        self.assertEqual(saved['pairwise_inequivalent_GF2_forms_lower_bound'],5)
        for key in ('computer_certifies_perfect_field_classification','all_P_forms_classified',
                    'complete_GF2_attainer_classification','nonperfect_field_forms_classified',
                    'independent_review','lean_formalized','improves_omega'):
            self.assertFalse(saved[key])

    def test_missing_AS_correction_is_rejected(self):
        original=verify.arf_numerators
        def broken(A,B,a,b,c,d):
            An,Bn,Rn=original(A,B,a,b,c,d)
            return An,Bn,Rn-b*c
        with patch.object(verify,'arf_numerators',side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError,'cleared AS identity'):
                verify.symbolic_controls()

    def test_wrong_binary_action_orientation_is_rejected(self):
        original=verify.binary_action
        with patch.object(verify,'binary_action',side_effect=lambda *a:original(*a).T):
            with self.assertRaisesRegex(ArithmeticError,'separable P twist action'):
                verify.symbolic_controls()

    def test_P_twist_corruption_is_rejected(self):
        original=verify.p_twist
        def broken(c):
            M=original(c);M[2,0]+=verify.t
            return M
        with patch.object(verify,'p_twist',side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError,'P twist determinant'):
                verify.symbolic_controls()

    def test_incorrect_weighted_action_is_rejected_over_GF4(self):
        original=verify.Field.transform
        def unweighted(F,A,B,G):
            AA,BB=original(F,A,B,G)
            determinant=F.mul(G[0],G[3])^F.mul(G[1],G[2])
            return F.mul(AA,F.inverse[determinant]),F.mul(BB,F.inverse[determinant])
        with patch.object(verify.Field,'transform',new=unweighted):
            with self.assertRaises(AssertionError):
                verify.finite_controls(2,0b111)

    def test_GF4_one_is_split_but_two_is_not(self):
        F=verify.Field(2,0b111)
        AS={F.sq(z)^z for z in range(4)}
        self.assertIn(1,AS)
        self.assertNotIn(2,AS)
        self.assertEqual(F.trace(1),0)
        self.assertEqual(F.trace(2),1)

    def test_missing_source_endpoint_is_rejected(self):
        original=verify.source_rows
        with patch.object(verify,'source_rows',side_effect=lambda M:original(M)[:-1]):
            with self.assertRaisesRegex(ArithmeticError,'complete source dimensions'):
                verify.five_GF2_forms()

    def test_dependency_pin_corruption_is_rejected(self):
        sources=verify.check_pins();target=ROOT/sources['local_dependencies'][0]['path']
        original=Path.read_bytes
        def corrupted(path):
            return original(path)+(b'corrupt' if path==target else b'')
        with patch.object(Path,'read_bytes',new=corrupted):
            with self.assertRaisesRegex(ArithmeticError,'source pin'):
                verify.check_pins()


if __name__=='__main__':
    unittest.main()

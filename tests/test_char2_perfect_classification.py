"""Exact coefficient, transformation, provenance and evidence-tier controls."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-25-char2-perfect-classification'
SPEC=importlib.util.spec_from_file_location('char2_perfect_classification',PACKAGE/'verify.py')
verify=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class PerfectClassificationTests(unittest.TestCase):
    def test_complete_report_and_evidence_scope(self):
        saved=json.loads((ROOT/'results/char2-perfect-classification-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(),saved)
        self.assertEqual(saved['finite_field_class_count_written_corollary'],5)
        for key in ('new_finite_attainer_census','computer_certifies_field_descent',
                    'computer_certifies_geometric_exhaustion','nonperfect_N_and_V_classified',
                    'independent_review','lean_formalized','compatible_tensor_map','improves_omega'):
            self.assertFalse(saved[key])

    def test_preserved_wrong_k_substitution_is_rejected(self):
        wrong={verify.u:verify.c**2+verify.c*verify.F+verify.c*verify.r+verify.c,
               verify.k:verify.F+verify.r+verify.v}
        with patch.object(verify,'initial_solution',return_value=wrong):
            with self.assertRaisesRegex(ArithmeticError,'initial coefficient solution'):
                verify.chart_controls()

    def test_normal_family_corruption_is_rejected(self):
        original=verify.normal
        def broken(*args,**kwargs):
            M=original(*args,**kwargs);M[2,2]+=verify.t
            return M
        with patch.object(verify,'normal',side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError,'forced normal family'):
                verify.chart_controls()

    def test_missing_AS_parameter_shift_is_rejected(self):
        original=verify.shifted_parameters()
        with patch.object(verify,'shifted_parameters',return_value=(original[0],original[1],original[2]-verify.z*verify.t)):
            with self.assertRaisesRegex(ArithmeticError,'AS shift'):
                verify.chart_controls()

    def test_wrong_binary_orientation_is_rejected(self):
        original=verify.binary_action
        with patch.object(verify,'binary_action',side_effect=lambda *a:original(*a).T):
            with self.assertRaisesRegex(ArithmeticError,'evaluation normalizer'):
                verify.normalization_controls()

    def test_quartic_corruption_is_rejected(self):
        original=verify.quartic
        with patch.object(verify,'quartic',side_effect=lambda M:original(M)+M[1,1]*M[0,1]**3):
            with self.assertRaisesRegex(ArithmeticError,'raw quartic restriction'):
                verify.chart_controls()

    def test_dependency_pin_corruption_is_rejected(self):
        sources=verify.check_pins();target=ROOT/sources['local_dependencies'][0]['path']
        original=Path.read_bytes
        def corrupted(path):return original(path)+(b'corrupt' if path==target else b'')
        with patch.object(Path,'read_bytes',new=corrupted):
            with self.assertRaisesRegex(ArithmeticError,'source pin'):
                verify.check_pins()


if __name__=='__main__':unittest.main()

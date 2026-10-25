"""Mutation guards for root-free N/V descent and its evidence boundary."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-25-char2-all-fields'
SPEC=importlib.util.spec_from_file_location('char2_all_fields',PACKAGE/'verify.py')
verify=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class AllFieldClassificationTests(unittest.TestCase):
    def test_saved_report_and_scope(self):
        saved=json.loads((ROOT/'results/char2-all-fields-2026-10-25/controls.json').read_text())
        self.assertEqual(verify.report(),saved)
        self.assertEqual(saved['written_classification_field'],'every characteristic-two field')
        for key in ('new_finite_census','computer_certifies_field_descent',
                    'computer_certifies_geometric_exhaustion','independent_review',
                    'lean_formalized','compatible_tensor_map','improves_omega'):
            self.assertFalse(saved[key])

    def test_missing_N_coefficient_is_rejected(self):
        original=verify.n_chart
        def broken():
            M=original();M[2,0]=0
            return M
        with patch.object(verify,'n_chart',side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError,'N restricted coefficients'):verify.n_controls()

    def test_incorrect_forced_root_is_rejected(self):
        with patch.object(verify,'forced_root',return_value=verify.lam):
            with self.assertRaisesRegex(ArithmeticError,'N forced root'):verify.n_controls()

    def test_missing_normalizer_transpose_is_rejected(self):
        original=verify.section_normalizer
        def broken(C):
            G,zz,delta=original(C);return G.T,zz,delta
        with patch.object(verify,'section_normalizer',side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError,'V left section normalizer'):verify.v_section_controls()

    def test_missing_section_scale_is_rejected(self):
        original=verify.section_normalizer
        def broken(C):
            G,zz,delta=original(C);return G,zz/delta,delta
        with patch.object(verify,'section_normalizer',side_effect=broken):
            with self.assertRaisesRegex(ArithmeticError,'V left section normalizer'):verify.v_section_controls()

    def test_unsquared_binary_factor_is_rejected(self):
        with patch.object(verify,'square_binary',side_effect=lambda T:T):
            with self.assertRaisesRegex(ArithmeticError,'V whole-family stabilizer'):verify.v_stabilizer_controls()

    def test_missing_complement_correction_is_rejected(self):
        rows=verify.generators();label,T,H,L,J,coords=rows[1]
        rows[1]=(label,T,H,L,J,(coords[0],coords[1]-verify.L**3*verify.z**4*verify.t,coords[2]))
        with patch.object(verify,'generators',return_value=rows):
            with self.assertRaisesRegex(ArithmeticError,'V whole-family stabilizer: lower'):verify.v_stabilizer_controls()

    def test_even_denominator_is_rejected(self):
        with self.assertRaisesRegex(ArithmeticError,'zero characteristic-two denominator'):
            verify.zero(verify.x/2,'inadmissible coefficient')

    def test_source_pin_corruption_is_rejected(self):
        sources=verify.check_pins();target=ROOT/sources['local_dependencies'][0]['path']
        original=Path.read_bytes
        def corrupted(path):return original(path)+(b'corrupt' if path==target else b'')
        with patch.object(Path,'read_bytes',new=corrupted):
            with self.assertRaisesRegex(ArithmeticError,'source pin'):verify.check_pins()


if __name__=='__main__':unittest.main()

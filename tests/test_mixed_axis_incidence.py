"""Uniform source replay and rejection of damaged incidence witnesses."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('axis_incidence_verifier', ROOT / 'research/ai/2026-10-21-mixed-axis-incidence/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class MixedAxisIncidenceTests(unittest.TestCase):
    def test_complete_uniform_source_replay(self):
        saved = ROOT / 'results/mixed-axis-incidence-2026-10-21/report.json'
        self.assertEqual(verify.report(), json.loads(saved.read_text()))
        self.assertEqual(verify.report()['quotient_dimensions'], [28, 10, 2, 0])
        self.assertFalse(verify.report()['improves_omega'])

    def test_hidden_exceptional_pair_is_rejected(self):
        # Nonzero generic polynomials can vanish identically in ell at t=1.
        with self.assertRaisesRegex(ArithmeticError, 'coefficient certificate failed'):
            verify.check_exception_factor((verify.T-1)*(verify.ELL**2+verify.U*verify.ELL+1))

    def test_changed_relation_minor_is_rejected(self):
        pair = copy.deepcopy(verify.certificate()['lower_minor_pair'])
        pair[1] = copy.deepcopy(pair[0])
        with self.assertRaisesRegex(ArithmeticError, 'minor sum is not t cubed'):
            verify.check_lower_minor_pair(verify.incidence_data()['h1'], pair)

    def test_changed_terminal_cube_is_rejected(self):
        parts, witness = verify.terminal_data()['cube_checks'][0]
        changed = copy.deepcopy(witness)
        changed['scales'][0] = '1'
        with self.assertRaisesRegex(ArithmeticError, 'Incorrect cubic minor diagonal'):
            verify.check_cube(parts, changed)


if __name__ == '__main__':
    unittest.main()

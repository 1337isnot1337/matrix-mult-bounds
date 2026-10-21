"""Exact replay of the shifted-parity support-distribution certificates."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'research/ai/2026-10-20-anisotropic-constructions/parity_balancing.py'
RESULTS = ROOT/'results/anisotropic-constructions-2026-10-20'
SPEC = importlib.util.spec_from_file_location('parity_balancing',SOURCE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ParityBalancingTests(unittest.TestCase):
    def certificate(self,name):
        return json.loads((RESULTS/f'parity_balancing_p_{name}.json').read_text())

    def test_exact_endpoint_certificates(self):
        for name in ('2_3','67_100'):
            with self.subTest(name=name):
                result = MODULE.verify_rational(self.certificate(name))
                self.assertEqual(result['exact_marginal_equations_checked'],675)
                self.assertEqual(result['exact_probability_total'],'1')
                self.assertTrue(result['strictly_positive_on_full_support'])

    def test_optimum_bracket_and_tight_support(self):
        result = MODULE.exact_optimum_checks()
        self.assertEqual(result['polynomial_values'],['25','-15287/400'])
        self.assertEqual(result['zero_weight_support_equations_checked'],11725)
        self.assertTrue(result['strict_capacity_comparison']['verified'])

    def test_changed_mass_is_rejected(self):
        record = deepcopy(self.certificate('2_3'))
        row = record['orbit_masses'][0]
        row[1] = str(int(row[1])+1)
        with self.assertRaisesRegex(ArithmeticError,'marginal identity'):
            MODULE.verify_rational(record)

    def test_duplicate_orbit_is_rejected(self):
        record = deepcopy(self.certificate('67_100'))
        record['orbit_masses'].append(record['orbit_masses'][0])
        with self.assertRaisesRegex(ArithmeticError,'Duplicate'):
            MODULE.verify_rational(record)

    def test_negative_full_support_floor_is_rejected(self):
        record = deepcopy(self.certificate('2_3'))
        record['uniform_term_mass'][0] = -1
        with self.assertRaisesRegex(ArithmeticError,'Negative'):
            MODULE.verify_rational(record)


if __name__ == '__main__':
    unittest.main()

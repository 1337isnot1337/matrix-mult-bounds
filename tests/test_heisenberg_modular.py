"""Exact modular-filtration and gate-certificate controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-heisenberg-seven'
spec = importlib.util.spec_from_file_location('heisenberg_modular_bound', PACKAGE/'modular_bound.py')
modular = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modular)


class HeisenbergModularTests(unittest.TestCase):
    def test_all_certificates_and_actual_group_algebra_controls(self):
        report = json.loads((ROOT/'results/heisenberg-seven-2026-10-20/modular-bound.json').read_text())
        receipt = modular.verify_report(report)
        self.assertEqual(receipt, {'prime_certificates': 15, 'excluded_primes': 14,
                                  'basis_vectors': 495, 'generator_products': 1485})
        bad = copy.deepcopy(report)
        bad['bounds'][0]['slice_bound_cubed'] = '1'
        with self.assertRaisesRegex(ValueError, 'changed rational'):
            modular.verify_report(bad)
        bad = copy.deepcopy(report)
        bad['proved_exclusion_primes'].append(53)
        with self.assertRaisesRegex(ValueError, 'exclusion-prime'):
            modular.verify_report(bad)

    def test_parameters_and_root_boundaries(self):
        for p, t in [(9, '1/2'), (5, '0'), (5, '1'), (5, '-1/2')]:
            with self.assertRaises(ValueError):
                modular.bound(p, t)
        for a in (0, 1, 2, 15, 16, 17, 10**50):
            q = modular.root_floor(a, 4)
            self.assertLessEqual(q**4, a)
            self.assertLess(a, (q+1)**4)


if __name__ == '__main__':
    unittest.main()

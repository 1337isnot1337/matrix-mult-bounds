"""Coefficient and scope controls for the paired-source long-leg argument."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-paired-bundle-injectivity'
spec = importlib.util.spec_from_file_location('paired_long_leg_verification', PACKAGE/'verify.py')
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class PairedLongLegTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT/'results/paired-bundle-injectivity-2026-10-23/certificate.json').read_text())

    def test_complete_regeneration_and_inspected_source_pins(self):
        receipt = verifier.verify_report(self.report)
        self.assertEqual(receipt['paired_full_column_controls'], 18)
        self.assertEqual(receipt['hankel_all_degree_controls'], 40)
        self.assertEqual(receipt['beyond_interval_exact_complex_rank'], 70)
        self.assertEqual(receipt['new_target_exclusions'], 0)
        self.assertFalse(receipt['formalized_all_size_theorem'])

    def test_grading_matches_the_full_independent_coefficient_builder(self):
        for p in range(7):
            columns = verifier.generic_koszul_columns((6, 4, 6), verifier.long_terms(2), p)
            self.assertEqual(verifier.source_rank_mod2(2, p),
                             verifier.generic_rank_mod2(columns))

    def test_hankel_dimension_bounds_and_quadratic_endpoints(self):
        for record in self.report['hankel_coefficient_controls']:
            a = record['a']
            self.assertEqual(record['ranks'], [verifier.hankel_rank(a, p)
                                              for p in range(2*a)])
        self.assertEqual([verifier.injectivity_endpoint(a) for a in [14, 15, 16]],
                         [182, 210, 240])
        for a in [-1, 0, 1]:
            with self.assertRaises(ValueError):
                verifier.injectivity_endpoint(a)

    def test_integer_kernel_rejects_corruption_and_dependent_vectors(self):
        witness = self.report['beyond_interval_countercontrol']
        columns = verifier.generic_koszul_columns((6, 4, 6), verifier.long_terms(2), 3)
        self.assertEqual(verifier.verify_integer_kernel(
            columns, witness['free_columns'], witness['integer_kernel_vectors']), 10)
        bad = copy.deepcopy(witness['integer_kernel_vectors'])
        bad[0][0][1] += 1
        with self.assertRaises(ValueError):
            verifier.verify_integer_kernel(columns, witness['free_columns'], bad)
        bad = copy.deepcopy(witness['integer_kernel_vectors'])
        bad[1] = bad[0]
        with self.assertRaises(ValueError):
            verifier.verify_integer_kernel(columns, witness['free_columns'], bad)

    def test_all_power_and_exponent_claims_are_rejected(self):
        for key in ['higher_degrees_decided', 'independent_review',
                    'lean_formalized', 'improves_omega']:
            bad = copy.deepcopy(self.report)
            bad[key] = True
            with self.assertRaises(ValueError):
                verifier.verify_report(bad)
        bad = copy.deepcopy(self.report)
        bad['proof_status'] = 'formalized'
        with self.assertRaises(ValueError):
            verifier.verify_report(bad)


if __name__ == '__main__':
    unittest.main()

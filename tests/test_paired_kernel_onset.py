"""Exact fixed-input kernels, their source embeddings, and target bounds."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-paired-kernel-onset'
spec = importlib.util.spec_from_file_location('paired_kernel_onset_verifier', PACKAGE/'verify.py')
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class PairedKernelOnsetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        results = ROOT/'results/paired-kernel-onset-2026-10-23'
        cls.certificate = json.loads((results/'certificate.json').read_text())
        cls.screen = json.loads((results/'target-screen.json').read_text())

    def test_exact_restricted_kernels_and_all_full_source_embeddings(self):
        receipt = verifier.verify_certificate(self.certificate)
        self.assertEqual(receipt['restricted_exact_complex_ranks'], 15)
        self.assertEqual(receipt['critical_full_source_integer_kernels'], [4, 45])
        self.assertFalse(receipt['all_size_proof_formalized'])

    def test_complete_pinned_target_comparison_replay(self):
        receipt = verifier.verify_screen(self.screen)
        self.assertEqual(receipt['target_count'], 28)
        self.assertEqual(receipt['exact_comparisons'], 25254)
        self.assertEqual(receipt['additional_intermediate_noncuts'], 2970)
        self.assertEqual(receipt['rank_exclusion_witnesses'], 0)

    def test_bound_does_not_claim_complete_source_kernel(self):
        self.assertEqual(verifier.kernel_lower(2, 3), 4)
        self.assertLess(verifier.kernel_lower(2, 3), 10)
        for a in range(2, 17):
            m, N = a*(a-1), a*(2*a-1)
            self.assertEqual(verifier.kernel_lower(a, m), 0)
            self.assertEqual(verifier.kernel_lower(a, m+1), a*verifier.choose(m, a-1))
            self.assertGreater(verifier.kernel_lower(a, N), 0)
        for p, rank in enumerate([4, 24, 60, 70, 36, 6, 0]):
            lower, upper = verifier.rank_bounds(2, p)
            self.assertLessEqual(lower, rank)
            self.assertGreaterEqual(upper, rank)

    def test_corrupt_integer_kernel_and_independence_are_rejected(self):
        witness = next(c for c in self.certificate['finite_exact_controls']
                       if c['a'] == 3 and c['degree'] == 7)
        bad = copy.deepcopy(witness['integer_kernel_vectors'])
        bad[0][0][1] += 1
        with self.assertRaises(ValueError):
            verifier.replay_full_source_embeddings(3, 7, witness['free_columns'], bad)
        bad = copy.deepcopy(witness['integer_kernel_vectors'])
        bad[1] = bad[0]
        with self.assertRaises(ValueError):
            verifier.replay_full_source_embeddings(3, 7, witness['free_columns'], bad)

    def test_unsupported_closure_and_exponent_scope_are_rejected(self):
        for key in ['complete_source_kernel_formula', 'independent_review',
                    'lean_formalized', 'improves_omega']:
            bad = copy.deepcopy(self.certificate)
            bad[key] = True
            with self.assertRaises(ValueError):
                verifier.verify_certificate(bad)
        bad = copy.deepcopy(self.screen)
        bad['undecided_is_not_a_pass'] = False
        with self.assertRaises(ValueError):
            verifier.verify_screen(bad)


if __name__ == '__main__':
    unittest.main()

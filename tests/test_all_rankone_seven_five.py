"""Exceptional endpoint and physical reversal corruption controls."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('all_rankone_seven_five_test', ROOT / 'research/ai/2026-10-21-all-rankone-seven-five/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class AllRankoneSevenFiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = verify.report()

    def test_report_and_projective_scope(self):
        expected = json.loads((ROOT / 'results/all-rankone-seven-five-2026-10-21/report.json').read_text())
        self.assertEqual(self.report, expected)
        self.assertEqual(self.report['endpoint']['final_nonplane_dimension'], 0)
        self.assertEqual(self.report['endpoint']['added_coordinate_sources'], 28)
        self.assertTrue(self.report['all_projective_rankone_partners_excluded_under_adopted_claims'])
        self.assertFalse(self.report['affine_chart_verifier_replayed_here'])
        self.assertFalse(self.report['smaller_first_spaces_classified'])
        self.assertFalse(self.report['improves_omega'])

    def test_missing_terminal_reduction_is_rejected(self):
        proof = verify.proof
        certificate = copy.deepcopy(proof.cert)
        certificate['records'].pop()
        bad = verify.EndpointProof(verify.common, certificate)
        bad.data = proof.data
        with self.assertRaises(ArithmeticError):
            bad.report()

    def test_wrong_coordinate_source_is_rejected(self):
        proof = verify.proof
        records = copy.deepcopy(proof.cert['records'])
        records[0]['sources'][0]['source_index'] += 1
        with self.assertRaises(ArithmeticError):
            proof.replay(verify.sp.SparseMatrix.eye(84), set(), records)

    def test_identity_is_not_the_required_mixed_reversal(self):
        with self.assertRaises(ArithmeticError):
            verify.reversal_report(lambda index: index)

    def test_partial_reversal_does_not_preserve_the_source(self):
        def partial(index):
            return verify.normal.extension.index(3-index//28, (index//7) % 4, index % 7)
        with self.assertRaises(ArithmeticError):
            verify.reversal_report(partial)


if __name__ == '__main__':
    unittest.main()

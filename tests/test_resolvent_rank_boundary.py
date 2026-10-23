"""Rank-gap identity acceptance and sharp-boundary corruption controls."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-resolvent-rank-six-locus'
RESULTS = ROOT / 'results/resolvent-rank-six-locus-2026-10-23'
spec = importlib.util.spec_from_file_location('resolvent_boundary', PACKAGE / 'verify_boundary.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class ResolventRankBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / 'rank-seven-certificate.json').read_text())
        cls.original = json.loads((RESULTS / 'certificate.json').read_text())

    def test_rank_gap_and_all_seven_sharp_compressions(self):
        report = verify.verify(self.certificate, self.original)
        self.assertEqual(report, json.loads((RESULTS / 'boundary-verification.json').read_text()))
        self.assertEqual([c['compressed_dimension_over_Q'] for c in report['compression_controls']],
                         [111] * 6 + [95])

    def test_corrupt_eight_minors_and_sharpness_witness_are_rejected(self):
        cases = []
        bad = copy.deepcopy(self.certificate)
        bad['size'] = 7
        cases.append(bad)
        bad = copy.deepcopy(self.certificate)
        bad['stages'][0]['minor'].pop()
        cases.append(bad)
        bad = copy.deepcopy(self.certificate)
        bad['remaining_basis_coefficients'][-1][4] = 1
        cases.append(bad)
        bad = copy.deepcopy(self.certificate)
        bad['rank_eight_witness_minor'][0][1] = 4
        cases.append(bad)
        for i, bad in enumerate(cases):
            with self.subTest(corruption=i), self.assertRaises(ValueError):
                verify.verify(bad, self.original)


if __name__ == '__main__':
    unittest.main()

"""Exact source and positive acceptance controls for SL(2,5) x C2."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT/'research/ai/2026-10-20-sl2-five-c2'
spec = importlib.util.spec_from_file_location('sl2_five_c2_source', RESEARCH/'source_data.py')
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)


class SL2FiveC2Tests(unittest.TestCase):
    def test_group_center_and_subgroup(self):
        G = source.group()
        cert = source.subgroup_certificate(G)
        self.assertEqual(len(G['matrices']), 240)
        self.assertEqual((len(cert['members']), len(cert['center'])), (48, 4))
        self.assertEqual(len(set().union(*map(set, cert['central_orbits']))), 240)
        for g in range(240):
            self.assertEqual(G['mul'][g][G['inv'][g]], 0)
        H = set(cert['members'])
        self.assertEqual(sum(set(o) <= H for o in cert['central_orbits']), 12)

    def test_exact_source_and_conditional_gate(self):
        report = source.source_certificate()
        self.assertEqual(report['complex_degrees'], [1, 2, 2, 3, 3, 4, 4, 5, 6]*2)
        self.assertGreater(report['conditional_gate']['strict_positive_margin_numerator'], 0)
        self.assertFalse(report['concurrent_rank_locus_screen']['excluded'])
        self.assertFalse(report['degeneration_constructed'])

    def test_known_weighted_control_embeds_in_product(self):
        from group_exact import verify_witness
        G = source.group()
        report = json.loads((ROOT/'results/group-potentials-2026-10-20/sl2-5-control3-3-3.json').read_text())
        witness = report['witness']
        receipt = verify_witness(G, [[2*g for g in row] for row in witness['sets']],
                                 witness['potentials'])
        self.assertEqual(receipt['intended_terms'], 27)
        self.assertEqual(receipt['minimum_extra_weight'],
                         witness['verification']['minimum_extra_weight'])

    def test_original_seven_source_certificate_is_unchanged(self):
        spec = importlib.util.spec_from_file_location('seven_source_regression',
            source.SEVEN/'source_certificate.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        expected = json.loads((ROOT/'results/sl2-seven-2026-10-20/source-certificate.json').read_text())
        expected.pop('conditional_exponent_gate')
        self.assertEqual(module.derive(), expected)


if __name__ == '__main__':
    unittest.main()

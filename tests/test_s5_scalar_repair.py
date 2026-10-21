"""Exact Laurent cancellation, conditional cost and finite disjoint circuits."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-s5-scalar-repair'
sys.path.insert(0, str(PACKAGE))


def load(name):
    spec = importlib.util.spec_from_file_location('s5_scalar_'+name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


repair, verifier = load('scalar_repair'), load('verify')


class S5ScalarRepairTests(unittest.TestCase):
    def test_actual_laurent_correction_and_missing_term_rejection(self):
        G, item = repair.control()
        self.assertEqual(item['verification']['scalar_corrections'], 1)
        self.assertEqual(item['verification']['corrected_negative_terms'], 1)
        self.assertEqual(item['verification']['minimum_surviving_weight'], 1)
        with self.assertRaises(ValueError):
            repair.verify_repair(G, item['sets'], item['potentials'], [])
        with self.assertRaises(ValueError):
            repair.verify_repair(G, item['sets'], item['potentials'], [[0,0,0,0,0,0]])
        bad = item['potentials'][:]
        bad[0] = 0.5
        with self.assertRaises(ValueError):
            repair.verify_repair(G, item['sets'], bad, item['corrections'])

    def test_complete_replay_and_nine_circuits(self):
        report = verifier.replay()
        self.assertEqual(report['specific_candidate']['monomial_correction_lower_bound'], 9)
        self.assertEqual(report['conditional_cost']['strict_positive_margin_numerator'], 6805979977)
        self.assertEqual(report['arbitrary_correction_bound']['auxiliary_rank_lower_bound'], 9)
        self.assertFalse(report['exponent_improvement'])

    def test_cost_and_disjointness_corruptions(self):
        path = ROOT/'results/s5-scalar-repair-2026-10-21'
        item = json.loads((path/'source-cost.json').read_text())
        bad = copy.deepcopy(item)
        bad['gate']['source_term_upper_numerators'][0] = 1
        with self.assertRaises(ValueError):
            verifier.verify_cost(bad)
        pack = json.loads((path/'first-trade-free-packing.json').read_text())
        G, _, _ = verifier.data(pack['shape'])
        bad = copy.deepcopy(pack['circuits'])
        bad[1] = bad[0]
        with self.assertRaises(ValueError):
            repair.verify_disjoint_circuits(G, pack['sets'], bad)

    def test_coordinate_packet_and_sharp_one_scalar_control(self):
        G, item = repair.control()
        extras = [list(v) for v in repair.terms(G, item['sets']) if not repair.intended(v)]
        circuit = {'vertices': extras, 'weights': [1,1],
                   'output_coordinates': sorted({tuple(v[4:6]) for v in extras})}
        receipt = repair.verify_coordinate_packing(G, item['sets'], [circuit], 2)
        self.assertEqual(receipt['auxiliary_rank_lower_bound'], item['verification']['scalar_corrections'])
        path = ROOT/'results/s5-scalar-repair-2026-10-21/first-coordinate-packing.json'
        packet = json.loads(path.read_text())
        G, _, _ = verifier.data(packet['shape'])
        with self.assertRaises(ValueError):
            repair.verify_coordinate_packing(G, packet['sets'], packet['circuits'], 0)


if __name__ == '__main__':
    unittest.main()

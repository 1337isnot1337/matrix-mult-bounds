"""Necessary saturation equations compared with all 4096 normalized small lifts."""
from itertools import product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT/'research/ai/2026-10-20-sl2-five-c2'
sys.path.insert(0, str(RESEARCH))
from source_data import group, subgroup_certificate, central_projection
from pair_saturation import pair_data, extend, saturated_reject, verify_saturated, replay
from binary_lift_system import pair_classes
from group_exact import pair_map


class SL2FiveSaturationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.G = group()
        cls.cert = subgroup_certificate(cls.G)
        cls.Q = central_projection(cls.G, cls.cert)
        cls.data = pair_data(cls.G, cls.Q, cls.cert['center'])
        cls.pairs = pair_classes(cls.G, cls.Q)

    def test_every_normalized_four_by_four_lift(self):
        projected = [[0, 1, 2, 3], [0, 1, 2, 3], [0]]
        system = extend({'variables': [], 'rows': []}, self.data, projected)
        self.assertGreaterEqual(len(system['rows']), 2)
        accepted, violations = 0, 0
        for choices in product(range(4), repeat=6):
            colors = [[0]+list(choices[:3]), [0]+list(choices[3:]), [0]]
            sets = [[self.G['mul'][self.cert['center'][c]][self.Q['representatives'][p]]
                     for c, p in zip(colors[f], row)] for f, row in enumerate(projected)]
            assignment = 0
            for i, (kind, f, p) in enumerate(system['variables']):
                color = colors[f][projected[f].index(p)]
                assignment |= ((color >> (kind == 'twist')) & 1) << i
            satisfies = all((row['mask'] & assignment).bit_count() % 2 == row['rhs']
                            for row in system['rows'])
            violations += not satisfies
            try:
                pair_map(self.G, sets[0], sets[1])
            except ValueError:
                continue
            accepted += 1
            self.assertTrue(satisfies, choices)
        self.assertEqual(accepted, 128)
        self.assertGreater(violations, 0)

    def test_projected_pair_capacity_certificate_and_tamper(self):
        record = saturated_reject(self.pairs, self.data, [list(range(5)), list(range(5)), [0]])
        self.assertEqual(record['type'], 'exact-pair-capacity')
        self.assertTrue(verify_saturated(self.pairs, self.data, record))
        record['blocked_points'].pop()
        with self.assertRaises(ValueError):
            verify_saturated(self.pairs, self.data, record)

    def test_both_completed_saturated_streams_and_tamper(self):
        results = ROOT/'results/sl2-five-c2-2026-10-20'
        for name, count, untraced in (('projected-saturated-first13', 169, 0),
                                     ('projected-saturated-learning-first13', 244, 1)):
            receipt = replay(results/(name+'.json'))
            self.assertEqual(receipt['counts_checked']['saturated-parity-subtotal'], count)
            self.assertEqual(receipt['untraced_cores_not_verified'], untraced)
            self.assertFalse(receipt['complete_exclusion'])
        record = json.loads((results/'saturated-first-circuit.json').read_text())
        record['rows'][0]['rhs'] ^= 1
        with self.assertRaises(ValueError):
            verify_saturated(self.pairs, self.data, record)


if __name__ == '__main__':
    unittest.main()

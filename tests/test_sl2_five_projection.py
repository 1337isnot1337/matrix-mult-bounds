"""Necessary binary lift equations checked against all small central lifts."""
import copy
import gzip
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT/'research/ai/2026-10-20-sl2-five-c2'
sys.path.insert(0, str(RESEARCH))
from source_data import group, subgroup_certificate, central_projection
from binary_lift_system import pair_classes, necessary_system, reject, verify_rejection
from group_exact import pair_map


class SL2FiveProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.G = group()
        cls.cert = subgroup_certificate(cls.G)
        cls.Q = central_projection(cls.G, cls.cert)
        cls.pairs = pair_classes(cls.G, cls.Q)

    def test_two_color_equations_against_all_64_lifts(self):
        q, r = sorted({c for c in self.pairs.values()})[:2]
        projected = [[0, q], [0, q], [0, r]]
        system = necessary_system(self.pairs, projected)
        owner_labels = [v for v in system['variables'] if v[0] == 'owner']
        self.assertEqual(len(owner_labels), 2)
        for colors in product(range(4), repeat=3):
            sets = [[0, self.G['mul'][self.cert['center'][c]][self.Q['representatives'][row[1]]]]
                    for c, row in zip(colors, projected)]
            try:
                for f in range(3):
                    pair_map(self.G, sets[f], sets[(f+1) % 3])
                actual = True
            except ValueError:
                actual = False
            feasible = False
            for owners in product(range(2), repeat=2):
                assignment = 0
                for i, label in enumerate(system['variables']):
                    bit = (owners[owner_labels.index(label)] if label[0] == 'owner'
                           else sets[label[1]][projected[label[1]].index(label[2])] & 1)
                    assignment |= bit << i
                feasible |= all((row['mask'] & assignment).bit_count() % 2 == row['rhs']
                                for row in system['rows'])
            self.assertEqual(feasible, actual, colors)

    def test_capacity_certificate_and_tamper(self):
        q = min(self.pairs.values())
        rejection = reject(self.pairs, [[0, q]]*3)
        self.assertEqual(rejection['type'], 'exact-capacity')
        self.assertTrue(verify_rejection(self.pairs, rejection))
        bad = copy.deepcopy(rejection)
        bad['blocked_points'].pop()
        with self.assertRaises(ValueError):
            verify_rejection(self.pairs, bad)

    def test_every_saved_binary_circuit_and_tamper(self):
        spec = importlib.util.spec_from_file_location('five_projected_replay',
            RESEARCH/'verify_projected_lifts.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        report = ROOT/'results/sl2-five-c2-2026-10-20/projected-binary.json'
        receipt = module.replay(report)
        self.assertGreater(receipt['counts_checked']['exact-parity'], 0)
        self.assertFalse(receipt['complete_exclusion'])
        path = report.with_suffix('.cuts.jsonl')
        payload = (path.read_bytes() if path.exists() else
                   gzip.decompress(Path(str(path)+'.gz').read_bytes()))
        record = next(json.loads(line) for line in payload.splitlines()
                      if json.loads(line)['type'] == 'exact-parity')
        record['rows'][0]['rhs'] ^= 1
        with self.assertRaises(ValueError):
            verify_rejection(self.pairs, record)


if __name__ == '__main__':
    unittest.main()

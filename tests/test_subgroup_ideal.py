"""Exact subgroup-ideal ranks, positive boundary and corruption controls."""
import copy
import gzip
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('subgroup_ideal_certificate',
    ROOT/'research/ai/2026-10-21-subgroup-ideal/ideal.py')
ideal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ideal)


class SubgroupIdealTests(unittest.TestCase):
    def test_all_exact_ideal_certificates_and_tamper(self):
        report = json.loads((ROOT/'results/subgroup-ideal-2026-10-21/certificates.json').read_text())
        receipts = [ideal.verify(G, r) for G, r in zip(ideal.sources(), report['records'])]
        self.assertEqual([r['ideal_dimension'] for r in receipts], [80, 88, 160])
        self.assertEqual([r['cosets'] for r in receipts], [144, 144, 288])
        self.assertEqual(receipts, report['verification'])
        bad = copy.deepcopy(report['records'][0])
        bad['integer_annihilators'][0][bad['cosets'][0][0]] += 1
        with self.assertRaises(ValueError):
            ideal.verify(ideal.sources()[0], bad)
        self.assertEqual(ideal.modular_rank([[1, 1], [1, 0]]), 2)

    def test_actual_positive_boundary_in_an_abelian_group(self):
        points = [(a, b) for a in range(3) for b in range(3)]
        lookup = {x: i for i, x in enumerate(points)}
        G = {'name': 'C3 x C3', 'matrices': points, 'identity': 0,
             'mul': [[lookup[(a+c) % 3, (b+d) % 3] for c, d in points] for a, b in points],
             'inv': [lookup[-a % 3, -b % 3] for a, b in points]}
        record = json.loads(json.dumps(ideal.derive(G, [0, 1, 2])))
        self.assertEqual(ideal.verify(G, record)['ideal_dimension'], 3)
        from group_exact import verify_witness
        witness = verify_witness(G, [[0, 1, 2], [0], [0, 3, 6]], [0]*7)
        self.assertEqual(witness['intended_terms'], 9)
        self.assertEqual(1*3, record['ideal_dimension'])

    def test_new_coset_cuts_cover_both_previous_failed_lifts(self):
        report = json.loads((ROOT/'results/subgroup-ideal-2026-10-21/certificates.json').read_text())
        record = report['records'][1]
        path = ROOT/'results/sl2-five-native-2026-10-20/split-full-capacity-10.cuts.jsonl.gz'
        checked = 0
        for line in gzip.decompress(path.read_bytes()).splitlines():
            item = json.loads(line)
            if item['type'] != 'exact-farkas':
                continue
            sets = list(map(set, item['sets']))
            self.assertTrue(any(set(C) <= S for S in sets for C in record['cosets']))
            checked += 1
        self.assertEqual(checked, 2)


if __name__ == '__main__':
    unittest.main()

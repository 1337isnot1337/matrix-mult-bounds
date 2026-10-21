"""Exact controls for the joint SL(2,5) projected/sign investigation."""
import copy
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-sl2-five-native-parity'
sys.path.insert(0, str(PACKAGE))


def load(name):
    spec = importlib.util.spec_from_file_location('five_native_'+name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


source, capacity, replay = load('data'), load('pair_capacity'), load('verify')
split_source = load('split_source')


class FiveNativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.G, cls.Q, cls.receipt = source.data()

    def test_all_endpoint_sign_colors_and_anchor_coverage(self):
        G, Q = self.G, self.Q
        checked = 0
        for (u, v), (c, offset) in Q['pairs'].items():
            for a, b in product(range(2), repeat=2):
                x, y = Q['representatives'][u], Q['representatives'][v]
                if a:
                    x = G['mul'][Q['z']][x]
                if b:
                    y = G['mul'][Q['z']][y]
                d = G['mul'][x][G['inv'][y]]
                expected = Q['fibers'][c][offset ^ a ^ b] if len(Q['fibers'][c]) == 2 else Q['fibers'][c][0]
                self.assertEqual(min(d, G['inv'][d]), expected)
                checked += 1
        self.assertEqual(checked, 7080)
        self.assertEqual(len(self.receipt['anchor_coverage']), 11)
        self.assertGreater(self.receipt['conditional_gate']['strict_positive_margin_numerator'], 0)

    def test_capacity_uses_the_required_pair_map_orientation(self):
        Q = self.Q
        orientation_differs = False
        for q in range(60):
            edges = [[s, Q['mul'][s][q]] for s in range(3)]
            item = {'legs': [0, 1], 'label': q, 'edges': edges}
            self.assertEqual(len(capacity.verify(Q, item)), 6)
            orientation_differs |= any(Q['mul'][s][Q['inv'][t]] != q for s, t in edges)
            bad = copy.deepcopy(item)
            bad['label'] = (q+1) % 60
            with self.assertRaisesRegex(ValueError, 'wrong projected label'):
                capacity.verify(Q, bad)
        self.assertTrue(orientation_differs)
        known = json.loads((ROOT/'results/group-potentials-2026-10-20/sl2-5-control3-3-3.json').read_text())['witness']
        projected = [[Q['projection'][g] for g in row] for row in known['sets']]
        self.assertEqual(capacity.violations(Q, projected), [])
        self.assertTrue(capacity.violations(Q, [list(range(10))]*3))

    def test_saved_exact_parity_circuits_and_tamper(self):
        path = ROOT/'results/sl2-five-native-2026-10-20/lazy-10.json'
        receipt = replay.replay(path)
        self.assertEqual(receipt['certificates'], {'exact-parity': 506})
        import gzip
        cuts = path.with_suffix('.cuts.jsonl')
        payload = cuts.read_bytes() if cuts.exists() else gzip.decompress(Path(str(cuts)+'.gz').read_bytes())
        item = json.loads(payload.splitlines()[0])
        item['rows'][0]['rhs'] ^= 1
        with self.assertRaises(ValueError):
            replay.verify_parity(self.Q, item)

    def test_complete_projected_triple_orbits(self):
        from collections import Counter
        patterns = capacity.triple_patterns(self.Q)
        self.assertEqual(len(patterns), 577)
        self.assertEqual(Counter(map(len, patterns.values())), {60: 567, 20: 10})
        covered = set()
        for canonical, triples in patterns.items():
            expected = {tuple(sorted(self.Q['mul'][p][g] for p in canonical))
                        for g in range(60)}
            self.assertEqual(expected, set(triples))
            self.assertFalse(covered.intersection(triples))
            covered.update(triples)
        self.assertEqual(covered, set(combinations(range(60), 3)))

    def test_split_cover_source_and_weighted_positive_control(self):
        expected = json.loads((ROOT/'results/sl2-five-native-2026-10-20/split-source-certificate.json').read_text())
        self.assertEqual(split_source.certificate(), expected)
        G, Q, receipt = split_source.split_data()
        self.assertEqual(receipt['inverse_class_fiber_counts'], {1: 0, 2: 37})
        self.assertEqual(Q['mul'], self.Q['mul'])
        self.assertLess(receipt['conditional_gate']['source_upper_numerator'],
                        self.receipt['conditional_gate']['source_upper_numerator'])
        for (u, v), (c, offset) in Q['pairs'].items():
            for a, b in product(range(2), repeat=2):
                x, y = 2*u+a, 2*v+b
                d = G['mul'][x][G['inv'][y]]
                self.assertEqual(min(d, G['inv'][d]), Q['fibers'][c][offset ^ a ^ b])
        known = json.loads((ROOT/'results/sl2-five-native-2026-10-20/split-control3.json').read_text())['witness']
        result = replay.verify_witness(G, known['sets'], known['potentials'])
        self.assertEqual(result['intended_terms'], 27)
        self.assertEqual(result['minimum_extra_weight'], 1)
        spec = importlib.util.spec_from_file_location('split_rank_locus',
            ROOT/'research/ai/2026-10-20-group-potentials/rank_locus_obstruction.py')
        sys.path.insert(0, str(ROOT/'research/ai/2026-10-20-group-potentials'))
        rank_locus = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(rank_locus)
        self.assertFalse(rank_locus.screen(receipt['complex_degrees'], [10]*3)['excluded'])


if __name__ == '__main__':
    unittest.main()

"""Exact S5 source, modular certificate and canonicalization controls."""
import copy
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-s5-split'
sys.path.insert(0, str(PACKAGE))


def load(name):
    spec = importlib.util.spec_from_file_location('s5_split_'+name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


source, radical, symmetry = load('s5_source'), load('verify_radical'), load('symmetry')
search_replay = load('verify_search')


class S5SplitTests(unittest.TestCase):
    def test_source_and_every_central_sign_color(self):
        expected = json.loads((ROOT/'results/s5-split-2026-10-21/source-certificate.json').read_text())
        self.assertEqual(source.certificate(), expected)
        self.assertEqual(sum(d*d for d in expected['complex_degrees']), 240)
        self.assertGreater(expected['conditional_gate']['strict_positive_margin_numerator'], 0)
        screen = source.rank_screen()
        self.assertFalse(screen['excluded'])
        self.assertEqual(screen['dimension_deficit'], -22)
        G, Q, receipt = source.data()
        self.assertEqual((len(receipt['anchor_coverage']), len(receipt['first_pair_anchor_disjunction'])), (23, 4))
        checked = 0
        for (u, v), (c, offset) in Q['pairs'].items():
            for a, b in product(range(2), repeat=2):
                g = G['mul'][2*u+a][G['inv'][2*v+b]]
                self.assertEqual(min(g, G['inv'][g]), Q['fibers'][c][offset ^ a ^ b])
                checked += 1
        self.assertEqual(checked, 28560)
        known = source.control()['witness']
        self.assertEqual(known['verification']['intended_terms'], 27)
        self.assertEqual(known['verification']['minimum_extra_weight'], 1)

    def test_radical_by_independent_group_convolution_and_corruption(self):
        report = json.loads((ROOT/'results/s5-split-2026-10-21/radical-pilot.json').read_text())
        receipt = radical.verify(report)
        self.assertEqual(receipt['power_dimensions'], [120, 87, 62, 53, 35, 26, 17, 0])
        self.assertEqual(receipt['group_products_checked'], 24360)
        self.assertFalse(receipt['target_excluded_by_this_bound'])
        bad = copy.deepcopy(report)
        bad['representation_matrices'][0][0] ^= 1
        with self.assertRaises(ValueError):
            radical.verify(bad)
        bad = copy.deepcopy(report)
        bad['power_bases'][0][0] = hex(int(bad['power_bases'][0][0], 16) ^ 1)
        with self.assertRaises(ValueError):
            radical.verify(bad)

    def test_lex_cnf_against_all_small_boolean_vectors(self):
        for n in range(5):
            top, clauses = [2*n], []
            def variable(label):
                top[0] += 1
                return top[0]
            symmetry.lex_geq(list(range(1, n+1)), list(range(n+1, 2*n+1)),
                             variable, clauses.append, 'test')
            for bits in product(range(2), repeat=2*n):
                feasible = False
                for extra in product(range(2), repeat=top[0]-2*n):
                    values = (0,)+bits+extra
                    if all(any(values[abs(v)] == int(v > 0) for v in row) for row in clauses):
                        feasible = True
                        break
                self.assertEqual(feasible, bits[:n] >= bits[n:])

    def test_canonical_weighted_control_and_conjugation_actions(self):
        G, Q, receipt = source.data()
        known = symmetry.canonical_control()['witness']
        self.assertEqual(known['verification']['minimum_extra_weight'], 1)
        actions = symmetry.actions(G, Q, receipt)
        self.assertEqual(len(actions), 24)
        order = receipt['projected_subgroup']+sorted(set(range(120))-set(receipt['projected_subgroup']))
        sets = [{Q['projection'][x] for x in row} for row in known['sets']]
        first = tuple(int(q in sets[0]) for q in order)
        for action in actions:
            self.assertEqual(set(action), set(range(120)))
            self.assertEqual({action[q] for q in receipt['projected_subgroup']}, set(receipt['projected_subgroup']))
            image = {action[q] for q in sets[0]}
            self.assertGreaterEqual(first, tuple(int(q in image) for q in order))
        self.assertGreaterEqual(tuple(int(q in sets[1]) for q in order),
                                tuple(int(q in sets[2]) for q in order))

    def test_both_saved_local_parity_streams(self):
        for name, count in [('local-target13-14-14', 2), ('local-learned13-14-14', 30)]:
            result = search_replay.replay(ROOT/'results/s5-split-2026-10-21'/(name+'.json'))
            self.assertEqual(result['certificates'], {'exact-parity': count})
            self.assertFalse(result['witness'])


if __name__ == '__main__':
    unittest.main()

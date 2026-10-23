"""Exact S5 source, modular certificate and canonicalization controls."""
import copy
import gzip
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
four, central = load('four_colors'), load('central_slice')


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

    def test_four_color_source_and_all_endpoint_colors(self):
        expected = json.loads((ROOT/'results/s5-split-2026-10-21/four-source-certificate.json').read_text())
        self.assertEqual(four.certificate(), expected)
        G, Q, receipt = four.data()
        self.assertEqual((len(G['mul']), len(Q['classes'])), (480, 72))
        self.assertEqual(len(receipt['anchor_coverage']), 23)
        count = 0
        for (u, v), (c, _) in Q['pairs'].items():
            for a, b in product(range(4), repeat=2):
                g = G['mul'][4*u+a][G['inv'][4*v+b]]
                self.assertEqual(min(g, G['inv'][g]), 4*c+(a ^ b))
                count += 1
        self.assertEqual(count, 114240)
        result = json.loads((ROOT/'results/s5-split-2026-10-21/four-encoding-control.json').read_text())
        self.assertEqual((result['signed_configurations'], result['accepted'], result['rejected']), (64, 24, 40))

    def test_central_slice_cut_beyond_pair_and_commuting_trade_tests(self):
        from group_exact import pair_map
        from verify_projected_reports import verify_farkas_record
        report = json.loads((ROOT/'results/s5-split-2026-10-21/central-slice-control.json').read_text())
        self.assertEqual(central.slice_control(), report['slice_control'])
        G, Q, receipt = four.data()
        sets = report['farkas']['sets']
        for f in range(3):
            self.assertEqual(len(pair_map(G, sets[f], sets[(f+1) % 3])), 16)
        self.assertEqual(central.commuting_violations(G, sets), 0)
        self.assertTrue(verify_farkas_record(G, report['farkas']))
        self.assertTrue(central.verify_match(Q, report['matching']))
        bad = copy.deepcopy(report['matching'])
        bad['points'][0] = bad['points'][1]
        with self.assertRaises(ValueError):
            central.verify_match(Q, bad)
        known = symmetry.canonical_control()['witness']
        projected = [[g//2 for g in S] for S in known['sets']]
        self.assertIsNone(central.find_match(Q, projected))

    def test_cyclic_center_source_and_matched_color_control(self):
        cyclic = load('cyclic_four')
        expected = json.loads((ROOT/'results/s5-split-2026-10-21/cyclic-four-source-certificate.json').read_text())
        self.assertEqual(cyclic.certificate(), expected)
        G, Q, receipt = cyclic.data((18, 18, 20))
        self.assertGreater(receipt['conditional_gate']['strict_positive_margin_numerator'], 0)
        self.assertFalse(receipt['central_slice_rank_three_cut_applicable'])
        self.assertEqual(sum(map(len, Q['fibers'].values())), 263)
        checked = 0
        for (u, v) in Q['pairs']:
            for a, b in product(range(4), repeat=2):
                label = 4*Q['mul'][u][Q['inv'][v]]+(a-b) % 4
                actual = G['mul'][4*u+a][G['inv'][4*v+b]]
                self.assertEqual(actual, label)
                checked += 1
        self.assertEqual(checked, 114240)
        self.assertEqual(cyclic.control()['witness']['verification']['minimum_extra_weight'], 1)
        self.assertEqual(central.matched_color_control()['C4']['matched_bijections'], 0)

    def test_colored_streams_and_actual_group_trade_templates(self):
        replayer = load('verify_four')
        trade = load('commuting_trades')
        cyclic = load('cyclic_four')
        for name, count, provider, template_count in [
                ('colored-warm18-18-20', 1218, four.data, 4816),
                ('cyclic-colored18-18-20', 1427, cyclic.data, 4096)]:
            path = ROOT/'results/s5-split-2026-10-21'/(name+'.json')
            result = replayer.replay(path)
            self.assertEqual(result['certificates'], {'exact-farkas': count})
            self.assertFalse(result['witness'])
            G, _, _ = provider()
            rows = trade.templates(G)
            self.assertEqual(len(rows), template_count)
            raw = gzip.decompress(path.with_suffix('.cuts.jsonl.gz').read_bytes())
            item = next(r for r in map(json.loads, raw.splitlines()) if len(r['weights']) == 2)
            self.assertGreater(trade.violations(G, item['sets'], rows), 0)
            known = cyclic.control()['witness']['sets'] if provider == cyclic.data else [
                [4*(g//2)+g % 2 for g in S] for S in source.control()['witness']['sets']]
            self.assertEqual(trade.violations(G, known, rows), 0)

    def test_trade_guided_models_and_complete_farkas_streams(self):
        replayer = load('verify_four')
        trade = load('commuting_trades')
        cyclic = load('cyclic_four')
        for name, count, provider, expected_matches in [('colored-trades18-18-20', 13, four.data, 2),
                                       ('cyclic-trades18-18-20', 14, cyclic.data, 0)]:
            path = ROOT/'results/s5-split-2026-10-21'/(name+'.json')
            result = replayer.replay(path)
            self.assertEqual(result['certificates'], {'exact-farkas': count})
            G, Q, _ = provider()
            rows = trade.templates(G)
            records = gzip.decompress(path.with_suffix('.cuts.jsonl.gz').read_bytes())
            matches = 0
            for item in map(json.loads, records.splitlines()):
                self.assertEqual(trade.violations(G, item['sets'], rows), 0)
                matching = central.find_match(Q, [[g//4 for g in S] for S in item['sets']])
                if matching is not None:
                    self.assertTrue(central.verify_match(Q, matching))
                    matches += 1
            self.assertEqual(matches, expected_matches)


if __name__ == '__main__':
    unittest.main()

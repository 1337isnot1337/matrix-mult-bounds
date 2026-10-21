"""Finite exact source calculation and interval checks for the SL(2,7) lane."""
import importlib.util
import copy
from itertools import product
from pathlib import Path
import random
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('sl2_seven_source',
    ROOT/'research/ai/2026-10-20-sl2-seven/source_certificate.py')
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)
spec_center = importlib.util.spec_from_file_location('sl2_seven_center',
    ROOT/'research/ai/2026-10-20-sl2-seven/central_involution.py')
center = importlib.util.module_from_spec(spec_center)
spec_center.loader.exec_module(center)


def load_local(name):
    spec = importlib.util.spec_from_file_location(name,
        ROOT/'research/ai/2026-10-20-sl2-seven'/f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lift = load_local('central_lift')
subgroup = load_local('subgroup_normalization')
# The replayer uses ordinary local imports when run as a script.
sys.path.insert(0, str(ROOT/'research/ai/2026-10-20-sl2-seven'))
replayer = load_local('verify_projected_reports')
fibers = load_local('abelian_fiber_cuts')
templates = load_local('parity_templates')


class SL2SevenTests(unittest.TestCase):
    def test_source_blocks_and_conditional_gate(self):
        report = source.derive()
        self.assertEqual(report['complex_degrees'], [1, 3, 3, 4, 4, 6, 6, 6, 7, 8, 8])
        self.assertEqual(sum(report['class_sizes']), 336)
        gate = source.exponent_gate(report['complex_degrees'])
        self.assertGreater(gate['strict_positive_margin_numerator'], 0)

    def test_integer_root_intervals(self):
        for n in range(1, 10):
            for a in (0, 1, 2, 15, 16, 17, 1000, 2**123+7):
                root = source.root_floor(a, n)
                self.assertLessEqual(root**n, a)
                self.assertGreater((root+1)**n, a)

    def test_bad_source_cost_rejected(self):
        with self.assertRaises(ArithmeticError):
            source.exponent_gate([20]*11)

    def test_center_pair_count_and_strict_threshold(self):
        G = source.group(7)
        exclusions = center.forced_center_pair_exclusions(G, [16, 16, 17])
        self.assertEqual([x['set'] for x in exclusions], [0, 1, 2])
        self.assertEqual([len(x['pairs']) for x in exclusions], [168]*3)
        self.assertEqual(len(center.forced_center_pair_exclusions(G, [12, 14, 14])), 1)
        self.assertFalse(center.forced_center_pair_exclusions(G, [12, 12, 12]))

    def test_central_collision_gives_opposite_supported_terms(self):
        G = source.group(7)
        z = center.forced_center_pair_exclusions(G, [16, 16, 17])[0]['central_involution']
        checked = 0
        for g in range(1, 336):
            if g == z:
                continue
            # t0=u0=s0=identity, s1=z, t1=g, u1=z*g.
            center.opposite_trade(G, 0, z, 0, g, 0, G['mul'][z][g])
            checked += 1
        self.assertEqual(checked, 334)

    def test_order_48_normalization_and_tampering(self):
        G = source.group(7)
        cert = subgroup.octahedral_certificate(G)
        self.assertTrue(subgroup.verify_certificate(G, cert))
        self.assertEqual(len(cert['witnesses']), 47)
        broken = copy.deepcopy(cert)
        broken['witnesses'][0]['anchor'] = 0
        self.assertFalse(subgroup.verify_certificate(G, broken))

    def test_lift_equations_against_all_small_sign_choices(self):
        G = source.group(7)
        Q = lift.quotient(G, G['matrices'].index((6, 0, 0, 6)))
        self.assertEqual((len(Q['representatives']), len(Q['classes'])), (168, 94))
        rng = random.Random(20261321)
        examples = [[[0]+rng.sample(range(1, 168), k-1) for _ in range(3)]
                    for k in (2, 3, 4) for _ in range(4)]
        examples.append([[0, 110, 109, 16], [0, 109, 127, 153], [0, 149, 33, 30]])
        from group_exact import pair_map
        for sets in examples:
            k = len(sets[0])
            try:
                system = lift.lift_system(Q, sets)
                predicted = lift.eliminate(system)['consistent']
            except ValueError:
                predicted = False
            found = False
            for bits in product((0, 1), repeat=3*(k-1)):
                actual = [[0]+[G['mul'][Q['z']][Q['representatives'][p]]
                              if bits[f*(k-1)+j] else Q['representatives'][p]
                              for j, p in enumerate(points[1:])]
                          for f, points in enumerate(sets)]
                try:
                    for f in range(3):
                        pair_map(G, actual[f], actual[(f+1) % 3])
                except ValueError:
                    continue
                found = True
                break
            self.assertEqual(found, predicted, sets)

    def test_parity_certificate_replay_and_tampering(self):
        G = source.group(7)
        Q = lift.quotient(G, G['matrices'].index((6, 0, 0, 6)))
        sets = [[0, 110, 109, 16], [0, 109, 127, 153], [0, 149, 33, 30]]
        system = lift.lift_system(Q, sets)
        decision = lift.eliminate(system)
        self.assertFalse(decision['consistent'])
        rows = [system['rows'][i] for i in decision['circuit']]
        item = {'sets': sets, 'variables': system['variables'], 'rows': rows,
                'blocked_points': sorted({tuple(p) for r in rows for p in r['support']})}
        self.assertTrue(replayer.verify_parity(Q, item))
        broken = copy.deepcopy(item)
        broken['rows'][0]['mask'] ^= 1
        with self.assertRaises(ValueError):
            replayer.verify_parity(Q, broken)

    def test_cyclic_subgroup_preimages(self):
        G = source.group(7)
        Q = lift.quotient(G, G['matrices'].index((6, 0, 0, 6)))
        records = fibers.cyclic_subgroups(G, Q)
        self.assertEqual([sum(len(r['subgroup']) == m for r in records)
                          for m in (3, 4, 7)], [28, 21, 8])

    def test_center_free_two_point_fibers_cannot_tile_cyclic_eight(self):
        checked = 0
        for differences in product((1, 2, 3, 5, 6, 7), repeat=3):
            sums = {sum(b*q for b, q in zip(bits, differences)) % 8
                    for bits in product((0, 1), repeat=3)}
            self.assertLess(len(sums), 8)
            checked += 1
        self.assertEqual(checked, 216)

    def test_pattern_canonicalization_preserves_right_translation(self):
        G = source.group(7)
        Q = lift.quotient(G, G['matrices'].index((6, 0, 0, 6)))
        rng = random.Random(20261322)
        for _ in range(12):
            points = rng.sample(range(168), 5)
            expected = templates.canonical_pattern(Q, points)
            for g in range(168):
                translated = [Q['mul'][p][g] for p in points]
                self.assertEqual(templates.canonical_pattern(Q, translated), expected)

    def test_template_clauses_preserve_independently_checked_lifts(self):
        class Pool:
            def __init__(self):
                self.labels = {}
            def id(self, label):
                if label not in self.labels:
                    self.labels[label] = len(self.labels)+1
                return self.labels[label]

        from group_exact import pair_map
        G = source.group(7)
        Q = lift.quotient(G, G['matrices'].index((6, 0, 0, 6)))
        forbidden = [[0, 110, 109, 16], [0, 109, 127, 153], [0, 149, 33, 30]]
        system = lift.lift_system(Q, forbidden)
        rows = [system['rows'][i] for i in lift.eliminate(system)['circuit']]
        item = {'sets': forbidden, 'variables': system['variables'], 'rows': rows,
                'blocked_points': sorted({tuple(p) for r in rows for p in r['support']})}
        pool = Pool()
        members = [[pool.id(('member', f, p)) for p in range(168)] for f in range(3)]
        clauses = []
        templates.append_templates(Q, [item], pool, members, clauses)
        checked = 0
        for f in range(3):
            for point in forbidden[f][1:]:
                sets = copy.deepcopy(forbidden)
                sets[f].remove(point)
                system = lift.lift_system(Q, sets)
                solution = lift.eliminate(system)
                if not solution['consistent']:
                    continue
                actual = lift.lifted_sets(G, Q, system, solution['assignment'], sets)
                for leg in range(3):
                    pair_map(G, actual[leg], actual[(leg+1) % 3])
                true = set()
                for label, variable in pool.labels.items():
                    if label[0] == 'member':
                        _, leg, p = label
                        value = p in sets[leg]
                    else:
                        _, leg, pattern = label
                        value = any(all(Q['mul'][p][g] in sets[leg] for p in pattern)
                                    for g in range(168))
                    if value:
                        true.add(variable)
                self.assertTrue(all(any((v in true) if v > 0 else (-v not in true)
                                        for v in clause) for clause in clauses))
                checked += 1
        self.assertGreater(checked, 0)


if __name__ == '__main__':
    unittest.main()

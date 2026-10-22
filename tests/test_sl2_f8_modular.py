"""Exact modular SL2(F8) certificates, routing, and false-claim controls."""

import copy
from fractions import Fraction
import importlib.util
from itertools import permutations
import json
from pathlib import Path
from random import Random
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-sl2-f8-modular'
RESULTS = ROOT/'results/sl2-f8-modular-2026-10-21'
sys.path.insert(0, str(PACKAGE))


def load(name):
    spec = importlib.util.spec_from_file_location('sl2_f8_modular_'+name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verifier, routing = load('verify'), load('bit_permutations')


class Sl2F8ModularTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modules, cls.generators, cls.central = [
            json.loads((RESULTS/name).read_text())
            for name in ['modules-powers.json', 'left-generators.json', 'central.json']]

    def test_complete_independent_replay(self):
        receipt = verifier.verify(self.modules, self.generators, self.central)
        self.assertEqual(receipt['representation_products_checked'], 762048)
        self.assertEqual(receipt['group_action_columns_checked'], 254016)
        self.assertEqual(receipt['radical_power_dimensions'], [504, 379, 319, 256, 184, 121, 61, 0])
        self.assertEqual(receipt['power_products_checked'], 19800)
        self.assertTrue(receipt['six_packets_plus_M7_coordinate_excluded'])
        self.assertFalse(receipt['arbitrary_complex_maps_excluded'])
        self.assertFalse(receipt['improves_omega'])

    def test_routes_against_literal_permutations_and_invalid_inputs(self):
        for n in [1, 2, 4]:
            for p in permutations(range(n)):
                network = routing.route(p)
                for i, j in enumerate(p):
                    self.assertEqual(routing.apply(1 << i, network), 1 << j)
        rng = Random(20261021)
        for n in [8, 32, 512]:
            for unused in range(5):
                p = list(range(n))
                rng.shuffle(p)
                network = routing.route(p)
                value = rng.getrandbits(n)
                expected = sum(((value >> i) & 1) << p[i] for i in range(n))
                self.assertEqual(routing.apply(value, network), expected)
        for p in [[], [1], [0, 0], [0, 1, 2]]:
            with self.assertRaises(ValueError):
                routing.route(p)

    def test_corrupted_representation_and_kernel_are_rejected(self):
        bad = copy.deepcopy(self.modules)
        bad['natural'][0][0] ^= 1
        with self.assertRaises(ValueError):
            verifier.verify(bad, self.generators, self.central)
        bad = copy.deepcopy(self.modules)
        bad['powers'][0][0] = hex(int(bad['powers'][0][0], 16) ^ 1)
        with self.assertRaises(ValueError):
            verifier.verify(bad, self.generators, self.central)

    def test_rational_packet_margin_and_single_target_non_exclusions(self):
        bound = Fraction(self.central['source_bound'])
        self.assertEqual(bound, Fraction(1035637, 2304))
        self.assertLess(bound, 450)
        self.assertLess(74**3, 648**2)
        self.assertGreater(6*74+49, bound)
        saved = json.loads((ROOT/'results/semisimple-koszul-2026-10-21/frontiers.json').read_text())
        shapes = next(row['koszul_surviving_shapes'] for row in saved['sources']
                      if row['source'] == 'C[SL(2,F8)]')
        self.assertEqual(len(shapes), 16)
        for a, b, c in shapes:
            self.assertLess((a*b*c)**2, bound**3)
        self.assertIn([18, 18, 25], shapes)


if __name__ == '__main__':
    unittest.main()

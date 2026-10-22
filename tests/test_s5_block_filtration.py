"""Exact modular block certificate, actual new exclusions, and tamper controls."""

import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-s5-block-filtration'
RESULTS = ROOT/'results/s5-block-filtration-2026-10-21'
sys.path.insert(0, str(PACKAGE))


def load(name):
    spec = importlib.util.spec_from_file_location('s5_block_'+name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


blocks, frontier = load('blocks'), load('frontier')


class S5BlockFiltrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS/'certificate.json').read_text())
        cls.frontier = json.loads((RESULTS/'frontier.json').read_text())

    def test_exact_block_replay_and_baseline_products(self):
        receipt = blocks.verify(self.certificate)
        self.assertEqual(receipt['centrality_checks'], 120)
        self.assertEqual(receipt['baseline_group_products_checked'], 24360)
        self.assertEqual(receipt['baseline_representation_products_checked'], 28800)
        self.assertTrue(receipt['M20_coordinate_target_excluded'])
        self.assertFalse(receipt['M19_target_constructed'])
        self.assertEqual(blocks.certificate(), self.certificate)

    def test_exact_frontier_retains_general_and_coordinate_scopes(self):
        self.assertEqual(frontier.report(), self.frontier)
        first, second = self.frontier['sources']
        self.assertEqual(first['full_complex_koszul_survivor_count'], 6)
        self.assertEqual(first['additional_coordinate_exclusions_after_koszul'], [])
        self.assertEqual(second['full_complex_koszul_survivor_count'], 45)
        self.assertEqual(second['additional_coordinate_exclusions_after_koszul'],
                         [[20, 20, 20], [19, 20, 21]])
        m19 = next(r for r in second['records'] if r['shape'] == [19]*3)
        self.assertFalse(m19['coordinate_modular_excluded'])
        self.assertFalse(m19['complex_koszul_excluded'])

    def test_rejects_corrupted_block_and_root_certificates(self):
        for key, replacement in [('central_idempotent_32', '0x0'),
                                 ('baseline_sha256', '0'*64),
                                 ('scope', 'Arbitrary complex maps'),
                                 ('proof_status', 'formalized')]:
            bad = copy.deepcopy(self.certificate)
            bad[key] = replacement
            with self.assertRaises(ValueError):
                blocks.verify(bad)
        bad = copy.deepcopy(self.certificate)
        bad['block_layers'][0][0] += 1
        with self.assertRaises(ValueError):
            blocks.verify(bad)
        bad = copy.deepcopy(self.certificate)
        bad['comparison']['kappa_strict_upper'] = '188/100'
        with self.assertRaises(ValueError):
            blocks.verify(bad)
        bad = copy.deepcopy(self.certificate)
        bad['improves_omega'] = True
        with self.assertRaises(ValueError):
            blocks.verify(bad)

    def test_invalid_parameters_and_exact_target_margin(self):
        for t in [Fraction(0), Fraction(1), Fraction(2)]:
            with self.assertRaises(ValueError):
                blocks.comparisons(t=t)
        with self.assertRaises(ValueError):
            blocks.comparisons(kappa_upper=Fraction(188, 100))
        upper = Fraction(self.certificate['comparison']['central_factor_upper_bounds'][2])
        self.assertLess(upper, 389)
        self.assertLess(upper**3, (19*20*21)**2)
        self.assertLess(upper**3, 20**6)
        self.assertGreater(upper**3, 19**6)


if __name__ == '__main__':
    unittest.main()

"""Subgroup completeness, certified new cuts and evidence corruption controls."""
import copy
import hashlib
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-subgroup-ideal-catalog'
RESULTS = ROOT/'results/subgroup-ideal-catalog-2026-10-21'
sys.path.insert(0, str(PACKAGE))
import subgroup_catalog as catalog

spec = importlib.util.spec_from_file_location('verify_subgroup_catalog', PACKAGE/'verify_catalog.py')
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class SubgroupCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = catalog.read(RESULTS/'catalog.json.gz')
        cls.groups = catalog.ideal.sources()

    def test_complete_exact_saved_catalog(self):
        receipt = verifier.verify_report(self.report)
        self.assertEqual(receipt, json.loads((RESULTS/'verification.json').read_text()))
        self.assertEqual([r['subgroups'] for r in receipt], [76, 164, 215])
        self.assertEqual([r['conjugacy_classes'] for r in receipt], [12, 22, 31])
        self.assertEqual([r['minimal_cosets_per_leg'] for r in receipt],
                         [[204]*3, [754]*3, [648]*3])

    def test_lattice_against_all_subsets_of_a_small_group(self):
        G = {'mul': [[a ^ b for b in range(8)] for a in range(8)]}
        brute = set()
        for size in range(9):
            for H in combinations(range(8), size):
                if 0 in H and all(a ^ b in H for a in H for b in H):
                    brute.add(H)
        rows = catalog.lattice(G)
        self.assertEqual({tuple(r['members']) for r in rows}, brute)
        self.assertEqual(verifier.verify_lattice(G, rows), brute)
        with self.assertRaisesRegex(ValueError, 'extension-complete'):
            verifier.verify_lattice(G, [r for r in rows if r['members'] != [0, 1]])

    def test_new_noncyclic_cuts_are_not_subsumed_by_earlier_cosets(self):
        record = self.report['records'][1]
        cuts = record['minimal_forbidden_cosets'][0]
        old = [set(C) for C in cuts if len(C) in (2, 5)]
        new = [set(C) for C in cuts if len(C) in (4, 6)]
        self.assertEqual(len(new), 550)
        self.assertTrue(all(not any(K <= H for K in old) for H in new))
        # Another order-four class has dimension 101 and is not forbidden
        # by the M10 output threshold 100.
        allowed = next(r for r in record['ideal_classes']
                       if len(r['subgroup']) == 4 and r['ideal_dimension'] == 101)
        self.assertTrue(all(C not in cuts for C in allowed['cosets']))
        M = self.groups[1]['mul']
        for item in record['ideal_classes']:
            H = item['subgroup']
            if len(H) in (4, 6) and item['ideal_dimension'] in (76, 84):
                self.assertFalse(any(catalog.generated(self.groups[1], [g]) == tuple(H)
                                     for g in H))
                if len(H) == 4:
                    self.assertTrue(all(M[g][g] == 0 for g in H))

    def test_corrupt_rank_and_missing_cut_are_rejected(self):
        record = copy.deepcopy(self.report['records'][1])
        item = next(r for r in record['ideal_classes'] if len(r['subgroup']) == 4
                    and r['ideal_dimension'] == 84)
        item['integer_annihilators'][0][item['cosets'][0][0]] += 1
        with self.assertRaises(ValueError):
            verifier.verify(self.groups[1], record)
        record = copy.deepcopy(self.report['records'][1])
        record['minimal_forbidden_cosets'][0].pop()
        with self.assertRaisesRegex(ValueError, 'missing minimal'):
            verifier.verify(self.groups[1], record)

    def test_complete_catalog_is_adapted_without_weakening_a_cut(self):
        record = self.report['records'][1]
        combined, receipt = verifier.split_search_record(self.groups[1], record)
        self.assertEqual(combined['ideal_dimension'], 88)
        self.assertEqual(len(combined['cosets']), 754)
        self.assertEqual(receipt['minimal_cosets_per_leg'], [754]*3)
        self.assertLess(88, 10*10)
        control = json.loads((RESULTS/'encoding-control.json').read_text())
        witness = json.loads((ROOT/'results/sl2-five-native-2026-10-20/'
                              'split-control3.json').read_text())['witness']
        from group_exact import verify_witness
        self.assertEqual(verify_witness(self.groups[1], witness['sets'], witness['potentials']),
                         control['weighted_control'])
        self.assertEqual(control['verified_subgroup_catalog'], receipt)
        self.assertEqual(control['catalog_sha256'],
                         hashlib.sha256((RESULTS/'catalog.json.gz').read_bytes()).hexdigest())
        self.assertTrue(control['known_projection_and_signs_accepted'])

    def test_all_exported_construction_contradictions_replay(self):
        path = ROOT/'research/ai/2026-10-20-sl2-five-native-parity/verify.py'
        spec = importlib.util.spec_from_file_location('catalog_native_replay', path)
        native = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(native)
        report = json.loads((RESULTS/'split-target10.json').read_text())
        self.assertEqual(report['status'], 'time-limit')
        self.assertEqual(report['encoding']['subgroup_ideal'],
                         {'dimension': 88, 'coset_clauses': 2262})
        receipt = native.replay(RESULTS/'split-target10.json')
        self.assertEqual(receipt, json.loads((RESULTS/'search-verification.json').read_text()))
        self.assertEqual(receipt['certificates'], {'exact-parity': 32})
        self.assertFalse(receipt['witness'])


if __name__ == '__main__':
    unittest.main()

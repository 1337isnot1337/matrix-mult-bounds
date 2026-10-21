"""Exact higher Koszul bounds and independent unequal-graph controls."""
import copy
import json
from math import comb
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-f8-unequal'
RESULTS = ROOT/'results/f8-unequal-2026-10-20'
sys.path.insert(0,str(PACKAGE))
sys.path.insert(0,str(PACKAGE.parent/'2026-10-20-paired-sources'))
import koszul_tables
import pair_averaging
import source_frontier
import graph_certificate
from all_ranks import matrix_basic_rank
from verify_stream_reports import verify_report


def load(name):
    return json.loads((RESULTS/name).read_text())


class UnequalF8Tests(unittest.TestCase):
    def test_complete_pencils_and_corrupted_rank_or_coefficients(self):
        report = load('koszul-pencils.json')
        self.assertEqual(koszul_tables.verify(report)['pencils_replayed'],32)
        for change in ['rank','coefficient','dimension','duplicate']:
            bad = copy.deepcopy(report)
            row = bad['records'][0]
            if change=='rank':
                row['rank_lower_bound'] += 1
            elif change=='coefficient':
                row['integer_slices'][0][0][0] = 0.5
            elif change=='dimension':
                row['slice_dimension'] += 1
            else:
                bad['records'][-1] = copy.deepcopy(row)
            with self.assertRaises(ValueError):
                koszul_tables.verify(bad)

    def test_full_first_space_matches_independent_padded_formula(self):
        for p in [1,2,3]:
            d = 2*p+1
            for a in range(1,4):
                for b in range(1,4):
                    if a*b>d:
                        continue
                    slices = [[[int(t==i*b+j) for j in range(b)]
                               for i in range(a)] for t in range(d)]
                    expected = sum(comb(d-a*b,p-q)*matrix_basic_rank(b,a,q)
                                   for q in range(max(0,p-(d-a*b)),min(a*b-1,p)+1))
                    self.assertEqual(koszul_tables.rank_mod(koszul_tables.koszul_matrix(slices,p)),expected)

    def test_rank_one_divisor_and_rectangular_column_repetition(self):
        for p in [1,2,3]:
            slices = [[[t+1,2*(t+1)],[3*(t+1),6*(t+1)]] for t in range(2*p+1)]
            self.assertEqual(koszul_tables.rank_mod(koszul_tables.koszul_matrix(slices,p)),comb(2*p,p))
        row = next(r for r in load('koszul-pencils.json')['records'] if (r['a'],r['b'],r['p'])==(3,2,2))
        slices = [[[X[i%3][j%2] if i//3==j//2 else 0 for j in range(4)]
                   for i in range(6)] for X in row['integer_slices']]
        self.assertEqual(koszul_tables.rank_mod(koszul_tables.koszul_matrix(slices,2)),2*row['rank_lower_bound'])

    def test_complete_pair_averaging_and_missing_class_rejection(self):
        report = pair_averaging.replay(load('koszul-pencils.json'))
        self.assertEqual(report,load('pair-averaging-16-16-26.json'))
        self.assertEqual(report['bounded_count_patterns'],7140)
        self.assertEqual(report['unordered_pairs_with_repetition'],520710)
        self.assertGreater(report['target_averaged_rank_lower_bound']['numerator'],7*1280)
        with self.assertRaises(ValueError):
            pair_averaging.coverage(pair_averaging.classes(16)[:-1],16)

    def test_source_frontier_and_unconstructed_count_survivor(self):
        result = source_frontier.report()
        self.assertEqual(result,load('source-frontier.json'))
        self.assertEqual(len(result['rank_locus_surviving_shapes']),26)
        self.assertEqual(len(result['minimal_surviving_shapes']),12)
        counts = [[0,0,0,4,4,4,4],[0,4,4,0,4,4,4],[3]*7]
        receipt = pair_averaging.count_receipt(load('koszul-pencils.json'),counts)
        self.assertEqual(receipt,load('count-survivor-16-20-21.json'))
        self.assertTrue(receipt['pair_capacity_passes'])
        self.assertEqual([r['maximum_certified_rank'] for r in receipt['koszul_levels']],[108,360,1260])
        self.assertFalse(any(r['excluded'] for r in receipt['koszul_levels']))

    def test_full_support_positive_control_and_actual_search_limits(self):
        control = load('graph-control.json')
        self.assertTrue(verify_report(control)['exact_witness_replayed'])
        witness = control['witness']
        self.assertEqual(graph_certificate.check(control['base_columns'],control['fiber_counts'],witness['sets']),witness['graph_receipt'])
        self.assertEqual(control['shape'],[4,4,3])
        self.assertTrue(control['positive_control_only'])
        for kind in ['generic','dual']:
            actual = load('graph-16-20-21-'+kind+'.json')
            receipt = verify_report(actual)
            self.assertEqual(receipt['exact_cuts_replayed'],0)
            self.assertFalse(receipt['exact_witness_replayed'])
            self.assertFalse(receipt['unsat_proof_checked'])
            self.assertFalse(actual['improves_omega'])

    def test_nonlinear_normal_control_does_not_imply_pair_injection(self):
        base = [1,8,2,16,4,32]
        counts = [[4,4,4,4,0,0,0],[4,4,0,4,4,4,0],[3]*7]
        H = graph_certificate.scalar_order()
        sets = []
        for f in range(3):
            row = []
            for i,a in enumerate(H):
                for j in range(counts[f][i]):
                    value = (base[2*f] if j&1 else 0) ^ (base[2*f+1] if j&2 else 0)
                    if i==1 and j==3 and f<2:
                        value ^= base[2*(f+1)]
                    row.append((a-1)*64+value)
            sets.append(row)
        receipt = graph_certificate.check(base,counts,sets,require_pairs=False)
        self.assertEqual(receipt['normal_fiber_triples_checked'],140)
        self.assertEqual(receipt['non_affine_four_point_fibers'],2)
        self.assertIn(None,receipt['pair_map_sizes'])
        with self.assertRaises(ValueError):
            graph_certificate.check(base,counts,sets)


if __name__=='__main__':
    unittest.main()

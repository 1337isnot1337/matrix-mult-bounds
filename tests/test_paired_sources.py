"""Exact all-coefficient controls for paired-source obstructions."""
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from math import comb
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-paired-sources'
RESULTS = ROOT/'results/paired-sources-2026-10-20'


def load(name):
    spec = importlib.util.spec_from_file_location('paired_'+name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


paired = load('paired'); budgets = load('budgets')
all_ranks = load('all_ranks')


class PairedSourceTests(unittest.TestCase):
    def test_saved_exact_rank_and_threshold_report(self):
        self.assertEqual(paired.verification(),json.loads((RESULTS/'verification.json').read_text()))

    def test_every_kernel_basis_vector_has_exact_zero_image(self):
        for a in range(2,7):
            dimensions,terms = paired.source(a)
            supports = []
            for label in range(3*a-2):
                vector = paired.kernel_vector(a,label)
                self.assertTrue(vector)
                self.assertFalse(paired.first_koszul_image(terms,vector))
                supports.append(set(vector))
            self.assertEqual(sum(map(len,supports)),len(set.union(*supports)))

    def test_single_coefficient_kernel_corruption_is_detected(self):
        _,terms = paired.source(4)
        vector = paired.kernel_vector(4,4)
        vector[next(iter(vector))] += 1
        self.assertTrue(paired.first_koszul_image(terms,vector))

    def test_full_capacity_matrix_targets_have_larger_first_koszul_rank(self):
        for a in range(2,7):
            dimensions,terms = paired.matrix_blocks([(a,2*a-1,a)])
            rank = paired.first_rank_mod2(dimensions,terms)
            self.assertEqual(rank,a**3*(2*a-1))
            self.assertGreater(rank,a**3*(2*a-1)-(3*a-2))

    def test_minimum_slice_minor_by_independent_determinants(self):
        for a in range(2,5):
            for p0,q0 in [(0,0),(a-1,0),(0,a-1),(a-1,a-1)]:
                X = sp.Matrix(a,a,lambda p,q:0 if p<p0 or (p==p0 and q<q0)
                              else (p+q+2 if (p,q)==(p0,q0) else 2*p-q+1))
                matrix = paired.slice_matrix(a,X)
                rows = [y*(2*a-1)+q0+v for y in range(a) for v in range(a)]
                columns = [(p0+y)*a+v for y in range(a) for v in range(a)]
                self.assertEqual(matrix.extract(rows,columns).det(),X[p0,q0]**(a*a))

    def test_saved_budget_upper_certificate(self):
        blob = gzip.decompress((RESULTS/'budget-potential.json.gz').read_bytes())
        saved = json.loads((RESULTS/'budget-verification.json').read_text())
        self.assertEqual(hashlib.sha256(blob).hexdigest(),saved['table_decompressed_sha256'])
        actual = budgets.verify_certificate(json.loads(blob))
        self.assertEqual(actual,{k:v for k,v in saved.items() if k!='table_decompressed_sha256'})
        self.assertEqual(actual['integer_transitions_checked'],825458)
        self.assertEqual(len(budgets.shapes()),267)
        self.assertNotIn((4,7,4),budgets.shapes())

    def test_invalid_budget_potential_is_rejected(self):
        table = json.loads(gzip.decompress((RESULTS/'budget-potential.json.gz').read_bytes()))
        table[budgets.index(16,28,28)] -= 1
        with self.assertRaisesRegex(ArithmeticError,'induction'):
            budgets.verify_certificate(table)

    def test_excluded_target_also_fails_ordinary_restriction_screen(self):
        a,b = 6,10
        loss = 2*a*(2*a-1-b)
        self.assertGreater(a*a-loss,b)
        self.assertGreater((2*a-1)*b,3*a*a-2*a)

    def test_independent_all_power_coefficient_controls(self):
        self.assertEqual(all_ranks.controls(),json.loads((RESULTS/'all-power-controls.json').read_text()))

    def test_source_closed_formula_matches_cohomological_euler_sum(self):
        for a in range(2,9):
            D,v,N = a-1,a*a,a*(2*a-1)
            for p in range(v+1):
                kernel = all_ranks.choose(v,p-1)*(3*D+1)
                kernel += sum((-1)**j*comb(v,p-j)*((j-1)*D-1)*((j+2)*D+1)
                              for j in range(2,p+1))
                self.assertEqual(all_ranks.source_rank(a,p),N*comb(v,p)-kernel)

    def test_degree_only_matrix_formula_matches_full_partition_sum(self):
        for l,r in [(1,4),(4,1)]+[(l,r) for l in range(2,7) for r in range(2,7)]:
            full = all_ranks.matrix_basic_ranks(l,r)
            self.assertEqual(full,tuple(all_ranks.matrix_basic_rank(l,r,p) for p in range(l*r+1)))
            self.assertEqual(full,tuple(all_ranks.matrix_partition_rank(l,r,p) for p in range(l*r+1)))

    def test_complete_frontier_and_every_strict_rank_witness(self):
        saved = json.loads((RESULTS/'all-power-frontier.json').read_text())
        self.assertEqual([row['a'] for row in saved['records']],list(range(2,17)))
        total = excluded = early = 0
        for row in saved['records']:
            a = row['a'];v,N = a*a,a*(2*a-1)
            eligible = set();considered = 0
            # Enumerate by first-leg dimension and its divisors, independently
            # of the search's nested outer-dimension loops.
            for first in range(1,v+1):
                for l in range(1,first+1):
                    if first%l: continue
                    r = first//l
                    if l>r: continue
                    for b in range(1,N+1):
                        if max(l*b,b*r)>N: continue
                        considered += 1
                        if (36*l*b*r)**3>(6*a-2)**8: eligible.add((l,b,r))
            rejected = row['excluded_by_first_leg_Koszul']
            remaining = row['remaining_after_this_screen']
            actual = [tuple(x['shape']) for x in rejected+remaining]
            self.assertEqual(len(actual),len(set(actual)))
            self.assertEqual(set(actual),eligible)
            self.assertEqual(row['positive_shapes_mod_BC_exchange'],considered)
            if a<=13: self.assertFalse(remaining)
            for witness in rejected:
                power = witness['power'];shape = witness['shape']
                source = all_ranks.source_rank(a,power)
                target = all_ranks.padded_matrix_rank(shape,v,power)
                self.assertEqual((source,target),(witness['source_rank'],witness['target_rank']))
                self.assertGreater(target,source)
            for survivor in remaining:
                for power in range(v):
                    self.assertLessEqual(all_ranks.padded_matrix_rank(survivor['shape'],v,power),
                                         all_ranks.source_rank(a,power))
            total += len(actual)
            excluded += len(rejected)
            if a<=13: early += len(rejected)
        self.assertEqual((early,total,excluded),(239,723,695))


if __name__ == '__main__': unittest.main()

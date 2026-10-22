"""Exact sharpness, hypothesis and discovery controls for the gap proof."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-balanced-puncture-gap'
RESULTS = ROOT/'results/balanced-puncture-gap-2026-10-21'


def load(filename,name):
    spec = importlib.util.spec_from_file_location(name,PACKAGE/filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load('verify.py','puncture_gap_controls')
d = load('discover.py','puncture_gap_discovery')


def binary_dense_rank(matrix):
    rows = [[int(value)%2 for value in matrix.row(i)] for i in range(matrix.rows)]
    rank = 0
    for j in range(matrix.cols):
        pivot = next((i for i in range(rank,len(rows)) if rows[i][j]),None)
        if pivot is None:
            continue
        rows[rank],rows[pivot] = rows[pivot],rows[rank]
        for i in range(rank+1,len(rows)):
            if rows[i][j]:
                rows[i] = [a^b for a,b in zip(rows[i],rows[rank])]
        rank += 1
    return rank


class BalancedPunctureGapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.controls = json.loads((RESULTS/'controls.json').read_text())
        cls.discovery = json.loads((RESULTS/'binary-kernels.json').read_text())

    def test_saved_controls_and_local_dependency_pins(self):
        self.assertEqual(self.controls,v.reports())
        sources = json.loads((PACKAGE/'sources.json').read_text())
        for source in sources['local_dependencies']:
            self.assertEqual(hashlib.sha256((ROOT/source['path']).read_bytes()).hexdigest(),
                             source['sha256'])
        self.assertEqual(sources['external_sources'][0]['field'],'complex numbers')
        self.assertFalse(sources['external_sources'][0]['proof_rebuilt_locally'])

    def test_all_five_constant_rank_two_canonical_pencils(self):
        for record in self.controls['canonical_pencils']:
            matrix = v.decode(record['matrix'])
            for variable in ['s','t']:
                witness = record['rank_lower_minor_witnesses'][variable]
                determinant = sp.expand(matrix.extract(witness['rows'],witness['columns']).det())
                self.assertEqual(determinant,sp.sympify(witness['determinant'],
                                                       locals={'s':v.S,'t':v.T}))
                self.assertIn(determinant,[v.S**2,-v.S**2,v.T**2,-v.T**2])
            count = 0
            for rows in itertools.combinations(range(matrix.rows),3):
                for columns in itertools.combinations(range(matrix.cols),3):
                    count += 1
                    self.assertEqual(sp.expand(matrix.extract(rows,columns).det()),0)
            self.assertEqual(count,record['rank_upper_three_minors_checked'])

    def test_independent_signed_amplification_of_every_sharp_control(self):
        for record in self.controls['sharpness_and_hypothesis_controls']:
            matrices = [v.decode(m) for m in record['matrix_basis']]
            expected = []
            m,n = matrices[0].shape
            kept_rows = [i for i in range(2*m) if i not in record['row_kernel']]
            kept_cols = [j for j in range(2*n) if j not in record['column_kernel']]
            for matrix in matrices:
                for i,j in itertools.product(range(2),repeat=2):
                    expected.append(sp.Matrix(len(kept_rows),len(kept_cols),
                        lambda r,c: matrix[kept_rows[r]//2,kept_cols[c]//2]
                        if (kept_rows[r]%2,kept_cols[c]%2)==(i,j) else 0))
            self.assertEqual(expected,[v.decode(m) for m in record['projected_matrices']])
            self.assertEqual(v.rank(sp.Matrix.vstack(*(v.flat(m) for m in expected))),
                             record['projected_first_dimension'])
        with self.assertRaises(ValueError):
            v.amplified_images([sp.eye(3)],[0,0],[0,1])

    def test_all_binary_rref_kernels_have_correct_rational_lifts(self):
        spaces = d.spaces()
        self.assertEqual(spaces,self.discovery['kernel_space_enumeration'])
        self.assertEqual(len({tuple(s['rows']) for s in spaces}),651)
        for space in spaces:
            kernel = sp.Matrix([[((row>>j)&1) for j in range(6)] for row in space['rows']])
            quotient = d.rational_quotient(space)
            self.assertEqual(kernel*quotient.T,sp.zeros(2,4))
            self.assertEqual(v.rank(quotient),4)
        self.assertEqual(self.discovery['ordered_kernel_pairs'],423801)
        self.assertEqual(sum(self.discovery['binary_image_dimension_histogram'].values()),423801)
        self.assertEqual(self.discovery['binary_image_dimension_histogram'],
                         {'0':1,'4':267,'5':2403,'6':18274,'7':53712,'8':349144})
        self.assertEqual(self.discovery['rational_replay_histogram'],{'0':1})
        self.assertEqual(self.discovery['nonzero_rational_low_image_counterexamples'],[])

    def test_bitpacked_discovery_against_independent_dense_binary_contractions(self):
        spaces = d.spaces()
        skew = v.pencil_spaces()['L1_plus_L1T_as_skew']
        basis = [skew.subs({v.S:1,v.T:0}),skew.subs({v.S:0,v.T:1})]
        # Fixed complete coverage of a 5-by-5 cross of varied RREF charts.
        for i,j in itertools.product([0,13,127,500,650],repeat=2):
            left,right = d.rational_quotient(spaces[i]),d.rational_quotient(spaces[j])
            matrices = []
            for matrix in basis:
                for a,b in itertools.product(range(2),repeat=2):
                    unit = sp.zeros(2);unit[a,b] = 1
                    matrices.append(v.flat(left*sp.kronecker_product(matrix,unit)*right.T))
            self.assertEqual(binary_dense_rank(sp.Matrix.vstack(*matrices)),
                             d.binary_rank(d.image_vectors(spaces[i],spaces[j])))

    def test_complex_field_condition_and_sharpness_are_explicit(self):
        records = {r['name']:r for r in self.controls['sharpness_and_hypothesis_controls']}
        self.assertEqual(records['sharp_three_L2']['projected_first_dimension'],3)
        self.assertEqual(records['dimension_one_rank_three_counterexample']['projected_first_dimension'],2)
        self.assertEqual(records['rank_one_exclusion_is_essential']['projected_first_dimension'],2)
        matrix = v.S*sp.eye(2)+v.T*sp.Matrix([[0,-1],[1,0]])
        self.assertEqual(sp.expand(matrix.det()),v.S**2+v.T**2)
        self.assertEqual(v.rank(matrix.subs({v.S:1,v.T:sp.I})),1)
        self.assertTrue(self.controls['complex_field_required'])


if __name__=='__main__':
    unittest.main()

"""Exact controls for the unequal-length cyclic construction question."""
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys
import unittest

import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/"research/ai/2026-10-20-anisotropic-constructions"
sys.path.insert(0,str(PACKAGE))
spec=importlib.util.spec_from_file_location("anisotropic_verify",PACKAGE/"verify.py")
verify=importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)
import representation_packing as packing
import central_minrank as central
import slice_rank_gap as rank_gap
import singular_support as singular


class AnisotropicConstructionTests(unittest.TestCase):
    def test_six_factor_index_formula(self):
        a,b=2,3;m=a+b-1
        direct={}
        for i,j,p,q,r,s in product(range(a),range(b),range(a),range(b),range(a),range(b)):
            direct[((j,p,r+s),(i+j,q,r))]=(i,p+q,s)
        f=list(range(1,a*b*m+1))
        for row in product(range(b),range(a),range(m)):
            for col in product(range(m),range(b),range(a)):
                point=direct.get((row,col))
                expected=verify.coefficient(f,a,b,*point) if point else 0
                self.assertEqual(verify.slice_entry(f,a,b,row,col),expected)

    def test_minors_with_varied_extreme_coordinates(self):
        a,b=2,3;m=a+b-1
        for i,k,s in product(range(a),range(m),range(b)):
            f=[0]*(a*b*m)
            for ii in range(i+1):
                for ss in range(b if ii<i else s+1):
                    f[(ii*m+k)*b+ss]=1+ii+2*ss
            matrix,pivot=verify.triangular_minor(f,a,b)
            self.assertEqual(sp.Matrix(matrix).det(),pivot**(a*b))
        with self.assertRaises(ValueError):
            verify.triangular_minor([0]*(a*b*m),a,b)

    def test_conditional_arithmetic_and_frontier(self):
        self.assertGreater(404352**561,25**2250)
        self.assertLess(404352**2243,25**9000)
        sources=verify.source_frontier(160)
        passing=[(row['source_leg_dimension'],row['a'],row['b'],tuple(shape['shape']))
                 for row in sources for shape in row['improving_shapes']
                 if shape['passes_minimum_rank_screen']]
        self.assertEqual(passing,[(160,4,5,(12,12,13))])

    def test_saved_scope_and_representation_controls(self):
        actual=json.loads(json.dumps(verify.report()))
        saved=json.loads((ROOT/'results/anisotropic-constructions-2026-10-20/certificate.json').read_text())
        self.assertEqual(actual,saved)
        self.assertFalse(actual['target_constructed'])
        self.assertFalse(actual['new_exponent_established'])
        self.assertEqual(actual['selected_full_action']['fitting_triples'],0)
        self.assertTrue(all(x['fitting_triples']==0 for x in actual['selected_two_factor_actions']))
        self.assertEqual(sum(x['fitting_triples'] for x in actual['positive_representation_controls']),2)
        self.assertEqual(packing.tensor_product({1:1},{2:1}),{1:1,3:1})

    def test_central_coefficients_from_full_source(self):
        a,b=2,3;m=a+b-1
        terms={}
        for i,j,p,q,r,s in product(range(a),range(b),range(a),range(b),range(a),range(b)):
            if p+q==i+s and r+s==j+p and i+j==q+r:
                terms[((j,p),(q,r))]=(i,s)
        f=[2,-1,3,0,5,-2]
        for row in product(range(b),range(a)):
            for column in product(range(b),range(a)):
                point=terms.get((row,column))
                expected=f[point[0]*b+point[1]] if point is not None else 0
                self.assertEqual(central.central_entry(f,a,b,row,column),expected)

    def test_central_minor_and_all_binary_slices(self):
        records=json.loads(json.dumps(central.controls()))
        saved=json.loads((ROOT/'results/anisotropic-constructions-2026-10-20/central-minrank-controls.json').read_text())
        self.assertEqual(records,saved)
        self.assertEqual(sum(r['nonzero_slices'] for r in records),596)
        for a,b in ((2,4),(3,5),(4,5)):
            for i,s in product(range(a),range(b)):
                f=[0]*(a*b)
                for ii,ss in product(range(a),range(b)):
                    if ii+ss!=i+s or ii<=i:
                        f[ii*b+ss]=2+ii-ss
                f[i*b+s]=7
                matrix,pivot=central.central_minor(f,a,b)
                self.assertEqual(sp.Matrix(matrix).det(),pivot**a)
        with self.assertRaises(ValueError):
            central.central_minor([0]*20,4,5)

    def test_complete_torus_profiles_are_centrally_incompatible(self):
        location=ROOT/'results/anisotropic-constructions-2026-10-20'
        discovered=json.loads((location/'anisotropic-general-torus-weights.json').read_text())
        audited=json.loads((location/'torus_weight_audit.json').read_text())
        self.assertEqual(audited['valid_deficit_polynomials'],2819)
        self.assertEqual(audited['compatible_pairs'],73)
        self.assertEqual(audited['distinct_second_profiles'],68)
        expected=[r['vertex_profiles'] for r in discovered['compatible_triples']]
        self.assertEqual(audited['triples'],expected)
        self.assertEqual(len(expected),2)
        for triple in expected:
            vertex=[dict(profile) for profile in triple]
            for i,j in ((0,1),(1,2),(2,0)):
                self.assertEqual(sum(c*vertex[j].get(w,0) for w,c in vertex[i].items()),20)
            self.assertTrue(any(all(v.get(w)==1 for v in vertex) for w in vertex[0]))

    def test_biform_blocks_match_full_source(self):
        a,b=2,3;m=a+b-1
        f=[2,-3,5,7,0,-1]
        for k in range(m):
            full=[f[i*b+s] if kk==k else 0
                  for i,kk,s in product(range(a),range(m),range(b))]
            for p,q in product(range(a),range(b)):
                for j,long_row,long_column,r in product(range(b),range(m),range(m),range(a)):
                    actual=verify.slice_entry(full,a,b,(j,p,long_row),(long_column,q,r))
                    expected=rank_gap.biform_entry(f,a,b,(j,long_row),(long_column,r)) if p+q==k else 0
                    self.assertEqual(actual,expected)

    def test_rank_gap_controls_and_ordinary_target_exclusion(self):
        actual=json.loads(json.dumps(rank_gap.report()))
        saved=json.loads((ROOT/'results/anisotropic-constructions-2026-10-20/slice-rank-gap-controls.json').read_text())
        self.assertEqual(actual,saved)
        self.assertEqual(sum(r['nonzero_slices'] for r in actual['binary_biform_controls']),4684)
        self.assertEqual(actual['binary_full_source_control']['minimum_rank_slices'],27)
        selected=actual['selected_target']
        self.assertLess(selected['lifted_rank_upper_bound'],selected['source_next_rank_lower_bound'])
        self.assertGreater(selected['target_rank_one_locus_projective_dimension'],
                           selected['source_minimum_locus_projective_dimension'])
        rejected=actual['enhanced_frontier']['excluded_after_minimum_rank_screen']
        self.assertIn((4,5,(12,12,13)),[(r['a'],r['b'],tuple(r['shape'])) for r in rejected])
        self.assertFalse(actual['new_exponent_established'])
        self.assertFalse(actual['target_constructed'])

    def test_singular_faces_and_exact_saved_scope(self):
        actual=json.loads(json.dumps(singular.report()))
        saved=json.loads((ROOT/'results/anisotropic-constructions-2026-10-20/singular-support-controls.json').read_text())
        self.assertEqual(actual,saved)
        selected=next(row for row in actual['support_degenerations']
                      if row['a']==row['b']==5 and row['mode']=='parity110')
        self.assertEqual(selected['retained_parity_patterns'],{'000':3925,'011':3900,'101':3900})
        self.assertEqual(selected['active_leg_dimensions'],[225]*3)
        self.assertEqual(selected['minimum_coordinate_slice_ranks'],[12]*3)
        ranks=actual['exact_parity_slice_controls']
        self.assertEqual([r['exact_rank_mod_prime'] for r in ranks[0]['slices']],[224]*3)
        self.assertEqual([r['exact_rank_mod_prime'] for r in ranks[1]['slices']],[225]*3)
        self.assertFalse(actual['new_exponent_established'])
        self.assertFalse(actual['improving_target_constructed'])

    def test_singular_scores_and_conditional_integer_certificates(self):
        for row in singular.exact_step_certificates():
            self.assertLess(int(row['integer_comparison']['left']),
                            int(row['integer_comparison']['right']))
        parity=singular.exact_parity_certificates()
        self.assertEqual(parity[1]['capacity_cubed'],['9625057','1'])
        self.assertEqual(parity[1]['target_leg_dimension_cubed'],9528128)
        direct=singular.conditional_direct_sum_certificates()[0]
        self.assertGreater(84**2243,20708**1000)
        self.assertGreater(24**2243,1246**1000)
        self.assertGreater(20708+1246,28**3)
        self.assertFalse(direct['target_constructed'])
        self.assertFalse(direct['new_exponent_established'])

    def test_parity_monomial_control_from_full_coefficient_formula(self):
        a,b=2,3;m=a+b-1
        witness=singular.exact_monomial_control(a,b)
        x,y,z=witness['source_coordinates_per_target_leg']
        for ix,iy,iz in product(range(a*a),range(a*b),range(a*b)):
            f=[0]*(a*b*m)
            f[x[ix]]=1
            sy,sz=y[iy],z[iz]
            yr=(sy//(a*m),(sy//m)%a,sy%m)
            zc=(sz//(a*b),(sz//a)%b,sz%a)
            coefficient=verify.slice_entry(f,a,b,yr,zc)
            i,j=divmod(ix,a)
            jj,k=divmod(iy,b)
            kk,ii=divmod(iz,a)
            self.assertEqual(coefficient,int(i==ii and j==jj and k==kk))


if __name__=='__main__':
    unittest.main()

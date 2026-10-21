"""Independent gate arithmetic, geometric controls and exact score replay."""
import importlib.util
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-hankel-wronskian-cap'
RESULTS=ROOT/'results/hankel-wronskian-cap-2026-10-21'


def load(name):
    spec=importlib.util.spec_from_file_location('hankel_section_'+name,PACKAGE/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


g=load('geometry');app=load('application')


def cap_from_statement(r,k):
    if 2*r<=k*(k+2):return r
    candidates=[]
    for p in range(1,r+1):
        for q in range(1,r+1):
            if min(p,q)<=k:candidates.append(r)
            else:candidates.append(min(p*q,r+(q-k)*((r-p)//(k-1)),r+(p-k)*((r-q)//(k-1))))
    return max(candidates)


def check_witness(a,shape,w):
    G=a*a;N=G*(2*a-1);x,y=w['parameter_dimensions']
    # Find z by the multiset rather than trusting a repeated coordinate order.
    remaining=list(shape);remaining.remove(x);remaining.remove(y);z=remaining[0]
    k=w['matrix_input_rank'];assert 2<=k<=min(x,y)
    loss=(N-y*z)+(N-x*z);assert loss>=0
    source=k*z+loss
    if w['gate']=='uniform_hankel_higher_input':
        r=w['symbol_rank'];assert 1<=r<a
        cap=cap_from_statement(r,k);assert cap==w['scalar_image_dimension_cap']
        assert source==w['source_lift_rank_upper']<(r+1)*G
        assert x*y>cap*G and w['full_dimension_cap']==cap*G
        if w['method']=='hankel_boundary_saturation':assert 2*r==k*(k+2)
        elif w['method']=='projection_saturation':assert 2*r<k*(k+2)
        else:assert 2*r>k*(k+2)
    else:
        assert w['gate']=='full_symbol_crossed_locus'
        assert w['full_symbol_rank']==a and w['lower_symbol_rank']==a-1
        cap=cap_from_statement(a-1,k);assert cap==w['lower_symbol_image_cap']
        assert x*y>cap*G
        R=source-(G-1)*a;assert R==w['crossed_rank_upper'] and R>=1
        old=min(N,2*a*R);proper=x*y<N;upper=old-int(proper)
        assert w['source_lift_rank_upper']==source
        assert w['unsectioned_crossed_dimension_upper']==old
        assert w['proper_source_parameter_subspace']==proper
        assert w['crossed_locus_dimension_upper']==upper
        assert w['rank_parameter_variety_dimension']==k*(x+y-k)>upper


class HankelSectionTests(unittest.TestCase):
    def test_geometry_reports_and_action_hypotheses(self):
        x=json.loads((RESULTS/'geometry.json').read_text());self.assertEqual(x,g.report())
        self.assertEqual(len(x['crossed_action_controls']),25)
        for c in x['crossed_action_controls']:
            self.assertEqual(c['basis_action_graph_reachable'],c['coefficient_dimension'])
            self.assertTrue(c['action_identity_verified']);self.assertTrue(c['binary_reversal_identity_verified'])
        for c in x['hankel_boundary_degree_controls']:
            self.assertEqual(c['target_dimension'],c['rank_parameter_hypersurface_dimension'])
            self.assertGreater(c['hankel_determinant_degree'],c['matrix_determinant_degree'])
            self.assertNotEqual(c['nonzero_hankel_determinant_derivative'],0)
        self.assertFalse(x['reducible_representation_countercontrol']['component_stability_alone_suffices'])

    def test_proper_section_is_conditional_and_sharp(self):
        self.assertEqual(g.crossed_dimension_cap(1,2,1,2),(2,3,True))
        self.assertEqual(g.crossed_dimension_cap(1,2,1,4),(3,3,False))
        self.assertEqual(g.crossed_dimension_cap(12,12,16,2500),(383,384,True))
        with self.assertRaises(ValueError):g.crossed_dimension_cap(2,3,0,4)
        with self.assertRaises(ValueError):g.crossed_dimension_cap(2,3,1,25)
        a,b,c,d=sp.symbols('a b c d');det=sp.Matrix([[a,b],[c,d]]).det()
        self.assertEqual(det.subs({c:0,d:0}),0)
        self.assertNotEqual(det,0)
        self.assertEqual(len(sp.factor_list(sp.Symbol('x')*sp.Symbol('y'))[1]),2)

    def test_hankel_specific_equality_and_generic_ruling_bounds(self):
        for r,k,expected in [(4,2,4),(12,4,12),(24,6,24),(5,2,7),(6,2,10),(8,3,11),(9,3,13)]:
            self.assertEqual(app.image_cap(r,k)[0],expected)
        self.assertEqual(app.image_cap(4,2)[1],'hankel_boundary_saturation')
        with self.assertRaises(ValueError):app.image_cap(3,1)
        # Generic closed targets do not inherit the Hankel equality extension:
        # Mat3's determinant hypersurface has dimension8 and degree3, not5.

    def test_all_rectangular_comparison_witnesses(self):
        x=json.loads((RESULTS/'rectangular.json').read_text());self.assertEqual(x,app.rectangular_report())
        old=json.loads((ROOT/'results/hankel-pencil-degree-2026-10-21/rectangular.json').read_text())
        self.assertEqual(x['additional_higher_input_exclusions'],254)
        self.assertEqual(x['remaining_necessary_test_survivors'],240)
        changes=0
        for s,prior in zip(x['sources'],old['sources']):
            self.assertEqual(s['a'],prior['a'])
            for row,previous in zip(s['records'],prior['records']):
                self.assertEqual(row['shape'],previous['shape'])
                if previous['excluded']:self.assertEqual(row,previous)
                elif row['excluded']:
                    changes+=1;check_witness(s['a'],row['shape'],row['witness'])
                else:self.assertIsNone(row['witness'])
        self.assertEqual(changes,254)
        self.assertEqual([len(s['survivors']) for s in x['sources'] if s['a']>=10],[9,62,169])
        self.assertFalse(x['singular_degenerations_excluded']);self.assertFalse(x['improves_omega'])

    def test_complete_square_partition_reports_and_scores(self):
        x=json.loads((RESULTS/'squares.json').read_text());self.assertEqual(x,app.square_report())
        expected=[94620376379,140053290292,202837340823,283043244655,378403133788]
        for source,numerator in zip(x['sources'],expected):
            a=source['a'];N=source['source_leg_dimension'];maximum=source['maximum']
            self.assertEqual(len(source['dimension_frontier']),N)
            self.assertEqual(maximum['upper_score_numerator'],numerator)
            for row in source['dimension_frontier']:
                D=row['target_leg_dimension'];shape=row['maximizing_relaxed_partition']
                if shape is None:continue
                self.assertEqual(sum(n*n for n in shape),D)
                self.assertEqual(sum(app.prior.squares.score_interval(n)[1] for n in shape),row['upper_score_numerator'])
                self.assertTrue(all(n in row['allowed_nonscalar_sizes'] for n in shape if n>1))
                if 1 in shape:self.assertTrue(row['scalars_allowed'])
                if shape.count(1)>1:self.assertTrue(row['repeated_scalars_allowed'])
                self.assertLessEqual(row['upper_score_numerator'],maximum['upper_score_numerator'])
            if a<=9:
                self.assertTrue(source['all_partitions_below_critical_score'])
                self.assertLess(numerator,source['critical_score_threshold']*10**6)
            else:self.assertFalse(source['all_partitions_below_critical_score'])
        self.assertFalse(x['candidate_constructed']);self.assertFalse(x['improves_omega'])

    def test_exact_equality_case_and_one_unit_countercontrol(self):
        w=app.additional_witness(12,12,50,50,50,2*(3312-2546))
        self.assertIsNotNone(w);self.assertEqual(w['unsectioned_crossed_dimension_upper'],384)
        self.assertEqual(w['crossed_locus_dimension_upper'],383)
        self.assertEqual(w['rank_parameter_variety_dimension'],384)
        self.assertNotIn(50,app.allowed_blocks(12,12,2546)[0])
        self.assertIn(50,app.allowed_blocks(12,12,2545)[0])
        # The known A810 source slice at641 cannot be rounded down to640.
        # This particular arithmetic filter leaves that historical target;
        # its stronger concurrent critical-state exclusion is a separate proof.
        self.assertIsNone(app.additional_witness(8,10,32,33,33,575))
        self.assertEqual(641-(80-1)*8,9)
        self.assertEqual(g.crossed_dimension_cap(8,10,9,1056),(162,163,True))


if __name__=='__main__':unittest.main()

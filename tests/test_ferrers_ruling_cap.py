"""Independent partitions, exact Jacobians and ordinary-application replay."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-ferrers-ruling-cap'
RESULTS=ROOT/'results/ferrers-ruling-cap-2026-10-21'


def load(name):
    s=importlib.util.spec_from_file_location('test_ferrers_'+name,PACKAGE/(name+'.py'))
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


v=load('verify');app=load('application')


def brute_partitions(r,k):
    all_best=0;proper_best=None
    for row in itertools.combinations_with_replacement(range(r+1),r):
        shape=list(reversed(row))
        if sum(shape[:k])>r or sum(min(k,x) for x in shape)>r:continue
        area=sum(shape);all_best=max(all_best,area)
        if len(shape)>k and shape[k]>k:
            proper_best=max(proper_best or 0,area)
    return all_best,proper_best


def witness_cap(r,k):
    # Independent complete-diagram DP, not the production closed formula.
    _,proper,_=v.partition_optima(r,k)
    return r if proper is None else max(r,proper)


def check_witness(a,shape,w):
    G=a*a;N=G*(2*a-1);x,y=w['parameter_dimensions']
    remaining=list(shape);remaining.remove(x);remaining.remove(y);z=remaining[0]
    k=w['matrix_input_rank'];loss=(N-y*z)+(N-x*z);R=k*z+loss
    if w['gate']=='uniform_hankel_higher_input':
        r=w['symbol_rank'];assert 1<=r<a
        cap=witness_cap(r,k)
        assert R==w['source_lift_rank_upper']<(r+1)*G
        assert cap==w['scalar_image_dimension_cap'] and x*y>cap*G
        assert w['full_dimension_cap']==cap*G and w['linear_hankel_space_cap']==r
    else:
        assert w['gate']=='full_symbol_crossed_locus'
        cap=witness_cap(a-1,k);assert cap==w['lower_symbol_image_cap'] and x*y>cap*G
        crossed=R-(G-1)*a;assert crossed==w['crossed_rank_upper']>=1
        dim=min(N,2*a*crossed)-int(x*y<N)
        assert w['crossed_locus_dimension_upper']==dim<k*(x+y-k)


class FerrersRulingTests(unittest.TestCase):
    def test_saved_independent_partition_and_jacobian_controls(self):
        x=json.loads((RESULTS/'controls.json').read_text());self.assertEqual(x,v.report())
        self.assertEqual(len(x['partition_optima']),125)
        self.assertEqual(len(x['ferrers_jacobians']),51)
        for row in x['ferrers_jacobians']:
            self.assertTrue(row['full_rank_jacobian_iff_durfee_at_most_k'])

    def test_separate_full_partition_enumeration(self):
        for r in range(1,7):
            for k in range(1,r+2):
                actual=brute_partitions(r,k)
                self.assertEqual(actual,v.partition_optima(r,k)[:2])
                self.assertEqual(actual[0],v.ruling_cap(r,k))

    def test_dominance_and_hypotheses_cannot_be_dropped(self):
        self.assertEqual(v.ruling_cap(5,2),7)
        self.assertEqual(v.closed_target_cap(5,2),(5,'linear_space_saturation'))
        hook=[4,1,1,1]
        self.assertTrue(v.jacobian_control(hook,1)['dominant_on_rank_k'])
        self.assertEqual(v.ruling_budgets(hook,2),(5,5))
        self.assertEqual(v.closed_target_cap(6,2)[0],9)
        self.assertFalse(v.jacobian_control([3,3,3],2)['dominant_on_rank_k'])
        for r,k in [(0,1),(1,0),(-1,2)]:
            with self.assertRaises(ValueError):v.ruling_cap(r,k)
            with self.assertRaises(ValueError):v.closed_target_cap(r,k)
        # The hook projection's dense image omits(0,1,1). Its three
        # factor equations have the unit ideal; this protects closedness.
        u1,u2,v1,v2=sp.symbols('u1 u2 v1 v2')
        ideal=sp.groebner([u1*v1,u1*v2-1,u2*v1-1],u1,u2,v1,v2)
        self.assertEqual([p.as_expr() for p in ideal.polys],[1])

    def test_sharpened_caps_and_exact_nondominant_extremizers(self):
        for r,k,generic,closed in [(7,2,11,11),(9,2,18,18),(8,3,11,8),
                                    (10,3,15,10),(11,3,17,11),(12,3,19,16)]:
            self.assertEqual(v.ruling_cap(r,k),generic)
            self.assertEqual(v.closed_target_cap(r,k)[0],closed)
        for r in range(1,21):
            for k in range(1,8):
                if r<k*(k+1):continue
                shape=v.square_extension(r,k)
                self.assertGreater(v.durfee(shape),k)
                self.assertEqual(sum(shape),v.closed_target_cap(r,k)[0])
                self.assertLessEqual(max(v.ruling_budgets(shape,k)),r)

    def test_all_new_rectangular_certificates_and_preserved_records(self):
        x=json.loads((RESULTS/'rectangular.json').read_text());self.assertEqual(x,app.rectangular_report())
        old=json.loads((ROOT/'results/hankel-wronskian-cap-2026-10-21/rectangular.json').read_text())
        changes=0
        for source,base in zip(x['sources'],old['sources']):
            for row,previous in zip(source['records'],base['records']):
                self.assertEqual(row['shape'],previous['shape'])
                if previous['excluded']:self.assertEqual(row,previous)
                elif row['excluded']:
                    changes+=1;check_witness(source['a'],row['shape'],row['witness'])
        self.assertEqual(changes,67)
        self.assertEqual(x['additional_ferrers_exclusions'],67)
        self.assertEqual(x['remaining_necessary_test_survivors'],173)
        self.assertEqual([len(s['survivors']) for s in x['sources'] if s['a']>=10],[5,38,130])
        self.assertFalse(x['candidate_constructed']);self.assertFalse(x['improves_omega'])

    def test_all_square_frontiers_and_every_saved_score(self):
        x=json.loads((RESULTS/'squares.json').read_text());self.assertEqual(x,app.square_report())
        old=json.loads((ROOT/'results/hankel-wronskian-cap-2026-10-21/squares.json').read_text())
        expected=[93741340669,140053290292,202837340823,281261289312,376216828388]
        for source,base,numerator in zip(x['sources'],old['sources'],expected):
            self.assertEqual(source['maximum']['upper_score_numerator'],numerator)
            self.assertEqual(len(source['dimension_frontier']),source['source_leg_dimension'])
            for row,previous in zip(source['dimension_frontier'],base['dimension_frontier']):
                self.assertEqual(row['target_leg_dimension'],previous['target_leg_dimension'])
                self.assertTrue(set(row['allowed_nonscalar_sizes'])<=set(previous['allowed_nonscalar_sizes']))
                if previous['upper_score_numerator'] is None:
                    self.assertIsNone(row['upper_score_numerator'])
                elif row['upper_score_numerator'] is not None:
                    self.assertLessEqual(row['upper_score_numerator'],previous['upper_score_numerator'])
                shape=row['maximizing_relaxed_partition']
                if shape is None:continue
                self.assertEqual(sum(n*n for n in shape),row['target_leg_dimension'])
                self.assertEqual(sum(app.prior.prior.squares.score_interval(n)[1] for n in shape),row['upper_score_numerator'])
            self.assertEqual(source['all_partitions_below_critical_score'],source['a']<=9)
        self.assertFalse(x['singular_degenerations_excluded']);self.assertFalse(x['improves_omega'])


if __name__=='__main__':unittest.main()

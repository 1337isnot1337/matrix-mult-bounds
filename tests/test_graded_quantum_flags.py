"""Independent coefficient and minor controls for leading-map obstructions."""
import importlib.util
import json
from pathlib import Path
import unittest
import sympy as sp
from itertools import product

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-20-graded-quantum-flags'
RESULTS=ROOT/'results/graded-quantum-flags-2026-10-20'

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

one=load('one_leg_flags',PACKAGE/'one_leg.py')
profiles=load('independent_profiles',PACKAGE/'profiles.py')
canonical=load('canonical_cartan',ROOT/'research/ai/2026-10-20-cyclic-equivariant/torus.py')
cyclic=load('canonical_cyclic',ROOT/'research/ai/2026-10-20-cyclic-mixed-map/verify.py')


class GradedQuantumFlagTests(unittest.TestCase):
    def test_independent_integer_recursion_matches_canonical_classification(self):
        actual=profiles.report();saved=json.loads((RESULTS/'profiles.json').read_text())
        self.assertEqual(actual,saved)
        reference=canonical.report()
        pairs=[{'deleted':r['deficit'],'shift':r['monomial_shift'],'factor10':f,'factor11':g}
               for r in reference['records'] for f,g in r['positive_factor_pairs']]
        self.assertEqual(sorted(actual['large_leg_factorizations'],key=str),sorted(pairs,key=str))
        target=actual['solutions'][0];ref=reference['surviving_vertex_characters'][0]
        self.assertEqual((target['U10'],target['W10'],target['V11']),(ref['U'],ref['V'],ref['W']))
        square=profiles.convolution(target['U10'],target['W10'])
        self.assertEqual((square[4],square[8]),(12,12))

    def test_rational_factorization_is_an_independent_oracle(self):
        x=sp.Symbol('x');records=[];S=profiles.report()['source_character']
        for i in range(13):
            for j in range(i,13):
                P=list(S);P[i]-=1;P[j]-=1
                if min(P)<0:continue
                shift=next(k for k,c in enumerate(P) if c)
                polynomial=sp.Poly(sum(c*x**k for k,c in enumerate(P[shift:])),x)
                content,factors=sp.factor_list(polynomial)
                self.assertEqual(content,1)
                for powers in product(*(range(e+1) for f,e in factors)):
                    A=sp.Poly(sp.prod(f.as_expr()**e for (f,_),e in zip(factors,powers)),x)
                    if A.eval(1)!=10 or any(c<0 for c in A.all_coeffs()):continue
                    B=polynomial.exquo(A)
                    if B.eval(1)!=11 or any(c<0 for c in B.all_coeffs()):continue
                    records.append({'deleted':[i,j],'shift':shift,
                                    'factor10':[int(c) for c in reversed(A.all_coeffs())],
                                    'factor11':[int(c) for c in reversed(B.all_coeffs())]})
        self.assertEqual(sorted(records,key=str),sorted(profiles.report()['large_leg_factorizations'],key=str))

    def test_exact_source_projection_matches_the_existing_cyclic_convention(self):
        for a in [2,3]:
            width=2*a-1;degree=width-1;V=a*a*width
            identity={(i,i):1 for i in range(V)}
            actual=one.projected_source(a,identity,identity)
            expected=[{} for _ in range(V)]
            for A,B,C in cyclic.source_terms(a):
                i,k,s=A//(width*a),(A//a)%width,A%a
                j,p,z=B//(a*width),(B//width)%a,B%width
                h,q,r=C//(a*a),(C//a)%a,C%a
                u=(i*a+s)*width+degree-k
                v=(p*a+j)*width+degree-z
                w=(r*a+q)*width+degree-h
                expected[u][v*V+w]=expected[u].get(v*V+w,0)+1
            self.assertEqual(actual,expected)

    def test_all_number_field_supports_and_modular_minors_replay(self):
        self.assertTrue(all(one.PRIME%d for d in range(2,sp.integer_nthroot(one.PRIME,2)[0]+1)))
        actual=one.report();saved=json.loads((RESULTS/'one-leg-certificates.json').read_text())
        self.assertEqual(actual,saved)
        ceilings={r['order']:r['slice_rank_upper_bound_for_all_one_leg_Laurent_limits'] for r in actual['records']}
        self.assertEqual(ceilings,{3:104,4:62,6:104,8:44,12:64,16:68,24:86})
        graded=actual['graded_order_three_six_controls']
        self.assertEqual(graded['phase_pairs_checked'],16)
        self.assertEqual(graded['source_central_dimension'],graded['target_central_dimension'])
        for witness in graded['nonzero_coefficient_witnesses']:
            self.assertNotEqual(witness['coefficient_mod_prime'],0)
            self.assertTrue(set(witness['retained_row_grades']).isdisjoint(graded['full_target_grades_lost_on_each_large_leg']))
            self.assertLess(witness['rank_upper_bound_from_row_support'],graded['target_minimum_nonzero_first_slice_rank'])

    def test_a_duplicate_minor_column_is_detected(self):
        saved=json.loads((RESULTS/'one-leg-certificates.json').read_text())['records'][0]
        _,matrix=one.root_map(4,saved['order'])
        rows=one.projected_source(4,matrix,matrix)
        columns=list(saved['minor_columns']);columns[0]=columns[1]
        bad=[[rows[i].get(j,0) for j in columns] for i in saved['minor_rows']]
        self.assertEqual(one.determinant_mod(bad),0)

    def test_sharp_nonordinary_laurent_fixture_with_nontrivial_bound(self):
        t=sp.Symbol('t')
        tensor={(2*b+c,b,c):sp.Integer(1) for b in range(2) for c in range(2)}
        tensor[4,2,2]=sp.Integer(1)
        # The last first-leg row has a genuine pole; two regular legs cancel it.
        first=[1,1,1,1,t**-2];other=[1,1,t]
        transformed={key:sp.cancel(value*first[key[0]]*other[key[1]]*other[key[2]])
                     for key,value in tensor.items()}
        self.assertEqual(transformed,tensor)
        constant_rows=[{b*3+c:1} for b in range(2) for c in range(2)]+[{}]
        row_ids,_=one.independent_minor(constant_rows)
        self.assertEqual(5-len(row_ids)+2,3)
        # Two B slices for the outer-product block, plus the separate A slice.
        decomposition={(2*b+c,b,c):sp.Integer(1) for b in range(2) for c in range(2)}
        decomposition[4,2,2]=1
        self.assertEqual(decomposition,tensor)
        diagonal={(new,b,c):value for new,old in enumerate([0,3,4])
                  for (a,b,c),value in tensor.items() if a==old}
        self.assertEqual(diagonal,{(i,i,i):1 for i in range(3)})


if __name__=='__main__':unittest.main()

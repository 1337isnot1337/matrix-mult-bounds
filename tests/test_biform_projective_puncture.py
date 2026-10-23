"""Replay all projective incidence cases without a generic-point assumption."""
import copy
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-biform-balanced-puncture'
RESULTS = ROOT/'results/biform-balanced-puncture-2026-10-21'
spec = importlib.util.spec_from_file_location('projective_puncture',PACKAGE/'projective.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
v = p.v


def replay_case(record):
    gi,li = record['g_case'],record['line_case']
    _,_,_,generators = p.generators(gi,li)
    assert (v.decode(record['syzygies'])-generators).applyfunc(sp.expand)==sp.zeros(36,3)
    matrix = v.decode(record['system'])
    assert matrix == (v.core_data()['annihilator']*sp.diag(
        generators,generators)).applyfunc(sp.expand)
    minor = matrix.extract(record['unit_minor_rows'],record['unit_minor_columns'])
    assert sp.expand(minor.det()) == record['unit_minor_determinant'] in [1,-1]
    if minor.rows==6:
        assert record['status']=='empty' and record['pair_kernel_dimension']==0
        return
    direction = v.decode(record['kernel_direction'])
    residual = v.decode(record['residual'])
    assert direction[record['free_coordinate']]==1
    assert (matrix*direction-residual).applyfunc(sp.expand)==sp.zeros(60,1)
    if record['status']=='empty':
        i,j = record['unit_residual_rows']
        assert sp.expand(residual[i]+record['unit_residual_second_coefficient']*residual[j]) == record['unit_residual_constant'] in [1,-1]
    elif gi==0:
        c,d,e = v.C,v.D,v.E
        assert residual.subs({d:-c,e:-c**2}).applyfunc(sp.expand)==sp.zeros(60,1)
        identity = record['reverse_ideal_identities']
        i,j = identity['first_row'],identity['second_row']
        assert sp.expand(residual[i]-identity['first_sign']*(c+d))==0
        coefficient = sp.sympify(identity['first_generator_coefficient'],
                                 locals={str(z):z for z in (v.A,v.B,c,d,e)})
        assert sp.expand(residual[j]-identity['second_sign']*(d**2+e)
                         -coefficient*(c+d))==0
    else:
        assert gi==3 and residual==sp.zeros(60,1)


class ProjectivePunctureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((RESULTS/'projective.json').read_text())

    def test_complete_disjoint_case_cover_and_saved_generation(self):
        self.assertEqual(self.report,p.certificate())
        records = self.report['cases']
        self.assertEqual(len(records),16)
        self.assertEqual({(r['g_case'],r['line_case']) for r in records},
                         set(itertools.product(range(4),repeat=2)))
        self.assertEqual(sum(len(r['unit_minor_rows'])==6 for r in records),5)
        self.assertEqual(sum(r.get('unit_residual_rows') is not None for r in records),3)
        self.assertEqual(sum(r['pair_kernel_dimension']==1 for r in records),8)

    def test_all_unit_minors_reverse_ideals_and_empty_cases(self):
        for record in self.report['cases']:
            with self.subTest(g_case=record['g_case'],line_case=record['line_case']):
                replay_case(record)
        corrupt = copy.deepcopy(self.report['cases'][0])
        corrupt['unit_minor_determinant'] *= -1
        with self.assertRaises(AssertionError):
            replay_case(corrupt)

    def test_every_projective_normal_family_uses_the_actual_core(self):
        core = v.core_data()['core']
        for record in self.report['cases']:
            if record['pair_kernel_dimension']!=1:
                continue
            gi,li = record['g_case'],record['line_case']
            g,lx,ly,_ = p.generators(gi,li)
            substitution = {v.D:-v.C,v.E:-v.C**2} if gi==0 else {}
            g = sp.expand(g.subs(substitution)) if hasattr(g,'subs') else g
            hs = [h for j,h in enumerate(v.H_MONOMIALS) if j!=gi]
            direction = v.decode(record['kernel_direction']).subs(substitution)
            h0 = sp.expand(sum(direction[j]*hs[j] for j in range(3)))
            h2 = sp.expand(sum(direction[3+j]*hs[j] for j in range(3)))
            _,_,matrices = v.syzygies(g,lx,ly,[h0,h2])
            zero = sp.zeros(36,1)
            m0,m2 = map(v.flat,matrices)
            expected = sp.Matrix.vstack(m0,zero,m2,zero).row_join(
                sp.Matrix.vstack(zero,m0,zero,m2))
            normal = v.decode(record['normal_family'])
            self.assertEqual((core*normal-expected).applyfunc(sp.expand),sp.zeros(144,2))
            # The two h classes modulo g are independent at every parameter:
            # their coefficient matrix has a constant unit 3-by-3 minor.
            classes = sp.Matrix.hstack(*(v.coefficient_vector(h,v.H_MONOMIALS)
                                        for h in [g,h0,h2]))
            determinants = [sp.expand(classes[list(rows),:].det())
                            for rows in itertools.combinations(range(4),3)]
            self.assertTrue(any(d in [1,-1] for d in determinants))
            for matrix in matrices:
                self.assertEqual((v.multiplication()*v.flat(matrix)).applyfunc(sp.expand),
                                 sp.zeros(16,1))

    def test_homogeneous_conic_equations_and_both_parameter_charts(self):
        r,s = sp.symbols('r s')
        g00,g10,g01,g11 = r**2,r*s,-r*s,-s**2
        self.assertEqual(sp.expand(g10+g01),0)
        self.assertEqual(sp.expand(g00*g11+g10**2),0)
        # First nonzero g coefficient x or y cannot lie on this conic.
        self.assertEqual((g00*g11+g10**2).subs({r:0}),0)
        for case in self.report['cases']:
            self.assertEqual(case['status']=='empty',case['g_case'] in [1,2])
        self.assertFalse(self.report['all_later_tensor_coefficients_verified'])


if __name__ == '__main__':
    unittest.main()

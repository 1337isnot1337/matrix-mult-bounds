"""Independent replay of balanced-puncture polynomial certificates."""
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
spec = importlib.util.spec_from_file_location('balanced_puncture', PACKAGE/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def replay_incidence(record):
    pair = v.decode(record['pair_coefficient_map'])
    annihilator = v.decode(record['pair_annihilator'])
    generators = v.decode(record['syzygy_generators'])
    system = v.decode(record['incidence_system'])
    direction = v.decode(record['kernel_direction'])
    residual = v.decode(record['residual'])
    assert pair.shape == (72, 12) and v.rank(pair) == 12
    assert annihilator.shape == (60, 72) and v.rank(annihilator) == 60
    assert annihilator*pair == sp.zeros(60, 12)
    assert system == annihilator*sp.diag(generators, generators)
    assert sp.expand(system.extract(record['unit_minor_rows'],
                                    record['unit_minor_columns']).det()) == 1
    assert (system*direction-residual).applyfunc(sp.expand) == sp.zeros(60, 1)
    a,b,c,d,e = v.A,v.B,v.C,v.D,v.E
    assert residual.subs({d:-c,e:-c**2}).applyfunc(sp.expand) == sp.zeros(60, 1)
    i,j = record['reverse_ideal_rows']
    assert sp.expand(residual[i]+c+d) == 0
    assert sp.expand(residual[j]+d**2+e+(a+2*c-d)*(c+d)) == 0
    # The chosen free coordinate is one at every point, even at a=b=c=0.
    assert direction[4] == 1


class BalancedPunctureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reports = {name:json.loads((RESULTS/(name+'.json')).read_text())
                       for name in ('affine_chart','controls')}

    def test_saved_reports_and_pinned_sources(self):
        self.assertEqual(v.reports(), self.reports)
        import hashlib
        sources = json.loads((PACKAGE/'sources.json').read_text())
        for source in sources['local_dependencies']:
            self.assertEqual(hashlib.sha256((ROOT/source['path']).read_bytes()).hexdigest(),
                             source['sha256'])

    def test_full_affine_incidence_certificate_and_corruptions(self):
        record = self.reports['affine_chart']
        replay_incidence(record)
        corrupt = copy.deepcopy(record)
        corrupt['unit_minor_rows'][0] = 0
        with self.assertRaises(AssertionError):
            replay_incidence(corrupt)
        corrupt = copy.deepcopy(record)
        matrix = v.decode(corrupt['incidence_system'])
        matrix[0,0] += 1
        corrupt['incidence_system'] = v.encode(matrix)
        with self.assertRaises(AssertionError):
            replay_incidence(corrupt)

    def test_symbolic_family_against_every_actual_core_coefficient(self):
        data = v.core_data()
        record = self.reports['affine_chart']
        normal = v.decode(record['normal_family'])
        actual = data['core']*normal
        x,y,a,b,c = v.X,v.Y,v.A,v.B,v.C
        _,_,matrices = v.syzygies((1+c*x)*(1-c*y),1+a*x,1+b*y,
                                  [-x*y,-x+y+c*x*y])
        m0,m2 = map(v.flat,matrices)
        zero = sp.zeros(36,1)
        expected = sp.Matrix.vstack(m0,zero,m2,zero).row_join(
            sp.Matrix.vstack(zero,m0,zero,m2))
        self.assertEqual((actual-expected).applyfunc(sp.expand),sp.zeros(144,2))
        pair = sp.Matrix.vstack(m0.T,m2.T)
        self.assertEqual(sp.expand(pair[:,[6,18]].det()),-1)
        self.assertEqual((v.multiplication()*m0).applyfunc(sp.expand),sp.zeros(16,1))
        self.assertEqual((v.multiplication()*m2).applyfunc(sp.expand),sp.zeros(16,1))

    def test_syzygy_control_from_independent_polynomial_convolution(self):
        record = self.reports['controls']['three_dimensional_syzygy_control']
        u,w = v.decode(record['u']),v.decode(record['v'])
        left = sp.Matrix.hstack(*u.T.nullspace()).T
        right = sp.Matrix.hstack(*w.T.nullspace()).T
        self.assertEqual(v.rank(left),5)
        self.assertEqual(v.rank(right),5)
        matrices = [v.decode(m) for m in record['matrices']]
        coefficients = sp.Matrix.hstack(*(v.flat(m) for m in matrices))
        self.assertEqual(v.rank(coefficients),3)
        for matrix in matrices:
            polynomial = sum(matrix[i,j]*p*q for i,p in enumerate(v.U_MONOMIALS)
                             for j,q in enumerate(v.V_MONOMIALS))
            self.assertEqual(sp.expand(polynomial),0)
            for i,j in itertools.product(range(2),repeat=2):
                unit = sp.zeros(2);unit[i,j] = 1
                projected = sp.kronecker_product(left,sp.eye(2))*sp.kronecker_product(
                    matrix,unit)*sp.kronecker_product(right.T,sp.eye(2))
                self.assertEqual(projected,sp.zeros(10))
        # Breaking one required product kernel must expose a coefficient.
        altered = left.copy();altered[0,:] = sp.eye(6)[0,:]
        self.assertTrue(any(altered*m*right.T != sp.zeros(5) for m in matrices))

    def test_coordinate_incidence_scope_is_exactly_36_fixed_line_pairs(self):
        records = self.reports['controls']['coordinate_charts']
        self.assertEqual(len(records),36)
        self.assertEqual({(r['u_index'],r['v_index']) for r in records},
                         set(itertools.product(range(6),repeat=2)))
        self.assertEqual({r['nonplane_dimension'] for r in records},{0,2})
        self.assertEqual(sum(r['nonplane_dimension']==2 for r in records),8)
        data = v.core_data()
        for record in records:
            i,j = record['u_index'],record['v_index']
            rows = [36*k+6*p+q for k in range(4) for p in range(6) for q in range(6)
                    if p!=i and q!=j]
            matrix = data['core'][rows,:]
            kernel = v.decode(record['kernel'])
            self.assertEqual(matrix*kernel,sp.zeros(100,kernel.cols))
            self.assertEqual(v.rank(kernel),kernel.cols)
            self.assertEqual(v.rank(matrix)+kernel.cols,24)


if __name__ == '__main__':
    unittest.main()

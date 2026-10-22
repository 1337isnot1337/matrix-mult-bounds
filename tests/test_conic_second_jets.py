"""Universal source replay and negative controls for conic two-jet compatibility."""
import copy
import gzip
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-21-conic-second-jets'
spec = importlib.util.spec_from_file_location('conic_second_jets',PACKAGE/'verify.py')
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)


def replay(matrix,operations,columns,laurent=False):
    rows = {i:{} for i in range(matrix.rows)}
    for (i,j),z in matrix.todok().items(): rows[i][j] = z
    active = set(rows)
    for i,j,scale in operations:
        assert i in active and j<columns
        scale = sp.sympify(scale,locals=v.m.SYMBOLS)
        assert rows[i][j]==scale
        if laurent:
            coeff,power = scale.as_coeff_exponent(v.d)
            assert coeff.is_Rational and coeff and power.is_Integer
        else: assert scale.is_Rational and scale
        pivot = {k:sp.expand(z/scale) for k,z in rows[i].items()}
        active.remove(i)
        for other in active:
            factor = rows[other].get(j,0)
            if factor:
                for k,z in pivot.items():
                    value = sp.expand(rows[other].get(k,0)-factor*z)
                    if value: rows[other][k] = value
                    else: rows[other].pop(k,None)
    assert not any(any(j<columns for j in rows[i]) for i in active)
    return rows,active


class ConicSecondJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.frozen = v.read('certificates')
        cls.actual = v.reports()

    def test_complete_reconstruction_and_dependency_pins(self):
        self.assertEqual(self.actual,self.frozen)
        for entry in json.loads((PACKAGE/'sources.json').read_text())['local_dependencies']:
            self.assertEqual(hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest(),entry['sha256'])
        e = v.m.E
        self.assertEqual(e.TERMS,[(e.index(i,s,6-p-q),e.index(p,j,6-r-s),e.index(r,q,6-i-j))
            for i,j,p,q,r,s in product(range(4),repeat=6)])
        self.assertEqual(len(e.TERMS),4096)
        self.assertEqual(sorted(sum((r['source_indices'] for r in self.actual['tangents']),[])),e.OUTSIDE)

    def test_full_tangent_dimensions_and_unconditional_basis_identifications(self):
        self.assertEqual([r['unknowns'] for r in self.actual['tangents']],[1176,784,784])
        self.assertEqual([r['constant_leading_eliminations'] for r in self.actual['tangents']],[720,560,560])
        self.assertEqual([r['unit_pivot_count'] for r in self.actual['tangents']],[392,221,221])
        self.assertEqual([v.m.decode(r['kernel']).cols for r in self.actual['tangents']],[64,3,3])
        self.assertEqual([r['basis_transform_determinant'] for r in self.actual['tangents']],['-4','-1','-1'])
        self.assertEqual(sum(v.m.decode(r['kernel']).cols for r in self.actual['tangents']),70)
        bad = copy.deepcopy(self.frozen['tangents'][0])
        bad['unit_operations'][0][2] = '0'
        with self.assertRaises(AssertionError):
            replay(v.m.decode(bad['reduced_matrix']),bad['unit_operations'],456)

    def test_laurent_unit_certificate_and_exact_mixed_residual_ideal(self):
        r = self.frozen['compatibility']
        self.assertEqual(r['unit_pivot_count'],49)
        rows,active = replay(v.m.decode(r['mixed_matrix']),r['unit_operations'],68,True)
        target = (v.a-v.c)*(v.b+v.c)*(v.c+v.d**3)
        rhs = [sp.cancel(rows[i].get(68,0)) for i in sorted(active) if rows[i].get(68,0)]
        self.assertEqual([str(z) for z in rhs],r['residuals'])
        for z,q in zip(rhs,r['quotients']):
            self.assertEqual(sp.cancel(z-target*sp.sympify(q,locals=v.m.SYMBOLS)),0)
        reverse = sp.sympify(r['quotients'][r['reverse_unit_index']],locals=v.m.SYMBOLS)
        self.assertEqual(reverse,-1/v.d)
        self.assertNotEqual(target.subs({v.a:1,v.b:2,v.c:3,v.d:1}),0)
        self.assertEqual(target.subs(v.c,-v.d**3).expand(),0)
        bad = copy.deepcopy(r['unit_operations']);bad[0][2] = '0'
        with self.assertRaises(AssertionError):
            replay(v.m.decode(r['mixed_matrix']),bad,68,True)

    def test_pure_normal_fibers_without_specializing_laurent_pivots(self):
        self.assertEqual([r['cohomology']['shape'] for r in self.actual['curvature']],[[324,137],[324,137]])
        for k in (1,2):
            r = self.actual['compatibility']['pure'][str(k)]
            self.assertTrue(r['own_base_velocity_block_zero'])
            target = (v.a-v.c)*(v.b+v.c)*(1 if k==1 else v.c)
            self.assertEqual(sp.expand(sp.sympify(r['residual_generator'],locals=v.m.SYMBOLS)-target),0)
            self.assertIn(r['quotients'][r['reverse_unit_index']],('1','-1'))

    def test_polynomial_two_jet_and_exact_linear_components(self):
        self.assertEqual(self.actual['witness_checks']['cubic_two_jet_residuals'],[0,0])
        self.assertEqual(self.actual['witness_checks']['uncorrected_third_residual_entries'],184)
        self.assertEqual(self.actual['witness_checks']['exact_linear_components'],['a=c','b=-c'])
        record = copy.deepcopy(v.read('witnesses'))
        y = record['cubic_component_two_jet']['source_row_correction_order2']
        row,col,value = y['entries'][0]
        y['entries'][0] = [row,col,'('+value+')+1']
        with self.assertRaises(AssertionError): v.witness_checks(record)

    def test_deterministic_compressed_artifacts(self):
        for name in ('witnesses','certificates'):
            raw = (v.RESULTS/(name+'.json.gz')).read_bytes()
            self.assertEqual(raw[4:8],b'\0\0\0\0')
            self.assertEqual(json.loads(gzip.decompress(raw)),v.read(name))


if __name__=='__main__': unittest.main()

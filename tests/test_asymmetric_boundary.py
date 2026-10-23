"""Replay global asymmetric-normal identities without trusting their discovery."""
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp
from sympy.polys.domains import GF
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-23-asymmetric-boundary'
spec = importlib.util.spec_from_file_location('asymmetric_boundary', PACKAGE/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def replay_support(original, record):
    current = original
    for stage in record['stages']:
        assert current.cols == stage['parameter_dimension']
        forms = []
        for minor in stage['minors']:
            positions = minor['positions']
            assert len(positions) == len({i for i, j in positions}) == 3
            assert len({j for i, j in positions}) == 3
            form = v.decode(minor['linear_form'])
            first = next(j for j in range(form.cols) if form[0, j])
            scales = []
            for k, (i, j) in enumerate(positions):
                entry = current[6*i+j, :]
                scale = entry[0, first]/form[0, first]
                assert scale and entry == scale*form
                assert all(not current[6*i+col, :].todok() for _, col in positions[k+1:])
                scales.append(scale)
            assert sp.prod(scales) == sp.Rational(minor['determinant_ratio'])
            forms.append(form)
        constraints = sp.Matrix.vstack(*forms)
        kernel = v.decode(stage['kernel'])
        assert v.rank(constraints) == stage['forced_rank']
        assert v.rank(kernel) == kernel.cols == current.cols-stage['forced_rank']
        assert not (constraints*kernel).todok()
        current = current*kernel
    assert current == v.decode(record['remaining_coefficient_map'])
    basis, parameter_map = (v.decode(record[key]) for key in ('basis', 'parameter_map'))
    assert basis*parameter_map == current and v.rank(parameter_map) == 12
    variables = sp.symbols('x:12')
    table = sp.Matrix(24, 6, lambda i, j: sum(
        basis[6*i+j, k]*variables[k] for k in range(12)))
    monomials = [tuple(m) for m in record['cubic_monomials']]
    assert len(monomials) == len(set(monomials)) == 364
    assert all(sum(m) == 3 and all(e >= 0 for e in m) for m in monomials)
    rows = []
    for minor in record['selected_minors']:
        submatrix = table[minor['rows'], minor['columns']]
        # Independent symbolic determinant rather than the polynomial-ring producer.
        polynomial = sp.Poly(submatrix.det(method='domain-ge'), *variables)
        _, primitive = polynomial.primitive()
        if primitive.LC() < 0:
            primitive = -primitive
        coefficients = primitive.as_dict()
        rows.append([coefficients.get(m, 0) for m in monomials])
    coefficients = sp.Matrix(rows)
    assert coefficients == v.decode(record['coefficient_matrix'])
    field = GF(record['prime'])
    actual = DomainMatrix.from_Matrix(coefficients).convert_to(field).det()
    assert int(actual) % record['prime'] == record['determinant_mod_prime'] != 0
    sharp = record['sharp_original_parameter']
    assert v.rank(sp.Matrix(24, 6, lambda i, j: original[6*i+j, sharp])) == 3


class AsymmetricBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = ROOT/'results/asymmetric-boundary-2026-10-23/certificates.json.gz'
        cls.payload = path.read_bytes()
        cls.frozen = json.loads(gzip.decompress(cls.payload))
        cls.actual = v.reports()

    def test_complete_rebuild_and_dependency_pins(self):
        self.assertEqual(self.actual, self.frozen)
        for entry in json.loads((PACKAGE/'sources.json').read_text())['local_dependencies']:
            self.assertEqual(hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest(), entry['sha256'])
        # Python 3.11/3.12 can use zlib's OS byte, while 3.13+ writes 255.
        # The saved artifact is pinned separately; compare the portable payload.
        raw = gzip.decompress(self.payload)
        self.assertEqual(self.payload[4:8], b'\0\0\0\0')
        self.assertEqual(raw, (json.dumps(self.frozen, sort_keys=True,
            separators=(',', ':'))+'\n').encode())
        manifest = json.loads((PACKAGE/'manifest.json').read_text())
        key = 'results/asymmetric-boundary-2026-10-23/certificates.json.gz'
        self.assertEqual(hashlib.sha256(self.payload).hexdigest(), manifest['sha256'][key])

    def test_auxiliary_split_every_coefficient_and_exact_product_kernel(self):
        record = self.frozen['split_obstruction']
        coefficient = v.decode(record['other_side_coefficient_map'])
        half = v.decode(record['half_coefficient_map'])
        embedding = v.decode(record['embedding'])
        self.assertEqual(v.rank(embedding), 84)
        self.assertEqual(v.rank(half), 72)
        for k in range(100):
            m = sp.Matrix(42, 6, lambda i, j: half[42*j+i, k])
            actual = sp.Matrix(200, 12, lambda i, j: coefficient[200*j+i, k])
            self.assertEqual(embedding*sp.kronecker_product(m, sp.eye(2)), actual)
        k = record['sharp_normal_parameter']
        actual = sp.Matrix(200, 12, lambda i, j: coefficient[200*j+i, k])
        span = v.decode(record['sharp_product_first_span'])
        self.assertEqual(v.rank(actual), 4)
        self.assertEqual(v.rank(span), 8)
        self.assertFalse((actual*span).todok())
        corrupt = span.copy()
        row, column = next((i, j) for i in range(12) for j in range(8)
                           if actual[:, i].todok())
        corrupt[row, column] += 1
        self.assertTrue((actual*corrupt).todok())

    def test_global_joint_row_and_column_support_certificates(self):
        core = v.predecessor().decode(v.predecessor().biform_structure()['core'])
        transposed = core[[36*k+6*j+i for k in range(4)
                           for i in range(6) for j in range(6)], :]
        for original, key in ((core, 'joint_row_support'),
                              (transposed, 'joint_column_support')):
            replay_support(original, self.frozen[key])
        corrupt = copy.deepcopy(self.frozen['joint_row_support'])
        corrupt['stages'][0]['minors'][0]['determinant_ratio'] = '0'
        with self.assertRaises(AssertionError):
            replay_support(core, corrupt)

    def test_one_sided_gap_and_dimension_five_countercontrol(self):
        record = self.frozen['projection_controls']
        self.assertEqual(record['sharp_positive_first_rank'], 4)
        self.assertEqual(record['five_dimensional_loss_first_rank'], 2)
        x, y = sp.symbols('x y')
        pencil = x*v.decode(record['base_matrices'][0])+y*v.decode(record['base_matrices'][1])
        self.assertEqual(pencil.extract([0, 1], [0, 1]).det(), x*x)
        self.assertEqual(pencil.extract([0, 2], [0, 2]).det(), y*y)


if __name__ == '__main__':
    unittest.main()

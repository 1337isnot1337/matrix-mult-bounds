"""Exact controls for the written polynomial flag argument and residual trap."""
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT/'research/ai/2026-10-20-singular-flags'
RESULTS = ROOT/'results/singular-flags-2026-10-20'


def load(name):
    spec = importlib.util.spec_from_file_location(name, PACKAGE/(name+'.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


flags = load('exact_flags')
obstruction = load('flag_obstruction')
gauge = load('gauge_control')


class SingularFlagTests(unittest.TestCase):
    def test_full_source_gl2_action(self):
        for m, B in [(2, 3), (3, 6), (4, 10)]:
            original = (sp.eye(m), sp.eye(B), sp.eye(B+m-1))
            expected = flags.tensor(*original)
            for action in [flags.shear, flags.translate]:
                actual = flags.source_change(*original, action, sp.Rational(2, 3))
                self.assertEqual(flags.tensor(*actual), expected)

    def test_known_controls_survive_full_normalization(self):
        for name, count in [('collision-m2-control', 18), ('collision-m3-control', 108),
                            ('collision-m4-B11', 400)]:
            witness = json.loads((ROOT/'results/mixed-restrictions-2026-10-20'/
                                  (name+'.json')).read_text())['witness']
            G, P, Q, weights = flags.coordinate_control(witness)
            m = witness['m']
            self.assertEqual(flags.check_limit(m, G, P, Q, weights)['coefficients_checked'], count)
            A, Y, Z, point = flags.normalize(m, G, P, Q, weights)
            self.assertGreater(point, 0)
            self.assertEqual(flags.check_limit(m, A, Y, Z, weights)['coefficients_checked'], count)
            for matrix, w, highest in [(A, weights[0], True), (Y, weights[1], True),
                                       (Z, weights[2], False)]:
                for rank, row in enumerate(sorted(range(matrix.rows), key=w.__getitem__)):
                    pivot = matrix.cols-1-rank if highest else rank
                    self.assertNotEqual(matrix[row, pivot], 0)
                    killed = range(pivot+1, matrix.cols) if highest else range(pivot)
                    self.assertTrue(all(matrix[row, column] == 0 for column in killed))

    def test_normal_form_makes_forced_coefficients_nonzero(self):
        witness = json.loads((ROOT/'results/mixed-restrictions-2026-10-20/'
                              'collision-m4-B11.json').read_text())['witness']
        G, P, Q, weights = flags.coordinate_control(witness)
        A, Y, Z, _ = flags.normalize(4, G, P, Q, weights)
        values = flags.tensor(A, Y, Z)
        ry = {row:rank for rank,row in enumerate(sorted(range(Y.rows), key=weights[1].__getitem__))}
        rz = {row:rank for rank,row in enumerate(sorted(range(Z.rows), key=weights[2].__getitem__))}
        checked = 0
        for p in range(4):
            for y in range(10):
                for z in range(10):
                    if 3-p+10-ry[y] == rz[z]:
                        self.assertEqual(values[(p*10+y)*10+z],
                                         A[p, 3-p]*Y[y, 10-ry[y]]*Z[z, rz[z]])
                        self.assertNotEqual(values[(p*10+y)*10+z], 0)
                        checked += 1
        self.assertGreater(checked, 0)

    def test_earlier_chamber_is_excluded(self):
        report = obstruction.inspect(4, 10, [7, 14, 21, 0])
        self.assertEqual(report, json.loads((RESULTS/'excluded-chamber.json').read_text()))
        self.assertEqual(len(report['forbidden_entries']), 6)
        first = report['forbidden_entries'][0]
        self.assertEqual(first['source_input_degrees'], [2, 6])
        self.assertEqual(first['source_output_pivot'], 8)
        self.assertEqual(first['weight'], '-6')

    def test_separated_cone_all_stated_additive_costs(self):
        for m in range(2, 9):
            n = m*(m+1)//2
            eta = [10*m*u for u in range(1, m)]+[0]
            for s in range(m-1):
                report = obstruction.inspect(m, n+s, eta)
                self.assertTrue(report['excluded_in_stated_constant_matrix_class'])
                self.assertTrue(any(c['p']==s+1 and c['y']==[0, m-1] and c['z']==[0, m-1]
                                    for c in report['forbidden_entries']))

    def test_balanced_perturbation_is_not_excluded_by_leading_pivots(self):
        report = obstruction.inspect(4, 10, [0, 201, 403, 607], 100)
        self.assertFalse(report['excluded_in_stated_constant_matrix_class'])
        with self.assertRaisesRegex(ValueError, 'strict'):
            obstruction.inspect(4, 10, [0, 2, 4, 6])

    def test_exact_residual_negative_control(self):
        self.assertEqual(gauge.run(), json.loads((RESULTS/'gauge-control.json').read_text()))
        for t in [1, 2, 4, 16, 32]:
            report = gauge.evaluate(t)
            expected = sp.Rational(1, t**6)
            self.assertEqual(sp.Rational(report['masked_squared_error']), expected)
            self.assertEqual(sp.Rational(report['full_squared_error']), expected+2*t**2+t**8)

    def test_target_diagonal_stabilizer_dimension(self):
        for m in range(2, 7):
            ps = flags.points(m)
            n = len(ps)
            rows = []
            for p in range(m):
                for y, (a, b) in enumerate(ps):
                    for z, (c, d) in enumerate(ps):
                        if p==a+c and a+b+c+d==m-1:
                            row = [0]*(m+2*n)
                            for index in [p, m+y, m+n+z]: row[index] = 1
                            rows.append(row)
            self.assertEqual(m+2*n-sp.Matrix(rows).rank(), m+2)

    def test_frozen_fixed_basis_query_hashes(self):
        for name in ['fixed-identity2', 'fixed-hadamard4', 'fixed-newton2', 'fixed-newton4']:
            report = json.loads((RESULTS/(name+'.json')).read_text())
            query = gzip.decompress((RESULTS/(name+'.smt2.gz')).read_bytes())
            self.assertEqual(hashlib.sha256(query).hexdigest(), report['query_sha256'])

    def test_fixed_basis_sat_controls_without_solver(self):
        for name in ['fixed-identity2', 'fixed-newton2']:
            report = json.loads((RESULTS/(name+'.json')).read_text())
            self.assertEqual(flags.fixed_basis_control(report['witness'])['coefficients_checked'], 18)


if __name__ == '__main__':
    unittest.main()

"""Complete dual replay and controls for the fixed full conic third jet."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-conic-fixed-third-obstruction'
RESULTS = ROOT / 'results/conic-fixed-third-obstruction-2026-10-23'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load('conic_fixed_third_acceptance', PACKAGE / 'verify.py')


class ConicFixedThirdObstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.witness = json.loads((RESULTS / 'dual-and-linear-branches.json').read_text())
        started = time.monotonic()
        cls.report = v.verify(cls.witness)
        cls.acceptance_seconds = time.monotonic()-started
        original = json.loads((ROOT / v.PRESCRIBED).read_text())
        cls.bs, cls.cs = [[v.decode(row, (14, 112)) for row in original[side]]
                         for side in ('B', 'C')]
        cls.ys = [v.decode(row, (100, 12)) for row in original['source_row_corrections']]
        cls.terms = v.source_terms()
        cls.w0 = v.select_rows(v.contract(cls.bs[0], cls.cs[0], cls.terms), v.FIRST)
        cls.weights = {(a, b, c): v.expression(z, 0)
                       for a, b, c, z in cls.witness['functional']}

    def test_complete_dual_and_both_all_order_components(self):
        self.assertEqual(self.report, json.loads((RESULTS / 'verification.json').read_text()))
        self.assertEqual(self.report['arbitrary_fourth_map_coefficients_annihilated'], 3136)
        self.assertEqual(self.report['arbitrary_fourth_kernel_coefficients_annihilated'], 1200)
        self.assertEqual(self.report['prescribed_map_orders_fixed'], [0, 1, 2, 3])
        self.assertEqual(self.report['prescribed_kernel_entry_counts'], [0, 0, 16])
        self.assertEqual(self.report['exceptional_exact_linear_components'], ['a=-d^3', 'b=d^3'])
        self.assertEqual(self.report['leading_minor_determinants'], ['1', '1', '-1'])
        self.assertEqual(self.report['rational_literal_source_control']['nonzero_fourth_coefficients'], '-16/3')

    def test_explicit_formula_regenerates_dual_and_complete_linear_maps(self):
        construction = load('conic_fixed_third_construction', PACKAGE / 'construct.py')
        self.assertEqual(construction.construct(), self.witness)

    def test_changed_dual_coefficient_fails_full_adjoint_identity(self):
        weights = dict(self.weights)
        position = next(iter(weights))
        weights[position] = v.add(weights[position], v.ONE)
        with self.assertRaisesRegex(ValueError, 'every fourth map coefficient'):
            v.check_adjoint(weights, self.bs[0], self.cs[0], self.w0, self.terms)

    def test_changed_prescribed_exceptional_curve_is_rejected(self):
        branch = copy.deepcopy(self.witness['linear_branches'][0])
        entry = branch['B'][1]['entries'][0]
        entry[2] = f'({entry[2]})+1'
        with self.assertRaisesRegex(ValueError, 'prescribed linear branch coefficient'):
            v.check_linear_branch(branch, self.bs, self.cs, self.ys, self.terms)

    def test_proof_third_coefficient_shape_and_kernel_pairing(self):
        for side, matrix in (('B', self.bs[3]), ('C', self.cs[3])):
            for (row, column), value in matrix.items():
                middle = column//28 if side == 'B' else column//7 % 4
                self.assertIn(middle, (1, 2))
                if middle == 1:
                    shift = 28 if side == 'B' else 7
                    self.assertEqual(value, v.multiply(v.D, matrix[row, column+shift]))
        q = v.expression('a*(a+d**3)**2*(b-d**3)**3/(3*d**2)')
        expected = {}
        for i in (1, 2):
            for j in (1, 2):
                for z, k, value in ((1, 0, v.scale(q, 2)),
                                    (2, 0, v.scale(v.multiply(v.D, q), 2)),
                                    (4, 3, q), (5, 3, v.multiply(v.D, q))):
                    expected[v.OUTSIDE.index(28*i+7*j+z), v.FIRST.index(28*i+7*j+k)] = value
        self.assertEqual(self.ys[2], expected)

    def test_scope_residual_pin_and_laurent_controls(self):
        for key, value, message in (
                ('chart', 'all d', 'd chart'),
                ('fourth_residual', '0', 'obstruction polynomial'),
                ('prescribed_sha256', '0'*64, 'source pin'),
                ('extension_criterion', 'all a,b,d', 'extension criterion')):
            bad = copy.deepcopy(self.witness)
            bad[key] = value
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, message):
                v.verify(bad)
        self.assertEqual(v.expression('(a+b*d)/(3*d**2)'),
                         v.scale(v.multiply(v.add(v.A, v.multiply(v.B, v.D)), v.power(v.D, -2)), v.Fraction(1, 3)))
        for text in ('1/a', '1/(d+1)', 'd**-3', 'd**(1/2)',
                     "__import__('os')", '1.0', '1/0'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                v.expression(text)

    def test_literal_source_pins_and_standard_library_import(self):
        predecessor = load('conic_fixed_third_original_literal_source', ROOT /
                           'research/ai/2026-10-23-conic-third-jets/verify.py')
        self.assertEqual(set(self.terms), set(predecessor.source_terms()))
        self.assertEqual(len(self.terms), 4096)
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for source in sources['local']:
            for path, digest in source['sha256'].items():
                self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), digest)
        with tempfile.TemporaryDirectory() as outside:
            program = 'import runpy,sys; runpy.run_path(sys.argv[1],run_name="isolated_acceptance"); print("stdlib-import-ok")'
            completed = subprocess.run([sys.executable, '-I', '-S', '-c', program,
                                        str(PACKAGE / 'verify.py')], cwd=outside,
                                       capture_output=True, text=True, check=True)
        self.assertEqual(completed.stdout.strip(), 'stdlib-import-ok')


if __name__ == '__main__':
    unittest.main()

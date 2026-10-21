"""Uniform elimination, coalescing column modes, and source scaling."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('pure_mixed_five_verifier', ROOT / 'research/ai/2026-10-21-pure-mixed-five-spaces/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class PureMixedFiveTests(unittest.TestCase):
    def test_complete_polynomial_certificate(self):
        saved = ROOT / 'results/pure-mixed-five-spaces-2026-10-21/report.json'
        self.assertEqual(verify.report(), json.loads(saved.read_text()))
        self.assertEqual(verify.report()['case_dimensions'], [6, 14])
        self.assertEqual(verify.report()['final_nonplane_dimension'], 0)

    def test_coalescing_modes_remain_covered(self):
        data = verify.split_data()
        q = data['q_coefficients'].subs({verify.A: -1})
        w = data['w_kernel'].subs({verify.A: -1})
        self.assertEqual(q*w, verify.sp.zeros(q.rows, w.cols))
        self.assertEqual(verify.third.matrix_rank(data['stable_coefficients'].subs({verify.A: -1})), 26)
        self.assertEqual(verify.third.matrix_rank(q), 18)
        generic = data['q_coefficients'].subs({verify.A: 1})*data['w_kernel'].subs({verify.A: 1})
        self.assertEqual(verify.third.matrix_rank(generic), 6)

    def test_changed_square_minor_scale_is_rejected(self):
        matrix, rows, record = verify.split_data()['minor_checks'][0]
        changed = copy.deepcopy(record)
        changed['scales'][0] = str(2*verify.sp.Rational(changed['scales'][0]))
        with self.assertRaisesRegex(ArithmeticError, 'Incorrect repeated diagonal'):
            verify.check_minor(matrix, rows, changed)

    def test_source_torus_preserves_flags_and_normalizes_partners(self):
        source = verify.third.load('pure_five_torus_source', ROOT / 'research/ai/2026-10-21-mixed-first-jets/verify.py')
        weight = lambda i: i//28+(i//7) % 4+i % 7
        self.assertEqual({sum(weight(i) for i in term) for term in source.TERMS}, {18})
        self.assertEqual(len(source.TERMS), 4096)
        for z in (1, 2, 4, 5):
            self.assertEqual(weight(source.index(0, 3, z)), weight(source.index(3, 0, z)))
        lam = verify.sp.Symbol('lambda', nonzero=True)
        left, right = verify.frames.chart_frames()
        for coordinates in (left, right):
            mixed = coordinates[12:, 6]
            scaled = verify.sp.diag(*(lam**i for i in (5, 6, 6, 7)))*mixed/lam**7
            expected = mixed.subs({verify.A: verify.A/lam, verify.B: verify.B/lam}, simultaneous=True)
            self.assertTrue(verify.frames.zero(scaled-expected))


if __name__ == '__main__':
    unittest.main()

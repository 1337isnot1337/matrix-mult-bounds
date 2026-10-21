"""Complete complex rank cover, exceptional fibers and damaged witnesses."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('two_coordinate_verifier', ROOT / 'research/ai/2026-10-21-mixed-two-coordinate-chart/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class TwoCoordinateTests(unittest.TestCase):
    def test_complete_replay(self):
        saved = ROOT / 'results/mixed-two-coordinate-chart-2026-10-21/report.json'
        self.assertEqual(verify.report(), json.loads(saved.read_text()))
        self.assertEqual(verify.report()['exceptional_case_dimensions'], [[16, 8, 6, 4, 2, 0], [6, 4, 0]])
        self.assertFalse(verify.report()['general_chart_target_excluded'])

    def test_omitting_nonreal_roots_is_rejected(self):
        curve = copy.deepcopy(verify.certificate()['rank_cover'][1])
        curve['exception_controls'] = [c for c in curve['exception_controls'] if c['value'] == '0']
        with self.assertRaisesRegex(ArithmeticError, 'root controls are incomplete'):
            verify.check_root_cover(verify.expression(curve['determinant']), verify.T, curve['exception_controls'])

    def test_changed_polynomial_normal_is_rejected(self):
        matrix = verify.source_data()['mixed']
        kernel = verify.decode(verify.certificate()['polynomial_kernel']).copy()
        column = next(j for i, j in matrix.todok())
        kernel[column, 0] += 1
        with self.assertRaisesRegex(ArithmeticError, 'normal-kernel identity failed'):
            verify.check_kernel(matrix, kernel)

    def test_generic_frame_misses_the_exceptional_fibers(self):
        kernel = verify.rank_data()['kernel']
        for point, expected in [((0, 0), 28), ((1, 1), 30)]:
            value = kernel.subs({verify.T: point[0], verify.H: point[1]})
            self.assertEqual(len(value.to_DM().rref()[1]), expected)


if __name__ == '__main__':
    unittest.main()

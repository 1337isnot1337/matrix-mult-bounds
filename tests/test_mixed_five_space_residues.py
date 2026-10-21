"""Replay the complete point certificate and reject corrupted local witnesses."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('mixed_five_space_verifier', ROOT / 'research/ai/2026-10-21-mixed-five-space-residues/verify.py')
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class MixedFiveSpaceTests(unittest.TestCase):
    def test_complete_certificate_replay(self):
        saved = ROOT / 'results/mixed-five-space-residues-2026-10-21/report.json'
        self.assertEqual(verify.report(), json.loads(saved.read_text()))
        self.assertEqual(verify.report()['normal_dimensions'], [88, 68, 54, 30, 18, 12, 4])

    def test_final_normals_are_the_complete_plane_kernel(self):
        final = verify.reduction()['final']
        self.assertEqual(verify.third.matrix_rank(final), 4)
        self.assertEqual(verify.third.matrix_rank(verify.sp.Matrix.hstack(final, verify.frames.plane_parameters())), 4)

    def test_missing_cover_is_rejected(self):
        _, block, parameters, _ = next(c for c in verify.reduction()['checks'] if c[0] == 'cover')
        with self.assertRaisesRegex(ArithmeticError, 'Uncovered nonzero'):
            verify.check_cover(block, parameters, [])

    def test_changed_minor_scale_is_rejected(self):
        _, matrix, rows, witness = next(c for c in verify.reduction()['checks'] if c[0] == 'minor')
        changed = copy.deepcopy(witness)
        changed['scales'][0] = str(2*verify.sp.Rational(changed['scales'][0]))
        with self.assertRaisesRegex(ArithmeticError, 'Incorrect repeated diagonal'):
            verify.check_minor(matrix, rows, changed)


if __name__ == '__main__':
    unittest.main()

"""Independent source replay and failure controls for the five-frame package."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results/invertible-five-frame-2026-10-21'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load('five_frame_verifier', ROOT / 'research/ai/2026-10-21-invertible-five-frame/verify.py')
original = load('five_frame_original_source', ROOT / 'tests/test_mixed_first_jets.py')


class InvertibleFiveFrameTests(unittest.TestCase):
    def test_exact_annihilators_and_saved_cubic_report(self):
        self.assertEqual(verify.report(), json.loads((RESULTS / 'report.json').read_text()))

    def test_cubic_curve_in_original_cyclic_source_coordinates(self):
        certificate = json.loads((RESULTS / 'cubic-control.json').read_text())
        self.assertEqual(verify.cubic_control(certificate, original.original_contract),
                         verify.report()['cubic_control'])

    def test_missing_fifth_row_recovers_twenty_dimensional_extension(self):
        for side in ('B', 'C'):
            self.assertEqual(verify.both.third.matrix_rank(verify.annihilator(side, verify.extension.G)), 92)

    def test_nonzero_source_correction_tamper_is_rejected(self):
        certificate = copy.deepcopy(json.loads((RESULTS / 'cubic-control.json').read_text()))
        correction = next(rows for rows in reversed(certificate['source_corrections']) if rows)
        correction[0][2] += 1
        with self.assertRaisesRegex(ArithmeticError, 'nonzero corrected coefficient'):
            verify.cubic_control(certificate)


if __name__ == '__main__':
    unittest.main()

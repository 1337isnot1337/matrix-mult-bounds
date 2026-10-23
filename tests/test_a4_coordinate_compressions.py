"""Complete finite census and exact coordinate-compression sharpness."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-23-a4-coordinate-compressions'
PARENT = ROOT / 'research/ai/2026-10-23-conjugation-limit'
RESULTS = ROOT / 'results/a4-coordinate-compressions-2026-10-23'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load('a4_independent_coordinate_tests', PACKAGE / 'verify.py')


class IndependentCoordinateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / 'certificate.json').read_text())
        cls.matrices = verify.outer_space()

    def test_complete_census_and_exact_sharpness(self):
        self.assertEqual(verify.verify(self.certificate),
                         json.loads((RESULTS / 'verification.json').read_text()))

    def test_rebuilt_outer_space_matches_the_certified_block_basis(self):
        block = load('a4_coordinate_block_control', PARENT / 'block_reduction.py')
        matrices, labels, _ = block.build_blocks(verify.source_verifier())
        expected = [{28 * (position // 112 - 84) + position % 112: value
                     for position, value in matrix.items()}
                    for matrix, label in zip(matrices, labels)
                    if label[0].startswith('lowest_')]
        self.assertEqual(self.matrices, expected)

    def test_false_exact_kernel_and_repeated_pair_are_rejected(self):
        witnesses = copy.deepcopy(self.certificate['sharpness_witnesses'])
        witnesses[0]['kernel_coefficients'][0].append([0, 1])
        with self.assertRaisesRegex(ValueError, 'exact kernel identity'):
            verify.verify_sharpness(witnesses, self.matrices)
        witnesses = [self.certificate['sharpness_witnesses'][0]] * 2
        with self.assertRaisesRegex(ValueError, 'repeated sharpness pair'):
            verify.verify_sharpness(witnesses, self.matrices)

    def test_wrong_scope_and_missing_kernel_direction_are_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad['cases'] -= 1
        with self.assertRaisesRegex(ValueError, 'finite-census scope'):
            verify.verify(bad)
        witnesses = copy.deepcopy(self.certificate['sharpness_witnesses'])
        witnesses[0]['kernel_coefficients'].pop()
        with self.assertRaisesRegex(ValueError, 'six independent'):
            verify.verify_sharpness(witnesses, self.matrices)


if __name__ == '__main__':
    unittest.main()

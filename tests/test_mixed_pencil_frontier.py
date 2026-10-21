"""Generic-pencil witnesses, source-coordinate replay, and minor tampering."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'research/ai/2026-10-21-mixed-first-jets'
RESULTS = ROOT / 'results/mixed-first-jets-2026-10-21'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pencil = load('mixed_pencil_certificate', PACKAGE / 'pencil_frontier.py')
original = load('mixed_pencil_original_source', ROOT / 'tests/test_mixed_first_jets.py')


class MixedPencilFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / 'generic-pencil-twojet.json').read_text())
        cls.maps = pencil.third.third_coefficients(cls.certificate)

    def test_rebuild_generic_family(self):
        seed = json.loads((PACKAGE / 'generic-pencil-seed.json').read_text())
        self.assertEqual(original.construct.construct(seed), self.certificate)

    def test_complete_normal_minor_and_symmetry_replay(self):
        self.assertEqual(pencil.report(), json.loads((RESULTS / 'generic-pencil-report.json').read_text()))

    def test_independent_generic_third_source_contraction(self):
        parameters = (1, -1, 2, 1, 0, -2, 1, 1, -1, 2, 1, 0, 1, -1, 1, 2)
        ps, qs, y, z = original.evaluate(self.certificate, parameters)
        residues = original.corrected_coefficients(ps, qs, y, z)
        self.assertEqual(residues[:3], [{}, {}, {}])
        for a, matrix in self.maps.items():
            expected = sp.Matrix([residues[3].get((a, b+4, c+4), 0)
                                  for b in range(14) for c in range(6)])
            self.assertEqual(matrix*sp.Matrix(parameters), expected)

    def test_changed_cubic_minor_zero_is_rejected(self):
        matrix = pencil.flatten(self.maps)
        certificate = copy.deepcopy(json.loads((RESULTS / 'generic-pencil-minors.json').read_text()))
        positions = certificate['rounds'][0]['minors'][0]['positions']
        matrix[84*positions[0][0]+positions[1][1], 0] = 1
        with self.assertRaisesRegex(ArithmeticError, 'triangular zero is nonzero'):
            pencil.verify_cubic_minors(matrix, certificate)


if __name__ == '__main__':
    unittest.main()

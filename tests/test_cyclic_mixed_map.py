"""Full coefficient checks for the mixed cyclic restriction."""
import copy
from fractions import Fraction
import importlib.util
from itertools import product
import json
from pathlib import Path
import unittest

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-20-cyclic-mixed-map"
spec = importlib.util.spec_from_file_location("cyclic_mixed_verify", PACKAGE / "verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class CyclicMixedMapTests(unittest.TestCase):
    def test_all_576_coefficients(self):
        result = verify.report(verify.load_maps())
        self.assertTrue(result["full_exact_equality"])
        self.assertEqual(result["incorrect_coefficients"], 0)
        self.assertEqual(result["actual_nonzero_coefficients"], 24)
        self.assertEqual(result, json.loads((verify.RESULTS / "certificate.json").read_text()))

    def test_maps_have_full_row_rank(self):
        for rows, entries in zip((6, 12, 8), verify.load_maps()):
            matrix = sp.zeros(rows, 12)
            for i, j, value in entries:
                matrix[i, j] = sp.Rational(value)
            self.assertEqual(matrix.rank(), rows)

    def test_earlier_rational_witness(self):
        maps = verify.load_maps(verify.RESULTS / "discovery/earlier-m233-rational-witness.json")
        self.assertEqual(verify.contract(2, maps), verify.target_terms(2, 3, 3))

    def test_corrupted_coefficient_is_rejected(self):
        maps = copy.deepcopy(verify.load_maps())
        maps[0][0][2] = str(Fraction(maps[0][0][2])+1)
        self.assertFalse(verify.report(maps)["full_exact_equality"])

    def test_natural_coordinate_controls(self):
        for a in (2, 3):
            maps = [[], [], []]
            for i, j in product(range(a), repeat=2):
                maps[0].append((i*a+j, i*a+j, "1"))
                maps[1].append((i*a+j, j*a*(2*a-1)+i, "1"))
                maps[2].append((i*a+j, (i*a+j)*a, "1"))
            self.assertEqual(verify.contract(a, maps), verify.target_terms(a, a, a))


if __name__ == "__main__":
    unittest.main()

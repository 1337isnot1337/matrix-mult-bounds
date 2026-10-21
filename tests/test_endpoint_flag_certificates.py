"""Acceptance and corruption checks for exact endpoint flag certificates."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]

def load(name, package, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "research/ai" / package / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

CHART = load("free_flag_chart", "2026-10-21-free-isotropic-flags", "verify_chart.py")
SOURCE = load("free_flag_source", "2026-10-21-free-isotropic-flags", "verify_source.py")
BOUNDARY = load("boundary_pair_maps", "2026-10-21-boundary-pair", "verify_integer_maps.py")
BARRIER = load("shifted_scalar_barrier", "2026-10-21-global-moment-flag", "verify_scalar_shifted_barrier.py")

class EndpointFlagCertificateTests(unittest.TestCase):
    def test_integral_chart_minor_lift_and_normalizing_bases(self):
        expected = json.loads((ROOT / "results/free-isotropic-flags-2026-10-21/chart_certificate_report.json").read_text())
        self.assertEqual(CHART.verify(), expected)

    def test_repeated_jacobian_column_is_rejected(self):
        columns = CHART.PIVOTS[:]
        columns[-1] = columns[0]
        with patch.object(CHART, "PIVOTS", columns):
            with self.assertRaises(AssertionError):
                CHART.verify()

    def test_literal_binary_source(self):
        witness = json.loads(SOURCE.DEFAULT.read_text())
        expected = json.loads((ROOT / "results/free-isotropic-flags-2026-10-21/source_verification.json").read_text())
        self.assertEqual(SOURCE.verify(witness), expected)

    def test_binary_negative_and_constant_corruptions(self):
        original = json.loads(SOURCE.DEFAULT.read_text())
        for q in (0, 4):
            with self.subTest(output_degree=q):
                witness = copy.deepcopy(original)
                witness["Z"][q][0] ^= 1
                with self.assertRaises(AssertionError):
                    SOURCE.verify(witness)

    def test_canonical_boundary_pair_original_source(self):
        expected = json.loads((ROOT / "results/ai/2026-10-21-boundary-pair/integer-maps-verification.json").read_text())
        self.assertEqual(BOUNDARY.report(), expected)

    def test_boundary_negative_and_constant_corruptions(self):
        original = BOUNDARY.construct(5)
        column = next(j for j, value in enumerate(original["shared"][0]) if value)
        for row in (-1, 0):
            with self.subTest(output_row=row):
                witness = copy.deepcopy(original)
                witness["Z"][row][column] += 1
                with self.assertRaises(AssertionError):
                    BOUNDARY.verify(witness)

    def test_scalar_barrier_exact_rank_and_sum_controls(self):
        expected = json.loads((ROOT / "results/global-moment-flag-2026-10-21/scalar_shifted_barrier_report.json").read_text())
        self.assertEqual(BARRIER.verify(), expected)

if __name__ == "__main__":
    unittest.main()

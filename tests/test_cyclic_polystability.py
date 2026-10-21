"""Exact smoothness identities for the central cyclic multiplicity block."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-20-cyclic-recoupling"
sys.path.insert(0, str(PACKAGE))
spec = importlib.util.spec_from_file_location("central_cyclic_polystability", PACKAGE / "central_polystability.py")
central = importlib.util.module_from_spec(spec)
spec.loader.exec_module(central)


class CyclicPolystabilityTests(unittest.TestCase):
    def test_exact_projective_smoothness_certificates(self):
        grouped = central.read_json(central.RESULTS / "grouped-a4.json.gz")
        certificate = json.loads((central.RESULTS / "central-cubic-smoothness.json").read_text())
        actual = central.verify(grouped, certificate)
        expected = json.loads((central.RESULTS / "central-polystability.json").read_text())
        self.assertEqual(actual, expected)
        self.assertEqual(actual["multiplier_nonzero_terms_by_chart"], [19, 18, 23, 20])

    def test_corrupted_polynomial_identity_is_rejected(self):
        grouped = central.read_json(central.RESULTS / "grouped-a4.json.gz")
        certificate = json.loads((central.RESULTS / "central-cubic-smoothness.json").read_text())
        changed = copy.deepcopy(certificate)
        changed["certificates"][0]["multipliers"][0][0][1] = "0"
        with self.assertRaises(AssertionError):
            central.verify(grouped, changed)


if __name__ == "__main__":
    unittest.main()

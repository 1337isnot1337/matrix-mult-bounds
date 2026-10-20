"""Verify the survivor's exact data without promoting it to a degeneration."""
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/ai/2026-10-20-koszul/mixed_family.py"
REPORT = ROOT / "results/koszul-2026-10-20/mixed_family.json"


class MixedFamilyTests(unittest.TestCase):
    def test_report_replay(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "report.json"
            subprocess.run([sys.executable, str(SCRIPT), "--output", str(output)],
                           check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(output.read_text()), json.loads(REPORT.read_text()))

    def test_analytic_formulas_and_boundary(self):
        cases = json.loads(REPORT.read_text())["cases"]
        for c in cases:
            k = c["k"]
            self.assertEqual(c["source_ranks"], [10*k, 30*k+3, 30*k+6, 10*k+3])
            self.assertEqual(c["target_ranks"], [10*k, 30*k, 30*k, 10*k])
            self.assertEqual(Fraction(c["profile_surplus"]), Fraction(4*k-210, 81))
            self.assertEqual(Fraction(c["profile_surplus"]) > 0, k >= 53)
            self.assertTrue(c["passes_shared_leg_koszul"])
            self.assertFalse(c["degeneration_constructed"])
        smallest = next(c for c in cases if c["k"] == 53)
        self.assertEqual(Fraction(smallest["profile_ratio"]), Fraction(37206, 37205))


if __name__ == "__main__":
    unittest.main()

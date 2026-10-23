"""Exact finite comparisons supporting the stated all-size closure proof."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"research/ai/2026-10-21-finite-character-closure/verify.py"
SPEC=importlib.util.spec_from_file_location("finite_flag_closure",PATH)
VERIFY=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)

class FiniteFlagClosureTests(unittest.TestCase):
    def test_exact_profile_and_matrix_extraction_comparisons(self):
        expected=json.loads((ROOT/"results/finite-character-closure-2026-10-21/report.json").read_text())
        self.assertEqual(VERIFY.verify(),expected)
        self.assertEqual(sum(c["status"].startswith("accepted") for c in expected["cases"]),5)

if __name__=="__main__":
    unittest.main()

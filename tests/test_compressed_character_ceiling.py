"""Exact controls for the specified compressed tensor's character ceiling."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"research/ai/2026-10-21-compressed-packing/verify_character_ceiling.py"
SPEC=importlib.util.spec_from_file_location("compressed_character_ceiling",PATH)
VERIFY=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)

class CompressedCharacterCeilingTests(unittest.TestCase):
    def test_all_exact_controls_and_certified_thresholds(self):
        expected=json.loads((ROOT/"results/compressed-packing-2026-10-21/character_ceiling.json").read_text())
        self.assertEqual(VERIFY.report(),expected)

if __name__=="__main__":
    unittest.main()

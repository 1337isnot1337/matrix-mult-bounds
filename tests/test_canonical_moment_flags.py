"""Exact replay and corruption checks for the integer moment flags."""
import copy, importlib.util, json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/"research/ai/2026-10-21-canonical-moment-flags"
RESULTS=ROOT/"results/canonical-moment-flags-2026-10-21"

def load_module(name,filename):
    spec=importlib.util.spec_from_file_location(name,PACKAGE/filename)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

VERIFY=load_module("canonical_integer_replay","verify_witness.py")
CONSTRUCT=load_module("canonical_integer_t4","construct_t4.py")

class CanonicalMomentFlagTests(unittest.TestCase):
    def setUp(self):
        self.witness=json.loads((RESULTS/"m4-integer-witness.json").read_text())

    def test_literal_constructor_matches_frozen_maps(self):
        self.assertEqual(CONSTRUCT.construct(),self.witness)

    def test_all_four_hundred_coefficients(self):
        expected=json.loads((RESULTS/"m4-integer-verification.json").read_text())
        expected.pop("witness_sha256")
        self.assertEqual(VERIFY.verify(self.witness),expected)

    def test_nonzero_negative_coefficient_is_rejected(self):
        damaged=copy.deepcopy(self.witness)
        damaged["z"][0][12]=1
        with self.assertRaises(AssertionError):
            VERIFY.verify(damaged)

if __name__=="__main__":
    unittest.main()

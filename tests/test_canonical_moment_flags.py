"""Exact reconstruction, source replay, hashes, and corruption checks."""
import copy,hashlib,importlib.util,json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/"research/ai/2026-10-21-canonical-moment-flags"
RESULTS=ROOT/"results/canonical-moment-flags-2026-10-21"
def module(name,filename):
    spec=importlib.util.spec_from_file_location(name,PACKAGE/filename)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result
VERIFY=module("canonical_integer_replay","verify_witness.py")
T4=module("canonical_integer_t4","construct_t4.py")
LARGER=module("canonical_integer_larger","construct_larger.py")

class CanonicalMomentFlagTests(unittest.TestCase):
    def test_literal_reconstructions_and_source_coefficients(self):
        for m in (4,5,6,7):
            with self.subTest(m=m):
                raw=(RESULTS/f"m{m}-integer-witness.json").read_bytes()
                witness=json.loads(raw)
                actual=T4.construct() if m==4 else LARGER.construct(m)
                self.assertEqual(actual,witness)
                expected=json.loads((RESULTS/f"m{m}-integer-verification.json").read_text())
                digest=expected.pop("witness_sha256")
                self.assertEqual(hashlib.sha256(raw).hexdigest(),digest)
                self.assertEqual(VERIFY.verify(witness),expected)

    def test_nonzero_negative_coefficient_is_rejected(self):
        damaged=copy.deepcopy(T4.construct());damaged["z"][0][12]=1
        with self.assertRaises(AssertionError): VERIFY.verify(damaged)

    def test_six_sector_recovery_index_error_is_rejected(self):
        damaged=copy.deepcopy(LARGER.construct(6))
        # q=5 first row is row15; reproduce the recovered off-by-one error.
        damaged["z"][15][25]=1;damaged["z"][15][26]=-1;damaged["z"][15][27]=0
        with self.assertRaises(AssertionError): VERIFY.verify(damaged)

if __name__=="__main__": unittest.main()

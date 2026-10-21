"""Focused acceptance for the affine-carry finite-field artifact."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/"research/ai/2026-10-21-affine-carry-flags/verify_m6_f2.py"
SPEC=importlib.util.spec_from_file_location("affine_carry_verify",PATH)
VERIFY=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)

def load(name, filename):
    spec=importlib.util.spec_from_file_location(name,PATH.parent/filename)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

FIRST=load("affine_carry_first_flag","verify_first_flag.py")
LIFT=load("affine_carry_finite_lift","verify_finite_lift.py")

class AffineCarryFlagsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w=json.loads((ROOT/"results/affine-carry-flags-2026-10-21/m6-f2-witness.json").read_text())

    def test_full_source_coefficients(self):
        result=VERIFY.verify(self.w)
        self.assertEqual(result,{"all":2646,"negative":420,"constant":336,
                                 "constant_nonzero":118,"positive_nonzero":778})

    def test_corrupted_source_output_coefficient(self):
        bad=copy.deepcopy(self.w)
        bad["Z"][0][0]^=1
        with self.assertRaisesRegex(ValueError,"negative"):
            VERIFY.verify(bad)

    def test_all_size_first_flag_relation_controls(self):
        expected=json.loads((ROOT/"results/affine-carry-flags-2026-10-21/first-flag-controls.json").read_text())
        self.assertEqual(FIRST.verify(),expected)

    def test_finite_congruence_replay_has_only_its_stated_scope(self):
        folder=ROOT/"results/affine-carry-flags-2026-10-21"
        lift=json.loads((folder/"m6-finite-lift-1025.json").read_text())
        expected=json.loads((folder/"m6-finite-lift-replay.json").read_text())
        expected.pop("artifact_sha256")
        self.assertEqual(LIFT.verify_lift(self.w,lift),expected)

if __name__=="__main__":
    unittest.main()


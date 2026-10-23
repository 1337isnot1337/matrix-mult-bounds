"""Independent coefficient, residual-rank and scope controls for both variable legs."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-two-variable-long-legs"
SPEC = importlib.util.spec_from_file_location("two_variable_long_legs", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class TwoVariableLongLegTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maps = json.loads((v.RESULT / "maps.json").read_text())

    def test_complete_replay(self):
        expected = json.loads((v.RESULT / "verification.json").read_text())
        self.assertEqual(v.verify(self.maps), expected)
        self.assertEqual({x["prime"] for x in expected["cases"]}, {2, 3, 101})
        for case in expected["cases"]:
            self.assertTrue(case["both_maps_variable"])
            self.assertLess(case["channels"], case["m"])
            self.assertGreater(case["good_slice_lower_bound"], 0)

    def test_native_source_and_channel_mismatch_is_rejected(self):
        with patch.object(v, "channel_slice", return_value={}):
            with self.assertRaisesRegex(ValueError, "Source/channel identity"):
                v.check_case(self.maps["cases"][0])

    def test_nonindependent_profiles_are_rejected(self):
        case = copy.deepcopy(self.maps["cases"][0])
        case["c_profiles"][1] = case["c_profiles"][0][:]
        with self.assertRaisesRegex(ValueError, "profiles must be independent"):
            v.check_case(case)

    def test_missing_control_is_rejected(self):
        record = copy.deepcopy(self.maps)
        record["cases"].pop()
        with self.assertRaisesRegex(ValueError, "inventory"):
            v.verify(record)

    def test_strict_channel_boundary(self):
        boundary = self.maps["boundary"]
        self.assertEqual(v.boundary_control(boundary)["symbol_rank_at_X1_Y1_F101"], 4)
        with self.assertRaisesRegex(ValueError, "strict channel gap"):
            v.check_case(boundary)

    def test_bad_source_pin_is_rejected(self):
        sources = json.loads((PACKAGE / "sources.json").read_text())
        sources["local_dependencies"][0]["sha256"] = "0"*64
        with self.assertRaisesRegex(ValueError, "Source pin mismatch"):
            v.check_sources(sources)

    def test_empty_interior_and_nonlocal_exceptions(self):
        small = copy.deepcopy(self.maps["cases"][0])
        small["n"] = 6
        self.assertEqual(v.good_indices(small), ([], []))
        case = self.maps["cases"][2]
        self.assertTrue(case["b_exceptions"])
        column = case["b_exceptions"][0]
        self.assertTrue(any(h != column for h, _, _ in v.terms(case, "b", 0, column)))
        self.assertTrue(all(q+v0 not in case["b_exceptions"]
                            for q in v.good_indices(case)[1] for v0 in range(case["m"])))


if __name__ == "__main__":
    unittest.main()

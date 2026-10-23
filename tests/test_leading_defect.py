"""Replay singular leading equations and reject stronger unsupported conclusions."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-leading-defect"
SPEC = importlib.util.spec_from_file_location("leading_defect", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class LeadingDefectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(v.RESULT.read_text())

    def test_literal_source_and_exact_leading_replay(self):
        self.assertEqual(v.verify(self.record), {
            "leading_equation_controls": 11, "pencil_controls": 2,
            "bilinear_kernel_controls": 10, "coordinate_span_controls": 3,
            "literal_source_coefficients_checked": 125440,
            "complete_target_constructed": False, "improves_omega": False})

    def test_reject_false_completion_and_changed_intersection(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(equality_leading_first_map_rank=4),
            lambda x: x.update(equality_minimum_balanced_first_map_pole_order=11),
            lambda x: x["leading_equation_controls"][0].update(complete_target_identity=True),
            lambda x: x["leading_equation_controls"][0].update(constant_output_rank=110),
            lambda x: x["minimum_slice_pencils"][0].update(polynomial_intersection_dimension=1),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_changed_predecessor_pins(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(4):
            bad = copy.deepcopy(original)
            bad["local_dependencies"][i]["sha256"] = "0"*64
            with self.assertRaises(ValueError):
                v.check_sources(bad)
        bad = copy.deepcopy(original)
        bad["external_dependencies"].pop()
        with self.assertRaises(ValueError):
            v.check_sources(bad)


if __name__ == "__main__":
    unittest.main()

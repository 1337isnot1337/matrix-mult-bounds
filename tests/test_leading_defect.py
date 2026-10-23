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
            "leading_equation_controls": 11, "source_gap_controls": 2,
            "literal_source_coefficients_checked": 25088, "dimension_controls": 9,
            "complete_target_constructed": False, "improves_omega": False})


    def test_reject_false_completion_and_changed_rank_bounds(self):
        for mutate in (
            lambda x: x.update(improves_omega=True),
            lambda x: x.update(necessary_total_defect=21),
            lambda x: x.update(maximum_total_leading_rank=208),
            lambda x: x["leading_equation_controls"][0].update(complete_target_identity=True),
            lambda x: x["leading_equation_controls"][0].update(compressed_unit_rank=2),
            lambda x: x["source_gap_controls"][1].update(literal_rank=19),
        ):
            bad = copy.deepcopy(self.record)
            mutate(bad)
            with self.assertRaises(ValueError):
                v.verify(bad)

    def test_reject_changed_predecessor_pins(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for i in range(5):
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

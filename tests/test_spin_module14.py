"""Exact rational spin-one module, exported lifts, and conditional gate."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-20-anisotropic-constructions/spin_module14.py"
SPEC = importlib.util.spec_from_file_location("spin_module14", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SpinModule14Tests(unittest.TestCase):
    def test_rational_construction_and_exported_full_source_maps(self):
        exported = json.loads(MODULE.FULL_MAPS.read_text())
        report, regenerated = MODULE.verify(exported=exported)
        report["witness_sha256"] = hashlib.sha256(MODULE.WITNESS.read_bytes()).hexdigest()
        report["full_maps_sha256"] = hashlib.sha256(MODULE.FULL_MAPS.read_bytes()).hexdigest()
        self.assertEqual(regenerated, exported)
        self.assertEqual(report, json.loads(MODULE.REPORT.read_text()))
        self.assertEqual(report["full_source_lifts"][1]["nonzero_target_coefficients"], 252)
        self.assertEqual(report["full_source_lifts"][1]["actual_response_support_upper_bound"], 192)

    def test_changed_channel_map_is_rejected(self):
        witness = json.loads(MODULE.WITNESS.read_text())
        changed = copy.deepcopy(witness)
        changed["Y"]["entries"][0][2] += 1
        with self.assertRaises(ArithmeticError):
            MODULE.verify(witness=changed)

    def test_conditional_gate_is_not_a_construction_claim(self):
        budget = MODULE.conditional_square_budget()
        self.assertGreater(budget["lower_bound_sum"], budget["source_threshold"])
        self.assertEqual(budget["conditional_exponent"], "8999/4000")
        self.assertFalse(budget["full_target_constructed"])
        self.assertFalse(budget["new_exponent_established"])


if __name__ == "__main__":
    unittest.main()

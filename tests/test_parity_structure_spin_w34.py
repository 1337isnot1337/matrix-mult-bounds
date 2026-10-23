"""Exact four-chain spin-module controls, with no optional dependencies."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_w34.py"
SPEC = importlib.util.spec_from_file_location("parity_structure_spin_w34", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FourChainSpinTests(unittest.TestCase):
    def test_complete_source_replay_and_rank_certificates(self):
        report = MODULE.verify()
        self.assertEqual(report["construction"]["ignored_space_dimension"], 34)
        self.assertEqual(report["construction"]["join_rank"], 76)
        self.assertEqual(report["construction"]["join_minor_determinant"], "1/73728")
        self.assertEqual(report["full_source_replays"][1]["source_terms_checked"], 262144)
        self.assertEqual(report["full_source_replays"][1]["nonzero_target_coefficients"], 252)
        self.assertEqual(report["full_first_response_rank_exact"], 192)
        self.assertEqual(report["G1_delete0_exclude1"]["rank_exact"], 117)
        self.assertFalse(report["new_exponent_established"])

    def test_nonzero_map_tamper_is_rejected(self):
        witness = json.loads(MODULE.WITNESS.read_text())
        witness["Y"]["entries"][0][2] *= 2
        with self.assertRaises(ArithmeticError):
            MODULE.verify(witness=witness)

    def test_false_kernel_vector_is_rejected(self):
        specification = json.loads(MODULE.G1_KERNEL.read_text())
        specification = copy.deepcopy(specification)
        specification["kernel_vectors"][0] = [[0, 1]]
        exported = json.loads(MODULE.MAPS.read_text())
        Z, _ = MODULE.unpack(exported["restrictions"][1]["maps"]["Z"], (84, 960))
        with self.assertRaises(ArithmeticError):
            MODULE.check_g1_kernel(Z, specification)


if __name__ == "__main__":
    unittest.main()

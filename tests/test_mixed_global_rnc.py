"""Finite convention checks for the written global RNC obstruction."""
from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-mixed-longlegs-candidate"
SPEC = importlib.util.spec_from_file_location("mixed_global_rnc", PACKAGE / "verify_global_rnc.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class MixedGlobalRncTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = VERIFY.report()

    def test_reproduce_exact_report(self):
        saved = json.loads((ROOT / "results/mixed-longlegs-candidate-2026-10-23/global_rnc_verification.json").read_text())
        self.assertEqual(saved, self.report)
        self.assertFalse(self.report["arbitrary_arc_theorem_verified_by_finite_controls"])

    def test_literal_binary_substitution_and_dual_convention(self):
        self.assertEqual(len(self.report["binary_covariance"]), 4)
        count = sum(row[key] for row in self.report["binary_covariance"]
                    for key in ("flattening_covariance_equalities", "tensor_covariance_equalities",
                                "scalar_compensation_equalities"))
        self.assertEqual(count, 8400)

    def test_rank_one_slice_scope_and_boundary(self):
        self.assertEqual(len(self.report["full_rank_one_slices"]), 15)
        self.assertEqual(len(self.report["full_noncurve_slices"]), 6)
        self.assertEqual(len(self.report["nonfull_slices"]), 42)
        self.assertTrue(all(row["rank"] > 1 for row in self.report["nonfull_slices"]))
        self.assertEqual(self.report["width_one_boundary_control"]["rank"], 1)
        self.assertNotEqual(self.report["width_one_boundary_control"]["rnc_quadratic_value"], 0)

    def test_third_conciseness_from_literal_blocks(self):
        self.assertEqual(len(self.report["third_conciseness"]), 6)
        self.assertEqual((self.report["source_third_rank"], self.report["target_third_rank"]), (140, 140))

    def test_frozen_integrated_files(self):
        manifest = json.loads((PACKAGE / "global_rnc_manifest.json").read_text())
        for item in manifest["integrated_files"]:
            self.assertEqual(sha256((ROOT / item["path"]).read_bytes()).hexdigest(), item["sha256"], item["path"])


if __name__ == "__main__":
    unittest.main()

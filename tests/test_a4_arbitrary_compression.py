"""Exact arbitrary-flag coverage and adversarial certificate controls."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-a4-compression-algebra"
RESULTS = ROOT / "results/a4-compression-algebra-2026-10-23"
spec = importlib.util.spec_from_file_location("a4_arbitrary_compression_test", PACKAGE / "verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class ArbitraryCompressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads((RESULTS / "certificate.json").read_text())

    def test_complete_source_and_all_flag_budgets(self):
        report = verify.accept(self.certificate)
        self.assertEqual(report, json.loads((RESULTS / "verification.json").read_text()))
        self.assertEqual(report["budget_pairs_checked"], 2809)
        self.assertEqual(report["universal_rank26_compression_image_dimension_at_least"], 38)
        self.assertEqual(report["fixed_full_limit_rank110_compression_image_dimension_at_least"], 104)
        self.assertFalse(report["arbitrary_moving_long_factor_maps_excluded"])
        self.assertFalse(report["exponent_improvement_claimed"])

    def test_omitted_budget_pair_is_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad["coverage"]["coarse"].pop()
        with self.assertRaisesRegex(ValueError, "finite coverage"):
            verify.accept(bad)

    def test_duplicate_budget_pair_is_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad["coverage"]["coarse"][-1] = bad["coverage"]["coarse"][0]
        with self.assertRaisesRegex(ValueError, "finite coverage"):
            verify.accept(bad)

    def test_false_hessian_rank_is_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad["coverage"]["quadratic"][0]["degrees"][8]["hessian_rank"] += 1
        with self.assertRaisesRegex(ValueError, "rational rank"):
            verify.accept(bad)

    def test_false_minor_combination_is_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad["minor_identities"]["degree4_caps1111"][0][0][1] += 1
        with self.assertRaisesRegex(ValueError, "minor identity|minor-identity|minor index"):
            verify.accept(bad)

    def test_missing_identity_case_is_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad["minor_identities"].pop("degree5_caps121")
        with self.assertRaisesRegex(ValueError, "minor-identity cases"):
            verify.accept(bad)

    def test_invalid_rational_coefficient_is_rejected(self):
        bad = copy.deepcopy(self.certificate)
        bad["minor_identities"]["degree5_caps111"][0][0][2] = 0
        with self.assertRaisesRegex(ValueError, "coefficient"):
            verify.accept(bad)

    def test_changed_prior_source_pin_is_rejected(self):
        manifest = json.loads((PACKAGE / "sources.json").read_text())
        manifest["repository_inputs"][0]["sha256"] = "0" * 64
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary)
            (package / "sources.json").write_text(json.dumps(manifest))
            with mock.patch.object(verify, "PACKAGE", package):
                with self.assertRaisesRegex(ValueError, "pinned prior source"):
                    verify.check_source_pins()


if __name__ == "__main__":
    unittest.main()

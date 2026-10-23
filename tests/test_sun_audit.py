"""Exact regression checks for the bounded Sun certificate audit."""

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "research/ai/2026-10-21-sun-audit/verify.py"
SPEC = importlib.util.spec_from_file_location("sun_audit_verify", MODULE)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class SunAuditTests(unittest.TestCase):
    def test_literal_normalization_and_repair(self):
        report = audit.scalar_audit()
        self.assertEqual(report["source_support_occurrences"], 354)
        self.assertEqual(len(report["literal_mismatches"]), 50)
        self.assertEqual(report["repair_mismatch_count"], 0)

    def test_complete_walsh_and_chart_domains(self):
        walsh = audit.walsh_audit()
        charts = audit.chart_audit()
        self.assertEqual(walsh["nonzero_integer_numerators"], [[0, 0, 128], [3, 15, 128]])
        self.assertEqual(charts["defects_checked"], 128)
        self.assertEqual(charts["failures"], [])

    def test_packet_obstruction_including_all_off_support_coefficients(self):
        report = audit.packet_pullback_audit()
        self.assertEqual(report["all_central_coefficient_checks"], 768)
        coefficients = report["all_64_coefficients"]
        self.assertEqual(len(coefficients), 64)
        self.assertEqual(sum(v["coefficient"] == "1/16" for v in coefficients), 8)
        self.assertEqual(sum(v["coefficient"] == "0" for v in coefficients), 56)
        self.assertEqual(report["koszul"]["rank"], 16)
        self.assertEqual(report["koszul"]["minor_determinant"], "1")
        self.assertEqual(report["koszul"]["border_rank_lower_bound"], 6)

    def test_five_empty_rational_module(self):
        report = audit.empty_module_audit()
        self.assertEqual(report["character_action_products"], 256)
        self.assertEqual(report["character_action_failures"], [])


if __name__ == "__main__":
    unittest.main()

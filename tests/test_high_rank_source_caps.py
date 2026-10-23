"""Source sharpness, strict thresholds and the full-short arithmetic gap."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-high-rank-source-caps/verify.py"
SPEC = importlib.util.spec_from_file_location("high_rank_source_caps", PATH)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class HighRankSourceCapsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads(VERIFY.RESULT.read_text())
        cls.certificates = json.loads(VERIFY.CERTIFICATES.read_text())
        cls.coherent, cls.source = VERIFY.literal_bases()

    def test_complete_report_and_all_fifteen_minors(self):
        VERIFY.replay_saved(self.report)
        self.assertEqual(self.report["source_controls"]["literal_source_terms"], 4096)
        self.assertEqual(self.report["source_controls"]["source_factorizations_checked"], 112)
        self.assertEqual(self.report["coherent_controls"]["credited_integer_minors_replayed"], 11)
        self.assertEqual(self.report["sharpness_controls"]["integer_sharpness_minors_replayed"], 4)
        self.assertEqual(self.report["profile_controls"]["all_nonincreasing_layer_size_profiles"], 245157)
        self.assertEqual([self.report["profile_controls"]["thresholds"][str(r)]["maximum_volume"]
                          for r in VERIFY.THRESHOLDS], [84, 88, 92, 96])

    def test_written_cases_and_strict_rank_endpoints(self):
        boundaries = [
            (100, (16, 12, 12, 12, 12, 12, 12)),
            (104, (16, 16, 12, 12, 12, 12, 12)),
            (108, (16, 16, 16, 12, 12, 12, 12)),
            (112, (16, 16, 16, 16, 12, 12, 12)),
        ]
        for threshold, profile in boundaries:
            self.assertEqual(VERIFY.necessary_rank_lower(profile), threshold)
            self.assertGreater(sum(profile), VERIFY.DIMENSIONS[VERIFY.THRESHOLDS.index(threshold)])
        self.assertEqual([VERIFY.source_dimension_cap(r) for r in (99, 100, 103, 104, 107, 108, 111, 112)],
                         [84, 88, 88, 92, 92, 96, 96, 112])
        with self.assertRaisesRegex(ArithmeticError, "invalid layer profile"):
            VERIFY.necessary_rank_lower((0, 1, 0, 0, 0, 0, 0))
        with self.assertRaisesRegex(ArithmeticError, "unsupported theorem"):
            VERIFY.dominating_profile((12,)*7, 101)

    def test_sharp_staircase_support_and_attained_ranks(self):
        result = VERIFY.sharpness_controls(self.certificates["sharp_spaces"], self.source)
        self.assertEqual([record["dimension"] for record in result["sharp_spaces"]], [84, 88, 92, 96])
        self.assertEqual([record["attained_rank"] for record in result["sharp_spaces"]], [96, 100, 104, 108])
        self.assertEqual([record["literal_terms_covered"] for record in result["sharp_spaces"]],
                         [3072, 3136, 3264, 3456])
        wrong = copy.deepcopy(self.certificates["sharp_spaces"])
        wrong.pop()
        with self.assertRaisesRegex(ArithmeticError, "inventory"):
            VERIFY.sharpness_controls(wrong, self.source)
        wrong = copy.deepcopy(self.certificates["sharp_spaces"])
        wrong[2]["rank_upper"] = 103
        with self.assertRaisesRegex(ArithmeticError, "rank budget"):
            VERIFY.sharpness_controls(wrong, self.source)

    def test_minor_rejects_outside_support_and_singular_coefficients(self):
        record = self.certificates["sharp_spaces"][3]
        minor = {key: record[key] for key in VERIFY.MINOR_FIELDS}
        minor["coefficient_mask"] = hex(1 << VERIFY.SOURCE.index((3, 6, 3)))
        with self.assertRaisesRegex(ArithmeticError, "support"):
            VERIFY.replay_minor(minor, self.source, VERIFY.SOURCE, 112, 108, VERIFY.family_coordinates(3))
        minor["coefficient_mask"] = "0x1"
        with self.assertRaisesRegex(ArithmeticError, "singular"):
            VERIFY.replay_minor(minor, self.source, VERIFY.SOURCE, 112, 108, VERIFY.family_coordinates(3))

    def test_exact_columns_and_unsupported_boundary_are_not_weakened(self):
        for record in self.certificates["sharp_spaces"]:
            allowed = VERIFY.family_coordinates(record["m"])
            columns = set(VERIFY.indices(int(record["column_support_mask"], 16), 112))
            self.assertGreater(VERIFY.check_column_support(allowed, columns, self.source), 0)
            with self.assertRaisesRegex(ArithmeticError, "literal joint support"):
                VERIFY.check_column_support(allowed, columns-{0}, self.source)
        with self.assertRaisesRegex(ArithmeticError, "scoped"):
            VERIFY.family_coordinates(4)
        boundary = self.report["sharpness_controls"]["boundary_m4"]
        self.assertEqual((boundary["dimension"], boundary["supported_columns"]), (100, 112))
        self.assertFalse(boundary["strict_rank112_hypothesis_proved_by_support"])
        counterexamples = self.report["sharpness_controls"]["weak_threshold_counterexamples"]
        self.assertEqual([record["dimension"] for record in counterexamples], [88, 92, 96, 112])
        self.assertTrue(all(record["dimension"] > record["exceeded_cap"] for record in counterexamples))

    def test_complete_full_short_gap_endpoint_and_retained_guard(self):
        target = VERIFY.target_controls()
        self.assertEqual(target["retained_long_ranks"], list(range(13))+[20])
        self.assertEqual(target["newly_excluded_long_ranks"], list(range(13, 20))+list(range(21, 29)))
        self.assertEqual((target["one_leg_cases_checked"], target["two_long_cases_checked"]), (102, 10404))
        self.assertEqual((target["prior_surviving_triples"], target["retained_triples"], target["newly_excluded_triples"]),
                         (841, 196, 645))
        self.assertEqual((target["screen_maximum_total"], target["screen_maximizers"]), (140, [[100, 20, 20]]))
        for r in (12, 20):
            self.assertFalse(VERIFY.full_short_screen(r)["excluded"])
        for r in (13, 19, 21, 28):
            self.assertTrue(VERIFY.full_short_screen(r)["excluded"])
        self.assertTrue(VERIFY.full_short_screen(101)["excluded_by_prior28"])
        self.assertFalse(VERIFY.full_short_screen(101, use_prior=False)["excluded"])
        with self.assertRaisesRegex(ArithmeticError, "individual bound"):
            VERIFY.full_short_screen(102)

    def test_source_versions_and_coherent_inventory_are_pinned(self):
        source = json.loads((VERIFY.HERE / "sources.json").read_text())
        VERIFY.check_sources(source)
        wrong = copy.deepcopy(source)
        wrong["local_dependencies"][0]["sha256"] = "0"*64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            VERIFY.check_sources(wrong)
        wrong = copy.deepcopy(source)
        wrong["local_dependencies"].pop()
        with self.assertRaisesRegex(ArithmeticError, "source inventory"):
            VERIFY.check_sources(wrong)
        source["field"] = "F2"
        with self.assertRaisesRegex(ArithmeticError, "version or field"):
            VERIFY.check_sources(source)
        wrong_certificates = copy.deepcopy(self.certificates)
        wrong_certificates["coherent13_ideals"].pop()
        with self.assertRaisesRegex(ArithmeticError, "credited coherent"):
            VERIFY.coherent_controls(wrong_certificates, self.coherent)

    def test_target_and_source_scope_cannot_be_strengthened_silently(self):
        for field in ("screen_maximizer_is_target_construction", "target_bound_sharp", "improves_omega",
                      "all_extremizers_classified"):
            wrong = copy.deepcopy(self.report)
            wrong["claim_scope"][field] = True
            with self.assertRaisesRegex(ArithmeticError, "scope"):
                VERIFY.replay_saved(wrong)
        wrong = copy.deepcopy(self.report)
        wrong["claim_scope"]["short_rank100_allowed_positive_long_ranks"] = list(range(1, 21))
        with self.assertRaisesRegex(ArithmeticError, "scope"):
            VERIFY.replay_saved(wrong)


if __name__ == "__main__":
    unittest.main()

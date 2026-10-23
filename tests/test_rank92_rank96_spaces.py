"""Exact controls for the sharp source caps below ranks92 and96."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-rank92-rank96-spaces/verify.py"
SPEC = importlib.util.spec_from_file_location("rank92_rank96_verifier", PATH)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class Rank92Rank96SpacesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificates = json.loads(VERIFY.CERTIFICATES.read_text())
        cls.coherent, cls.source = VERIFY.literal_bases()

    def test_complete_report_and_written_cases(self):
        report = json.loads(VERIFY.RESULT.read_text())
        VERIFY.replay_saved(report)
        profiles = report["profile_controls"]
        self.assertEqual(profiles["all_nonincreasing_layer_size_profiles"], 245157)
        self.assertEqual(profiles["thresholds"]["92"]["maximum_volume"], 68)
        self.assertEqual(profiles["thresholds"]["96"]["maximum_volume"], 72)
        self.assertEqual(len(profiles["thresholds"]["92"]["written_case_counts"]), 4)
        self.assertEqual(len(profiles["thresholds"]["96"]["written_case_counts"]), 3)

    def test_source_pins_and_coherent_inventory_reject_corruption(self):
        sources = json.loads((VERIFY.HERE / "sources.json").read_text())
        sources["local_dependencies"][0]["sha256"] = "0"*64
        with self.assertRaisesRegex(ArithmeticError, "digest"):
            VERIFY.check_sources(sources)
        bad = copy.deepcopy(self.certificates)
        bad["coherent9_ideals"].pop()
        with self.assertRaises(ArithmeticError):
            VERIFY.coherent_controls(bad, self.coherent)

    def test_minor_rejects_wrong_support_and_singular_coefficients(self):
        record = self.certificates["sharp_spaces"][0]
        minor = {key: record[key] for key in VERIFY.MINOR_FIELDS}
        outside = VERIFY.SOURCE.index((3, 6, 3))
        minor["coefficient_mask"] = hex(1 << outside)
        with self.assertRaisesRegex(ArithmeticError, "support"):
            VERIFY.replay_minor(minor, self.source, VERIFY.SOURCE, 112, 91,
                                VERIFY.family_coordinates(2))
        minor["coefficient_mask"] = "0x1"
        with self.assertRaisesRegex(ArithmeticError, "singular"):
            VERIFY.replay_minor(minor, self.source, VERIFY.SOURCE, 112, 91,
                                VERIFY.family_coordinates(2))

    def test_cover_rejects_missing_essential_row_or_column(self):
        for record in self.certificates["sharp_spaces"]:
            allowed = VERIFY.family_coordinates(record["m"])
            rows = set(VERIFY.indices(int(record["row_cover_mask"], 16), 112))
            columns = set(VERIFY.indices(int(record["column_cover_mask"], 16), 112))
            self.assertGreater(VERIFY.check_cover(allowed, rows, columns, self.source), 0)
            with self.assertRaisesRegex(ArithmeticError, "misses"):
                VERIFY.check_cover(allowed, rows-{84}, columns, self.source)
            with self.assertRaisesRegex(ArithmeticError, "misses"):
                VERIFY.check_cover(allowed, rows, columns-{0}, self.source)

    def test_m1_cover_extension_is_not_accepted(self):
        with self.assertRaisesRegex(ArithmeticError, "scoped"):
            VERIFY.family_coordinates(1)
        rows = set(range(84, 91))
        columns = set(range(80))
        self.assertIn((56, 80), self.source[(3, 0, 0)])
        with self.assertRaisesRegex(ArithmeticError, "misses"):
            VERIFY.check_cover({(3, 0, 0)}, rows, columns, self.source)

    def test_strict_thresholds_and_scope_are_preserved(self):
        self.assertEqual([VERIFY.source_dimension_cap(rank) for rank in (91, 92, 95, 96)],
                         [68, 72, 72, 112])
        wrong_budget = copy.deepcopy(self.certificates["sharp_spaces"])
        wrong_budget[0]["rank_upper"] = 90
        with self.assertRaisesRegex(ArithmeticError, "budget"):
            VERIFY.sharpness_controls(wrong_budget, self.source)
        wrong_scope = json.loads(VERIFY.RESULT.read_text())
        wrong_scope["claim_scope"]["target_rank_pair_theorem_claimed"] = True
        with self.assertRaisesRegex(ArithmeticError, "scope"):
            VERIFY.replay_saved(wrong_scope)


if __name__ == "__main__":
    unittest.main()

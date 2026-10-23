from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/ai/2026-10-23-exact-monomial-search/search.py"
SPEC = importlib.util.spec_from_file_location("exact_monomial_search", SCRIPT)
SEARCH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SEARCH)


class ExactMonomialSearchTests(unittest.TestCase):
    def test_exact_ordering_breaks_float_tie(self):
        lower = Fraction(2**60 - 2, 2**60)
        higher = Fraction(2**60 - 1, 2**60)
        self.assertEqual(float(lower), float(higher))
        lower_record = {
            "dimensions": [2, 2, 3],
            "weights": {"x": [0, 0], "y": [0, 0]},
            "score": {"ratio_exact": str(lower)},
        }
        higher_record = {
            "dimensions": [2, 2, 3],
            "weights": {"x": [0, 1], "y": [0, 1]},
            "score": {"ratio_exact": str(higher)},
        }
        top = []
        SEARCH.offer(top, lower_record, limit=1)
        SEARCH.offer(top, higher_record, limit=1)
        self.assertEqual(top[0]["score"]["ratio_exact"], str(higher))

    def test_nontrivial_support_certificate_replays(self):
        first = SEARCH.make_record((0, 0), (0, 1, 1, 0))
        SEARCH.replay_record(first)
        self.assertEqual(first["score"]["source_exact"], "6")
        self.assertEqual(first["score"]["target_exact"], "6")
        self.assertEqual(len(first["blocks"]), 3)

    def test_input_roles_are_not_canonicalized_by_swapping(self):
        original = SEARCH.make_record((-7, 2, -1, -6), (-5, -8))
        swapped = SEARCH.make_record((-5, -8), (-7, 2, -1, -6))
        SEARCH.replay_record(original)
        SEARCH.replay_record(swapped)
        self.assertEqual(original["score"]["ratio_exact"], "1/2")
        self.assertEqual(swapped["score"]["ratio_exact"], "1")

    def test_corrupted_support_is_rejected(self):
        record = SEARCH.make_record((0, 0), (0, 1, 1, 0))
        record["support_certificate"]["zero_terms"].pop()
        with self.assertRaisesRegex(ValueError, "does not replay"):
            SEARCH.replay_record(record)

    def test_small_search_has_exact_top_score(self):
        report = SEARCH.run_search("binary", max_sum=5, top_k=3)
        self.assertEqual(report["cases_tested"], 30)
        self.assertEqual(report["exact_violation_count"], 0)
        self.assertEqual(report["leaderboard"][0]["score"]["ratio_exact"], "1")


if __name__ == "__main__":
    unittest.main()

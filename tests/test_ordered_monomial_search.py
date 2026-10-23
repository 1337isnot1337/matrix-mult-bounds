from contextlib import redirect_stdout
from copy import deepcopy
from fractions import Fraction
import importlib.util
from io import StringIO
from itertools import product
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-ordered-monomial-search"


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, PACKAGE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VERIFY = load("ordered_monomial_verify", "verify.py")
# The executable search imports its sibling. Keep that generic name local to
# module initialization so other tests retain their own import environment.
previous = sys.modules.get("verify")
sys.modules["verify"] = VERIFY
try:
    SEARCH = load("ordered_monomial_search", "search.py")
finally:
    if previous is None:
        del sys.modules["verify"]
    else:
        sys.modules["verify"] = previous


class OrderedMonomialSearchTests(unittest.TestCase):
    def test_all_small_ordered_supports_match_independent_verifier(self):
        count = 0
        for a in range(2, 5):
            for b in range(2, 7 - a):
                for x in product(range(2), repeat=a):
                    for y in product(range(2), repeat=b):
                        if min(x) == min(y) == 0:
                            VERIFY.check_record(SEARCH.candidate(x, y, SEARCH.ARCHIVE.slopes(6)))
                            count += 1
        self.assertEqual(count, 190)

    def test_input_swap_changes_actual_shared_axis_score(self):
        h = SEARCH.ARCHIVE.slopes(5)
        original = SEARCH.candidate((0, 0), (0, 0, 1), h)
        swapped = SEARCH.candidate((0, 0, 1), (0, 0), h)
        self.assertEqual(VERIFY.check_record(original), Fraction(13, 14))
        self.assertEqual(VERIFY.check_record(swapped), Fraction(9, 14))

    def test_omitted_orientation_can_score_strictly_higher(self):
        h = SEARCH.ARCHIVE.slopes(7)
        original = SEARCH.candidate((0, 0, 0), (0, 1, 0, 1), h)
        swapped = SEARCH.candidate((0, 1, 0, 1), (0, 0, 0), h)
        self.assertEqual(VERIFY.check_record(original), Fraction(18, 35))
        self.assertEqual(VERIFY.check_record(swapped), Fraction(9, 14))

    def test_all_size_alternating_family_exact_controls(self):
        for m in range(2, 13):
            with self.subTest(m=m):
                h = SEARCH.ARCHIVE.slopes(2 * m + 3)
                x, y = (0, 0, 0), (0, 1) * m
                original = SEARCH.candidate(x, y, h)
                swapped = SEARCH.candidate(y, x, h)
                VERIFY.check_record(original)
                self.assertEqual(VERIFY.check_record(swapped), Fraction(9, 14))
                self.assertEqual(Fraction(original["score"]["target"]), max(3, m) + 1)
                self.assertEqual(Fraction(swapped["score"]["target"]), 2 * m + 1)

    def test_corrupted_support_partition_block_and_score_are_rejected(self):
        record = SEARCH.candidate((0, 0), (0, 0, 1), SEARCH.ARCHIVE.slopes(5))
        edits = [lambda r: r["support"]["terms"].pop(),
                 lambda r: r["support"]["sectors"].reverse(),
                 lambda r: r["blocks"][0].update(a=3),
                 lambda r: r["score"].update(target="5")]
        for edit in edits:
            with self.subTest(edit=edit):
                bad = deepcopy(record)
                edit(bad)
                with self.assertRaises(ValueError):
                    VERIFY.check_record(bad)

    def test_ordered_count_formula_and_small_completed_run(self):
        self.assertEqual(VERIFY.coverage(2, 11),
                         {"historical": 12976, "omitted": 11732, "ordered": 24708})
        self.assertEqual(VERIFY.coverage(3, 10),
                         {"historical": 209692, "omitted": 160560, "ordered": 370252})
        with redirect_stdout(StringIO()):
            report = SEARCH.run(2, 5)
        self.assertEqual(report["coverage"]["ordered"], 51)
        self.assertEqual(report["orientation_comparison"]["historical_better"], 12)
        VERIFY.check_report(json.loads(json.dumps(report)))
        bad = deepcopy(report)
        bad["coverage"]["omitted"] -= 1
        with self.assertRaisesRegex(ValueError, "coverage"):
            VERIFY.check_report(bad)
        bad = deepcopy(report)
        bad["dimension_summaries"]["omitted"] = []
        with self.assertRaisesRegex(ValueError, "inventory"):
            VERIFY.check_report(bad)

    def test_saved_reports_accept_independently(self):
        for mode in ("binary", "ternary"):
            path = ROOT / f"results/ordered-monomial-search-2026-10-23/{mode}.json"
            report = json.loads(path.read_text())
            self.assertEqual(VERIFY.check_report(report), report["acceptance"])


if __name__ == "__main__":
    unittest.main()

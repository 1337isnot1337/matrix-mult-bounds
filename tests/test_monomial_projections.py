from fractions import Fraction
import importlib.util
from itertools import product
from pathlib import Path
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/ai/2026-10-23-monomial-projections/verify.py"
SPEC = importlib.util.spec_from_file_location("monomial_projections", SCRIPT)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def direct_optimum(terms):
    ys, zs = (sorted({t[k] for t in terms}) for k in (1, 2))
    best = Fraction()
    for ym, zm in product(range(1 << len(ys)), range(1 << len(zs))):
        ykeep = {y for i, y in enumerate(ys) if ym & (1 << i)}
        zkeep = {z for i, z in enumerate(zs) if zm & (1 << i)}
        kept = tuple(t for t in terms if t[1] in ykeep and t[2] in zkeep)
        best = max(best, VERIFY.component_score(kept))
    return best


class MonomialProjectionTests(unittest.TestCase):
    def test_all_two_by_three_supports_against_all_masks(self):
        full = [(i, j, i+j) for i in range(2) for j in range(3)]
        for mask in range(1 << len(full)):
            terms = tuple(t for k, t in enumerate(full) if mask & (1 << k))
            value, kept = VERIFY.optimize(terms)
            self.assertEqual(value, direct_optimum(terms), mask)
            ys, zs = {t[1] for t in kept}, {t[2] for t in kept}
            self.assertEqual(kept, tuple(t for t in terms if t[1] in ys and t[2] in zs))
            self.assertEqual(value, VERIFY.component_score(kept))

    def test_worked_example_and_independent_replay(self):
        record = VERIFY.make_record((0, 0, 1), (0, 0, 0))
        self.assertEqual(record["old_score_exact"], "3")
        self.assertEqual(record["projected_score_exact"], "5")
        self.assertEqual(record["ratio_exact"], "45/56")
        self.assertEqual(record["keep_y"], [0, 2])
        self.assertEqual(len(VERIFY.components(map(tuple, record["projected_terms"]))), 2)
        with patch.object(VERIFY, "optimize", side_effect=AssertionError("optimizer called")):
            VERIFY.replay_record(record)

    def test_corrupted_term_score_and_mask_are_rejected(self):
        for field, bad in (("projected_score_exact", "6"), ("keep_y", [0, 1, 2]),
                           ("keep_z", [99]), ("projected_terms", [])):
            record = VERIFY.make_record((0, 0, 1), (0, 0, 0))
            record[field] = bad
            with self.assertRaises(ValueError):
                VERIFY.replay_record(record)

    def test_small_census_is_complete_and_has_a_strict_gain(self):
        report = VERIFY.run(2, 6)
        self.assertEqual(report["cases_tested"], 190)
        self.assertEqual(report["strict_score_improvements"], 35)
        self.assertEqual(report["exact_violation_count"], 0)
        self.assertEqual(report["best"]["ratio_exact"], "1")
        for field in ("best", "first_improvement", "worked_example"):
            VERIFY.replay_record(report[field])


if __name__ == "__main__":
    unittest.main()

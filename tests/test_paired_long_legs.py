import importlib.util
from itertools import combinations
import json
from pathlib import Path
import unittest


VERIFY_PATH = (
    Path(__file__).resolve().parents[1]
    / "research/ai/2026-10-23-paired-long-legs/verify.py"
)
SPEC = importlib.util.spec_from_file_location("paired_long_legs_verify", VERIFY_PATH)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)
RESULTS = Path(__file__).resolve().parents[1] / "results/paired-long-legs-2026-10-23"
RANK_ATLAS_PATH = (
    Path(__file__).resolve().parents[1]
    / "research/ai/2026-10-23-paired-long-legs/rank_atlas.py"
)


class PairedLongLegTests(unittest.TestCase):
    def test_saved_verification_report_replays(self):
        saved = json.loads((RESULTS / "verification.json").read_text())
        actual = json.loads(json.dumps(VERIFY.verify(rank_controls=True)))
        self.assertEqual(actual, saved)

    def test_exact_interpolation_and_full_spark_controls(self):
        for a in range(2, 7):
            with self.subTest(a=a):
                result = VERIFY.verify_interpolation(a)
                self.assertEqual(result["product_coefficients"], a * a)
                self.assertEqual(
                    result["full_spark_subsets"],
                    __import__("math").comb(2 * a - 1, a),
                )

    def test_saved_survivor_alignment(self):
        result = VERIFY.verify_saved_frontier()
        self.assertEqual(result["survivors"], 28)
        self.assertEqual(result["forced_short_leg_strict"], 22)
        self.assertEqual(result["square_outer_equalities"], 6)

    def test_independent_source_rank_controls(self):
        for a in (2, 3):
            for p in range(a + 1):
                with self.subTest(a=a, p=p):
                    result = VERIFY.verify_source_rank_mod2(a, p)
                    self.assertTrue(result["full_column_rank"])

    def test_first_higher_degree_pilots(self):
        rational = VERIFY.verify_small_source_rank_over_q(2, 3)
        self.assertEqual(rational["rank_over_q"], 70)
        self.assertEqual(rational["domain"], 80)
        self.assertEqual(rational["kernel_dimension"], 10)
        ternary = VERIFY.verify_source_rank_mod2(3, 4)
        self.assertTrue(ternary["full_column_rank"])

    def test_support_count_matches_small_block_enumeration(self):
        for a in (2, 3, 4):
            n = a * (2 * a - 1)
            for p in range(a + 2):
                with self.subTest(a=a, p=p):
                    expected = sum(
                        len({index // a for index in subset}) <= a - 1
                        for subset in combinations(range(n), p)
                    )
                    self.assertEqual(VERIFY.support_low_count(a, p), expected)

    def test_p_a_plus_1_target_rank_floor_scope(self):
        report = VERIFY.verify_support_dominance()
        records = {item["a"]: item for item in report["records"]}
        self.assertEqual(
            [len(records[a]["target_b_rank_not_larger"]) for a in (14, 15, 16)],
            [0, 4, 6],
        )
        self.assertTrue(
            all(not item["target_c_rank_not_larger"] for item in records.values())
        )

    def test_a3_graded_higher_degree_rank_atlas_replays(self):
        spec = importlib.util.spec_from_file_location(
            "paired_long_legs_rank_atlas", RANK_ATLAS_PATH
        )
        atlas = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(atlas)
        saved = json.loads((RESULTS / "graded-rank-atlas-a3.json").read_text())
        actual = json.loads(json.dumps(atlas.atlas(3, [4, 5, 6, 7])))
        self.assertEqual(actual, saved)
        self.assertEqual(saved["records"][-1]["kernel_dimension_over_q"], 730)


if __name__ == "__main__":
    unittest.main()

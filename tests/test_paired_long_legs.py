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
KERNEL_REPRESENTATION_PATH = (
    Path(__file__).resolve().parents[1]
    / "research/ai/2026-10-23-paired-long-legs/kernel_representation.py"
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
        self.assertEqual(
            [len(records[a]["target_c_rank_not_larger"]) for a in (14, 15, 16)],
            [0, 4, 6],
        )
        for record in records.values():
            self.assertEqual(
                record["target_b_rank_not_larger"],
                record["target_c_rank_not_larger"],
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

    def test_saved_a4_p5_full_rank_control(self):
        saved = json.loads(
            (RESULTS / "graded-rank-atlas-a4-p5.json").read_text()
        )
        record = saved["records"][0]
        self.assertEqual((record["a"], record["p"]), (4, 5))
        self.assertEqual(record["bigrade_blocks"], 524)
        self.assertEqual(record["domain"], 1_572_480)
        self.assertEqual(record["rank_mod_2"], record["domain"])
        self.assertEqual(record["rank_over_q"], record["domain"])
        self.assertEqual(record["kernel_dimension_over_q"], 0)

    def test_saved_kernel_representation_decompositions_replay(self):
        atlas_spec = importlib.util.spec_from_file_location(
            "paired_long_legs_rank_atlas", RANK_ATLAS_PATH
        )
        atlas = importlib.util.module_from_spec(atlas_spec)
        atlas_spec.loader.exec_module(atlas)
        a2_saved = json.loads((RESULTS / "graded-rank-atlas-a2-p3.json").read_text())
        self.assertEqual(
            json.loads(json.dumps(atlas.atlas(2, [3]))),
            a2_saved,
        )
        a3_p8_saved = json.loads(
            (RESULTS / "graded-rank-atlas-a3-p8.json").read_text()
        )
        self.assertEqual(
            json.loads(json.dumps(atlas.atlas(3, [8]))),
            a3_p8_saved,
        )
        a3_p9_p14_saved = json.loads(
            (RESULTS / "graded-rank-atlas-a3-p9-p14.json").read_text()
        )
        self.assertEqual(
            json.loads(json.dumps(atlas.atlas(3, list(range(9, 15))))),
            a3_p9_p14_saved,
        )

        representation_spec = importlib.util.spec_from_file_location(
            "paired_long_legs_kernel_representation", KERNEL_REPRESENTATION_PATH
        )
        representation = importlib.util.module_from_spec(representation_spec)
        representation_spec.loader.exec_module(representation)
        inputs = [
            RESULTS / "graded-rank-atlas-a2-p3.json",
            RESULTS / "graded-rank-atlas-a3.json",
            RESULTS / "graded-rank-atlas-a3-p8.json",
            RESULTS / "graded-rank-atlas-a3-p9-p14.json",
        ]
        actual = json.loads(json.dumps(representation.report(inputs)))
        saved = json.loads(
            (RESULTS / "kernel-decomposition-a2-p3-a3-p7-p14.json").read_text()
        )
        self.assertEqual(actual, saved)
        self.assertEqual(
            [(r["a"], r["p"], r["kernel_dimension"]) for r in saved["records"]],
            [
                (2, 3, 10),
                (3, 7, 730),
                (3, 8, 3780),
                (3, 9, 7581),
                (3, 10, 8208),
                (3, 11, 5625),
                (3, 12, 2520),
                (3, 13, 720),
                (3, 14, 120),
            ],
        )
        self.assertEqual(
            [
                (
                    r["p"],
                    r["rank_over_q"],
                    r["domain"],
                    r["kernel_dimension_over_q"],
                )
                for r in a3_p9_p14_saved["records"]
            ],
            [
                (9, 37464, 45045, 7581),
                (10, 18819, 27027, 8208),
                (11, 6660, 12285, 5625),
                (12, 1575, 4095, 2520),
                (13, 225, 945, 720),
                (14, 15, 135, 120),
            ],
        )
        a2_types = [
            (item["highest_weight"], item["multiplicity"])
            for item in saved["records"][0]["irreducibles"]
        ]
        self.assertEqual(a2_types, [([0, 5], 1), ([0, 3], 1)])
        a3_types = {
            (item["highest_weight"][0], item["highest_weight"][1] // 2):
            item["multiplicity"]
            for item in saved["records"][1]["irreducibles"]
        }
        self.assertEqual(
            [a3_types[(0, t)] for t in range(11)],
            [3, 1, 5, 3, 6, 3, 5, 2, 3, 1, 1],
        )
        self.assertEqual(
            [a3_types[(2, t)] for t in range(1, 10)],
            [2, 1, 2, 1, 2, 1, 2, 1, 1],
        )
        a3_p8_types = {
            (item["highest_weight"][0], item["highest_weight"][1] // 2):
            item["multiplicity"]
            for item in saved["records"][2]["irreducibles"]
        }
        self.assertEqual(
            [a3_p8_types[(0, t)] for t in range(11)],
            [2, 3, 7, 7, 9, 7, 7, 4, 3, 1, 1],
        )
        self.assertEqual(
            [a3_p8_types[(2, t)] for t in range(11)],
            [3, 5, 10, 11, 14, 12, 11, 7, 5, 2, 1],
        )
        self.assertEqual(
            [a3_p8_types.get((4, t), 0) for t in range(11)],
            [0, 1, 2, 3, 3, 3, 3, 2, 1, 0, 0],
        )


if __name__ == "__main__":
    unittest.main()

import importlib.util
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


if __name__ == "__main__":
    unittest.main()

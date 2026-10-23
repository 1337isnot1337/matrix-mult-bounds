"""Complete census, endpoint, prerequisite, and scope controls for total202."""

import copy
import gzip
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-leading-rank202/verify.py"
SPEC = importlib.util.spec_from_file_location("leading_rank202_verifier", PATH)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class LeadingRank202Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads(VERIFY.RESULT.read_text())
        cls.census = json.loads(gzip.decompress(VERIFY.CENSUS.read_bytes()))

    def test_complete_exported_pair_and_triple_census(self):
        VERIFY.replay_saved(self.report, self.census)
        counts = self.report["pair_controls"]["counts"]
        self.assertEqual(sum(record["pairs_checked"] for record in counts.values()), 20706)
        self.assertEqual([counts[kind]["newly_excluded"] for kind in ("mixed", "long")], [488, 329])
        triples = self.report["triple_controls"]
        self.assertEqual(triples["triples_checked"], 1050804)
        self.assertEqual((triples["prior_surviving"], triples["new_surviving"], triples["newly_excluded"]),
                         (603885, 541407, 62478))

    def test_strict_thresholds_and_equality_are_preserved(self):
        self.assertEqual([VERIFY.source_dimension_cap(r) for r in (91, 92, 95, 96)],
                         [68, 72, 72, 112])
        at92 = VERIFY.pair_screen(50, 82, "mixed")
        self.assertEqual((at92["source_rank_ceiling"], at92["kernel_lower"], at92["new_kernel_upper"]),
                         (92, 70, 72))
        self.assertFalse(at92["excluded"])
        self.assertTrue(VERIFY.pair_screen(50, 83, "mixed")["excluded"])
        self.assertFalse(VERIFY.pair_screen(100, 28, "mixed")["excluded"])
        self.assertTrue(VERIFY.pair_screen(100, 29, "mixed")["excluded"])
        equality = VERIFY.pair_screen(70, 66, "mixed")
        self.assertEqual(equality["kernel_lower"], equality["new_kernel_upper"])
        self.assertFalse(equality["excluded"])

    def test_complete_mixed_gap_and_both_quotient_constraints(self):
        mixed129 = [VERIFY.pair_screen(a, 129-a, "mixed") for a in range(28, 101)]
        self.assertEqual(len(mixed129), 73)
        self.assertTrue(all(record["excluded"] for record in mixed129))
        self.assertFalse(VERIFY.pair_screen(55, 74, "long")["excluded"])
        for kind, maximum, divisor, dimension in (("mixed", 100, 10, 110), ("long", 101, 11, 100)):
            for a in range(maximum + 1):
                for b in range(102):
                    total = a+b
                    product = (a // divisor) * (b // divisor)
                    formula = total <= 136
                    if 129 <= total <= 132:
                        formula = product >= dimension-72
                    elif 133 <= total <= 136:
                        formula = product >= dimension-68
                    self.assertEqual(not VERIFY.pair_screen(a, b, kind)["excluded"], formula)

    def test_unique_arithmetic_endpoint_and_full_short_rectangle(self):
        triples = self.report["triple_controls"]
        self.assertEqual((triples["maximum_total"], triples["maximizers"]), (202, [[70, 66, 66]]))
        self.assertEqual(triples["full_short"], {"surviving_triples": 841, "long_rank_interval": [0, 28],
                                                "maximum_total": 156, "maximizers": [[100, 28, 28]]})
        self.assertFalse(VERIFY.pair_screen(66, 66, "long")["excluded"])
        self.assertTrue(VERIFY.pair_screen(66, 66, "mixed")["excluded"])
        self.assertFalse(self.report["claim_scope"]["screen_maximizer_is_target_construction"])

    def test_prior136_guard_and_rank_domains_are_retained(self):
        self.assertTrue(VERIFY.pair_screen(100, 100, "mixed")["excluded_by_prior136"])
        self.assertFalse(VERIFY.pair_screen(100, 100, "mixed", use_prior=False)["excluded"])
        for args in ((101, 0, "mixed"), (0, 102, "long"), (True, 0, "mixed"), (-1, 0, "long")):
            with self.assertRaisesRegex(ArithmeticError, "individual bounds"):
                VERIFY.pair_screen(*args)
        with self.assertRaisesRegex(ArithmeticError, "unknown target pair"):
            VERIFY.pair_screen(0, 0, "short")
        with self.assertRaisesRegex(ArithmeticError, "invalid source rank"):
            VERIFY.source_dimension_cap(-1)

    def test_exact_source_versions_and_byte_pins(self):
        document = json.loads((VERIFY.HERE / "sources.json").read_text())
        VERIFY.check_sources(document)
        wrong = copy.deepcopy(document)
        wrong["local_dependencies"][2]["sha256"] = "0"*64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            VERIFY.check_sources(wrong)
        wrong = copy.deepcopy(document)
        wrong["local_dependencies"].pop()
        with self.assertRaisesRegex(ArithmeticError, "source inventory"):
            VERIFY.check_sources(wrong)
        document["source_cap_commit"] = "0"*40
        with self.assertRaisesRegex(ArithmeticError, "version or field"):
            VERIFY.check_sources(document)

    def test_wrong_scope_and_single_census_bit_are_rejected(self):
        for field in ("screen_maximizer_is_target_construction", "target_leading_rank_bounds_sharp",
                      "smaller_exponent_established"):
            wrong = copy.deepcopy(self.report)
            wrong["claim_scope"][field] = True
            with self.assertRaisesRegex(ArithmeticError, "scope"):
                VERIFY.replay_saved(wrong, self.census)
        wrong_census = copy.deepcopy(self.census)
        payload = bytearray.fromhex(wrong_census["triples"]["new_survivors_hex"])
        payload[-1] ^= 1
        wrong_census["triples"]["new_survivors_hex"] = payload.hex()
        with self.assertRaisesRegex(ArithmeticError, "complete census"):
            VERIFY.replay_saved(self.report, wrong_census)


if __name__ == "__main__":
    unittest.main()

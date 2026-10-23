"""Exact source witnesses, inherited censuses, and scope controls for rank91/198."""

import copy
import gzip
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-rank91-core/verify.py"
SPEC = importlib.util.spec_from_file_location("rank91_core_verifier", PATH)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class Rank91CoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificates = json.loads(VERIFY.CERTIFICATES.read_text())
        cls.report = json.loads(VERIFY.RESULT.read_text())
        cls.census = json.loads(gzip.decompress(VERIFY.CENSUS.read_bytes()))

    def test_complete_source_and_target_acceptance(self):
        VERIFY.replay_saved(self.report, self.census)
        source = self.report["source_controls"]
        self.assertEqual((source["integer_minors_replayed"], source["equality_ideals"],
                          source["transpose_basis_identities"], source["transpose_literal_terms"]),
                         (4, 8, 112, 4096))
        self.assertEqual((source["core_dimension"], source["core_rank_lower"]), (56, 91))
        counts = self.report["target_controls"]["pair_counts"]
        self.assertEqual(sum(record["checked"] for record in counts.values()), 20706)
        self.assertEqual([counts[kind]["newly_excluded"] for kind in ("mixed", "long")], [36, 24])
        triples = self.report["target_controls"]["triple_counts"]
        self.assertEqual((triples["checked"], triples["prior202_retained"], triples["retained"],
                          triples["newly_excluded"]), (1050804, 541407, 536157, 5250))
        self.assertEqual((triples["maximum_total"], triples["maximizers"]),
                         (198, [[62, 66, 70], [62, 70, 66]]))

    def test_frozen202_census_is_retained_bit_for_bit(self):
        old_path = ROOT / "results/leading-rank202-2026-10-23/census.json.gz"
        old = json.loads(gzip.decompress(old_path.read_bytes()))
        for kind in ("mixed", "long", "triples"):
            self.assertEqual(self.census[kind]["prior202_survivors_hex"],
                             old[kind]["new_survivors_hex"])
            old_bits = bytes.fromhex(self.census[kind]["prior202_survivors_hex"])
            new_bits = bytes.fromhex(self.census[kind]["survivors_hex"])
            self.assertTrue(all(new_byte & ~old_byte == 0 for old_byte, new_byte in zip(old_bits, new_bits)))

    def test_missing_or_changed_coherent_witness_is_rejected(self):
        missing = copy.deepcopy(self.certificates)
        missing["coherent_pairs"].pop()
        with self.assertRaisesRegex(ArithmeticError, "incomplete coherent"):
            VERIFY.source_controls(missing)
        wrong = copy.deepcopy(self.certificates)
        wrong["coherent_pairs"][2]["coefficient_mask"] = "0x1000"
        with self.assertRaisesRegex(ArithmeticError, "binomial support"):
            VERIFY.source_controls(wrong)
        wrong = copy.deepcopy(self.certificates)
        mask = int(wrong["coherent_pairs"][2]["minor_rows_mask"], 16)
        wrong["coherent_pairs"][2]["minor_rows_mask"] = hex(mask & (mask-1))
        with self.assertRaisesRegex(ArithmeticError, "minor dimensions"):
            VERIFY.source_controls(wrong)

    def test_core_support_shape_and_singular_minor_are_rejected(self):
        wrong = copy.deepcopy(self.certificates)
        wrong["core"]["layers"][5][0] = 3
        with self.assertRaisesRegex(ArithmeticError, "common core"):
            VERIFY.source_controls(wrong)
        wrong = copy.deepcopy(self.certificates)
        outside = VERIFY.SOURCE.index((3, 6, 3))
        wrong["core"]["coefficient_mask"] = hex(int(wrong["core"]["coefficient_mask"], 16) | (1 << outside))
        with self.assertRaisesRegex(ArithmeticError, "support leaves"):
            VERIFY.source_controls(wrong)
        wrong = copy.deepcopy(self.certificates)
        wrong["core"]["coefficient_mask"] = "0x1"
        with self.assertRaisesRegex(ArithmeticError, "singular modulo two"):
            VERIFY.source_controls(wrong)

    def test_strict_threshold_and_unproved_sharpness_stay_distinct(self):
        self.assertEqual([VERIFY.source_cap(rank) for rank in (90, 91, 92, 95, 96)],
                         [67, 68, 72, 72, 112])
        self.assertTrue(self.report["source_controls"]["weak_rank91_cap67_disproved_by_pinned_dimension68_example"])
        scope = self.report["claim_scope"]
        self.assertFalse(scope["source_dimension_cap_claimed_sharp"])
        self.assertFalse(scope["target_bound_claimed_sharp"])
        self.assertFalse(scope["target_constructed"])
        self.assertFalse(scope["improves_omega"])
        self.assertEqual(set(VERIFY.equality_profiles()), set(VERIFY.PROFILES))

    def test_prior_exception_and_changed_endpoint_are_preserved(self):
        self.assertTrue(VERIFY.pair_screen(100, 100, "mixed")["excluded"])
        self.assertFalse(VERIFY.pair_screen(100, 100, "mixed", use_prior=False)["excluded"])
        self.assertFalse(VERIFY.pair_screen(70, 66, "mixed", endpoint=False)["excluded"])
        self.assertTrue(VERIFY.pair_screen(70, 66, "mixed")["excluded"])
        self.assertFalse(VERIFY.pair_screen(100, 28, "mixed")["excluded"])
        self.assertTrue(VERIFY.pair_screen(100, 29, "mixed")["excluded"])
        for a, b, c in ((62, 66, 70), (62, 70, 66)):
            self.assertFalse(VERIFY.pair_screen(a, b, "mixed")["excluded"])
            self.assertFalse(VERIFY.pair_screen(a, c, "mixed")["excluded"])
            self.assertFalse(VERIFY.pair_screen(b, c, "long")["excluded"])

    def test_single_census_bit_or_scope_inflation_is_rejected(self):
        wrong = copy.deepcopy(self.census)
        bits = bytearray.fromhex(wrong["triples"]["survivors_hex"])
        bits[0] ^= 1
        wrong["triples"]["survivors_hex"] = bits.hex()
        with self.assertRaisesRegex(ArithmeticError, "census or scope"):
            VERIFY.replay_saved(self.report, wrong)
        for field in ("source_dimension_cap_claimed_sharp", "target_constructed", "improves_omega"):
            wrong = copy.deepcopy(self.report)
            wrong["claim_scope"][field] = True
            with self.assertRaisesRegex(ArithmeticError, "census or scope"):
                VERIFY.replay_saved(wrong, self.census)

    def test_changed_source_version_inventory_or_digest_is_rejected(self):
        sources = json.loads((VERIFY.HERE / "sources.json").read_text())
        wrong = copy.deepcopy(sources)
        wrong["base_commit"] = "0"*40
        with self.assertRaisesRegex(ArithmeticError, "version or field"):
            VERIFY.check_sources(wrong)
        wrong = copy.deepcopy(sources)
        wrong["local_dependencies"].pop()
        with self.assertRaisesRegex(ArithmeticError, "source inventory"):
            VERIFY.check_sources(wrong)
        wrong = copy.deepcopy(sources)
        wrong["local_dependencies"][0]["sha256"] = "0"*64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            VERIFY.check_sources(wrong)


if __name__ == "__main__":
    unittest.main()

"""Complete seven-case replay and failure controls for every-pair144."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-all-pair-rank144/verify.py"
SPEC = importlib.util.spec_from_file_location("all_pair_rank144", PATH)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class AllPairRank144Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads(verify.CERTIFICATES.read_text())
        cls.slices, cls.entries = verify.literal_source()

    def test_frozen_evidence_replays(self):
        document = json.loads(verify.RESULT.read_text())
        verify.replay_saved(document)
        self.assertEqual(document["compression_controls"]["complete_size10_ideals"], 7)
        self.assertEqual(document["compression_controls"]["forcing_steps"], 96)
        self.assertEqual(document["lowering_controls"]["basis_identities"], 336)

    def test_complete_ideal_inventory_and_two_tori(self):
        expected = ((3, 3, 2, 2), (3, 3, 3, 1), (4, 2, 2, 2),
                    (4, 3, 2, 1), (4, 3, 3, 0), (4, 4, 1, 1), (4, 4, 2, 0))
        self.assertEqual(verify.short_ideals(), expected)
        controls = verify.source_controls(self.slices, self.entries)
        self.assertEqual(controls["second_torus_distinct_weights"],
                         {"parameters": 112, "rows": 112, "columns": 112})
        # The first torus cannot force coordinate auxiliary column limits.
        self.assertEqual(4 + 4 * 0 - 28 * 0, 0 + 4 * 1 - 28 * 0)
        self.assertNotEqual(4 - 16 * 0 - 256 * 0, 0 - 16 * 1 - 256 * 0)
        self.assertEqual(controls["torus_coefficient_identities"], 8192)

    def test_missing_duplicate_and_wrong_budget_certificates_are_rejected(self):
        document = copy.deepcopy(self.certificate)
        document["size10_ideals"].pop()
        with self.assertRaisesRegex(ArithmeticError, "incomplete size10"):
            verify.replay_certificates(document, self.slices)
        document = copy.deepcopy(self.certificate)
        document["size10_ideals"][1] = copy.deepcopy(document["size10_ideals"][0])
        with self.assertRaisesRegex(ArithmeticError, "duplicate ideal"):
            verify.replay_certificates(document, self.slices)
        document = copy.deepcopy(self.certificate)
        document["row_deletion_budget"] = 13
        with self.assertRaisesRegex(ArithmeticError, "certificate header"):
            verify.replay_certificates(document, self.slices)

    def test_invalid_edges_and_repeated_matching_endpoints_are_rejected(self):
        record = copy.deepcopy(self.certificate["size10_ideals"][2])
        record["matching"][1] = record["matching"][0][:]
        with self.assertRaisesRegex(ArithmeticError, "endpoints are not disjoint"):
            verify.replay_record(record, self.slices)
        record = copy.deepcopy(self.certificate["size10_ideals"][0])
        edges = verify.literal_graph(tuple(record["shape"]), self.slices)
        outside = next([r, c] for r in range(28) for c in range(28) if (r, c) not in edges)
        record["matching"][0] = outside
        with self.assertRaisesRegex(ArithmeticError, "absent from the literal"):
            verify.replay_record(record, self.slices)

    def test_false_and_incomplete_forcing_sequences_are_rejected(self):
        record = copy.deepcopy(self.certificate["size10_ideals"][0])
        record["forced_cover"]["steps"].pop()
        with self.assertRaisesRegex(ArithmeticError, "incomplete one-sided"):
            verify.replay_record(record, self.slices)
        record = copy.deepcopy(self.certificate["size10_ideals"][0])
        first = record["forced_cover"]["steps"][0]
        # A matching edge cannot force its own endpoint without a prior choice.
        first["forcing_edge"] = record["matching"][first["matching_index"]][:]
        with self.assertRaisesRegex(ArithmeticError, "no prior unselected"):
            verify.replay_record(record, self.slices)
        record = copy.deepcopy(self.certificate["size10_ideals"][0])
        record["forced_cover"]["steps"][1] = copy.deepcopy(record["forced_cover"]["steps"][0])
        with self.assertRaisesRegex(ArithmeticError, "repeated forcing index"):
            verify.replay_record(record, self.slices)

    def test_exact_pair_screen_and_strict_source_thresholds(self):
        controls = verify.rank_pair_controls()
        self.assertEqual(controls["mixed_rank_pairs_checked"], 10302)
        self.assertEqual(controls["long_rank_pairs_checked"], 10404)
        self.assertEqual(controls["mixed_pairs_above144_excluded"], 1653)
        self.assertEqual(controls["long_pairs_above144_excluded"], 1711)
        self.assertEqual(controls["before_compression_exception"], [[100, 100]])
        self.assertFalse(verify.pair_screen(100, 100, "mixed", use_compression=False)["excluded"])
        self.assertTrue(verify.pair_screen(100, 100, "mixed")["excluded"])
        for ceiling, cap in ((23, 8), (24, 16), (36, 16), (37, 24), (47, 24),
                             (48, 32), (63, 32), (64, 44), (79, 44), (80, 112)):
            self.assertEqual(verify.source_cap(ceiling), cap)
        self.assertFalse(verify.pair_screen(100, 44, "mixed")["excluded"])
        with self.assertRaisesRegex(ArithmeticError, "individually established bounds"):
            verify.pair_screen(90, 110, "mixed")

    def test_source_pins_and_inflated_scope_are_rejected(self):
        document = json.loads((verify.HERE / "sources.json").read_text())
        document["local_dependencies"][2]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            verify.check_sources(document)
        document = json.loads(verify.RESULT.read_text())
        document["claim_scope"]["leading_rank_bounds_sharp"] = True
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)
        document = json.loads(verify.RESULT.read_text())
        document["rank_pair_controls"]["every_pair_sum_upper"] = 143
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)


if __name__ == "__main__":
    unittest.main()

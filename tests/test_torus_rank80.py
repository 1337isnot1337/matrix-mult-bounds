"""Exact replay and failure controls for the A4 rank-80 frontier."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-torus-rank80/verify.py"
SPEC = importlib.util.spec_from_file_location("torus_rank80", PATH)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class TorusRank80Tests(unittest.TestCase):
    def test_frozen_evidence_replays(self):
        document = json.loads(verify.RESULT.read_text())
        verify.replay_saved(document)
        self.assertEqual(document["minor_controls"]["integer_minors_checked"], 35)
        self.assertEqual(document["minor_controls"]["source51_ideals"], 24)
        self.assertEqual(document["source_controls"]["source_basis_factorizations"], 112)

    def test_complete_small_and_large_ideal_inventories(self):
        self.assertEqual(len(verify.short_ideals(9)), 7)
        self.assertEqual(len(verify.short_ideals(13)), 3)
        profiles = verify.layer_controls()["remaining_profiles"]
        self.assertEqual(len(profiles), 3)
        self.assertEqual([item["ideals"] for item in profiles], [8, 8, 8])
        for ideal in verify.remaining_ideals():
            self.assertEqual(sum(map(sum, ideal)), 51)
            self.assertIn(ideal[3], ((4, 0, 0, 0), (1, 1, 1, 1)))

    def test_missing_and_duplicate_certificates_are_rejected(self):
        document = json.loads(verify.CERTIFICATES.read_text())
        document["source51_ideals"].pop()
        with self.assertRaisesRegex(ArithmeticError, "incomplete source51"):
            verify.replay_certificates(document)
        document = json.loads(verify.CERTIFICATES.read_text())
        document["coherent13_ideals"][1] = copy.deepcopy(document["coherent13_ideals"][0])
        with self.assertRaisesRegex(ArithmeticError, "duplicate coherent"):
            verify.replay_certificates(document)
        document = json.loads(verify.CERTIFICATES.read_text())
        document["coherent9_ideals"].pop()
        with self.assertRaisesRegex(ArithmeticError, "incomplete coherent"):
            verify.replay_certificates(document)

    def test_outside_support_and_singular_minors_are_rejected(self):
        document = json.loads(verify.CERTIFICATES.read_text())
        first = document["source51_ideals"][0]
        outside = next(n for n, (i, k, s) in enumerate(verify.SOURCE) if s >= first["shape"][k][i])
        first["coefficient_mask"] = hex(1 << outside)
        with self.assertRaisesRegex(ArithmeticError, "support leaves"):
            verify.replay_certificates(document)
        document = json.loads(verify.CERTIFICATES.read_text())
        document["source51_ideals"][0]["coefficient_mask"] = "0x1"
        with self.assertRaisesRegex(ArithmeticError, "singular modulo two"):
            verify.replay_certificates(document)

    def test_wrong_minor_size_and_modulus_are_rejected(self):
        document = json.loads(verify.CERTIFICATES.read_text())
        pair = document["coherent20_pair"]
        mask = int(pair["minor_rows_mask"], 16)
        pair["minor_rows_mask"] = hex(mask & (mask - 1))
        with self.assertRaisesRegex(ArithmeticError, "wrong dimensions"):
            verify.replay_certificates(document)
        document = json.loads(verify.CERTIFICATES.read_text())
        document["verification_modulus"] = 3
        with self.assertRaisesRegex(ArithmeticError, "certificate header"):
            verify.replay_certificates(document)

    def test_source_pins_and_inventory_are_checked(self):
        document = json.loads((verify.HERE / "sources.json").read_text())
        corrupt = copy.deepcopy(document)
        corrupt["local_dependencies"][2]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            verify.check_sources(corrupt)
        document["local_dependencies"].pop()
        with self.assertRaisesRegex(ArithmeticError, "source inventory"):
            verify.check_sources(document)

    def test_integer_frontier_and_strict_rank80_boundary(self):
        record = verify.rank_pair_controls()
        self.assertEqual(record["rank_pairs_checked"], 12321)
        self.assertEqual(record["excluded_pairs_above_144"], 2926)
        self.assertEqual(record["new_pairs_of_sum_145_through_160"], 1096)
        self.assertEqual(verify.kernel_cap(63), 32)
        self.assertEqual(verify.kernel_cap(64), 50)
        self.assertEqual(verify.kernel_cap(79), 50)
        self.assertEqual(verify.kernel_cap(80), 112)
        self.assertFalse(record["boundary_control"]["excluded"])
        self.assertTrue(record["ordinary_control"]["excluded"])

    def test_inflated_scope_and_changed_budget_are_rejected(self):
        document = json.loads(verify.RESULT.read_text())
        document["claim_scope"]["dimension_bound_sharp"] = True
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)
        document = json.loads(verify.RESULT.read_text())
        document["rank_pair_controls"]["new_range_kernel_upper"] = 51
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)


if __name__ == "__main__":
    unittest.main()

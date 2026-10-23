"""Independent certificate replay and failure controls for the rank-64 frontier."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-torus-order-ideal/verify.py"
SPEC = importlib.util.spec_from_file_location("torus_order_ideal", PATH)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class TorusOrderIdealTests(unittest.TestCase):
    def test_frozen_evidence_replays_with_full_coverage(self):
        document = json.loads(verify.RESULT.read_text())
        verify.replay_saved(document)
        self.assertEqual(document["source_controls"]["literal_terms"], 4096)
        self.assertEqual(document["infinitesimal_controls"]["total_basis_identities"], 336)
        self.assertEqual(document["infinitesimal_controls"]["zero_boundary_identities"], 72)
        self.assertEqual(document["order_ideal_certificates"]["distinct_certificates"], 611)
        self.assertEqual(document["sharpness_control"]["supported_rows"], 56)

    def test_missing_and_duplicate_ideals_are_rejected(self):
        document = json.loads(verify.CERTIFICATES.read_text())
        document["records"].pop()
        with self.assertRaisesRegex(ArithmeticError, "incomplete order-ideal"):
            verify.replay_certificates(document)
        document = json.loads(verify.CERTIFICATES.read_text())
        document["records"][1] = copy.deepcopy(document["records"][0])
        with self.assertRaisesRegex(ArithmeticError, "duplicate ideal"):
            verify.replay_certificates(document)

    def test_support_outside_ideal_and_singular_integer_minor_are_rejected(self):
        document = json.loads(verify.CERTIFICATES.read_text())
        first = document["records"][0]
        outside = next(n for n, (i, k, s) in enumerate(verify.COORDINATES)
                       if s >= first["shape"][k][i])
        first["coefficient_mask"] = hex(1 << outside)
        with self.assertRaisesRegex(ArithmeticError, "support leaves"):
            verify.replay_certificates(document)
        # The smallest coordinate belongs to every nonempty ideal but its
        # source matrix has rank16, so its purported 64-minor must fail.
        document = json.loads(verify.CERTIFICATES.read_text())
        document["records"][0]["coefficient_mask"] = "0x1"
        with self.assertRaisesRegex(ArithmeticError, "singular modulo two"):
            verify.replay_certificates(document)

    def test_invalid_minor_masks_and_changed_field_claim_are_rejected(self):
        document = json.loads(verify.CERTIFICATES.read_text())
        first = document["records"][0]
        mask = int(first["minor_rows_mask"], 16)
        first["minor_rows_mask"] = hex(mask & (mask - 1))
        with self.assertRaisesRegex(ArithmeticError, "64 distinct rows"):
            verify.replay_certificates(document)
        document = json.loads(verify.CERTIFICATES.read_text())
        document["records"][0]["minor_columns_mask"] = hex(1 << 112)
        with self.assertRaisesRegex(ArithmeticError, "out of range"):
            verify.replay_certificates(document)
        document = json.loads(verify.CERTIFICATES.read_text())
        document["verification_modulus"] = 3
        with self.assertRaisesRegex(ArithmeticError, "certificate header"):
            verify.replay_certificates(document)

    def test_source_digest_mutation_and_missing_dependency_are_rejected(self):
        document = json.loads((verify.HERE / "sources.json").read_text())
        corrupt = copy.deepcopy(document)
        corrupt["local_dependencies"][2]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            verify.check_sources(corrupt)
        document["local_dependencies"].pop()
        with self.assertRaisesRegex(ArithmeticError, "source inventory"):
            verify.check_sources(document)

    def test_new_rank_pairs_are_excluded_but_rank64_boundary_is_open(self):
        record = verify.rank_pair_controls()
        self.assertEqual(record["rank_pairs_checked"], 12321)
        self.assertEqual(record["excluded_pairs_above_160"], 1830)
        self.assertEqual(record["new_pairs_of_sum_161_through_176"], 840)
        self.assertEqual(record["new_range_minimum_kernel_lower"], 36)
        self.assertEqual(verify.kernel_cap(47), 24)
        self.assertEqual(verify.kernel_cap(48), 32)
        self.assertEqual(verify.kernel_cap(63), 32)
        self.assertEqual(verify.kernel_cap(64), 112)
        self.assertEqual(record["boundary_control"]["source_defect"], 64)
        self.assertFalse(record["boundary_control"]["excluded"])

    def test_changed_budget_and_inflated_scope_are_rejected(self):
        document = json.loads(verify.RESULT.read_text())
        document["rank_pair_controls"]["new_range_kernel_upper"] = 36
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)
        document = json.loads(verify.RESULT.read_text())
        document["claim_scope"]["long_rank_sum_bound_sharp"] = True
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)

    def test_binary_determinant_and_mask_boundary_controls(self):
        self.assertTrue(verify.invertible_mod2([1, 2, 4], 3))
        self.assertTrue(verify.invertible_mod2([2, 4, 1], 3))
        self.assertFalse(verify.invertible_mod2([1, 1, 4], 3))
        with self.assertRaisesRegex(ArithmeticError, "invalid binary"):
            verify.invertible_mod2([1, 2, 8], 3)
        with self.assertRaisesRegex(ArithmeticError, "noncanonical"):
            verify.parse_mask("0X1", 48)
        with self.assertRaisesRegex(ArithmeticError, "noncanonical"):
            verify.parse_mask("-0x1", 48)


if __name__ == "__main__":
    unittest.main()

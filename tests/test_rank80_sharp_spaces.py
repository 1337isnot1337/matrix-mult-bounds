"""Exact finite coverage and meaningful corruption tests for the sharp cap44."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/ai/2026-10-23-rank80-sharp-spaces/verify.py"
SPEC = importlib.util.spec_from_file_location("rank80_sharp_spaces", PATH)
verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify)


class Rank80SharpSpacesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads(verify.CERTIFICATES.read_text())
        cls.bases = verify.literal_bases()

    def test_frozen_evidence_replays(self):
        document = json.loads(verify.RESULT.read_text())
        verify.replay_saved(document)
        self.assertEqual(document["minor_controls"]["integer_minors_checked"], 1721)
        self.assertEqual(document["minor_controls"]["source45_ideals"], 1709)
        self.assertEqual(document["minor_controls"]["sharpness"]["uniform_rank_upper"], 79)
        self.assertEqual(document["source_controls"]["weak_rank80_boundary"],
                         {"dimension": 56, "supported_columns": 80})

    def test_complete_inventory_has_all_structural_conditions(self):
        ideals = verify.remaining_ideals()
        self.assertEqual(len(ideals), 1709)
        self.assertEqual(len(set(ideals)), 1709)
        for shape in ideals:
            self.assertEqual(sum(map(sum, shape)), 45)
            self.assertLessEqual(sum(shape[2]), 12)
            self.assertFalse(shape[3][0] >= 2 and shape[3][1] >= 1)
            self.assertTrue(all(shape[k][i] >= shape[k + 1][i]
                                for k in range(6) for i in range(4)))
            if sum(shape[5]):
                self.assertLessEqual(sum(shape[1]), 8)
        self.assertEqual(len(verify.short_ideals(9)), 7)
        self.assertEqual(len(verify.short_ideals(13)), 3)

    def test_missing_duplicate_and_invalid_shapes_are_rejected(self):
        document = copy.deepcopy(self.certificate)
        document["source45_ideals"].pop()
        with self.assertRaisesRegex(ArithmeticError, "incomplete source45"):
            verify.replay_certificates(document, self.bases)
        document = copy.deepcopy(self.certificate)
        document["source45_ideals"][1] = copy.deepcopy(document["source45_ideals"][0])
        with self.assertRaisesRegex(ArithmeticError, "duplicate source45"):
            verify.replay_certificates(document, self.bases)
        document = copy.deepcopy(self.certificate)
        document["source45_ideals"][0]["shape"][0][0] = 5
        with self.assertRaisesRegex(ArithmeticError, "invalid or duplicate source45"):
            verify.replay_certificates(document, self.bases)

    def test_outside_support_singular_and_wrong_size_minors_are_rejected(self):
        record = copy.deepcopy(self.certificate["source45_ideals"][0])
        shape = record["shape"]
        allowed = {(i, k, s) for i, k, s in verify.SOURCE if s < shape[k][i]}
        outside = next(n for n, coordinate in enumerate(verify.SOURCE) if coordinate not in allowed)
        record["coefficient_mask"] = hex(1 << outside)
        with self.assertRaisesRegex(ArithmeticError, "support leaves"):
            verify.replay_minor(record, self.bases[1], verify.SOURCE, 112, 80, allowed)
        record["coefficient_mask"] = "0x1"
        with self.assertRaisesRegex(ArithmeticError, "singular modulo two"):
            verify.replay_minor(record, self.bases[1], verify.SOURCE, 112, 80, allowed)
        record = copy.deepcopy(self.certificate["source45_ideals"][0])
        mask = int(record["minor_rows_mask"], 16)
        record["minor_rows_mask"] = hex(mask & (mask - 1))
        with self.assertRaisesRegex(ArithmeticError, "wrong dimensions"):
            verify.replay_minor(record, self.bases[1], verify.SOURCE, 112, 80, allowed)

    def test_sharpness_cover_and_rank_witness_are_checked(self):
        record = copy.deepcopy(self.certificate["sharp44_space"])
        control = verify.sharpness_controls(record, self.bases[1])
        self.assertEqual((control["dimension"], control["cover_rows"], control["cover_columns"]), (44, 35, 44))
        record["cover_rows_mask"] = hex(int(record["cover_rows_mask"], 16) ^ 1)
        with self.assertRaisesRegex(ArithmeticError, "support cover"):
            verify.sharpness_controls(record, self.bases[1])
        record = copy.deepcopy(self.certificate["sharp44_space"])
        record["rank79_minor"]["coefficient_mask"] = "0x1"
        with self.assertRaisesRegex(ArithmeticError, "singular modulo two"):
            verify.sharpness_controls(record, self.bases[1])
        # A single extra source coordinate escapes this fixed79-vertex cover.
        record = self.certificate["sharp44_space"]
        rows = set(verify.indices(int(record["cover_rows_mask"], 16), 112))
        columns = set(verify.indices(int(record["cover_columns_mask"], 16), 112))
        self.assertTrue(any(r not in rows and c not in columns for r, c in self.bases[1][3, 2, 0]))

    def test_source_pins_modulus_and_scope_are_enforced(self):
        document = json.loads((verify.HERE / "sources.json").read_text())
        document["local_dependencies"][2]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ArithmeticError, "digest mismatch"):
            verify.check_sources(document)
        document = copy.deepcopy(self.certificate)
        document["verification_modulus"] = 3
        with self.assertRaisesRegex(ArithmeticError, "certificate header"):
            verify.replay_certificates(document, self.bases)
        document = json.loads(verify.RESULT.read_text())
        document["claim_scope"]["target_rank_pair_application"] = True
        with self.assertRaisesRegex(ArithmeticError, "evidence or scope"):
            verify.replay_saved(document)


if __name__ == "__main__":
    unittest.main()

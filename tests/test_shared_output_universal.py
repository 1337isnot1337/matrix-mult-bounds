"""Pin integrity and exact arithmetic for the universal-identification addendum.

These controls check immutable evidence and the finite rank accounting.  The
all-parameter kernel bounds are justified by the written algebraic proof, not
by this test or by sampling first-leg identifications.
"""
from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = Path("research/ai/2026-10-23-shared-output-koszul")
RESULTS = Path("results/shared-output-koszul-2026-10-23")


def read_json(path):
    return json.loads((ROOT / path).read_text())


class SharedOutputUniversalTests(unittest.TestCase):
    def test_universal_manifest_pin_integrity(self):
        manifest = read_json(PACKAGE / "universal_manifest.json")
        expected_paths = {
            str(PACKAGE / "universal_identifications.md"),
            str(PACKAGE / "claims_universal.json"),
            str(PACKAGE / "manifest.json"),
            str(RESULTS / "universal_arithmetic.json"),
        }
        self.assertEqual(set(manifest["files"]), expected_paths)
        for path, expected_digest in manifest["files"].items():
            with self.subTest(path=path):
                self.assertRegex(expected_digest, r"^[0-9a-f]{64}$")
                actual_digest = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
                self.assertEqual(actual_digest, expected_digest)
        self.assertEqual(
            manifest["canonical_checkpoint_manifest_sha256"],
            manifest["files"][str(PACKAGE / "manifest.json")],
        )

    def test_universal_arithmetic_and_canonical_sharpness(self):
        report = read_json(RESULTS / "universal_arithmetic.json")
        certificate = read_json(RESULTS / "certificate.json")
        canonical = read_json(RESULTS / "verification.json")
        target = ["E3"] * 10 + ["E2"] + ["O"] * 2
        dimensions = {"E3": (3, 7), "E2": (2, 6), "O": (4, 2)}
        counts = Counter("/".join(pair) for pair in combinations(target, 2))
        bounds = report["pair_bounds"]
        self.assertEqual(len(bounds), len(counts))
        self.assertEqual({row["pair"] for row in bounds}, set(counts))

        total = sum(certificate["intrinsic/" + name]["rank"] for name in target)
        self.assertEqual(report["target_intrinsic_rank"], total)
        self.assertEqual(total, canonical["target"]["intrinsic_rank"])
        for row in bounds:
            with self.subTest(pair=row["pair"]):
                left, right = row["pair"].split("/")
                b, c = dimensions[left]
                d, e = dimensions[right]
                domain = c * d + e * b
                self.assertEqual(row["domain_dimension"], domain)
                self.assertEqual(row["count"], counts[row["pair"]])
                self.assertIsInstance(row["kernel_upper_bound"], int)
                self.assertGreaterEqual(row["kernel_upper_bound"], 0)
                self.assertLessEqual(row["kernel_upper_bound"], domain)
                lower_bound = domain - row["kernel_upper_bound"]
                self.assertEqual(row["rank_lower_bound"], lower_bound)
                sharp = certificate["cross/" + row["pair"]]
                self.assertEqual(sharp["columns"], domain)
                self.assertEqual(sharp["rank"], lower_bound)
                total += counts[row["pair"]] * lower_bound

        source = canonical["source"]["koszul_rank"]
        self.assertEqual(report["source_rank"], source)
        self.assertEqual(report["target_rank_lower_bound"], total)
        self.assertEqual(report["rank_gap_lower_bound"], total - source)
        self.assertGreater(total, source)
        self.assertEqual((source, total, total - source), (2595, 2616, 21))
        self.assertEqual(report["proof"], str(PACKAGE / "universal_identifications.md"))
        self.assertEqual(report["claim_status"], "proof-written-unreviewed")
        self.assertFalse(report["new_exponent_established"])


if __name__ == "__main__":
    unittest.main()

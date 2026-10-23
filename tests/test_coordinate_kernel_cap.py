"""Original-source reconstruction, complete matching coverage and corrupted witnesses."""
import copy
import gzip
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-coordinate-kernel-cap"
SPEC = importlib.util.spec_from_file_location("coordinate_kernel_cap", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class CoordinateKernelCapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = json.loads(gzip.decompress(v.CERTIFICATE.read_bytes()))
        cls.summary = json.loads((v.RESULT / "verification.json").read_text())

    def test_all_exported_matchings_and_original_source_replay(self):
        actual = v.verify()
        self.assertEqual(actual["matching_census"], {
            "matching_25": 7744, "unique_left_24": 132, "unique_right_24": 132})
        self.assertEqual(actual["source_control"]["original_source_terms"], 4096)
        self.assertTrue(actual["source_control"]["endpoint_reversal"])

    def test_reject_missing_or_repeated_ten_subset(self):
        for change in (lambda x: x["witnesses"].pop(),
                       lambda x: x["witnesses"].__setitem__(1, x["witnesses"][0])):
            bad = copy.deepcopy(self.certificate)
            change(bad)
            with self.assertRaises(ValueError):
                v.check_certificate(bad)

    def test_reject_duplicate_matching_vertex_and_nonunique_cover(self):
        entry = next(e for e in self.certificate["witnesses"] if len(e["matching"]) == 25)
        bad = copy.deepcopy(entry["matching"])
        bad[1] = bad[0]
        with self.assertRaises(ValueError):
            v.check_witness(entry["cells"], bad)
        # A valid24-edge submatching of a25-edge witness cannot certify a
        # unique size24 cover. This checks the extra implication argument.
        with self.assertRaises(ValueError):
            v.check_witness(entry["cells"], entry["matching"][:24])

    def test_reject_altered_sources_or_certificate_digest(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for change in (lambda x: x["local_dependencies"][0].update(sha256="0"*64),
                       lambda x: x["local_dependencies"].pop(),
                       lambda x: x.update(certificate_sha256="0"*64)):
            bad = copy.deepcopy(original)
            change(bad)
            with self.assertRaises(ValueError):
                v.check_sources(bad)

    def test_reject_inflated_review_or_exponent_claim(self):
        for field in ("independent_review", "improves_omega", "target_constructed"):
            bad = copy.deepcopy(self.summary)
            bad[field] = True
            with self.assertRaises(ValueError):
                v.verify(bad)


if __name__ == "__main__":
    unittest.main()

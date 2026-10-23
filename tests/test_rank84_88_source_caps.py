"""Complete ideal/minor replay, strict thresholds and evidence-corruption rejection."""
import copy
import gzip
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-rank84-88-source-caps"
SPEC = importlib.util.spec_from_file_location("rank84_88_acceptance", PACKAGE / "verify.py")
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


class Rank84And88SourceCapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source, cls.coherent = v.literal_bases()
        cls.documents = {rank: json.loads(gzip.decompress(
            (v.RESULT / f"rank{rank}-minors.json.gz").read_bytes())) for rank in v.CASES}
        cls.record = json.loads((v.RESULT / "verification.json").read_text())

    def test_all_literal_source_ideals_and_odd_minors_replay(self):
        record = v.verify()
        self.assertEqual([x["source_ideals"] for x in record["source_caps"]], [1404, 118])
        self.assertEqual([x["dimension_cap"] for x in record["source_caps"]], [56, 60])
        self.assertEqual(record["target_controls"]["excluded_pairs"], 644)

    def test_sharp_spaces_and_unrealized136_boundary_are_kept_distinct(self):
        controls = self.record["staircase_controls"]
        self.assertEqual([(x["dimension"], x["uniform_rank_upper"]) for x in controls],
                         [(56, 80), (60, 84), (64, 88)])
        boundary = self.record["target_controls"]["boundary_control"]
        self.assertEqual(boundary["required_kernel_dimension"], boundary["kernel_dimension"])
        self.assertEqual(boundary["rank_upper"], boundary["rank_budget"])
        self.assertFalse(boundary["realized_compression_kernel"])
        self.assertFalse(boundary["target_constructed"])

    def test_reject_missing_or_duplicated_source_ideal(self):
        for change in (lambda d: d["source_minors"].pop(),
                       lambda d: d["source_minors"].__setitem__(1, d["source_minors"][0])):
            bad = copy.deepcopy(self.documents[88])
            change(bad)
            with self.assertRaises(ValueError):
                v.verify_document(bad, self.source, self.coherent)

    def test_reject_corrupted_minor_and_changed_strict_threshold(self):
        for change in (lambda d: d["source_minors"][0].update(coefficient_mask="0x0"),
                       lambda d: d["coherent_minors"][-1].update(rank_lower=29),
                       lambda d: d.update(threshold=89)):
            bad = copy.deepcopy(self.documents[88])
            change(bad)
            with self.assertRaises(ValueError):
                v.verify_document(bad, self.source, self.coherent)

    def test_reject_changed_sources_and_artifact_digest(self):
        original = json.loads((PACKAGE / "sources.json").read_text())
        for change in (lambda d: d["local_dependencies"][0].update(sha256="0"*64),
                       lambda d: d["local_dependencies"].pop(),
                       lambda d: d["certificates"].update({"84": "0"*64})):
            bad = copy.deepcopy(original)
            change(bad)
            with self.assertRaises(ValueError):
                v.check_sources(bad)

    def test_reject_a_claim_that_the_boundary_space_is_an_actual_kernel(self):
        bad = copy.deepcopy(self.record)
        bad["target_controls"]["boundary_control"]["realized_compression_kernel"] = True
        with self.assertRaises(ValueError):
            v.verify(bad)


if __name__ == "__main__":
    unittest.main()

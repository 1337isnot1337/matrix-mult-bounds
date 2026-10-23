"""Replay the separate internal audit without importing the reviewed package."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/reviews/2026-10-23-divisor-source-caps"
SPEC = importlib.util.spec_from_file_location("divisor_cap_review", PACKAGE / "audit.py")
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class DivisorCapReviewTests(unittest.TestCase):
    def test_independent_literal_matrix_controls(self):
        saved = ROOT / "results/divisor-source-cap-review-2026-10-23/controls.json"
        self.assertEqual(audit.audit(), json.loads(saved.read_text()))

    def test_reviewed_dependency_bytes(self):
        sources = json.loads((PACKAGE / "sources.json").read_text())
        for entry in sources["local_dependencies"]:
            with self.subTest(path=entry["path"]):
                self.assertEqual(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest(),
                                 entry["sha256"])


if __name__ == "__main__":
    unittest.main()

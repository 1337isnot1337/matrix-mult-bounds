"""Verify the immutable checkpoint without freezing live project files."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "research/ai/2026-10-20-session2/manifest.json"
# Recorded at e0d7ed5c9d614adaca7fb93a7b3f04e899cf5cac. The manifest also
# contains snapshots of live files, such as STATUS.md; those may evolve.
MANIFEST_SHA256 = "bc95c70c4bb3de7e271f52b51902ad4d9d8a77e314af59627f93964ca25e4063"
ARCHIVE_PREFIXES = (
    "research/ai/2026-10-20-session2/",
    "results/session2-2026-10-20/",
)
ARCHIVE_FILES = {
    "research/ai/2026-10-20-session2/README.md",
    "research/ai/2026-10-20-session2/claims.json",
    "research/ai/2026-10-20-session2/dimension_search.py",
    "research/ai/2026-10-20-session2/drafts/strong_scoring_fragment.py.txt",
    "research/ai/2026-10-20-session2/research_note.md",
    "research/ai/2026-10-20-session2/tensor_checks.py",
    "results/session2-2026-10-20/dimension_search.json.gz",
    "results/session2-2026-10-20/tensor_checks.json",
    "results/session2-2026-10-20/tests.initial_failure.txt",
    "results/session2-2026-10-20/tests.txt",
    "results/session2-2026-10-20/verification.json",
}


class ArchiveIntegrityTests(unittest.TestCase):
    def test_session2_manifest_unchanged(self):
        self.assertEqual(hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
                         MANIFEST_SHA256)

    def test_session2_manifest_covers_all_archived_files(self):
        entries = json.loads(MANIFEST.read_text(encoding="utf-8"))["files"]
        archived = {name for name in entries if name.startswith(ARCHIVE_PREFIXES)}
        self.assertEqual(archived, ARCHIVE_FILES)

    def test_session2_archive_hashes(self):
        entries = json.loads(MANIFEST.read_text(encoding="utf-8"))["files"]
        for name in sorted(ARCHIVE_FILES):
            with self.subTest(path=name):
                path = ROOT / name
                self.assertFalse(path.is_symlink(), "Archive members must be regular files")
                self.assertTrue(path.is_file(), "Missing archived file")
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),
                                 entries[name]["sha256"])


if __name__ == "__main__":
    unittest.main()

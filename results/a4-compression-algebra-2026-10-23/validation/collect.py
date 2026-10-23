"""Record unchanged baseline evidence and fresh checks on the proof checkpoint."""

from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import unittest


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent
PACKAGE = ROOT / "research/ai/2026-10-23-a4-compression-algebra"
BASELINE = "6db05f5592b2f252ebc718cfececd5625a44aed5"
CHECKPOINT_TREE = "bd724a8d4b805a1d7334279289cb5aa181573e19"
PRIOR = ROOT / "results/conjugation-limit-2026-10-23"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*arguments):
    return subprocess.check_output(["git", *arguments], cwd=ROOT, text=True).strip()


def test_ids(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from test_ids(item)
        else:
            yield item.id()


def main():
    started = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    require(tree == CHECKPOINT_TREE, "this collector is for the frozen theorem checkpoint")
    baseline = json.loads((PRIOR / "validation.json").read_text())
    plan = json.loads((PRIOR / "validation/plan.json").read_text())
    require(baseline["tested_local_commit"] == BASELINE
            and baseline["full_regression"]["final_passed_tests_after_scratch_correction"] == 905,
            "wrong retained baseline")
    for filename, digest in baseline["artifact_sha256"].items():
        require(sha(PRIOR / "validation" / filename) == digest,
                "retained baseline artifact changed: " + filename)
    completed = list(plan["prefix_passed_ids"])
    for index in range(3):
        shard = json.loads((PRIOR / "validation" / f"shard-{index}.json").read_text())
        completed.extend(shard["completed_ids"])
    require(len(completed) == len(set(completed)) == 905
            and set(completed) == set(plan["expected_ids"]), "retained baseline coverage is incomplete")

    entries = []
    archive_entries = []
    changed = []
    for record in git("ls-tree", "-r", BASELINE).splitlines():
        metadata, filename = record.split("\t", 1)
        object_id = metadata.split()[2]
        path = ROOT / filename
        if not path.exists():
            changed.append(filename)
            continue
        data = path.read_bytes()
        current = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if current != object_id:
            changed.append(filename)
        if filename.endswith(".py"):
            require(current == object_id, "baseline Python source changed: " + filename)
            entries.append([filename, sha(path)])
        if (filename.startswith("research/ai/2026-10-20/")
                or filename.startswith("research/ai/2026-10-20-session2/")
                or filename in ("requirements.txt", "tools/replay.py")):
            require(current == object_id, "archive replay input changed: " + filename)
            archive_entries.append([filename, sha(path)])
    allowed_changes = {"PROVENANCE.md", "STATUS.md", "docs/research_directions.md", "research/ACTIVE.md",
                       "research/claims.json", "research/ai/2026-10-23-conjugation-limit/README.md",
                       "research/ai/2026-10-23-conjugation-limit/sources.json"}
    require(set(changed) == allowed_changes, "unexpected baseline non-Python changes")
    for name, field in [("block-validation.json", "tested_file_sha256"),
                        ("escape-validation.json", "file_sha256")]:
        receipt = json.loads((PRIOR / name).read_text())
        for filename, digest in receipt[field].items():
            require(sha(ROOT / filename) == digest, "prior continuation input changed: " + filename)

    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
    current_ids = sorted(test_ids(suite))
    require(len(current_ids) == len(set(current_ids)), "duplicate current test identifiers")
    added = sorted(set(current_ids) - set(plan["expected_ids"]))
    require(not (set(plan["expected_ids"]) - set(current_ids)), "a baseline test disappeared")
    new_ids = [x for x in added if x.startswith("test_a4_arbitrary_compression.")]
    prior_delta = [x for x in added if x.startswith("test_conjugation_block_reduction.")]
    require(len(new_ids) == 8 and len(prior_delta) == 3 and len(added) == 11,
            "unexpected test delta from the retained905-case baseline")

    environment = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1")
    jobs = [
        ("acceptance.log", [sys.executable, str(PACKAGE / "verify.py")]),
        ("focused-tests.log", [sys.executable, "-m", "unittest", "discover", "-s", "tests",
                               "-p", "test_a4_arbitrary_compression.py", "-v"]),
        ("repository-tests.log", [sys.executable, "-m", "unittest", "discover", "-s", "tests",
                                  "-p", "test_research.py", "-v"]),
    ]
    checks = []
    for filename, command in jobs:
        before = time.monotonic()
        result = subprocess.run(command, cwd=ROOT, env=environment, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (HERE / filename).write_text(result.stdout)
        require(result.returncode == 0, "fresh validation failed: " + filename)
        checks.append({"command": command, "exit_code": result.returncode,
                       "seconds": round(time.monotonic()-before, 3), "log": filename,
                       "log_sha256": sha(HERE / filename)})
    require(json.loads((HERE / "acceptance.log").read_text())
            == json.loads((RESULTS / "verification.json").read_text()), "accepted report changed")
    require(git("rev-parse", "HEAD") == started and git("rev-parse", "HEAD^{tree}") == tree,
            "the frozen checkpoint changed during validation")
    receipt = {
        "schema": "a4-arbitrary-compression-validation-v1",
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0], "tested_local_commit": started, "tested_tree": tree,
        "tree_and_head_unchanged_during_validation": True,
        "method": "retained full baseline plus exact unchanged-byte checks and fresh delta; not a fresh full-suite run",
        "baseline": {"receipt": "results/conjugation-limit-2026-10-23/validation.json",
                     "receipt_sha256": sha(PRIOR / "validation.json"),
                     "tested_local_commit": BASELINE, "tested_tree": baseline["tested_tree"],
                     "completed_tests": 905, "initial_failures": baseline["full_regression"]["initial_failed_test_ids"],
                     "final_unresolved_failures": [], "retained_artifacts_hash_verified": len(baseline["artifact_sha256"]),
                     "exact_disjoint_coverage_rechecked": True,
                     "unchanged_python_files": len(entries), "unchanged_archive_replay_inputs": len(archive_entries),
                     "changed_non_python_files": sorted(changed)},
        "prior_delta_receipts": [{"path": "results/conjugation-limit-2026-10-23/" + name,
                                  "sha256": sha(PRIOR / name)}
                                 for name in ["block-validation.json", "escape-validation.json"]],
        "prior_delta_test_ids": prior_delta, "new_test_ids": new_ids,
        "current_discovered_test_ids": current_ids, "current_discovered_tests": len(current_ids),
        "fresh_focused_tests_passed": 8, "fresh_repository_checks_passed": 18,
        "fresh_checks": checks,
        "archive_replay": {"repeated": False, "all_five_previously_passed": True,
                           "baseline_receipt": "results/conjugation-limit-2026-10-23/validation.json",
                           "archive_and_replay_source_bytes_verified_unchanged": True},
        "unchanged_python_manifest": entries, "unchanged_archive_replay_manifest": archive_entries,
        "tested_file_sha256": {str(path.relative_to(ROOT)): sha(path)
                               for path in [*sorted(PACKAGE.glob("*")),
                                            ROOT / "tests/test_a4_arbitrary_compression.py",
                                            RESULTS / "certificate.json", RESULTS / "verification.json"]
                               if path.is_file()},
        "review_status": "written and unreviewed; proof checks within the generating session are not independent review",
        "fresh_complete_hosted_CI_required_before_merge": True,
    }
    (RESULTS / "validation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"accepted": True, "current_tests": len(current_ids), "baseline_tests": 905,
                      "prior_delta_tests": len(prior_delta), "new_focused_tests": len(new_ids),
                      "repository_checks": 18, "unchanged_python_files": len(entries),
                      "unchanged_archive_replay_inputs": len(archive_entries)}, indent=2))


if __name__ == "__main__":
    main()

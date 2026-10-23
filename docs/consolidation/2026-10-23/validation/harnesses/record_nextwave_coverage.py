"""Extend the preserved 1,933-test coverage with the five reviewed packages.

This local evidence harness never writes into the tested worktree and never
replaces a previous receipt. Inventory imports the reviewed unittest modules;
it does not execute optional discovery or a source branch's historical harness.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import run_full_validation as evidence


BASE = Path(__file__).resolve().parent
BASELINE = "a764cf16c5f453709aa29bfafa1314c103f3d516"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def active_code(path):
    return (not path.startswith("docs/consolidation/") and (
        path.endswith((".py", ".lean", ".sh", ".toml", ".lock"))
        or path.startswith(("tests/", ".github/workflows/"))
        or Path(path).name in {"requirements.txt", "lean-toolchain"}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--repo", type=Path, default=BASE / "nextwave_repo")
    parser.add_argument("--log-dir", type=Path, default=BASE / "test_logs/nextwave")
    args = parser.parse_args()
    logs = args.log_dir.resolve()
    summary_path = logs / "summary.json"
    summary = json.loads(summary_path.read_text())
    if not summary["passed"] or summary["head"] != args.expected_head:
        parser.error("Require a passing focused gate at this exact frozen head")
    if any((logs / name).exists() for name in ("discovery.json", "coverage_union.json")):
        parser.error("Existing coverage receipts are immutable")
    evidence.REPO = args.repo.resolve()
    before = evidence.snapshot()
    if before["head"] != args.expected_head or before["status"]:
        parser.error("The tested head and tracked worktree must remain unchanged")
    old_inventory_path = BASE / "test_logs/postvalidation_catchup/discovery.json"
    old_union_path = BASE / "test_logs/postvalidation_catchup/coverage_union.json"
    closure_path = BASE / "test_logs/closure_final/equivalence.json"
    old_inventory = json.loads(old_inventory_path.read_text())
    old_union = json.loads(old_union_path.read_text())
    closure = json.loads(closure_path.read_text())
    if not old_union["passed"] or not closure["passed"]:
        parser.error("Require the preserved passing prior coverage/equivalence receipts")
    expected_files = json.loads((BASE / "nextwave_previous_validation_hashes.json").read_text())
    changed_prior = [name for name, sha in expected_files.items()
                     if not Path(name).is_file() or digest(Path(name)) != sha]
    if changed_prior:
        parser.error("Prior validation evidence changed: " + repr(changed_prior))
    source_static = json.loads((BASE / "nextwave_code_static.json").read_text())
    expected_added = {
        Path(item["path"]).stem + "." + test
        for item in source_static if item["path"].startswith("tests/")
        for test in item.get("test_ids", [])
    }
    if len(expected_added) != 17:
        parser.error("The reviewed source inventory must contain exactly 17 new tests")
    evidence.write_json(logs / "inventory_tree_before.json", before)
    env = os.environ.copy()
    env.update(PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0",
               OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
    command = [sys.executable, "tools/test_shard.py", "--list"]
    started = time.monotonic()
    with (logs / "discovery.log").open("w") as output, (logs / "discovery.stderr.log").open("w") as error:
        process = subprocess.Popen(command, cwd=evidence.REPO, env=env,
                                   stdout=output, stderr=error)
        print(f"Listing reviewed test inventory at {args.expected_head}", flush=True)
        last_status = started
        while process.poll() is None:
            if time.monotonic() - last_status >= 30:
                print(f"Inventory imports in progress: {time.monotonic()-started:.0f}s", flush=True)
                last_status = time.monotonic()
            time.sleep(1)
    if process.returncode:
        raise RuntimeError("List-only discovery failed; inspect the new discovery stderr log")
    discovery = json.loads((logs / "discovery.log").read_text())
    evidence.write_json(logs / "discovery.json", discovery)
    after = evidence.snapshot()
    evidence.write_json(logs / "inventory_tree_after.json", after)
    previous = set(old_inventory["test_ids"])
    current = set(discovery["test_ids"])
    selected = {test for job in summary["jobs"] if job["kind"] == "unittest"
                for test in job["printed_test_ids"]}
    added, removed = current - previous, previous - current
    tracked_changes = sorted(path for path in set(before["file_sha256"]) | set(after["file_sha256"])
                             if before["file_sha256"].get(path) != after["file_sha256"].get(path))
    previous_paths = git(evidence.REPO, "ls-tree", "-r", "--name-only", BASELINE).decode().splitlines()
    code_paths = [path for path in previous_paths if active_code(path)]
    changed_existing_code = []
    for path in code_paths:
        old_entry = git(evidence.REPO, "ls-tree", BASELINE, "--", path)
        new_entry = git(evidence.REPO, "ls-tree", args.expected_head, "--", path)
        if old_entry != new_entry:
            changed_existing_code.append(path)
    changed_prior = [name for name, sha in expected_files.items()
                     if not Path(name).is_file() or digest(Path(name)) != sha]
    paths = (old_inventory_path, old_union_path, closure_path, summary_path,
             BASE / "nextwave_code_audit.json", BASE / "nextwave_previous_validation_hashes.json")
    receipt = {
        "schema": "matrix-mult-bounds-nextwave-additive-coverage-v1",
        "recorded_at": evidence.utc_now(),
        "head": before["head"],
        "head_tree": before["head_tree"],
        "published_baseline": BASELINE,
        "discovery_command": command,
        "discovery_elapsed_seconds": round(time.monotonic() - started, 3),
        "previous_inventory": {"tests": len(previous), "modules": old_inventory["total_modules"]},
        "final_inventory": {"tests": len(current), "modules": discovery["total_modules"]},
        "tests_added": sorted(added),
        "tests_removed": sorted(removed),
        "expected_new_source_test_ids": sorted(expected_added),
        "added_tests_match_reviewed_source_inventory": added == expected_added,
        "focused_tests_passed": len(selected),
        "new_tests_covered": sorted(added & selected),
        "new_tests_without_focused_coverage": sorted(added - selected),
        "focused_ids_outside_final_inventory": sorted(selected - current),
        "composite_passing_ids": len(previous | selected),
        "composite_exactly_covers_final_inventory": previous | selected == current,
        "existing_code_and_config_paths_compared": len(code_paths),
        "changed_existing_code_or_config": changed_existing_code,
        "tracked_files_changed_during_inventory": tracked_changes,
        "frozen_head_unchanged": before["head"] == after["head"],
        "clean_tracked_status_after": not after["status"],
        "archive_unchanged": before["archive_sha256"] == after["archive_sha256"],
        "archive_files_hashed": len(before["archive_sha256"]),
        "prior_validation_files_checked": len(expected_files),
        "changed_prior_validation_files": changed_prior,
        "source_receipts": [{"path": str(path), "sha256": digest(path)} for path in paths],
        "scope_caveat": (
            "This adds 17 newly executed tests to the prior 1,933-test composite, which derives "
            "from the 1,916-test full baseline, 29 repair/late focused tests, and 33 subsequent "
            "catch-up tests plus two closure metadata checks. The final complete suite was "
            "listed, not freshly executed locally at this commit. Hosted full Python-matrix, "
            "archive-replay and Lean CI remains the merge gate. Finite computation does not "
            "promote mathematical claim review status."
        ),
    }
    receipt["passed"] = (
        len(previous) == 1933 and old_inventory["total_modules"] == 432
        and len(current) == 1950 and discovery["total_modules"] == 437
        and len(selected) == 28 and added == expected_added and not removed
        and not (added - selected) and not (selected - current)
        and previous | selected == current
        and len(discovery["test_ids"]) == len(current) == discovery["total_tests"]
        and not changed_existing_code and not tracked_changes and not changed_prior
        and receipt["frozen_head_unchanged"] and receipt["clean_tracked_status_after"]
        and receipt["archive_unchanged"]
    )
    evidence.write_json(logs / "coverage_union.json", receipt)
    print(json.dumps({key: receipt[key] for key in (
        "passed", "final_inventory", "focused_tests_passed", "tests_added", "tests_removed",
        "new_tests_without_focused_coverage", "composite_exactly_covers_final_inventory",
        "changed_existing_code_or_config", "changed_prior_validation_files")}), flush=True)
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

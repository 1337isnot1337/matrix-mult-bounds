"""Record an additive coverage receipt after successful frozen catch-up checks."""
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--repo", type=Path, default=BASE / "catchup_repo")
    parser.add_argument("--log-dir", type=Path, default=BASE / "test_logs/postvalidation_catchup")
    args = parser.parse_args()
    logs = args.log_dir.resolve()
    summary_path = logs / "summary.json"
    summary = json.loads(summary_path.read_text())
    if not summary["passed"] or summary["head"] != args.expected_head:
        parser.error("A successful focused receipt at the declared frozen commit is required")
    if (logs / "discovery.json").exists() or (logs / "coverage_union.json").exists():
        parser.error("Do not replace existing coverage evidence")
    evidence.REPO = args.repo.resolve()
    before = evidence.snapshot()
    if before["head"] != args.expected_head or before["status"]:
        parser.error("Keep the tested commit and tracked worktree unchanged")
    evidence.write_json(logs / "inventory_tree_before.json", before)
    env = os.environ.copy()
    env.update(PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0",
               OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
    command = [sys.executable, "tools/test_shard.py", "--list"]
    started = time.monotonic()
    with (logs / "discovery.log").open("w") as output, (logs / "discovery.stderr.log").open("w") as error:
        process = subprocess.Popen(command, cwd=evidence.REPO, env=env,
                                   stdout=output, stderr=error)
        print(f"Recording list-only final inventory at {args.expected_head}", flush=True)
        last_status = started
        while process.poll() is None:
            if time.monotonic() - last_status >= 30:
                print(f"Inventory imports in progress: {time.monotonic()-started:.0f}s", flush=True)
                last_status = time.monotonic()
            time.sleep(1)
    if process.returncode:
        raise RuntimeError(f"List-only discovery failed; inspect {logs / 'discovery.stderr.log'}")
    discovery = json.loads((logs / "discovery.log").read_text())
    evidence.write_json(logs / "discovery.json", discovery)
    after = evidence.snapshot()
    evidence.write_json(logs / "inventory_tree_after.json", after)
    old_inventory_path = BASE / "test_logs/final_focused/discovery.json"
    old_union_path = BASE / "test_logs/coverage_union.json"
    old_inventory = json.loads(old_inventory_path.read_text())
    previous = set(old_inventory["test_ids"])
    current = set(discovery["test_ids"])
    selected = {test_id for row in summary["jobs"] if row["kind"] == "unittest"
                for test_id in row["printed_test_ids"]}
    added, removed = current - previous, previous - current
    changed = sorted(path for path in set(before["file_sha256"]) | set(after["file_sha256"])
                     if before["file_sha256"].get(path) != after["file_sha256"].get(path))
    receipt = {
        "schema": "matrix-mult-bounds-additive-validation-coverage-v1",
        "recorded_at": evidence.utc_now(),
        "head": before["head"],
        "head_tree": before["head_tree"],
        "discovery_command": command,
        "discovery_elapsed_seconds": round(time.monotonic() - started, 3),
        "previous_inventory": {"tests": len(previous), "modules": old_inventory["total_modules"]},
        "final_inventory": {"tests": len(current), "modules": discovery["total_modules"]},
        "tests_added": sorted(added),
        "tests_removed": sorted(removed),
        "focused_tests_passed": len(selected),
        "new_tests_covered": sorted(added & selected),
        "new_tests_without_focused_coverage": sorted(added - selected),
        "focused_ids_outside_final_inventory": sorted(selected - current),
        "composite_passing_ids": len(previous | selected),
        "composite_exactly_covers_final_inventory": previous | selected == current,
        "direct_verifiers_passed": [row["name"] for row in summary["jobs"]
                                    if row["kind"] == "json_verifier" and row["status"] == "passed"],
        "tracked_files_changed_during_inventory": changed,
        "frozen_head_unchanged": before["head"] == after["head"],
        "clean_tracked_status_after": not after["status"],
        "archive_unchanged": before["archive_sha256"] == after["archive_sha256"],
        "source_receipts": [
            {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            for path in (old_union_path, old_inventory_path, summary_path)
        ],
        "scope_caveat": (
            "This receipt extends the earlier composite of a full 1,916-test baseline at caf51fe "
            "and 29 focused tests at e2baf117 with the reviewed catch-up acceptance checks. "
            "The final complete suite was listed but not freshly executed locally at this commit. "
            "Hosted full CI, including the Python matrix, replay lane, and Lean build, remains "
            "the merge gate. Finite computational checks do not promote mathematical claim status."
        ),
    }
    receipt["passed"] = (not removed and not (added - selected) and not (selected - current)
                         and receipt["composite_exactly_covers_final_inventory"]
                         and len(discovery["test_ids"]) == len(current) == discovery["total_tests"]
                         and not changed and receipt["frozen_head_unchanged"]
                         and receipt["clean_tracked_status_after"] and receipt["archive_unchanged"])
    evidence.write_json(logs / "coverage_union.json", receipt)
    print(json.dumps({key: receipt[key] for key in (
        "passed", "final_inventory", "focused_tests_passed", "tests_added", "tests_removed",
        "new_tests_without_focused_coverage", "composite_exactly_covers_final_inventory")}), flush=True)
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

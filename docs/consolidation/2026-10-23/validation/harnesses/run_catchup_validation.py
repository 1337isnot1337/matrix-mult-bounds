"""Run reviewed acceptance checks on the coordinator's frozen catch-up tree.

This harness lives outside all worktrees. It uses a new evidence directory,
retains earlier validation receipts, and never invokes historical harnesses.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import time

import run_full_validation as evidence


BASE = Path(__file__).resolve().parent
PRIOR_RECEIPTS = (
    "test_logs/summary.json",
    "test_logs/tree_before.json",
    "test_logs/tree_after.json",
    "test_logs/coverage_union.json",
    "test_logs/final_focused/summary.json",
    "test_logs/final_focused/tree_before.json",
    "test_logs/final_focused/tree_after.json",
)


def hashes(paths):
    return {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}


def command_for(job, repo):
    if job["kind"] == "unittest":
        if not job.get("targets") or job.get("expected_tests", 0) < 1:
            raise ValueError(f"Missing unit targets/count: {job['name']}")
        return [sys.executable, "-m", "unittest", *job["targets"], "-v"]
    if job["kind"] == "json_verifier":
        relative = Path(job["script"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("Verifier must be a relative repository path")
        if not (repo / relative).is_file():
            raise ValueError(f"Missing reviewed verifier: {relative}")
        if not isinstance(job.get("expected_json"), dict):
            raise ValueError("The direct verifier needs an expected JSON report")
        return [sys.executable, str(relative)]
    raise ValueError(f"Unsupported acceptance kind: {job['kind']}")


def classify_result(job, row):
    log = Path(row["log"])
    if job["kind"] == "unittest":
        row.update(evidence.parse_log(log))
        ids = row["printed_test_ids"]
        row["expected_test_count_matches"] = row["tests_run"] == job["expected_tests"]
        row["unique_printed_test_ids"] = len(set(ids))
        row["no_skips"] = row["unittest_result"] == "OK"
        return (row["returncode"] == 0 and row["no_skips"]
                and row["expected_test_count_matches"]
                and len(ids) == len(set(ids)) == job["expected_tests"]
                and not row["failure_headers"])
    try:
        report = json.loads(log.read_text())
    except (ValueError, UnicodeError) as error:
        row["report_error"] = str(error)
        return False
    row["report"] = report
    row["expected_report_matches"] = report == job["expected_json"]
    return row["returncode"] == 0 and row["expected_report_matches"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-tree-ready", action="store_true")
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--repo", type=Path, default=BASE / "catchup_repo")
    parser.add_argument("--plan", type=Path, default=BASE / "catchup_validation_plan.json")
    parser.add_argument("--log-dir", type=Path, default=BASE / "test_logs/postvalidation_catchup")
    args = parser.parse_args()
    if not args.final_tree_ready:
        parser.error("The coordinator must declare the frozen tree ready before execution")
    if not re.fullmatch(r"[0-9a-f]{40}", args.expected_head):
        parser.error("Use the exact 40-character frozen commit SHA")
    if sys.flags.optimize:
        parser.error("Acceptance checks require Python assertions enabled")
    repo = args.repo.resolve()
    logs = args.log_dir.resolve()
    if logs == repo or repo in logs.parents:
        parser.error("Evidence must be written outside the frozen worktree")
    if logs.exists():
        parser.error("Use a new evidence directory; existing evidence is immutable")
    plan = json.loads(args.plan.read_text())
    jobs = plan["jobs"]
    names = [job["name"] for job in jobs]
    if len(names) != len(set(names)) or any(not re.fullmatch(r"[a-z0-9-]+", name) for name in names):
        parser.error("Each job must have a distinct safe filename")
    commands = [command_for(job, repo) for job in jobs]
    evidence.REPO = repo
    before = evidence.snapshot()
    if before["head"] != args.expected_head or before["status"]:
        parser.error("The worktree must be clean and at the exact declared frozen commit")
    prior_paths = [BASE / name for name in PRIOR_RECEIPTS]
    prior_before = hashes(prior_paths)
    logs.mkdir(parents=True)
    evidence.write_json(logs / "plan.json", plan)
    evidence.write_json(logs / "tree_before.json", before)
    environment = os.environ.copy()
    environment.update(PYTHONOPTIMIZE="0", PYTHONPATH="tests", PYTHONHASHSEED="0",
                       PYTHONDONTWRITEBYTECODE="1", OMP_NUM_THREADS="1",
                       OPENBLAS_NUM_THREADS="1")
    state = {
        "started_at": evidence.utc_now(),
        "head": before["head"],
        "head_tree": before["head_tree"],
        "tracked_content_sha256": before["tracked_content_sha256"],
        "repo": str(repo),
        "python": platform.python_version(),
        "python_executable": sys.executable,
        "assertions_enabled": True,
        "plan_sha256": hashlib.sha256(args.plan.read_bytes()).hexdigest(),
        "harness_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "prior_receipt_sha256": prior_before,
        "scope": plan["scope"],
        "jobs": [],
    }
    processes = []
    overall_start = time.monotonic()
    for job, command in zip(jobs, commands):
        log_path = logs / f"{job['name']}.log"
        output = log_path.open("w")
        process = subprocess.Popen(command, cwd=repo, env=environment,
                                   stdout=output, stderr=subprocess.STDOUT)
        row = {"name": job["name"], "kind": job["kind"], "command": command,
               "pid": process.pid, "started_at": evidence.utc_now(),
               "log": str(log_path), "status": "running"}
        state["jobs"].append(row)
        processes.append((job, process, output, time.monotonic(), row))
        print(f"Started {job['name']}: PID {process.pid}", flush=True)
    evidence.write_json(logs / "progress.json", state)
    last_status = time.monotonic()
    while any(row["status"] == "running" for _, _, _, _, row in processes):
        for job, process, output, start, row in processes:
            if row["status"] != "running" or process.poll() is None:
                continue
            output.close()
            row.update(returncode=process.returncode, completed_at=evidence.utc_now(),
                       elapsed_seconds=round(time.monotonic() - start, 3))
            row["status"] = "passed" if classify_result(job, row) else "failed"
            row["log_sha256"] = hashlib.sha256(Path(row["log"]).read_bytes()).hexdigest()
            evidence.write_json(logs / "progress.json", state)
            print(f"Completed {row['name']}: {row['status']} in {row['elapsed_seconds']}s", flush=True)
        if time.monotonic() - last_status >= 30:
            for _, _, _, start, row in processes:
                if row["status"] == "running":
                    lines = Path(row["log"]).read_text(errors="replace").splitlines()
                    tail = lines[-1][:180] if lines else "starting"
                    print(f"{row['name']} {time.monotonic()-start:.0f}s: {tail}", flush=True)
            last_status = time.monotonic()
        time.sleep(1)
    after = evidence.snapshot()
    evidence.write_json(logs / "tree_after.json", after)
    changed = sorted(path for path in set(before["file_sha256"]) | set(after["file_sha256"])
                     if before["file_sha256"].get(path) != after["file_sha256"].get(path))
    units = [row for row in state["jobs"] if row["kind"] == "unittest"]
    ids = [test_id for row in units for test_id in row["printed_test_ids"]]
    state.update(
        completed_at=evidence.utc_now(),
        elapsed_seconds=round(time.monotonic() - overall_start, 3),
        tests_run=sum(row["tests_run"] or 0 for row in units),
        unique_test_ids=len(set(ids)),
        duplicated_test_ids=len(ids) - len(set(ids)),
        direct_verifiers_run=sum(row["kind"] == "json_verifier" for row in state["jobs"]),
        tracked_files_changed_during_validation=changed,
        frozen_head_unchanged=before["head"] == after["head"],
        clean_tracked_status_after=not after["status"],
        archive_unchanged=before["archive_sha256"] == after["archive_sha256"],
        archive_files_hashed=len(before["archive_sha256"]),
        prior_receipts_unchanged=prior_before == hashes(prior_paths),
    )
    state["passed"] = (
        all(row["status"] == "passed" for row in state["jobs"])
        and not changed and state["frozen_head_unchanged"]
        and state["clean_tracked_status_after"] and state["archive_unchanged"]
        and state["prior_receipts_unchanged"] and not state["duplicated_test_ids"]
    )
    evidence.write_json(logs / "summary.json", state)
    evidence.write_json(logs / "progress.json", state)
    print(json.dumps({key: state[key] for key in (
        "head", "passed", "tests_run", "direct_verifiers_run", "elapsed_seconds",
        "archive_unchanged", "tracked_files_changed_during_validation",
        "prior_receipts_unchanged")}), flush=True)
    return 0 if state["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

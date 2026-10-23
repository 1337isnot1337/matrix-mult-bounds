"""Record the six-test quadratic extension on an exact frozen integration."""
from __future__ import annotations

import argparse
import ast
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import run_full_validation as evidence


BASE = Path(__file__).resolve().parent
PASSING = "e38eb5c21c3e840cd900bfa85c1a4a6808e530fe"
SOURCE = "c7b7257bac3c000543de66a27b3485a29589156c"
PACKAGE = "research/ai/2026-10-23-quadratic-kernel-indices"
TEST = "tests/test_quadratic_kernel_indices.py"
RESULT = "results/quadratic-kernel-indices-2026-10-23/controls.json"
CLAIM = "AI-QUADRATIC-KERNEL-INDICES-001"
SOURCES = PACKAGE + "/sources.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def entries(repo, sha):
    result = {}
    for item in git(repo, "ls-tree", "-r", "-z", sha).split(b"\0"):
        if item:
            metadata, name = item.split(b"\t", 1)
            result[name.decode()] = metadata.decode()
    return result


def claims(repo, sha):
    data = json.loads(git(repo, "show", sha + ":research/claims.json"))
    return {row["id"]: row for row in data["claims"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--log-dir", type=Path, default=BASE / "test_logs/quadratic_followup")
    args = parser.parse_args()
    repo, logs = args.repo.resolve(), args.log_dir.resolve()
    summary_path = logs / "summary.json"
    summary = json.loads(summary_path.read_text())
    if not summary["passed"] or summary["head"] != args.expected_head or summary["tests_run"] != 8:
        parser.error("Require the eight passing focused checks at this exact frozen head")
    if (logs / "coverage_union.json").exists() or (logs / "discovery.json").exists():
        parser.error("Existing evidence is immutable")
    evidence.REPO = repo
    before = evidence.snapshot()
    if before["head"] != args.expected_head or before["status"]:
        parser.error("The frozen tested head must remain clean and unchanged")
    prior_hash_path = BASE / "quadratic_followup_previous_validation_hashes.json"
    previous_hashes = json.loads(prior_hash_path.read_text())
    if any(not Path(p).is_file() or digest(Path(p)) != sha for p, sha in previous_hashes.items()):
        parser.error("A preserved earlier evidence file changed")
    old_inventory_path = BASE / "test_logs/live_catchup/discovery.json"
    old_coverage_path = BASE / "test_logs/live_catchup/coverage_union.json"
    old_inventory = json.loads(old_inventory_path.read_text())
    assert json.loads(old_coverage_path.read_text())["passed"]
    evidence.write_json(logs / "inventory_tree_before.json", before)
    env = os.environ.copy()
    env.update(PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0",
               OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
    command = [sys.executable, "tools/test_shard.py", "--list"]
    started = time.monotonic()
    print("Listing the frozen quadratic-followup unittest inventory", flush=True)
    with (logs / "discovery.log").open("w") as output, (logs / "discovery.stderr.log").open("w") as error:
        result = subprocess.run(command, cwd=repo, env=env, stdout=output, stderr=error, timeout=180)
    if result.returncode:
        raise RuntimeError("Final list-only inventory failed; inspect its stderr log")
    inventory = json.loads((logs / "discovery.log").read_text())
    evidence.write_json(logs / "discovery.json", inventory)
    after = evidence.snapshot()
    evidence.write_json(logs / "inventory_tree_after.json", after)

    old_entries, final_entries, source_entries = (
        entries(repo, revision) for revision in (PASSING, args.expected_head, SOURCE))
    changes = sorted(p for p in old_entries.keys() | final_entries.keys()
                     if old_entries.get(p) != final_entries.get(p))
    exact_source_paths = [PACKAGE + "/README.md", PACKAGE + "/proof.md", PACKAGE + "/verify.py", TEST, RESULT]
    allowed = {"PROVENANCE.md", "STATUS.md", "docs/research_directions.md", "research/ACTIVE.md",
               "research/claims.json", SOURCES, *exact_source_paths}
    unexpected = [p for p in changes if p not in allowed and not p.startswith("docs/consolidation/")]
    exact_source = {p: final_entries.get(p) == source_entries.get(p) for p in exact_source_paths}
    new_paths_are_additions = all(p not in old_entries and p in final_entries for p in exact_source_paths + [SOURCES])
    question = PACKAGE + "/QUESTION.md"
    unchanged_question = final_entries.get(question) == old_entries.get(question) == source_entries.get(question)
    old_tests = [p for p in old_entries if p.startswith("tests/")]
    unchanged_old_tests = all(final_entries.get(p) == old_entries[p] for p in old_tests)

    original_source_record = json.loads(git(repo, "show", SOURCE + ":" + SOURCES))
    repaired_source_record = json.loads((repo / SOURCES).read_text())
    expected_repaired = deepcopy(original_source_record)
    readme_dependency = next(row for row in expected_repaired["local_dependencies"]
                             if row["path"] == "research/ai/2026-10-20-anisotropic-constructions/README.md")
    readme_dependency["sha256"] = digest(repo / readme_dependency["path"])
    only_pin_repaired = repaired_source_record == expected_repaired
    pin_checks = [{"path": row["path"], "expected_sha256": row["sha256"],
                   "actual_sha256": digest(repo / row["path"])}
                  for row in repaired_source_record["local_dependencies"]]
    pins_exact = all(row["expected_sha256"] == row["actual_sha256"] for row in pin_checks)
    literal_path = "research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md"
    literal_blob_exact = repaired_source_record["literal_source_blob"] == git(
        repo, "rev-parse", args.expected_head + ":" + literal_path).decode().strip()
    repair_report_path = BASE / "quadratic_pin_resolution.json"
    repair_report = json.loads(repair_report_path.read_text())
    repair_outputs_exact = all(digest(repo / row["path"]) == row["sha256"] for row in repair_report["output_files"])
    originals_exact = all((repo / row["path"]).read_bytes() == git(
        repo, "show", row["source_commit"] + ":" + row["source_path"])
        for row in repair_report["output_files"] if "source_commit" in row)

    old_claims, final_claims, source_claims = (claims(repo, rev) for rev in (PASSING, args.expected_head, SOURCE))
    added_claims = sorted(final_claims.keys() - old_claims.keys())
    removed_claims = sorted(old_claims.keys() - final_claims.keys())
    revised_claims = sorted(key for key in old_claims if old_claims[key] != final_claims.get(key))
    new_claim_exact = final_claims.get(CLAIM) == source_claims.get(CLAIM)
    claim = final_claims.get(CLAIM, {})
    new_claim_unreviewed = claim.get("status") == "proof-written-unreviewed" and all(
        claim.get(flag) is False for flag in ("independent_review", "lean_formalized", "improves_omega"))

    parsed = ast.parse(git(repo, "show", SOURCE + ":" + TEST))
    expected_new_tests = {"test_quadratic_kernel_indices.QuadraticKernelIndicesTests." + node.name
                          for cls in parsed.body if isinstance(cls, ast.ClassDef)
                          and cls.name == "QuadraticKernelIndicesTests" for node in cls.body
                          if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")}
    previous, current = set(old_inventory["test_ids"]), set(inventory["test_ids"])
    selected = {test for row in summary["jobs"] for test in row["printed_test_ids"]}
    tracked_changes = sorted(p for p in before["file_sha256"].keys() | after["file_sha256"].keys()
                             if before["file_sha256"].get(p) != after["file_sha256"].get(p))
    changed_prior = [p for p, sha in previous_hashes.items() if not Path(p).is_file() or digest(Path(p)) != sha]
    source_paths = [summary_path, old_inventory_path, old_coverage_path, prior_hash_path,
                    repair_report_path, BASE / "quadratic_followup_code_audit.json"]
    receipt = {
        "schema": "matrix-mult-bounds-quadratic-followup-coverage-v1", "recorded_at": evidence.utc_now(),
        "head": before["head"], "head_tree": before["head_tree"], "passing_comparison_head": PASSING,
        "source_commit": SOURCE,
        "discovery_command": command, "discovery_elapsed_seconds": round(time.monotonic() - started, 3),
        "previous_inventory": {"tests": len(previous), "modules": old_inventory["total_modules"]},
        "final_inventory": {"tests": len(current), "modules": inventory["total_modules"]},
        "tests_added": sorted(current - previous), "tests_removed": sorted(previous - current),
        "new_tests_without_focused_coverage": sorted((current - previous) - selected),
        "focused_tests_passed": len(selected), "focused_ids_outside_final_inventory": sorted(selected - current),
        "composite_exactly_covers_final_inventory": previous | selected == current,
        "changed_paths_since_passing_publication_tree": changes, "unexpected_changes": unexpected,
        "existing_test_files_checked": len(old_tests), "all_existing_test_bytes_unchanged": unchanged_old_tests,
        "new_source_paths_are_additions": new_paths_are_additions,
        "exact_source_file_checks": exact_source, "original_question_unchanged": unchanged_question,
        "only_context_readme_pin_repaired": only_pin_repaired, "strict_dependency_pin_checks": pin_checks,
        "literal_mathematical_blob_pin_exact": literal_blob_exact,
        "pin_repair_outputs_exact": repair_outputs_exact, "original_pin_and_dependency_bytes_retained": originals_exact,
        "claims_count": len(final_claims), "added_claim_ids": added_claims,
        "removed_claim_ids": removed_claims, "revised_existing_claim_ids": revised_claims,
        "new_claim_matches_exact_source": new_claim_exact, "new_claim_keeps_unreviewed_status_flags": new_claim_unreviewed,
        "tracked_files_changed_during_inventory": tracked_changes, "frozen_head_unchanged": before["head"] == after["head"],
        "clean_tracked_status_after": not after["status"], "archive_unchanged": before["archive_sha256"] == after["archive_sha256"],
        "archive_files_hashed": len(before["archive_sha256"]), "previous_evidence_files_checked": len(previous_hashes),
        "changed_previous_evidence_files": changed_prior,
        "source_receipts": [{"path": str(p), "sha256": digest(p)} for p in source_paths],
        "scope_caveat": "This extends the prior 1,951-test passing composite with six new quadratic-kernel tests and two focused repository checks. All earlier test definitions and unrelated active content are unchanged. The final complete suite was listed, not freshly executed in one local run. Final-head hosted Python matrix, replay and Lean CI remains required. Finite controls do not promote mathematical review or formalization status.",
    }
    receipt["passed"] = (
        len(previous) == 1951 and old_inventory["total_modules"] == 437
        and len(current) == inventory["total_tests"] == len(inventory["test_ids"]) == 1957
        and inventory["total_modules"] == 438 and len(expected_new_tests) == 6
        and current - previous == expected_new_tests and not previous - current
        and len(selected) == 8 and not selected - current and previous | selected == current
        and not unexpected and unchanged_old_tests and new_paths_are_additions and all(exact_source.values())
        and unchanged_question and only_pin_repaired and pins_exact and literal_blob_exact
        and repair_outputs_exact and originals_exact
        and len(old_claims) == 612 and len(final_claims) == 613 and added_claims == [CLAIM]
        and not removed_claims and not revised_claims and new_claim_exact and new_claim_unreviewed
        and not tracked_changes and not changed_prior and receipt["frozen_head_unchanged"]
        and receipt["clean_tracked_status_after"] and receipt["archive_unchanged"])
    evidence.write_json(logs / "coverage_union.json", receipt)
    print(json.dumps({key: receipt[key] for key in (
        "passed", "head", "final_inventory", "tests_added", "tests_removed", "focused_tests_passed",
        "unexpected_changes", "added_claim_ids", "revised_existing_claim_ids", "changed_previous_evidence_files")}), flush=True)
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

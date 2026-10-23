"""Record four new quadratic tests and exact source revisions on the frozen RAM tree."""
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

ROOT = Path("/dev/shm/matrix-consolidation-5e4a124ebf61")
DISK = Path("/workspace/scratch/5e4a124ebf61/consolidation")
sys.path.insert(0, str(DISK))
import run_full_validation as evidence

PASSING = "45b082d12e2d0e36a1c542899000b192cdcc1bb7"
SOURCE = "f00613b057cc4437fad4d10e22f1b6c8cc891872"
PACKAGE = "research/ai/2026-10-23-quadratic-kernel-indices"
TEST = "tests/test_quadratic_kernel_indices.py"
SOURCES = PACKAGE + "/sources.json"
RESULT = "results/quadratic-kernel-indices-2026-10-23/controls.json"
CLAIMS = {"AI-QUADRATIC-KERNEL-INDICES-001", "AI-QUADRATIC-INDEX-DICHOTOMY-002"}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])

def entries(repo, sha):
    result = {}
    for item in git(repo, "ls-tree", "-r", "-z", sha).split(b"\0"):
        if item:
            meta, name = item.split(b"\t", 1)
            result[name.decode()] = meta.decode()
    return result

def claims(repo, sha):
    return {row["id"]: row for row in json.loads(git(repo, "show", sha + ":research/claims.json"))["claims"]}

def methods(raw):
    return {node.name: node for cls in ast.parse(raw).body if isinstance(cls, ast.ClassDef)
            and cls.name == "QuadraticKernelIndicesTests" for node in cls.body
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")}

def subsequence(left, right):
    iterator = iter(right)
    return all(any(item == wanted for item in iterator) for wanted in left)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--log-dir", type=Path, default=ROOT / "test_logs_balanced_followup")
    args = parser.parse_args()
    repo, logs = args.repo.resolve(), args.log_dir.resolve()
    summary_path = logs / "summary.json"
    summary = json.loads(summary_path.read_text())
    if not summary["passed"] or summary["head"] != args.expected_head or summary["tests_run"] != 12:
        parser.error("Require 12 passing focused checks at this exact frozen head")
    if (logs / "coverage_union.json").exists() or (logs / "discovery.json").exists():
        parser.error("Existing evidence is immutable")
    evidence.REPO = repo
    before = evidence.snapshot()
    if before["head"] != args.expected_head or before["status"]:
        parser.error("The tested worktree must remain clean at the frozen revision")
    prior_hash_path = ROOT / "balanced_followup_previous_validation_hashes.json"
    prior_hashes = json.loads(prior_hash_path.read_text())
    if any(not Path(p).is_file() or digest(Path(p)) != h for p, h in prior_hashes.items()):
        parser.error("An earlier evidence file changed")
    inventory_path = DISK / "test_logs/quadratic_followup/discovery.json"
    coverage_path = DISK / "test_logs/quadratic_followup/coverage_union.json"
    equivalence_path = DISK / "test_logs/structural_followup/equivalence.json"
    old_inventory = json.loads(inventory_path.read_text())
    assert json.loads(coverage_path.read_text())["passed"] and json.loads(equivalence_path.read_text())["passed"]
    evidence.write_json(logs / "inventory_tree_before.json", before)
    env = os.environ.copy()
    env.update(PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0",
               OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
    command = [sys.executable, "tools/test_shard.py", "--list"]
    start = time.monotonic()
    print("Listing the frozen balanced-followup unittest inventory", flush=True)
    with (logs / "discovery.log").open("w") as out, (logs / "discovery.stderr.log").open("w") as err:
        result = subprocess.run(command, cwd=repo, env=env, stdout=out, stderr=err, timeout=180)
    if result.returncode:
        raise RuntimeError("Final inventory failed; inspect its stderr log")
    inventory = json.loads((logs / "discovery.log").read_text())
    evidence.write_json(logs / "discovery.json", inventory)
    after = evidence.snapshot()
    evidence.write_json(logs / "inventory_tree_after.json", after)
    old_entries, final_entries, source_entries = (entries(repo, rev) for rev in (PASSING, args.expected_head, SOURCE))
    changes = sorted(p for p in old_entries.keys() | final_entries.keys()
                     if old_entries.get(p) != final_entries.get(p))
    exact_paths = [PACKAGE + "/README.md", PACKAGE + "/dichotomy.md", PACKAGE + "/verify.py", RESULT, TEST]
    allowed = {"STATUS.md", "PROVENANCE.md", "docs/research_directions.md", "research/ACTIVE.md",
               "research/claims.json", SOURCES, *exact_paths}
    unexpected = [p for p in changes if p not in allowed and not p.startswith("docs/consolidation/")]
    source_checks = {p: final_entries.get(p) == source_entries.get(p) for p in exact_paths}
    old_tests = [p for p in old_entries if p.startswith("tests/") and p != TEST]
    other_tests_unchanged = all(final_entries.get(p) == old_entries[p] for p in old_tests)
    old_methods, final_methods = (methods(git(repo, "show", rev + ":" + TEST)) for rev in (PASSING, args.expected_head))
    added_methods = sorted(final_methods.keys() - old_methods.keys())
    changed_methods = sorted(name for name in old_methods if ast.dump(old_methods[name]) != ast.dump(final_methods[name]))
    report_assertions_retained = subsequence(
        [ast.dump(node) for node in old_methods["test_complete_finite_report"].body],
        [ast.dump(node) for node in final_methods["test_complete_finite_report"].body])
    expected_new = {"test_quadratic_kernel_indices.QuadraticKernelIndicesTests." + name for name in added_methods}
    previous, current = set(old_inventory["test_ids"]), set(inventory["test_ids"])
    selected = {test for row in summary["jobs"] for test in row["printed_test_ids"]}
    source_record = json.loads(git(repo, "show", SOURCE + ":" + SOURCES))
    actual_record = json.loads((repo / SOURCES).read_text())
    expected_record = deepcopy(source_record)
    dependency = next(row for row in expected_record["local_dependencies"]
                      if row["path"] == "research/ai/2026-10-20-anisotropic-constructions/README.md")
    dependency["sha256"] = digest(repo / dependency["path"])
    only_pin_repaired = actual_record == expected_record
    pin_checks = [{"path": row["path"], "expected_sha256": row["sha256"],
                   "actual_sha256": digest(repo / row["path"])} for row in actual_record["local_dependencies"]]
    pins_exact = all(row["expected_sha256"] == row["actual_sha256"] for row in pin_checks)
    repair_path = ROOT / "balanced_followup_pin_resolution.json"
    repair = json.loads(repair_path.read_text())
    outputs_exact = all(digest(repo / row["path"]) == row["sha256"] for row in repair["output_files"])
    backups = [row for row in repair["output_files"] if "source_commit" in row] + repair["earlier_exact_originals_retained"]
    originals_exact = all((repo / row["path"]).read_bytes() == git(
        repo, "show", row["source_commit"] + ":" + row["source_path"]) for row in backups)
    old_claims, final_claims, source_claims = (claims(repo, rev) for rev in (PASSING, args.expected_head, SOURCE))
    changed_claims = sorted(key for key in old_claims.keys() | final_claims.keys()
                            if old_claims.get(key) != final_claims.get(key))
    exact_claim_revisions = set(changed_claims) == CLAIMS and all(final_claims[key] == source_claims[key] for key in CLAIMS)
    flags = ("status", "independent_review", "lean_formalized", "improves_omega")
    flags_unchanged = old_claims.keys() == final_claims.keys() and all(
        all(old_claims[key].get(flag) == final_claims[key].get(flag) for flag in flags) for key in old_claims)
    changed_fields = {key: sorted(field for field in old_claims[key].keys() | final_claims[key].keys()
                                 if old_claims[key].get(field) != final_claims[key].get(field)) for key in changed_claims}
    tracked_changes = sorted(p for p in before["file_sha256"].keys() | after["file_sha256"].keys()
                             if before["file_sha256"].get(p) != after["file_sha256"].get(p))
    changed_prior = [p for p, h in prior_hashes.items() if not Path(p).is_file() or digest(Path(p)) != h]
    source_receipts = [summary_path, inventory_path, coverage_path, equivalence_path, prior_hash_path,
                       repair_path, ROOT / "balanced_followup_code_audit.json"]
    receipt = {
        "schema": "matrix-mult-bounds-balanced-followup-coverage-v1", "recorded_at": evidence.utc_now(),
        "head": before["head"], "head_tree": before["head_tree"], "passing_comparison_head": PASSING, "source_commit": SOURCE,
        "discovery_command": command, "discovery_elapsed_seconds": round(time.monotonic() - start, 3),
        "previous_inventory": {"tests": len(previous), "modules": old_inventory["total_modules"]},
        "final_inventory": {"tests": len(current), "modules": inventory["total_modules"]},
        "tests_added": sorted(current - previous), "tests_removed": sorted(previous - current),
        "new_tests_without_focused_coverage": sorted((current - previous) - selected),
        "focused_tests_passed": len(selected), "focused_ids_outside_final_inventory": sorted(selected - current),
        "composite_exactly_covers_final_inventory": previous | selected == current,
        "changed_paths_since_passing_tree": changes, "unexpected_changes": unexpected,
        "source_exact_updated_artifact_checks": source_checks,
        "unmodified_test_files_checked": len(old_tests), "other_test_modules_byte_exact": other_tests_unchanged,
        "new_test_methods": added_methods, "changed_existing_test_methods": changed_methods,
        "all_previous_finite_report_assertions_retained_in_order": report_assertions_retained,
        "only_reviewed_context_pin_repaired_from_source": only_pin_repaired, "strict_dependency_pin_checks": pin_checks,
        "pin_repair_outputs_exact": outputs_exact, "all_four_original_metadata_readme_blobs_retained": originals_exact,
        "claims_count": len(final_claims), "changed_claim_fields": changed_fields,
        "both_claim_revisions_match_exact_source": exact_claim_revisions, "all_claim_status_flags_unchanged": flags_unchanged,
        "tracked_files_changed_during_inventory": tracked_changes, "frozen_head_unchanged": before["head"] == after["head"],
        "clean_tracked_status_after": not after["status"], "archive_unchanged": before["archive_sha256"] == after["archive_sha256"],
        "archive_files_hashed": len(before["archive_sha256"]), "previous_evidence_files_checked": len(prior_hashes),
        "changed_previous_evidence_files": changed_prior,
        "source_receipts": [{"path": str(p), "sha256": digest(p)} for p in source_receipts],
        "scope_caveat": "The complete updated ten-test quadratic module and two repository checks passed. This adds four tests to the prior 1,957-test composite and reruns the modified finite-report assertions and original package regressions. Other test modules and unrelated active content are unchanged. The full final local suite was listed, not freshly executed in one run. Final-head hosted Python matrix, replay and Lean CI remains required; all mathematical review/status flags are preserved.",
    }
    receipt["passed"] = (
        len(previous) == 1957 and old_inventory["total_modules"] == 438
        and len(current) == inventory["total_tests"] == len(inventory["test_ids"]) == 1961
        and inventory["total_modules"] == 438 and len(expected_new) == 4
        and current - previous == expected_new and not previous - current
        and len(selected) == 12 and not selected - current and previous | selected == current
        and not unexpected and all(source_checks.values()) and other_tests_unchanged
        and not old_methods.keys() - final_methods.keys() and changed_methods == ["test_complete_finite_report"]
        and report_assertions_retained and only_pin_repaired and pins_exact and outputs_exact and originals_exact
        and len(old_claims) == len(final_claims) == 614 and exact_claim_revisions and flags_unchanged
        and not tracked_changes and not changed_prior and receipt["frozen_head_unchanged"]
        and receipt["clean_tracked_status_after"] and receipt["archive_unchanged"])
    evidence.write_json(logs / "coverage_union.json", receipt)
    print(json.dumps({key: receipt[key] for key in ["passed", "head", "final_inventory", "tests_added", "tests_removed",
        "focused_tests_passed", "unexpected_changes", "changed_claim_fields", "changed_previous_evidence_files"]}), flush=True)
    return 0 if receipt["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())

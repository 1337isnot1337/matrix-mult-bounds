"""Record the one-test Hankel extension on the frozen final integration."""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import run_full_validation as evidence


BASE = Path(__file__).resolve().parent
PASSING = "33a0f407b2071ed30433b2b1fbd8a577c50ea044"
HANKEL = "232867536a9011d45d5014d14aeac1eeb6af0864"
QUADRATIC = "7ecec6ebac9a6bb0dbeec2bf337fc4cadb23a1bb"
PACKAGE = "research/ai/2026-10-23-hankel-all-characteristics"
TEST_PATH = "tests/test_hankel_all_characteristics.py"
NEW_METHOD = "test_finite_field_homogeneous_interpolation_and_its_boundary"
NEW_TEST = "test_hankel_all_characteristics.HankelAllCharacteristicsTests." + NEW_METHOD


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
    parser.add_argument("--log-dir", type=Path, default=BASE / "test_logs/live_catchup")
    args = parser.parse_args()
    repo, logs = args.repo.resolve(), args.log_dir.resolve()
    summary_path = logs / "summary.json"
    summary = json.loads(summary_path.read_text())
    if not summary["passed"] or summary["head"] != args.expected_head or summary["tests_run"] != 4:
        parser.error("Require the four passing focused checks at this exact frozen head")
    if (logs / "coverage_union.json").exists() or (logs / "discovery.json").exists():
        parser.error("Existing evidence is immutable")
    evidence.REPO = repo
    before = evidence.snapshot()
    if before["head"] != args.expected_head or before["status"]:
        parser.error("The frozen tested head must remain clean and unchanged")
    prior_hash_path = BASE / "live_catchup_previous_validation_hashes.json"
    previous_hashes = json.loads(prior_hash_path.read_text())
    if any(not Path(p).is_file() or digest(Path(p)) != sha for p, sha in previous_hashes.items()):
        parser.error("A preserved earlier evidence file changed")
    old_inventory_path = BASE / "test_logs/nextwave/discovery.json"
    old_coverage_path = BASE / "test_logs/nextwave/coverage_union.json"
    old_equivalence_path = BASE / "test_logs/nextwave_publication/equivalence.json"
    old_inventory = json.loads(old_inventory_path.read_text())
    assert json.loads(old_coverage_path.read_text())["passed"]
    assert json.loads(old_equivalence_path.read_text())["passed"]
    evidence.write_json(logs / "inventory_tree_before.json", before)
    env = os.environ.copy()
    env.update(PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0",
               OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
    command = [sys.executable, "tools/test_shard.py", "--list"]
    started = time.monotonic()
    print("Listing the frozen final unittest inventory", flush=True)
    with (logs / "discovery.log").open("w") as output, (logs / "discovery.stderr.log").open("w") as error:
        result = subprocess.run(command, cwd=repo, env=env, stdout=output, stderr=error, timeout=180)
    if result.returncode:
        raise RuntimeError("Final list-only inventory failed; inspect its stderr log")
    inventory = json.loads((logs / "discovery.log").read_text())
    evidence.write_json(logs / "discovery.json", inventory)
    after = evidence.snapshot()
    evidence.write_json(logs / "inventory_tree_after.json", after)
    old_entries, final_entries = entries(repo, PASSING), entries(repo, args.expected_head)
    changes = sorted(p for p in old_entries.keys() | final_entries.keys()
                     if old_entries.get(p) != final_entries.get(p))
    allowed = {"PROVENANCE.md", "STATUS.md", "docs/research_directions.md", "research/ACTIVE.md",
               "research/claims.json", TEST_PATH, PACKAGE + "/README.md", PACKAGE + "/proof.md",
               PACKAGE + "/sources.json", "research/ai/2026-10-23-quadratic-kernel-indices/QUESTION.md"}
    unexpected = [p for p in changes if p not in allowed and not p.startswith("docs/consolidation/")]
    old_ast = ast.parse(git(repo, "show", PASSING + ":" + TEST_PATH))
    final_ast = ast.parse(git(repo, "show", args.expected_head + ":" + TEST_PATH))
    trimmed = copy.deepcopy(final_ast)
    for node in trimmed.body:
        if isinstance(node, ast.ClassDef) and node.name == "HankelAllCharacteristicsTests":
            node.body = [item for item in node.body if not isinstance(item, ast.FunctionDef)
                         or item.name != NEW_METHOD]
    old_test_ast_preserved = ast.dump(trimmed) == ast.dump(old_ast)
    source_entries = entries(repo, HANKEL)
    exact_source_paths = [TEST_PATH, PACKAGE + "/README.md", PACKAGE + "/proof.md", PACKAGE + "/sources.json"]
    exact_hankel = all(final_entries.get(p) == source_entries.get(p) for p in exact_source_paths)
    question = "research/ai/2026-10-23-quadratic-kernel-indices/QUESTION.md"
    exact_question = final_entries.get(question) == entries(repo, QUADRATIC).get(question)
    old_claims, final_claims, source_claims = claims(repo, PASSING), claims(repo, args.expected_head), claims(repo, HANKEL)
    changed_claims = sorted(key for key in old_claims.keys() | final_claims.keys()
                           if old_claims.get(key) != final_claims.get(key))
    changed_fields = {key: sorted(field for field in old_claims.get(key, {}).keys() | final_claims.get(key, {}).keys()
                                 if old_claims.get(key, {}).get(field) != final_claims.get(key, {}).get(field))
                      for key in changed_claims}
    flags = ("status", "independent_review", "lean_formalized", "improves_omega")
    flags_unchanged = old_claims.keys() == final_claims.keys() and all(
        all(old_claims[key].get(flag) == final_claims[key].get(flag) for flag in flags) for key in old_claims)
    exact_claim_correction = len(changed_claims) == 1 and all(
        changed_fields[key] == ["limitations"] and final_claims[key] == source_claims.get(key)
        for key in changed_claims)
    previous, current = set(old_inventory["test_ids"]), set(inventory["test_ids"])
    selected = {test for row in summary["jobs"] for test in row["printed_test_ids"]}
    tracked_changes = sorted(p for p in before["file_sha256"].keys() | after["file_sha256"].keys()
                             if before["file_sha256"].get(p) != after["file_sha256"].get(p))
    changed_prior = [p for p, sha in previous_hashes.items() if not Path(p).is_file() or digest(Path(p)) != sha]
    source_paths = [summary_path, old_inventory_path, old_coverage_path, old_equivalence_path,
                    prior_hash_path, BASE / "live_catchup_code_audit.json"]
    receipt = {
        "schema": "matrix-mult-bounds-live-catchup-coverage-v1", "recorded_at": evidence.utc_now(),
        "head": before["head"], "head_tree": before["head_tree"], "passing_comparison_head": PASSING,
        "discovery_command": command, "discovery_elapsed_seconds": round(time.monotonic() - started, 3),
        "previous_inventory": {"tests": len(previous), "modules": old_inventory["total_modules"]},
        "final_inventory": {"tests": len(current), "modules": inventory["total_modules"]},
        "tests_added": sorted(current - previous), "tests_removed": sorted(previous - current),
        "new_tests_without_focused_coverage": sorted((current - previous) - selected),
        "focused_tests_passed": len(selected), "focused_ids_outside_final_inventory": sorted(selected - current),
        "composite_exactly_covers_final_inventory": previous | selected == current,
        "changed_paths_since_passing_publication_tree": changes, "unexpected_changes": unexpected,
        "prior_hankel_test_module_ast_preserved": old_test_ast_preserved,
        "updated_hankel_files_match_exact_source": exact_hankel, "new_question_matches_exact_source": exact_question,
        "claims_count": len(final_claims), "changed_claim_fields": changed_fields,
        "claim_correction_matches_exact_source": exact_claim_correction, "claim_status_flags_unchanged": flags_unchanged,
        "tracked_files_changed_during_inventory": tracked_changes, "frozen_head_unchanged": before["head"] == after["head"],
        "clean_tracked_status_after": not after["status"], "archive_unchanged": before["archive_sha256"] == after["archive_sha256"],
        "archive_files_hashed": len(before["archive_sha256"]), "previous_evidence_files_checked": len(previous_hashes),
        "changed_previous_evidence_files": changed_prior,
        "source_receipts": [{"path": str(p), "sha256": digest(p)} for p in source_paths],
        "scope_caveat": "This extends the prior 1,950-test passing composite with one new Hankel test and three focused pin/metadata checks. All earlier test definitions are preserved and all unrelated active content is unchanged. The final complete suite was listed, not freshly executed in one local run. Final-head hosted Python matrix, replay and Lean CI remains required; mathematical review/status flags are unchanged.",
    }
    receipt["passed"] = (
        len(previous) == 1950 and old_inventory["total_modules"] == 437
        and len(current) == inventory["total_tests"] == len(inventory["test_ids"]) == 1951
        and inventory["total_modules"] == 437 and current - previous == {NEW_TEST}
        and not previous - current and len(selected) == 4 and not selected - current
        and previous | selected == current and old_test_ast_preserved and exact_hankel and exact_question
        and not unexpected and len(final_claims) == 612 and exact_claim_correction and flags_unchanged
        and not tracked_changes and not changed_prior and receipt["frozen_head_unchanged"]
        and receipt["clean_tracked_status_after"] and receipt["archive_unchanged"])
    evidence.write_json(logs / "coverage_union.json", receipt)
    print(json.dumps({key: receipt[key] for key in (
        "passed", "head", "final_inventory", "tests_added", "tests_removed", "focused_tests_passed",
        "unexpected_changes", "changed_claim_fields", "changed_previous_evidence_files")}), flush=True)
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

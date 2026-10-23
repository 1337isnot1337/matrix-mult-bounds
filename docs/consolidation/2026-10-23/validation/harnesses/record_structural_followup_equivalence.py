"""Transfer passing quadratic coverage over a metadata/proof-only sequel."""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess

import run_full_validation as evidence


BASE = Path(__file__).resolve().parent
PASSING = "dcd18b0cb9cc00b8a7394f78b36d53c7e35d6b82"
SOURCE = "80bd2ae6e1231c5fcd6ea1b01684d49e4b496def"
PACKAGE = "research/ai/2026-10-23-quadratic-kernel-indices"
SOURCES = PACKAGE + "/sources.json"
CLAIM = "AI-QUADRATIC-INDEX-DICHOTOMY-002"


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
    parser.add_argument("--log-dir", type=Path, default=BASE / "test_logs/structural_followup")
    args = parser.parse_args()
    repo, logs = args.repo.resolve(), args.log_dir.resolve()
    summary_path = logs / "summary.json"
    summary = json.loads(summary_path.read_text())
    if not summary["passed"] or summary["head"] != args.expected_head or summary["tests_run"] != 3:
        parser.error("Require the three passing checks at this exact frozen head")
    if (logs / "equivalence.json").exists():
        parser.error("Existing evidence is immutable")
    evidence.REPO = repo
    before = evidence.snapshot()
    if before["head"] != args.expected_head or before["status"]:
        parser.error("The frozen tested head must remain clean and unchanged")
    prior_hash_path = BASE / "structural_followup_previous_validation_hashes.json"
    previous_hashes = json.loads(prior_hash_path.read_text())
    if any(not Path(p).is_file() or digest(Path(p)) != sha for p, sha in previous_hashes.items()):
        parser.error("A preserved earlier evidence file changed")
    inventory_path = BASE / "test_logs/quadratic_followup/discovery.json"
    coverage_path = BASE / "test_logs/quadratic_followup/coverage_union.json"
    inventory = json.loads(inventory_path.read_text())
    prior_coverage = json.loads(coverage_path.read_text())
    assert prior_coverage["passed"]
    evidence.write_json(logs / "equivalence_tree_before.json", before)
    old_entries, final_entries, source_entries = (
        entries(repo, revision) for revision in (PASSING, args.expected_head, SOURCE))
    changes = sorted(p for p in old_entries.keys() | final_entries.keys()
                     if old_entries.get(p) != final_entries.get(p))
    allowed = {"PROVENANCE.md", "STATUS.md", "docs/research_directions.md", "research/ACTIVE.md",
               "research/claims.json", PACKAGE + "/README.md", PACKAGE + "/dichotomy.md", SOURCES}
    unexpected = [p for p in changes if p not in allowed and not p.startswith("docs/consolidation/")]
    tests_before = {p: value for p, value in old_entries.items() if p.startswith("tests/")}
    tests_after = {p: value for p, value in final_entries.items() if p.startswith("tests/")}
    tests_exact = tests_before == tests_after
    code_paths = sorted(p for p in old_entries.keys() | final_entries.keys()
                        if not p.startswith("docs/consolidation/") and (
                            Path(p).suffix in {".py", ".lean", ".toml", ".yml", ".yaml", ".sh"}
                            or Path(p).name in {"requirements.txt", "lean-toolchain", "Dockerfile", "Makefile"}))
    changed_code = [p for p in code_paths if old_entries.get(p) != final_entries.get(p)]
    source_proof_checks = {p: final_entries.get(p) == source_entries.get(p)
                           for p in [PACKAGE + "/README.md", PACKAGE + "/dichotomy.md"]}
    existing_artifact_checks = {p: final_entries.get(p) == old_entries.get(p)
                               for p in [PACKAGE + "/proof.md", PACKAGE + "/verify.py", PACKAGE + "/QUESTION.md",
                                         "tests/test_quadratic_kernel_indices.py",
                                         "results/quadratic-kernel-indices-2026-10-23/controls.json"]}

    source_record = json.loads(git(repo, "show", SOURCE + ":" + SOURCES))
    actual_record = json.loads((repo / SOURCES).read_text())
    expected_record = deepcopy(source_record)
    dependency = next(row for row in expected_record["local_dependencies"]
                      if row["path"] == "research/ai/2026-10-20-anisotropic-constructions/README.md")
    dependency["sha256"] = digest(repo / dependency["path"])
    only_reviewed_pin_repaired = actual_record == expected_record
    pin_checks = [{"path": row["path"], "expected_sha256": row["sha256"],
                   "actual_sha256": digest(repo / row["path"])} for row in actual_record["local_dependencies"]]
    pins_exact = all(row["expected_sha256"] == row["actual_sha256"] for row in pin_checks)
    prior_record = json.loads(git(repo, "show", PASSING + ":" + SOURCES))
    expected_increment = deepcopy(prior_record)
    expected_increment["external_sources"].append(source_record["external_sources"][-1])
    only_external_theorem_added = actual_record == expected_increment
    repair_path = BASE / "structural_followup_pin_resolution.json"
    repair = json.loads(repair_path.read_text())
    outputs_exact = all(digest(repo / row["path"]) == row["sha256"] for row in repair["output_files"])
    backups = [row for row in repair["output_files"] if "source_commit" in row] + repair["earlier_exact_originals_retained"]
    originals_exact = all((repo / row["path"]).read_bytes() == git(
        repo, "show", row["source_commit"] + ":" + row["source_path"]) for row in backups)
    old_claims, final_claims, source_claims = (claims(repo, rev) for rev in (PASSING, args.expected_head, SOURCE))
    added_claims = sorted(final_claims.keys() - old_claims.keys())
    removed_claims = sorted(old_claims.keys() - final_claims.keys())
    revised_claims = sorted(key for key in old_claims if old_claims[key] != final_claims.get(key))
    claim = final_claims.get(CLAIM, {})
    new_claim_exact = claim == source_claims.get(CLAIM)
    new_claim_unreviewed = claim.get("status") == "proof-written-unreviewed" and all(
        claim.get(flag) is False for flag in ("independent_review", "lean_formalized", "improves_omega"))
    selected = {test for row in summary["jobs"] for test in row["printed_test_ids"]}
    known_ids = set(inventory["test_ids"])
    after = evidence.snapshot()
    evidence.write_json(logs / "equivalence_tree_after.json", after)
    tracked_changes = sorted(p for p in before["file_sha256"].keys() | after["file_sha256"].keys()
                             if before["file_sha256"].get(p) != after["file_sha256"].get(p))
    changed_prior = [p for p, sha in previous_hashes.items() if not Path(p).is_file() or digest(Path(p)) != sha]
    receipt = {
        "schema": "matrix-mult-bounds-structural-followup-equivalence-v1", "recorded_at": evidence.utc_now(),
        "head": before["head"], "head_tree": before["head_tree"], "passing_comparison_head": PASSING,
        "source_commit": SOURCE, "inventory": {"tests": inventory["total_tests"], "modules": inventory["total_modules"]},
        "inventory_reference": {"path": str(inventory_path), "sha256": digest(inventory_path)},
        "passing_coverage_reference": {"path": str(coverage_path), "sha256": digest(coverage_path)},
        "fresh_inventory_required": False, "tests_added": [], "tests_removed": [],
        "focused_tests_passed": len(selected), "focused_ids_outside_transferred_inventory": sorted(selected - known_ids),
        "changed_paths_since_passing_publication_tree": changes, "unexpected_changes": unexpected,
        "test_files_checked": len(tests_before), "all_test_paths_and_bytes_unchanged": tests_exact,
        "active_code_config_dependency_paths_checked": len(code_paths), "changed_active_code_config_dependency_paths": changed_code,
        "source_proof_and_readme_checks": source_proof_checks, "existing_package_artifact_checks": existing_artifact_checks,
        "only_reviewed_context_pin_repaired_from_source": only_reviewed_pin_repaired,
        "only_external_theorem_added_to_prior_maintained_sources": only_external_theorem_added,
        "strict_dependency_pin_checks": pin_checks, "pin_repair_outputs_exact": outputs_exact,
        "all_three_original_metadata_and_readme_blobs_retained": originals_exact,
        "claims_count": len(final_claims), "added_claim_ids": added_claims,
        "removed_claim_ids": removed_claims, "revised_existing_claim_ids": revised_claims,
        "new_claim_matches_exact_source": new_claim_exact, "new_claim_keeps_unreviewed_status_flags": new_claim_unreviewed,
        "tracked_files_changed_during_equivalence_check": tracked_changes,
        "frozen_head_unchanged": before["head"] == after["head"], "clean_tracked_status_after": not after["status"],
        "archive_unchanged": before["archive_sha256"] == after["archive_sha256"],
        "archive_files_hashed": len(before["archive_sha256"]), "previous_evidence_files_checked": len(previous_hashes),
        "changed_previous_evidence_files": changed_prior,
        "source_receipts": [{"path": str(p), "sha256": digest(p)} for p in
                            [summary_path, prior_hash_path, repair_path, BASE / "structural_followup_code_audit.json"]],
        "scope_caveat": "All 1,957 test definitions and active executable/configuration/dependency bytes are unchanged from the passing quadratic integration. Three existing metadata/pin checks were rerun on this revision. The 1,957-test inventory and composite coverage transfer by exact bytes; no new full local run or research discovery was performed. Final-head hosted Python matrix, replay and Lean CI remains required. The added mathematical claim retains its exact unreviewed source status.",
    }
    receipt["passed"] = (inventory["total_tests"] == len(known_ids) == 1957 and inventory["total_modules"] == 438
        and len(selected) == 3 and not selected - known_ids and tests_exact and not changed_code and not unexpected
        and all(source_proof_checks.values()) and all(existing_artifact_checks.values())
        and only_reviewed_pin_repaired and only_external_theorem_added and pins_exact and outputs_exact and originals_exact
        and len(old_claims) == 613 and len(final_claims) == 614 and added_claims == [CLAIM]
        and not removed_claims and not revised_claims and new_claim_exact and new_claim_unreviewed
        and not tracked_changes and not changed_prior and receipt["frozen_head_unchanged"]
        and receipt["clean_tracked_status_after"] and receipt["archive_unchanged"])
    evidence.write_json(logs / "equivalence.json", receipt)
    print(json.dumps({key: receipt[key] for key in ["passed", "head", "inventory", "focused_tests_passed",
        "unexpected_changes", "changed_active_code_config_dependency_paths", "added_claim_ids",
        "revised_existing_claim_ids", "changed_previous_evidence_files"]}), flush=True)
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

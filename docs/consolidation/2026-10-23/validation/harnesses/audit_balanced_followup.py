"""Audit172 archived topic snapshots and the exact main6e reconciliation."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
BASE = "42363c18136a75a1a1e35b65b21c243a764a23ba"
MAIN = "6e11f7c1dfd73ae2d460e43f620a7f982920f043"
SOURCE = "f00613b057cc4437fad4d10e22f1b6c8cc891872"
PREFIX = "docs/consolidation/2026-10-23/"
SELF_RECEIPTS = {PREFIX + x for x in ["central_resolution_manifest.json", "preservation_report.json", "packaged_evidence_index.json"]}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=str(ROOT / "structural_followup_repo"))
    parser.add_argument("--commit", required=True)
    parser.add_argument("--superseding-report", action="append", default=[])
    args = parser.parse_args()

    def git(*parts):
        return subprocess.check_output(["git", "-C", args.repo, *parts])

    old = (ROOT / "structural_followup_resolution_manifest.42363c18.json").read_bytes()
    prior_path = ROOT / "balanced_followup_output/prior_manifest.42363c18.json"
    if prior_path.exists():
        assert prior_path.read_bytes() == old
    else:
        prior_path.write_bytes(old)
    prior = json.loads(old)
    outputs = {r["path"]: deepcopy(r) for r in prior["outputs"]}
    superseded = deepcopy(prior["superseded_outputs"])
    inputs = {str(prior_path): digest(old)}
    conflicts = set(prior["covered_conflicts"])
    logs = ["merge_log.json", "catchup_merge_log.json", "final_catchup_merge_log.json", "late_merge_log.json", "receipt_merge_log.json",
        "postvalidation_merge_log.json", "closure_merge_log.json", "nextwave_merge_log.json", "nextwave_concurrent_merge_log.json",
        "main_advance_merge_log.json", "concurrent_434_merge_log.json", "live_catchup_merge_log.json",
        "main_advance_6e11f7c1_merge_log.json", "quadratic_followup_merge_log.json", "structural_followup_merge_log.json", "balanced_followup_merge_log.json"]
    for name in logs:
        raw = (ROOT / name).read_bytes()
        inputs[str(ROOT / name)] = digest(raw)
        for row in json.loads(raw):
            conflicts.update(row.get("provisional_conflicts", []))
    decisions = {r["path"]: deepcopy(r) for r in prior.get("conflict_decisions", [])}

    def add(row, report):
        row = deepcopy(row)
        assert row["reason"]
        decisions[row["path"]] = {"path": row["path"], "resolution_report": report, "decision": row["reason"]}
        if row["path"] in SELF_RECEIPTS:
            return
        previous = outputs.get(row["path"])
        if previous:
            if previous["sha256"] != row["sha256"]:
                superseded.append({"path": row["path"], "previous_sha256": previous["sha256"], "previous_report": previous["report"],
                    "final_sha256": row["sha256"], "final_report": report, "reason": row["reason"]})
            row["origins"] = previous.get("origins", []) + row.get("origins", [])
        row["report"] = report
        row.setdefault("origins", []).append({k: row[k] for k in ["source_commit", "source_path", "report", "reason"] if k in row})
        outputs[row["path"]] = row

    reports = ["balanced_followup_source_resolution.json", "balanced_followup_docs_resolution.json", "balanced_followup_integration_resolution.json", "balanced_followup_pin_resolution.json"] + args.superseding_report
    for name in reports:
        raw = (ROOT / name).read_bytes()
        inputs[str(ROOT / name)] = digest(raw)
        for row in json.loads(raw)["output_files"]:
            add(row, name)
    claim_path = ROOT / "balanced_followup_output/resolution_report.json"
    inputs[str(claim_path)] = digest(claim_path.read_bytes())
    manifest = deepcopy(prior)
    manifest.update({"assembled_at": datetime.now(timezone.utc).isoformat(), "prior_reviewed_union": BASE,
        "current_main": MAIN, "latest_source": SOURCE, "topic_source_snapshots": 172, "topic_branch_names": 138,
        "outputs": [outputs[p] for p in sorted(outputs)], "covered_conflicts": sorted(conflicts), "superseded_outputs": superseded,
        "inputs": inputs, "method": "Preserve every prior reviewed resolution,612 unchanged claim records and all614 status flags. Apply the exact two authored claim fields and source-exact extended verifier/test/control/proof bytes, with one explicit context README digest repair and exact originals retained."})
    manifest["conflict_decisions"] = [decisions.get(p) or {"path": p, "resolution_report": outputs[p]["report"] if p in outputs else "prior published resolution",
        "decision": outputs[p]["reason"] if p in outputs else "Retain the prior explicit remapping/deletion decision."} for p in sorted(conflicts)]
    for path in conflicts:
        assert path in outputs or path in prior["deletions"] or path in decisions, path
    resolution_path = ROOT / "balanced_followup_resolution_manifest.json"
    write_json(resolution_path, manifest)
    plans = ["catchup_plan.json", "final_catchup_plan.json", "supplemental_catchup_plan.json", "late_catchup_plan.json", "receipt_catchup_plan.json",
        "claims_output/postvalidation_plan.json", "claims_output/closure_plan.json", "nextwave_plan.json", "live_catchup_plan.json", "quadratic_followup_plan.json", "structural_followup_plan.json", "balanced_followup_plan.json"]
    archives = ["archive_tags.json", "archive_update_tags.json", "archive_final_tags.json", "archive_shift_window_tags.json", "archive_late_tags.json",
        "archive_receipt_tags.json", "archive_postvalidation_tags.normalized.json", "archive_closure_tags.normalized.json", "archive_nextwave_tags.normalized.json", "archive_live_catchup_tags.normalized.json", "archive_quadratic_c7.normalized.json", "archive_quadratic_80bd.normalized.json", "archive_quadratic_f006.normalized.json"]
    receipt_path = ROOT / "balanced_followup_preservation_report.json"
    command = [sys.executable, str(ROOT / "claims_output/audit_preservation.py"), "--repo", args.repo, "--commit", args.commit,
        "--snapshot", str(ROOT / "snapshot.json"), "--claims-report", str(claim_path), "--resolutions", str(resolution_path),
        "--conflicts", str(ROOT / "provisional_conflicts.json"), "--output", str(receipt_path)]
    for option, names in [("--catchup", plans), ("--archive-tags", archives), ("--merge-log", logs)]:
        for name in names:
            command += [option, str(ROOT / name)]
    subprocess.run(command, check=True)
    audit = json.loads(receipt_path.read_bytes())
    assert audit["archive_tag_receipts_checked"] == 172 and audit["final_claim_ids"] == 614
    for commit in [MAIN, SOURCE, BASE, "5d1441090e1c3c804d0ba0797a20ec303b5c08d5", "434178af88a16a3d13e9db60dd97453207dbf2b2"]:
        subprocess.run(["git", "-C", args.repo, "merge-base", "--is-ancestor", commit, args.commit], check=True)
    assert git("rev-parse", MAIN + "^{tree}") == git("rev-parse", "9b0bb20a6a891d9d352029d7775d650e065a51ea^{tree}")
    final_ledger = git("show", args.commit + ":research/claims.json")
    assert final_ledger == (ROOT / "balanced_followup_output/claims.json").read_bytes()
    before = {r["id"]: r for r in json.loads(git("show", BASE + ":research/claims.json"))["claims"]}
    after = {r["id"]: r for r in json.loads(final_ledger)["claims"]}
    assert len(before) == len(after) == 614 and set(before) == set(after)
    changed = {cid for cid in before if before[cid] != after[cid]}
    assert changed == {"AI-QUADRATIC-INDEX-DICHOTOMY-002", "AI-QUADRATIC-KERNEL-INDICES-001"}
    source_claims = {r["id"]: r for r in json.loads(git("show", SOURCE + ":research/claims.json"))["claims"]}
    for cid in changed:
        assert after[cid] == source_claims[cid]
        for field in ["status", "evidence", "independent_review", "lean_formalized", "improves_omega"]:
            assert before[cid][field] == after[cid][field]
    pin = json.loads((ROOT / "balanced_followup_pin_resolution.json").read_bytes())
    source_pin = json.loads(git("show", SOURCE + ":research/ai/2026-10-23-quadratic-kernel-indices/sources.json"))
    final_pin = json.loads(git("show", args.commit + ":research/ai/2026-10-23-quadratic-kernel-indices/sources.json"))
    source_pin["local_dependencies"][1]["sha256"] = pin["maintained_pin"]
    assert source_pin == final_pin
    assert digest(git("show", args.commit + ":" + "research/ai/2026-10-20-anisotropic-constructions/README.md")) == pin["maintained_pin"]
    write_json(ROOT / "balanced_followup_history_receipt.json", {"status": "passed", "head": args.commit,
        "current_main": MAIN, "main_tree_equals_already_captured_column_source": True, "current_main_already_ancestor_of_published_baseline": True,
        "new_source_sha": SOURCE, "source_and_main_histories_preserved_as_ancestors": True,
        "topic_source_snapshots": 172, "topic_branch_names": 138, "integration_histories_separate_from_topic_counts": True,
        "claims": 614, "unchanged_records_from171": 612, "added_claim_ids": [], "revised_claim_ids": sorted(changed), "all_status_flags_preserved": True,
        "strict_pin_repair_only": "local_dependencies[1].sha256; both original source and old README retained byte-exact.",
        "source_pin_repair_report": "balanced_followup_pin_resolution.json", "archive_receipt": "archive_quadratic_f006.json",
        "preservation_report_sha256": digest(receipt_path.read_bytes()), "recorded_at": datetime.now(timezone.utc).isoformat()})


if __name__ == "__main__":
    main()

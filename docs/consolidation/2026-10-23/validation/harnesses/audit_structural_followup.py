"""Audit171 archived topic snapshots and the exact main6e reconciliation."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
BASE = "dcd18b0cb9cc00b8a7394f78b36d53c7e35d6b82"
MAIN = "6e11f7c1dfd73ae2d460e43f620a7f982920f043"
SOURCE = "80bd2ae6e1231c5fcd6ea1b01684d49e4b496def"
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

    old = git("show", BASE + ":" + PREFIX + "central_resolution_manifest.json")
    prior_path = ROOT / "structural_followup_output/prior_manifest.dcd18b0c.json"
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
        "main_advance_6e11f7c1_merge_log.json", "quadratic_followup_merge_log.json", "structural_followup_merge_log.json"]
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

    reports = ["structural_followup_source_resolution.json", "structural_followup_docs_resolution.json", "structural_followup_integration_resolution.json", "structural_followup_pin_resolution.json"] + args.superseding_report
    for name in reports:
        raw = (ROOT / name).read_bytes()
        inputs[str(ROOT / name)] = digest(raw)
        for row in json.loads(raw)["output_files"]:
            add(row, name)
    claim_path = ROOT / "structural_followup_output/resolution_report.json"
    inputs[str(claim_path)] = digest(claim_path.read_bytes())
    manifest = deepcopy(prior)
    manifest.update({"assembled_at": datetime.now(timezone.utc).isoformat(), "prior_reviewed_union": BASE,
        "current_main": MAIN, "latest_source": SOURCE, "topic_source_snapshots": 171, "topic_branch_names": 138,
        "outputs": [outputs[p] for p in sorted(outputs)], "covered_conflicts": sorted(conflicts), "superseded_outputs": superseded,
        "inputs": inputs, "method": "Preserve every prior reviewed resolution and all613 previous claim records. Add the exact captured structural dichotomy proof and one written-unreviewed claim; preserve the new external-theorem citation and retain the reviewed context-README digest with byte-exact originals. All imported main code is already present and current main is already an ancestor."})
    manifest["conflict_decisions"] = [decisions.get(p) or {"path": p, "resolution_report": outputs[p]["report"] if p in outputs else "prior published resolution",
        "decision": outputs[p]["reason"] if p in outputs else "Retain the prior explicit remapping/deletion decision."} for p in sorted(conflicts)]
    for path in conflicts:
        assert path in outputs or path in prior["deletions"] or path in decisions, path
    resolution_path = ROOT / "structural_followup_resolution_manifest.json"
    write_json(resolution_path, manifest)
    plans = ["catchup_plan.json", "final_catchup_plan.json", "supplemental_catchup_plan.json", "late_catchup_plan.json", "receipt_catchup_plan.json",
        "claims_output/postvalidation_plan.json", "claims_output/closure_plan.json", "nextwave_plan.json", "live_catchup_plan.json", "quadratic_followup_plan.json", "structural_followup_plan.json"]
    archives = ["archive_tags.json", "archive_update_tags.json", "archive_final_tags.json", "archive_shift_window_tags.json", "archive_late_tags.json",
        "archive_receipt_tags.json", "archive_postvalidation_tags.normalized.json", "archive_closure_tags.normalized.json", "archive_nextwave_tags.normalized.json", "archive_live_catchup_tags.normalized.json", "archive_quadratic_c7.normalized.json", "archive_quadratic_80bd.normalized.json"]
    receipt_path = ROOT / "structural_followup_preservation_report.json"
    command = [sys.executable, str(ROOT / "claims_output/audit_preservation.py"), "--repo", args.repo, "--commit", args.commit,
        "--snapshot", str(ROOT / "snapshot.json"), "--claims-report", str(claim_path), "--resolutions", str(resolution_path),
        "--conflicts", str(ROOT / "provisional_conflicts.json"), "--output", str(receipt_path)]
    for option, names in [("--catchup", plans), ("--archive-tags", archives), ("--merge-log", logs)]:
        for name in names:
            command += [option, str(ROOT / name)]
    subprocess.run(command, check=True)
    audit = json.loads(receipt_path.read_bytes())
    assert audit["archive_tag_receipts_checked"] == 171 and audit["final_claim_ids"] == 614
    for commit in [MAIN, SOURCE, BASE, "5d1441090e1c3c804d0ba0797a20ec303b5c08d5", "434178af88a16a3d13e9db60dd97453207dbf2b2"]:
        subprocess.run(["git", "-C", args.repo, "merge-base", "--is-ancestor", commit, args.commit], check=True)
    assert git("rev-parse", MAIN + "^{tree}") == git("rev-parse", "9b0bb20a6a891d9d352029d7775d650e065a51ea^{tree}")
    final_ledger = git("show", args.commit + ":research/claims.json")
    assert final_ledger == (ROOT / "structural_followup_output/claims.json").read_bytes()
    before = {r["id"]: r for r in json.loads(git("show", BASE + ":research/claims.json"))["claims"]}
    after = {r["id"]: r for r in json.loads(final_ledger)["claims"]}
    assert len(before) == 613 and len(after) == 614
    assert all(after[cid] == row for cid, row in before.items())
    added = set(after) - set(before)
    assert added == {"AI-QUADRATIC-INDEX-DICHOTOMY-002"}
    source_claims = {r["id"]: r for r in json.loads(git("show", SOURCE + ":research/claims.json"))["claims"]}
    assert after[next(iter(added))] == source_claims[next(iter(added))]
    pin = json.loads((ROOT / "structural_followup_pin_resolution.json").read_bytes())
    source_pin = json.loads(git("show", SOURCE + ":research/ai/2026-10-23-quadratic-kernel-indices/sources.json"))
    final_pin = json.loads(git("show", args.commit + ":research/ai/2026-10-23-quadratic-kernel-indices/sources.json"))
    source_pin["local_dependencies"][1]["sha256"] = pin["maintained_pin"]
    assert source_pin == final_pin
    assert digest(git("show", args.commit + ":" + "research/ai/2026-10-20-anisotropic-constructions/README.md")) == pin["maintained_pin"]
    write_json(ROOT / "structural_followup_history_receipt.json", {"status": "passed", "head": args.commit,
        "current_main": MAIN, "main_tree_equals_already_captured_column_source": True, "current_main_already_ancestor_of_published_baseline": True,
        "new_source_sha": SOURCE, "source_and_main_histories_preserved_as_ancestors": True,
        "topic_source_snapshots": 171, "topic_branch_names": 138, "integration_histories_separate_from_topic_counts": True,
        "claims": 614, "unchanged_records_from_dcd": 613, "added_claim_ids": sorted(added), "all_status_flags_preserved": True,
        "strict_pin_repair_only": "local_dependencies[1].sha256; both original source and old README retained byte-exact.",
        "source_pin_repair_report": "structural_followup_pin_resolution.json", "archive_receipt": "archive_quadratic_80bd.json",
        "preservation_report_sha256": digest(receipt_path.read_bytes()), "recorded_at": datetime.now(timezone.utc).isoformat()})


if __name__ == "__main__":
    main()

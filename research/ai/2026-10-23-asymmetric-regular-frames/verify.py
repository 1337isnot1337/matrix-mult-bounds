"""Exact finite frame-budget scan and unit-rank-upgrade controls."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/asymmetric-regular-frames-2026-10-23/controls.json"
PREVIOUS = ROOT / "research/ai/2026-10-23-partial-regular-frames"
SPEC = importlib.util.spec_from_file_location("asymmetric_frames_predecessor", PREVIOUS / "verify.py")
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
require = prior.require


def check_sources(record=None):
    record = json.loads((PACKAGE / "sources.json").read_text()) if record is None else record
    expected = {"research/ai/2026-10-23-partial-regular-frames/proof.md",
                "research/ai/2026-10-23-partial-regular-frames/verify.py",
                "research/ai/2026-10-20-koszul/cyclic_finite_target.md"}
    entries = record["local_dependencies"]
    require(len(entries) == 3 and {x["path"] for x in entries} == expected,
            "Changed dependency inventory")
    for entry in entries:
        require(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest() == entry["sha256"],
                "Changed source: " + entry["path"])
    return len(entries)


def a4_margins(rb, rc):
    require(type(rb) is int and type(rc) is int and 1 <= rb <= 110 and 1 <= rc <= 110,
            "Invalid A4 partial frame dimensions")
    qb, qc, eb, ec = 112-rb, 112-rc, 110-rb, 110-rc
    margins = [16-2*qb-qc, 11-eb-ec-qb, 100-112+16-qc, 100-112+16-qc]
    return {"frame_pair": [rb, rc], "strict_margins": margins,
            "sufficient": all(v > 0 for v in margins)}


def scan():
    records = [a4_margins(rb, rc) for rb in range(1, 111) for rc in range(1, 111)]
    good = [r for r in records if r["sufficient"]]
    pairs = [r["frame_pair"] for r in good]
    minimal = [p for p in pairs if not any(q != p and q[0] <= p[0] and q[1] <= p[1]
                                          for q in pairs)]
    require(len(good) == 9 and minimal == [[106, 110], [107, 109]],
            "Unexpected complete A4 frame-budget frontier")
    return {"registered_range": [[1, 110], [1, 110]], "examined_pairs": len(records),
            "sufficient_pairs": good, "minimal_pairs": minimal,
            "boundary_controls": [a4_margins(106, 109), a4_margins(105, 110),
                                  a4_margins(110, 108)]}


def unit_upgrade_controls():
    t = s.Symbol("t", nonzero=True)
    records = []
    for rc in range(2, 6):
        rb, target, n = rc-1, rc+1, rc+3
        h, j = s.eye(target)[:, :rc], s.eye(target)[:, :rb]
        b = s.eye(n)[:target, :]
        c = b.T
        b[rc, rc] = t
        c[rc, rc] = 1/t
        u = s.eye(n)[:, :rb]
        v = c*h
        require(b*c == s.eye(target) and b*u == j, "Unit/right-frame identity failed")
        require(v == s.eye(n)[:, :rc], "Kept C frame is not regular")
        b0 = b.subs(t, 0)
        require(b0*v == h and b0.rank() == rc > rb, "Unit did not upgrade row rank")
        require(c[rc, rc] == 1/t, "Lost remaining C-pole control")
        records.append({"original_right_frame": rb, "regular_column_frame": rc,
                        "limiting_row_rank": rc, "unit_identity_exact": True,
                        "unselected_column_pole": True,
                        "source_contraction_minima_asserted": False})
    return records


def unit_corank_controls():
    n, target = 10, 8
    c = s.eye(n)[:, :target]
    records = []
    for corank in range(1, 5):
        for outside in range(min(2, corank)+1):
            inside = corank-outside
            killed = list(range(inside)) + list(range(target, target+outside))
            unit = s.eye(n)
            for j in killed:
                unit[j, j] = 0
            image_rank = (unit*c).rank()
            require(n-unit.rank() == corank and image_rank >= target-corank,
                    "Unit-image rank lower bound failed")
            require(image_rank == target-inside, "Alignment example rank incorrect")
            records.append({"unit_corank": corank, "kernel_outside_column_image": outside,
                            "unit_image_rank": image_rank, "uniform_rank_floor": target-corank})
    return records


def report():
    prior.verify(json.loads(prior.RESULT.read_text()))
    return {"scope": "Finite rank-budget frontier and matrix identities; frame existence is assumed.",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "source_pins": check_sources(), "a4_scan": scan(),
            "unit_rank_upgrade_examples": unit_upgrade_controls(),
            "unit_corank_alignment_examples": unit_corank_controls(),
            "regular_unit_image_threshold": 106,
            "uniformly_included_unit_corank": 4,
            "ordinary_rank_floor": 12, "target_small_slice_rank": 11}


def verify(record):
    require(record == report(), "Changed evidence, strict boundary or theorem scope")
    return {"examined_pairs": record["a4_scan"]["examined_pairs"],
            "sufficient_pairs": len(record["a4_scan"]["sufficient_pairs"]),
            "minimal_pairs": record["a4_scan"]["minimal_pairs"],
            "unit_upgrade_controls": len(record["unit_rank_upgrade_examples"]),
            "unit_corank_controls": len(record["unit_corank_alignment_examples"]),
            "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True) + "\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

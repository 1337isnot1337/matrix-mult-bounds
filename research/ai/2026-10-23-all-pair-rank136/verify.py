"""Exact integer acceptance for the balanced A4 every-pair bound136."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT = ROOT / "results/all-pair-rank136-2026-10-23/controls.json"
SOURCE_PATHS = (
    "research/ai/2026-10-23-all-pair-rank144/proof.md",
    "research/ai/2026-10-23-rank84-rank88-spaces/proof.md",
)


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def check_sources(document=None):
    if document is None:
        document = json.loads((HERE / "sources.json").read_text())
    entries = document["local_dependencies"]
    require(tuple(entry["path"] for entry in entries) == SOURCE_PATHS, "changed source inventory")
    for entry in entries:
        path = ROOT / entry["path"]
        require(path.is_file(), "missing source prerequisite")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"], "source digest mismatch")
    return {entry["path"]: entry["sha256"] for entry in entries}


def new_source_cap(rank_ceiling):
    require(type(rank_ceiling) is int and rank_ceiling >= 0, "invalid source rank ceiling")
    if rank_ceiling < 84:
        return 56
    if rank_ceiling < 88:
        return 60
    return 112


def pair_screen(a, b, kind, use_prior=True):
    require(kind in ("mixed", "long"), "unknown target pair")
    maximum_a = 100 if kind == "mixed" else 101
    require(type(a) is int and type(b) is int
            and 0 <= a <= maximum_a and 0 <= b <= 101,
            "rank lies outside the established individual bounds")
    require(type(use_prior) is bool, "invalid prerequisite switch")
    shared, parameter_dimension = (10, 110) if kind == "mixed" else (11, 100)
    delta = 224 - a - b
    lower = parameter_dimension - (a // shared) * (b // shared)
    upper = new_source_cap(delta)
    prior = use_prior and a + b > 144
    return {"ranks": [a, b], "kind": kind, "source_rank_ceiling": delta,
            "kernel_lower": lower, "new_kernel_upper": upper,
            "excluded_by_prior144": prior, "new_kernel_contradiction": lower > upper,
            "excluded": prior or lower > upper}


def rank_pair_controls():
    populations = {
        "mixed": [pair_screen(a, b, "mixed") for a in range(101) for b in range(102)],
        "long": [pair_screen(a, b, "long") for a in range(102) for b in range(102)],
    }
    counts, intervals = {}, []
    for kind, records in populations.items():
        prior = [record for record in records if sum(record["ranks"]) > 144]
        new = [record for record in records if 137 <= sum(record["ranks"]) <= 144]
        require(all(record["excluded_by_prior144"] for record in prior), "prior144 coverage was lost")
        require(all(record["new_kernel_contradiction"] for record in new), "new sum136 exclusion failed")
        require(all(record["excluded"] for record in records if sum(record["ranks"]) > 136),
                "complete sum136 screen failed")
        counts[kind] = {"rank_pairs_checked": len(records), "prior_pairs_above144": len(prior),
                        "new_pairs_of_sum137_through144": len(new),
                        "all_pairs_above136_excluded": len(prior) + len(new)}
        for low, high, cap in ((141, 144, 56), (137, 140, 60)):
            group = [record for record in new if low <= sum(record["ranks"]) <= high]
            lower = min(record["kernel_lower"] for record in group)
            require(all(record["new_kernel_upper"] == cap for record in group), "strict source threshold changed")
            expected_lower = 61 if kind == "mixed" else (58 if low == 141 else 64)
            require(lower == expected_lower and lower > cap, "endpoint kernel margin changed")
            intervals.append({"kind": kind, "sum_interval": [low, high], "cases": len(group),
                              "kernel_lower_minimum": lower, "kernel_upper": cap,
                              "minimum_dimension_gap": lower - cap})
    require(counts == {
        "mixed": {"rank_pairs_checked": 10302, "prior_pairs_above144": 1653,
                  "new_pairs_of_sum137_through144": 492, "all_pairs_above136_excluded": 2145},
        "long": {"rank_pairs_checked": 10404, "prior_pairs_above144": 1711,
                 "new_pairs_of_sum137_through144": 500, "all_pairs_above136_excluded": 2211},
    }, "integer-pair coverage counts changed")
    boundary = [pair_screen(68, 68, "mixed"), pair_screen(68, 68, "long"), pair_screen(100, 36, "mixed")]
    require(all(record["source_rank_ceiling"] == 88 and not record["excluded"] for record in boundary),
            "strict rank88 boundary was improperly excluded")
    retained = {"with_prior": pair_screen(100, 100, "mixed"),
                "new_caps_alone": pair_screen(100, 100, "mixed", use_prior=False)}
    require(retained["with_prior"]["excluded"] and not retained["new_caps_alone"]["excluded"],
            "prior144 necessity control failed")
    require(2 * 204 == 3 * 136 and 100 + 36 == 136, "rank-sum consequence arithmetic failed")
    return {"pair_counts": counts, "interval_margins": intervals,
            "retained_prerequisite_control": retained, "boundary_controls": boundary,
            "boundary_controls_are_constructions": False,
            "every_pair_sum_upper": 136, "all_three_rank_sum_upper": 204,
            "short_rank100_long_rank_upper": 36}


def controls():
    return {"schema": "all-pair-rank136-controls-v1", "source_pins": check_sources(),
            "rank_pair_controls": rank_pair_controls(),
            "claim_scope": {"claim_id": "AI-A4-ALL-PAIR-RANK136-001", "field": "C",
                            "retains_every_pair144_prerequisite": True,
                            "arbitrary_complex_leading_kernels": True,
                            "arbitrary_finite_Laurent_poles": True,
                            "every_balanced_pair_sum_upper": 136,
                            "total_balanced_rank_upper": 204,
                            "short_rank100_long_rank_upper": 36,
                            "necessary_conditions_only": True,
                            "leading_rank_bounds_sharp": False,
                            "matrix_target_constructed": False,
                            "smaller_exponent_established": False,
                            "independent_external_review": False, "formalized": False},
            "acceptance_arithmetic": "integers only; imported source theorems checked by proof hash"}


def replay_saved(document):
    require(document == controls(), "saved evidence or scope differs from exact replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = controls()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report, indent=2) + "\n")
    else:
        require(json.loads(RESULT.read_text()) == report, "saved evidence or scope differs from exact replay")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

"""Finite exact controls for the written two-regular-leg rank frontier."""
from __future__ import annotations

import argparse
import hashlib
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/regular-leg-frontier-2026-10-23/controls.json"
DEPENDENCIES = {
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md",
    "research/ai/2026-10-20-graded-quantum-flags/saturation.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["field"] == "C", "Changed field")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES)
            and {entry["path"] for entry in entries} == DEPENDENCIES,
            "Changed source inventory")
    for entry in entries:
        digest = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(digest == entry["sha256"], "Changed source: " + entry["path"])
    return len(entries)


def indices(a):
    return (list(product(range(a), range(2*a-1), range(a))),
            list(product(range(a), range(a), range(2*a-1))),
            list(product(range(2*a-1), range(a), range(a))))


def compressed_coordinates(a, deleted_rows, deleted_columns):
    """Original six-index tensor; each retained coefficient sees one F entry."""
    first, rows, columns = indices(a)
    require(deleted_rows <= set(rows) and deleted_columns <= set(columns),
            "Invalid coordinate deletion")
    visible = set()
    terms = 0
    for i, j, p, q, r, z in product(range(a), repeat=6):
        if (j, p, r+z) not in deleted_rows and (i+j, q, r) not in deleted_columns:
            visible.add((i, p+q, z))
            terms += 1
    hidden = [list(index) for index in sorted(set(first) - visible)]
    # The supports of distinct first coordinates are disjoint in this model.
    return {"a": a, "source_dimension": len(first),
            "regular_ranks": [len(rows)-len(deleted_rows),
                              len(columns)-len(deleted_columns)],
            "retained_source_terms": terms, "projected_rank": len(visible),
            "kernel_dimension": len(hidden), "hidden_coordinates": hidden}


def compression_controls():
    records = []
    for a in range(2, 7):
        first, rows, columns = indices(a)
        # Every g tensor h_0 is hidden; the bound dim W<=a^2 is attained.
        deleted_rows = {row for row in rows if row[1] == 0}
        deleted_columns = set(columns[-2:]) if a >= 3 else set()
        coherent = compressed_coordinates(a, deleted_rows, deleted_columns)
        require(coherent["hidden_coordinates"] == [[i, 0, z]
                    for i in range(a) for z in range(a)], "Coherent kernel mismatch")
        require(coherent["kernel_dimension"] == a*a, "Wrong coherent kernel rank")
        require(2*len(first)-sum(coherent["regular_ranks"]) < 2*a*a,
                "Coherent example is outside strict threshold")
        coherent["kind"] = "full_coherent_kernel"
        records.append(coherent)

        # Partition the a^2 pivots of F_(0,0,0) between the two deletions.
        pivots = [(j, 0, z) for j in range(a) for z in range(a)]
        cut = len(pivots)//2
        minimal = compressed_coordinates(a, set(pivots[:cut]), set(pivots[cut:]))
        require(minimal["hidden_coordinates"] == [[0, 0, 0]],
                "Minimum-rank kernel mismatch")
        require(2*len(first)-sum(minimal["regular_ranks"]) == a*a,
                "Minimum-rank defect mismatch")
        minimal["kind"] = "single_minimum_slice"
        records.append(minimal)
    return records


def twice_minimum_controls():
    records = []
    for a in range(2, 7):
        # F_(0,0,0)+F_(0,2a-2,0): two disjoint permutation submatrices.
        support = []
        for i, j, p, q, r, z in product(range(a), repeat=6):
            if i == z == 0 and p+q in (0, 2*a-2):
                support.append(((j, p, r+z), (i+j, q, r)))
        require(len(support) == 2*a*a, "Wrong twice-minimum support size")
        require(len({row for row, col in support}) == len(support)
                and len({col for row, col in support}) == len(support),
                "Twice-minimum matrix is not a partial permutation")
        records.append({"a": a, "matrix_rank": len(support),
                        "scalar_hankel_rank": 2, "below_twice_minimum": False})
    return records


def projected_lower_bound(left, right):
    """Only established compression-kernel bounds, with strict thresholds."""
    require(type(left) is int and type(right) is int
            and 0 <= left <= 112 and 0 <= right <= 112, "Invalid map rank")
    defect = 224-left-right
    if defect < 16:
        return 112
    if defect == 16 and left < 112 and right < 112:
        return 111  # Equality has at most one hidden slice if both defects are positive.
    if defect < 32:
        return 96
    return 0


def screen(left, right, kind):
    require(kind in ("long_long", "short_long"), "Unknown rank-pair kind")
    require(0 <= left <= (110 if kind == "long_long" else 100)
            and 0 <= right <= 110, "Rank exceeds target leg")
    beta, third = (11, 100) if kind == "long_long" else (10, 110)
    lower = projected_lower_bound(left, right)
    upper = 112-third+(left//beta)*(right//beta)
    ordinary = left+right > 208
    return {"ranks": [left, right], "projected_lower": lower,
            "target_support_upper": upper,
            "excluded": ordinary or lower > upper,
            "ordinary_regularity_forced": ordinary}


def rank_pair_controls():
    records = {}
    for kind, maximum in (("long_long", 110), ("short_long", 100)):
        cases = [screen(left, right, kind)
                 for left in range(maximum+1) for right in range(111)]
        high = [case for case in cases if sum(case["ranks"]) >= 193]
        survivors = [case["ranks"] for case in high if not case["excluded"]]
        records[kind] = {"rank_pairs_checked": len(cases),
                         "pairs_of_total_rank_at_least_193": len(high),
                         "excluded_high_pairs": sum(case["excluded"] for case in high),
                         "surviving_high_pairs": survivors}
    expected = [[100, q] for q in range(100, 108)] + [[p, 110] for p in range(90, 98)]
    require(records["long_long"]["surviving_high_pairs"] == [],
            "The long-leg rank theorem failed")
    require(sorted(records["short_long"]["surviving_high_pairs"]) == sorted(expected),
            "The mixed frontier changed")
    return records


def report():
    return {"scope": "Finite controls for a written all-order rank frontier over C",
            "proof_status": "proof-written-unreviewed", "independent_review": False,
            "improves_omega": False, "target_constructed": False,
            "coordinate_compressions": compression_controls(),
            "twice_minimum_boundary": twice_minimum_controls(),
            "rank_pair_screen": rank_pair_controls()}


def verify(record):
    check_sources()
    require(record == report(), "Changed finite evidence or scope")
    return {"coordinate_compressions": 10, "twice_minimum_controls": 5,
            "rank_pairs_checked": 23532, "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    check_sources()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2)+"\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), sort_keys=True))


if __name__ == "__main__":
    main()

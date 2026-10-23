"""Exact middle-catalecticant controls for the invertible-leading-first chart.

The universal GL(5) lower bounds are proved in catalecticant_chart.md.
Finite first-basis controls check conventions and are not their proof.
"""
from __future__ import annotations

from itertools import product
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("mixed_catalecticant_base", HERE / "verify.py")
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
RESULTS = BASE.RESULTS
IDENTITY = [[int(i == j) for j in range(5)] for i in range(5)]
EXPECTED = {"S": 12, "F2": 4, "F3": 5, "O33": 5, "O42": 4, "M2": 4}


def full(width, transpose=False):
    b, c = width, width + 4
    entries = [(i, j, i + j) for i in range(5) for j in range(b)]
    if transpose:
        return c, b, [(i, k, j) for i, j, k in entries]
    return b, c, entries


def output_block(d, e):
    if d + e != 6 or min(d, e) < 1:
        raise ValueError("output shape must have positive input lengths summing to six")
    return d, e, [(j + k, j, k) for j in range(d) for k in range(e)]


def rows_for_tensor(b, c, entries, first=IDENTITY):
    """Rows (r,C index), columns (s,B index), coefficient first[r+s,i]."""
    if len(first) != 5 or any(len(row) != 5 for row in first):
        raise ValueError("first map must be 5 by 5")
    rows = [{} for _ in range(3 * c)]
    for entry in entries:
        i, j, k = entry[:3]
        coefficient = entry[3] if len(entry) == 4 else 1
        for r in range(3):
            for s in range(3):
                value = coefficient * first[r + s][i]
                if value:
                    BASE.add(rows[r * c + k], s * b + j, value)
    return 3 * b, rows


def transpose_rows(ncols, rows):
    result = [{} for _ in range(ncols)]
    for i, row in enumerate(rows):
        for j, value in row.items():
            result[j][i] = value
    return len(rows), result


def map_rank(matrix):
    return BASE.rational_rank([{j: value for j, value in enumerate(row) if value}
                               for row in matrix])


def rank_for_tensor(tensor, first=IDENTITY):
    return BASE.rational_rank(rows_for_tensor(*tensor, first=first)[1])


def first_frames():
    return {
        "identity": IDENTITY,
        "reversal": [[int(i + j == 4) for j in range(5)] for i in range(5)],
        "cyclic_permutation": [[int(j == (i + 1) % 5) for j in range(5)] for i in range(5)],
        "distinct_diagonal": [[(1, 2, 3, 5, 7)[i] if i == j else 0
                                for j in range(5)] for i in range(5)],
        "upper_unipotent": [[1 if i == j else (i + j + 1 if i < j else 0)
                              for j in range(5)] for i in range(5)],
        "evaluation_vandermonde": [[i ** j for j in range(5)] for i in range(5)],
    }


def quadratic_map(q):
    """L_q:A5 -> V3; its transpose is polynomial multiplication by q."""
    if len(q) != 3:
        raise ValueError("quadratic coefficient vector must have length three")
    rows = []
    for r in range(3):
        rows.append({r + s: value for s, value in enumerate(q) if value})
    return rows


def report():
    discovery = hashlib.sha256((HERE / "discovery_input.json").read_bytes()).hexdigest()
    if discovery != "c53abefde0cb5d5e2e816f96ae6c257ee843f59e6c28d13a6ae1994de9ab88f3":
        raise ValueError("frozen candidate changed")
    canonical = {name: rank_for_tensor(BASE.block(name)) for name in BASE.NAMES}
    if canonical != EXPECTED:
        raise ValueError("canonical middle-catalecticant ranks changed")
    source = 10 * canonical["S"]
    target = sum(count * canonical[name] for name, count in BASE.COUNTS.items())
    if (source, target) != (120, 130):
        raise ValueError("candidate catalecticant totals changed")

    width_controls = []
    for width in range(1, 13):
        rank = rank_for_tensor(full(width))
        if rank != width + 2:
            raise ValueError("canonical Full rank formula failed")
        width_controls.append({"type": "Full", "width": width, "rank": rank})
    for width in range(1, 9):
        rank = rank_for_tensor(full(width, True))
        if rank != width + 2:
            raise ValueError("canonical Mid rank formula failed")
        width_controls.append({"type": "Mid", "width": width, "rank": rank})
        if rows_for_tensor(*full(width, True)) != transpose_rows(*rows_for_tensor(*full(width))):
            raise ValueError("literal Full/Mid transpose identity failed")
    for d in range(1, 6):
        e = 6 - d
        rank = rank_for_tensor(output_block(d, e))
        if rank != min(d, e) + 2:
            raise ValueError("canonical shared-output rank formula failed")
        width_controls.append({"type": "SharedOutput", "d": d, "e": e, "rank": rank})

    frame_controls = []
    for name, frame in first_frames().items():
        if map_rank(frame) != 5:
            raise ValueError("first-frame control is singular")
        ranks = {block: rank_for_tensor(BASE.block(block), frame) for block in BASE.NAMES}
        if any(ranks[block] < EXPECTED[block] for block in BASE.NAMES):
            raise ValueError("first-frame control violates a proved block lower bound")
        frame_controls.append({"name": name, "matrix": frame, "ranks": ranks,
                               "target_rank": sum(BASE.COUNTS[block] * ranks[block]
                                                  for block in BASE.COUNTS)})

    quadratic_controls = []
    for q in product((-1, 0, 1), repeat=3):
        if not any(q):
            continue
        rank = BASE.rational_rank(quadratic_map(q))
        if rank != 3:
            raise ValueError("nonzero quadratic contraction is not surjective")
        quadratic_controls.append({"coefficients": list(q), "rank": rank})

    singular = [[int(i == j == 0) for j in range(5)] for i in range(5)]
    singular_ranks = {name: rank_for_tensor(BASE.block(name), singular) for name in BASE.NAMES}
    singular_target = sum(BASE.COUNTS[name] * singular_ranks[name] for name in BASE.COUNTS)
    if singular_target != 62:
        raise ValueError("singular-first scope diagnostic changed")

    return {
        "status": "Universal target lower bound and invertible-leading-first chart obstruction; singular charts unresolved",
        "field": "complex",
        "discovery_sha256": discovery,
        "matrix_convention": "Rows (r,C index), columns (s,B index); block T_(r+s), r,s=0,1,2",
        "canonical_block_ranks": canonical,
        "source_rank": source,
        "target_universal_lower_bound": target,
        "rank_gap": target - source,
        "target_scope": "Arbitrary independent invertible first identifications for every target block",
        "source_scope": "Ten Full(5,10) blocks with one common canonical first basis",
        "universal_proof": "catalecticant_chart.md, using PAR04 product-vector avoidance and polynomial multiplication",
        "width_and_output_controls": width_controls,
        "first_frame_controls": frame_controls,
        "quadratic_contraction_controls": quadratic_controls,
        "singular_first_projection_diagnostic": {"matrix": singular, "target_rank": singular_target,
            "meaning": "The rank-130 lower bound requires invertible first identifications; this is not a degeneration construction"},
        "excluded_chart": "A Laurent first map whose scalar-normalized nonzero leading matrix is invertible",
        "necessary_leading_first_rank_range": [1, 4],
        "arbitrary_singular_first_maps_excluded": False,
        "degeneration_constructed": False,
        "improved_exponent_established": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RESULTS / "catalecticant_verification.json")
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"source_rank": result["source_rank"],
                      "target_universal_lower_bound": result["target_universal_lower_bound"],
                      "necessary_leading_first_rank_range": [1, 4],
                      "output": str(args.output)}, indent=2))

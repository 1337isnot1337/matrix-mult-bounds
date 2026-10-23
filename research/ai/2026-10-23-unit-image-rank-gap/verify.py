"""Finite exact controls for the written low-rank-locus Laurent argument."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import random

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/unit-image-rank-gap-2026-10-23/controls.json"
BASE = "1c04903c215f396150605c0778024e856ec0b0d4"
DEPENDENCIES = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md",
    "research/ai/2026-10-23-regular-unit-image/proof.md",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == BASE, "Changed source baseline")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES) and
            {e["path"] for e in entries} == set(DEPENDENCIES),
            "Changed dependency inventory")
    for entry in entries:
        digest = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(digest == entry["sha256"], "Source digest mismatch: " + entry["path"])
    return len(entries)


def rank_preserving_retraction(h, y):
    """Construct P with PH=I and rank(PY)=rank(Y), using exact row spaces."""
    total, retained = h.shape
    require(h.rank() == retained and y.rows == total and y.cols <= retained,
            "Invalid retraction dimensions or inclusion")
    frame = h
    for j in range(total):
        candidate = frame.row_join(s.eye(total)[:, j])
        if candidate.rank() > frame.cols:
            frame = candidate
        if frame.cols == total:
            break
    inverse = frame.inv()
    coordinates = inverse*y
    top, bottom = coordinates[:retained, :], coordinates[retained:, :]
    pivots = top.T.rref()[1]
    rows = [s.eye(retained)[j, :] for j in pivots]
    rows += [v.T for v in top.T.nullspace()]
    operations = s.Matrix.vstack(*rows)
    transformed = operations*top
    span = transformed[:len(pivots), :]
    additions = s.zeros(retained, total-retained)
    next_row = len(pivots)
    for j in range(bottom.rows):
        candidate = span.col_join(bottom[j, :])
        if candidate.rank() > span.rows:
            additions[next_row, j] = 1
            span = candidate
            next_row += 1
    p = s.eye(retained).row_join(operations.inv()*additions)*inverse
    require(p*h == s.eye(retained), "Constructed map is not a left inverse")
    require((p*y).rank() == y.rank(), "Constructed retraction loses rank")
    return p


def margins(a, m, n, retained):
    require(all(type(v) is int and v > 0 for v in (a, m, n, retained)) and a >= 2,
            "Invalid positive dimensions")
    source, target = a*a*(2*a-1), m*n
    require(retained <= target <= source, "Invalid retained unit image")
    e, q, k = target-retained, source-retained, source-target
    gaps = {"first_pole": a*a-3*q, "injectivity": n-e-q,
            "rank_locus": 2*a*a-n-3*q, "parameter_dimension": m*m-a*a}
    regular = all(value > 0 for value in gaps.values())
    return {"retained": retained, "target_defect": e, "source_defect": q,
            "strict_margins": gaps, "forces_regularity": regular,
            "ordinary_rank_floor": a*a-2*k, "target_rank_one": n,
            "excludes_target": regular and n < a*a-2*k}


def retraction_controls():
    rng = random.Random(20261023)
    records = []
    for retained in range(1, 5):
        for extra in range(4):
            total = retained+extra
            # Non-coordinate inclusions, rank-deficient Y, and Y=0 are included.
            frame = s.eye(total)
            for j in range(total-1):
                frame[j+1, :] += (j+1)*frame[j, :]
            h = frame[:, :retained]
            for requested in range(retained+1):
                coefficients = s.Matrix(total, requested,
                                        lambda i, j: rng.randrange(-2, 3))
                y = coefficients.row_join(s.zeros(total, retained-requested))
                p = rank_preserving_retraction(h, y)
                records.append({"retained": retained, "extra": extra,
                                "requested_columns": requested,
                                "input_rank": y.rank(), "output_rank": (p*y).rank()})
    return records


def hidden_rank_control():
    retained, extra = 8, 3
    h = s.eye(retained+extra)[:, :retained]
    y = s.zeros(retained+extra, retained)
    for j in range(5):
        y[j, j] = 1
    for j in range(3):
        y[retained+j, 5+j] = 1
    p = rank_preserving_retraction(h, y)
    require((h.T*y).rank() == 5 and (p*y).rank() == 8,
            "Fixed projection no longer demonstrates the lost rank")
    return {"retained": retained, "extra": extra, "input_rank": 8,
            "fixed_projection_rank": 5, "constructed_retraction_rank": 8}


def source_matrix(a, coefficients):
    """Reconstruct the literal cyclic coefficients, without a pilot import."""
    middle = 2*a-1
    index = [(j, p, ell) for j in range(a) for p in range(a) for ell in range(middle)]
    columns = [(height, q, r) for height in range(middle) for q in range(a) for r in range(a)]
    return s.Matrix([[coefficients.get((height-j, p+q, ell-r), 0)
                      for height, q, r in columns] for j, p, ell in index])


def source_controls():
    records = []
    for a in (2, 3, 4):
        middle = 2*a-1
        for label, g, h in (
            ("minimum", {(0, 0): 1}, [1]+[0]*(middle-1)),
            ("coherent_mixed_outer", {(i, i): 1 for i in range(a)},
             [2**k for k in range(middle)]),
            ("sharp_two_coherent_factors", {(0, 0): 1},
             [1]+[0]*(middle-2)+[1]),
        ):
            f = {(i, k, j): value*h[k] for (i, j), value in g.items()
                 for k in range(middle)}
            rank = source_matrix(a, f).to_DM().rank()
            if label == "minimum":
                require(rank == a*a, "Wrong minimum-rank source control")
            elif label == "coherent_mixed_outer":
                require(a*a <= rank < 2*a*a, "Coherent slice left the low-rank locus")
            else:
                require(rank == 2*a*a, "The strict rank-locus boundary moved")
            records.append({"a": a, "case": label, "exact_rank": rank,
                            "strict_locus_threshold": 2*a*a})
    return records


def report():
    cases = [margins(4, 10, 11, r) for r in (110, 109, 108, 107, 106)]
    require([c["excludes_target"] for c in cases] == [True]*4+[False],
            "Changed the written rank107 boundary")
    return {"scope": "Finite exact controls; no formal Laurent proof or exponent gain.",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "source_pin_count": check_sources(), "a4_rank_margins": cases,
            "retraction_controls": retraction_controls(),
            "hidden_rank_control": hidden_rank_control(), "source_controls": source_controls()}


def verify(record):
    require(record == report(), "Changed evidence, mathematical scope or strict margins")
    return {"retractions": len(record["retraction_controls"]),
            "source_matrices": len(record["source_controls"]),
            "a4_rank_cases": len(record["a4_rank_margins"]),
            "lowest_excluded_unit_image_rank": 107, "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True)+"\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

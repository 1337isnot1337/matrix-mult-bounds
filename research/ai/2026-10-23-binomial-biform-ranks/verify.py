"""Exact binomial rank witnesses: full minors and entry-cover upper bounds."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/binomial-biform-ranks-2026-10-23/controls.json"
BASE = "3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93"
SOURCES = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    entries = record["source_references"]
    require(record["base_commit"] == BASE and record["imported_theorems"] == [],
            "Changed source baseline or elementary-proof scope")
    require(len(entries) == len(SOURCES) and {e["path"] for e in entries} == set(SOURCES),
            "Changed source inventory")
    for entry in entries:
        actual = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(actual == entry["sha256"], "Source digest mismatch: " + entry["path"])
    return len(entries)


def residue_lengths(a, step):
    require(type(a) is int and type(step) is int and 1 <= step < a,
            "Offsets must be positive and smaller than the source size")
    return [len(range(i, a, step)) for i in range(step)]


def rank_formula(a, u, v):
    left, right = residue_lengths(a, u), residue_lengths(a, v)
    return a*a + sum(min(n, m) for n in left for m in right)


def literal_matrix(a, u, v, orientation, alpha=1, beta=1):
    residue_lengths(a, u)
    residue_lengths(a, v)
    require(orientation in (0, 1) and alpha != 0 and beta != 0,
            "Two nonzero coefficients and a valid orientation are required")
    coefficients = {(0, 0): alpha, (u, v): beta} if orientation == 0 else {
        (u, 0): alpha, (0, v): beta}
    middle = 2*a-1
    return s.Matrix([[coefficients.get((height-j, ell-r), 0)
                      for height in range(middle) for r in range(a)]
                     for j in range(a) for ell in range(middle)])


def entry_cover(a, u, v):
    """Take the smaller side of each literal residue block."""
    rows, cols = set(), set()
    middle = 2*a-1
    for i, n in enumerate(residue_lengths(a, u)):
        for j, m in enumerate(residue_lengths(a, v)):
            if n <= m:
                rows.update((i+k*u)*middle+j+ell*v
                            for k in range(n) for ell in range(m+1))
            else:
                cols.update((i+height*u)*a+j+r*v
                            for height in range(n+1) for r in range(m))
    require(len(rows)+len(cols) == rank_formula(a, u, v), "Cover has the wrong size")
    return sorted(rows), sorted(cols)


def case_formats():
    cases = [(a, u, v, orientation) for a in range(2, 7)
             for u in range(1, a) for v in range(1, a) for orientation in range(2)]
    cases += [(7, d, d, orientation) for d in (2, 3) for orientation in range(2)]
    return cases


def discover_case(a, u, v, orientation):
    matrix = literal_matrix(a, u, v, orientation)
    expected = rank_formula(a, u, v)
    # Discovery uses exact row reduction. Acceptance independently checks
    # the exported determinant and cover, without replaying this selection.
    columns = list(matrix.to_DM().rref()[1])
    rows = list(matrix.extract(range(matrix.rows), columns).T.to_DM().rref()[1])
    require(len(rows) == len(columns) == expected, "Exact discovery rank disagrees with formula")
    determinant = int(matrix.extract(rows, columns).to_DM().det())
    require(abs(determinant) == 1, "Discovered minor is not unimodular")
    cover_rows, cover_cols = entry_cover(a, u, v)
    return {"a": a, "u": u, "v": v, "orientation": orientation,
            "exact_rank": expected, "minor_rows": rows, "minor_columns": columns,
            "minor_determinant": determinant, "cover_rows": cover_rows,
            "cover_columns": cover_cols}


def verify_case(record):
    a, u, v, orientation = (record[k] for k in ("a", "u", "v", "orientation"))
    matrix = literal_matrix(a, u, v, orientation)
    expected = rank_formula(a, u, v)
    require(record["exact_rank"] == expected, "Changed exact rank")
    rows, cols = record["minor_rows"], record["minor_columns"]
    require(len(rows) == len(set(rows)) == len(cols) == len(set(cols)) == expected,
            "Wrong minor dimension or repeated index")
    cover_rows, cover_cols = record["cover_rows"], record["cover_columns"]
    require(len(cover_rows) == len(set(cover_rows)) and len(cover_cols) == len(set(cover_cols)),
            "Repeated cover index")
    require(all(type(i) is int and 0 <= i < matrix.rows
                for i in rows+cols+cover_rows+cover_cols), "Invalid matrix index")
    require(len(cover_rows)+len(cover_cols) == expected, "Wrong exact upper-cover size")
    chosen_rows, chosen_cols = set(cover_rows), set(cover_cols)
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            require(matrix[i, j] == 0 or i in chosen_rows or j in chosen_cols,
                    "A literal coefficient is not covered")
    determinant = int(matrix.extract(rows, cols).to_DM().det())
    require(determinant == record["minor_determinant"] and abs(determinant) == 1,
            "Corrupt exact lower minor")


def arithmetic_controls():
    gap_cases = diagonal_cases = 0
    for a in range(2, 31):
        for u in range(1, a):
            for v in range(1, a):
                require(rank_formula(a, u, v) >= a*a+a, "Binomial lower gap failed")
                gap_cases += 1
            quotient, remainder = divmod(a, u)
            expected = a*a+quotient*u*u+remainder*remainder
            require(rank_formula(a, u, u) == expected == a*a+a*u-remainder*(u-remainder),
                    "Quotient/remainder rank identity failed")
            diagonal_cases += 1
    examples = [{"a": a, "offset": d, "exact_rank": rank_formula(a, d, d),
                 "naive_threshold": a*(a+d), "deficit": (a % d)*(d-a % d)}
                for a, d in ((4, 2), (5, 2), (5, 3), (7, 2), (7, 3))]
    return {"size_range": [2, 30], "lower_gap_cases": gap_cases,
            "quotient_remainder_cases": diagonal_cases, "examples": examples}


def report():
    return {"scope": "Finite integer minor/cover certificates supporting an all-size written proof.",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "theorem_field_scope": "Every field, with both binomial coefficients nonzero.",
            "finite_coefficient_scope": "Integer unit coefficients; unimodular minors transfer to every field.",
            "source_reference_count": check_sources(),
            "cases": [discover_case(*case) for case in case_formats()],
            "arithmetic_controls": arithmetic_controls()}


def verify(record):
    require(record["scope"] == "Finite integer minor/cover certificates supporting an all-size written proof."
            and record["proof_status"] == "proof-written-unreviewed"
            and record["improves_omega"] is False, "Changed proof scope")
    require(record["theorem_field_scope"] == "Every field, with both binomial coefficients nonzero."
            and record["finite_coefficient_scope"] ==
            "Integer unit coefficients; unimodular minors transfer to every field.",
            "Changed field or finite-control scope")
    require(record["source_reference_count"] == check_sources(), "Changed source reference count")
    require([(r["a"], r["u"], r["v"], r["orientation"]) for r in record["cases"]] == case_formats(),
            "Changed exact coverage inventory")
    for case in record["cases"]:
        verify_case(case)
    require(record["arithmetic_controls"] == arithmetic_controls(), "Changed arithmetic scope")
    return {"exact_minor_cover_cases": len(record["cases"]),
            "lower_gap_cases": record["arithmetic_controls"]["lower_gap_cases"],
            "quotient_remainder_cases": record["arithmetic_controls"]["quotient_remainder_cases"],
            "improves_omega": False}


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

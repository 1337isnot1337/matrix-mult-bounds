"""Exact finite minors, divisor cycles and literal residue-block controls."""
from __future__ import annotations

import argparse
import hashlib
from itertools import combinations, product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/divisor-source-caps-2026-10-23/controls.json"
BASE = "3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93"
DEPENDENCIES = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    entries = record["local_dependencies"]
    require(record["base_commit"] == BASE, "Changed source baseline")
    require(len(entries) == len(DEPENDENCIES) and
            {entry["path"] for entry in entries} == set(DEPENDENCIES),
            "Changed dependency inventory")
    for entry in entries:
        digest = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(digest == entry["sha256"], "Source digest mismatch: " + entry["path"])
    require(record["field"] == "C" and record["inherited_external_input"] ==
            "P1 bundle splitting in the pinned biform block lemma; its original credit and review status are retained.",
            "Changed field or inherited dependency")
    return len(entries)


def biform_entries(a, coordinates):
    """Literal entries of R_a, keyed by (j,L,H,r); no rank theorem used."""
    entries = {}
    for i, ell in coordinates:
        for j, r in product(range(a), repeat=2):
            key = (j, ell+r, i+j, r)
            entries[key] = entries.get(key, 0)+1
    return entries


def matrix(a, coordinates):
    middle = 2*a-1
    rows = [(j, ell) for j in range(a) for ell in range(middle)]
    cols = [(height, r) for height in range(middle) for r in range(a)]
    entries = biform_entries(a, coordinates)
    return [[entries.get((j, ell, height, r), 0) for height, r in cols]
            for j, ell in rows]


def coordinates(alpha, beta, orientation):
    return [(0, 0), (alpha, beta)] if orientation == 0 else [(alpha, 0), (0, beta)]


def bareiss_determinant(values):
    """Independent exact integer determinant for the exported square minors."""
    n = len(values)
    require(all(len(row) == n for row in values), "Nonsquare minor")
    if n == 0:
        return 1
    data = [row[:] for row in values]
    sign, previous = 1, 1
    for k in range(n-1):
        pivot_row = next((i for i in range(k, n) if data[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            data[k], data[pivot_row] = data[pivot_row], data[k]
            sign = -sign
        pivot = data[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = pivot*data[i][j]-data[i][k]*data[k][j]
                require(numerator % previous == 0, "Bareiss exact division failed")
                data[i][j] = numerator//previous
            data[i][k] = 0
        previous = pivot
    return sign*data[-1][-1]


def discover_unit_minor(values, size):
    """Discovery only: unit-pivot elimination in a two-monomial forest matrix."""
    data = [row[:] for row in values]
    original_rows = list(range(len(data)))
    selected_rows, selected_cols = [], []
    rank = 0
    for col in range(len(data[0])):
        pivot_row = next((i for i in range(rank, len(data)) if data[i][col]), None)
        if pivot_row is None:
            continue
        data[rank], data[pivot_row] = data[pivot_row], data[rank]
        original_rows[rank], original_rows[pivot_row] = original_rows[pivot_row], original_rows[rank]
        pivot = data[rank][col]
        require(abs(pivot) == 1, "Discovery encountered a nonunit pivot")
        for i in range(rank+1, len(data)):
            coefficient = data[i][col]//pivot
            if coefficient:
                data[i] = [x-coefficient*y for x, y in zip(data[i], data[rank])]
        selected_rows.append(original_rows[rank])
        selected_cols.append(col)
        rank += 1
        if rank == size:
            return selected_rows, selected_cols
    raise ValueError("Required minor was not found")


def minor_controls():
    records = []
    for p in range(2, 7):
        for alpha, beta, orientation in product(range(1, p), range(1, p), range(2)):
            values = matrix(p, coordinates(alpha, beta, orientation))
            rows, cols = discover_unit_minor(values, p*p+p)
            determinant = bareiss_determinant([[values[i][j] for j in cols] for i in rows])
            require(abs(determinant) == 1, "Two-monomial minor is not unimodular")
            records.append({"p": p, "alpha": alpha, "beta": beta,
                            "orientation": orientation, "rows": rows, "columns": cols,
                            "determinant": determinant})
    return records


def residue_controls():
    records = []
    for p in range(2, 7):
        for d in range(1, 4):
            a = p*d
            for alpha, beta, orientation in product(range(1, p), range(1, p), range(2)):
                base = biform_entries(p, coordinates(alpha, beta, orientation))
                scaled = biform_entries(a, [(d*i, d*j) for i, j in
                                            coordinates(alpha, beta, orientation)])
                observed = {}
                for (j, ell, height, r), value in scaled.items():
                    require(j % d == height % d and ell % d == r % d,
                            "Off-residue matrix entry")
                    key = (j % d, r % d, j//d, ell//d, height//d, r//d)
                    observed[key] = value
                expected = {(u, v, *key): value for u, v in product(range(d), repeat=2)
                            for key, value in base.items()}
                require(observed == expected, "Literal residue-block identity failed")
                records.append({"p": p, "d": d, "alpha": alpha, "beta": beta,
                                "orientation": orientation, "blocks": d*d,
                                "literal_entries": len(scaled)})
    return records


def divisor_controls():
    records = []
    for a in range(2, 25):
        for d in range(1, a):
            if a % d:
                continue
            unseen = set(product(range(a), repeat=2))
            orbits = []
            while unseen:
                start = min(unseen)
                orbit = []
                point = start
                while point not in orbit:
                    orbit.append(point)
                    unseen.remove(point)
                    point = ((point[0]+d) % a, (point[1]+d) % a)
                require(point == start and len(orbit) == a//d, "Wrong divisor orbit")
                for (i, j), (k, ell) in combinations(orbit, 2):
                    require(i != k and j != ell and (i-k) % d == (j-ell) % d == 0,
                            "A cycle pair is not a nonseparable rescaled biform")
                orbits.append(orbit)
            require(len(orbits) == a*d, "Wrong dimension cap")
            strip_columns = {(i+j, r) for i in range(d)
                             for j, r in product(range(a), repeat=2)}
            require(len(strip_columns) == a*(a+d-1), "Wrong sharp strip support")
            records.append({"a": a, "d": d, "p": a//d, "dimension_cap": a*d,
                            "sharp_ceiling_min": a*(a+d-1),
                            "strict_ceiling_max": a*(a+d)-1,
                            "orbit_count": len(orbits), "strip_columns": len(strip_columns)})
    return records


def a4_corollary():
    return [{"target_corank": c, "first_rank_margin": 24-(11+4+c),
             "active_ruling_margin": 16-6-c, "ruling_dimension": 10,
             "source_dimension_cap": 8, "excluded": c <= 8} for c in range(10)]


def nondivisor_control():
    values = matrix(5, [(0, 0), (2, 2)])
    active_rows = [i for i, row in enumerate(values) if any(row)]
    active_cols = [j for j in range(len(values)) if any(row[j] for row in values)]
    rows, cols = discover_unit_minor(values, 34)
    record = {"a": 5, "d": 2, "coordinates": [[0, 0], [2, 2]],
              "exact_rank": 34, "naive_divisor_threshold": 35,
              "active_rows": active_rows, "active_columns": active_cols,
              "active_determinant": bareiss_determinant(
                  [[values[i][j] for j in active_cols] for i in active_rows]),
              "minor_rows": rows, "minor_columns": cols,
              "minor_determinant": bareiss_determinant(
                  [[values[i][j] for j in cols] for i in rows])}
    verify_nondivisor_control(record)
    return record


def verify_nondivisor_control(record):
    require((record["a"], record["d"], record["coordinates"], record["exact_rank"],
             record["naive_divisor_threshold"]) == (5, 2, [[0, 0], [2, 2]], 34, 35),
            "Changed nondivisor scope")
    values = matrix(5, [(0, 0), (2, 2)])
    active_rows = [i for i, row in enumerate(values) if any(row)]
    active_cols = [j for j in range(len(values)) if any(row[j] for row in values)]
    require(record["active_rows"] == active_rows and record["active_columns"] == active_cols
            and len(active_rows) == len(active_cols) == 35, "Wrong active nondivisor matrix")
    upper = bareiss_determinant([[values[i][j] for j in active_cols] for i in active_rows])
    require(upper == record["active_determinant"] == 0, "Wrong exact rank upper bound")
    rows, cols = record["minor_rows"], record["minor_columns"]
    require(len(rows) == len(set(rows)) == len(cols) == len(set(cols)) == 34,
            "Wrong nondivisor lower minor")
    require(all(type(i) is int and 0 <= i < len(values) for i in rows+cols),
            "Invalid nondivisor minor index")
    lower = bareiss_determinant([[values[i][j] for j in cols] for i in rows])
    require(lower == record["minor_determinant"] and abs(lower) == 1,
            "Wrong exact rank lower bound")


def report():
    return {"scope": "Finite exact controls; the all-size theorem is written and unreviewed.",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "source_pin_count": check_sources(), "base_minors": minor_controls(),
            "residue_blocks": residue_controls(), "divisor_strips": divisor_controls(),
            "a4_corollary": a4_corollary(), "nondivisor_boundary": nondivisor_control()}


def verify(record):
    require(record["scope"] == "Finite exact controls; the all-size theorem is written and unreviewed."
            and record["proof_status"] == "proof-written-unreviewed"
            and record["improves_omega"] is False, "Changed mathematical scope")
    require(record["source_pin_count"] == check_sources(), "Changed source count")
    formats = [(p, alpha, beta, orientation) for p in range(2, 7)
               for alpha, beta, orientation in product(range(1, p), range(1, p), range(2))]
    require([(r["p"], r["alpha"], r["beta"], r["orientation"])
             for r in record["base_minors"]] == formats, "Changed minor inventory")
    for entry in record["base_minors"]:
        p = entry["p"]
        values = matrix(p, coordinates(entry["alpha"], entry["beta"], entry["orientation"]))
        rows, cols = entry["rows"], entry["columns"]
        size = p*p+p
        require(len(rows) == len(set(rows)) == len(cols) == len(set(cols)) == size,
                "Wrong minor size or repeated indices")
        require(all(type(i) is int and 0 <= i < len(values) for i in rows+cols),
                "Invalid minor index")
        actual = bareiss_determinant([[values[i][j] for j in cols] for i in rows])
        require(actual == entry["determinant"] and abs(actual) == 1, "Corrupt exact minor")
    require(record["residue_blocks"] == residue_controls(), "Changed residue certificate")
    require(record["divisor_strips"] == divisor_controls(), "Changed divisor or strip control")
    require(record["a4_corollary"] == a4_corollary(), "Changed inherited A4 cutoff")
    verify_nondivisor_control(record["nondivisor_boundary"])
    return {"base_minors": len(formats), "residue_blocks": len(record["residue_blocks"]),
            "divisor_strips": len(record["divisor_strips"]), "a4_cases": 10,
            "nondivisor_boundaries": 1, "improves_omega": False}


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

#!/usr/bin/env python3
"""Exact complete-grid shape certificate and fixed-grid local controls.

Only standard-library integer and rational arithmetic is used. The finite
checks are controls for the written all-dimension arguments in proof.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent


def shape_row(a: int, b: int, c: int) -> dict:
    if any(type(value) is not int or value < 0 for value in (a, b, c)):
        raise ValueError("Part sizes must be nonnegative integers")
    d = a + b + c
    if not d:
        raise ValueError("The coordinate count must be positive")
    capacities = [comb(d, value) for value in (a, b, c)]
    edges = comb(d, a) * comb(d - a, b)
    degrees = [edges // value for value in capacities]
    if any(value * degree != edges for value, degree in zip(capacities, degrees)):
        raise ValueError("Nonintegral full-hypergraph degree")
    incidence_cap = 2 * edges // (sum(degrees) - 1)
    cap = min(*capacities, incidence_cap)
    left = cap**4 * 3**(3*d)
    right = 4**(4*d)
    return {"shape": [a, b, c], "coordinate_count": d,
            "vertex_capacities": capacities, "edges": edges,
            "vertex_degrees": degrees, "incidence_cap": incidence_cap,
            "product_cap": cap, "cap_fourth_times_3_power_3d": left,
            "4_power_4d": right, "strict_integer_margin": right - left,
            "excluded_by_complete_grid_budget": left < right}


def shape_certificate() -> dict:
    rows = []
    summaries = []
    for d in range(1, 34):
        current = [shape_row(a, b, d - a - b)
                   for a in range(d // 3 + 1)
                   for b in range(a, (d - a) // 2 + 1)]
        rows.extend(current)
        largest = max(row["product_cap"] for row in current)
        summaries.append({"coordinate_count": d, "shapes_checked": len(current),
                          "maximum_product_cap": largest,
                          "maximizing_shapes": [row["shape"] for row in current
                                                if row["product_cap"] == largest],
                          "all_shapes_excluded": all(row["excluded_by_complete_grid_budget"]
                                                     for row in current)})
    return {"scope": "Fixed ordered cardinality shape; complete leading grid; not actual tensor rank",
            "field_for_uniform_identity": "characteristic zero",
            "shape_rows": rows, "coordinate_summaries": summaries,
            "all_shapes_excluded_through_d": 32,
            "first_included_non_exclusion_control_d": 33,
            "independent_review": False, "improves_omega": False}


def verify_certificate(saved: dict) -> dict:
    actual = shape_certificate()
    if saved != actual:
        raise ValueError("Saved complete shape certificate differs from exact recomputation")
    summaries = actual["coordinate_summaries"]
    if [row["all_shapes_excluded"] for row in summaries] != [True]*32 + [False]:
        raise ValueError("The stated dimension boundary is not certified")
    return {"accepted": True, "shapes_checked": len(actual["shape_rows"]),
            "excluded_coordinate_counts": list(range(1, 33)),
            "d33_non_exclusion_shape": [11, 11, 11]}


def dual_matrices(q: int, columns: int | None = None):
    if q < 2 or (columns is not None and not 1 <= columns < q):
        raise ValueError("Need q>=2 and 1<=columns<q")
    m = q - 1 if columns is None else columns
    e = [[Fraction(int(i == j) if i < q-1 else -1) for j in range(m)]
         for i in range(q)]
    d = [[Fraction(int(i == j)) - Fraction(1, q) if i < q-1
          else -Fraction(1, q) for j in range(m)] for i in range(q)]
    return e, d


def rational_rank(matrix) -> int:
    rows = [[Fraction(x) for x in row] for row in matrix]
    pivot = 0
    for column in range(len(rows[0]) if rows else 0):
        found = next((i for i in range(pivot, len(rows)) if rows[i][column]), None)
        if found is None:
            continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        scale = rows[pivot][column]
        rows[pivot] = [x / scale for x in rows[pivot]]
        for i in range(pivot + 1, len(rows)):
            scale = rows[i][column]
            if scale:
                rows[i] = [x - scale*y for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def local_control(q: int, columns: int | None = None) -> dict:
    e, d = dual_matrices(q, columns)
    m = len(e[0])
    centered = all(sum(row[j] for row in matrix) == 0
                   for matrix in (e, d) for j in range(m))
    dual = all(sum(e[i][j]*d[i][k] for i in range(q)) == int(j == k)
               for j in range(m) for k in range(m))
    pair_rows = [[e[i][j]*d[i][k] for j in range(m) for k in range(m)]
                 for i in range(q)]
    return {"ambient_q": q, "target_dimension": m, "centered": centered,
            "dual_pairing_identity": dual, "pair_product_rank": rational_rank(pair_rows),
            "zero_projected_rows": [i for i, row in enumerate(pair_rows) if not any(row)]}


def local_controls() -> dict:
    rows = [local_control(q) for q in range(2, 9)]
    restricted = local_control(4, 2)
    if any(not row["centered"] or not row["dual_pairing_identity"] for row in rows + [restricted]):
        raise ValueError("A centering or dual identity failed")
    if rows[0]["pair_product_rank"] != 1 or any(row["pair_product_rank"] != row["ambient_q"]
                                               for row in rows[1:]):
        raise ValueError("Unexpected full-target local rank")
    if restricted["pair_product_rank"] != 3 or restricted["zero_projected_rows"] != [2]:
        raise ValueError("The restricted-target escape control failed")
    return {"full_target_controls": rows, "restricted_target_control": restricted,
            "scope": "Finite exact rational controls; the all-dimension proof is in proof.md"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-certificate", action="store_true")
    args = parser.parse_args()
    path = HERE / "certificate.json"
    if args.write_certificate:
        path.write_text(json.dumps(shape_certificate(), indent=2) + "\n")
    result = {"shape_certificate": verify_certificate(json.loads(path.read_text())),
              "local_controls": local_controls()}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

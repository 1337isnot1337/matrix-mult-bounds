"""Local exact controls for the PR129-based normalized rank-sum deduction.

Reconstruct the adopted finite source ingredients; do not import another
verifier or fetch a remote file. Universal assertions remain written proofs.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/long-leg-torus-sum-2026-10-23/controls.json"
PR129_HEAD = "9eca895e3618ad1f560e0565dc30134478e88da8"
PR129_SHA256 = "36a9b1a2e1e79c342087bd424ad462200154508b2743b2477f5121afd96930ad"
PR129_BLOB = "0143933a0ab7ae4259a5be62653fd1465d7c107e"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "torus_sources.json").read_text())
    adopted = record["adopted_source_cap"]
    require(adopted["pr"] == 129 and adopted["commit"] == PR129_HEAD,
            "Changed adopted torus-cap attribution")
    require(adopted["sha256"] == PR129_SHA256 and adopted["git_blob_sha"] == PR129_BLOB,
            "Changed adopted source proof pin")
    expected_local = "research/ai/2026-10-23-long-leg-rank-obstruction/adopted/pr129_torus_low_rank_proof.md.txt"
    require(adopted["local_copy"] == expected_local, "Changed adopted source-copy path")
    data = (ROOT / expected_local).read_bytes()
    require(hashlib.sha256(data).hexdigest() == PR129_SHA256,
            "Adopted torus-cap proof bytes changed")
    git_data = b"blob "+str(len(data)).encode()+b"\0"+data
    require(hashlib.sha1(git_data).hexdigest() == PR129_BLOB,
            "Adopted source copy disagrees with its immutable Git blob")
    expected = {
        "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
        "research/ai/2026-10-23-long-leg-rank-obstruction/proof.md",
        "research/ai/2026-10-23-long-leg-rank-obstruction/corank_one.md",
    }
    entries = record["local_dependencies"]
    require(len(entries) == len(expected) and {e["path"] for e in entries} == expected,
            "Changed local predecessor inventory")
    for entry in entries:
        require(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
                == entry["sha256"], "Changed local predecessor: "+entry["path"])
    require(record["regular_kernel_predecessor"]["commit"] ==
            "08ac3e983e270cf3df4e26d960ceb16415f7ef31", "Changed PR113 credit")
    concurrent = {e["pr"]: e["commit"] for e in record["concurrent_work"]}
    require(concurrent == {
        125: "fc0a139ef447a4d8640f0fdf1781836ea7fa868a",
        132: "f9bce104af5e50d796488a1c8d5ff4d8d02ba260",
        142: "036671f072123569bd764808ff57d18128ff11d0",
    }, "Changed concurrent-work attribution")
    require(record["external_theorems_added"] is False,
            "Unstated external theorem dependency")
    return {"adopted_source_copies": 1, "local_predecessor_pins": len(entries),
            "concurrent_acknowledgments": len(concurrent)}


def coordinate_entries(i, k, z):
    """Literal positions for the one source coefficient F_(i,k,z)=1."""
    entries = {}
    for j, p, q, r in itertools.product(range(4), repeat=4):
        if p+q == k:
            row = (j*4+p)*7+z+r
            column = ((i+j)*4+q)*4+r
            require((row, column) not in entries, "Repeated literal source position")
            entries[row, column] = 1
    return entries


def torus_and_coordinate_controls():
    weights, coordinates, count = set(), [], 0
    hankel_counts = [1, 2, 3, 4, 3, 2, 1]
    for i, k, z in itertools.product(range(4), range(7), range(4)):
        weight = i+4*k+28*z
        weights.add(weight)
        entries = coordinate_entries(i, k, z)
        rows = {row for row, col in entries}
        columns = {col for row, col in entries}
        require(len(rows) == len(columns) == len(entries) == 16*hankel_counts[k],
                "Coordinate source matrix is not the prescribed partial permutation")
        for row, col in entries:
            j, rem = divmod(row, 28)
            p, ell = divmod(rem, 7)
            h, rem = divmod(col, 16)
            q, r = divmod(rem, 4)
            require((h-j, p+q, ell-r) == (i, k, z),
                    "Literal source coefficient convention changed")
            require(weight == -j+4*p+28*ell+h+4*q-28*r,
                    "Diagonal source rank-preservation identity failed")
            count += 1
        coordinates.append({"coordinate": [i, k, z], "rank": len(entries)})
    require(weights == set(range(112)) and count == 4096,
            "Source weights or literal term coverage changed")
    return {"distinct_parameter_weights": len(weights), "literal_terms": count,
            "coordinates": coordinates}


def cross_extreme_controls():
    count = 0
    for i, z, ip, zp in itertools.product(range(4), repeat=4):
        a, b = coordinate_entries(i, 0, z), coordinate_entries(ip, 6, zp)
        arows, brows = {r for r, c in a}, {r for r, c in b}
        acols, bcols = {c for r, c in a}, {c for r, c in b}
        require(not arows & brows and not acols & bcols,
                "Extreme source blocks are not a rank direct sum")
        require(len(arows | brows) == len(acols | bcols) == 32,
                "Cross-extreme source pair has wrong rank")
        count += 1
    return {"pairs_checked": count, "rank_of_each_sum": 32}


def matching_minor_controls():
    pairs, seen = [], set()
    for i, z in itertools.product(range(4), repeat=2):
        if (i, z) in seen:
            continue
        other = ((i+2) % 4, (z+2) % 4)
        pairs.append(((i, z), other))
        seen.update(((i, z), other))
    require(len(pairs) == 8 and len(seen) == 16, "Outer-grid matching failed")
    records = []
    for k in (0, 6):
        p = q = k//2
        for (i, z), (ip, zp) in pairs:
            entries = coordinate_entries(i, k, z)
            second = coordinate_entries(ip, k, zp)
            require(not set(entries) & set(second), "Distinct source parameters overlap")
            entries.update(second)
            imin, zmin = min(i, ip), min(z, zp)
            rows = [(j*4+p)*7+ell for j in range(4)
                    for ell in range(zmin, zmin+6)]
            columns = [(h*4+q)*4+r for h in range(imin, imin+6) for r in range(4)]
            minor = s.Matrix([[entries.get((row, col), 0) for col in columns]
                              for row in rows])
            determinant = int(minor.det())
            require(len(set(rows)) == len(set(columns)) == 24 and determinant == 1,
                    "Adopted matching determinant-one minor failed")
            records.append({"middle_index": k, "outer_pair": [[i, z], [ip, zp]],
                            "rows": rows, "columns": columns,
                            "minor_size": 24, "determinant": determinant})
    return records


def support_controls():
    records = []
    for first_width, expected_columns in ((2, 20), (3, 24)):
        coordinates = [(i, 0, z) for i in range(first_width) for z in range(4)]
        columns = set()
        for coordinate in coordinates:
            columns.update(c for r, c in coordinate_entries(*coordinate))
        require(len(coordinates) == 4*first_width and len(columns) == expected_columns,
                "Sharp source-space support count failed")
        records.append({"parameter_dimension": len(coordinates),
                        "source_rank_upper_bound": len(columns),
                        "coordinates": [list(x) for x in coordinates]})
    # This member of the 12-plane reaches rank24, so that plane is not below24.
    entries = {}
    for i in range(3):
        entries.update(coordinate_entries(i, 0, i))
    rows = sorted({r for r, c in entries})
    columns = sorted({c for r, c in entries})
    matrix = s.Matrix([[entries.get((r, c), 0) for c in columns] for r in rows])
    require(matrix.rank() == 24, "Literal rank24 boundary witness changed")
    return {"linear_spaces": records, "twelve_plane_witness_rank": 24,
            "source_cap_at_rank23": 8, "source_cap_is_sharp": True,
            "rank24_cap_eight_is_false": True}


def rank_budgets():
    pairs = list(itertools.product(range(1, 111), repeat=2))
    excluded = [(rb, rc) for rb, rc in pairs if rb+rc >= 201]
    require(len(excluded) == 210 and all(224-rb-rc <= 23 for rb, rc in excluded),
            "Polar source rank budget changed")
    require(all(max(rb, rc)-96 >= 5 for rb, rc in excluded),
            "Regular unit-image rank budget failed")
    additional = [(rb, rc) for rb, rc in excluded if rb <= 101 and rc <= 101]
    require(additional == [(100, 101), (101, 100), (101, 101)],
            "New scope relative to PR129 changed")
    boundary = [(rb, rc) for rb, rc in pairs if rb <= 101 and rc <= 101 and rb+rc == 200]
    require(boundary == [(99, 101), (100, 100), (101, 99)]
            and 224-200 == 24, "First remaining source-cap boundary changed")
    require(100-8 == 92 and 92 > 90 and 5 > 2, "Invertible-kernel contradiction failed")
    return {"normalized_rank_pairs": len(pairs), "pairs_excluded_by_sum": len(excluded),
            "maximum_remaining_rank_sum": 200,
            "adopted_individual_rank_cap": 101,
            "new_pairs_beyond_adopted_individual_cap": [list(x) for x in additional],
            "remaining_sum200_boundary_pairs": [list(x) for x in boundary],
            "maximum_first_map_image_dimension_under_contradiction": 8,
            "minimum_first_map_kernel_dimension": 92,
            "maximum_singular_mat10_space_dimension": 90,
            "minimum_unit_image_rank_under_contradiction": 5,
            "maximum_residual_rank": 2,
            "first_unexcluded_source_rank_budget": 24,
            "boundary_is_construction": False}


@lru_cache(maxsize=1)
def report():
    return {"proof_status": "proof-written-unreviewed", "improves_omega": False,
            "scope": "Finite controls for the adopted PR129 source cap and new sum200 deduction.",
            "source_checks": check_sources(),
            "torus_and_coordinates": torus_and_coordinate_controls(),
            "cross_extremes": cross_extreme_controls(),
            "matching_minors": matching_minor_controls(),
            "source_supports": support_controls(),
            "rank_budgets": rank_budgets()}


def verify(record):
    check_sources()
    require(record == report(), "Changed torus source controls or rank-sum scope")
    return {"literal_source_terms": 4096, "coordinate_ranks": 112,
            "cross_extreme_pairs": 256, "determinant_one_matching_minors": 16,
            "source_support_spaces": 2, "normalized_rank_pairs": 12100,
            "new_pairs_beyond_pr129_individual_cap": 3,
            "maximum_remaining_rank_sum": 200, "improves_omega": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate the exact controls")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True)+"\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))

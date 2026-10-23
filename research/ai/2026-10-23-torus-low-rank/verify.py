"""Exact finite controls for the sharp A4 rank-at-most-23 subspace bound.

The standard library suffices. The arbitrary-complex-subspace and Laurent
claims rest on proof.md; these controls verify the source action and minors.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/torus-low-rank-2026-10-23/controls.json"
DEPENDENCIES = {
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-koszul/cyclic_finite_target.py",
}
PARAMETERS = list(itertools.product(range(4), range(7), range(4)))
ROWS = list(itertools.product(range(4), range(4), range(7)))
COLUMNS = list(itertools.product(range(7), range(4), range(4)))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def weight(parameter):
    i, k, s = parameter
    return i + 4*k + 28*s


def determinant(matrix):
    """Integer Bareiss elimination, including row swaps and exact division."""
    size = len(matrix)
    require(size and all(len(row) == size for row in matrix), "Nonsquare minor")
    work = [list(row) for row in matrix]
    previous, sign = 1, 1
    for column in range(size-1):
        pivot_row = next((i for i in range(column, size) if work[i][column]), None)
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work[pivot_row], work[column] = work[column], work[pivot_row]
            sign = -sign
        pivot = work[column][column]
        for i in range(column+1, size):
            for j in range(column+1, size):
                numerator = pivot*work[i][j] - work[i][column]*work[column][j]
                require(numerator % previous == 0, "Nonexact Bareiss division")
                work[i][j] = numerator // previous
            work[i][column] = 0
        previous = pivot
    return sign * work[-1][-1]


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == "addb447b3c1e00ff8b9cb0070de8bee9da3bd813",
            "Changed source baseline")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES) and
            {entry["path"] for entry in entries} == DEPENDENCIES,
            "Changed source dependency inventory")
    for entry in entries:
        digest = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(digest == entry["sha256"], "Source digest mismatch: " + entry["path"])
    predecessors = record["credited_predecessors"]
    require([(x["commit"], x["path"]) for x in predecessors] == [
        ("08ac3e983e270cf3df4e26d960ceb16415f7ef31",
         "research/ai/2026-10-23-one-regular-leg/proof.md"),
        ("addb447b3c1e00ff8b9cb0070de8bee9da3bd813",
         "research/ai/2026-10-23-singular-long-rank/proof.md")],
        "Changed credited predecessors")
    require(record["field"] == "C" and not record["external_theorems_added"],
            "Changed theorem scope")
    return len(entries)


def source_supports():
    """Reconstruct all 4096 literal monomial terms, then compare conventions."""
    supports = {parameter: set() for parameter in PARAMETERS}
    labels = {}
    for i, j, p, q, r, s in itertools.product(range(4), repeat=6):
        parameter = (i, p+q, s)
        row, column = (j, p, r+s), (i+j, q, r)
        require((row, column) not in labels, "Repeated source matrix position")
        labels[row, column] = parameter
        supports[parameter].add((row, column))
    require(len(labels) == 4096, "Wrong literal source support size")
    source = ROOT / "research/ai/2026-10-20-koszul/cyclic_finite_target.py"
    spec = importlib.util.spec_from_file_location("torus_canonical_source", source)
    maintained = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(maintained)
    # Every possible parameter has a distinct nonzero label. Each source
    # entry selects one parameter, so this compares all 112^2 entries.
    parameter_labels = {parameter: i+1 for i, parameter in enumerate(PARAMETERS)}
    coefficients = list(range(1, 113))
    for row, column in itertools.product(ROWS, COLUMNS):
        literal = parameter_labels.get(labels.get((row, column)), 0)
        require(literal == maintained.slice_entry(coefficients, 4, row, column),
                "Literal source differs from the maintained convention")
    return supports


def action_and_coordinate_controls(supports):
    require(sorted(weight(p) for p in PARAMETERS) == list(range(112)),
            "Parameter weights are not distinct")
    ranks_by_middle = {}
    equalities = 0
    for parameter, support in supports.items():
        i, k, s = parameter
        require(len({row for row, _ in support}) == len(support) and
                len({column for _, column in support}) == len(support),
                "A coordinate slice is not a partial permutation")
        rank = len(support)
        require(rank == 16 * (1, 2, 3, 4, 3, 2, 1)[k], "Coordinate rank changed")
        ranks_by_middle.setdefault(k, set()).add(rank)
        for (j, p, ell), (h, q, r) in support:
            require(i == h-j and k == p+q and s == ell-r, "Source index mismatch")
            require(weight(parameter) == (-j+4*p+28*ell)+(h+4*q-28*r),
                    "Diagonal action does not preserve a source term")
            equalities += 1
    cross_count = 0
    for i, s, other_i, other_s in itertools.product(range(4), repeat=4):
        support = supports[i, 0, s] | supports[other_i, 6, other_s]
        require(len(support) == len({row for row, _ in support}) ==
                len({column for _, column in support}) == 32,
                "Cross-extreme pair does not have rank 32")
        cross_count += 1
    return {"distinct_parameter_weights": 112, "weight_range": [0, 111],
            "source_terms_checked": equalities,
            "literal_matrix_entries_compared": 112*112,
            "coordinate_slices_checked": len(supports),
            "coordinate_ranks_by_middle_index": [sorted(ranks_by_middle[k])[0]
                                                  for k in range(7)],
            "cross_extreme_pairs_checked": cross_count, "cross_extreme_pair_rank": 32}


def matching_minors(supports):
    seen = set()
    records = []
    for i in range(2):
        for s in range(4):
            pair = [(i, s), (i+2, (s+2) % 4)]
            require(not any(p in seen for p in pair), "Matching pairs overlap")
            seen.update(pair)
            i0, s0 = min(x[0] for x in pair), min(x[1] for x in pair)
            block_rows = [(j, ell) for j in range(4) for ell in range(s0, s0+6)]
            block_columns = [(h, r) for h in range(i0, i0+6) for r in range(4)]
            values = []
            for k in (0, 6):
                p = q = k//2
                rows = [(j, p, ell) for j, ell in block_rows]
                columns = [(h, q, r) for h, r in block_columns]
                require(len(set(rows)) == len(set(columns)) == 24 and
                        set(rows) <= set(ROWS) and set(columns) <= set(COLUMNS),
                        "Invalid 24 by 24 source minor")
                support = supports[pair[0][0], k, pair[0][1]] | supports[pair[1][0], k, pair[1][1]]
                matrix = [[int((row, column) in support) for column in columns] for row in rows]
                value = determinant(matrix)
                require(value == 1, "Matching minor is not determinant one")
                values.append({"middle_index": k, "determinant": value})
            records.append({"pair": [list(x) for x in pair], "minor_size": 24,
                            "row_indices_in_28_by_28_block": [7*j+ell for j, ell in block_rows],
                            "column_indices_in_28_by_28_block": [4*h+r for h, r in block_columns],
                            "determinants": values})
    require(seen == set(itertools.product(range(4), repeat=2)), "Matching omits coordinates")
    return records


def support_plane_control(supports, first_indices):
    coordinates = [(i, 0, s) for i in first_indices for s in range(4)]
    columns = {column for parameter in coordinates for _, column in supports[parameter]}
    require(columns == {(h, 0, r) for h in range(max(first_indices)+4) for r in range(4)},
            "Wrong coordinate-plane support")
    return {"coordinates": [list(x) for x in coordinates], "dimension": len(coordinates),
            "supported_columns": len(columns), "all_slice_rank_upper": len(columns)}


def echelon_specialization(basis):
    """Check an explicitly supplied echelon basis and its polynomial limit."""
    require(bool(basis), "Empty echelon basis")
    pivots = [min(vector, key=weight) for vector in basis]
    require(len(set(pivots)) == len(basis), "Repeated pivot coordinate")
    records = []
    for vector, pivot in zip(basis, pivots):
        require(vector[pivot] == 1 and all(vector.get(p, 0) == 0 for p in pivots if p != pivot),
                "Basis is not in reduced echelon form")
        terms = []
        limit = {}
        for coordinate, coefficient in sorted(vector.items(), key=lambda item: weight(item[0])):
            require(coordinate in PARAMETERS and coefficient != 0, "Invalid nonzero term")
            exponent = weight(coordinate)-weight(pivot)
            require(exponent >= 0, "Normalized basis has a pole")
            if exponent == 0:
                limit[coordinate] = coefficient
            terms.append({"coordinate": list(coordinate), "coefficient": coefficient,
                          "normalized_exponent": exponent})
        require(limit == {pivot: 1}, "Specialization is not a coordinate vector")
        records.append({"pivot": list(pivot), "normalized_terms": terms})
    return {"dimension": len(basis), "basis": records,
            "independent_coordinate_limits": True,
            "status": "Finite control of the written arbitrary-subspace argument"}


def threshold(defect):
    require(isinstance(defect, int) and 0 <= defect <= 110, "Invalid long-leg defect")
    upper, active_lower = 15+defect, 12-defect
    return {"long_defect": defect, "long_limit_rank": 110-defect,
            "source_rank_upper": upper, "active_image_rank_lower": active_lower,
            "correction_rank_upper": 2, "rank23_subspace_dimension_upper": 8,
            "target_ruling_dimension": 10,
            "excluded_by_written_torus_ruling_theorem": upper <= 23 and active_lower > 2}


def report():
    pins = check_sources()
    supports = source_supports()
    return {"scope": "Exact finite controls; arbitrary-subspace and all-Laurent-order claims use proof.md.",
            "proof_status": "proof-written-unreviewed", "independent_review": False,
            "improves_omega": False, "source_pin_count": pins,
            "action_and_coordinate_controls": action_and_coordinate_controls(supports),
            "matching_minors": matching_minors(supports),
            "sharp_rank23_plane": support_plane_control(supports, [0, 1]),
            "rank24_boundary_plane": support_plane_control(supports, [0, 1, 2]),
            "echelon_specialization_control": echelon_specialization([
                {(0, 0, 0): 1, (1, 0, 0): 2, (1, 0, 1): -3},
                {(0, 0, 1): 1, (0, 0, 2): 5, (0, 0, 3): -1},
                {(1, 0, 2): 1, (1, 0, 3): 7}]),
            "thresholds": [threshold(c) for c in range(10)],
            "maximum_linear_subspace_dimension_at_rank23": 8,
            "remaining_balanced_long_rank_upper": 101,
            "rank101_long_limits_excluded": False}


def verify(record):
    require(record == report(), "Changed controls, source scope, threshold or proof status")
    action = record["action_and_coordinate_controls"]
    return {"literal_source_terms_checked": action["source_terms_checked"],
            "literal_matrix_entries_compared": action["literal_matrix_entries_compared"],
            "coordinate_slices_checked": action["coordinate_slices_checked"],
            "cross_extreme_pairs_checked": action["cross_extreme_pairs_checked"],
            "determinant_one_minors_checked": 2*len(record["matching_minors"]),
            "sharp_rank23_linear_space_dimension": 8,
            "excluded_defects": [x["long_defect"] for x in record["thresholds"]
                                 if x["excluded_by_written_torus_ruling_theorem"]],
            "remaining_balanced_long_rank_upper": 101, "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate the finite controls")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True)+"\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

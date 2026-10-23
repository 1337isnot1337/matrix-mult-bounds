"""Replay exact certificates for the sharp A4 rank<64 dimension bound."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT_DIR = ROOT / "results/torus-order-ideal-2026-10-23"
CERTIFICATES = RESULT_DIR / "certificates.json"
RESULT = RESULT_DIR / "controls.json"
SOURCE_PATHS = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-graded-quantum-flags/saturation.md",
    "research/ai/2026-10-23-torus-rank-frontier/proof.md",
)
MIDDLE_RANKS = (1, 2, 3, 4, 3, 2, 1)
COORDINATES = tuple(product(range(4), range(3), range(4)))
CERTIFICATE_HEADER = {
    "schema": "torus-order-ideal-minors-v1",
    "source": "canonical cyclic A4",
    "coefficient_domain": "integers 0 and 1",
    "verification_modulus": 2,
    "minor_size": 64,
    "ideal_size": 33,
    "coordinate_order": "(i,k,s) lexicographic on range(4) x range(3) x range(4)",
    "mask_encoding": "canonical hexadecimal; bit n selects index n",
}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def check_sources(document=None):
    if document is None:
        document = json.loads((HERE / "sources.json").read_text())
    entries = document["local_dependencies"]
    require(tuple(item["path"] for item in entries) == SOURCE_PATHS,
            "changed source inventory")
    for item in entries:
        path = ROOT / item["path"]
        require(path.is_file(), "missing source prerequisite")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"],
                "source digest mismatch")
    return {item["path"]: item["sha256"] for item in entries}


def row_index(j, p, ell):
    return (4 * j + p) * 7 + ell


def column_index(h, q, r):
    return (4 * h + q) * 4 + r


def decode_position(row, column):
    jp, ell = divmod(row, 7)
    j, p = divmod(jp, 4)
    hq, r = divmod(column, 4)
    h, q = divmod(hq, 4)
    return j, p, ell, h, q, r


def literal_source():
    """Use the original six-index product, not discovery's matrix formula."""
    slices = {coordinate: set() for coordinate in product(range(4), range(7), range(4))}
    entries = {}
    for i, j, p, q, r, s in product(range(4), repeat=6):
        coordinate = (i, p + q, s)
        position = row_index(j, p, r + s), column_index(i + j, q, r)
        require(position not in entries, "overlapping literal coefficient labels")
        entries[position] = coordinate
        slices[coordinate].add(position)
    require(len(entries) == 4096, "literal term count changed")
    return slices, entries


def source_controls(slices, entries):
    for i, k, s in slices:
        support = slices[i, k, s]
        expected = 16 * MIDDLE_RANKS[k]
        require(len(support) == expected, "monomial slice size changed")
        require(len({row for row, column in support}) == expected
                and len({column for row, column in support}) == expected,
                "monomial slice is not the required partial permutation")
    for row, column in product(range(112), repeat=2):
        j, p, ell, h, q, r = decode_position(row, column)
        expected = (h - j, p + q, ell - r)
        if not (0 <= h - j < 4 and 0 <= ell - r < 4):
            expected = None
        require(entries.get((row, column)) == expected, "coefficient formula mismatch")
    weights = {i + 4 * k + 28 * s for i, k, s in slices}
    require(weights == set(range(112)), "source weights are not distinct")
    for (row, column), (i, k, s) in entries.items():
        j, p, ell, h, q, r = decode_position(row, column)
        require((-j + 4 * p + 28 * ell) + (h + 4 * q - 28 * r)
                == i + 4 * k + 28 * s, "torus row/column identity failed")
    return {"literal_terms": len(entries), "matrix_entries_checked": 112 * 112,
            "monomial_slices": len(slices), "distinct_source_weights": len(weights),
            "monomial_ranks_by_middle": [16 * value for value in MIDDLE_RANKS]}


def add_entry(matrix, position, value):
    new = matrix.get(position, 0) + value
    if new:
        matrix[position] = new
    else:
        matrix.pop(position, None)


def infinitesimal_controls(slices):
    """Check every basis vector in all three literal integer identities."""
    counts = Counter()
    for coordinate, support in slices.items():
        i, k, s = coordinate
        for direction in ("i", "k", "s"):
            actual = {}
            for row, column in support:
                j, p, ell, h, q, r = decode_position(row, column)
                if direction == "i":
                    if j < 3:
                        add_entry(actual, (row_index(j + 1, p, ell), column), -(j + 1))
                    if h > 0:
                        add_entry(actual, (row, column_index(h - 1, q, r)), h)
                elif direction == "k":
                    if p > 0:
                        add_entry(actual, (row_index(j, p - 1, ell), column), 4 - p)
                    if q > 0:
                        add_entry(actual, (row, column_index(h, q - 1, r)), 4 - q)
                else:
                    if ell > 0:
                        add_entry(actual, (row_index(j, p, ell - 1), column), ell)
                    if r < 3:
                        add_entry(actual, (row, column_index(h, q, r + 1)), -(r + 1))
            if direction == "i" and i > 0:
                target, scale = (i - 1, k, s), i
            elif direction == "k" and k > 0:
                target, scale = (i, k - 1, s), 7 - k
            elif direction == "s" and s > 0:
                target, scale = (i, k, s - 1), s
            else:
                target, scale = None, 0
            expected = ({position: scale for position in slices[target]} if target else {})
            require(actual == expected, "infinitesimal equivariance identity failed")
            counts[direction] += 1
            counts["zero_boundary_identities"] += int(target is None)
    require(sum(counts[d] for d in ("i", "k", "s")) == 336,
            "incomplete infinitesimal basis coverage")
    return {"identities_per_direction": {d: counts[d] for d in ("i", "k", "s")},
            "total_basis_identities": 336,
            "zero_boundary_identities": counts["zero_boundary_identities"],
            "weight_decreases": {"i": 1, "k": 4, "s": 28},
            "arithmetic": "integers; no characteristic-two equivariance inference"}


def enumerate_ideals(volume=33):
    """Fill heights recursively, independently of discovery's triple loop.

    A height h[k][i] includes exactly s=0,...,h[k][i]-1. Each choice
    is bounded by the already filled neighbors in the i and k directions.
    """
    require(type(volume) is int and 0 <= volume <= 48, "invalid ideal volume")
    result, heights = [], []

    def visit(position, remaining):
        if position == 12:
            if remaining == 0:
                result.append(tuple(tuple(heights[4 * k:4 * k + 4]) for k in range(3)))
            return
        k, i = divmod(position, 4)
        ceiling = min(4, heights[position - 1] if i else 4,
                      heights[position - 4] if k else 4, remaining)
        for height in range(ceiling + 1):
            if remaining - height > 4 * (11 - position):
                continue
            heights.append(height)
            visit(position + 1, remaining - height)
            heights.pop()

    visit(0, volume)
    return tuple(result)


def parse_shape(value):
    require(type(value) is list and len(value) == 3
            and all(type(row) is list and len(row) == 4 for row in value),
            "invalid ideal shape dimensions")
    require(all(type(entry) is int and 0 <= entry <= 4 for row in value for entry in row),
            "invalid ideal height")
    shape = tuple(map(tuple, value))
    require(sum(map(sum, shape)) == 33, "ideal volume is not 33")
    require(all(shape[k][i] >= shape[k][i + 1] for k in range(3) for i in range(3))
            and all(shape[k][i] >= shape[k + 1][i] for k in range(2) for i in range(4)),
            "shape is not an order ideal")
    return shape


def parse_mask(value, width):
    require(type(value) is str, "mask must be a hexadecimal string")
    try:
        mask = int(value, 16)
    except ValueError as error:
        raise ArithmeticError("invalid hexadecimal mask") from error
    require(0 <= mask < 1 << width and value == hex(mask),
            "mask is out of range or noncanonical")
    return mask


def mask_indices(mask, width):
    return [index for index in range(width) if (mask >> index) & 1]


def invertible_mod2(rows, size):
    """Fixed low-column elimination, separate from discovery's pivot search."""
    require(len(rows) == size and all(type(row) is int and 0 <= row < 1 << size for row in rows),
            "invalid binary square matrix")
    matrix = list(rows)
    for column in range(size):
        pivot = next((row for row in range(column, size) if (matrix[row] >> column) & 1), None)
        if pivot is None:
            return False
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        for row in range(column + 1, size):
            if (matrix[row] >> column) & 1:
                matrix[row] ^= matrix[column]
    return True


def replay_certificates(document=None, slices=None):
    if document is None:
        document = json.loads(CERTIFICATES.read_text())
    require(set(document) == set(CERTIFICATE_HEADER) | {"records"}, "changed certificate fields")
    require(all(document[key] == value for key, value in CERTIFICATE_HEADER.items()),
            "changed certificate header")
    require(type(document["records"]) is list, "certificate records must be a list")
    if slices is None:
        slices, _ = literal_source()
    expected = set(enumerate_ideals())
    require(len(expected) == 611, "size-33 order-ideal inventory changed")
    seen, sizes = set(), []
    for record in document["records"]:
        require(set(record) == {"shape", "coefficient_mask", "minor_rows_mask", "minor_columns_mask"},
                "changed minor certificate fields")
        shape = parse_shape(record["shape"])
        require(shape not in seen, "duplicate ideal certificate")
        seen.add(shape)
        selected = mask_indices(parse_mask(record["coefficient_mask"], 48), 48)
        require(selected and all(COORDINATES[index][2] < shape[COORDINATES[index][1]][COORDINATES[index][0]]
                                 for index in selected), "coefficient support leaves its ideal")
        rows = mask_indices(parse_mask(record["minor_rows_mask"], 112), 112)
        columns = mask_indices(parse_mask(record["minor_columns_mask"], 112), 112)
        require(len(rows) == len(columns) == 64, "minor does not select 64 distinct rows and columns")
        full_rows = [0] * 112
        for index in selected:
            for row, column in slices[COORDINATES[index]]:
                full_rows[row] ^= 1 << column
        minor = [sum(((full_rows[row] >> column) & 1) << index
                     for index, column in enumerate(columns)) for row in rows]
        require(invertible_mod2(minor, 64), "saved integer minor is singular modulo two")
        sizes.append(len(selected))
    require(seen == expected, "incomplete order-ideal certificate coverage")
    return {"ideal_box": [4, 3, 4], "ideal_volume": 33,
            "exhaustive_ideals": len(expected), "distinct_certificates": len(seen),
            "integer_minors_checked": len(seen), "minor_size": 64,
            "all_determinants_modulo_two": 1,
            "coefficient_support_size_min": min(sizes),
            "coefficient_support_size_max": max(sizes),
            "replay_uses_discovery": False,
            "field_transfer": "An odd integer determinant is nonzero over C."}


def sharpness_controls(slices):
    coordinates = [(i, k, s) for i in range(4) for k in range(2) for s in range(4)]
    support = set().union(*(slices[coordinate] for coordinate in coordinates))
    rows = {row for row, column in support}
    columns = {column for row, column in support}
    require(len(coordinates) == 32 and len(rows) == len(columns) == 56,
            "dimension-32 sharpness plane support changed")
    require(all(decode_position(row, column)[1] in (0, 1) for row, column in support),
            "sharpness plane has an unsupported p row")
    return {"coordinates": "all i,s in range(4), middle k in {0,1}",
            "parameter_dimension": 32, "supported_rows": len(rows),
            "supported_columns": len(columns), "uniform_rank_upper": 56,
            "strict_rank_threshold": 64}


def kernel_cap(delta):
    if delta < 16:
        return 0
    if delta < 32:
        return 16
    if delta < 48:
        return 24
    if delta < 64:
        return 32
    return 112  # No improved dimension bound at rank 64 is used here.


def screen(b, c):
    require(type(b) is int and type(c) is int and 0 <= b <= 110 and 0 <= c <= 110,
            "invalid long-map rank")
    delta = 224 - b - c
    lower = 100 - (b // 11) * (c // 11)
    cap = kernel_cap(delta)
    ordinary = delta < 16
    return {"ranks": [b, c], "source_defect": delta, "kernel_lower": lower,
            "kernel_upper": cap, "ordinary_regularity_forced": ordinary,
            "excluded": cap < lower or ordinary}


def rank_pair_controls():
    cases = [screen(b, c) for b in range(111) for c in range(111)]
    high = [case for case in cases if sum(case["ranks"]) >= 161]
    new = [case for case in high if sum(case["ranks"]) <= 176]
    require(all(case["excluded"] for case in high), "sum-160 frontier failed")
    require(max((case["ranks"][0] // 11) * (case["ranks"][1] // 11) for case in new) == 64,
            "new-range floor product changed")
    require(min(case["kernel_lower"] for case in new) == 36
            and all(case["kernel_upper"] == 32 for case in new), "new-range kernel margins changed")
    return {"rank_pairs_checked": len(cases), "pairs_above_160": len(high),
            "excluded_pairs_above_160": sum(case["excluded"] for case in high),
            "new_pairs_of_sum_161_through_176": len(new),
            "new_range_maximum_floor_product": 64,
            "new_range_minimum_kernel_lower": 36,
            "new_range_kernel_upper": 32,
            "boundary_control": screen(80, 80),
            "ordinary_control": screen(110, 110)}


def report():
    slices, entries = literal_source()
    return {"schema": "torus-order-ideal-controls-v1", "field": "C",
            "source_sha256": check_sources(),
            "certificates_sha256": hashlib.sha256(CERTIFICATES.read_bytes()).hexdigest(),
            "source_controls": source_controls(slices, entries),
            "infinitesimal_controls": infinitesimal_controls(slices),
            "order_ideal_certificates": replay_certificates(slices=slices),
            "sharpness_control": sharpness_controls(slices),
            "rank_pair_controls": rank_pair_controls(),
            "claim_scope": {"source_rank_strict_upper": 64, "source_space_dimension_upper": 32,
                            "dimension_bound_sharp": True, "balanced_long_rank_sum_upper": 160,
                            "long_rank_sum_bound_sharp": False, "target_constructed": False,
                            "improves_omega": False, "formalized_proof": False,
                            "proof_status": "proof-written-unreviewed", "independent_review": False}}


def replay_saved(document):
    require(document["schema"] == "torus-order-ideal-controls-v1", "unknown evidence schema")
    require(document == report(), "saved evidence or scope differs from exact replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write aggregate controls, then replay them")
    args = parser.parse_args()
    if args.write:
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2) + "\n")
    replay_saved(json.loads(RESULT.read_text()))
    print("PASS: 4096 source terms, 336 lowering identities, all 611 size-33 ideals and 64-minors, 12321 rank pairs.")
    print("Written bounds: source rank<64 implies dimension<=32, sharply; balanced long-rank sum<=160.")
    print("No target, sharpness of the long-rank frontier, formalization, or exponent improvement is claimed.")


if __name__ == "__main__":
    main()

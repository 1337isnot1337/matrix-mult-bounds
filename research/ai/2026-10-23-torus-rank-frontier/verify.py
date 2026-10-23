"""Exact finite controls for the written rank-48 and long-sum-176 theorems."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT = ROOT / "results/torus-rank-frontier-2026-10-23/controls.json"
SOURCE_PATHS = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-graded-quantum-flags/saturation.md",
    "research/ai/2026-10-23-torus-low-rank/proof.md",
)
MIDDLE_RANKS = [1, 2, 3, 4, 3, 2, 1]
FORBIDDEN = ((0, 5), (1, 6), (1, 5))


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


def literal_source():
    """Build every monomial slice from the original six-index product."""
    slices = {coordinate: set() for coordinate in product(range(4), range(7), range(4))}
    entries = {}
    for i, j, p, q, r, s in product(range(4), repeat=6):
        coordinate = (i, p + q, s)
        position = (row_index(j, p, r + s), column_index(i + j, q, r))
        require(position not in entries, "literal source has overlapping coefficient labels")
        entries[position] = coordinate
        slices[coordinate].add(position)
    require(len(entries) == 4096, "literal term count changed")
    return slices, entries


def biform_matrix(coordinates):
    """Direct coefficient formula R(g), independent of literal_source."""
    coefficients = set(map(tuple, coordinates))
    return [[int((h - j, ell - r) in coefficients)
             for h in range(7) for r in range(4)]
            for j in range(4) for ell in range(7)]


def determinant(matrix):
    """Fraction-free exact integer determinant with row pivoting."""
    a = [list(row) for row in matrix]
    size = len(a)
    require(all(len(row) == size for row in a), "determinant requires a square matrix")
    if not size:
        return 1
    sign, previous = 1, 1
    for k in range(size - 1):
        pivot_row = next((i for i in range(k, size) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                require(numerator % previous == 0, "nonexact Bareiss division")
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def independent_minor(matrix):
    """Discover rational pivot rows/columns; acceptance recomputes a determinant."""
    basis, rows, columns = {}, [], []
    for row_index_, original in enumerate(matrix):
        row = {j: Fraction(value) for j, value in enumerate(original) if value}
        while row:
            column = min(row)
            if column not in basis:
                scale = row[column]
                basis[column] = {j: value / scale for j, value in row.items()}
                rows.append(row_index_)
                columns.append(column)
                break
            scale = row[column]
            for j, value in basis[column].items():
                new = row.get(j, 0) - scale * value
                if new:
                    row[j] = new
                else:
                    row.pop(j, None)
    minor = [[matrix[i][j] for j in columns] for i in rows]
    det = determinant(minor)
    if det == -1:
        rows[0], rows[1] = rows[1], rows[0]
        det = 1
    return rows, columns, det


def pair_coordinates():
    used, pairs = set(), []
    for coordinate in product(range(4), repeat=2):
        if coordinate in used:
            continue
        partner = ((coordinate[0] + 2) % 4, (coordinate[1] + 2) % 4)
        used.update((coordinate, partner))
        pairs.append([list(coordinate), list(partner)])
    return pairs


def pair_certificates():
    records = []
    for pair in pair_coordinates():
        matrix = biform_matrix(pair)
        rows, columns, det = independent_minor(matrix)
        require(len(rows) == 24 and det == 1, "rank-24 pair certificate changed")
        records.append({"coordinates": pair, "minor_rows": rows,
                        "minor_columns": columns, "minor_determinant": det})
    return records


def replay_pairs(records):
    require([record["coordinates"] for record in records] == pair_coordinates(),
            "pair inventory changed")
    for record in records:
        rows, columns = record["minor_rows"], record["minor_columns"]
        require(len(rows) == len(columns) == 24 and len(set(rows)) == len(set(columns)) == 24,
                "minor dimensions or unique indices changed")
        require(all(type(i) is int and 0 <= i < 28 for i in rows + columns),
                "invalid minor index")
        matrix = biform_matrix(record["coordinates"])
        actual = determinant([[matrix[i][j] for j in columns] for i in rows])
        require(actual == record["minor_determinant"] == 1,
                "saved rank-24 minor is not determinant one")
    return len(records)


def source_controls(slices, entries):
    factor_entries = 0
    for i, k, s in product(range(4), range(7), range(4)):
        support = slices[i, k, s]
        expected_rank = 16 * MIDDLE_RANKS[k]
        require(len(support) == expected_rank, "monomial source rank mismatch")
        require(len({row for row, column in support}) == expected_rank
                and len({column for row, column in support}) == expected_rank,
                "monomial slice is not a partial permutation")
        # Check H_k tensor R(e_(i,s)) with the actual original source indexing.
        biform = biform_matrix([(i, s)])
        expected = set()
        for p, q in product(range(4), repeat=2):
            if p + q != k:
                continue
            for j, ell, h, r in product(range(4), range(7), range(7), range(4)):
                if biform[7 * j + ell][4 * h + r]:
                    expected.add((row_index(j, p, ell), column_index(h, q, r)))
        require(support == expected, "literal tensor-factor formula mismatch")
        factor_entries += len(expected)
    weights = {i + 4 * k + 28 * s for i, k, s in slices}
    require(weights == set(range(112)), "parameter weights are not distinct")
    for (row, column), (i, k, s) in entries.items():
        jp, ell = divmod(row, 7)
        j, p = divmod(jp, 4)
        hq, r = divmod(column, 4)
        h, q = divmod(hq, 4)
        require((-j + 4 * p + 28 * ell) + (h + 4 * q - 28 * r)
                == i + 4 * k + 28 * s, "torus row/column weights mismatch")
    return {"literal_terms": len(entries), "monomial_slices": len(slices),
            "ranks_by_middle_coordinate": [16 * value for value in MIDDLE_RANKS],
            "factorization_nonzero_entries": factor_entries,
            "distinct_parameter_weights": len(weights)}


def middle_pair_controls(slices):
    records = []
    for left, right in FORBIDDEN:
        count = 0
        expected = 16 * (MIDDLE_RANKS[left] + MIDDLE_RANKS[right])
        for i, s, i2, s2 in product(range(4), repeat=4):
            one, two = slices[i, left, s], slices[i2, right, s2]
            require(not ({r for r, c in one} & {r for r, c in two}),
                    "forbidden middle slices have overlapping rows")
            require(not ({c for r, c in one} & {c for r, c in two}),
                    "forbidden middle slices have overlapping columns")
            require(len(one | two) == expected, "forbidden middle rank mismatch")
            count += 1
        records.append({"middle_pair": [left, right], "short_pairs_checked": count,
                        "partial_permutation_rank": expected})
    allowed = []
    for size in range(1, 5):
        for subset in combinations((0, 1, 5, 6), size):
            if all(not set(pair) <= set(subset) for pair in FORBIDDEN):
                allowed.append(set(subset))
    maximal = sorted(sorted(subset) for subset in allowed
                     if not any(subset < other for other in allowed))
    require(maximal == [[0, 1], [0, 6], [5, 6]], "middle support classification changed")
    return {"forbidden_pairs": records, "maximal_middle_supports": maximal,
            "total_short_pairs_checked": sum(record["short_pairs_checked"] for record in records)}


def threshold_controls(records, slices):
    """Embed the eight core minors in rank-48 literal-source matrices."""
    count = 0
    for middle in (1, 5):
        pq = [(p, q) for p, q in product(range(4), repeat=2) if p + q == middle]
        for record in records:
            support = set().union(*(slices[i, middle, s] for i, s in record["coordinates"]))
            core = biform_matrix(record["coordinates"])
            core_minor = [[core[r][c] for c in record["minor_columns"]]
                          for r in record["minor_rows"]]
            # H_1 and H_5 have two disjoint anti-diagonal blocks. In block-paired
            # row/column order the actual selected 48-minor is diag(Rminor,Rminor).
            for block, (p, q) in enumerate(pq):
                for other, (p2, q2) in enumerate(pq):
                    actual = [[int((row_index(row // 7, p, row % 7),
                                    column_index(column // 4, q2, column % 4)) in support)
                               for column in record["minor_columns"]]
                              for row in record["minor_rows"]]
                    expected = (core_minor if block == other
                                else [[0] * 24 for _ in range(24)])
                    require(actual == expected, "rank-two middle minor embedding failed")
            count += 1
    # Middle 0 and 6 are disjoint for all g choices. Each choice of a paired
    # minor on either block gives a block-diagonal 48-minor of determinant one.
    outer_count = 0
    for left, right in product(records, repeat=2):
        full_support = set().union(*(slices[i, middle, s]
                                     for middle, record in ((0, left), (6, right))
                                     for i, s in record["coordinates"]))
        for middle, record in ((0, left), (6, right)):
            p = q = middle // 2
            support = set().union(*(slices[i, middle, s] for i, s in record["coordinates"]))
            actual = [[int((row_index(r // 7, p, r % 7), column_index(c // 4, q, c % 4)) in support)
                       for c in record["minor_columns"]] for r in record["minor_rows"]]
            require(determinant(actual) == 1, "outer block minor embedding failed")
        for row_record, column_record, p, q in ((left, right, 0, 3), (right, left, 3, 0)):
            require(all((row_index(r // 7, p, r % 7), column_index(c // 4, q, c % 4))
                        not in full_support for r in row_record["minor_rows"]
                        for c in column_record["minor_columns"]),
                    "two-extreme minor has an off-diagonal entry")
        outer_count += 1
    return {"rank_two_middle_48_minors": count,
            "two_extreme_48_minors": outer_count,
            "all_minor_determinants": 1,
            "scope": "Threshold obstructions; not a dimension-24 sharpness witness."}


def kernel_cap(delta):
    if delta < 16:
        return 0
    if delta < 32:
        return 16
    if delta < 48:
        return 24
    return 112  # No improved bound is asserted at or above 48.


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
    high = [case for case in cases if sum(case["ranks"]) >= 177]
    new = [case for case in high if sum(case["ranks"]) <= 192]
    require(all(case["excluded"] for case in high), "sum-176 frontier failed")
    require(max((case["ranks"][0] // 11) * (case["ranks"][1] // 11) for case in new) == 72,
            "new-range floor product changed")
    require(min(case["kernel_lower"] for case in new) == 28
            and all(case["kernel_upper"] == 24 for case in new), "new-range kernel margins changed")
    return {"rank_pairs_checked": len(cases), "pairs_above_176": len(high),
            "excluded_pairs_above_176": sum(case["excluded"] for case in high),
            "new_pairs_of_sum_177_through_192": len(new),
            "new_range_maximum_floor_product": 72,
            "new_range_minimum_kernel_lower": 28,
            "new_range_kernel_upper": 24,
            "boundary_control": screen(88, 88),
            "ordinary_control": screen(110, 110)}


def report():
    slices, entries = literal_source()
    pairs = pair_certificates()
    replay_pairs(pairs)
    return {"schema": "torus-rank-frontier-controls-v1", "field": "C",
            "source_sha256": check_sources(), "source_controls": source_controls(slices, entries),
            "rank24_pair_certificates": pairs, "middle_pair_controls": middle_pair_controls(slices),
            "rank48_threshold_controls": threshold_controls(pairs, slices),
            "rank_pair_controls": rank_pair_controls(),
            "claim_scope": {"source_rank_strict_upper": 48, "source_space_dimension_upper": 24,
                            "balanced_long_rank_sum_upper": 176, "dimension_bound_sharp": False,
                            "target_constructed": False, "improves_omega": False,
                            "proof_status": "proof-written-unreviewed", "independent_review": False}}


def replay_saved(document):
    require(document["schema"] == "torus-rank-frontier-controls-v1", "unknown evidence schema")
    require(document["source_sha256"] == check_sources(), "evidence source pins mismatch")
    replay_pairs(document["rank24_pair_certificates"])
    require(document == report(), "saved evidence or scope differs from exact regeneration")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="regenerate frozen evidence before replay")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2) + "\n")
    replay_saved(json.loads(RESULT.read_text()))
    print("PASS: 112 source slices, 8 rank-24 minors, 768 forbidden pairs, 80 rank-48 minors, 12321 rank pairs.")
    print("Written necessary bounds: source rank<48 implies dimension<=24; balanced long-rank sum<=176.")
    print("No sharpness, target construction, independent review, or exponent improvement is claimed.")


if __name__ == "__main__":
    main()

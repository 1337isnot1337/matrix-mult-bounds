"""Exact acceptance for the A4 source rank<80 and balanced sum144 bounds."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT_DIR = ROOT / "results/torus-rank80-2026-10-23"
CERTIFICATES = RESULT_DIR / "certificates.json"
RESULT = RESULT_DIR / "controls.json"
SHORT = tuple(product(range(4), repeat=2))
SOURCE = tuple(product(range(4), range(7), range(4)))
MULTIPLICITIES = (1, 2, 3, 4, 3, 2, 1)
SOURCE_PATHS = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-graded-quantum-flags/saturation.md",
    "research/ai/2026-10-23-torus-order-ideal/proof.md",
)
HEADER = {
    "schema": "torus-rank80-minors-v1", "coefficient_domain": "integers 0 and 1",
    "verification_modulus": 2,
    "mask_encoding": "canonical hexadecimal; bit n selects index n",
    "coherent_coordinate_order": "(i,s) lexicographic on range(4) x range(4)",
    "source_coordinate_order": "(i,k,s) lexicographic on range(4) x range(7) x range(4)",
}
FAMILIES = ("coherent20_pair", "coherent9_ideals", "coherent13_ideals", "source51_ideals")


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def check_sources(document=None):
    if document is None:
        document = json.loads((HERE / "sources.json").read_text())
    entries = document["local_dependencies"]
    require(tuple(item["path"] for item in entries) == SOURCE_PATHS, "changed source inventory")
    for item in entries:
        path = ROOT / item["path"]
        require(path.is_file(), "missing source prerequisite")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], "source digest mismatch")
    return {item["path"]: item["sha256"] for item in entries}


def literal_bases():
    coherent = {coordinate: set() for coordinate in SHORT}
    source = {coordinate: set() for coordinate in SOURCE}
    seen = set()
    for i, j, p, q, r, s in product(range(4), repeat=6):
        position = ((4 * j + p) * 7 + r + s, (4 * (i + j) + q) * 4 + r)
        require(position not in seen, "overlapping literal source coefficient labels")
        seen.add(position)
        source[i, p + q, s].add(position)
    for i, j, r, s in product(range(4), repeat=4):
        coherent[i, s].add((7 * j + r + s, 4 * (i + j) + r))
    require(len(seen) == 4096 and sum(map(len, coherent.values())) == 256,
            "literal source or coherent term count changed")
    return coherent, source


def source_controls(coherent, source):
    for i, k, s in SOURCE:
        expected = set()
        for p, q in product(range(4), repeat=2):
            if p + q != k:
                continue
            for row, column in coherent[i, s]:
                j, ell = divmod(row, 7)
                h, r = divmod(column, 4)
                expected.add(((4 * j + p) * 7 + ell, (4 * h + q) * 4 + r))
        require(source[i, k, s] == expected, "literal H_k tensor R factorization mismatch")
        rank = 16 * MULTIPLICITIES[k]
        require(len(expected) == rank
                and len({row for row, column in expected}) == rank
                and len({column for row, column in expected}) == rank,
                "monomial partial-permutation rank mismatch")
    middle_supports = [set().union(*(source[i, k, s] for i, s in SHORT)) for k in (1, 5)]
    row_sets = [{row for row, column in support} for support in middle_supports]
    column_sets = [{column for row, column in support} for support in middle_supports]
    require(not (row_sets[0] & row_sets[1]) and not (column_sets[0] & column_sets[1]),
            "middle1 and middle5 blocks are not disjoint on both legs")
    require(list(map(len, row_sets)) == list(map(len, column_sets)) == [56, 56],
            "middle block support size changed")
    return {"literal_source_terms": 4096, "literal_coherent_terms": 256,
            "source_basis_factorizations": 112,
            "middle_multiplicities": list(MULTIPLICITIES),
            "disjoint_middle_pair": [1, 5], "row_support_sizes": [56, 56],
            "column_support_sizes": [56, 56]}


def short_ideals(volume, ceiling=(4, 4, 4, 4)):
    """Independent recursive enumeration, optionally inside a preceding layer."""
    result, values = [], []

    def visit(position, remaining):
        if position == 4:
            if remaining == 0:
                result.append(tuple(values))
            return
        upper = min(ceiling[position], values[-1] if values else 4, remaining)
        for height in range(upper + 1):
            if remaining - height > 4 * (3 - position):
                continue
            values.append(height)
            visit(position + 1, remaining - height)
            values.pop()

    visit(0, volume)
    return tuple(result)


def remaining_profiles():
    profiles = []
    for n0 in range(17):
        for n1 in range(n0 + 1):
            for n2 in range(min(n1, 12) + 1):
                for n3 in range(min(n2, 4) + 1):
                    for n4 in range(min(n3, 4) + 1):
                        if n0 + n1 + n2 + n3 + n4 == 51:
                            profiles.append((n0, n1, n2, n3, n4, 0, 0))
    return tuple(profiles)


def remaining_ideals():
    result = []
    for profile in remaining_profiles():
        chosen = []

        def visit(k):
            if k == 5:
                result.append(tuple(chosen) + ((0, 0, 0, 0), (0, 0, 0, 0)))
                return
            parent = chosen[-1] if chosen else (4, 4, 4, 4)
            for shape in short_ideals(profile[k], parent):
                # At k3 the rank20 pair forbids both (0,1) and (1,0).
                if k == 3 and shape[0] >= 2 and shape[1] >= 1:
                    continue
                chosen.append(shape)
                visit(k + 1)
                chosen.pop()

        visit(0)
    return tuple(sorted(result))


def parse_mask(value, width):
    require(type(value) is str, "mask must be a hexadecimal string")
    try:
        mask = int(value, 16)
    except ValueError as error:
        raise ArithmeticError("invalid hexadecimal mask") from error
    require(0 <= mask < 1 << width and value == hex(mask), "mask is out of range or noncanonical")
    return mask


def indices(mask, width):
    return [index for index in range(width) if (mask >> index) & 1]


def invertible_mod2(rows, size):
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


def replay_minor(record, basis, coordinates, matrix_size, rank, allowed):
    expected_keys = {"coefficient_mask", "minor_rows_mask", "minor_columns_mask"}
    require(set(record) in (expected_keys, expected_keys | {"shape"}), "changed minor fields")
    mask = parse_mask(record["coefficient_mask"], len(coordinates))
    selected = [coordinates[index] for index in indices(mask, len(coordinates))]
    require(selected and set(selected) <= allowed, "coefficient support leaves its ideal")
    rows = indices(parse_mask(record["minor_rows_mask"], matrix_size), matrix_size)
    columns = indices(parse_mask(record["minor_columns_mask"], matrix_size), matrix_size)
    require(len(rows) == len(columns) == rank, "minor has the wrong dimensions")
    full_rows = [0] * matrix_size
    for coordinate in selected:
        for row, column in basis[coordinate]:
            full_rows[row] ^= 1 << column
    minor = [sum(((full_rows[row] >> column) & 1) << index
                 for index, column in enumerate(columns)) for row in rows]
    require(invertible_mod2(minor, rank), "saved integer minor is singular modulo two")


def replay_certificates(document=None, bases=None):
    if document is None:
        document = json.loads(CERTIFICATES.read_text())
    require(set(document) == set(HEADER) | set(FAMILIES), "changed certificate fields")
    require(all(document[key] == value for key, value in HEADER.items()), "changed certificate header")
    coherent, source = bases if bases is not None else literal_bases()
    pair = document["coherent20_pair"]
    require(pair["coefficient_mask"] == "0x12", "changed coherent rank20 pair")
    replay_minor(pair, coherent, SHORT, 28, 20, {(0, 1), (1, 0)})
    counts = {}
    for volume, rank, expected_count in ((9, 24, 7), (13, 28, 3)):
        expected = set(short_ideals(volume))
        require(len(expected) == expected_count, "coherent ideal inventory changed")
        seen = set()
        for record in document[f"coherent{volume}_ideals"]:
            shape = tuple(record["shape"])
            require(shape in expected and shape not in seen, "invalid or duplicate coherent ideal")
            seen.add(shape)
            allowed = {(i, s) for i, s in SHORT if s < shape[i]}
            replay_minor(record, coherent, SHORT, 28, rank, allowed)
        require(seen == expected, "incomplete coherent ideal coverage")
        counts[f"coherent{volume}_ideals"] = len(seen)
    expected = set(remaining_ideals())
    require(len(expected) == 24, "source51 leftover inventory changed")
    seen = set()
    for record in document["source51_ideals"]:
        shape = tuple(tuple(row) for row in record["shape"])
        require(shape in expected and shape not in seen, "invalid or duplicate source51 ideal")
        seen.add(shape)
        allowed = {(i, k, s) for i, k, s in SOURCE if s < shape[k][i]}
        replay_minor(record, source, SOURCE, 112, 80, allowed)
    require(seen == expected, "incomplete source51 ideal coverage")
    return {"coherent20_pair_minors": 1, **counts, "source51_ideals": len(seen),
            "integer_minors_checked": 35, "all_determinants_modulo_two": 1,
            "replay_uses_discovery": False,
            "field_transfer": "Each odd integer determinant is nonzero over C."}


def layer_controls():
    profiles = remaining_profiles()
    expected = {(16, 16, 12, 4, 3, 0, 0), (16, 16, 11, 4, 4, 0, 0),
                (16, 15, 12, 4, 4, 0, 0)}
    require(set(profiles) == expected, "remaining layer profiles changed")
    counts = Counter(tuple(map(sum, shape)) for shape in remaining_ideals())
    require(set(counts) == expected and set(counts.values()) == {8}, "leftover profile counts changed")
    return {"middle3_pair_rank_lower": 4 * 20, "middle2_13ideal_rank_lower": 3 * 28,
            "middle1_and_5_obstruction_rank_lower": 2 * 24 + 2 * 16,
            "middle5_nonempty_dimension_upper": 16 + 8 + 8 + 4 * 4,
            "middle4_empty_dimension_upper": 16 + 16 + 12 + 4,
            "remaining_dimension_upper_before_minors": 16 + 16 + 12 + 4 + 4,
            "remaining_profiles": [{"layer_sizes": list(profile), "ideals": counts[profile]}
                                   for profile in sorted(profiles)]}


def kernel_cap(delta):
    for threshold, bound in ((16, 0), (32, 16), (48, 24), (64, 32), (80, 50)):
        if delta < threshold:
            return bound
    return 112


def screen(b, c):
    require(type(b) is int and type(c) is int and 0 <= b <= 110 and 0 <= c <= 110,
            "invalid long-map rank")
    delta = 224 - b - c
    lower = 100 - (b // 11) * (c // 11)
    cap = kernel_cap(delta)
    ordinary = delta < 16
    return {"ranks": [b, c], "source_defect": delta, "kernel_lower": lower,
            "kernel_upper": cap, "ordinary_regularity_forced": ordinary,
            "excluded": lower > cap or ordinary}


def rank_pair_controls():
    cases = [screen(b, c) for b in range(111) for c in range(111)]
    high = [case for case in cases if sum(case["ranks"]) > 144]
    new = [case for case in high if sum(case["ranks"]) <= 160]
    require(all(case["excluded"] for case in high), "sum144 frontier failed")
    require(min(case["kernel_lower"] for case in new) == 51
            and all(case["kernel_upper"] == 50 for case in new), "new kernel margins changed")
    return {"rank_pairs_checked": len(cases), "pairs_above_144": len(high),
            "excluded_pairs_above_144": sum(case["excluded"] for case in high),
            "new_pairs_of_sum_145_through_160": len(new),
            "new_range_maximum_floor_product": 49, "new_range_minimum_kernel_lower": 51,
            "new_range_kernel_upper": 50, "boundary_control": screen(72, 72),
            "ordinary_control": screen(110, 110)}


def report():
    bases = literal_bases()
    return {"schema": "torus-rank80-controls-v1", "field": "C",
            "source_sha256": check_sources(),
            "certificates_sha256": hashlib.sha256(CERTIFICATES.read_bytes()).hexdigest(),
            "source_controls": source_controls(*bases),
            "minor_controls": replay_certificates(bases=bases),
            "layer_controls": layer_controls(), "rank_pair_controls": rank_pair_controls(),
            "claim_scope": {"source_rank_strict_upper": 80, "source_space_dimension_upper": 50,
                            "dimension_bound_sharp": False, "balanced_long_rank_sum_upper": 144,
                            "long_rank_sum_bound_sharp": False, "target_constructed": False,
                            "improves_omega": False, "formalized_proof": False,
                            "proof_status": "proof-written-unreviewed", "independent_review": False}}


def replay_saved(document):
    require(document["schema"] == "torus-rank80-controls-v1", "unknown evidence schema")
    require(document == report(), "saved evidence or scope differs from exact replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write aggregate controls before replay")
    args = parser.parse_args()
    if args.write:
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2) + "\n")
    replay_saved(json.loads(RESULT.read_text()))
    print("PASS: literal source/block factorization, 35 integer minors, all24 source51 leftovers, 12321 rank pairs.")
    print("Written necessary bounds: source rank<80 implies dimension<=50; balanced long-rank sum<=144.")
    print("No sharpness, target construction, formalization, or exponent improvement is claimed.")


if __name__ == "__main__":
    main()

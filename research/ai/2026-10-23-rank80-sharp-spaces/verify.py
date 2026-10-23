"""Exact acceptance for the sharp complex A4 source dimension44 below rank80."""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT_DIR = ROOT / "results/rank80-sharp-spaces-2026-10-23"
CERTIFICATES = RESULT_DIR / "certificates.json"
RESULT = RESULT_DIR / "controls.json"
SHORT = tuple(product(range(4), repeat=2))
SOURCE = tuple(product(range(4), range(7), range(4)))
MULTIPLICITIES = (1, 2, 3, 4, 3, 2, 1)
SOURCE_PATHS = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-23-torus-order-ideal/proof.md",
    "research/ai/2026-10-23-torus-rank80/proof.md",
    "results/torus-rank80-2026-10-23/certificates.json",
)
HEADER = {
    "schema": "rank80-sharp-spaces-minors-v1",
    "coefficient_domain": "integers 0 and 1", "verification_modulus": 2,
    "mask_encoding": "canonical hexadecimal; bit n selects index n",
    "coherent_coordinate_order": "(i,s) lexicographic on range(4) x range(4)",
    "source_coordinate_order": "(i,k,s) lexicographic on range(4) x range(7) x range(4)",
}
FAMILIES = ("coherent20_pair", "coherent9_ideals", "coherent13_ideals",
            "source45_ideals", "sharp44_space")
SHARP_SHAPE = ((4, 4, 4, 4), (4, 4, 4, 4), (4, 4, 4, 0),
               (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))


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
            "literal term count changed")
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
                "monomial rank mismatch")
    middle = [set().union(*(source[i, k, s] for i, s in SHORT)) for k in (1, 5)]
    row_sets = [{row for row, column in support} for support in middle]
    column_sets = [{column for row, column in support} for support in middle]
    require(not (row_sets[0] & row_sets[1]) and not (column_sets[0] & column_sets[1]),
            "middle1 and middle5 supports overlap")
    boundary_coordinates = [coordinate for coordinate in SOURCE if coordinate[0] < 2]
    boundary_support = set().union(*(source[coordinate] for coordinate in boundary_coordinates))
    boundary_columns = {column for row, column in boundary_support}
    require(len(boundary_coordinates) == 56 and len(boundary_columns) == 80,
            "strict rank80 boundary control changed")
    return {"literal_source_terms": 4096, "literal_coherent_terms": 256,
            "source_basis_factorizations": 112, "middle_multiplicities": list(MULTIPLICITIES),
            "disjoint_middle_pair": [1, 5],
            "weak_rank80_boundary": {"dimension": 56, "supported_columns": 80}}


@lru_cache(maxsize=None)
def short_ideals(volume, ceiling=(4, 4, 4, 4)):
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


def layer_profiles(volume=45):
    result, chosen = [], []

    def visit(k, remaining):
        if k == 7:
            if remaining == 0:
                result.append(tuple(chosen))
            return
        upper = min(chosen[-1] if chosen else 16, remaining)
        if k == 2:
            upper = min(upper, 12)
        if k >= 3:
            upper = min(upper, 4)
        for size in range(upper + 1):
            if size * (7 - k) < remaining:
                continue
            if k == 5 and size and chosen[1] > 8:
                continue
            chosen.append(size)
            visit(k + 1, remaining - size)
            chosen.pop()

    visit(0, volume)
    return tuple(result)


@lru_cache(maxsize=None)
def remaining_ideals():
    result = []
    for profile in layer_profiles():
        chosen = []

        def visit(k):
            if k == 7:
                result.append(tuple(chosen))
                return
            parent = chosen[-1] if chosen else (4, 4, 4, 4)
            for shape in short_ideals(profile[k], parent):
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
    selected = [coordinates[index] for index in indices(parse_mask(record["coefficient_mask"], len(coordinates)), len(coordinates))]
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


def sharpness_controls(record, source):
    require(set(record) == {"shape", "cover_rows_mask", "cover_columns_mask", "rank79_minor"},
            "changed sharpness fields")
    shape = tuple(tuple(row) for row in record["shape"])
    require(shape == SHARP_SHAPE, "changed sharp space")
    allowed = {(i, k, s) for i, k, s in SOURCE if s < shape[k][i]}
    require(len(allowed) == 44, "sharp space dimension changed")
    rows = set(indices(parse_mask(record["cover_rows_mask"], 112), 112))
    columns = set(indices(parse_mask(record["cover_columns_mask"], 112), 112))
    expected_rows = {(4 * j + p) * 7 + ell for j, p, ell in product(range(4), range(4), range(7))
                     if p == 0 or (p == 1 and j == 3)}
    expected_columns = {(4 * h + q) * 4 + r for h, q, r in product(range(7), range(4), range(4))
                        if (q == 0 and h <= 5) or (q == 1 and h <= 4)}
    require(rows == expected_rows and columns == expected_columns, "changed support cover")
    support = set().union(*(source[coordinate] for coordinate in allowed))
    require(all(row in rows or column in columns for row, column in support), "uncovered source coefficient")
    require(len(rows) == 35 and len(columns) == 44, "support-cover size changed")
    require(tuple(tuple(row) for row in record["rank79_minor"]["shape"]) == shape,
            "rank79 witness belongs to a different space")
    replay_minor(record["rank79_minor"], source, SOURCE, 112, 79, allowed)
    return {"dimension": 44, "cover_rows": len(rows), "cover_columns": len(columns),
            "uniform_rank_upper": 79, "attained_rank": 79,
            "literal_coefficients_covered": len(support), "cover_uses_matching_algorithm": False}


def replay_certificates(document=None, bases=None):
    if document is None:
        document = json.loads(CERTIFICATES.read_text())
    require(set(document) == set(HEADER) | set(FAMILIES), "changed certificate fields")
    require(all(document[key] == value for key, value in HEADER.items()), "changed certificate header")
    coherent, source = bases if bases is not None else literal_bases()
    pair = document["coherent20_pair"]
    require(pair["coefficient_mask"] == "0x12", "changed coherent rank20 pair")
    replay_minor(pair, coherent, SHORT, 28, 20, {(0, 1), (1, 0)})
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
    expected = set(remaining_ideals())
    require(len(expected) == 1709, "source45 inventory changed")
    seen = set()
    for record in document["source45_ideals"]:
        shape = tuple(tuple(row) for row in record["shape"])
        require(shape in expected and shape not in seen, "invalid or duplicate source45 ideal")
        seen.add(shape)
        allowed = {(i, k, s) for i, k, s in SOURCE if s < shape[k][i]}
        replay_minor(record, source, SOURCE, 112, 80, allowed)
    require(seen == expected, "incomplete source45 ideal coverage")
    sharp = sharpness_controls(document["sharp44_space"], source)
    histogram = Counter(tuple(map(sum, shape)) for shape in expected)
    return {"coherent_minors": 11, "source45_ideals": len(seen),
            "source45_layer_profiles": len(histogram), "sharp_space_minors": 1,
            "integer_minors_checked": 1721, "all_determinants_modulo_two": 1,
            "replay_uses_discovery": False, "sharpness": sharp,
            "field_transfer": "Each odd integer determinant is nonzero over C."}


def controls():
    pins = check_sources()
    bases = literal_bases()
    return {"schema": "rank80-sharp-spaces-controls-v1", "source_pins": pins,
            "source_controls": source_controls(*bases),
            "minor_controls": replay_certificates(bases=bases),
            "certificate_sha256": hashlib.sha256(CERTIFICATES.read_bytes()).hexdigest(),
            "claim_scope": {"claim_id": "AI-A4-RANK80-SHARP-LINEAR-SPACE-001",
                            "field": "C", "rank_strictly_less_than": 80,
                            "maximum_dimension": 44, "dimension_bound_sharp": True,
                            "arbitrary_complex_linear_spaces": True,
                            "order_ideal_reduction_characteristic_zero": True,
                            "target_rank_pair_application": False,
                            "matrix_target_constructed": False,
                            "smaller_exponent_established": False,
                            "independent_external_review": False,
                            "formalized": False}}


def replay_saved(document):
    require(document == controls(), "saved evidence or scope differs from exact replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write the exact acceptance record")
    args = parser.parse_args()
    report = controls()
    if args.write:
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report, indent=2) + "\n")
    else:
        require(json.loads(RESULT.read_text()) == report, "saved evidence or scope differs from exact replay")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

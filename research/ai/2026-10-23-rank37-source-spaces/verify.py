"""Exact acceptance for the sharp source dimension16 bound below rank37."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT_DIR = ROOT / "results/rank37-source-spaces-2026-10-23"
CERTIFICATES = RESULT_DIR / "certificates.json"
RESULT = RESULT_DIR / "controls.json"
SOURCE = tuple(product(range(4), range(7), range(4)))
SHORT = tuple(product(range(4), repeat=2))
MULTIPLICITIES = (1, 2, 3, 4, 3, 2, 1)
SOURCE_PATHS = ("research/ai/2026-10-20-koszul/cyclic_finite_target.md",
                "research/ai/2026-10-23-torus-order-ideal/proof.md",
                "research/ai/2026-10-23-torus-rank80/proof.md")
HEADER = {"schema": "rank37-source-minors-v1", "coefficient_domain": "integers 0 and 1",
          "verification_modulus": 2,
          "source_coordinate_order": "(i,k,s) lexicographic on range(4) x range(7) x range(4)",
          "coherent_coordinate_order": "(i,s) lexicographic on range(4) x range(4)",
          "mask_encoding": "canonical hexadecimal; bit n selects index n"}


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
    positions = set()
    for i, j, p, q, r, s in product(range(4), repeat=6):
        position = ((4 * j + p) * 7 + r + s, (4 * (i + j) + q) * 4 + r)
        require(position not in positions, "overlapping literal coefficient labels")
        positions.add(position)
        source[i, p + q, s].add(position)
    for i, j, r, s in product(range(4), repeat=4):
        coherent[i, s].add((7 * j + r + s, 4 * (i + j) + r))
    require(len(positions) == 4096, "literal source term count changed")
    return coherent, source


def source_controls(coherent, source):
    for i, k, s in SOURCE:
        support = source[i, k, s]
        expected = set()
        for p, q in product(range(4), repeat=2):
            if p + q != k:
                continue
            for row, column in coherent[i, s]:
                j, ell = divmod(row, 7)
                h, r = divmod(column, 4)
                expected.add(((4 * j + p) * 7 + ell, (4 * h + q) * 4 + r))
        require(support == expected, "coherent-block factorization failed")
        rank = 16 * MULTIPLICITIES[k]
        require(len(support) == len({r for r, c in support}) == len({c for r, c in support}) == rank,
                "monomial source rank changed")
    bottom = set().union(*(source[i, 0, s] for i, s in SHORT))
    require(len({r for r, c in bottom}) == len({c for r, c in bottom}) == 28,
            "dimension16 sharpness plane support changed")
    return {"literal_source_terms": 4096, "literal_coherent_terms": 256,
            "monomial_slices_and_factorizations": 112,
            "middle_multiplicities": list(MULTIPLICITIES),
            "sharpness_dimension": 16, "sharpness_middle_support": [0],
            "sharpness_uniform_rank_upper": 28}


def ideal_inventory():
    """Recursively fill both height rows, independently of discovery's shape products."""
    result, heights = [], []

    def visit(position, remaining):
        if position == 8:
            if remaining == 0:
                top = heights[4:8]
                if not (top[0] >= 2 and top[1] >= 1):
                    result.append((tuple(heights[:4]), tuple(top)))
            return
        k, i = divmod(position, 4)
        upper = min(4, heights[position - 1] if i else 4,
                    heights[position - 4] if k else 4, remaining)
        for height in range(upper + 1):
            if remaining - height > 4 * (7 - position):
                continue
            heights.append(height)
            visit(position + 1, remaining - height)
            heights.pop()

    visit(0, 17)
    return tuple(result)


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
    matrix = list(rows)
    require(len(matrix) == size and all(type(row) is int and 0 <= row < 1 << size for row in matrix),
            "invalid binary square matrix")
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
    chosen = [coordinates[n] for n in indices(parse_mask(record["coefficient_mask"], len(coordinates)), len(coordinates))]
    require(chosen and set(chosen) <= allowed, "coefficient support leaves its ideal")
    rows = indices(parse_mask(record["minor_rows_mask"], matrix_size), matrix_size)
    columns = indices(parse_mask(record["minor_columns_mask"], matrix_size), matrix_size)
    require(len(rows) == len(columns) == rank, "minor has the wrong dimensions")
    full_rows = [0] * matrix_size
    for coordinate in chosen:
        for row, column in basis[coordinate]:
            full_rows[row] ^= 1 << column
    minor = [sum(((full_rows[row] >> column) & 1) << index
                 for index, column in enumerate(columns)) for row in rows]
    require(invertible_mod2(minor, rank), "saved integer minor is singular modulo two")


def replay_certificates(document=None, bases=None):
    if document is None:
        document = json.loads(CERTIFICATES.read_text())
    require(set(document) == set(HEADER) | {"coherent20_pair", "source17_ideals"}, "changed certificate fields")
    require(all(document[key] == value for key, value in HEADER.items()), "changed certificate header")
    coherent, source = bases if bases is not None else literal_bases()
    pair = document["coherent20_pair"]
    require(pair["coefficient_mask"] == "0x12", "changed coherent rank20 pair")
    replay_minor(pair, coherent, SHORT, 28, 20, {(0, 1), (1, 0)})
    expected = set(ideal_inventory())
    require(len(expected) == 13, "size17 ideal inventory changed")
    seen = set()
    for record in document["source17_ideals"]:
        shape = tuple(tuple(row) for row in record["shape"])
        require(shape in expected and shape not in seen, "invalid or duplicate source17 ideal")
        seen.add(shape)
        allowed = {point for point in SOURCE if point[1] < 2 and point[2] < shape[point[1]][point[0]]}
        replay_minor(record, source, SOURCE, 112, 37, allowed)
    require(seen == expected, "incomplete source17 ideal coverage")
    counts = Counter(sum(shape[1]) for shape in expected)
    require(dict(counts) == {1: 1, 2: 2, 3: 4, 4: 6}, "axis-length counts changed")
    return {"coherent20_pair_minors": 1, "source37_minors": len(seen),
            "integer_minors_checked": 14, "all_determinants_modulo_two": 1,
            "axis_length_inventory": {str(k): counts[k] for k in sorted(counts)},
            "replay_uses_discovery": False,
            "field_transfer": "Every odd integer determinant is nonzero over C."}


def report():
    bases = literal_bases()
    return {"schema": "rank37-source-controls-v1", "field": "C",
            "source_sha256": check_sources(),
            "certificates_sha256": hashlib.sha256(CERTIFICATES.read_bytes()).hexdigest(),
            "source_controls": source_controls(*bases), "minor_controls": replay_certificates(bases=bases),
            "claim_scope": {"source_rank_strict_upper": 37, "source_space_dimension_upper": 16,
                            "dimension_bound_sharp": True, "mixed_leg_rank_consequence_claimed": False,
                            "target_constructed": False, "improves_omega": False,
                            "formalized_proof": False, "independent_review": False,
                            "proof_status": "proof-written-unreviewed"}}


def replay_saved(document):
    require(document["schema"] == "rank37-source-controls-v1", "unknown evidence schema")
    require(document == report(), "saved evidence or scope differs from exact replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2) + "\n")
    replay_saved(json.loads(RESULT.read_text()))
    print("PASS: 4096 source terms,112 factorizations,all13 size17 ideals and37-minors,coherent20-minor,sharp16-plane.")
    print("Written theorem: every complex A4 source space below rank37 has dimension<=16, sharply.")
    print("No mixed-leg rank consequence, target construction, or exponent improvement is claimed here.")


if __name__ == "__main__":
    main()

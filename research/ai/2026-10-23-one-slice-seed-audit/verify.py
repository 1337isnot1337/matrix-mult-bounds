"""Exact hypotheses and arithmetic for the Q(5,4) one-slice audit.

Only the Python standard library is used.  The all-power degeneration is
deduced in README.md from the cited theorem; this file does not construct
or claim to verify a complete Laurent degeneration map.
"""

from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
import os
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
SEED_PATH = "research/ai/2026-10-20-paired-construction/q54-exact.json"
SOURCE_DIMS = (25, 32, 32)
TARGET_DIMS = (16, 16, 16)


def reference_root():
    override = os.environ.get("MATRIX_BOUNDS_REFERENCE_REPO")
    return Path(override).resolve() if override else PACKAGE.parents[2]


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def matmul(left, right):
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("Incompatible nonempty matrix dimensions")
    columns = transpose(right)
    return [[sum(x*y for x, y in zip(row, column)) for column in columns]
            for row in left]


def rank(matrix):
    """Gaussian elimination over Q, with no floating-point decisions."""
    if not matrix:
        return 0
    work = [list(map(Fraction, row)) for row in matrix]
    rows, columns = len(work), len(work[0])
    if any(len(row) != columns for row in work):
        raise ValueError("Matrix must be rectangular")
    pivot_row = 0
    for column in range(columns):
        pivot = next((i for i in range(pivot_row, rows)
                      if work[i][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        for i in range(pivot_row+1, rows):
            if not work[i][column]:
                continue
            factor = work[i][column]/pivot_value
            work[i][column:] = [x-factor*y for x, y in
                               zip(work[i][column:], work[pivot_row][column:])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def determinant(matrix):
    work = [list(map(Fraction, row)) for row in matrix]
    size = len(work)
    if any(len(row) != size for row in work):
        raise ValueError("Matrix must be square")
    result = Fraction(1)
    for column in range(size):
        pivot = next((i for i in range(column, size) if work[i][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for i in range(column+1, size):
            if work[i][column]:
                factor = work[i][column]/pivot_value
                work[i][column:] = [x-factor*y for x, y in
                                   zip(work[i][column:], work[column][column:])]
    return result


def source_terms():
    return [(5*p+q, 8*y+q+v, 4*(p+y)+v)
            for p, q, y, v in product(range(5), range(5), range(4), range(4))]


def sparse_columns(matrix):
    return [[(i, matrix[i][j]) for i in range(len(matrix)) if matrix[i][j]]
            for j in range(len(matrix[0]))]


def seed_coefficient_check(maps):
    columns = [sparse_columns(matrix) for matrix in maps]
    tensor = {}
    for indices in source_terms():
        for entries in product(*(columns[leg][indices[leg]] for leg in range(3))):
            index = tuple(entry[0] for entry in entries)
            value = entries[0][1]*entries[1][1]*entries[2][1]
            tensor[index] = tensor.get(index, 0)+value
    failures = []
    nonzero = 0
    for a, b, c in product(range(16), repeat=3):
        i, h = divmod(a, 4)
        ii, j = divmod(b, 4)
        jj, hh = divmod(c, 4)
        expected = int(i == ii and j == jj and h == hh)
        value = tensor.get((a, b, c), 0)
        nonzero += int(value != 0)
        if value != expected:
            failures.append([a, b, c, value, expected])
    if failures:
        raise AssertionError(f"Seed coefficient mismatch: {failures[:3]}")
    return {"source_terms_checked": 400, "target_positions_checked": 4096,
            "target_nonzero_coefficients": nonzero, "coefficient_failures": 0}


def compressed_kernel_check(maps, leg):
    others = [i for i in range(3) if i != leg]
    left, right = [sparse_columns(maps[i]) for i in others]
    matrix = [[0]*SOURCE_DIMS[leg] for _ in range(256)]
    for term in source_terms():
        for i, x in left[term[others[0]]]:
            for j, y in right[term[others[1]]]:
                matrix[16*i+j][term[leg]] += x*y
    value = rank(matrix)
    return {"leg": "ABC"[leg], "source_dimension": SOURCE_DIMS[leg],
            "two_map_slice_space_rank_over_Q": value,
            "kernel_dimension_over_Q": SOURCE_DIMS[leg]-value}


def corner_slice_check(maps):
    _, bmap, cmap = maps
    functional = [int(i in (0, 24)) for i in range(25)]
    raw = [[0]*32 for _ in range(32)]
    for a, b, c in source_terms():
        raw[b][c] += functional[a]
    if any(sum(row) != 1 or any(x not in (0, 1) for x in row) for row in raw):
        raise AssertionError("Raw corner slice is not a permutation matrix")
    if any(sum(column) != 1 for column in transpose(raw)):
        raise AssertionError("Raw corner slice repeats a column")

    selected_b = [8*y+s for y in (0, 3) for s in range(8)]
    selected_c = [4*z+v for z in range(8) for v in (0, 3)]
    for matrix, selected in ((bmap, selected_b), (cmap, selected_c)):
        if any(matrix[i][j] for i in range(16) for j in range(32)
               if j not in selected):
            raise AssertionError("Long map uses an unselected short coordinate")
    det_b = determinant([[row[j] for j in selected_b] for row in bmap])
    det_c = determinant([[row[j] for j in selected_c] for row in cmap])
    if abs(det_b) != 1 or abs(det_c) != 1:
        raise AssertionError("Selected long maps are not unimodular")

    factor_indices = [(8*y+4*alpha+v, 4*(4*alpha+y)+v)
                      for alpha, y, v in product((0, 1), (0, 3), (0, 3))]
    xmap = [[row[b] for b, _ in factor_indices] for row in bmap]
    ymap = [[row[c] for _, c in factor_indices] for row in cmap]
    compressed = matmul(matmul(bmap, raw), transpose(cmap))
    if compressed != matmul(xmap, transpose(ymap)):
        raise AssertionError("Eight-term compressed factorization failed")

    augmented = [row+[0]*8 for row in raw]
    augmented += [[0]*32+[-int(i == j) for j in range(8)] for i in range(8)]
    extended_b = [row+xrow for row, xrow in zip(bmap, xmap)]
    extended_c = [row+yrow for row, yrow in zip(cmap, ymap)]
    cancellation = matmul(matmul(extended_b, augmented), transpose(extended_c))
    if any(value for row in cancellation for value in row):
        raise AssertionError("Appended-slice cancellation failed")
    return {
        "functional_nonzero_coordinates_A_pq": [[0, 0], [4, 4]],
        "raw_permutation_size": 32,
        "raw_rank_q": rank(raw),
        "left_compressed_rank": rank(matmul(bmap, raw)),
        "right_compressed_rank": rank(matmul(raw, transpose(cmap))),
        "both_compressed_rank_s": rank(compressed),
        "factor_column_pairs_B_C": [list(pair) for pair in factor_indices],
        "factor_column_ranks": [rank(xmap), rank(ymap)],
        "selected_long_map_determinants": [int(det_b), int(det_c)],
        "factorization_entries_checked": 256,
        "augmented_raw_slice_rank": rank(augmented),
        "augmented_cancellation_entries_checked": 256,
        "augmented_cancellation_failures": 0,
    }


def powered_parameters(k):
    if not isinstance(k, int) or isinstance(k, bool) or k < 1:
        raise ValueError("Power must be a positive integer")
    q, s, target_leg = 32**k, 8**k, 16**k
    return {"k": k, "raw_rank_q": q, "appended_slice_s": s,
            "target_other_leg_dimension": target_leg,
            "guaranteed_extracted_slice_t": q+s-2*target_leg,
            "square_matrix_dimension": 4**k}


def endpoint_comparison():
    h4 = Fraction(1)
    for j in range(1, 4):
        h4 *= Fraction(3*j+1, 3*j)
    pstar = h4*Fraction(13, 2)
    checks = [
        {"claim": "16*sqrt(2) < 23", "left": 512, "right": 23**2,
         "relation": "<"},
        {"claim": "32^(3/4) < 14", "left": 32**3, "right": 14**4,
         "relation": "<"},
        {"claim": "37 < (910/81)^(3/2)", "left": 37**2*pstar.denominator**3,
         "right": pstar.numerator**3, "relation": "<"},
    ]
    if not all(row["left"] < row["right"] for row in checks):
        raise AssertionError("Strict endpoint separation failed")
    return {"h_4": str(h4), "P_star_5_4": str(pstar),
            "integer_separator": 37, "strict_integer_comparisons": checks,
            "individual_character_values_assumed_equal": False,
            "equal_cyclic_assignment_survives": True,
            "actual_endpoint_character_exists_claimed": False}


def check_source_pins():
    data = json.loads((PACKAGE/"sources.json").read_text())
    checked = []
    for entry in data["local_dependencies"]:
        actual = sha256((reference_root()/entry["path"]).read_bytes()).hexdigest()
        if actual != entry["sha256"]:
            raise AssertionError(f"Dependency hash changed: {entry['path']}")
        checked.append({"path": entry["path"], "sha256": actual})
    return checked


@lru_cache(maxsize=1)
def certificate():
    source_pins = check_source_pins()
    data = json.loads((reference_root()/SEED_PATH).read_text())
    maps = data["maps_target_by_source"]
    if any(len(matrix) != 16 or any(len(row) != dim for row in matrix)
           for matrix, dim in zip(maps, SOURCE_DIMS)):
        raise AssertionError("Unexpected seed map dimensions")
    return {
        "source": "Q(5,4)", "target": "M(4,4,4)",
        "source_dimensions": list(SOURCE_DIMS), "target_dimensions": list(TARGET_DIMS),
        "coefficient_ring": "Z", "elimination_field": "Q",
        "seed_identity": seed_coefficient_check(maps),
        "fixed_seed_initial_slice_kernels": [compressed_kernel_check(maps, i)
                                               for i in range(3)],
        "corner_slice": corner_slice_check(maps),
        "powered_formula_controls": [powered_parameters(k) for k in (1, 2)],
        "all_power_formula": "M(4^k,4^k,4^k) + J_(32^k+8^k-2*16^k) <=deg Q(5,4)^k + J_(8^k)",
        "all_power_proof": "README.md, Section 3; Alman-Li v1, Propositions 5.3 and 5.4",
        "endpoint_comparison": endpoint_comparison(),
        "source_pins_checked": source_pins,
        "complete_laurent_map_supplied": False,
        "actual_degeneration_via_imported_theorem": True,
        "improves_omega": False,
        "independent_mathematical_review": False,
    }


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2))

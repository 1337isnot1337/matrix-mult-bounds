"""Exact Laurent collision of three current matrix cores into a jet trace.

The full source contraction, including every negative power and every mixed
coefficient, is replayed over integers. This is a constructive degeneration
control, not the unconstructed M27 + M7 target or an exponent improvement.
"""

import argparse
from collections import Counter, defaultdict
from copy import deepcopy
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPARSE = HERE / "parity_structure_jet_collision_sparse.json"
REPORT = HERE / "parity_structure_jet_collision_certificate.json"


def original_column(a, leg, i, middle, s):
    long = 2 * a - 1
    return ((i * long + middle) * a + s,
            (s * a + i) * long + middle,
            (middle * a + s) * a + i)[leg]


def source_terms(a):
    long = 2 * a - 1
    for i, j, p, q, r, s in product(range(a), repeat=6):
        yield ((i * long + p + q) * a + s,
               (j * a + p) * long + r + s,
               ((i + j) * a + q) * a + r)


def core_point(a, core, i, j):
    if core == 0:
        return i, j, 0
    if core == 1:
        return a - 1 - i, 2 * a - 2 - j, a - 1
    return j + 1, a - 1, a - 2 - i


def build(a=8):
    if type(a) is not int or a < 3:
        raise ValueError("The composed family requires an integer a >= 3")
    n = a - 2
    maps = [[], [], []]
    nodes, weights = (1, -1, 0), (1, 1, -2)
    for core, node in enumerate(nodes):
        for i, j, degree in product(range(n), range(n), range(3)):
            coefficient = node ** degree
            if not coefficient:
                continue
            row = degree * n * n + n * i + j
            point = core_point(a, core, i, j)
            for leg in range(3):
                power = degree - (2 if leg == 2 else 0)
                numerator = coefficient * (weights[core] if leg == 2 else 1)
                maps[leg].append([row, original_column(a, leg, *point), power, numerator])
    # Keep the unused final diagonal of each of the two M_(a-1) blocks.
    for core in (0, 1):
        point = core_point(a, core, n, n)
        for leg in range(3):
            maps[leg].append([3 * n * n + core,
                              original_column(a, leg, *point), 0, 2 if leg == 2 else 1])
    return {
        "format": "matrix-core-three-point-laurent-collision-v1",
        "source_lengths": [a, a], "source_leg_dimension": a * a * (2 * a - 1),
        "ordinary_intermediate_blocks": [n, n, n, 1, 1],
        "target": "M_n tensor truncated-polynomial trace of length3, direct sum two scalars",
        "matrix_core_size": n, "jet_length": 3, "target_leg_dimension": 3 * n * n + 2,
        "target_row_convention": "jet_degree*n*n + n*row + column; then two scalar rows",
        "evaluation_nodes": list(nodes), "third_leg_weight_numerators": list(weights),
        "map_denominators": [1, 1, 2],
        "entry_convention": ["target_row", "original_source_column", "epsilon_exponent", "integer_numerator"],
        "maps": maps, "full_target_27_plus_7_witness": False, "new_exponent_established": False,
    }


def contract_laurent(maps, source, source_dimension, target_dimension):
    """Integer numerator coefficients indexed by (power,xrow,yrow,zrow)."""
    if len(maps) != 3:
        raise ValueError("Exactly three Laurent maps are required")
    inverse = []
    for entries in maps:
        columns = defaultdict(list)
        occupied = set()
        for entry in entries:
            if (not isinstance(entry, list) or len(entry) != 4
                    or any(type(value) is not int for value in entry)):
                raise ValueError("A Laurent entry requires four integers")
            row, column, power, numerator = entry
            if not (0 <= row < target_dimension and 0 <= column < source_dimension and numerator):
                raise ValueError("A Laurent entry is out of range or has zero numerator")
            if (row, column, power) in occupied:
                raise ValueError("A Laurent coefficient is repeated")
            occupied.add((row, column, power))
            columns[column].append((row, power, numerator))
        inverse.append(columns)
    coefficients = Counter()
    source_count = 0
    selected_source_count = 0
    contributions = Counter()
    for point in source:
        source_count += 1
        if any(point[leg] not in inverse[leg] for leg in range(3)):
            continue
        selected_source_count += 1
        for terms in product(*(inverse[leg][point[leg]] for leg in range(3))):
            power = sum(term[1] for term in terms)
            coefficient = terms[0][2] * terms[1][2] * terms[2][2]
            rows = tuple(term[0] for term in terms)
            coefficients[(power,) + rows] += coefficient
            contributions[power] += 1
    actual = {key: value for key, value in coefficients.items() if value}
    metadata = {"source_terms_examined": source_count,
                "source_terms_meeting_all_three_maps": selected_source_count,
                "individual_contributions_by_power": {str(k): v for k, v in sorted(contributions.items())},
                "nonzero_coefficients_by_power": {str(k): v for k, v in sorted(Counter(key[0] for key in actual).items())}}
    return actual, metadata


def expected_polynomial(n, include_scalars=True, denominator=2):
    """Exact full family: jet-degree sums 2,4,6 give epsilon powers 0,2,4."""
    result = {}
    for dx, dy, dz in product(range(3), repeat=3):
        total = dx + dy + dz
        if total not in (2, 4, 6):
            continue
        for i, j, k in product(range(n), repeat=3):
            rows = (dx * n * n + n * i + j,
                    dy * n * n + n * j + k,
                    dz * n * n + n * k + i)
            result[(total - 2,) + rows] = denominator
    if include_scalars:
        for scalar in (3 * n * n, 3 * n * n + 1):
            result[0, scalar, scalar, scalar] = denominator
    return result


def scalar_control():
    maps = [[], [], []]
    for source_column, (node, weight) in enumerate(zip((1, -1, 0), (1, 1, -2))):
        for degree in range(3):
            if not node ** degree:
                continue
            for leg in range(3):
                maps[leg].append([degree, source_column,
                                  degree - (2 if leg == 2 else 0),
                                  node ** degree * (weight if leg == 2 else 1)])
    actual, metadata = contract_laurent(maps, ((i, i, i) for i in range(3)), 3, 3)
    if actual != expected_polynomial(1, include_scalars=False):
        raise ArithmeticError("The complete scalar three-point collision failed")
    # Constant slices: S0 is its own inverse; N=S1*S0 is nonzero nilpotent.
    slices = [[[int(i + j + k == 2) for k in range(3)] for j in range(3)] for i in range(3)]
    def multiply(left, right):
        return [[sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    identity = [[int(i == j) for j in range(3)] for i in range(3)]
    zero = [[0] * 3 for _ in range(3)]
    if multiply(slices[0], slices[0]) != identity:
        raise ArithmeticError("The scalar leading slice is not invertible")
    nilpotent = multiply(slices[1], slices[0])
    square = multiply(nilpotent, nilpotent)
    if square == zero or multiply(square, nilpotent) != zero:
        raise ArithmeticError("The normalized scalar slice does not have nilpotence index three")
    return {**metadata, "constant_target_terms": 6,
            "normalized_nonzero_nilpotent_slice": nilpotent,
            "nilpotence_index": 3,
            "ordinary_full_format_diagonal3_restriction_excluded_by_written_slice_argument": True,
            "border_rank_equals_three_by_conciseness_and_explicit_collision": True}


def verify(data=None, check_tamper=True):
    data = json.loads(SPARSE.read_text()) if data is None else data
    a, b = data["source_lengths"]
    if a != b or a < 3 or data["matrix_core_size"] != a - 2 or data["jet_length"] != 3:
        raise ValueError("Unexpected source or jet target")
    n = a - 2
    source_dimension, target_dimension = a * a * (2 * a - 1), 3 * n * n + 2
    if (data["source_leg_dimension"] != source_dimension
            or data["target_leg_dimension"] != target_dimension
            or data["map_denominators"] != [1, 1, 2]):
        raise ValueError("Unexpected format or coefficient denominator")
    actual, metadata = contract_laurent(data["maps"], source_terms(a), source_dimension, target_dimension)
    expected = expected_polynomial(n)
    if actual != expected:
        raise ArithmeticError("The complete Laurent tensor identity fails")
    tamper_rejected = None
    if check_tamper:
        changed = deepcopy(data)
        changed["maps"][0][0][3] *= 2
        tampered, _ = contract_laurent(changed["maps"], source_terms(a), source_dimension, target_dimension)
        tamper_rejected = tampered != expected
        if not tamper_rejected:
            raise ArithmeticError("A nonzero-to-nonzero Laurent coefficient tamper was accepted")
    return {"source": f"A({a},{a})", "matrix_core_size": n,
            "source_leg_dimension": source_dimension, "target_leg_dimension": target_dimension,
            "map_nonzero_monomials": [len(entries) for entries in data["maps"]],
            **metadata, "constant_target_terms": 6 * n ** 3 + 2,
            "all_negative_powers_cancel_exactly": True,
            "all_constant_mixed_and_unwanted_coefficients_zero": True,
            "complete_remainder_powers": [2, 4],
            "nonzero_to_nonzero_tamper_rejected": tamper_rejected,
            "scalar_genuinely_singular_control": scalar_control(),
            "standard_library_only": True, "full_target_27_plus_7_witness": False,
            "new_exponent_established": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        data = build()
        report = verify(data)
        SPARSE.write_text(json.dumps(data, separators=(",", ":")) + "\n")
        REPORT.write_text(json.dumps(report, indent=2) + "\n")
    else:
        report = verify()
    print(json.dumps(report, indent=2))

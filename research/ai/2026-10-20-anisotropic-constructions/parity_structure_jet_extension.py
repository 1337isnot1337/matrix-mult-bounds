"""Retain both off-diagonal arms in the current three-core Laurent collision.

This constructs and checks a full 3*n*n+4*n+2 dimensional limit.  It is a
positive control, not a restriction to the 778-dimensional matrix target.
The companion jet_collision module supplies only the exact source iterator
and generic sparse Laurent contraction; no numerical dependency is used.
"""

import argparse
from collections import Counter
from copy import deepcopy
import importlib.util
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPARSE = HERE / "parity_structure_jet_extension_sparse.json"
REPORT = HERE / "parity_structure_jet_extension_certificate.json"
_SPEC = importlib.util.spec_from_file_location(
    "_jet_extension_exact_helpers", HERE / "parity_structure_jet_collision.py")
_HELPERS = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_HELPERS)


def arm_row(n, core, direction, index):
    """direction 0 is the n-by-1 upper arm, direction 1 the 1-by-n lower."""
    return 3 * n * n + (2 * core + direction) * n + index


def scalar_row(n, core):
    return 3 * n * n + 4 * n + core


def build(a=8):
    if type(a) is not int or a < 3:
        raise ValueError("The family requires an integer a >= 3")
    n = a - 2
    maps = [[], [], []]
    for core, (node, weight) in enumerate(zip((1, -1, 0), (1, 1, -2))):
        for i, j, degree in product(range(n), range(n), range(3)):
            coefficient = node ** degree
            if coefficient:
                row = degree * n * n + n * i + j
                point = _HELPERS.core_point(a, core, i, j)
                for leg in range(3):
                    maps[leg].append([
                        row, _HELPERS.original_column(a, leg, *point),
                        3 * degree - (6 if leg == 2 else 0),
                        coefficient * (weight if leg == 2 else 1)])
    for core in (0, 1):
        for direction, index in product(range(2), range(n)):
            i, j = (index, n) if direction == 0 else (n, index)
            point = _HELPERS.core_point(a, core, i, j)
            for leg in range(3):
                maps[leg].append([
                    arm_row(n, core, direction, index),
                    _HELPERS.original_column(a, leg, *point),
                    3 - (6 if leg == 2 else 0),
                    1 if direction == 0 else 2])
        point = _HELPERS.core_point(a, core, n, n)
        for leg in range(3):
            maps[leg].append([
                scalar_row(n, core), _HELPERS.original_column(a, leg, *point),
                2 - (6 if leg == 2 else 0), 2 if leg == 2 else 1])
    return {
        "format": "matrix-core-jet-with-two-full-arms-v1",
        "source_lengths": [a, a],
        "source_leg_dimension": a * a * (2 * a - 1),
        "ordinary_intermediate_blocks": [n + 1, n + 1, n],
        "matrix_core_size": n,
        "target_leg_dimension": 3 * n * n + 4 * n + 2,
        "target_row_convention": "three n*n core degrees; then upper/lower n-arms for each of two cores; then two scalars",
        "map_denominators": [1, 1, 2],
        "entry_convention": ["target_row", "original_source_column", "parameter_exponent", "integer_numerator"],
        "maps": maps,
        "full_target_27_plus_7_witness": False,
        "new_exponent_established": False,
    }


def expected_polynomial(n):
    """Independent expansion of the three block traces, with denominator two."""
    result = {}
    # The three core traces undergo the collision at parameters +t^3,-t^3,0.
    for dx, dy, dz in product(range(3), repeat=3):
        total = dx + dy + dz
        if total in (2, 4, 6):
            for i, j, k in product(range(n), repeat=3):
                result[(3 * total - 6,
                        dx * n * n + n * i + j,
                        dy * n * n + n * j + k,
                        dz * n * n + n * k + i)] = 2
    for core, node in enumerate((1, -1)):
        u = lambda i: arm_row(n, core, 0, i)
        v = lambda i: arm_row(n, core, 1, i)
        d = scalar_row(n, core)
        # Exactly one extra matrix vertex: A_X*u_Y*v_Z and its two cyclic placements.
        for degree, i, j in product(range(3), range(n), range(n)):
            A = degree * n * n + n * i + j
            for rows in ((A, u(j), v(i)), (u(j), v(i), A), (v(i), A, u(j))):
                result[(3 * degree,) + rows] = 2 * node ** degree
        # Exactly two extra vertices. The Z scalar has an additional factor two.
        for i in range(n):
            result[2, d, v(i), u(i)] = 2
            result[2, u(i), d, v(i)] = 2
            result[2, v(i), u(i), d] = 4
        result[0, d, d, d] = 2
    return result


def concise_constant(coefficients, dimension):
    """Prove each flattening rank by its nonempty, pairwise-disjoint row supports."""
    constant = {key[1:]: value for key, value in coefficients.items() if key[0] == 0}
    ranks = []
    for axis in range(3):
        pivots, seen = {}, set()
        other = [i for i in range(3) if i != axis]
        for point, value in constant.items():
            if not value:
                raise ArithmeticError("A stored constant coefficient vanishes")
            column = tuple(point[i] for i in other)
            if column in pivots and pivots[column] != point[axis]:
                raise ArithmeticError("The disjoint-row-support flattening certificate failed")
            pivots[column] = point[axis]
            seen.add(point[axis])
        if seen != set(range(dimension)):
            raise ArithmeticError("The constant target loses a declared direction")
        ranks.append(len(seen))
    return ranks


def verify(data=None, check_tamper=True):
    data = json.loads(SPARSE.read_text()) if data is None else data
    a, b = data["source_lengths"]
    n = a - 2
    source_dimension = a * a * (2 * a - 1)
    target_dimension = 3 * n * n + 4 * n + 2
    if (a != b or a < 3 or data["matrix_core_size"] != n
            or data["source_leg_dimension"] != source_dimension
            or data["target_leg_dimension"] != target_dimension
            or data["map_denominators"] != [1, 1, 2]):
        raise ValueError("Unexpected source, target, or denominator")
    expected = expected_polynomial(n)
    actual, metadata = _HELPERS.contract_laurent(
        data["maps"], _HELPERS.source_terms(a), source_dimension, target_dimension)
    if actual != expected:
        raise ArithmeticError("The complete extended Laurent identity fails")
    ranks = concise_constant(actual, target_dimension)
    tamper_rejected = None
    if check_tamper:
        changed = deepcopy(data["maps"])
        # Tamper an arm rather than merely repeating the core test.
        index = next(index for index, term in enumerate(changed[0])
                     if term[0] == arm_row(n, 0, 0, 0))
        changed[0][index][3] *= 2
        tampered, _ = _HELPERS.contract_laurent(
            changed, _HELPERS.source_terms(a), source_dimension, target_dimension)
        tamper_rejected = tampered != expected
        if not tamper_rejected:
            raise ArithmeticError("A nonzero-to-nonzero arm tamper was accepted")
    value_counts = Counter(value for key, value in actual.items() if key[0] == 0)
    if value_counts != Counter({2: 6 * n ** 3 + 6 * n ** 2 + 2}):
        raise ArithmeticError("The constant coefficients are not normalized to one")
    return {
        "source": f"A({a},{a})", "matrix_core_size": n,
        "target_leg_dimension": target_dimension,
        "source_leg_dimension": source_dimension,
        "selected_original_source_columns_per_leg": [len({term[1] for term in entries}) for entries in data["maps"]],
        "map_nonzero_monomials": [len(entries) for entries in data["maps"]],
        **metadata,
        "constant_target_terms": 6 * n ** 3 + 6 * n ** 2 + 2,
        "constant_target_flattening_ranks": ranks,
        "retained_off_diagonal_directions_per_leg": 4 * n,
        "all_negative_powers_cancel_exactly": True,
        "every_constant_coefficient_equals_one": True,
        "all_unwanted_constant_coefficients_zero": True,
        "nonzero_to_nonzero_arm_tamper_rejected": tamper_rejected,
        "standard_library_only": True,
        "full_target_27_plus_7_witness": False,
        "new_exponent_established": False,
    }


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

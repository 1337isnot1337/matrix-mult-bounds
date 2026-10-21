"""Exact four-map obstruction and a corrected endpoint positive control."""

from collections import defaultdict
from copy import deepcopy
from itertools import product
import json
from pathlib import Path


FIXED_MAPS = [
    [[0, 13, 0, 1], [0, 14, 1, 1], [1, 14, 0, 1]],
    [[0, 13, 0, 1], [0, 14, 1, -1], [1, 14, 0, -1]],
    [[7, 1, 7, 1], [7, 0, 6, -1], [6, 0, 7, -1]],
    [[7, 1, 7, 1], [7, 0, 6, 1], [6, 0, 7, 1]],
]
CORRECTED_MAPS = [[[0, 13, 0, 1]], [[1, 14, 0, 1]],
                  [[6, 0, 7, 1]], [[7, 1, 7, 1]]]


def difference(first, second):
    values = defaultdict(int)
    for sign, rows in [(1, first), (-1, second)]:
        for i, k, s, value in rows:
            values[i, k, s] += sign * value
    return [[i, k, s, value] for (i, k, s), value in sorted(values.items()) if value]


def physical(entries):
    result = defaultdict(int)
    for i, k, s, value in entries:
        if not (0 <= i < 8 and 0 <= k < 15 and 0 <= s < 8):
            raise ValueError("A source coordinate is outside A88")
        for q in range(8):
            p = k - q
            if 0 <= p < 8:
                result[i * 8 + q, p * 8 + s] += value
    return {key: value for key, value in result.items() if value}


def trace_functional(first, second):
    left, right = physical(first), physical(second)
    product_matrix = defaultdict(int)
    for (i, j), u in left.items():
        for (jj, k), v in right.items():
            if j == jj:
                product_matrix[i, k] += u * v
    coefficients = defaultdict(int)
    for (row, column), value in product_matrix.items():
        p, s = divmod(row, 8)
        i, q = divmod(column, 8)
        coefficients[i, p + q, s] += value
    return {key: value for key, value in coefficients.items() if value}


def target_product():
    first = {(0, 25): 1, (1, 26): -1}
    second = {(25, 0): 1, (26, 1): -1}
    result = defaultdict(int)
    for (i, j), u in first.items():
        for (jj, k), v in second.items():
            if j == jj:
                result[i, k] += u * v
    return dict(result)


def verify_fixed_maps(maps):
    functional = trace_functional(difference(maps[0], maps[1]),
                                  difference(maps[2], maps[3]))
    for coordinate in product(range(8), range(15), range(8)):
        expected = -4 if coordinate == (0, 7, 7) else 0
        if functional.get(coordinate, 0) != expected:
            raise ArithmeticError("The fixed-map functional identity failed")
    return functional


def report():
    actual = verify_fixed_maps(FIXED_MAPS)
    extreme = trace_functional([[0, 14, 0, 1]], [[7, 0, 7, 1]])
    if extreme != {(0, 7, 7): 1}:
        raise AssertionError("The normalized extreme functional is incorrect")
    expected = target_product()
    if expected != {(0, 0): 1, (1, 1): 1}:
        raise AssertionError("The independent target matrix product failed")
    corrected = trace_functional(difference(CORRECTED_MAPS[0], CORRECTED_MAPS[1]),
                                 difference(CORRECTED_MAPS[2], CORRECTED_MAPS[3]))
    if corrected.get((1, 8, 7), 0) != 1:
        raise AssertionError("The corrected endpoint control did not escape")
    return {"source": "A(8,8)", "target_block": "M27 within M27 direct sum M7",
            "fixed_target_rows": [25, 53, 675, 703], "fixed_maps_common_order": deepcopy(FIXED_MAPS),
            "full_trace_functional_coordinates_checked": 960,
            "nonzero_obstruction_functional": [[*key, value] for key, value in actual.items()],
            "normalized_extreme_functional": [[*key, value] for key, value in extreme.items()],
            "target_product": [[*key, value] for key, value in expected.items()],
            "test_target_matrix_unit": [1, 1], "forced_source_value": 0, "required_target_value": 1,
            "corrected_endpoint_maps_common_order": deepcopy(CORRECTED_MAPS),
            "corrected_endpoint_value": 1,
            "completion_with_these_maps_fixed_excluded": True,
            "general_anchor_families_excluded": False,
            "arbitrary_source_restrictions_excluded": False,
            "new_exponent_established": False}


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[3] / "results" / "anisotropic-constructions-2026-10-20" / "fixed-anchor-obstruction.json"
    output.write_text(json.dumps(report(), indent=2) + "\n")
    print(output)

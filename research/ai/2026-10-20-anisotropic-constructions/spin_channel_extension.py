"""Exact eight-entry private-channel extension of the W34 spin core.

The result is a glued partial matrix tensor, not a full square tensor and
not a matrix-multiplication exponent improvement.  All acceptance uses
standard-library integer arithmetic.
"""

from collections import defaultdict
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parity_structure_spin_w34 as base
from crossed_module11 import unpack
from spin_module14 import column_entries, full_terms, pack
from parity_structure_spin_endpoint import determinant_mod


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
MAPS = DIRECTORY / "spin-channel-extension-maps.json"
MINOR = DIRECTORY / "spin-channel-extension-core-minor.json"
REPORT = DIRECTORY / "spin-channel-extension-certificate.json"


def coordinate(i, k, s):
    return (15*i+k)*8+s


def build_maps():
    exported = json.loads(base.MAPS.read_text())
    restriction = next(item for item in exported["restrictions"] if item["source"] == [8, 8])
    old = [unpack(restriction["maps"][name], (rows, 960)) for name, rows in zip("XYZ", (9, 84, 84))]
    denominators = [item[1] for item in old]
    X = [row[:] for row in old[0][0]]
    Y = [row[:] for index, row in enumerate(old[1][0]) if index % 28]
    Z = [row[:] for index, row in enumerate(old[2][0]) if index % 28]
    dx, dy, dz = denominators
    cells = []
    for start, j in product((3, 6), (5, 7)):
        a, b = 7-j, 8-j
        first_rows = (
            {coordinate(a, start+1, 0): 1, coordinate(b, start+2, 0): 1},
            {coordinate(a, start, 0): 2},
            {coordinate(b, start, 0): 1},
            {coordinate(a, start+2, 0): 1},
            {coordinate(b, start+2, 0): -2},
            {coordinate(b, start+1, 0): 1, coordinate(a, start, 0): 1},
        )
        for entries in first_rows:
            row = [0]*960
            for column, value in entries.items():
                row[column] = dx*value
            X.append(row)
        for p in (start, start+1):
            row = [0]*960
            row[coordinate(p, 0, j)] = dy
            Y.append(row)
        cells.append({"p_start": start, "last_short_index": j,
                      "first_short_indices": [a, b]})
    return [X, Y, Z], denominators, cells


def coefficient_replay(maps, denominators):
    sparse = [column_entries(matrix) for matrix in maps]
    image = defaultdict(int)
    response = defaultdict(lambda: defaultdict(int))
    source_count, active_count = 0, 0
    for x, y, z in full_terms(8, 8):
        source_count += 1
        yy, zz = sparse[1].get(y, ()), sparse[2].get(z, ())
        for row_y, value_y in yy:
            for row_z, value_z in zz:
                response[x][row_y, row_z] += value_y*value_z
        xx = sparse[0].get(x, ())
        if xx and yy and zz:
            active_count += 1
            for tx, cx in xx:
                for ty, cy in yy:
                    for tz, cz in zz:
                        image[tx, ty, tz] += cx*cy*cz
    image = {key: value for key, value in image.items() if value}
    response = {x: {pair: value for pair, value in row.items() if value}
                for x, row in response.items() if any(row.values())}
    scale = denominators[0]*denominators[1]*denominators[2]
    expected = {(3*I+J, 27*J+alpha, 27*I+alpha): scale
                for I, J, alpha in product(range(3), range(3), range(27))}
    expected.update({(9+3*v+I, 81+v, 27*I): scale
                     for v, I in product(range(8), range(3))})
    if image != expected:
        differences = [(key, image.get(key, 0), expected.get(key, 0))
                       for key in image.keys() | expected.keys()
                       if image.get(key, 0) != expected.get(key, 0)]
        raise ArithmeticError(f"The glued coefficient identity failed: {differences[:5]}")
    low = {coordinate(i, k, s) for i, k, s in product(range(8), range(3), range(8))}
    added = {coordinate(i, k, 0) for i, k in product(range(4), range(3, 9))}
    if set(response) != low | added:
        raise ArithmeticError("The exact216-coordinate response support changed")
    if any(pair[0] >= 81 for x in low for pair in response[x]):
        raise ArithmeticError("An added Y row has an unintended low-coordinate response")
    if any(pair[0] < 81 or pair[1] % 27 for x in added for pair in response[x]):
        raise ArithmeticError("The tail uses a nonprivate middle channel or an old Y row")
    return response, {"source_terms_checked": source_count,
                      "active_source_terms": active_count,
                      "target_dimensions": [33, 89, 81],
                      "target_coefficients_checked": 33*89*81,
                      "nonzero_target_coefficients": len(expected),
                      "integer_coefficient_scale": scale,
                      "new_first_response_support_coordinates": sorted(added)}


def check_core_minor(response, specification):
    rows = specification["source_rows"]
    pairs = [tuple(pair) for pair in specification["Y_Z_pairs"]]
    if (specification["prime"] != 65521 or len(rows) != 192 or len(set(rows)) != 192
            or len(pairs) != 192 or len(set(pairs)) != 192
            or any(type(x) is not int or (x//8) % 15 >= 3 for x in rows)
            or any(not (0 <= y < 81 and 0 <= z < 81) for y, z in pairs)):
        raise ArithmeticError("The retained-core minor labels are invalid")
    matrix = [[response[x].get(pair, 0) for pair in pairs] for x in rows]
    value = determinant_mod(matrix, 65521)
    if not value or value != specification["determinant_mod65521"]:
        raise ArithmeticError("The retained-core minor failed")
    return value


def verify(exported=None, specification=None):
    maps, denominators, cells = build_maps()
    export = {"source": "A(8,8)", "field": "Q",
              "target": "M(3,3,27) with eight private-channel Y entries and their24 X entries",
              "target_dimensions": [33, 89, 81], "private_middle_channel": 0,
              "deleted_original_middle_channel": 0,
              "private_original_middle_channel": 1,
              "maps": {name: pack(matrix, denominator) for name, matrix, denominator in zip("XYZ", maps, denominators)},
              "new_exponent_established": False}
    if exported is not None and exported != export:
        raise ArithmeticError("The actual exported maps disagree with the exact construction")
    response, replay = coefficient_replay(maps, denominators)
    specification = json.loads(MINOR.read_text()) if specification is None else specification
    minor = check_core_minor(response, specification)
    return {"source": "A(8,8)", "retained_core": "M(3,3,27)",
            "attached_Y_entries": 8, "attached_X_entries": 24,
            "middle_channels_filled_for_each_attached_vertex": 1,
            "required_middle_channels_for_full_vertex": 27,
            "cells": cells, "coefficient_replay": replay,
            "retained_core_response_rank_exact": 192,
            "retained_core_minor_determinant_mod65521": minor,
            "additional_response_rank_exact": 24, "full_response_rank_exact": 216,
            "first_preimage_dimension_after_extension": 960-216+33,
            "base_full_maps_sha256": hashlib.sha256(base.MAPS.read_bytes()).hexdigest(),
            "full_square_target_constructed": False,
            "new_exponent_established": False}, export


if __name__ == "__main__":
    report, exported = verify()
    MAPS.write_text(json.dumps(exported, indent=2)+"\n")
    checked, _ = verify(exported=json.loads(MAPS.read_text()))
    if checked != report:
        raise ArithmeticError("The saved-map replay changed the certificate")
    report["full_maps_sha256"] = hashlib.sha256(MAPS.read_bytes()).hexdigest()
    report["core_minor_sha256"] = hashlib.sha256(MINOR.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))

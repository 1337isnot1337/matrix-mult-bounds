"""An exact full-channel M(3,7,27) extension and its fixed-map response cost."""

import argparse
from collections import defaultdict
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crossed_module11 import unpack
from spin_module14 import column_entries, full_terms, pack
from parity_structure_spin_endpoint import determinant_mod

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
BASE = DIRECTORY / "parity_structure_spin_w34_full_maps.json"
MAPS = DIRECTORY / "parity_structure_spin_four_columns_maps.json"
MINORS = DIRECTORY / "parity_structure_spin_four_columns_response_minors.json"
REPORT = DIRECTORY / "parity_structure_spin_four_columns_certificate.json"


def column(i, k, s):
    return (15*i+k)*8+s


def build():
    """Reconstruct the maps with integer arithmetic from the frozen W34 seed."""
    original = json.loads(BASE.read_text())["restrictions"][1]["maps"]
    Xold, dx = unpack(original["X"], (9, 960))
    Yold, dy = unpack(original["Y"], (84, 960))
    Zold, dz = unpack(original["Z"], (84, 960))
    if (dx, dy, dz) != (2, 48, 24):
        raise ArithmeticError("The W34 denominator convention changed")
    retained = [28*vertex+alpha+1 for vertex in range(3) for alpha in range(27)]
    X = [[0]*960 for _ in range(21)]
    for I, J in product(range(3), repeat=2):
        X[7*I+J] = Xold[3*I+J][:]
    Y = [Yold[row][:] for row in retained]+[[0]*960 for _ in range(108)]
    Z = [Zold[row][:] for row in retained]

    assignments = {0: (0, 1), 14: (1, 1), 5: (2, 1)}
    remaining = [alpha for alpha in range(27) if alpha not in assignments]
    for number, alpha in enumerate(remaining):
        r, block = divmod(number, 3)
        H, j = 9+2*block, 3+2*block
        assignments[alpha] = r, j
        Z[alpha][column(r, H, 1)] += dz
        Z[27+alpha][column(r, H, 0)] += dz//2
        Z[27+alpha][column(r, H+1, 1)] -= dz//2
        Z[54+alpha][column(r, H+1, 0)] += dz

    for group, start in enumerate((3, 6)):
        images = (
            ((6, start+1, 0, 1), (7, start+2, 0, 1)),
            ((6, start, 0, 2),),
            ((7, start, 0, 1),),
            ((6, start+2, 0, 1),),
            ((7, start+2, 0, -2),),
            ((7, start+1, 0, 1), (6, start, 0, 1)),
        )
        for local, image in enumerate(images):
            vertex, I = divmod(local, 3)
            J = 3+2*group+vertex
            for i, k, s, coefficient in image:
                X[7*I+J][column(i, k, s)] += dx*coefficient
        for vertex in range(2):
            J, p = 3+2*group+vertex, start+vertex
            for alpha, (r, j) in assignments.items():
                Y[27*J+alpha][column(p, r, j)] = dy

    return {
        "source": [8, 8], "target": [3, 7, 27], "field": "Q",
        "target_coordinate_orders": ["7*I+J", "27*J+alpha", "27*I+alpha"],
        "source_coordinate_order": "(i*15+k)*8+s",
        "new_channel_assignments_r_j": {str(alpha): list(assignments[alpha]) for alpha in range(27)},
        "maps": {name: pack(matrix, denominator)
                 for name, matrix, denominator in zip("XYZ", (X, Y, Z), (dx, dy, dz))},
        "new_exponent_established": False,
    }


def parse(data):
    if (data["source"] != [8, 8] or data["target"] != [3, 7, 27]
            or data["field"] != "Q" or data.get("new_exponent_established") is not False):
        raise ArithmeticError("The full-channel construction scope changed")
    parsed = [unpack(data["maps"][name], (rows, 960))
              for name, rows in zip("XYZ", (21, 189, 81))]
    return [item[0] for item in parsed], [item[1] for item in parsed]


def contraction(maps):
    inverse = [column_entries(matrix) for matrix in maps]
    tensor = defaultdict(int)
    response = defaultdict(lambda: defaultdict(int))
    count = 0
    for x, y, z in full_terms(8, 8):
        count += 1
        xe, ye, ze = (inverse[0].get(x, ()), inverse[1].get(y, ()), inverse[2].get(z, ()))
        for ty, cy in ye:
            for tz, cz in ze:
                value = cy*cz
                response[x][81*ty+tz] += value
                for tx, cx in xe:
                    tensor[tx, ty, tz] += cx*value
    tensor = {key: value for key, value in tensor.items() if value}
    response = {x: {pair: value for pair, value in row.items() if value}
                for x, row in response.items() if any(row.values())}
    return tensor, response, count


def check_response(response, specification):
    support = {column(i, k, s) for i, k, s in product(range(8), range(9), range(8))}
    if set(response) != support or specification["prime"] != 65521:
        raise ArithmeticError("The exact 576-coordinate response support changed")
    bands = ((0, 81), (81, 135), (135, 189))
    if [block["block"] for block in specification["blocks"]] != [0, 1, 2]:
        raise ArithmeticError("The response block list is malformed")
    for x, row in response.items():
        block = ((x//8) % 15)//3
        low, high = bands[block]
        if any(not low <= pair//81 < high for pair in row):
            raise ArithmeticError("The three response output blocks are not disjoint")
    reports = []
    for block in specification["blocks"]:
        number = block["block"]
        rows, columns = block["source_rows"], block["target_pair_columns"]
        wanted = {column(i, k, s) for i, k, s in
                  product(range(8), range(3*number, 3*number+3), range(8))}
        low, high = bands[number]
        if (len(rows) != 192 or len(set(rows)) != 192 or set(rows) != wanted
                or len(columns) != 192 or len(set(columns)) != 192
                or any(type(pair) is not int or not 81*low <= pair < 81*high for pair in columns)):
            raise ArithmeticError("A response minor has invalid rows or columns")
        matrix = [[response[row].get(pair, 0) for pair in columns] for row in rows]
        determinant = determinant_mod(matrix, 65521)
        if not determinant or determinant != block["determinant_mod65521"]:
            raise ArithmeticError("A regenerated response minor failed")
        reports.append({"long_source_coordinates": list(range(3*number, 3*number+3)),
                        "source_coordinate_upper_bound": 192,
                        "minor_dimension": 192, "determinant_mod65521": determinant,
                        "rank_exact": 192})
    return reports


def verify(data=None, specification=None):
    data = json.loads(MAPS.read_text()) if data is None else data
    specification = json.loads(MINORS.read_text()) if specification is None else specification
    maps, denominators = parse(data)
    image, response, count = contraction(maps)
    scale = denominators[0]*denominators[1]*denominators[2]
    expected = {(7*I+J, 27*J+alpha, 27*I+alpha): scale
                for I, J, alpha in product(range(3), range(7), range(27))}
    if image != expected:
        raise ArithmeticError("The complete M(3,7,27) coefficient identity failed")
    blocks = check_response(response, specification)
    return {
        "source": "A(8,8)", "target": "M(3,7,27)", "field": "Q",
        "map_denominators": denominators, "integer_coefficient_scale": scale,
        "map_nonzero_counts": [sum(bool(value) for row in matrix for value in row) for matrix in maps],
        "source_terms_checked": count, "target_coefficients_checked": 21*189*81,
        "nonzero_target_coefficients": len(image),
        "response_source_coordinate_upper_bound": len(response),
        "response_blocks": blocks, "full_first_response_rank_exact": 576,
        "first_target_dimension": 21, "first_response_preimage_dimension": 960-576+21,
        "fixed_map_extension_bound_only": True,
        "full_square_target_constructed": False, "new_exponent_established": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-maps", action="store_true")
    args = parser.parse_args()
    if args.write_maps:
        MAPS.write_text(json.dumps(build(), indent=2)+"\n")
    report = verify()
    report["maps_sha256"] = hashlib.sha256(MAPS.read_bytes()).hexdigest()
    report["response_minors_sha256"] = hashlib.sha256(MINORS.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))

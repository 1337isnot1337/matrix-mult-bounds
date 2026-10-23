"""Exact complete-source replay of a simple-pole coupled spin repair."""

import argparse
from collections import defaultdict
import hashlib
from itertools import product
import json
from math import lcm
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crossed_module11 import modular_rank, multiply, unpack
from spin_module14 import column_entries, full_terms
from parity_structure_spin_endpoint import determinant_mod

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
MAPS = DIRECTORY / "parity_structure_spin_w34_laurent_maps.json"
MINOR = DIRECTORY / "parity_structure_spin_w34_laurent_response_minor.json"
REPORT = DIRECTORY / "parity_structure_spin_w34_laurent_certificate.json"


def parse(data):
    if (data.get("new_exponent_established") is not False
            or data["source"] != [8, 8] or data["target"] != [3, 3, 27]
            or data["endpoint_coordinate"] != [7, 0, 7]):
        raise ArithmeticError("The Laurent construction has a different scope")
    maps, denominators = [], []
    for axis, name in enumerate("XYZ"):
        wanted = ({"0"}, {"-1", "0"}, {"0", "1"})[axis]
        if set(data["maps"][name]) != wanted:
            raise ArithmeticError("The allowed Laurent powers changed")
        terms, common = {}, 1
        for power, item in data["maps"][name].items():
            matrix, denominator = unpack(item, ((9, 960), (81, 960), (81, 960))[axis])
            terms[int(power)] = (matrix, denominator)
            common = lcm(common, denominator)
        maps.append({power: [[value*(common//denominator) for value in row] for row in matrix]
                     for power, (matrix, denominator) in terms.items()})
        denominators.append(common)
    for matrix in maps[1].values():
        if any(value and column//120 > 1 for row in matrix for column, value in enumerate(row)):
            raise ArithmeticError("The second map left the p=0,1 source space")
    for matrix in maps[2].values():
        if any(value and column % 8 > 1 for row in matrix for column, value in enumerate(row)):
            raise ArithmeticError("The third map left the q=0,1 source space")
    return maps, denominators


def polynomial_inverse(terms):
    inverse = defaultdict(list)
    for power, matrix in terms.items():
        for column, entries in column_entries(matrix).items():
            inverse[column].extend((row, power, value) for row, value in entries)
    return inverse


def specialize_one(maps):
    answer = []
    for axis in maps:
        matrices = list(axis.values())
        answer.append([[sum(matrix[i][j] for matrix in matrices)
                        for j in range(960)] for i in range(len(matrices[0]))])
    return answer


def response_one(specialized):
    Y, Z = (column_entries(matrix) for matrix in specialized[1:])
    response = defaultdict(lambda: defaultdict(int))
    for x, y, z in full_terms(8, 8):
        for ty, cy in Y.get(y, ()):
            for tz, cz in Z.get(z, ()):
                response[x][81*ty+tz] += cy*cz
    return {x: {pair: value for pair, value in row.items() if value}
            for x, row in response.items() if any(row.values())}


def verify(data=None, specification=None, check_response=True):
    data = json.loads(MAPS.read_text()) if data is None else data
    maps, denominators = parse(data)
    inverse = [polynomial_inverse(axis) for axis in maps]
    image = defaultdict(int)
    endpoint = defaultdict(int)
    source_count = 0
    endpoint_column = (7*15)*8+7
    for x, y, z in full_terms(8, 8):
        source_count += 1
        ye, ze = inverse[1].get(y, ()), inverse[2].get(z, ())
        if x == endpoint_column:
            for ty, py, cy in ye:
                for tz, pz, cz in ze:
                    endpoint[py+pz, ty, tz] += cy*cz
        for tx, px, cx in inverse[0].get(x, ()):
            for ty, py, cy in ye:
                for tz, pz, cz in ze:
                    image[px+py+pz, tx, ty, tz] += cx*cy*cz
    image = {key: value for key, value in image.items() if value}
    scale = denominators[0]*denominators[1]*denominators[2]
    expected = {(0, 3*i+j, 27*j+alpha, 27*i+alpha): scale
                for i, j, alpha in product(range(3), range(3), range(27))}
    if image != expected:
        differences = [(key, image.get(key, 0), expected.get(key, 0))
                       for key in image.keys() | expected.keys()
                       if image.get(key, 0) != expected.get(key, 0)]
        raise ArithmeticError(f"The complete Laurent coefficient identity failed: {differences[:4]}")
    if any(endpoint.values()):
        raise ArithmeticError("The endpoint response is not identically zero in t")

    B, db = unpack(data["auxiliary"]["pole_row_coefficients_B"], (81, 3))
    N, dn = unpack(data["auxiliary"]["endpoint_zero_deleted_Y_rows"], (3, 960))
    actual = multiply(B, N)
    pole = maps[1][-1]
    if any(actual[i][j]*denominators[1] != pole[i][j]*db*dn
           for i in range(81) for j in range(960)):
        raise ArithmeticError("The saved factorization of the polar map failed")
    # The unused third column gives a rational upper bound; the two
    # modular lower bounds then certify exact rank, rather than merely
    # suggesting it from a reduction modulo one prime.
    if any(row[2] for row in B) or modular_rank(B) != 2 or modular_rank(pole) != 2:
        raise ArithmeticError("The polar map does not have the stated exact rank2")

    report = {
        "source": "A(8,8)", "target": "M(3,3,27)", "field": "Q(t)",
        "map_degrees": {"X": [0], "Y": [-1, 0], "Z": [0, 1]},
        "common_leg_denominators": denominators, "integer_coefficient_scale": scale,
        "source_terms_checked": source_count,
        "all_Laurent_target_coefficients_checked": 3*9*81*81,
        "nonzero_constant_target_coefficients": len(image),
        "negative_power_coefficients_zero": True, "positive_power_coefficients_zero": True,
        "endpoint": [7, 0, 7], "endpoint_all_Laurent_coefficients_checked": 3*81*81,
        "endpoint_response_identically_zero": True, "polar_map_rank_exact": 2,
        "full_square_target_constructed": False, "new_exponent_established": False,
    }
    if check_response:
        specification = json.loads(MINOR.read_text()) if specification is None else specification
        response = response_one(specialize_one(maps))
        rows, columns = specification["source_rows"], specification["target_pair_columns"]
        if (specification["prime"] != 65521 or len(rows) != 191 or len(set(rows)) != 191
                or len(columns) != 191 or len(set(columns)) != 191
                or any(type(row) is not int or row not in response for row in rows)
                or any(type(column) is not int or not 0 <= column < 81**2 for column in columns)):
            raise ArithmeticError("The specialized response minor is malformed")
        matrix = [[response[row].get(column, 0) for column in columns] for row in rows]
        determinant = determinant_mod(matrix, 65521)
        if not determinant or determinant != specification["determinant_mod65521"]:
            raise ArithmeticError("The specialized response minor failed")
        if (len(response) != 191 or endpoint_column in response
                or any((column//8) % 15 > 2 for column in response)):
            raise ArithmeticError("The specialized response upper bound changed")
        report.update({"specialization": "t=1", "specialized_response_rank_exact": 191,
                       "specialized_response_minor_determinant_mod65521": determinant})
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--without-response", action="store_true")
    args = parser.parse_args()
    report = verify(check_response=not args.without_response)
    report["maps_sha256"] = hashlib.sha256(MAPS.read_bytes()).hexdigest()
    if not args.without_response:
        report["response_minor_sha256"] = hashlib.sha256(MINOR.read_bytes()).hexdigest()
        REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))

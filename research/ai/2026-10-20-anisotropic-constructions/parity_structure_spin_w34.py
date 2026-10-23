"""Standard-library replay of the four-chain spin module and its rank data.

This checks the saved rational maps, all full-source coefficients, a
192-dimensional response, and the exact three-dimensional G1 kernel.
It does not establish a full square target or an exponent improvement.
"""

from collections import defaultdict
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crossed_module11 import (determinant, horizontal, j_shift, k_shift,
                              modular_rank, multiply, transpose, unpack)
from spin_module14 import check_product, column_entries, full_terms, lift, pack, reduced_terms
from parity_structure_spin_endpoint import determinant_mod


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
WITNESS = DIRECTORY / "parity_structure_spin_w34_witness.json"
MAPS = DIRECTORY / "parity_structure_spin_w34_full_maps.json"
RESPONSE_MINOR = DIRECTORY / "parity_structure_spin_w34_response_minor.json"
G1_KERNEL = DIRECTORY / "parity_structure_spin_w34_g1_delete0_kernel.json"
REPORT = DIRECTORY / "parity_structure_spin_w34_certificate.json"


def construction_checks(witness, maps, denominators):
    profile, generators = witness["profile"], witness["generators"]
    if profile != [4, 3, 3, 3] or len(generators) != 4:
        raise ArithmeticError("The four-chain profile changed")
    columns = []
    for length, generator in zip(profile, generators):
        if len(generator) != 5-length or any(len(row) != 8 for row in generator):
            raise ArithmeticError("A chain generator has the wrong dimensions")
        for shift in range(length):
            column = [0]*32
            for a, row in enumerate(generator):
                for j, value in enumerate(row):
                    if type(value) is not int:
                        raise ArithmeticError("The chain generators must be integral")
                    column[8*(a+shift)+j] = value
            columns.append(column)
    U = transpose(columns)
    Q, _ = unpack(witness["U_left_annihilator"], (19, 32))
    if (modular_rank(U) != 13 or modular_rank(Q) != 19
            or any(any(row) for row in multiply(Q, U))):
        raise ArithmeticError("The thirteen-dimensional subspace is incorrect")

    def left(matrix, index):
        p, s = divmod(index, 2)
        shifted = j_shift(matrix, s)
        zero = [[0]*len(matrix[0]) for _ in range(40)]
        return shifted+zero if p == 0 else zero+shifted

    Wfull = horizontal(*(left(U, index) for index in range(4)))
    indices = witness["W_basis_column_indices"]
    if (len(indices) != 34 or len(set(indices)) != 34
            or any(type(index) is not int or not 0 <= index < 52 for index in indices)):
        raise ArithmeticError("The ignored-space basis selection changed")
    W = [[row[index] for index in indices] for row in Wfull]
    if modular_rank(W) != 34 or 2*sum(length+1 for length in profile) != 34:
        raise ArithmeticError("The ignored-space dimension is not34")

    X, Y, Z = maps
    dx, dy, dz = denominators
    expected_X = []
    for index in range(9):
        a, b, c, d, e, f, g, h, i = [int(index == j) for j in range(9)]
        expected_X.append([2*(e+i), 4*d-h, b, 2*a, 2*c, -b,
                           h, 2*g, 2*i, -h, b-4*f, 2*(a+e)])
    if dx != 2 or X != expected_X:
        raise ArithmeticError("The specified spin-one first map changed")

    plus = transpose([row[36:] for row in Z[:14]])
    minus = transpose([row[:36] for row in Z[28:]])
    if any(any(row[:36]) for row in Z[:14]) or any(any(row[36:]) for row in Z[28:]):
        raise ArithmeticError("The endpoint-pair block form is incorrect")
    for channel, column in product(range(14), range(36)):
        if (2*Z[14+channel][column] != plus[column][channel]
                or 2*Z[14+channel][36+column] != -minus[column][channel]):
            raise ArithmeticError("The central spin block is incorrect")
    v = k_shift(plus, 0)
    difference = [[a-b for a, b in zip(row0, row1)]
                  for row0, row1 in zip(v, k_shift(minus, 1))]
    for residual in (k_shift(plus, 1), k_shift(minus, 0), difference):
        if any(any(row) for row in multiply(Q, residual)):
            raise ArithmeticError("An endpoint-pair relation failed")

    q0, q1 = [], []
    for row in Q:
        q0.append([row[8*a+H] if H < 8 else 0 for a in range(4) for H in range(9)])
        q1.append([row[8*a+H-1] if H else 0 for a in range(4) for H in range(9)])
    constraints = [row+[0]*36 for row in q1] + [[0]*36+row for row in q0]
    constraints += [row0+[-value for value in row1] for row0, row1 in zip(q0, q1)]
    if modular_rank(constraints) != 57:
        raise ArithmeticError("The endpoint-pair space does not have dimension15")

    L = [left(v, index) for index in range(4)]
    central = [[a-b for a, b in zip(row0, row3)] for row0, row3 in zip(L[0], L[3])]
    B = horizontal([[2*dz*value for value in row] for row in W],
                   [[2*value for value in row] for row in L[1]],
                   central, [[2*value for value in row] for row in L[2]])
    expected = [[2*dy*dz*int(j == 34+i) for j in range(76)] for i in range(42)]
    if multiply(Y, B) != expected:
        raise ArithmeticError("The saved map is not the exact76-column join dual")
    rows = witness["join_row_indices"]
    if (len(rows) != 76 or len(set(rows)) != 76
            or any(type(row) is not int or not 0 <= row < 80 for row in rows)):
        raise ArithmeticError("The join minor rows are invalid")
    actual = Fraction(determinant([B[row] for row in rows]), (2*dz)**76)
    if actual != Fraction(witness["join_minor_determinant"]) or not actual:
        raise ArithmeticError("The rational join determinant disagrees")
    return {"U_dimension": 13, "ignored_space_dimension": 34,
            "pair_space_dimension": 15, "selected_channels": 14,
            "join_rank": 76, "join_minor_determinant": str(actual),
            "exact_endpoint_pair_relations": True, "exact_join_duality": True}


def full_response(maps):
    """Return complete integer Y/Z responses in original common coordinates."""
    Y, Z = (column_entries(matrix) for matrix in maps[1:])
    answer = defaultdict(lambda: defaultdict(int))
    for x, y, z in full_terms(8, 8):
        for row_y, value_y in Y.get(y, ()):
            for row_z, value_z in Z.get(z, ()):
                answer[x][84*row_y+row_z] += value_y*value_z
    return {coordinate: {pair: value for pair, value in row.items() if value}
            for coordinate, row in answer.items() if any(row.values())}


def check_response_minor(response, specification):
    rows, columns = specification["source_rows"], specification["target_pair_columns"]
    if (specification["prime"] != 65521 or len(rows) != 192 or len(set(rows)) != 192
            or len(columns) != 192 or len(set(columns)) != 192
            or any(type(row) is not int or row not in response for row in rows)
            or any(type(column) is not int or not 0 <= column < 84**2 for column in columns)):
        raise ArithmeticError("The response minor specification is invalid")
    matrix = [[response[row].get(column, 0) for column in columns] for row in rows]
    actual = determinant_mod(matrix, 65521)
    if not actual or actual != specification["determinant_mod65521"]:
        raise ArithmeticError("The rebuilt response minor failed")
    if len(response) != 192 or any((row//8) % 15 > 2 for row in response):
        raise ArithmeticError("The192-coordinate response upper bound changed")
    return actual


def check_g1_kernel(Z, specification):
    """Check the complete4992-row transfer, including the rational upper bound."""
    if (specification["deleted_middle"] != 0
            or specification["excluded_retained_middle"] != 1
            or specification["prime"] != 65521):
        raise ArithmeticError("The G1 scope or field changed")
    sparse_vectors = specification["kernel_vectors"]
    vectors = []
    for entries in sparse_vectors:
        vector = [0]*120
        for column, value in entries:
            if (type(column) is not int or not 0 <= column < 120
                    or type(value) is not int or not value or vector[column]):
                raise ArithmeticError("A G1 kernel vector is malformed")
            vector[column] = value
        vectors.append(vector)
    if len(vectors) != 3 or modular_rank(vectors) != 3:
        raise ArithmeticError("The three G1 kernel vectors are not independent")

    def coefficient(label, column):
        i, s, I, beta = label
        L, j = divmod(column, 8)
        r = L-s
        return Z[28*I+beta][(r*15+i+j)*8+1] if 0 <= r < 8 else 0

    for label in product(range(8), range(8), range(3), range(2, 28)):
        for entries in sparse_vectors:
            if sum(value*coefficient(label, column) for column, value in entries):
                raise ArithmeticError("A claimed G1 kernel vector is not annihilated")
    rows, columns = specification["minor_row_labels"], specification["minor_columns"]
    if (len(rows) != 117 or len(set(map(tuple, rows))) != 117
            or len(columns) != 117 or len(set(columns)) != 117
            or any(type(column) is not int or not 0 <= column < 120 for column in columns)):
        raise ArithmeticError("The G1 minor dimensions are invalid")
    for label in rows:
        if (len(label) != 4 or any(type(value) is not int for value in label)
                or not (0 <= label[0] < 8 and 0 <= label[1] < 8
                        and 0 <= label[2] < 3 and 2 <= label[3] < 28)):
            raise ArithmeticError("A G1 minor row label is invalid")
    actual = determinant_mod([[coefficient(row, column) for column in columns] for row in rows], 65521)
    if not actual or actual != specification["minor_determinant_mod65521"]:
        raise ArithmeticError("The rebuilt G1 minor failed")
    return {"matrix_shape": [4992, 120], "rank_exact": 117, "kernel_dimension_exact": 3,
            "kernel_vectors": sparse_vectors, "minor_determinant_mod65521": actual,
            "deleted_original_middle_channel": 0, "excluded_original_middle_channel": 1}


def verify(witness=None, exported=None, response_specification=None, g1_specification=None):
    witness = json.loads(WITNESS.read_text()) if witness is None else witness
    exported = json.loads(MAPS.read_text()) if exported is None else exported
    response_specification = (json.loads(RESPONSE_MINOR.read_text())
                              if response_specification is None else response_specification)
    g1_specification = json.loads(G1_KERNEL.read_text()) if g1_specification is None else g1_specification
    if witness.get("new_exponent_established") is not False or exported.get("new_exponent_established") is not False:
        raise ArithmeticError("The subsystem does not establish a smaller exponent")
    maps, denominators = [], []
    for name, shape in zip("XYZ", ((9, 12), (42, 80), (42, 72))):
        matrix, denominator = unpack(witness[name], shape)
        maps.append(matrix)
        denominators.append(denominator)
    scale = denominators[0]*denominators[1]*denominators[2]
    construction = construction_checks(witness, maps, denominators)
    reduced = check_product(reduced_terms(), maps, scale, 14)
    reduced.pop("response_support_coordinates")
    replays = []
    if len(exported["restrictions"]) != 2:
        raise ArithmeticError("The two full-source lifts must both be present")
    for copies in (1, 2):
        a, b, full = lift(maps, copies)
        actual = {"source": [a, b], "target": [3, 3, 14*copies],
                  "maps": {name: pack(matrix, denominator)
                           for name, matrix, denominator in zip("XYZ", full, denominators)}}
        if actual != exported["restrictions"][copies-1]:
            raise ArithmeticError("A saved full-source map disagrees with its rational lift")
        replay = check_product(full_terms(a, b), full, scale, 14*copies)
        replay.pop("response_support_coordinates")
        replay.update({"source": [a, b], "target": [3, 3, 14*copies],
                       "mixed_copy_coefficients_checked": copies == 2})
        replays.append(replay)
    response = full_response(full)
    response_determinant = check_response_minor(response, response_specification)
    transfer = check_g1_kernel(full[2], g1_specification)
    return {"source": "A(8,8)", "target": "M(3,3,28)",
            "construction": construction, "map_denominators": denominators,
            "integer_coefficient_scale": scale, "reduced_replay": reduced,
            "full_source_replays": replays, "full_first_response_rank_exact": 192,
            "response_minor_determinant_mod65521": response_determinant,
            "G1_delete0_exclude1": transfer,
            "full_square_target_constructed": False, "new_exponent_established": False}


if __name__ == "__main__":
    report = verify()
    for key, path in (("witness_sha256", WITNESS), ("full_maps_sha256", MAPS),
                      ("response_minor_sha256", RESPONSE_MINOR), ("G1_kernel_sha256", G1_KERNEL)):
        report[key] = hashlib.sha256(path.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))

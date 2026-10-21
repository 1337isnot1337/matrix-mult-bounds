"""Exact coefficient replay of a spin-one fourteen-channel module and lifts.

All accepted evidence is integer arithmetic.  The optional discovery
script is not imported and no third-party dependency is needed.
"""

from collections import defaultdict
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crossed_module11 import determinant, horizontal, j_shift, k_shift, modular_rank, multiply, transpose, unpack


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
WITNESS = DIRECTORY / "spin-module14-witness.json"
FULL_MAPS = DIRECTORY / "spin-module14-full-maps.json"
REPORT = DIRECTORY / "spin-module14-certificate.json"


def construction_checks(witness, maps, denominators):
    profile = witness["profile"]
    generators = witness["generators"]
    if profile != [3, 3, 3, 2, 2] or len(generators) != 5:
        raise ArithmeticError("Incorrect chain profile")
    columns = []
    for length, generator in zip(profile, generators):
        if len(generator) != 5-length or any(len(row) != 8 for row in generator):
            raise ArithmeticError("Incorrect polynomial generator shape")
        for shift in range(length):
            column = [0]*32
            for a, row in enumerate(generator):
                for j, value in enumerate(row):
                    if type(value) is not int:
                        raise ArithmeticError("Generator coefficients must be integers")
                    column[8*(a+shift)+j] = value
            columns.append(column)
    U = transpose(columns)
    Q, _ = unpack(witness["U_left_annihilator"], (19, 32))
    if modular_rank(U) != 13 or modular_rank(Q) != 19 or any(any(row) for row in multiply(Q, U)):
        raise ArithmeticError("The intermediate subspace and annihilator disagree")

    def left(matrix, index):
        p, s = divmod(index, 2)
        shifted = j_shift(matrix, s)
        zero = [[0]*len(matrix[0]) for _ in range(40)]
        return shifted+zero if p == 0 else zero+shifted

    Wfull = horizontal(*(left(U, j) for j in range(4)))
    indices = witness["W_basis_column_indices"]
    if len(indices) != 36 or len(set(indices)) != 36 or any(not 0 <= j < 52 for j in indices):
        raise ArithmeticError("Incorrect ignored-space basis selection")
    W = [[row[j] for j in indices] for row in Wfull]
    if modular_rank(W) != 36:
        raise ArithmeticError("The ignored-space basis is not independent")
    # Each chain contributes at most length+1 columns under two shifts,
    # separately in the two p blocks.  This is the matching upper bound.
    if 2*sum(length+1 for length in profile) != 36:
        raise ArithmeticError("The structural ignored-space bound changed")

    X, Y, Z = maps
    dx, dy, dz = denominators
    expected_X = []
    for index in range(9):
        entries = [int(index == j) for j in range(9)]
        a, b, c, d, e, f, g, h, i = entries
        expected_X.append([2*(e+i), 4*d-h, b, 2*a, 2*c, -b,
                           h, 2*g, 2*i, -h, b-4*f, 2*(a+e)])
    if dx != 2 or X != expected_X:
        raise ArithmeticError("The first map is not the specified spin-one map")
    P = [[0, 1, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0], [0, -1, 0, 1]]
    Pinv2 = [[0, 2, 0, 0], [1, 0, 0, -1], [0, 0, 2, 0], [1, 0, 0, 1]]
    for index, coefficients in enumerate(X):
        physical = [[coefficients[(i*3+p+q)*2+s] for p in range(2) for s in range(2)]
                    for i in range(2) for q in range(2)]
        transformed = multiply(multiply(Pinv2, physical), P)
        entries = [int(index == j) for j in range(9)]
        a, b, c, d, e, f, g, h, i = entries
        expected = [[4*a, 4*b, 4*c, 0], [4*d, 4*e, 4*f, 0], [4*g, 4*h, 4*i, 0],
                    [4*d-2*h, -4*a+4*i, 2*b-4*f, 4*(a+e+i)]]
        if transformed != expected:
            raise ArithmeticError("The triangular spin-one identity failed")
    plus = transpose([row[36:] for row in Z[:14]])
    minus = transpose([row[:36] for row in Z[28:]])
    if any(any(row[:36]) for row in Z[:14]) or any(any(row[36:]) for row in Z[28:]):
        raise ArithmeticError("The endpoint-pair block form is incorrect")
    for channel in range(14):
        for column in range(36):
            if (2*Z[14+channel][column] != plus[column][channel]
                    or 2*Z[14+channel][36+column] != -minus[column][channel]):
                raise ArithmeticError("The central spin-one block is incorrect")
    v = k_shift(plus, 0)
    difference = [[a-b for a, b in zip(row0, row1)]
                  for row0, row1 in zip(v, k_shift(minus, 1))]
    for residual in (k_shift(plus, 1), k_shift(minus, 0), difference):
        if any(any(row) for row in multiply(Q, residual)):
            raise ArithmeticError("A required endpoint-pair relation failed")

    # Build QK0 and QK1 directly, without dense shift matrices.
    q0, q1 = [], []
    for row in Q:
        q0.append([row[8*a+H] if H < 8 else 0 for a in range(4) for H in range(9)])
        q1.append([row[8*a+H-1] if H else 0 for a in range(4) for H in range(9)])
    constraints = [row+[0]*36 for row in q1] + [[0]*36+row for row in q0]
    constraints += [row0+[-v for v in row1] for row0, row1 in zip(q0, q1)]
    if modular_rank(constraints) != 57:
        raise ArithmeticError("The pair space does not have the stated dimension15")

    L = [left(v, j) for j in range(4)]
    central = [[a-b for a, b in zip(row0, row3)] for row0, row3 in zip(L[0], L[3])]
    B = horizontal([[2*dz*value for value in row] for row in W],
                   [[2*value for value in row] for row in L[1]],
                   central, [[2*value for value in row] for row in L[2]])
    actual = multiply(Y, B)
    expected = [[2*dy*dz*int(j == 36+i) for j in range(78)] for i in range(42)]
    if actual != expected:
        raise ArithmeticError("The saved map is not the exact join dual")
    selected_rows = witness["join_row_indices"]
    if len(selected_rows) != 78 or len(set(selected_rows)) != 78 or any(not 0 <= j < 80 for j in selected_rows):
        raise ArithmeticError("Invalid join minor rows")
    exact_minor = Fraction(determinant([B[j] for j in selected_rows]), (2*dz)**78)
    if exact_minor != Fraction(witness["join_minor_determinant"]):
        raise ArithmeticError("The exact rational join determinant disagrees")
    return {"U_dimension": 13, "ignored_space_dimension": 36, "pair_space_dimension": 15,
            "selected_channels": 14, "join_rank": 78, "join_minor_determinant": str(exact_minor),
            "triangular_spin_map_checked": True, "endpoint_pair_relations_checked": True,
            "exact_join_duality_checked": True}


def conditional_square_budget():
    records = []
    for n, lower in ((27, 93509), (6, 3171), (3, 666)):
        if pow(6*n, 8999) <= pow(lower, 4000):
            raise ArithmeticError("A conditional exponent comparison failed")
        records.append({"block_size": n, "strict_lower_bound_at_p": lower})
    if sum(record["strict_lower_bound_at_p"] for record in records) <= 46**3:
        raise ArithmeticError("The conditional square-sum score does not pass")
    return {"unconstructed_square_target": [27, 6, 3], "common_leg_dimension": 774,
            "conditional_exponent": "8999/4000", "conditional_exponent_decimal": "2.24975",
            "integer_lower_bounds": records, "lower_bound_sum": 97346, "source_threshold": 97336,
            "full_target_constructed": False, "new_exponent_established": False}


def column_entries(matrix):
    answer = defaultdict(list)
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value:
                answer[j].append((i, value))
    return answer


def reduced_terms():
    for i, s, p, q, a, j in product(range(2), range(2), range(2), range(2), range(4), range(8)):
        yield ((i*3+p+q)*2+s, (p*5+a+s)*8+j, (q*4+a)*9+j+i)


def full_terms(a, b):
    m = a+b-1
    for i, p, r, j, q, s in product(range(a), range(a), range(a), range(b), range(b), range(b)):
        yield ((i*m+p+q)*b+s, (p*m+r+s)*b+j, (r*m+i+j)*b+q)


def check_product(terms, maps, denominator, middle):
    sparse = [column_entries(matrix) for matrix in maps]
    image = defaultdict(int)
    checked, active = 0, 0
    response_support = set()
    for x, y, z in terms:
        checked += 1
        yvalues, zvalues = sparse[1].get(y, ()), sparse[2].get(z, ())
        if yvalues and zvalues:
            response_support.add(x)
        xvalues = sparse[0].get(x, ())
        if not (xvalues and yvalues and zvalues):
            continue
        active += 1
        for tx, cx in xvalues:
            for ty, cy in yvalues:
                for tz, cz in zvalues:
                    image[tx, ty, tz] += cx*cy*cz
    image = {key: value for key, value in image.items() if value}
    expected = {(3*i+j, j*middle+k, i*middle+k): denominator
                for i, j, k in product(range(3), range(3), range(middle))}
    if image != expected:
        differences = [(key, image.get(key, 0), expected.get(key, 0))
                       for key in image.keys() | expected.keys()
                       if image.get(key, 0) != expected.get(key, 0)]
        raise ArithmeticError(f"Full matrix multiplication identity failed: {differences[:5]}")
    return {"source_terms_checked": checked, "active_source_terms": active,
            "target_coefficients_checked": 9*(3*middle)**2,
            "nonzero_target_coefficients": len(image),
            "response_support_coordinates": sorted(response_support)}


def lift(maps, copies):
    if copies not in (1, 2):
        raise ValueError("Only the stated one-copy and parity-matched lifts are defined")
    a, b = (4, 8) if copies == 1 else (8, 8)
    m, middle = a+b-1, copies*14
    answer = [[[0]*(a*b*m) for _ in range(rows)] for rows in (9, 3*middle, 3*middle)]
    for row, column, value in ((r, c, v) for c, entries in column_entries(maps[0]).items() for r, v in entries):
        ik, s = divmod(column, 2)
        i, k = divmod(ik, 3)
        answer[0][row][(i*m+k)*b+copies*s] = value
    for e in range(copies):
        for column, entries in column_entries(maps[1]).items():
            pL, j = divmod(column, 8)
            p, L = divmod(pL, 5)
            physical = (p*m+e+copies*L)*b+j
            for row, value in entries:
                vertex, channel = divmod(row, 14)
                answer[1][vertex*middle+e*14+channel][physical] = value
        for column, entries in column_entries(maps[2]).items():
            qa, H = divmod(column, 9)
            q, ar = divmod(qa, 4)
            physical = ((e+copies*ar)*m+H)*b+q
            for row, value in entries:
                vertex, channel = divmod(row, 14)
                answer[2][vertex*middle+e*14+channel][physical] = value
    return a, b, answer


def pack(matrix, denominator):
    return {"shape": [len(matrix), len(matrix[0])], "denominator": denominator,
            "entries": [[i, j, value] for i, row in enumerate(matrix) for j, value in enumerate(row) if value]}


def verify(witness=None, exported=None):
    witness = json.loads(WITNESS.read_text()) if witness is None else witness
    if witness.get("new_exponent_established") is not False:
        raise ArithmeticError("This subsystem does not establish a smaller exponent")
    maps, denominators = [], []
    for name, shape in zip("XYZ", ((9, 12), (42, 80), (42, 72))):
        matrix, denominator = unpack(witness[name], shape)
        maps.append(matrix)
        denominators.append(denominator)
    scale = denominators[0]*denominators[1]*denominators[2]
    construction = construction_checks(witness, maps, denominators)
    reduced = check_product(reduced_terms(), maps, scale, 14)
    reduced.pop("response_support_coordinates")
    report = {"source": "cyclic C(2,2) tensor C(2,4) tensor C(2,8)",
              "source_dimensions": [12, 80, 72], "target": "M(3,3,14)",
              "map_denominators": denominators, "integer_coefficient_scale": scale,
              "construction_checks": construction,
              "reduced_replay": reduced, "full_source_lifts": [],
              "conditional_square_budget": conditional_square_budget(),
              "new_exponent_established": False}
    export = {"field": "Q", "target_coordinate_orders": ["3*i+j", "j*middle+k", "i*middle+k"],
              "last_leg_convention": "The row i*middle+k denotes the variable Z_(k,i)",
              "restrictions": [], "new_exponent_established": False}
    for copies in (1, 2):
        a, b, full = lift(maps, copies)
        entry = {"source": [a, b], "target": [3, 3, 14*copies],
                 "maps": {name: pack(matrix, denominator)
                          for name, matrix, denominator in zip("XYZ", full, denominators)}}
        export["restrictions"].append(entry)
        if exported is not None:
            old = exported["restrictions"][copies-1]
            if old != entry:
                raise ArithmeticError("Exported full-source maps disagree with the actual lift")
            full = [unpack(old["maps"][name], (rows, a*b*(a+b-1)))[0]
                    for name, rows in zip("XYZ", (9, 42*copies, 42*copies))]
        replay = check_product(full_terms(a, b), full, scale, 14*copies)
        support = replay.pop("response_support_coordinates")
        m = a+b-1
        if any((index//b) % m > 2 for index in support):
            raise ArithmeticError("An ambient response lies outside the proved three long coordinates")
        replay.update({"source": f"A({a},{b})", "target": f"M(3,3,{14*copies})",
                       "source_common_dimension": a*b*m,
                       "actual_response_support_upper_bound": len(support),
                       "unconditional_response_upper_bound": 3*a*b,
                       "response_kernel_dimension_lower_bound": a*b*m-len(support),
                       "mixed_copy_coefficients_checked": copies == 2})
        report["full_source_lifts"].append(replay)
    return report, export


if __name__ == "__main__":
    report, exported = verify()
    FULL_MAPS.write_text(json.dumps(exported, indent=2)+"\n")
    replayed, _ = verify(exported=json.loads(FULL_MAPS.read_text()))
    if replayed != report:
        raise ArithmeticError("The exported-map replay is inconsistent")
    report["witness_sha256"] = hashlib.sha256(WITNESS.read_bytes()).hexdigest()
    report["full_maps_sha256"] = hashlib.sha256(FULL_MAPS.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))

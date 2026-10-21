"""Exact rational C(2,4) tensor C(2,8) -> M(2,2,11) certificate.

Acceptance and full coefficient replay use only the standard library.
The saved maps are ordinary constant maps, not numerical approximations.
"""

from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WITNESS = ROOT / "results/anisotropic-constructions-2026-10-20/crossed-module11-witness.json"
REPORT = ROOT / "results/anisotropic-constructions-2026-10-20/crossed-module11-certificate.json"


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(first, second):
    columns = transpose(second)
    return [[sum(a*b for a, b in zip(row, column)) for column in columns] for row in first]


def horizontal(*matrices):
    return [sum((list(matrix[row]) for matrix in matrices), []) for row in range(len(matrices[0]))]


def modular_rank(matrix, prime=65521):
    rows = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        selected = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if selected is None:
            continue
        rows[rank], rows[selected] = rows[selected], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [value*inverse % prime for value in rows[rank]]
        for i in range(rank+1, len(rows)):
            value = rows[i][column]
            if value:
                rows[i] = [(a-value*b) % prime for a, b in zip(rows[i], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def determinant(matrix):
    """Bareiss elimination over the integers, with checked exact divisions."""
    rows = [list(row) for row in matrix]
    if any(len(row) != len(rows) for row in rows):
        raise ValueError("Determinant requires a square matrix")
    previous, sign = 1, 1
    for pivot in range(len(rows)-1):
        selected = next((i for i in range(pivot, len(rows)) if rows[i][pivot]), None)
        if selected is None:
            return 0
        if selected != pivot:
            rows[pivot], rows[selected] = rows[selected], rows[pivot]
            sign = -sign
        value = rows[pivot][pivot]
        for i in range(pivot+1, len(rows)):
            for j in range(pivot+1, len(rows)):
                numerator = rows[i][j]*value-rows[i][pivot]*rows[pivot][j]
                if numerator % previous:
                    raise ArithmeticError("Nonexact Bareiss division")
                rows[i][j] = numerator//previous
            rows[i][pivot] = 0
        previous = value
    return sign*rows[-1][-1]


def unpack(specification, shape):
    if specification["shape"] != list(shape):
        raise ArithmeticError("Wrong rational map shape")
    denominator = specification["denominator"]
    if type(denominator) is not int or denominator <= 0:
        raise ArithmeticError("Invalid rational map denominator")
    answer = [[0]*shape[1] for _ in range(shape[0])]
    seen = set()
    for row, column, value in specification["entries"]:
        if not (type(row) is int and type(column) is int and type(value) is int
                and 0 <= row < shape[0] and 0 <= column < shape[1] and value):
            raise ArithmeticError("Invalid rational map entry")
        if (row, column) in seen:
            raise ArithmeticError("Duplicate rational map entry")
        seen.add((row, column))
        answer[row][column] = value
    return answer, denominator


def u_matrix(generators):
    if len(generators) != 6 or any(len(g) != 3 or any(len(row) != 8 for row in g) for g in generators):
        raise ArithmeticError("Six degree-two vector-polynomial generators are required")
    columns = []
    for generator in generators:
        if any(type(value) is not int for row in generator for value in row):
            raise ArithmeticError("Generator coefficients must be integers")
        for shift in range(2):
            rows = [[0]*8 for _ in range(4)]
            for i in range(3):
                rows[i+shift] = list(generator[i])
            columns.append([value for row in rows for value in row])
    return transpose(columns)


def j_shift(matrix, shift):
    if len(matrix) != 32 or shift not in (0, 1):
        raise ArithmeticError("Invalid J input")
    answer = [[0]*len(matrix[0]) for _ in range(40)]
    for a in range(4):
        for j in range(8):
            answer[8*(a+shift)+j] = list(matrix[8*a+j])
    return answer


def k_shift(matrix, shift):
    if len(matrix) != 36 or shift not in (0, 1):
        raise ArithmeticError("Invalid K input")
    return [list(matrix[9*a+j+shift]) for a in range(4) for j in range(8)]


def source_terms():
    return [(2*i+u, 8*(a+u)+j, 9*a+j+i)
            for i, u, a, j in product(range(2), range(2), range(4), range(8))]


def replay_source(y_map, z_map, denominator):
    y_columns, z_columns = defaultdict(list), defaultdict(list)
    for row, values in enumerate(y_map):
        for column, value in enumerate(values):
            if value:
                y_columns[column].append((row, value))
    for row, values in enumerate(z_map):
        for column, value in enumerate(values):
            if value:
                z_columns[column].append((row, value))
    image = Counter()
    contributions = 0
    for x, y, z in source_terms():
        for (a, left), (b, right) in product(y_columns[y], z_columns[z]):
            image[x, a, b] += left*right
            contributions += 1
    image = {point: value for point, value in image.items() if value}
    target = {(2*i+u, 11*u+j, 11*i+j): denominator
              for i, u, j in product(range(2), range(2), range(11))}
    if image != target:
        raise ArithmeticError("Full crossed-module source coefficient identity failed")
    return {"original_source_terms": len(source_terms()), "integer_contributions": contributions,
            "target_coefficients_checked": 4*22*22, "nonzero_target_coefficients": len(image),
            "all_other_coefficients_zero": True}


def verify_witness(witness):
    if witness.get("new_exponent_established") is not False:
        raise ArithmeticError("The module certificate establishes no exponent improvement")
    y_map, y_denominator = unpack(witness["Y"], (22, 40))
    z_map, z_denominator = unpack(witness["Z"], (22, 36))
    q_map, q_denominator = unpack(witness["U_left_annihilator"], (20, 32))
    U = u_matrix(witness["generators"])
    if modular_rank(U) != 12 or modular_rank(q_map) != 20:
        raise ArithmeticError("U and its annihilator do not have complementary ranks")
    if any(value for row in multiply(q_map, U) for value in row):
        raise ArithmeticError("Saved annihilator does not annihilate U")
    W = horizontal(j_shift(U, 0), j_shift(U, 1))
    if modular_rank(W) != 18:
        raise ArithmeticError("Wrong dimension of J0U+J1U")
    # Six length-two chains span W with at most18 vectors. The modular
    # lower bound therefore certifies the exact rational rank18.
    identity = [[int(i == j) for j in range(36)] for i in range(36)]
    q0 = multiply(q_map, k_shift(identity, 0))
    q1 = multiply(q_map, k_shift(identity, 1))
    zero = [[0]*36 for _ in range(20)]
    constraints = horizontal(q1, zero)+horizontal(zero, q0)+horizontal(q0, [[-v for v in row] for row in q1])
    if modular_rank(constraints) != 60:
        raise ArithmeticError("The complete pair constraint matrix is not full row rank")
    # The constraint matrix has60 rows and72 columns, so its exact
    # rational kernel dimension is12.
    z0, z1 = transpose(z_map[:11]), transpose(z_map[11:])
    for vectors in [k_shift(z0, 1), k_shift(z1, 0),
                    [[a-b for a, b in zip(left, right)]
                     for left, right in zip(k_shift(z0, 0), k_shift(z1, 1))]]:
        if any(value for row in multiply(q_map, vectors) for value in row):
            raise ArithmeticError("A saved pair violates a complete U-membership condition")
    pivots = witness["W_basis_column_indices"]
    if len(pivots) != 18 or len(set(pivots)) != 18 or any(type(i) is not int or not 0 <= i < 24 for i in pivots):
        raise ArithmeticError("Invalid W basis-column indices")
    w_basis = [[z_denominator*row[i] for i in pivots] for row in W]
    V = k_shift(z0, 0)
    B = horizontal(w_basis, j_shift(V, 0), j_shift(V, 1))
    exact_determinant = Fraction(determinant(B), z_denominator**40)
    if not exact_determinant or exact_determinant != Fraction(witness["join_determinant"]):
        raise ArithmeticError("The complete rational join determinant does not match")
    target_rows = [[y_denominator*z_denominator*int(column == row+18) for column in range(40)]
                   for row in range(22)]
    if multiply(y_map, B) != target_rows:
        raise ArithmeticError("Y is not the required dual of the complete join basis")
    coefficient_check = replay_source(y_map, z_map, y_denominator*z_denominator)
    return {"source": "C(2,4) tensor C(2,8)", "source_format": [4, 40, 36],
            "target": "M(2,2,11)", "target_format": [4, 22, 22],
            "ordinary_rational_restriction": True, "first_leg_map": "identity",
            "generator_nonzero_coefficients": sum(bool(value) for generator in witness["generators"]
                                                  for row in generator for value in row),
            "U_dimension": 12, "JU_dimension": 18, "pair_space_dimension": 12,
            "selected_pairs": 11, "join_determinant": str(exact_determinant),
            "Y_denominator": y_denominator, "Z_denominator": z_denominator,
            "Y_nonzero_entries": len(witness["Y"]["entries"]),
            "Z_nonzero_entries": len(witness["Z"]["entries"]),
            "coefficient_replay": coefficient_check,
            "annihilator_denominator": q_denominator,
            "modular_rank_prime": 65521, "new_exponent_established": False}


def main():
    witness = json.loads(WITNESS.read_text())
    report = verify_witness(witness)
    report["witness_sha256"] = hashlib.sha256(WITNESS.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

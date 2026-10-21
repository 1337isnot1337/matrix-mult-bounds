"""Discovery control: project the two-bit spin1 lift into A(4,4).

This explicitly changes the lift instead of imposing carry admissibility.
It records the entire correction tensor. No matrix multiplication witness
or exponent improvement is asserted for the projected source alone.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT / "results/anisotropic-constructions-2026-10-20/parity_balancing_spin1/scalar_witness.json"
OUTPUT = ROOT / "results/anisotropic-constructions-2026-10-20/bitwise-hankel-projection.json"


def raw_row(local, first, middle, last):
    factors = []
    for bit in range(2):
        col = ((first >> bit & 1)*3+middle[bit])*2+(last >> bit & 1)
        factors.append([(row, local[row][col]) for row in range(9) if local[row][col]])
    result = {}
    for (left, a), (right, b) in product(*factors):
        i = left//3+3*(right//3)
        j = left % 3+3*(right % 3)
        result[9*i+j] = a*b
    return result


def basis_columns():
    local = json.loads(INPUT.read_text())["base_common_map_numerator"]
    fibers = [[mid for mid in product(range(3), repeat=2) if mid[0]+2*mid[1] == total]
              for total in range(7)]
    columns = []
    for first, total, last in product(range(4), range(7), range(4)):
        if len(fibers[total]) == 1:
            raw = raw_row(local, first, fibers[total][0], last)
            columns.append([(row, 0, value) for row, value in raw.items()])
            continue
        if total == 2:
            base, alternate, parameter = (0, 1), (2, 0), 1
        elif total == 4:
            base, alternate, parameter = (2, 1), (0, 2), 2
        else:
            raise ArithmeticError("Unexpected two-bit carry fiber")
        original = raw_row(local, first, base, last)
        other = raw_row(local, first, alternate, last)
        difference = dict(other)
        for row, value in original.items():
            difference[row] = difference.get(row, 0)-value
        columns.append([(row, 0, value) for row, value in original.items()]
                       + [(row, parameter, value) for row, value in difference.items() if value])
    return columns


def source_points():
    return [((7*i+p+q)*4+s, (7*p+r+s)*4+j, (7*r+i+j)*4+q)
            for i, p, r, j, q, s in product(range(4), repeat=6)]


def coefficient_polynomials():
    columns = basis_columns()
    coefficients = defaultdict(Counter)
    for x, y, z in source_points():
        for (i, pi, a), (j, pj, b), (k, pk, c) in product(columns[x], columns[y], columns[z]):
            coefficients[i, j, k][pi, pj, pk] += a*b*c
    return {point: {monomial: value for monomial, value in poly.items() if value}
            for point, poly in coefficients.items() if any(poly.values())}


def matrix_tensor(n=9, scale=1):
    return {(n*i+j, n*j+k, n*k+i): scale for i, j, k in product(range(n), repeat=3)}


def evaluate(polynomials, parameters=(Fraction(1, 3),)*6):
    weights = [(1, parameters[2*i], parameters[2*i+1]) for i in range(3)]
    answer = {}
    for point, poly in polynomials.items():
        value = sum(coefficient*weights[0][m[0]]*weights[1][m[1]]*weights[2][m[2]]
                    for m, coefficient in poly.items())
        if value:
            answer[point] = value/64
    return answer


def difference(left, right):
    result = dict(left)
    for point, value in right.items():
        result[point] = result.get(point, 0)-value
    return {point: value for point, value in result.items() if value}


def sparse_rank(rows):
    pivots = {}
    for values in sorted(rows, key=len):
        row = {col: Fraction(value) for col, value in values.items() if value}
        while row:
            col = min(row)
            value = row[col]
            if col not in pivots:
                pivots[col] = {j: entry/value for j, entry in row.items()}
                break
            for j, entry in pivots[col].items():
                row[j] = row.get(j, 0)-value*entry
                if not row[j]:
                    del row[j]
    return len(pivots)


def map_rank(parameters=(Fraction(1, 3), Fraction(1, 3))):
    rows = [defaultdict(Fraction) for _ in range(81)]
    for column, entries in enumerate(basis_columns()):
        for row, parameter, value in entries:
            rows[row][column] += value*(1 if not parameter else parameters[parameter-1])
    return sparse_rank(rows)


def identity_slice_rank(tensor):
    rows = [defaultdict(Fraction) for _ in range(81)]
    for (x, y, z), value in tensor.items():
        if y//9 == y % 9:
            rows[x][z] += value
    return sparse_rank(rows)


def selected_coefficient(point):
    """Recompute one coefficient directly from all original source terms."""
    columns = basis_columns()
    selected = [[[(parameter, value) for row, parameter, value in column
                  if row == point[leg]] for column in columns] for leg in range(3)]
    answer = Counter()
    for x, y, z in source_points():
        for (pi, a), (pj, b), (pk, c) in product(selected[0][x], selected[1][y], selected[2][z]):
            answer[pi, pj, pk] += a*b*c
    return {monomial: value for monomial, value in answer.items() if value}


def spin1_square_coefficient(point):
    """Coefficient of (M3 + trace tensor trace tensor trace)^2."""
    factors = []
    for digit in range(2):
        unit = [((row//9)//(3**digit) % 3, (row % 9)//(3**digit) % 3)
                for row in point]
        mm = int(unit[0][1] == unit[1][0] and unit[1][1] == unit[2][0]
                 and unit[2][1] == unit[0][0])
        scalar = int(all(i == j for i, j in unit))
        factors.append(mm+scalar)
    return factors[0]*factors[1]


def carry_control():
    witnesses = []
    for point, expected in [((9, 0, 61), {(0, 0, 0): 64, (1, 0, 0): -64}),
                            ((12, 50, 39), {(0, 0, 0): 128, (1, 0, 0): -128})]:
        actual = selected_coefficient(point)
        if actual != expected:
            raise ArithmeticError("Carry coefficient changed")
        desired = spin1_square_coefficient(point)
        forced = Fraction(64*desired-actual[(0, 0, 0)], actual[(1, 0, 0)])
        witnesses.append({"target_rows": list(point),
                          "projected_constant_numerator": actual[(0, 0, 0)],
                          "projected_alpha_x_numerator": actual[(1, 0, 0)],
                          "denominator": 64, "uncompressed_spin1_square_coefficient": desired,
                          "forced_alpha_x": str(forced)})
    if witnesses[0]["forced_alpha_x"] == witnesses[1]["forced_alpha_x"]:
        raise ArithmeticError("Expected incompatible carry equations")
    return {"field": "characteristic zero (also valid whenever 2 is invertible)",
            "comparison": "S tensor S, where S=M3+trace tensor trace tensor trace",
            "all_six_parameter_identity_excluded": True,
            "witnesses": witnesses,
            "general_source_compression_excluded": False}


def discovery():
    polynomials = coefficient_polynomials()
    target = matrix_tensor(scale=64)
    immutable = []
    for point in sorted(set(polynomials) | set(target)):
        poly = dict(polynomials.get(point, {}))
        poly[0, 0, 0] = poly.get((0, 0, 0), 0)-target.get(point, 0)
        poly = {m: value for m, value in poly.items() if value}
        if set(poly) == {(0, 0, 0)}:
            immutable.append({"target_rows": list(point), "constant_defect_numerator": poly[0, 0, 0],
                              "denominator": 64})
    image = evaluate(polynomials)
    residual = difference(image, matrix_tensor())
    samples = []
    for alpha, beta in [(Fraction(1, 3), Fraction(1, 3)), (Fraction(0), Fraction(0)),
                        (Fraction(1), Fraction(1)), (Fraction(1, 2), Fraction(1, 2)),
                        (Fraction(-1), Fraction(-1)), (Fraction(0), Fraction(1)),
                        (Fraction(1), Fraction(0))]:
        sampled = difference(evaluate(polynomials, (alpha, beta)*3), matrix_tensor())
        samples.append({"alpha": str(alpha), "beta": str(beta), "map_rank": map_rank((alpha, beta)),
                        "residual_coefficients": len(sampled),
                        "residual_identity_slice_rank": identity_slice_rank(sampled)})
    report = {"source": "full A(4,4)", "intended_comparison_tensor": "M9",
              "source_dimension": 112, "target_parameter_dimension": 81,
              "projection_parameters": "alpha_leg and beta_leg independently on each of three legs",
              "parameter_choice": "alpha=beta=1/3 on every leg (physical Hankel-fiber average)",
              "source_terms": len(source_points()),
              "coefficient_polynomials": len(polynomials),
              "map_rank_at_average": map_rank(), "source_image_coefficients_at_average": len(image),
              "complete_residual_coefficients_at_average": len(residual),
              "residual_identity_slice_rank_at_average": identity_slice_rank(residual),
              "immutable_defect_count": len(immutable), "first_immutable_defects": immutable[:12],
              "rational_projection_samples": samples,
              "ordinary_source_to_M9_identity": not residual,
              "all_six_parameter_source_to_M9_identity_excluded_by_immutable_coefficient": bool(immutable),
              "uncompressed_spin1_square_carry_control": carry_control(),
              "general_source_compression_excluded": False, "new_exponent_established": False}
    OUTPUT.write_text(json.dumps(report, indent=2)+"\n")
    return report


if __name__ == "__main__":
    print(json.dumps(discovery(), indent=2))

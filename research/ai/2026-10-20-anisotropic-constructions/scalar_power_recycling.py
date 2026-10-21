"""Exact telescoping reuse of the A22 scalar defect, with its full cost."""

import argparse
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json
from math import comb, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT / "results/anisotropic-constructions-2026-10-20/parity_balancing_spin1/scalar_witness.json"
OUTPUT = ROOT / "results/anisotropic-constructions-2026-10-20/scalar-power-recycling.json"


def a22_points():
    return [((3*i+p+q)*2+s, (2*j+p)*3+r+s, ((i+j)*2+q)*2+r)
            for i, j, p, q, r, s in product(range(2), repeat=6)]


def matrix_points(n):
    return [(n*i+j, n*j+k, n*k+i)
            for i, j, k in product(range(n), repeat=3)]


def grouped_row(first, second, n=3):
    i, j = divmod(first, n)
    p, q = divmod(second, n)
    return n*n*(n*i+p)+n*j+q


def construct_square():
    """Maps from A22^2 direct_sum A22 direct_sum M3 to M9."""
    seed = json.loads(INPUT.read_text())
    if seed["common_map_denominator"] != 2:
        raise ValueError("The recorded spin1 map denominator changed")
    maps = []
    for leg, name in enumerate("ABC"):
        local = [row[:12] for row in seed["map_numerators"][name]]
        rows = [[] for _ in range(81)]
        for x0, x1 in product(range(9), repeat=2):
            row = rows[grouped_row(x0, x1)]
            for s0, s1 in product(range(12), repeat=2):
                value = local[x0][s0]*local[x1][s1]
                if value:
                    row.append([12*s0+s1, value])
            sign = -1 if leg == 2 else 1
            if x1 in (0, 4, 8):
                for s in range(12):
                    if local[x0][s]:
                        row.append([144+s, sign*2*local[x0][s]])
            if x0 in (0, 4, 8):
                row.append([156+x1, sign*4])
        maps.append(rows)
    return {"source": "A(2,2)^2 direct sum A(2,2) direct sum M3",
            "source_dimensions": [165]*3, "target": "M9",
            "target_dimensions": [81]*3, "field": "Q",
            "common_map_denominator": 4, "sparse_map_numerators": maps,
            "source_blocks": [[0, 144], [144, 156], [156, 165]],
            "target_row_order": "9*I+J, 9*J+K, 9*K+I",
            "new_exponent_established": False}


def square_points():
    base = a22_points()
    return ([tuple(12*u[i]+v[i] for i in range(3))
             for u, v in product(base, repeat=2)]
            + [tuple(144+x for x in p) for p in base]
            + [tuple(156+x for x in p) for p in matrix_points(3)])


def transform(maps, points, source_dimension=165):
    columns = []
    for rows in maps:
        cols = [[] for _ in range(source_dimension)]
        for row, entries in enumerate(rows):
            for col, value in entries:
                if type(col) is not int or not 0 <= col < source_dimension:
                    raise ValueError("Invalid source column")
                if type(value) is not int or value == 0:
                    raise ValueError("Invalid nonzero integer numerator")
                cols[col].append((row, value))
        columns.append(cols)
    answer = defaultdict(int)
    for x, y, z in points:
        for (i, a), (j, b), (k, c) in product(columns[0][x], columns[1][y], columns[2][z]):
            answer[i, j, k] += a*b*c
    return {key: value for key, value in answer.items() if value}


def scalar_perturbed_matrix(n=3):
    answer = defaultdict(int)
    for p in matrix_points(n):
        answer[p] += 1
    for p in product(range(0, n*n, n+1), repeat=3):
        answer[p] += 1
    return dict(answer)


def verify_square(certificate):
    if certificate["source"] != "A(2,2)^2 direct sum A(2,2) direct sum M3":
        raise ValueError("The complete auxiliary sources must be declared")
    if certificate["source_dimensions"] != [165]*3 or certificate["target_dimensions"] != [81]*3:
        raise ValueError("Incorrect source or target dimensions")
    if certificate["common_map_denominator"] != 4 or certificate["new_exponent_established"] is not False:
        raise ValueError("Incorrect denominator or scope")
    maps = certificate["sparse_map_numerators"]
    if len(maps) != 3 or any(len(rows) != 81 for rows in maps):
        raise ValueError("All three complete 81-row maps are required")
    points = square_points()
    if len(points) != 4187 or len(set(points)) != 4187:
        raise ArithmeticError("Source support reconstruction failed")
    target = {p: 64 for p in matrix_points(9)}
    if transform(maps, points) != target:
        raise ArithmeticError("The complete M9 tensor identity failed")
    s = scalar_perturbed_matrix()
    expected_base = defaultdict(int)
    for (p, a), (q, b) in product(s.items(), repeat=2):
        expected_base[tuple(grouped_row(p[i], q[i]) for i in range(3))] += 64*a*b
    actual_base = transform(maps, points[:4096])
    if actual_base != dict(expected_base):
        raise ArithmeticError("The uncorrected square must retain its full trace defect")
    residual = dict(actual_base)
    for p, value in target.items():
        residual[p] = residual.get(p, 0)-value
    residual = {p: value for p, value in residual.items() if value}
    correction = transform(maps, points[4096:])
    if correction != {p: -value for p, value in residual.items()}:
        raise ArithmeticError("The supplied correction did not equal the complete residual")
    return {"source_terms_checked": len(points), "target_coefficients_checked": 81**3,
            "nonzero_target_coefficients": len(target),
            "uncorrected_square_nonzero_coefficients": len(actual_base),
            "correction_nonzero_coefficients": len(correction),
            "map_nonzeros_per_leg": [sum(map(len, rows)) for rows in maps],
            "complete_auxiliary_sources_used": True, "exact_identity": True}


def kronecker(a, b):
    return [[x*y for x in row_a for y in row_b]
            for row_a in a for row_b in b]


def exact_rank(matrix):
    rows = [[Fraction(x) for x in row] for row in matrix]
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        divisor = rows[rank][col]
        rows[rank] = [x/divisor for x in rows[rank]]
        for i in range(rank+1, len(rows)):
            factor = rows[i][col]
            if factor:
                rows[i] = [x-factor*y for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def residual_identity_slice(n, k):
    """Coefficient matrix R_k(A, I^(tensor k), C), in tensor-factor order."""
    size = n*n
    m = [[int(i == ell and j == p) for p, ell in product(range(n), repeat=2)]
         for i, j in product(range(n), repeat=2)]
    s = [[m[row][col]+n*int(row//n == row % n and col//n == col % n)
          for col in range(size)] for row in range(size)]
    mm = [[1]]
    ss = [[1]]
    for _ in range(k):
        mm, ss = kronecker(mm, m), kronecker(ss, s)
    return [[x-y for x, y in zip(row_s, row_m)] for row_s, row_m in zip(ss, mm)]


def cost_report():
    records = []
    for k in range(1, 9):
        rank = 9**k-8**k
        lower = isqrt(rank)
        lower += lower*lower < rank
        auxiliary = sum(12**j*9**(k-1-j) for j in range(k))
        records.append({"power": k, "target_matrix_size": 3**k,
                        "residual_flattening_rank": rank,
                        "independent_scalar_correction_lower_bound": rank,
                        "independent_matrix_correction_size_lower_bound": lower,
                        "telescoping_auxiliary_leg_dimension": auxiliary,
                        "total_telescoping_source_leg_dimension": 12**k+auxiliary,
                        "naive_scalar_extended_power_leg_dimension": 13**k,
                        "residual_identity_slice_eigenvalues": [
                            {"scalar_positions": j, "eigenvalue_relative_to_trace_pairing": 10**j-1,
                             "multiplicity": comb(k, j)*8**(k-j)} for j in range(k+1)]})
    return {"powers": records,
            "finite_gate_for_A22_powers": {
                "exact_comparison": "6^18*12^9 < 1000^8",
                "left_integer": 6**18*12**9, "right_integer": 1000**8,
                "strict_inequality": 6**18*12**9 < 1000**8,
                "scope": "The existing sixfold finite gate and square direct sums from pure A22 tensor powers",
                "general_tensor_power_constructions_excluded": False},
            "telescoping_gate_comparison": {"exact_comparison": "18^9 < 1000^4",
                                             "left_integer": 18**9, "right_integer": 1000**4,
                                             "strict_inequality": 18**9 < 1000**4},
            "new_exponent_established": False}


def controls():
    rank_controls = []
    for n, k in [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]:
        observed = exact_rank(residual_identity_slice(n, k))
        expected = n**(2*k)-(n*n-1)**k
        if observed != expected:
            raise ArithmeticError("The exact residual slice rank failed")
        rank_controls.append({"matrix_size": n, "power": k, "exact_slice_rank": observed})
    return rank_controls


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    witness = construct_square()
    report = {"square_witness": witness, "square_verification": verify_square(witness),
              "residual_rank_controls": controls(), "costs": cost_report(),
              "review_status": "Author checked in this generating session; no external independent review or formalization"}
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"output": str(args.output), "verification": report["square_verification"],
                      "rank_controls": report["residual_rank_controls"], "new_exponent_established": False}, indent=2))


if __name__ == "__main__":
    main()

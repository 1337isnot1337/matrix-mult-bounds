"""Integer restrictions Q_(k+1,k) -> M(k,4,k), k >= 2.

The k=4 case is Q_(5,4) -> M(4,4,4).  This is a direct coefficient
certificate, not a numerical residual or an exponent improvement.
"""

from collections import Counter
from itertools import product
from pathlib import Path
import argparse
import json


def subspaces(k):
    """Rows are coefficient vectors in increasing monomial order."""
    if not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer at least two")
    outer = [[0]*(k+1) for _ in range(k)]
    for i in range(k-1):
        outer[i][i+1] = 1
    outer[-1][0], outer[-1][k] = 1, -1
    inner = [[0]*k for _ in range(2)]
    inner[0][0], inner[1][k-1] = 1, 1
    return outer, inner


def product_matrix_and_dual(k):
    """D contains products U_i W_v; L D^T = D^T L = identity."""
    outer, inner = subspaces(k)
    d = [[0]*(2*k) for _ in range(2*k)]
    for i, v, p, q in product(range(k), range(2), range(k+1), range(k)):
        d[2*i+v][p+q] += outer[i][p]*inner[v][q]
    dual = [[0]*(2*k) for _ in range(2*k)]
    for i in range(k-1):
        dual[2*i][i+1] = 1
        dual[2*i+1][i+k] = 1
    dual[2*k-4][2*k-1] = 1
    dual[1][0] = 1
    dual[2*k-2][0] = 1
    dual[2*k-1][2*k-1] = -1
    for i, j in product(range(2*k), repeat=2):
        if sum(dual[i][s]*d[j][s] for s in range(2*k)) != int(i == j):
            raise ArithmeticError("The asserted integer inverse is wrong")
        if sum(d[s][i]*dual[s][j] for s in range(2*k)) != int(i == j):
            raise ArithmeticError("The reverse integer inverse is wrong")
    return d, dual


def maps(k):
    """Dense target-by-source integer maps in the documented flattenings."""
    outer, inner = subspaces(k)
    _, dual = product_matrix_and_dual(k)
    n, b, width = k+1, k, 2*k
    first = [[0]*(n*n) for _ in range(k*k)]
    second = [[0]*(b*width) for _ in range(4*k)]
    third = [[0]*(width*b) for _ in range(4*k)]
    for i, h, p, q in product(range(k), range(k), range(n), range(n)):
        first[k*i+h][n*p+q] = outer[h][p]*outer[i][q]
    for i, y, v, yy, j in product(range(k), range(2), range(2), range(b), range(width)):
        second[4*i+2*y+v][width*yy+j] = inner[y][yy]*dual[2*i+v][j]
    for y, v, h, z, vv in product(range(2), range(2), range(k), range(width), range(b)):
        third[k*(2*y+v)+h][b*z+vv] = dual[2*h+y][z]*inner[v][vv]
    return first, second, third


def sparse_columns(matrix):
    return [[(row, matrix[row][column]) for row in range(len(matrix))
             if matrix[row][column]] for column in range(len(matrix[0]))]


def coefficient_table(k):
    first, second, third = map(sparse_columns, maps(k))
    n, width = k+1, 2*k
    coefficients, counts = Counter(), Counter()
    zero_source_terms = 0
    for p, q, y, v in product(range(n), range(n), range(k), range(k)):
        terms = (first[n*p+q], second[width*y+q+v], third[k*(p+y)+v])
        if any(not values for values in terms):
            zero_source_terms += 1
        for (ia, ca), (ib, cb), (ic, cc) in product(*terms):
            coefficients[ia, ib, ic] += ca*cb*cc
            counts[ia, ib, ic] += 1
    return coefficients, counts, zero_source_terms


def multiply(left, right):
    """Apply the supplied maps to a k-by-4 and a 4-by-k matrix."""
    k = len(left)
    if (k < 2 or len(right) != 4 or any(len(row) != 4 for row in left)
            or any(len(row) != k for row in right)):
        raise ValueError("Expected a k-by-4 matrix and a 4-by-k matrix")
    first, second, third = maps(k)
    left_vector = [entry for row in left for entry in row]
    right_vector = [entry for row in right for entry in row]
    b = [sum(second[r][s]*left_vector[r] for r in range(4*k))
         for s in range(2*k*k)]
    c = [sum(third[r][s]*right_vector[r] for r in range(4*k))
         for s in range(2*k*k)]
    n, width = k+1, 2*k
    source_output = [sum(b[width*y+q+v]*c[k*(p+y)+v]
                         for y, v in product(range(k), repeat=2))
                     for p, q in product(range(n), repeat=2)]
    output = [sum(first[r][s]*source_output[s] for s in range(n*n))
              for r in range(k*k)]
    return [output[k*i:k*(i+1)] for i in range(k)]


def certificate(k=4, include_maps=True):
    coefficients, counts, zero_source_terms = coefficient_table(k)
    expected = {(k*i+h, 4*i+j, k*j+h): 1
                for i, j, h in product(range(k), range(4), range(k))}
    failures = []
    checked = 0
    for key in product(range(k*k), range(4*k), range(4*k)):
        checked += 1
        if coefficients[key] != expected.get(key, 0):
            failures.append([list(key), coefficients[key], expected.get(key, 0)])
    if failures:
        raise ArithmeticError(f"Full integer coefficient check failed: {failures[:3]}")
    d, dual = product_matrix_and_dual(k)
    map_values = maps(k)
    result = {
        "k": k, "source": f"Q_({k+1},{k})", "target": f"M({k},4,{k})",
        "source_dimensions": [(k+1)**2, 2*k*k, 2*k*k],
        "target_dimensions": [k*k, 4*k, 4*k],
        "source_terms_checked": (k+1)**2*k*k,
        "source_terms_mapping_to_zero": zero_source_terms,
        "expanded_source_contributions": sum(counts.values()),
        "all_target_coefficient_positions_checked": checked,
        "target_nonzero_coefficients": len(expected),
        "off_support_coefficients_checked": checked-len(expected),
        "off_support_cancellation_positions": sum(value == 0 for value in coefficients.values()),
        "coefficient_failures": 0,
        "map_nonzero_counts": [sum(value != 0 for row in matrix for value in row)
                                for matrix in map_values],
        "coefficient_ring": "Z", "valid_over_every_field": True,
        "source_A_flattening": "p*(k+1)+q",
        "source_B_flattening": "y*(2*k)+s",
        "source_C_flattening": "z*k+v",
        "target_A_flattening": "i*k+h",
        "target_B_flattening": "i*4+j",
        "target_C_flattening": "j*k+h",
        "product_matrix_D_rows": d,
        "product_dual_L_rows": dual,
        "inverse_identity": "L D^T = D^T L = I_(2k)",
        "restriction_constructed": True, "singular_parameters_used": False,
        "numerical_fit_used_in_certificate": False,
        "improves_omega": False, "novelty_claimed": False,
    }
    if include_maps:
        result["maps_target_by_source"] = list(map_values)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = certificate(args.k)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({key: value for key, value in report.items()
                      if key not in {"maps_target_by_source", "product_matrix_D_rows",
                                     "product_dual_L_rows"}}, indent=2))

"""Exact controls for the boundary-column extension of the integer seed.

The theorem in outer_product_boundary.md concerns this specified chart.
It does not exclude arbitrary restrictions or degenerations of Q_(6,4).
"""

import importlib.util
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import json


SPEC = importlib.util.spec_from_file_location("outer_product_seed", Path(__file__).with_name("outer_product_injection.py"))
SEED = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SEED)


def boundary_maps(k, crossed=False):
    """Return maps into the old 4k-dimensional B and C output supports."""
    _, old_b, old_c = SEED.maps(k)
    width = 2*k+1
    b = [[0]*(k*width) for _ in range(4*k)]
    c = [[0]*(width*k) for _ in range(4*k)]
    for row in range(4*k):
        for y, s in product(range(k), range(2*k)):
            b[row][y*width+s] = old_b[row][y*(2*k)+s]
        for z, v in product(range(2*k), range(k)):
            c[row][z*k+v] = old_c[row][z*k+v]
        if crossed:
            b[row][(k-1)*width+2*k] = old_b[row][k+1]
            c[row][2*k*k+k-1] = -old_c[row][(k+1)*k]
    return b, c


def source_slices(k, b, c):
    n, width, side = k+2, 2*k+1, 4*k
    bc, cc = SEED.sparse_columns(b), SEED.sparse_columns(c)
    slices = [[0]*(side*side) for _ in range(n*n)]
    for p, q, y, v in product(range(n), range(n), range(k), range(k)):
        for (ib, vb), (ic, vc) in product(bc[y*width+q+v], cc[(p+y)*k+v]):
            slices[n*p+q][side*ib+ic] += vb*vc
    return slices


def pivots(matrix):
    a = [[Fraction(value) for value in row] for row in matrix]
    rank, columns = 0, []
    for column in range(len(a[0])):
        pivot = next((row for row in range(rank, len(a)) if a[row][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        value = a[rank][column]
        a[rank] = [entry/value for entry in a[rank]]
        for row in range(rank+1, len(a)):
            value = a[row][column]
            if value:
                a[row] = [entry-value*other for entry, other in zip(a[row], a[rank])]
        columns.append(column)
        rank += 1
        if rank == len(a):
            break
    return columns


def determinant(matrix):
    """Fraction-free Bareiss determinant, including row swaps."""
    a = [row[:] for row in matrix]
    previous, sign = 1, 1
    for column in range(len(a)-1):
        pivot = next((row for row in range(column, len(a)) if a[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            a[column], a[pivot] = a[pivot], a[column]
            sign = -sign
        value = a[column][column]
        for row in range(column+1, len(a)):
            for col in range(column+1, len(a)):
                numerator = a[row][col]*value-a[row][column]*a[column][col]
                if numerator % previous:
                    raise ArithmeticError("Nonintegral Bareiss step")
                a[row][col] = numerator//previous
            a[row][column] = 0
        previous = value
    return sign*a[-1][-1]


def projected_slices(k, slices):
    b_rows = [4*i+v for i, v in product(range(k), range(2))]
    c_rows = [k*(2*y)+h for y, h in product(range(2), range(k))]
    columns = [4*k*ib+ic for ib, ic in product(b_rows, c_rows)]
    return [[row[column] for column in columns] for row in slices]


def arbitrary_boundary_control(k):
    """A finite check of the proved symbolic rank-one update formula."""
    b, c = boundary_maps(k)
    base = projected_slices(k, source_slices(k, b, c))
    width, n = 2*k+1, k+2
    for row, y in product(range(4*k), range(k)):
        b[row][y*width+2*k] = (3*row+2*y+1) % 7-3
        c[row][2*k*k+y] = (5*row+3*y+2) % 11-5
    actual = projected_slices(k, source_slices(k, b, c))
    changed = [row for row in range(n*n) if actual[row] != base[row]]
    if changed != [n*n-1]:
        raise ArithmeticError("A boundary modification changed a noncorner projected slice")
    b_rows = [4*i+v for i, v in product(range(k), range(2))]
    c_rows = [k*(2*y)+h for y, h in product(range(2), range(k))]
    expected = [b[ib][(k-1)*width+2*k]*c[ic][2*k*k+k-1]
                for ib, ic in product(b_rows, c_rows)]
    if [x-y for x, y in zip(actual[-1], base[-1])] != expected:
        raise ArithmeticError("The corner rank-one update formula failed")
    return {"k": k, "modified_boundary_columns_per_leg": k,
            "projected_source_rows_changed": changed,
            "corner_update_is_specified_outer_product": True}


def certificate(k=4, include_maps=True):
    b, c = boundary_maps(k, crossed=True)
    slices = source_slices(k, b, c)
    n = k+2
    if any(slices[-1]):
        raise ArithmeticError("The crossed boundary does not kill the corner slice")
    columns = pivots(slices[:-1])
    if len(columns) != n*n-1:
        raise ArithmeticError("Unexpected source first-leg rank")
    minor = [[row[column] for column in columns] for row in slices[:-1]]
    det = determinant(minor)
    if abs(det) != 1:
        raise ArithmeticError("The exact rank certificate is not unimodular")
    base_b, base_c = boundary_maps(k)
    base_rank = len(pivots(projected_slices(k, source_slices(k, base_b, base_c))))
    if base_rank != n*n:
        raise ArithmeticError("The unmodified projected map is not injective")
    result = {
        "k": k, "source": f"Q_({n},{k})",
        "source_A_dimension": n*n, "old_target_BC_dimensions": [4*k, 4*k],
        "zero_boundary_pre_A_rank": base_rank,
        "crossed_boundary_pre_A_rank": n*n-1,
        "crossed_boundary_A_kernel": [[n-1, n-1]],
        "killed_corner_all_output_coefficients_checked": (4*k)**2,
        "rank_minor_source_rows": list(range(n*n-1)),
        "rank_minor_output_columns": columns,
        "rank_minor_determinant": det,
        "arbitrary_boundary_control": arbitrary_boundary_control(k),
        "proved_boundary_chart_maximum_A_kernel_dimension": 1,
        "required_A_kernel_dimension_for_stated_M_extension": 2*k+1,
        "stated_boundary_chart_all_order_extension_excluded": True,
        "arbitrary_leading_maps_excluded": False,
        "general_degeneration_excluded": False, "improves_omega": False,
    }
    if include_maps:
        result["long_maps_target_by_source"] = [b, c]
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
                      if key != "long_maps_target_by_source"}, indent=2))

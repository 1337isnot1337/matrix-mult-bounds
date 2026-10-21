"""Exact reduced corner at the endpoint M1 seed; standard library only.

The coefficient identity is constructive. The corner tensor itself cannot
degenerate to M(4,4,4), by the low-rank slice subspace proved in the note.
This does not exclude arbitrary Q(6,4) degeneration charts.
"""

from collections import defaultdict
from fractions import Fraction
import argparse
import json
from pathlib import Path


P = ((1, 0, 0, 0, -1, 0), (0, 0, 1, 0, 0, 0),
     (0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 1))
ENDPOINTS = (0, 3)
INTERIORS = (1, 2)
PRODUCT_PIVOTS = (0, 2, 3, 5, 6, 7, 8)


def ordinary_product_tensor():
    """P times span(1,t^3), in basis (1-t^4,t^2,t^3,t^5,t^6,t^7,t^8)."""
    return [(0, 0, 0, 1), (0, 1, 2, 1), (0, 1, 5, -1),
            (1, 0, 1, 1), (1, 1, 3, 1), (2, 0, 2, 1),
            (2, 1, 4, 1), (3, 0, 3, 1), (3, 1, 6, 1)]


def residual_product_tensor():
    """P times span(t,t^2), modulo P times span(1,t^3)."""
    return [(0, 0, 0, 1), (1, 1, 1, 1), (2, 0, 1, 1)]


def canonical_tensor():
    result = defaultdict(int)
    for terms, width, offset in ((ordinary_product_tensor(), 7, 0),
                                 (residual_product_tensor(), 2, 14)):
        for p, y, a, first in terms:
            for q, v, b, second in terms:
                result[(4*p+q, offset+width*y+b, offset+2*a+v)] += first*second
    return {key: value for key, value in result.items() if value}


def native_maps():
    A = [[0]*36 for _ in range(16)]
    B = [[0]*36 for _ in range(18)]
    C = [[0]*36 for _ in range(18)]
    for p in range(4):
        for q in range(4):
            for a in range(6):
                for b in range(6):
                    A[4*p+q][6*a+b] = P[p][a]*P[q][b]
    for y, native_y in enumerate(ENDPOINTS):
        for a, s in enumerate(PRODUCT_PIVOTS):
            B[7*y+a][9*native_y+s] = 1
    for v, native_v in enumerate(ENDPOINTS):
        for a, z in enumerate(PRODUCT_PIVOTS):
            C[2*a+v][4*z+native_v] = 1
    for y, native_y in enumerate(INTERIORS):
        B[14+2*y][9*native_y+1] = 1
        B[14+2*y+1][9*native_y] = 1
        B[14+2*y+1][9*native_y+4] = 1
    for v, native_v in enumerate(INTERIORS):
        C[14+v][4+native_v] = 1
        C[16+v][native_v] = 1
        C[16+v][16+native_v] = 1
    return A, B, C


def native_contraction(maps):
    sparse_columns = [
        [[(row, M[row][col]) for row in range(len(M)) if M[row][col]]
         for col in range(36)] for M in maps
    ]
    A, B, C = sparse_columns
    result = defaultdict(int)
    for p in range(6):
        for q in range(6):
            for y in range(4):
                for v in range(4):
                    for a, first in A[6*p+q]:
                        for b, second in B[9*y+q+v]:
                            for c, third in C[4*(p+y)+v]:
                                result[(a, b, c)] += first*second*third
    return {key: value for key, value in result.items() if value}


def rank(matrix):
    rows = [list(map(Fraction, row)) for row in matrix]
    if not rows:
        return 0
    pivot_row = 0
    for col in range(len(rows[0])):
        found = next((i for i in range(pivot_row, len(rows)) if rows[i][col]), None)
        if found is None:
            continue
        rows[pivot_row], rows[found] = rows[found], rows[pivot_row]
        scale = rows[pivot_row][col]
        rows[pivot_row] = [value/scale for value in rows[pivot_row]]
        for i in range(pivot_row+1, len(rows)):
            scale = rows[i][col]
            if scale:
                rows[i] = [a-scale*b for a, b in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def flattening(tensor, leg):
    dims = (16, 18, 18)
    other = [i for i in range(3) if i != leg]
    matrix = [[0]*(dims[other[0]]*dims[other[1]]) for _ in range(dims[leg])]
    for key, value in tensor.items():
        matrix[key[leg]][key[other[0]]*dims[other[1]]+key[other[1]]] = value
    return matrix


def b_slice(tensor, functional):
    matrix = [[0]*18 for _ in range(16)]
    for (a, b, c), value in tensor.items():
        matrix[a][c] += value*functional.get(b, 0)
    return matrix


def verify():
    canonical = canonical_tensor()
    native = native_contraction(native_maps())
    failures = [(a, b, c) for a in range(16) for b in range(18) for c in range(18)
                if canonical.get((a, b, c), 0) != native.get((a, b, c), 0)]
    assert not failures
    # Interior B coordinates are 14=x00, 15=x01, 16=x10, 17=x11.
    # Setting x01=0 leaves C coordinates 14,16,17; C15 vanishes identically.
    low_rank_basis = (14, 16, 17)
    supports = []
    for b in low_rank_basis:
        matrix = b_slice(canonical, {b: 1})
        support = sorted({c for row in matrix for c, value in enumerate(row) if value})
        assert set(support) <= {14, 16, 17}
        supports.append(support)
    rank_three_witness = rank(b_slice(canonical, {14: 1, 17: 1}))
    assert rank_three_witness == 3
    pure_slice = [[canonical.get((15, b, c), 0) for c in range(18)] for b in range(18)]
    assert rank(pure_slice) == 4
    # The four-dimensional t^5 tensor P fibre has B support14 and C support4.
    fibre = {(a-12, b, c): value for (a, b, c), value in canonical.items() if a >= 12}
    fibre_b = [[0]*(4*18) for _ in range(18)]
    fibre_c = [[0]*(4*18) for _ in range(18)]
    for (a, b, c), value in fibre.items():
        fibre_b[b][18*a+c] = value
        fibre_c[c][18*a+b] = value
    fibre_dimensions = [rank(fibre_b), rank(fibre_c)]
    assert fibre_dimensions == [14, 4]
    return {
        "source": "Q(6,4)",
        "corner_dimensions": [16, 18, 18],
        "corner_flattening_ranks": [rank(flattening(canonical, i)) for i in range(3)],
        "native_terms_checked": 576,
        "coefficient_positions_checked": 5184,
        "coefficient_failures": len(failures),
        "corner_nonzero_coefficients": len(canonical),
        "coefficient_ring": "Z",
        "P_basis_coefficients": P,
        "endpoint_product_basis": ["1-t^4", "t^2", "t^3", "t^5", "t^6", "t^7", "t^8"],
        "ordinary_product_terms": ordinary_product_tensor(),
        "residual_product_terms": residual_product_tensor(),
        "low_rank_B_functional_basis_indices": list(low_rank_basis),
        "low_rank_B_functional_basis_C_supports": supports,
        "entire_three_dimensional_slice_space_rank_at_most": 3,
        "rank_three_witness_B_coordinates": {14: 1, 17: 1},
        "rank_three_witness_rank": rank_three_witness,
        "pure_t5_tensor_t5_slice_rank": 4,
        "t5_tensor_P_fibre_support_dimensions": fibre_dimensions,
        "maps_target_by_native_source": native_maps(),
        "corner_terms": [list(key)+[value] for key, value in sorted(canonical.items())],
        "corner_cannot_degenerate_to_M4": True,
        "Q64_general_degeneration_excluded": False,
        "improves_omega": False,
        "review_scope": "same-session exact controls; no external review",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ("maps_target_by_native_source", "corner_terms")}, indent=2))


if __name__ == "__main__":
    main()

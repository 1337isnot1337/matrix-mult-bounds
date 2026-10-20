"""Exact finite Koszul and symmetrizer calculations; not an exponent proof.

The Koszul routine reconstructs the preceding session's code. The symmetrizer
calculation records the small candidate obstruction discussed in that session.
"""
from __future__ import annotations
import argparse
from itertools import combinations
import json
from pathlib import Path
import sympy as sp


def convolution(a: int, b: int, output_axis: int = 2):
    if min(a, b) < 1 or output_axis not in (0, 1, 2):
        raise ValueError("invalid convolution dimensions or output axis")
    inputs = [i for i in range(3) if i != output_axis]
    terms, dims = [], [0, 0, 0]
    for i in range(a):
        for j in range(b):
            term = [0, 0, 0]
            term[inputs[0]], term[inputs[1]], term[output_axis] = i, j, i + j
            terms.append(tuple(term))
    dims[inputs[0]], dims[inputs[1]], dims[output_axis] = a, b, a + b - 1
    return dims, terms


def koszul_matrix(dims, terms, p: int, shared: int = 0):
    v, w = [i for i in range(3) if i != shared]
    A = dims[shared]
    if not 0 <= p < A:
        raise ValueError("invalid exterior degree")
    columns = list(combinations(range(A), p))
    rows = list(combinations(range(A), p + 1))
    row_index = {s: i for i, s in enumerate(rows)}
    mat = sp.zeros(dims[w] * len(rows), dims[v] * len(columns))
    for term in terms:
        i, j, k = term[shared], term[v], term[w]
        for t, c in enumerate(columns):
            if i in c:
                continue
            row = tuple(sorted((*c, i)))
            sign = (-1) ** sum(q < i for q in c)
            mat[k * len(rows) + row_index[row], j * len(columns) + t] += sign
    return mat


def symmetrizer_matrix(dims, terms):
    """Coefficients of M_z L - (M_z L)^T for an n by n slice space."""
    n, m, depth = dims
    if n != m:
        raise ValueError("this symmetrizer uses equal first and second dimensions")
    xs = sp.symbols(f"l0:{n*n}")
    L = sp.Matrix(n, n, xs)
    equations = []
    for z in range(depth):
        M = sp.zeros(n, n)
        for i, j, k in terms:
            if k == z:
                M[i, j] += 1
        A = M * L
        equations.extend(A[i, j] - A[j, i] for i in range(n) for j in range(i + 1, n))
    return sp.linear_eq_to_matrix(equations, xs)[0]


def run():
    cases = []
    for a, b in [(2, 2), (2, 3), (3, 3), (3, 4), (4, 7)]:
        dims, terms = convolution(a, b, 0)
        for p in range(1, min(dims[0] - 1, 4)):
            M = koszul_matrix(dims, terms, p)
            cases.append({"convolution": [a, b], "dimensions": dims, "exterior_degree": p,
                          "matrix_shape": list(M.shape), "rank": int(M.rank())})
    source_dims, source_terms = convolution(3, 3)
    target_terms = [(i + j, i, j) for i in range(2) for j in range(2)]
    target_terms += [(i, 2, i + 2) for i in range(3)]
    source_eq = symmetrizer_matrix(source_dims, source_terms)
    target_eq = symmetrizer_matrix([3, 3, 5], target_terms)
    sr, tr = int(source_eq.rank()), int(target_eq.rank())
    if (sr, tr) != (8, 9):
        raise AssertionError(f"unexpected symmetrizer ranks: {(sr, tr)}")
    _, c23 = convolution(2, 3, 0)
    M = koszul_matrix([4, 2, 3], c23, 2)
    det = int(M.det())
    if M.rank() != 12 or det == 0:
        raise AssertionError("the C(2,3) Koszul matrix is not invertible")
    return {"status": "exact finite calculations; supporting arguments remain unreviewed",
            "sympy_version": sp.__version__, "koszul_cases": cases,
            "c23_exterior_degree_2": {"shape": [12, 12], "rank": 12, "determinant": det,
                "three_sector_target_rank": 36, "rank_one_flattening_bound": 3,
                "target_border_rank_lower_bound": 12, "c46_source_rank_upper_bound": 9},
            "symmetrizer": {"source": "C(3,3)", "target_dimensions": [3, 3, 5],
                "target_terms": target_terms, "source_equation_rank": sr,
                "source_kernel_dimension": 9 - sr, "target_equation_rank": tr,
                "target_kernel_dimension": 9 - tr,
                "target_full_column_rank_witness_rows": list(target_eq.T.rref()[1])}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))

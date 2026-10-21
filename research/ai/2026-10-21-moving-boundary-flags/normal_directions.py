"""Exact normal directions for maximal first extensions of the root flags."""
import argparse
from collections import defaultdict
from functools import lru_cache
import importlib.util
from itertools import product
import json
from pathlib import Path

import sympy as sp

PATH = Path(__file__).resolve().parents[1] / '2026-10-21-quantum-extension-spaces/extensions.py'
SPEC = importlib.util.spec_from_file_location('moving_boundary_extensions', PATH)
extension = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(extension)
KERNEL = [extension.index(i, j, z)
          for i, j, z in product(range(4), range(4), extension.LONG)]
NORMAL = [112*b+j for b in range(8) for j in range(112)
          if (j//28 if b < 4 else (j//7) % 4) in (1, 2)]


def row_matrix(rows):
    return sp.MutableSparseMatrix(len(rows), 112,
                                  {(i, j): value for i, row in enumerate(rows)
                                   for j, value in row.items()})


def complement(rows):
    combined = extension.G+rows
    _, pivots = row_matrix(combined).T.to_DM().rref()
    return [combined[i] for i in pivots if i >= 4]


def sparse_nullspace(matrix):
    reduced, pivots = matrix.to_DM().rref()
    reduced = reduced.to_Matrix()
    free = [j for j in range(matrix.cols) if j not in pivots]
    entries = {(j, k): 1 for k, j in enumerate(free)}
    for k, j in enumerate(free):
        for i, p in enumerate(pivots):
            if reduced[i, j]:
                entries[p, k] = -reduced[i, j]
    return sp.MutableSparseMatrix(matrix.cols, len(free), entries), free


def derivative_operator(left, right):
    """Map the eight leading rows to the 64-by-4-by-4 first coefficient."""
    entries = defaultdict(int)
    for (x, col), value in left.todok().items():
        u, c = divmod(col, 4)
        for b in range(4):
            entries[16*x+4*b+c, 112*b+u] += value
    for (x, col), value in right.todok().items():
        b, v = divmod(col, 112)
        for c in range(4):
            entries[16*x+4*b+c, 448+112*c+v] += value
    return sp.MutableSparseMatrix(1024, 896, dict(entries))


def distinct_rows(matrix):
    by_row = defaultdict(dict)
    for (i, j), value in matrix.todok().items():
        by_row[i][j] = value
    rows = sorted({tuple(sorted(row.items())) for row in by_row.values()})
    return sp.MutableSparseMatrix(len(rows), matrix.cols,
                                  {(i, j): value for i, row in enumerate(rows)
                                   for j, value in row})


@lru_cache(None)
def data():
    identity = [{i: 1} for i in range(112)]
    first = extension.contract(extension.G, extension.G, range(112))
    annihilator = sp.MutableSparseMatrix(sp.Matrix.hstack(*first.nullspace()).T)
    core = first[extension.A0, :]
    _, selected = core.to_DM().rref()
    selector = sp.MutableSparseMatrix(12, 16, {(i, j): 1 for i, j in enumerate(selected)})
    recover = sp.MutableSparseMatrix(core[:, list(selected)].inv().T*selector)
    left = extension.contract(identity, extension.G, KERNEL)
    right = extension.contract(extension.G, identity, KERNEL)
    operator = derivative_operator(left, right)
    first_constraints = sp.kronecker_product(sp.SparseMatrix.eye(64), annihilator)*operator[:, NORMAL]
    first_kernel, free = sparse_nullspace(first_constraints)
    derivative = operator[:, NORMAL]*first_kernel
    y = sp.kronecker_product(sp.SparseMatrix.eye(64), recover)*derivative
    cb = sp.Matrix(256, 112, lambda r, c: left[r//4, 4*c+r % 4])
    cc = sp.Matrix(256, 112, lambda r, c: right[r//4, 112*(r % 4)+c])
    zb = sparse_nullspace(cb.T)[0].T
    zc = sparse_nullspace(cc.T)[0].T
    eb, ec = complement(extension.EB), complement(extension.EC)
    cuts = []
    for side, basis, quotient in (('B', eb, zb), ('C', ec, zc)):
        for row in basis:
            if side == 'B':
                one = extension.contract([row], identity, KERNEL)
                old = extension.contract([row], extension.G, extension.A0)
                offset = 448
            else:
                one = extension.contract(identity, [row], KERNEL)
                old = extension.contract(extension.G, [row], extension.A0)
                offset = 0
            entries = {(4*x+c, offset+112*c+v): value
                       for (x, v), value in one.todok().items() for c in range(4)}
            direct = sp.MutableSparseMatrix(256, 896, entries)
            residual = (direct[:, NORMAL]*first_kernel
                        - sp.kronecker_product(sp.SparseMatrix.eye(64), old.T)*y)
            cuts.append(quotient*residual)
    raw = sp.MutableSparseMatrix.vstack(*cuts)
    return {'first': first, 'first_constraints': first_constraints,
            'first_kernel': first_kernel, 'free': free,
            'operator': operator, 'recover': recover,
            'cross_constraints': distinct_rows(raw), 'raw_cross_rows': raw.rows,
            'left_constraints': cb, 'right_constraints': cc,
            'E_B_complement': eb, 'E_C_complement': ec}


def plane_directions():
    """P_z changes by -e_(k,j,z), Q_z by e_(j,k,z)."""
    directions = []
    for j, k in product((0, 3), (1, 2)):
        p = [{extension.index(k, j, z): -1} for z in extension.LONG]
        q = [{extension.index(j, k, z): 1} for z in extension.LONG]
        directions.append(p+q)
    return directions


def report():
    d = data()
    first, cross = d['first_constraints'], d['cross_constraints']
    directions = sp.Matrix.hstack(*(sp.Matrix([row.get(j, 0) for row in rows
                                               for j in range(112)])
                                   for rows in plane_directions()))
    normal = directions[NORMAL, :]
    parameters = normal[d['free'], :]
    assert d['first_kernel']*parameters == normal
    assert first*normal == sp.zeros(256, 4)
    assert cross*parameters == sp.zeros(cross.rows, 4)
    assert extension.rational_rank(parameters) == 4
    certificates = {'first_normal_constraints': extension.rank_certificate(first),
                    'normal_cross_constraints': extension.rank_certificate(cross)}
    assert certificates['first_normal_constraints']['rational_rank'] == 220
    assert certificates['normal_cross_constraints']['rational_rank'] == 224
    assert d['first_kernel'].cols == 228
    return {'prime': extension.PRIME, 'field': 'Q',
            'kernel_coordinates': KERNEL, 'normal_variable_indices': NORMAL,
            'E_B_complement': d['E_B_complement'], 'E_C_complement': d['E_C_complement'],
            'first_normal_kernel_dimension': 228,
            'raw_cross_rows': d['raw_cross_rows'],
            'distinct_nonzero_cross_rows': cross.rows,
            'rank_certificates': certificates,
            'remaining_normal_dimension': 4, 'plane_directions': plane_directions(),
            'scope': 'Exact finite linear lemma for the all-order proof; both outside first-jet quotient ranks must be 16.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')

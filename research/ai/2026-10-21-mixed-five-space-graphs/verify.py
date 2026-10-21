"""Exact closure for four fixed mixed-row graphs, including quadratic spans."""
import argparse
from functools import lru_cache
import importlib.util
from itertools import combinations_with_replacement
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('graph_pure', HERE.parent / '2026-10-21-pure-mixed-five-spaces/verify.py')
pure = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pure)
uniform, point, frames, normal, third = pure.uniform, pure.point, pure.frames, pure.normal, pure.third
encode = uniform.encode
GRAPHS = ((1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1), (1, 1, 1, 1, 1, 1), (2, -1, 1, 3, -2, 1))
PRIME = 32003


def quadratic_span(matrix, witnesses):
    """Full modular row rank proves the rational quadrics span Sym^2."""
    n, rows = matrix.cols, matrix.rows//3
    if matrix.rows != 3*rows or not n:
        raise ArithmeticError('Invalid three-column quadratic space')
    monomials = list(combinations_with_replacement(range(n), 2))
    if len(witnesses) != len(monomials):
        raise ArithmeticError('Wrong number of quadratic witnesses')
    indices = {pair: i for i, pair in enumerate(monomials)}
    cells = [[{} for _ in range(3)] for _ in range(rows)]
    for (i, j), value in matrix.todok().items():
        value = sp.Rational(value)
        if int(value.q) % PRIME == 0:
            raise ArithmeticError('Quadratic denominator is not a modular unit')
        cells[i % rows][i//rows][j] = int(value.p)*pow(int(value.q), -1, PRIME) % PRIME
    pivots = {}

    def product(out, left, right, sign):
        for i, x in left.items():
            for j, y in right.items():
                k = indices[tuple(sorted((i, j)))]
                value = (out.get(k, 0)+sign*x*y) % PRIME
                if value:
                    out[k] = value
                else:
                    out.pop(k, None)

    for r, s, c, d in witnesses:
        if not (0 <= r < s < rows and 0 <= c < d < 3):
            raise ArithmeticError('Invalid quadratic minor coordinates')
        poly = {}
        product(poly, cells[r][c], cells[s][d], 1)
        product(poly, cells[r][d], cells[s][c], -1)
        while poly:
            pivot = min(poly)
            if pivot not in pivots:
                inverse = pow(poly[pivot], -1, PRIME)
                pivots[pivot] = {j: x*inverse % PRIME for j, x in poly.items()}
                break
            scalar = poly[pivot]
            for j, x in pivots[pivot].items():
                value = (poly.get(j, 0)-scalar*x) % PRIME
                if value:
                    poly[j] = value
                else:
                    poly.pop(j, None)
        if not poly:
            raise ArithmeticError('Quadratic witness rows are dependent')
    if len(pivots) != len(monomials):
        raise ArithmeticError('Quadratic span is incomplete')
    return {'prime': PRIME, 'parameters': n, 'quadratic_dimension': len(monomials),
            'rank_mod_prime': len(pivots)}


@lru_cache(None)
def source_data():
    data = uniform.data()
    specialization = {frames.A: 1, frames.B: 1}
    psi = sp.SparseMatrix(data['virtual']['psi'].subs(specialization))
    tensor = sp.SparseMatrix(data['virtual']['third'].subs(specialization))
    sources = sp.SparseMatrix(data['sources'].subs(specialization))
    plane = frames.plane_parameters()[data['normal_certificate']['free_coordinates'], :]
    if not frames.zero(psi*plane) or not frames.zero(tensor*plane):
        raise ArithmeticError('Plane directions have nonzero obstructions')
    first, second = sp.SparseMatrix.eye(64), sp.SparseMatrix.eye(64)
    for k, source in enumerate(normal.KERNEL):
        i, s, z = source//28, (source//7) % 4, source % 7
        if i == 2:
            first[normal.KERNEL.index(28+7*s+z), k] -= 1
        if s == 2:
            second[normal.KERNEL.index(28*i+7+z), k] += 1
    change = first*second
    if any(i >= j for i, j in (change-sp.eye(64)).todok()):
        raise ArithmeticError('Source basis change is not unitriangular')
    return psi, tensor, sources, plane, change


@lru_cache(None)
def graph_data(graph):
    psi, tensor, sources, plane, change = source_data()
    shear = sp.SparseMatrix.eye(7)
    for i, value in enumerate(graph):
        shear[i, 6] = value
    psi = sp.kronecker_product(shear.T, sp.SparseMatrix.eye(200))*psi
    tensor = sp.kronecker_product(sp.SparseMatrix.eye(448), shear.T)*tensor
    low = sp.kronecker_product(sources.T, sp.SparseMatrix.eye(49))*tensor
    mixed = sp.MutableSparseMatrix.vstack(psi[1200:1400, :],
        low[[49*i+7*j+6 for i in range(16) for j in range(7)], :])
    kernel, free = normal.sparse_nullspace(mixed)
    if kernel.cols != 32 or not frames.zero(mixed*kernel):
        raise ArithmeticError('Unexpected graph normal kernel')
    rows = 312
    entries = {(rows*(i//200)+i % 200, k): value for (i, k), value in psi.todok().items()}
    for source in range(16):
        for (i, k), value in low[49*source:49*(source+1), :].todok().items():
            b, c = divmod(i, 7)
            entries[rows*c+200+7*source+b, k] = value
    obstruction = sp.SparseMatrix(7*rows, 88, entries)*kernel
    basis, _ = point.row_basis(point.joint(obstruction, rows))
    _, columns = point.flat(basis, kernel.cols).to_DM().rref()
    columns = list(columns)
    quotient = kernel[:, columns]
    n = quotient.cols
    if n != 28 or third.matrix_rank(sp.Matrix.hstack(plane, quotient)) != 32:
        raise ArithmeticError('Incorrect complement to plane directions')
    obstruction = obstruction[:, columns]
    if obstruction[6*rows:, :].todok():
        raise ArithmeticError('The actual mixed row is not annihilated')
    basis, _ = point.row_basis(point.joint(obstruction, rows))
    even = [2*n*j+k for j in range(3) for k in range(n)]
    odd = [2*n*j+n+k for j in range(3) for k in range(n)]
    projection = basis[:, odd]-basis[:, even]
    stable_kernel, _ = normal.sparse_nullspace(projection.T)
    stable = stable_kernel.T*basis
    if not frames.zero(stable[:, odd]-stable[:, even]):
        raise ArithmeticError('Stable rows have nonzero projection')
    w_coefficients = pure.flat3(stable[:, even], n)
    w_kernel, _ = normal.sparse_nullspace(w_coefficients)
    q_rows, _ = point.row_basis(projection)
    q = pure.flat3(q_rows, n)
    if (basis.rows, stable.rows, w_kernel.cols) != (56, 10, 10):
        raise ArithmeticError('Unexpected graph projection dimensions')
    parameters, rounds = sp.SparseMatrix.eye(n), []
    while parameters.cols:
        cuts, witnesses = pure.forced_forms(q*parameters, q_rows.rows, 3, 2)
        if not cuts.rows:
            break
        reduced, _ = normal.sparse_nullspace(cuts)
        if reduced.cols >= parameters.cols:
            raise ArithmeticError('Square minors did not reduce parameters')
        rounds.append({'before': parameters.cols, 'after': reduced.cols, 'minors': witnesses})
        parameters = parameters*reduced
    remaining = q*parameters
    if third.matrix_rank(remaining) != parameters.cols:
        raise ArithmeticError('Projection has a nonzero coefficient kernel')
    transformed = sp.kronecker_product(change.T, sp.SparseMatrix.eye(49))*tensor*quotient
    return {'normal_free': free, 'quotient': quotient, 'basis': basis, 'stable': stable,
            'w_kernel': w_kernel, 'q_rounds': rounds, 'q_remaining': remaining,
            'third': transformed}


def terminal(data):
    parameters = data['w_kernel']
    base = point.flat(data['basis'], 28)
    selected, records = set(), []
    while parameters.cols:
        xp, jp = base*parameters, data['third']*parameters
        count = data['basis'].rows
        rows = count+7*len(selected)
        entries = {(rows*(i//count)+i % count, j): value for (i, j), value in xp.todok().items()}
        for k, source in enumerate(sorted(selected)):
            for (i, j), value in jp[49*source:49*(source+1), :].todok().items():
                b, c = divmod(i, 7)
                entries[rows*c+count+7*k+b, j] = value
        obstruction = sp.SparseMatrix(7*rows, parameters.cols, entries)
        mixed = obstruction[6*rows:, :]
        if mixed.todok():
            reduced, _ = normal.sparse_nullspace(mixed)
            if reduced.cols >= parameters.cols:
                raise ArithmeticError('Mixed-row equations did not reduce parameters')
            records.append({'kind': 'mixed_row', 'before': parameters.cols, 'after': reduced.cols})
            parameters = parameters*reduced
            continue
        row_basis, pivots = point.row_basis(point.joint(obstruction, rows))
        joint = sp.SparseMatrix(448, 7*parameters.cols,
            {(i//7, parameters.cols*(i % 7)+j): value for (i, j), value in jp.todok().items()})
        residual = joint-joint[:, pivots]*row_basis
        additions = []
        for source in range(64):
            if source in selected:
                continue
            block = residual[7*source:7*(source+1), :]
            if not block.todok():
                continue
            cover = point.cover({(i, j//parameters.cols) for i, j in block.todok()})
            bound = None
            if cover:
                point.check_cover(block, parameters.cols, cover)
                bound = {'cover': cover}
            else:
                rank = third.matrix_rank(block)
                if rank <= 2:
                    bound = {'joint_B_rank': rank}
            if bound is not None:
                additions.append({'source_position': source, 'source_index': normal.KERNEL[source], 'bound': bound})
        if not additions:
            raise ArithmeticError('Graph terminal elimination stalled')
        selected.update(item['source_position'] for item in additions)
        records.append({'kind': 'low_sources', 'parameters': parameters.cols, 'sources': additions})
    return records


@lru_cache(None)
def report():
    witnesses = {tuple(item['graph']): item['selected_minors']
                 for item in json.loads((HERE / 'quadratic-witnesses.json').read_text())}
    if not sp.isprime(PRIME):
        raise ArithmeticError('Modular characteristic must be prime')
    cases = []
    for graph in GRAPHS:
        data = graph_data(graph)
        quadratic = quadratic_span(data['q_remaining'], witnesses[graph]) if data['q_remaining'].cols else None
        cases.append({'graph': list(graph), 'normal_dimension': 32, 'plane_dimension': 4,
                      'normal_free_coordinates': data['normal_free'], 'quotient': encode(data['quotient']),
                      'joint_rows': 56, 'stable_rows': 10, 'stable_kernel': encode(data['w_kernel']),
                      'square_minor_rounds': data['q_rounds'], 'quadratic_span': quadratic,
                      'terminal': terminal(data), 'final_nonplane_dimension': 0})
    return {'claim': 'AI-MIXED-FIVE-GRAPH-CONTROLS-090', 'partner': {'a': 1, 'b': 1},
            'cases': cases, 'all_graphs_classified': False, 'independent_review': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = json.dumps(report(), indent=2, default=int)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result)
    else:
        print(result, end='')

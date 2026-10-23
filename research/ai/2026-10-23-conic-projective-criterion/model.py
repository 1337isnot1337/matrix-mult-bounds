"""Homogeneous conic frames and the complete pinned source operator.

The four residual strata are disjoint and cover both residual projective lines.
All frame operations divide only by the literal constants +1 or -1.
"""
from itertools import product
import importlib.util
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[3]
a, b, c, d, x, t = s.symbols('a b c d x t')
SYMBOLS = dict(zip(('a', 'b', 'c', 'd', 'x', 't'), (a, b, c, d, x, t)))
STRATA = ('finite', 'a_infinity', 'b_infinity', 'both_infinity')
LONG = (1, 2, 4, 5)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expand(matrix):
    return matrix.applyfunc(s.expand)


def encode(matrix):
    return {'shape': list(matrix.shape), 'entries': [
        [i, j, str(s.expand(z))] for (i, j), z in sorted(matrix.todok().items()) if z]}


def index(i, j, z):
    return 28*i+7*j+z


def residuals(stratum):
    if stratum not in STRATA:
        raise ValueError('Unknown residual projective stratum')
    aa = (0, 1) if stratum in ('a_infinity', 'both_infinity') else (1, a)
    bb = (0, 1) if stratum in ('b_infinity', 'both_infinity') else (1, b)
    return aa+bb


def core_frame(kernel, side):
    """A seven-row frame containing the two fixed G cores, with a unit minor."""
    pivot = next(j for j, z in enumerate(kernel) if z in (-1, 1))
    free = [j for j in range(8) if j != pivot]
    canonical = s.Matrix(7, 8, lambda i, j:
        int(j == free[i])-kernel[free[i]]/kernel[pivot]*int(j == pivot))
    g = (s.Matrix([[0, 0, 0, 1, 0, -1, 0, 0],
                   [0, 0, 1, 0, -1, 0, 0, 0]]) if side == 'B' else
         s.Matrix([[0, 0, 0, -1, 0, 0, 1, 0],
                   [0, -1, 0, 0, 1, 0, 0, 0]]))
    assert not expand(g*kernel).todok()
    remove = g[:, free].rref()[1]
    frame = g.col_join(canonical[[i for i in range(7) if i not in remove], :])
    assert s.expand(frame[:, free].det()) in (-1, 1)
    return frame, pivot


def core_to_map(core, side):
    """Embed a seven-by-four cubic core into its complete fourteen-by-112 map."""
    result = s.zeros(14, 112)
    for (row, comp), value in core.todok().items():
        j, r = divmod(comp, 2)
        for (power,), coefficient in s.Poly(value, x).terms():
            if coefficient == 0:
                continue
            if not 0 <= power <= 3:
                raise ValueError('The literal core must have x degree at most three')
            for eps in (0, 1):
                column = (index(power, 3*j, 4-3*r+eps) if side == 'B'
                          else index(3*r, power, 4-3*j+eps))
                result[2*row+eps, column] = coefficient
    return expand(result)


def pivot_coordinates(core_pivot, side):
    endpoint, comp = divmod(core_pivot, 4)
    j, r = divmod(comp, 2)
    return [(index(3*endpoint, 3*j, 4-3*r+eps) if side == 'B'
             else index(3*r, 3*endpoint, 4-3*j+eps)) for eps in (0, 1)]


def homogeneous_base(r, q, aa0, aa1, bb0, bb1):
    """Here q is the homogeneous coordinate called s in the written proof."""
    u = s.Matrix([aa1*r, -aa1*q, aa0*r, -aa0*q])
    v = s.Matrix([-bb1*r, bb0*r, bb1*q, -bb0*q])
    delta = s.expand((aa1*r-aa0*q)*(bb1*r+bb0*q))
    assert s.expand((u.T*v)[0]+delta) == 0
    ub, bp = core_frame((r*v).col_join(-q*v), 'B')
    vc, cp = core_frame((r*u).col_join(-q*u), 'C')
    U = ub[:, :4]+x**3*ub[:, 4:]
    V = vc[:, :4]+x**3*vc[:, 4:]
    if r == 1:
        K, L = ub[:, 4:]*v, vc[:, 4:]*u
    elif q == 1:
        K, L = ub[:, :4]*v, vc[:, :4]*u
    else:
        raise ValueError('A normalized homogeneous conic chart is required')
    K, L = expand(K), expand(L)
    assert not expand(U*v-(q+r*x**3)*K).todok()
    assert not expand(V*u-(q+r*x**3)*L).todok()
    B, C = core_to_map(U, 'B'), core_to_map(V, 'C')
    rawb = [index(p, j, z) for p, j, z in product((0, 3), (0, 3), LONG)]
    rawc = [index(j, p, z) for p, j, z in product((0, 3), (0, 3), LONG)]
    omitted_b, omitted_c = pivot_coordinates(bp, 'B'), pivot_coordinates(cp, 'C')
    rawb = omitted_b+[j for j in rawb if j not in omitted_b]
    rawc = omitted_c+[j for j in rawc if j not in omitted_c]
    return {'r': r, 's': q, 'a0': aa0, 'a1': aa1, 'b0': bb0, 'b1': bb1,
            'u': u, 'v': v, 'delta': delta, 'U': U, 'V': V, 'K': K, 'L': L,
            'B': B, 'C': C, 'raw_B': rawb, 'raw_C': rawc}


def base(stratum, conic_chart='finite'):
    aa0, aa1, bb0, bb1 = residuals(stratum)
    if conic_chart == 'finite':
        return homogeneous_base(1, c, aa0, aa1, bb0, bb1)
    if conic_chart == 'infinity':
        return homogeneous_base(0, 1, aa0, aa1, bb0, bb1)
    raise ValueError('Unknown conic chart')


def normals(data, middle):
    return (core_to_map(x**middle*data['K']*data['u'].T, 'B'),
            core_to_map(-x**middle*data['L']*data['v'].T, 'C'))


def plane_fields(data):
    """The twelve independent motions of the three ambient two-planes."""
    rawb, rawc = data['raw_B'], data['raw_C']
    lb, lc = data['B'][:, rawb], data['C'][:, rawc]
    fields = []
    for node, endpoint, middle in product(range(3), (0, 3), (1, 2)):
        db, dc = s.zeros(16, 112), s.zeros(16, 112)
        for side, raw, matrix in (('B', rawb, db), ('C', rawc, dc)):
            for row, loc in enumerate(raw):
                first, rem = divmod(loc, 28)
                second, z = divmod(rem, 7)
                p, q = (first, second) if side == 'B' else (second, first)
                def idx(pp, qq, zz):
                    return index(pp, qq, zz) if side == 'B' else index(qq, pp, zz)
                if node == 0 and p == endpoint:
                    matrix[row, idx(middle, q, z)] += 1
                if node == (2 if side == 'B' else 1) and q == endpoint:
                    matrix[row, idx(p, middle, z)] += 1
                if node == (1 if side == 'B' else 2):
                    if endpoint == 0:
                        if z == 6-middle:
                            matrix[row, idx(p, q, 6)] -= 2
                        if z == 3-middle:
                            matrix[row, idx(p, q, 3)] -= 1
                    else:
                        if z == 6-middle:
                            matrix[row, idx(p, q, 3)] -= 1
                        if z == 3-middle:
                            matrix[row, idx(p, q, 0)] -= 2
        fields.append((expand(lb*db), expand(lc*dc)))
    return fields


def complete_operator(stratum):
    """Use the credited full source quotient, with the new polynomial frames."""
    previous = load('research/ai/2026-10-21-conic-second-jets/verify.py',
                    'conic_projective_previous_'+stratum)
    data = base(stratum)
    m = previous.m
    m.base = lambda: (data['B'], data['C'])
    geometry = (data['raw_B'], data['raw_C'], plane_fields(data))
    m.geometry = lambda: geometry
    m.flattening.cache_clear()
    m.sector.cache_clear()
    previous.normals = lambda: {k: normals(data, k) for k in (1, 2)}
    return previous, data


def reverse_map(matrix):
    """Literal source reversal, followed by the two-row parity permutation."""
    result = s.zeros(*matrix.shape)
    for (row, col), value in matrix.todok().items():
        i, rem = divmod(col, 28)
        j, z = divmod(rem, 7)
        result[row ^ 1, index(3-i, 3-j, 6-z)] = value
    return result

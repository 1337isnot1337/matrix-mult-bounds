"""Exact polynomial flag controls; no numerical or solver dependencies."""
from __future__ import annotations

from math import comb
import sympy as sp


def points(m):
    return [(a, degree-a) for degree in range(m) for a in range(degree+1)]


def tensor(G, P, Q):
    """Direct multiplication and output evaluation, independent of flag degrees."""
    result = []
    for p in range(G.rows):
        for y in range(P.rows):
            product = [sum(G[p, i]*P[y, k-i]
                           for i in range(max(0, k-P.cols+1), min(G.cols-1, k)+1))
                       for k in range(Q.cols)]
            result.extend(sum(value*Q[z, k] for k, value in enumerate(product))
                          for z in range(Q.rows))
    return result


def check_limit(m, G, P, Q, weights):
    coordinates = points(m)
    values = iter(tensor(G, P, Q))
    retained = discarded = checked = 0
    for p in range(m):
        for y, (a, b) in enumerate(coordinates):
            for z, (c, d) in enumerate(coordinates):
                value = next(values)
                wanted = int(p == a+c and a+b+c+d == m-1)
                weight = weights[0][p]+weights[1][y]+weights[2][z]
                if wanted and weight != 0:
                    raise ArithmeticError('target grading incorrect')
                if weight <= 0 and value != (wanted if weight == 0 else 0):
                    raise ArithmeticError(f'wrong leading coefficient {(p,y,z)}')
                retained += bool(wanted)
                discarded += bool(value and weight > 0)
                checked += 1
    return {'coefficients_checked': checked, 'retained_terms': retained,
            'discarded_positive_terms': discarded}


def shear(degree, c):
    """Row action f(t) -> (1+ct)^degree f(t/(1+ct))."""
    return sp.Matrix(degree+1, degree+1,
                     lambda j, k: comb(degree-j, k-j)*c**(k-j) if k >= j else 0)


def translate(degree, b):
    return sp.Matrix(degree+1, degree+1,
                     lambda j, k: comb(j, k)*b**(j-k) if k <= j else 0)


def source_change(G, P, Q, action, parameter):
    return (G*action(G.cols-1, parameter), P*action(P.cols-1, parameter),
            Q*action(Q.cols-1, -parameter).T)


def echelon_flag(matrix, weights, highest):
    if len(set(weights)) != len(weights):
        raise ValueError('strict flag weights required')
    result = matrix.copy()
    order = sorted(range(matrix.rows), key=weights.__getitem__)
    pivots = []
    for rank, row in enumerate(order):
        for old_row, pivot in pivots:
            factor = result[row, pivot]/result[old_row, pivot]
            result[row, :] -= factor*result[old_row, :]
        pivot = matrix.cols-1-rank if highest else rank
        if result[row, pivot] == 0:
            raise ArithmeticError('nongeneric flag at selected source point')
        pivots.append((row, pivot))
    return result


def normalize(m, G, P, Q, weights, maximum_point=100):
    """Construct the written normal form for an exact rational control."""
    for c in range(1, maximum_point+1):
        changed = source_change(G, P, Q, shear, sp.Integer(c))
        try:
            A = echelon_flag(changed[0], weights[0], True)
            Y = echelon_flag(changed[1], weights[1], True)
            Z = echelon_flag(changed[2], weights[2], False)
        except ArithmeticError:
            continue
        break
    else:
        raise ArithmeticError('no generic control point in specified finite search')
    D = m-1
    s = A[D-1, 1]/A[D, 0]
    gamma = 1/(A[D, 0]*s**D)
    for p in range(m):
        A[p, :] *= gamma*s**p
    coordinates = points(m)
    ry = {row: rank for rank, row in enumerate(sorted(range(Y.rows), key=weights[1].__getitem__))}
    sector_scale = {a+b: 1/Y[y, Y.cols-1-ry[y]]
                    for y, (a, b) in enumerate(coordinates) if a == 0}
    for y, (a, b) in enumerate(coordinates):
        Y[y, :] *= sector_scale[a+b]*s**(-a)
    for z, (a, b) in enumerate(coordinates):
        Z[z, :] *= s**(-a)/(gamma*sector_scale[D-a-b])
    A, Y, Z = source_change(A, Y, Z, translate, -A[D-1, 0])
    if list(A[D, :]) != [1]+[0]*D or list(A[D-1, :]) != [0, 1]+[0]*(D-1):
        raise ArithmeticError('failed shared pivot anchors')
    return A, Y, Z, c


def coordinate_control(witness, perturb=True):
    m, B = witness['m'], witness['B']
    n = m*(m+1)//2
    G, P, Q = sp.zeros(m), sp.zeros(n, B), sp.zeros(n, B+m-1)
    for row, column in enumerate(witness['source_x_indices']):
        G[row, column] = 1
    for row, column in enumerate(witness['source_y_indices']):
        P[row, column] = 1
    for row, columns in enumerate(witness['output_source_indices']):
        for column in columns:
            Q[row, column] = 1
    weights = [list(witness['weights'][name]) for name in ('x', 'y', 'z')]
    if perturb:
        weights = [[100*w for w in leg] for leg in weights]
        for i, (a, b) in enumerate(points(m)):
            weights[1][i] += (a+b)**2
            weights[2][i] -= (m-1-a-b)**2
    return G, P, Q, weights


def fixed_basis_control(witness):
    """Replay a frozen fixed-basis SAT witness without importing its solver."""
    m, B = witness['m'], witness['B']
    n, width = m*(m+1)//2, B+m-1
    G = sp.Matrix(witness['shared_matrix'])
    P = sp.zeros(n, B)
    Q = sp.Matrix([[sp.Rational(value) for value in row]
                   for row in witness['output_matrix']])
    if witness.get('basis_model') == 'reverse-Newton':
        t = sp.Symbol('t')
        conversion = sp.Matrix(width, width,
            lambda j, k: sp.Poly(sp.prod(t-i for i in range(j)), t).nth(k))
        for y, j in enumerate(witness['source_y_indices']):
            P[y, :] = conversion[j, :B]
        # Q originally evaluates coordinates in the Newton output basis.
        Q = Q*conversion.inv().T
    else:
        for y, j in enumerate(witness['source_y_indices']):
            P[y, j] = 1
    weights = [witness['weights'][name] for name in ('x', 'y', 'z')]
    return check_limit(m, G, P, Q, weights)

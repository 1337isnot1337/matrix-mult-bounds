"""Exact coefficient acceptance for the fixed-shared-leg graded ansatz."""
import importlib.util
from pathlib import Path
import sympy as sp

spec = importlib.util.spec_from_file_location('fatpoint', Path(__file__).with_name('fatpoint_route.py'))
target = importlib.util.module_from_spec(spec)
spec.loader.exec_module(target)


def verify(a, b, p, q, g=None, alpha=1, beta=0):
    dims, terms = target.tensor(a)
    n = dims[1]
    if p.shape != (b, n) or q.shape != (n, b+a-1):
        raise ValueError('incorrect coefficient map dimensions')
    g = sp.eye(a) if g is None else g
    if g.shape != (a, a):
        raise ValueError('incorrect shared map dimension')
    if not all(value.is_Rational for matrix in (p, q, g) for value in matrix):
        raise ValueError('certificate entries must be exact rationals')
    degrees = [d for d in range(a) for _ in range(d+1)]
    exponents = [i for d in range(a) for i in range(d+1)]
    desired = set(terms)
    bad_negative, bad_constant = [], []
    count = 0
    basis = [q[:, h:h+b]*p for h in range(a)]
    for i in range(a):
        coefficients = sp.zeros(n, n)
        for h in range(a):
            coefficients += g[i, h]*basis[h]
        for y in range(n):
            for z in range(n):
                power = (alpha*(degrees[y]+degrees[z]-(a-1))
                         + beta*(i-exponents[y]-exponents[z]))
                if (i, y, z) in desired and power != 0:
                    raise ValueError('target terms must have weight zero')
                if power > 0:
                    continue
                count += 1
                expected = int((i, y, z) in desired) if power == 0 else 0
                if coefficients[z, y] != expected:
                    (bad_negative if power < 0 else bad_constant).append([i, y, z])
    return {'exact': not bad_negative and not bad_constant,
            'coefficient_positions_checked': count,
            'negative_power_failures': bad_negative,
            'constant_coefficient_failures': bad_constant}


def small_control(a):
    if a == 2:
        y_indices, z_indices = [0, 2, 1], [2, 0, 1]
    elif a == 3:
        y_indices, z_indices = [0, 5, 4, 3, 2, 1], [3, 5, 6, 0, 1, 2]
    else:
        raise ValueError('only the two explicit small controls are supplied')
    n = a*(a+1)//2
    p, q = sp.zeros(n, n), sp.zeros(n, n+a-1)
    for j, index in enumerate(y_indices):
        p[index, j] = 1
    for j, index in enumerate(z_indices):
        q[j, index] = 1
    return p, q

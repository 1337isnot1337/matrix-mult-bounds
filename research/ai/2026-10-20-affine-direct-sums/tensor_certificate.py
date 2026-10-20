"""Check actual binary-form coefficients in determinant-adapted bases."""
from __future__ import annotations

from collections import defaultdict
from math import comb

import sympy as sp

from full_direct_sums import line_certificate


def adapted_basis(p, q):
    """Basis of bidegree (p,q), stored as v,w exponents with u,s implicit."""
    result = []
    for order in range(min(p, q) + 1):
        for degree in range(p + q - 2 * order + 1):
            left = min(degree, p - order)
            right = degree - left
            poly = {(left + r, right + order - r): (-1)**r * comb(order, r)
                    for r in range(order + 1)}
            result.append((order, degree, poly))
    return result


def verify_tensor(a, b, c, d, r=1, s=-1, u=0):
    """Expand every product, then check filtration and the retained tensor."""
    cert = line_certificate(a, b, c, d, r, s, u)
    x = adapted_basis(a - 1, c - 1)
    y = adapted_basis(b - 1, d - 1)
    z = adapted_basis(a + b - 2, c + d - 2)
    p, q = a + b - 2, c + d - 2
    monomials = [(v, w) for v in range(p + 1) for w in range(q + 1)]
    monomial_index = {exponents: i for i, exponents in enumerate(monomials)}
    basis_matrix = sp.Matrix([[poly.get(exponents, 0) for _, _, poly in z]
                             for exponents in monomials])
    inverse = basis_matrix.inv()
    retained_labels = {tuple(point) for point in cert["retained_labels"]}
    checked = nonzero = surviving = 0
    for i, alpha, left in x:
        for j, beta, right in y:
            poly = defaultdict(int)
            for (v, w), coefficient in left.items():
                for (vv, ww), other in right.items():
                    poly[v + vv, w + ww] += coefficient * other
            vector = sp.zeros(len(monomials), 1)
            for exponents, coefficient in poly.items():
                vector[monomial_index[exponents]] = coefficient
            coordinates = inverse * vector
            for index, (k, gamma, _) in enumerate(z):
                coefficient = coordinates[index]
                checked += 1
                if k < i + j and coefficient:
                    raise ArithmeticError("coefficient violates determinant filtration")
                if k == i + j:
                    expected = int(gamma == alpha + beta)
                    if coefficient != expected:
                        raise ArithmeticError("leading block is not ordinary convolution")
                if coefficient:
                    nonzero += 1
                    weight = cert["x_weights"][i] + cert["y_weights"][j] + cert["z_weights"][k]
                    if weight < 0:
                        raise ArithmeticError("negative supported weight")
                    if weight == 0:
                        surviving += 1
                        if ((i, j, k) not in retained_labels
                                or gamma != alpha + beta or coefficient != 1):
                            raise ArithmeticError("incorrect retained coefficient")
    expected_surviving = sum((a + c - 1 - 2 * i) * (b + d - 1 - 2 * j)
                             for i, j, k in retained_labels)
    if surviving != expected_surviving:
        raise ArithmeticError("missing retained coefficients")
    return {"source": [a, b, c, d], "line": [r, s, u],
            "coefficients_checked": checked, "nonzero_coefficients": nonzero,
            "surviving_coefficients": surviving,
            "retained_labels": cert["retained_labels"]}

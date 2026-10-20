"""Exact full Clebsch--Gordan coefficients, including off-leading blocks."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import cache
from itertools import permutations, product
from math import comb

import sympy as sp


@cache
def equivariant_basis(p, q):
    result = []
    for order in range(min(p, q) + 1):
        pp, qq = p - order, q - order
        for degree in range(pp + qq + 1):
            poly = defaultdict(Fraction)
            for left in range(max(0, degree - qq), min(degree, pp) + 1):
                right = degree - left
                scale = Fraction(comb(pp, left) * comb(qq, right), comb(pp + qq, degree))
                for r in range(order + 1):
                    poly[left + r, right + order - r] += scale * (-1)**r * comb(order, r)
            result.append((order, degree, dict(poly)))
    return result


@cache
def output_transform(p, q, total_degree):
    monomials = [(v, total_degree - v)
                 for v in range(max(0, total_degree - q), min(p, total_degree) + 1)]
    basis = [(order, degree, poly) for order, degree, poly in equivariant_basis(p, q)
             if order + degree == total_degree]
    matrix = sp.Matrix([[poly.get(monomial, 0) for _, _, poly in basis] for monomial in monomials])
    inverse = matrix.inv()
    return monomials, [(order, degree) for order, degree, _ in basis], inverse


def full_blocks(a, b, c, d):
    if any(not isinstance(n, int) or n < 1 for n in (a, b, c, d)):
        raise ValueError("positive integer dimensions required")
    blocks = defaultdict(list)
    p, q = a + b - 2, c + d - 2
    for i, alpha, left in equivariant_basis(a - 1, c - 1):
        for j, beta, right in equivariant_basis(b - 1, d - 1):
            poly = defaultdict(Fraction)
            for (v, w), value in left.items():
                for (vv, ww), other in right.items():
                    poly[v + vv, w + ww] += value * other
            monomials, labels, inverse = output_transform(p, q, i + alpha + j + beta)
            values = inverse * sp.Matrix([poly[monomial] for monomial in monomials])
            for (k, gamma), value in zip(labels, values):
                if value:
                    if k < i + j:
                        raise ArithmeticError("filtration violation")
                    blocks[i, j, k].append((alpha, beta, gamma, Fraction(value)))
    result = []
    for (i, j, k), terms in sorted(blocks.items()):
        dims = (a + c - 1 - 2 * i, b + d - 1 - 2 * j,
                a + b + c + d - 3 - 2 * k)
        result.append({"labels": (i, j, k), "dims": dims, "terms": terms})
    return result


def convolution_isomorphism(block):
    """Exhibit an axis/reversal/diagonal-factor equivalence, or return None."""
    dims = block["dims"]
    for axes in permutations(range(3)):
        aa, bb, cc = [dims[axis] for axis in axes]
        if cc != aa + bb - 1:
            continue
        expected = {(i, j, i + j) for i in range(aa) for j in range(bb)}
        for reverse in product((False, True), repeat=3):
            transformed = {}
            for *coordinates, coefficient in block["terms"]:
                point = tuple(dims[axis] - 1 - coordinates[axis] if reverse[t]
                              else coordinates[axis] for t, axis in enumerate(axes))
                transformed[point] = coefficient
            if set(transformed) != expected:
                continue
            values = {(i, j): coefficient for (i, j, k), coefficient in transformed.items()}
            if aa == 1 or bb == 1:
                factors_z = [values.get((0, k), values.get((k, 0))) for k in range(cc)]
                factors_x, factors_y = [Fraction(1)] * aa, [Fraction(1)] * bb
            else:
                factors_z = [values[0, 0], Fraction(1)]
                for k in range(2, cc):
                    i = min(aa - 1, k - 1)
                    j = k - i
                    factors_z.append(values[i, j] * factors_z[i] * factors_z[j]
                                     / (values[i, 0] * values[0, j]))
                factors_x = [values[i, 0] / factors_z[i] for i in range(aa)]
                factors_y = [values[0, j] / factors_z[j] for j in range(bb)]
            if any(values[i, j] != factors_x[i] * factors_y[j] * factors_z[i + j]
                   for i in range(aa) for j in range(bb)):
                continue
            return {"convolution_lengths": [aa, bb], "axes": list(axes),
                    "reversals": list(reverse),
                    "x_factors": list(map(str, factors_x)),
                    "y_factors": list(map(str, factors_y)),
                    "z_factors": list(map(str, factors_z))}
    return None


def dot_slice_bound(block):
    dims = block["dims"]
    best = 1
    for axis in range(3):
        other = [i for i in range(3) if i != axis]
        for fixed in range(dims[axis]):
            matrix = sp.zeros(dims[other[0]], dims[other[1]])
            for *coordinates, coefficient in block["terms"]:
                if coordinates[axis] == fixed:
                    matrix[coordinates[other[0]], coordinates[other[1]]] = coefficient
            best = max(best, int(matrix.rank()))
    return best


def tight_uniform_certificate(block):
    """Certify tight support and exact simultaneous uniform marginals.

    For scalar coefficients the cited tight-support asymptotic-subrank theorem
    then supplies the lower bound min(dimensions), valid for every character.
    """
    a, b, c = block["dims"]
    constants = {i + j - k for i, j, k, value in block["terms"]}
    if len(constants) != 1:
        raise ArithmeticError("support is not tight in the stated coordinates")
    masses = [value**2 * Fraction(comb(a - 1, i) * comb(b - 1, j), comb(c - 1, k))
              for i, j, k, value in block["terms"]]
    total = sum(masses, Fraction())
    if total <= 0:
        raise ArithmeticError("empty probability certificate")
    marginals = []
    for axis, dimension in enumerate((a, b, c)):
        marginal = [sum((mass for term, mass in zip(block["terms"], masses)
                         if term[axis] == coordinate), Fraction()) / total
                    for coordinate in range(dimension)]
        if any(value != Fraction(1, dimension) for value in marginal):
            raise ArithmeticError("nonuniform marginal")
        marginals.append(list(map(str, marginal)))
    return {"tight_weights": ["i", "j", "-k"], "constant": constants.pop(),
            "probabilities": [str(mass / total) for mass in masses],
            "marginals": marginals, "asymptotic_subrank": min(a, b, c),
            "theorem": "Strassen tight scalar support formula; CVZ arXiv:1609.07476v2 Theorem 1.1.31"}


if __name__ == "__main__":
    for dims in [(2, 2, 2, 2), (3, 3, 3, 3), (2, 3, 3, 2)]:
        print("SOURCE", dims)
        for block in full_blocks(*dims):
            witness = convolution_isomorphism(block)
            print(block["labels"], block["dims"],
                  witness["convolution_lengths"] if witness else "unknown")

#!/usr/bin/env python3
"""Exact controls for quantum-character convolution profiles.

No arbitrary-character claim is checked or made by this program.
"""

from fractions import Fraction as F
from math import comb


def uniform_marginals(a, b):
    weights = {
        (i, j, i + j): F(comb(a - 1, i) * comb(b - 1, j),
                         comb(a + b - 2, i + j))
        for i in range(a) for j in range(b)
    }
    total = sum(weights.values(), F(0))
    assert total == a + b - 1
    for leg, size in enumerate((a, b, a + b - 1)):
        marginal = [sum((w for term, w in weights.items() if term[leg] == k), F(0))
                    for k in range(size)]
        assert marginal == [F(total, size)] * size
    return len(weights)


def falling(a, n):
    out = F(1)
    for i in range(n):
        out *= a - i
    return out


def rising(a, n):
    out = F(1)
    for i in range(n):
        out *= a + i
    return out


def fifth_over_value_direct(beta, s):
    return sum((F(comb(5, k)) * falling(beta, k) * falling(1 - beta, 5 - k)
                / (s**k * (1 + s)**(5 - k)) for k in range(6)), F(0))


def fifth_over_value_positive(beta, s):
    return beta * (1 - beta) * sum((
        F(comb(3, k)) * rising(2 - beta, k) * rising(1 + beta, 3 - k)
        / (s**(2 + k) * (1 + s)**(5 - k)) for k in range(4)), F(0))


def integer_root(n, degree):
    assert isinstance(n, int) and n >= 0 and degree > 0
    lo, hi = 0, 1 << ((n.bit_length() + degree - 1) // degree)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**degree <= n:
            lo = mid
        else:
            hi = mid
    if hi**degree <= n:
        lo = hi
    assert lo**degree <= n < (lo + 1)**degree
    return lo


def eighth_root_interval(x, denominator=10**18):
    k = integer_root(x.numerator * denominator**8 // x.denominator, 8)
    lo, hi = F(k, denominator), F(k + 1, denominator)
    assert lo**8 <= x < hi**8
    return lo, hi


def stencil_interval(numerator, start=F(4, 5), step=F(1, 20), offset=F(1)):
    lo = hi = F(0)
    for k in range(6):
        s = start + k * step
        a, b = eighth_root_interval(s**numerator * (offset + s)**(8 - numerator))
        c = (-1)**(5 - k) * comb(5, k)
        if c >= 0:
            lo += c * a
            hi += c * b
        else:
            lo += c * b
            hi += c * a
    return lo, hi


def main():
    terms = sum(uniform_marginals(a, b) for a in range(1, 17) for b in range(1, 17))
    print(f"Uniform orbit marginals: 256 sources, {terms} rational coefficient masses PASS")
    derivative_checks = 0
    for b in range(1, 8):
        beta = F(b, 8)
        for s in (F(1, 10), F(1, 2), F(4, 5), F(1), F(2), F(10)):
            direct = fifth_over_value_direct(beta, s)
            positive = fifth_over_value_positive(beta, s)
            assert direct == positive > 0
            derivative_checks += 1
    for beta in (F(0), F(1)):
        assert fifth_over_value_direct(beta, F(1)) == 0
        assert fifth_over_value_positive(beta, F(1)) == 0
    print(f"Independent fifth-derivative formulas: {derivative_checks} interior and 2 endpoint cases PASS")
    for b in range(1, 8):
        lo, hi = stencil_interval(b)
        assert 0 < lo <= hi
        print(f"beta={b}/8: exact stencil in [{lo}, {hi}] PASS")
    for n in (1, 2):
        for b in range(1, 8):
            lo, hi = stencil_interval(b, F(16*n), F(n), F(20*n-1))
            assert 0 < lo <= hi
    print("Finite matched-stencil signs at n=1,2: 14 exact intervals PASS")
    print("These controls do not establish a higher-difference inequality for arbitrary characters.")


if __name__ == "__main__":
    main()

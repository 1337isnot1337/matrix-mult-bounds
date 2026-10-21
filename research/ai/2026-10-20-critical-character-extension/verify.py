#!/usr/bin/env python3
"""Exact algebra and radical interval controls for the accompanying note.

Python standard library only. This checks finite algebraic statements, not
the universal tensor premises or the full analytic arguments.
"""

from fractions import Fraction as F
from math import comb


def padd(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pscale(a, c):
    return [v * c for v in a]


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += v * w
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def falling(x, n):
    out = F(1)
    for k in range(n):
        out *= x - k
    return out


def integer_cube_root(n):
    """Return floor(cuberoot(n)) for a nonnegative integer, exactly."""
    assert n >= 0
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    if hi**3 <= n:
        lo = hi
    assert lo**3 <= n < (lo + 1)**3
    return lo


def cube_root_interval(x, denominator=10**15):
    assert x >= 0
    scaled_floor = x.numerator * denominator**3 // x.denominator
    a = integer_cube_root(scaled_floor)
    lo, hi = F(a, denominator), F(a + 1, denominator)
    assert lo**3 <= x < hi**3
    return lo, hi


def profile_interval(s):
    assert s > 0
    if s >= 1:
        v = s + F(1, 2)
        return v, v
    lo, hi = cube_root_interval(s)
    factor = 1 + s / 2
    return lo * factor, hi * factor


def fifth_difference_interval():
    lo = hi = F(0)
    for k in range(6):
        coefficient = (-1) ** (5 - k) * comb(5, k)
        a, b = profile_interval(F(4, 5) + F(k, 20))
        if coefficient >= 0:
            lo += coefficient * a
            hi += coefficient * b
        else:
            lo += coefficient * b
            hi += coefficient * a
    return lo, hi


def main():
    u = [F(0), F(1)]
    z = [F(1), F(-2)]
    r = pmul(u, z)
    e2 = padd(pmul(u, u), pscale(pmul(u, pmul(z, z)), F(2)))
    j = padd(padd(e2, pscale(r, F(-5, 4))), pscale(pmul(r, r), F(-2)))
    factor = pscale(
        pmul(pmul(u, pmul([F(-1), F(4)], [F(-1), F(4)])),
             [F(3), F(-2)]), F(1, 4)
    )
    assert j == factor
    print("Exact two-equal-variable factorization: PASS")

    left_derivatives = [falling(F(1, 3), n) + F(1, 2) * falling(F(4, 3), n)
                        for n in range(5)]
    right_derivatives = [F(3, 2), F(1), F(0), F(0), F(0)]
    assert left_derivatives[:3] == right_derivatives[:3]
    assert left_derivatives[3:] == [F(2, 9), F(-20, 27)]
    alpha = F(3, 4)
    normalized_right_third = alpha * (alpha - 1) * (alpha - 2) * F(2, 3)**3
    normalized_left_third = normalized_right_third + alpha * F(2, 9) / F(3, 2)
    assert normalized_right_third == F(5, 72)
    assert normalized_left_third == F(13, 72)
    print("Critical one-sided derivatives through order four: PASS")

    for point in [(F(3, 4),) * 3, (F(0), F(1), F(1))]:
        deficit = F(9, 4) - sum(point)
        squared_distance = sum((p - F(3, 4))**2 for p in point)
        assert squared_distance == F(11, 4) * deficit
    assert F(4, 125)**2 > F(1, 1000)
    assert F(3, 4) - F(1, 1000) - F(4, 125) == F(717, 1000)
    assert F(3, 4) - F(1, 1000) + F(4, 125) == F(781, 1000)
    assert F(1, 100)**2 == F(1, 10000)
    assert F(3, 4) - F(1, 10000) - F(1, 100) == F(7399, 10000)
    assert F(3, 4) - F(1, 10000) + F(1, 100) == F(7599, 10000)
    print("Sharp constant equality examples and rational parameter boxes: PASS")

    lo, hi = fifth_difference_interval()
    outer_lo, outer_hi = F(-306600, 10**11), F(-306599, 10**11)
    assert outer_lo < lo <= hi < outer_hi < 0
    print("Fifth difference exact rational enclosure: PASS")
    print(f"  lower = {lo}")
    print(f"  upper = {hi}")
    print(f"  approximate interval = [{float(lo):.18g}, {float(hi):.18g}]")
    print("No smaller matrix multiplication exponent is established by these checks.")


if __name__ == "__main__":
    main()

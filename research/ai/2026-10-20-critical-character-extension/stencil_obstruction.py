#!/usr/bin/env python3
"""Exact controls for the all-scale matched-stencil obstruction.

The shared-input Koszul rank formula is imported from
../2026-10-20-koszul/research_note.md, Section 3. These calculations verify
its specialization; they are not an independent proof of that formula.
"""

from fractions import Fraction
from math import comb


POSITIVE = ((5, 17), (10, 19), (1, 21))
NEGATIVE = ((1, 16), (10, 18), (5, 20))
SMALL_POLYNOMIAL_CERTIFICATES = (
    (171, -99),
    (263148689, -24792051),
    (245470502231930, -3038048120670),
    (162696452587579494790, -283929472530121710),
    (90326924459049957577553040, -22965165863895412216160),
    (45244265658998166692802035517275, -1700055817867419873663046725),
    (21223899599229850460334061619210389340,
     -118625644051316468742842160169860),
)


def binomial(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def koszul_rank(a, b, p):
    assert 0 <= p < a
    return b * comb(a, p) - binomial(a - 1, p - 1) * max(b - a + p, 0)


def rank_sum(blocks, n, p):
    return sum(multiplicity * koszul_rank(20 * n, b * n, p)
               for multiplicity, b in blocks)


def dimensions(blocks, n):
    a = 20 * n
    return (a,
            sum(multiplicity * b * n for multiplicity, b in blocks),
            sum(multiplicity * (a + b * n - 1)
                for multiplicity, b in blocks))


def hinge_sum(n, p):
    return sum((-1) ** (5 - k) * comb(5, k) * max(p + (k - 4) * n, 0)
               for k in range(6))


def piecewise_hinge(n, p):
    if p <= n:
        return n - 4 * p
    if p <= 2 * n:
        return 6 * p - 9 * n
    if p <= 3 * n:
        return 11 * n - 4 * p
    if p <= 4 * n:
        return p - 4 * n
    return 0


def scaled_rank_polynomial(n, denominator):
    """Return denominator**(4*n-1) * D_n(1/denominator), as an integer."""
    return sum((rank_sum(POSITIVE, n, p) - rank_sum(NEGATIVE, n, p))
               * denominator**(4*n-1-p) for p in range(1, 4*n))


def main():
    checks = 0
    for n in range(1, 33):
        a = 20 * n
        expected_dimensions = (20 * n, 296 * n, 616 * n - 16)
        assert dimensions(POSITIVE, n) == expected_dimensions
        assert dimensions(NEGATIVE, n) == expected_dimensions
        for p in range(a):
            actual = rank_sum(POSITIVE, n, p) - rank_sum(NEGATIVE, n, p)
            hinge = hinge_sum(n, p)
            assert hinge == piecewise_hinge(n, p), (n, p)
            assert actual == -binomial(a - 1, p - 1) * hinge, (n, p)
            checks += 1

        first = rank_sum(POSITIVE, n, n) - rank_sum(NEGATIVE, n, n)
        second = rank_sum(POSITIVE, n, 2 * n) - rank_sum(NEGATIVE, n, 2 * n)
        assert first == 3 * n * comb(20 * n - 1, n - 1) > 0
        assert second == -3 * n * comb(20 * n - 1, 2 * n - 1) < 0

    for n, pair in enumerate(SMALL_POLYNOMIAL_CERTIFICATES, start=1):
        actual = tuple(scaled_rank_polynomial(n, d) for d in (19, 9))
        assert actual == pair
        assert pair[0] > 0 > pair[1]

    # Squared positivity margins in the moment bounds (10) and (11).
    # The increments of both quadratics are positive above their thresholds.
    first_threshold = Fraction(5**2) - 4 * (Fraction(19*5, 20) + Fraction(171, 200))
    second_threshold = Fraction(8**2) - 4 * (Fraction(9*8, 5) + Fraction(18, 25))
    assert first_threshold == Fraction(129, 50) > 0
    assert second_threshold == Fraction(88, 25) > 0
    assert 2*5 + 1 - Fraction(19, 5) > 0
    assert 2*8 + 1 - Fraction(36, 5) > 0

    print("Matched dimensions at all 32 scales: PASS")
    print(f"All-degree rank differences and hinge pieces: {checks} cases PASS")
    print("Both opposite-sign witnesses at all 32 scales: PASS")
    print("All-scale replication proof: 14 integer certificates and both moment bounds PASS")
    print("No universal profile inequality or exponent improvement is asserted.")


if __name__ == "__main__":
    main()

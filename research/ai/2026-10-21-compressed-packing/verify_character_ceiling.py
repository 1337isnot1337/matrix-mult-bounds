#!/usr/bin/env python3
"""Exact controls for the character ceiling of the compressed alternative."""

import argparse
from collections import Counter
from fractions import Fraction
import json
from math import comb, isqrt
from pathlib import Path


def matrix_product(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def polynomial_from_roots(roots):
    result = [1]
    for root in roots:
        nxt = [0] * (len(result) + 1)
        for i, c in enumerate(result):
            nxt[i] -= root * c
            nxt[i + 1] += c
        result = nxt
    return result


def check_jordan(max_r=12):
    checks = 0
    for r in range(1, max_r + 1):
        reconstructed = Counter()
        expected = Counter()
        for i in range(1, r + 1):
            nilpotent = [[int(b == a + 1) for a in range(i)]
                         for b in range(i)]
            power = [[int(a == b) for a in range(i)] for b in range(i)]
            for x in range(r):
                for a in range(i):
                    for b in range(i):
                        if power[b][a]:
                            reconstructed[x, i, a, i - 1 - b] += power[b][a]
                power = matrix_product(nilpotent, power)
            for x in range(i):
                for a in range(i - x):
                    expected[x, i, a, i - 1 - x - a] += 1

            # f_i(t,e)=sum_b q_b e^(i-b) t^b. Evaluation at t=e*j
            # makes the last-column eigenvector identity e^i*f_i(j,1)=0.
            q = polynomial_from_roots(range(1, i + 1))
            assert q[-1] == 1
            for j in range(1, i + 1):
                assert sum(c * j**b for b, c in enumerate(q)) == 0
                checks += 1
            # The global Vandermonde determinant is nonzero; evaluation
            # coordinates with label j occur in precisely r-j+1 blocks.
        assert reconstructed == expected
        determinant = 1
        for j in range(1, r + 1):
            for k in range(j + 1, r + 1):
                determinant *= k - j
        assert determinant > 0
        assert [sum(i >= j for i in range(1, r + 1))
                for j in range(1, r + 1)] == list(range(r, 0, -1))
    return {"max_r": max_r, "integer_root_identities": checks,
            "nilpotent_tensors_and_multiplicities": True}


def check_error_reindexing(m):
    s = m // 2
    upper = Counter()
    lower = Counter()
    for i in range(1, s):
        for a in range(i + 1):
            for c in range(i + 1):
                if a + c <= i - 1:
                    q = m - i + a + c
                    upper[m - 1 - q, i, a, c] += 1
            for c in range(i):
                if a + c >= i + 1:
                    q = a + c - i - 1
                    lower[q, i - 1, i - a, i - 1 - c] += 1
    expected_upper = Counter()
    expected_lower = Counter()
    for size, target in [(s - 1, expected_upper), (s - 2, expected_lower)]:
        for i in range(1, size + 1):
            for x in range(i):
                for a in range(i - x):
                    target[x, i, a, i - 1 - x - a] += 1
    assert upper == expected_upper
    assert lower == expected_lower
    return len(upper) + len(lower)


def check_central_slices(m):
    s = m // 2
    ranks = []
    for q in sorted({s - 2, s - 1, s} & set(range(m))):
        rows, columns = set(), set()
        pairs = []
        for a in range(m):
            for b in range(m - a):
                for c in range(m - a - b):
                    d = m - 1 - a - b - c
                    if a + c == q:
                        pairs.append(((a, b), (c, d)))
                        rows.add((a, b))
                        columns.add((c, d))
        assert len(rows) == len(columns) == len(pairs)
        assert len(pairs) == (q + 1) * (m - q)
        ranks.append(len(pairs))
    expected = [s*s+s-2, s*s+s, s*s+s]
    if s == 1:
        expected = expected[1:]
    assert ranks == expected
    return ranks


def fourth_root_interval(value, scale=10**12):
    """A rigorous rational interval, using only integer arithmetic."""
    value = Fraction(value)
    n = value.numerator * scale**4 // value.denominator
    root = isqrt(isqrt(n))
    low = Fraction(root, scale)
    high = Fraction(root + 1, scale)
    assert low**4 <= value < high**4
    return low, high


def check_finite_comparison():
    h = [Fraction(0), Fraction(1)]
    for n in range(1, 308):
        h.append(h[-1] * Fraction(3*n+1, 3*n))
    confirmed = []
    first_interval_success = None
    for s in range(2, 154):
        upper = Fraction(0)
        for j in list(range(1, s)) + list(range(1, s-1)):
            upper += fourth_root_interval(j**3)[1]
        for rank in [s*s+s-2, s*s+s, s*s+s]:
            upper += fourth_root_interval(rank**3)[1]
        m = 2*s
        n = s*(2*s+1)
        source_p = h[m] * (n + Fraction(m-1, 2))
        lower = fourth_root_interval(source_p**3)[0]
        if upper < lower:
            if first_interval_success is None:
                first_interval_success = s
            confirmed.append(s)
        if s >= 60:
            assert upper < lower
    assert confirmed == list(range(60, 154))
    return {"certified_s_interval": [60, 153],
            "certified_cases": len(confirmed),
            "first_success_of_this_upper_estimate": first_interval_success,
            "rational_interval_scale": 10**12}


def check_polynomial_threshold():
    base = 154
    coefficients = []
    for k in range(5):
        c = 16 * comb(4, k) * base**(4-k)
        if k <= 3:
            c -= 2401 * comb(3, k) * (base+1)**(3-k)
        coefficients.append(c)
    assert coefficients == [58154621, 60692821, 1160271, 7455, 16]
    assert min(coefficients) > 0
    return {"all_s_at_least": base,
            "positive_shifted_polynomial_coefficients": coefficients,
            "all_even_m_comparison_from": 120,
            "asymptotic_unpowered_ratio_upper": "4/7"}


def report():
    cases = []
    for m in range(2, 82, 2):
        cases.append({"m": m, "error_terms_checked": check_error_reindexing(m),
                      "central_slice_ranks": check_central_slices(m)})
    return {"status": "exact character upper bound for the specified alternative tensor",
            "scope": "endpoint p_X=p_Y=p_Z=3/4 over characteristic zero; no exponent improvement",
            "jordan_checks": check_jordan(),
            "error_and_slice_cases": cases,
            "finite_comparison": check_finite_comparison(),
            "all_size_threshold": check_polynomial_threshold()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({"cases": len(data["error_and_slice_cases"]),
                      "finite_comparison": data["finite_comparison"],
                      "all_size_threshold": data["all_size_threshold"]}, sort_keys=True))


if __name__ == "__main__":
    main()

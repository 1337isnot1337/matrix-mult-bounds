"""All-size upper certificate for the unequal determinant-filtration score.

This bounds an analytic score, not the matrix multiplication exponent.
All acceptance arithmetic is rational or integer.  See research_note.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
import json
from math import comb, gcd, isqrt
from pathlib import Path


TAIL_MINIMUM = 11
TAIL_BOUND = Q(97, 100)
ROOT_SCALE = 10**15


@lru_cache(None)
def h(n: int) -> Q:
    if n < 1:
        raise ValueError("positive length required")
    result = Q(1)
    for k in range(1, n):
        result *= Q(3*k + 1, 3*k)
    return result


def profile(a: int, b: int) -> Q:
    small, large = sorted((a, b))
    return h(small) * Q(2*large + small - 1, 2)


def sqrt_interval(value: Q, scale: int = ROOT_SCALE) -> tuple[Q, Q]:
    if value < 0 or scale < 1:
        raise ValueError("nonnegative radicand and positive scale required")
    numerator = isqrt(value.numerator * scale**2 // value.denominator)
    lo = Q(numerator, scale)
    hi = lo if lo*lo == value else Q(numerator + 1, scale)
    if not lo*lo <= value <= hi*hi:
        raise ArithmeticError("invalid square-root enclosure")
    return lo, hi


@lru_cache(None)
def weight_interval(a: int, c: int) -> tuple[Q, Q]:
    endpoints = [sqrt_interval(h(a+c-1-2*i)**3)
                 for i in range(min(a, c))]
    return tuple(sum((row[j] for row in endpoints), Q(0))
                 for j in range(2))


def ratio_cube_interval(a: int, b: int, c: int, d: int) -> tuple[Q, Q]:
    """Enclose (U / (P_*(a,b) P_*(c,d)))^3, not the exact entropy optimum."""
    A, B = a+c-1, b+d-1
    R = profile(A, B) / (h(A)*h(B))
    source = profile(a, b)*profile(c, d)
    w1, w2 = weight_interval(a, c), weight_interval(b, d)
    return tuple(R**3 * (w1[j]*w2[j])**2 / source**3 for j in range(2))


# Polynomials have tuple exponent keys and rational coefficients.  Every
# polynomial below has degree at most eight; all constructions are explicit.
def constant(value: Q | int, dimension: int) -> dict:
    return {(0,)*dimension: Q(value)} if value else {}


def variable(index: int, dimension: int) -> dict:
    key = [0]*dimension
    key[index] = 1
    return {tuple(key): Q(1)}


def add(*polynomials: dict) -> dict:
    result: dict = {}
    for polynomial in polynomials:
        for key, value in polynomial.items():
            result[key] = result.get(key, Q(0)) + value
    return {key: value for key, value in result.items() if value}


def scale(polynomial: dict, factor: Q | int) -> dict:
    return {key: value*factor for key, value in polynomial.items()
            if value*factor}


def multiply(*polynomials: dict) -> dict:
    if not polynomials:
        raise ValueError("at least one polynomial required")
    dimension = len(next(iter(polynomials[0])))
    result = constant(1, dimension)
    for polynomial in polynomials:
        out: dict = {}
        for first, first_value in result.items():
            for second, second_value in polynomial.items():
                key = tuple(x+y for x, y in zip(first, second))
                out[key] = out.get(key, Q(0)) + first_value*second_value
        result = {key: value for key, value in out.items() if value}
    return result


def power(polynomial: dict, exponent: int) -> dict:
    if exponent < 1:
        raise ValueError("positive exponent required")
    return multiply(*([polynomial]*exponent))


def shift(polynomial: dict, index: int, amount: int) -> dict:
    """Substitute x_index -> x_index + amount using the binomial theorem."""
    result: dict = {}
    for key, value in polynomial.items():
        for exponent in range(key[index]+1):
            shifted = list(key)
            shifted[index] = exponent
            shifted = tuple(shifted)
            result[shifted] = result.get(shifted, Q(0)) + (
                value*comb(key[index], exponent)*amount**(key[index]-exponent))
    return {key: value for key, value in result.items() if value}


def evaluate(polynomial: dict, point: tuple[int, ...]) -> Q:
    return sum((value * product_of(x**n for x, n in zip(point, key))
                for key, value in polynomial.items()), Q(0))


def product_of(values) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def cones() -> list[tuple[str, str]]:
    result = []
    for order in permutations("bcd"):
        label = "".join(order)
        for side in (("lo", "hi") if order[-1] == "c" else ("auto",)):
            result.append((label, side))
    return result


def cone_sizes(a, gaps, order: str, side: str):
    """Works for both exact numbers and polynomial dictionaries."""
    is_poly = isinstance(a, dict)
    plus = add if is_poly else lambda *items: sum(items)
    x, y, z = gaps
    if side == "lo":
        x = plus(x, z)
    elif side == "hi":
        z = plus(x, z)
    elif side != "auto":
        raise ValueError("unknown cone side")
    sizes = {"a": a}
    previous = a
    for label, gap in zip(order, (x, y, z)):
        previous = plus(previous, gap)
        sizes[label] = previous
    return sizes


def inequality_polynomial(minimum: int, order: str, side: str,
                          all_large: bool) -> dict:
    """Cross-multiplied Jensen/recurrence upper certificate, equation (8)."""
    dimension = 4 if all_large else 3
    one = constant(1, dimension)
    a = constant(minimum, dimension)
    offset = 0
    if all_large:
        a = add(a, variable(0, dimension))
        offset = 1
    gaps = [variable(offset+i, dimension) for i in range(3)]
    sizes = cone_sizes(a, gaps, order, side)
    b, c, d = (sizes[label] for label in "bcd")
    ranks = {"a": 0, **{label: i+1 for i, label in enumerate(order)}}
    lower = lambda labels: min(labels, key=lambda label: ranks[label])
    upper = lambda labels: max(labels, key=lambda label: ranks[label])
    m = sizes[lower("bd")]
    ell = sizes[lower("cd")]
    L = sizes[upper("cd")]
    N = sizes[order[-1]]
    e = sizes[lower(("c", upper("bd")))]
    A0, B0 = add(a, c, scale(one, -1)), add(b, d, scale(one, -1))
    u, v = (B0, A0) if side == "hi" else (A0, B0)
    X = add(scale(b, 2), a, scale(one, -1))
    Y = add(scale(L, 2), ell, scale(one, -1))
    V = add(scale(v, 2), u, scale(one, -1))
    denominator = multiply(v, add(scale(ell, 3), scale(one, -1)),
                           power(X, 3), power(Y, 3))
    if all_large:
        left = scale(denominator, TAIL_BOUND**3*h(minimum)**3/minimum)
        numerator_a = a
    else:
        left = scale(denominator, TAIL_BOUND**3*h(minimum)**3)
        numerator_a = power(a, 2)
    right = scale(multiply(numerator_a, power(m, 2), N,
                           add(scale(e, 3), scale(one, -1)), power(V, 3)), 8)
    return add(left, scale(right, -1))


def direct_inequality_value(sizes: dict[str, int], minimum: int,
                            all_large: bool) -> Q:
    """Independent scalar form of equation (8), used to check the expansion."""
    a, b, c, d = (sizes[label] for label in "abcd")
    m, M = sorted((b, d))
    ell, L = sorted((c, d))
    e, N = sorted((c, M))
    u, v = sorted((a+c-1, b+d-1))
    X, Y, V = 2*b+a-1, 2*L+ell-1, 2*v+u-1
    denominator = v*(3*ell-1)*X**3*Y**3
    if all_large:
        left = TAIL_BOUND**3*h(minimum)**3/minimum*denominator
        numerator_a = a
    else:
        left = TAIL_BOUND**3*h(minimum)**3*denominator
        numerator_a = a*a
    return left - 8*numerator_a*m*m*N*(3*e-1)*V**3


def coefficient_certificate(polynomial: dict) -> dict:
    if not polynomial or any(value < 0 for value in polynomial.values()):
        raise ArithmeticError("polynomial has a negative coefficient")
    denominator = 1
    for value in polynomial.values():
        denominator = denominator*value.denominator // gcd(denominator, value.denominator)
    rows = [[list(key), int(value*denominator)]
            for key, value in sorted(polynomial.items())]
    divisor = 0
    for _, value in rows:
        divisor = gcd(divisor, value)
    normalized = [[key, value//divisor] for key, value in rows]
    payload = json.dumps(normalized, separators=(",", ":")).encode()
    return {"monomials": len(rows),
            "total_degree": max(sum(key) for key in polynomial),
            "minimum_normalized_coefficient": min(value for _, value in normalized),
            "normalized_coefficients_sha256": sha256(payload).hexdigest()}


def report() -> dict:
    tails, small_tails = [], []
    residuals = set()
    for order, side in cones():
        polynomial = inequality_polynomial(TAIL_MINIMUM, order, side, True)
        tails.append({"order": order, "side": side,
                      **coefficient_certificate(polynomial)})
    for minimum in range(2, TAIL_MINIMUM):
        for order, side in cones():
            polynomial = inequality_polynomial(minimum, order, side, False)
            thresholds = []
            receipts = []
            for index in range(3):
                for threshold in range(1, 17):
                    candidate = shift(polynomial, index, threshold)
                    if all(value >= 0 for value in candidate.values()):
                        thresholds.append(threshold)
                        receipts.append(coefficient_certificate(candidate))
                        break
                else:
                    raise ArithmeticError("the small-minimum tail is not certified")
            small_tails.append({"minimum": minimum, "order": order, "side": side,
                                "gap_thresholds": thresholds, "certificates": receipts})
            for gaps in product(*(range(threshold) for threshold in thresholds)):
                sizes = cone_sizes(minimum, gaps, order, side)
                residuals.add(tuple(sizes[label] for label in "abcd"))
    small_checks = []
    exceptional = (2, 2, 2, 2)
    for source in sorted(residuals):
        lo, hi = ratio_cube_interval(*source)
        if source != exceptional and hi >= TAIL_BOUND**3:
            raise ArithmeticError(f"finite residual failed: {source}")
        small_checks.append({"source": list(source), "ratio_cube_lower": str(lo),
                             "ratio_cube_upper": str(hi),
                             "exceptional": source == exceptional})
    if exceptional not in residuals:
        raise ArithmeticError("the sharp exceptional case was omitted")
    lo, hi = ratio_cube_interval(*exceptional)
    sharp_lower, sharp_upper = Q(974772906, 10**9), Q(974772907, 10**9)
    if not TAIL_BOUND**3 < sharp_lower**3 < lo <= hi < sharp_upper**3 < Q(39,40)**3:
        raise ArithmeticError("sharp constant interval did not certify")
    return {
        "claim": "AI-UNEQUAL-ENTROPY-001",
        "statement": "For all a,b,c,d>=2, U/(P_*(a,b)P_*(c,d)) <= "
                     "(81/350)*(1+14*sqrt(14)/27)^(4/3), attained only at (2,2,2,2).",
        "score_consequence": "The defined optimistic entropy score is at most this "
                             "constant times the matching source profile.",
        "nonexceptional_bound": str(TAIL_BOUND),
        "sharp_constant_interval": [str(sharp_lower), str(sharp_upper)],
        "tail_minimum": TAIL_MINIMUM,
        "all_large_cones": tails,
        "small_minimum_tails": small_tails,
        "finite_residual_count": len(residuals),
        "finite_residuals": small_checks,
        "scope": "All-size analytic upper certificate; no weighted tensor extraction "
                 "theorem, no new tensor degeneration, no smaller omega.",
        "proof_status": "AI-derived written proof with exact arithmetic certificates; "
                        "not independently reviewed or formally verified",
        "improves_omega": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in
                     ("statement", "tail_minimum", "finite_residual_count",
                      "sharp_constant_interval", "improves_omega")}, indent=2))


if __name__ == "__main__":
    main()

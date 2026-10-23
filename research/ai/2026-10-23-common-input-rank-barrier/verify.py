"""Exact finite controls for the common-input rank barrier.

Only Python's standard library is required. Modular full rank of an integer
matrix certifies full rank over Q and C. Finite controls do not prove the
imported all-size determinant theorem or construct a tensor degeneration.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement, product
import json
from math import comb
from pathlib import Path


PRIME = 65521
Radical = dict[int, Fraction]


def positive_int(value: int, name: str) -> int:
    if type(value) is not int or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def degree(value: int) -> int:
    if type(value) is not int or value < 0:
        raise ValueError("degree must be a nonnegative integer")
    return value


def symmetric_dimension(a: int, q: int) -> int:
    positive_int(a, "a")
    degree(q)
    return comb(a + q - 1, q)


@lru_cache(None)
def monomials(a: int, q: int) -> tuple[tuple[int, ...], ...]:
    positive_int(a, "a")
    degree(q)
    if a == 1:
        return ((q,),)
    return tuple((i,) + rest for i in range(q + 1)
                 for rest in monomials(a - 1, q - i))


def full_matrix(a: int, b: int, q: int, swapped: bool = False) -> list[list[int]]:
    """Build Phi for Full; swapped=True builds Psi from literal coefficients."""
    positive_int(a, "a")
    positive_int(b, "b")
    degree(q)
    if type(swapped) is not bool:
        raise ValueError("swapped must be a bool")
    lower, upper = monomials(a, q), monomials(a, q + 1)
    lookup = {m: i for i, m in enumerate(upper)}
    y, z = (a + b - 1, b) if swapped else (b, a + b - 1)
    matrix = [[0] * (z * len(lower)) for _ in range(y * len(upper))]
    for i in range(a):
        for j in range(b):
            row_leg, col_leg = (i + j, j) if swapped else (j, i + j)
            for k, monomial in enumerate(lower):
                image = list(monomial)
                image[i] += 1
                row = row_leg * len(upper) + lookup[tuple(image)]
                col = col_leg * len(lower) + k
                matrix[row][col] += 1
    return matrix


def modular_rank(matrix: list[list[int]]) -> int:
    """Exact rank modulo the fixed prime; used only as a complex-rank lower bound."""
    if not matrix or not matrix[0]:
        return 0
    rows = [[value % PRIME for value in row] for row in matrix]
    height, width = len(rows), len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("ragged matrix")
    rank = 0
    for col in range(width):
        pivot = next((r for r in range(rank, height) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = pow(rows[rank][col], -1, PRIME)
        rows[rank] = [(x * scale) % PRIME for x in rows[rank]]
        for row in range(rank + 1, height):
            scale = rows[row][col]
            if scale:
                rows[row] = [(x - scale * y) % PRIME
                             for x, y in zip(rows[row], rows[rank])]
        rank += 1
        if rank == height:
            break
    return rank


def determinant(matrix: list[list[int]]) -> int:
    """Bareiss determinant, with exact divisions and row pivoting."""
    rows = [row[:] for row in matrix]
    n = len(rows)
    if n == 0 or any(len(row) != n for row in rows):
        raise ValueError("a nonempty square matrix is required")
    previous, sign = 1, 1
    for col in range(n - 1):
        if not rows[col][col]:
            pivot = next((r for r in range(col + 1, n) if rows[r][col]), None)
            if pivot is None:
                return 0
            rows[col], rows[pivot] = rows[pivot], rows[col]
            sign = -sign
        pivot_value = rows[col][col]
        for row in range(col + 1, n):
            for j in range(col + 1, n):
                numerator = rows[row][j] * pivot_value - rows[row][col] * rows[col][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError("Bareiss division was not exact")
                rows[row][j] = quotient
            rows[row][col] = 0
        previous = pivot_value
    return sign * rows[-1][-1]


def block_ranks(a: int, b: int, q: int, orientation: str = "full") -> tuple[int, int]:
    positive_int(a, "a")
    positive_int(b, "b")
    degree(q)
    if orientation not in ("full", "mid"):
        raise ValueError("orientation must be full or mid")
    h = symmetric_dimension(a, q)
    phi = min((a + b - 1) * h, b * symmetric_dimension(a, q + 1))
    psi = b * h
    return (phi, psi) if orientation == "full" else (psi, phi)


def mixture_ranks(a: int, blocks: tuple[tuple[str, int], ...], q: int) -> tuple[int, int]:
    ranks = [block_ranks(a, b, q, orientation) for orientation, b in blocks]
    return tuple(sum(r[i] for r in ranks) for i in (0, 1))


def cube_free(value: int) -> tuple[int, int]:
    """Return multiplier, radicand with cbrt(value)=multiplier*cbrt(radicand)."""
    positive_int(value, "radicand")
    multiplier, radicand, divisor = 1, 1, 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        multiplier *= divisor ** (exponent // 3)
        radicand *= divisor ** (exponent % 3)
        divisor += 1
    return multiplier, radicand * value


def radical_term(radicand: int, coefficient: int | Fraction = 1) -> Radical:
    multiplier, base = cube_free(radicand)
    value = Fraction(coefficient) * multiplier
    return {base: value} if value else {}


def radical_add(*values: Radical) -> Radical:
    result: Radical = {}
    for value in values:
        for key, coefficient in value.items():
            result[key] = result.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def radical_scale(value: Radical, factor: int | Fraction) -> Radical:
    return {key: coefficient * factor for key, coefficient in value.items()
            if coefficient * factor}


def integer_cube_root(value: int) -> int:
    if type(value) is not int or value < 0:
        raise ValueError("cube-root argument must be a nonnegative integer")
    if value < 2:
        return value
    root = 1 << ((value.bit_length() + 2) // 3)
    while True:
        next_root = (2 * root + value // (root * root)) // 3
        if next_root >= root:
            break
        root = next_root
    while (root + 1) ** 3 <= value:
        root += 1
    while root ** 3 > value:
        root -= 1
    return root


@lru_cache(None)
def root_interval(radicand: int, bits: int = 80) -> tuple[Fraction, Fraction]:
    positive_int(radicand, "radicand")
    positive_int(bits, "bits")
    scale = 1 << bits
    value = radicand * scale ** 3
    lower = integer_cube_root(value)
    upper = lower if lower ** 3 == value else lower + 1
    return Fraction(lower, scale), Fraction(upper, scale)


def radical_interval(value: Radical, bits: int = 80) -> tuple[Fraction, Fraction]:
    lower, upper = Fraction(0), Fraction(0)
    for key, coefficient in value.items():
        lo, hi = root_interval(key, bits)
        if coefficient < 0:
            lo, hi = hi, lo
        lower += coefficient * lo
        upper += coefficient * hi
    return lower, upper


def radical_sign(value: Radical) -> int:
    if not value:
        return 0
    lower, upper = radical_interval(value)
    if lower > 0:
        return 1
    if upper < 0:
        return -1
    raise ArithmeticError("the exact radical sign was not resolved at 80 bits")


def profile(a: int, b: int) -> Radical:
    """Return Gamma=2^(4/3)*G, so all cube-root radicands are integers."""
    positive_int(a, "a")
    if type(b) is not int or b < 0:
        raise ValueError("b must be a nonnegative integer")
    if b == 0:
        return {}
    small, large = sorted((a, b))
    return radical_term(3 * small - 1, 2 * large + small - 1)


def curvature(a: int, k: int) -> Radical:
    positive_int(k, "k")
    return radical_add(radical_scale(profile(a, k), 2),
                       radical_scale(profile(a, k - 1), -1),
                       radical_scale(profile(a, k + 1), -1))


def koszul_full(a: int, b: int, p: int) -> int:
    """Existing shared-input formula, used only for the balancing comparison."""
    positive_int(a, "a")
    positive_int(b, "b")
    degree(p)
    if p >= a:
        return 0
    correction = comb(a - 1, p - 1) if p else 0
    return b * comb(a, p) - max(b - a + p, 0) * correction


def balancing_control(a: int) -> dict:
    if type(a) is not int or a < 2:
        raise ValueError("balancing requires a >= 2")
    source = (("full", a - 1), ("full", a + 1))
    target = (("full", a), ("full", a))
    source_k = [koszul_full(a, a - 1, p) + koszul_full(a, a + 1, p)
                for p in range(a)]
    target_k = [2 * koszul_full(a, a, p) for p in range(a)]
    if source_k != target_k:
        raise AssertionError("the shared Koszul control did not match")
    q = a - 1
    source_r, target_r = mixture_ranks(a, source, q), mixture_ranks(a, target, q)
    gap = Fraction(a - 1, a) * symmetric_dimension(a, q)
    if source_r[0] + gap != target_r[0] or gap.denominator != 1:
        raise AssertionError("incorrect symmetric-power rank gap")
    polynomial_gap = (3*a-1)*(3*a-3)**3 - (3*a-4)*(3*a-2)**3
    if polynomial_gap != 6*a - 5:
        raise AssertionError("incorrect exact score comparison")
    score_gap = radical_add(radical_scale(profile(a, a), 2),
                            radical_scale(profile(a, a - 1), -1),
                            radical_scale(profile(a, a + 1), -1))
    if radical_sign(score_gap) != 1:
        raise AssertionError("the misleading profile was not increasing")
    return {
        "a": a, "long_dimensions": [2*a, 4*a-2],
        "nonzero_slice_rank": 2*a, "shared_koszul_ranks": source_k,
        "degree": q, "source_symmetric_power_ranks": list(source_r),
        "target_symmetric_power_ranks": list(target_r),
        "phi_rank_gap": int(gap), "score_cube_comparison_numerator": polynomial_gap,
        "potential_increases": True, "degeneration_excluded": True,
    }


def matrix_controls() -> dict:
    count, maximum_entries = 0, 0
    for a, b, q, swapped in product(range(1, 5), range(1, 5), range(5), (False, True)):
        matrix = full_matrix(a, b, q, swapped)
        actual = modular_rank(matrix)
        expected = block_ranks(a, b, q)[int(swapped)]
        if actual != expected or actual != min(len(matrix), len(matrix[0])):
            raise AssertionError((a, b, q, swapped, actual, expected))
        count += 1
        maximum_entries = max(maximum_entries, len(matrix) * len(matrix[0]))
    critical = []
    for a, b in product(range(1, 5), range(1, 4)):
        matrix = full_matrix(a, b, b - 1)
        value = determinant(matrix)
        if abs(value) != 1:
            raise AssertionError((a, b, value))
        critical.append({"a": a, "b": b, "degree": b-1,
                         "size": len(matrix), "determinant": value})
    return {"grid_a_b": [1, 4], "degrees": [0, 4], "orientations": ["Phi", "Psi"],
            "matrices": count, "maximum_entries": maximum_entries,
            "prime": PRIME, "all_modular_ranks_full": True,
            "critical_integer_determinants": critical}


def curvature_controls() -> dict:
    nonzero, zero, identities, mixture_identities = 0, 0, 0, 0
    for a in range(1, 13):
        slope = radical_term(3*a-1, 2)
        intercept = radical_term(3*a-1, a-1)
        weights = {k: curvature(a, k) for k in range(1, a+3)}
        for weight in weights.values():
            sign = radical_sign(weight)
            if sign < 0:
                raise AssertionError("negative curvature")
            nonzero += sign > 0
            zero += sign == 0
        actual_intercept = radical_add(*(radical_scale(w, k) for k, w in weights.items()))
        if actual_intercept != intercept:
            raise AssertionError("intercept identity failed")
        for b in range(1, 21):
            rebuilt = radical_add(radical_scale(slope, b),
                                  *(radical_scale(w, min(b, k)) for k, w in weights.items()))
            if rebuilt != profile(a, b):
                raise AssertionError("finite curvature identity failed")
            identities += 1
        if a == 1 or a > 8:
            continue
        for b, d in product(range(1, 6), repeat=2):
            for modes in product(("full", "mid"), repeat=3):
                blocks = tuple(zip(modes, (b, d, a+1)))
                expected = radical_add(*(profile(a, width) for _, width in blocks))
                rebuilt: Radical = {}
                for k, weight in weights.items():
                    phi, psi = mixture_ranks(a, blocks, k-1)
                    factor = Fraction(k*(phi+psi), (a-1)*symmetric_dimension(a, k-1))
                    rebuilt = radical_add(rebuilt, radical_scale(weight, factor))
                if rebuilt != expected:
                    raise AssertionError("the rank decomposition failed")
                mixture_identities += 1
    return {"a": [1, 12], "b": [1, 20], "profile_identities": identities,
            "positive_curvatures": nonzero, "zero_curvatures": zero,
            "mixture_a": [2, 8], "mixture_widths": "b,d in 1..5 and a+1",
            "mixture_orientations": "all eight choices",
            "rank_decomposition_identities": mixture_identities,
            "sign_method": "certified rational cube-root intervals with 80 fractional bits"}


def dimension_controls() -> dict:
    types = tuple(product(("full", "mid"), range(1, 4)))
    targets = [blocks for size in range(1, 4)
               for blocks in combinations_with_replacement(types, size)]
    checked, compatible, equality = 0, 0, 0
    for a, width, copies in product(range(1, 6), range(1, 6), range(1, 4)):
        source_score = radical_scale(profile(a, width), copies)
        for blocks in targets:
            checked += 1
            second = sum(b if mode == "full" else a+b-1 for mode, b in blocks)
            third = sum(a+b-1 if mode == "full" else b for mode, b in blocks)
            if second > copies*width or third > copies*(a+width-1):
                continue
            compatible += 1
            target_score = radical_add(*(profile(a, b) for _, b in blocks))
            sign = radical_sign(radical_add(source_score, radical_scale(target_score, -1)))
            if sign < 0:
                raise AssertionError("a dimension-compatible improving profile was found")
            equality += sign == 0
    return {"a_B": [1, 5], "source_copies": [1, 3], "target_widths": [1, 3],
            "target_blocks": [1, 3], "target_orientations": ["full", "mid"],
            "formats_checked": checked, "dimension_compatible": compatible,
            "equal_scores": equality}


def report() -> dict:
    return {
        "schema_version": 1,
        "arithmetic": "integers, Fraction, finite-field rank and certified radical intervals",
        "field_scope": "all-size imported determinant theorem and degeneration claim over C",
        "claim_scope": "finite controls; no tensor construction or exponent improvement",
        "coefficient_matrices": matrix_controls(),
        "symmetric_curvature": curvature_controls(),
        "heterogeneous_dimension_formats": dimension_controls(),
        "balancing_controls": [balancing_control(a) for a in range(2, 13)],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key != "balancing_controls"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()


"""Replay exact certificates for an unconstructed all-dimension target family."""
import argparse
from fractions import Fraction
from functools import lru_cache
import json
from math import comb, factorial
from pathlib import Path

from koszul import choose, intrinsic_rank


def target(m):
    degree = m - 1
    monomials = [(i, d - i) for d in range(m) for i in range(d + 1)]
    weights = []
    for x in range(m):
        row = []
        for i, j in monomials:
            k = degree - i - j
            row.append(Fraction((-1) ** k * choose(k, x - i),
                                factorial(i) * factorial(j) * factorial(k)))
        weights.append(row)
    support = [(a + c, y, z)
               for y, (a, b) in enumerate(monomials)
               for z, (c, d) in enumerate(monomials) if a + b + c + d == degree]
    return monomials, weights, support


def interpolation_check(m):
    monomials, weights, support = target(m)
    degree = m - 1

    @lru_cache(None)
    def coefficient(x, a, b):
        return sum(weights[x][h] * i ** a * j ** b
                   for h, (i, j) in enumerate(monomials))

    negative = constant = positive_nonzero = 0
    for a, b in monomials:
        for c, d in monomials:
            epsilon_degree = a + b + c + d - degree
            for x in range(m):
                value = coefficient(x, a + c, b + d)
                if epsilon_degree < 0:
                    negative += 1
                    assert value == 0
                elif epsilon_degree == 0:
                    constant += 1
                    assert value == int(a + c == x)
                else:
                    positive_nonzero += bool(value)
    rows = [{(x, z) for x, y, z in support if y == i} for i in range(len(monomials))]
    assert all(rows)
    assert len(set.union(*rows)) == sum(map(len, rows))
    assert len(support) == comb(m + 2, 3)
    return {"m": m, "dimensions": [m, len(monomials), len(monomials)],
            "border_rank": len(monomials), "constant_support_terms": len(support),
            "coefficient_checks": m * len(monomials) ** 2,
            "negative_power_coefficients_checked": negative,
            "constant_coefficients_checked": constant,
            "nonzero_positive_power_coefficients": positive_nonzero}


def koszul_check(m, k):
    size = k * m * (m + 1) // 2
    target_ranks = [k * sum(intrinsic_rank(m, u, m + 1 - u, p)
                            for u in range(1, m + 1)) for p in range(m)]
    source = [intrinsic_rank(m, size, size + m - 1, p) for p in range(m)]
    expected = [size * comb(m - 1, p) for p in range(m)]
    slack = [(m - p) * choose(m - 1, p - 1) for p in range(m)]
    assert target_ranks == expected
    assert [s - t for s, t in zip(source, target_ranks)] == slack
    return {"m": m, "k": k, "shared_degrees_checked": m,
            "minimum_shared_rank_slack": min(slack)}


def coordinate_gap(m, k):
    return k * ((m - 1) ** 2 // 4) - (m - 1) // 2


def gap_check(m, k):
    # Independent capacity lower bound: each endpoint receives at most two edges.
    doubled = [w for w in range(m) for _ in range(2 * k)]
    capacity_bound = sum(doubled[:m * k - 1])
    assert coordinate_gap(m, k) == capacity_bound
    return capacity_bound


def exact_conditional_exponent():
    a, b = 168, 125
    lhs = (1 << (3 * b)) * (b * b) ** b
    rhs = (1 << a) * (a * (a + b)) ** b
    assert lhs > rhs
    return {"premise": "H(1), the unconstructed sequence of source degenerations",
            "d_lower_bound": str(Fraction(a, b)),
            "Q_at_d_exceeds_one_by_exact_integer_comparison": True,
            "left_integer_bit_length": lhs.bit_length(),
            "right_integer_bit_length": rhs.bit_length(),
            "conditional_exponent_upper_bound": str(Fraction(3 * b, a)),
            "conditional_exponent_decimal": float(Fraction(3 * b, a)),
            "exponent_bound_achieved": False}


def run():
    interpolation = [interpolation_check(m) for m in range(2, 9)]
    koszul = [koszul_check(m, k) for m in range(2, 41) for k in (1, 2, 7, 53)]
    gap_cases = [(m, k) for m in range(2, 101) for k in (1, 2, 3, 7, 53)]
    for m, k in gap_cases:
        gap_check(m, k)
    return {"status": "target certificates and conditional implication; construction open",
            "source_degeneration_constructed": False, "new_exponent_established": False,
            "proof": "research/ai/2026-10-20-koszul/all_dimension_targets.md",
            "interpolation": interpolation,
            "total_interpolation_coefficient_checks": sum(r["coefficient_checks"] for r in interpolation),
            "koszul_cases": len(koszul),
            "koszul_shared_degrees_checked": sum(r["shared_degrees_checked"] for r in koszul),
            "koszul_m_range": [2, 40], "koszul_k_values": [1, 2, 7, 53],
            "gap_formula_cases": len(gap_cases), "gap_m_range": [2, 100],
            "gap_k_values": [1, 2, 3, 7, 53],
            "critical_overhead_cube": str(Fraction(729, 686)),
            "conditional_exponent": exact_conditional_exponent()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items() if key != "interpolation"}, indent=2))

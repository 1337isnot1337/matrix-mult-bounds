#!/usr/bin/env python3
"""Exact finite certificates for the exponential-jet algebra smoothing.

This verifies an algebra degeneration, not the required convolution-tensor
degeneration. The natural constant ratio generator is a rejected candidate.
Only the Python standard library is required.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import factorial
import json
from pathlib import Path

_family_spec = spec_from_file_location(
    'singular_smoothing_family', Path(__file__).with_name('verify_family.py'))
_family = module_from_spec(_family_spec)
_family_spec.loader.exec_module(_family)
identity, inverse, product = _family.identity, _family.inverse, _family.product
rank, rational_matrix = _family.rank, _family.rational_matrix


def polynomial_product(left, right, length):
    result = [Fraction(0)] * length
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right[:length - i]):
                if b:
                    result[i + j] += a * b
    return result


def polynomial_power(poly, exponent, length):
    result = [Fraction(1)] + [Fraction(0)] * (length - 1)
    for _ in range(exponent):
        result = polynomial_product(result, poly, length)
    return result


def matrix_vector(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def smoothing_basis(m):
    n = m * (m + 1) // 2
    pairs = [(a, degree - a) for degree in range(m)
             for a in range(degree + 1)]
    g = [Fraction(0)] + [Fraction(1, factorial(k)) for k in range(1, n)]
    powers = [polynomial_power(g, b, n) for b in range(m)]
    columns = [[Fraction(0)] * a + powers[b][:n - a] for a, b in pairs]
    matrix = [list(row) for row in zip(*columns)]
    return pairs, columns, matrix, inverse(matrix)


def annihilator_polynomials(m):
    """Return Q(z) z^i, where Q has the lower-degree exponential roots."""
    n = m * (m + 1) // 2
    q = [Fraction(1)] + [Fraction(0)] * (n - 1)
    for node in range(m - 1):
        factor = [Fraction(-node), Fraction(1)]
        for _ in range(m - 1 - node):
            q = polynomial_product(q, factor, n)
    return [[Fraction(0)] * i + q[:n - i] for i in range(m)]


def verify(max_m):
    records = []
    pair_checks = 0
    coefficient_checks = 0
    dual_coefficient_checks = 0
    ratio_interior_checks = 0
    certificate = None
    for m in range(2, max_m + 1):
        degree = m - 1
        pairs, columns, basis, inv = smoothing_basis(m)
        n = len(pairs)
        lower = n - m
        indices = {pair: i for i, pair in enumerate(pairs)}
        assert product(basis, inv) == identity(n)
        assert product(inv, basis) == identity(n)
        zero_exponent_count = 0
        positive_exponent_count = 0
        for i, alpha in enumerate(pairs):
            for j, beta in enumerate(pairs):
                expanded = matrix_vector(
                    inv, polynomial_product(columns[i], columns[j], n))
                special = [Fraction(0)] * n
                for k, (gamma, coefficient) in enumerate(zip(pairs, expanded)):
                    exponent = sum(alpha) + sum(beta) - sum(gamma)
                    if coefficient:
                        assert exponent >= 0, (m, alpha, beta, gamma)
                        if exponent == 0:
                            special[k] = coefficient
                            zero_exponent_count += 1
                        else:
                            positive_exponent_count += 1
                    coefficient_checks += 1
                expected = [Fraction(0)] * n
                if sum(alpha) + sum(beta) <= degree:
                    index = indices[(alpha[0] + beta[0], alpha[1] + beta[1])]
                    expected[index] = Fraction(1)
                assert special == expected, (m, alpha, beta)
                pair_checks += 1

        # p(partial_t)|_(t=0) has values k! p_k on the monomial t^k.
        dual_polys = annihilator_polynomials(m)
        differential_rows = [[coefficient * factorial(k)
                              for k, coefficient in enumerate(poly)]
                             for poly in dual_polys]
        dual_in_basis = product(differential_rows, basis)
        assert all(not x for row in dual_in_basis for x in row[:lower])
        assert rank([row[lower:] for row in dual_in_basis]) == m
        dual_coefficient_checks += m * n

        # Natural constant candidate: tau=(exp(t)-1)/t and ell dual to g^D.
        # Interior monomials shift as expected, but boundary contributions
        # need not vanish. Record the failure without a numerical tolerance.
        tau = [Fraction(1, factorial(k + 1)) for k in range(n)]
        ell = inv[indices[(0, degree)]]
        tau_powers = [polynomial_power(tau, i, n) for i in range(m)]
        krylov = [[sum(a * b for a, b in zip(
                       ell, polynomial_product(tau_i, column, n)))
                   for tau_i in tau_powers] for column in columns]
        for row, (a, b) in zip(krylov, pairs):
            for i in range(min(a, degree) + 1):
                expected = int(a == i and b + i == degree)
                assert row[i] == expected, (m, a, b, i, row[i])
                ratio_interior_checks += 1
        bad_lower = [(pairs[j], i, value)
                     for j, row in enumerate(krylov[:lower])
                     for i, value in enumerate(row) if value]
        assert bad_lower, "This tested constant-ratio candidate unexpectedly passed"
        record = {
            "m": m, "N": n,
            "basis_rank": n,
            "ordered_products_checked": n * n,
            "zero_exponent_nonzero_coefficients": zero_exponent_count,
            "positive_exponent_nonzero_coefficients": positive_exponent_count,
            "basis_scaling_determinant_exponent": sum(a + b for a, b in pairs),
            "homogeneous_dual_rank": rank(dual_in_basis),
            "natural_ratio_candidate": {
                "status": "rejected-constant-window-boundary-errors",
                "lower_degree_boundary_nonzeros": len(bad_lower),
                "lower_degree_block_rank": rank(krylov[:lower]),
                "first_boundary_error": {
                    "input": list(bad_lower[0][0]),
                    "moment_index": bad_lower[0][1],
                    "coefficient": str(bad_lower[0][2]),
                },
            },
        }
        assert record["basis_scaling_determinant_exponent"] == m * (m * m - 1) // 3
        records.append(record)
        if m == 4:
            certificate = {
                "basis_order_a_b": [list(pair) for pair in pairs],
                "basis_columns_in_t_monomials": rational_matrix(basis),
                "inverse_basis_matrix": rational_matrix(inv),
                "degree_scaling_exponents": [a + b for a, b in pairs],
                "top_degree_annihilator_polynomials_Q_z_power_i": rational_matrix(dual_polys),
                "top_degree_differential_functionals_in_basis": rational_matrix(dual_in_basis),
                "natural_ratio_krylov_in_basis": rational_matrix(krylov),
            }
    return {
        "status": "exact-finite-controls-passed",
        "claim_scope": "Explicit curvilinear algebra smoothing and its dual coordinates only.",
        "constructs_algebra_smoothing": True,
        "constructs_required_tensor_degeneration": False,
        "improves_omega": False,
        "arithmetic": "Python fractions.Fraction and integers",
        "parameters": {"m_min": 2, "m_max": max_m},
        "coverage": {
            "ordered_pair_products": pair_checks,
            "transported_structure_coefficients": coefficient_checks,
            "differential_dual_coefficients": dual_coefficient_checks,
            "natural_ratio_interior_identity_checks": ratio_interior_checks,
        },
        "m4_certificate": certificate,
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=6)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_m < 2:
        parser.error("--max-m must be at least 2")
    report = verify(args.max_m)
    serialized = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
        print(json.dumps({"status": report["status"],
                          "coverage": report["coverage"],
                          "output": str(args.output)}))
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()

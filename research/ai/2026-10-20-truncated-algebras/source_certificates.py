"""Exact polynomial certificates for source costs; no numerical tensor fitting."""
from __future__ import annotations

from collections import defaultdict
from itertools import product

from product_search import cw_support, product_support


def cw_polynomial(q):
    """Expand the standard q+2-term Laurent border decomposition of CW_q."""
    if not isinstance(q, int) or q < 1:
        raise ValueError("positive integer q required")
    coefficients = defaultdict(int)

    def add_term(forms, shift, scalar):
        for left, middle, right in product(*forms):
            i, ei, ai = left
            j, ej, aj = middle
            k, ek, ak = right
            coefficients[shift + ei + ej + ek, i, j, k] += scalar * ai * aj * ak

    for i in range(1, q + 1):
        form = [(0, 0, 1), (i, 1, 1)]
        add_term([form] * 3, -2, 1)
    aggregate = [(0, 0, 1)] + [(i, 2, 1) for i in range(1, q + 1)]
    add_term([aggregate] * 3, -3, -1)
    corner = [(0, 0, 1), (q + 1, 3, 1)]
    # These two coefficients multiply the same rank-one product, so together
    # they cost one term, not two.
    add_term([corner] * 3, -3, 1)
    add_term([corner] * 3, -2, -q)
    return {index: value for index, value in coefficients.items() if value}


def verify_cw(q):
    polynomial = cw_polynomial(q)
    if any(power < 0 for power, i, j, k in polynomial):
        raise ArithmeticError("uncancelled negative Laurent coefficient")
    leading = {(i, j, k): value for (power, i, j, k), value in polynomial.items() if power == 0}
    if leading != {point: 1 for point in cw_support(q)}:
        raise ArithmeticError("wrong CW leading coefficient")
    return {"q": q, "rank_one_terms": q + 2,
            "leading_tensor_terms": len(leading),
            "total_nonzero_polynomial_coefficients": len(polynomial),
            "polynomial_degree": max(power for power, i, j, k in polynomial),
            "negative_powers": 0}


def verify_digit_product(a, b):
    r = a * b
    source = [(i, j, r - 1 - i - j) for i in range(r) for j in range(r - i)]
    minimum = min(sum(value % b for value in point) for point in source)
    retained = [point for point in source if sum(value % b for value in point) == minimum]
    if minimum != b - 1 or set(retained) != set(product_support((a, b))):
        raise ArithmeticError("incorrect no-carry degeneration")
    return {"factors": [a, b], "source_rank_bound": r,
            "input_terms": len(source), "retained_terms": len(retained),
            "minimum_low_digit_sum": minimum}


if __name__ == "__main__":
    import json
    print(json.dumps({"cw": [verify_cw(q) for q in range(1, 9)],
                      "digit_products": [verify_digit_product(a, b)
                                         for a in range(2, 7) for b in range(2, 7)]}, indent=2))

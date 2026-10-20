"""Exact ten-point border-rank certificate for the degree-three target.

Evaluation at epsilon times ten triangular-grid nodes, followed by cubic
coefficient interpolation, has the required tensor as its constant term.
The certificate is from a diagonal rank-ten source, NOT from C(4,10k).
"""
import argparse
from collections import Counter
import json
from pathlib import Path

import sympy as sp


def run():
    monomials = [(i, degree - i) for degree in range(4) for i in range(degree + 1)]
    points = monomials[:]
    evaluation = sp.Matrix([[s ** i * t ** j for i, j in monomials] for s, t in points])
    inverse = evaluation.inv()
    weights = inverse[6:10, :]
    constant_support = []
    counts = Counter()
    for i, (a, b) in enumerate(monomials):
        for j, (c, d) in enumerate(monomials):
            power = a + b + c + d - 3
            for x in range(4):
                coeff = sum(weights[x, node] * s ** (a + c) * t ** (b + d)
                            for node, (s, t) in enumerate(points))
                counts["total_coefficients_checked"] += 1
                if power < 0:
                    counts["negative_power_coefficients_checked"] += 1
                    if coeff != 0:
                        raise AssertionError("negative epsilon power did not cancel")
                elif power == 0:
                    counts["constant_coefficients_checked"] += 1
                    expected = int(a + c == x)
                    if coeff != expected:
                        raise AssertionError("constant coefficient differs from target")
                    if coeff:
                        constant_support.append([x, i, j])
                elif coeff:
                    counts["nonzero_positive_power_coefficients"] += 1
    # In this basis each (X,Z) coordinate occurs in only one Y row, and every
    # Y row has support; this independently certifies flattening rank ten.
    yz_rows = [{(x, z) for x, y, z in constant_support if y == i} for i in range(10)]
    if any(not row for row in yz_rows) or any(yz_rows[i] & yz_rows[j]
                                            for i in range(10) for j in range(i)):
        raise AssertionError("disjoint-support flattening certificate failed")
    return {"status": "exact border-rank certificate for target only",
            "source_convolution_degeneration_constructed": False,
            "dimensions": [4, 10, 10], "border_rank": 10,
            "rank_one_terms": 10, "maximum_epsilon_degree_after_cancellation": 3,
            "monomials_st_exponents": monomials, "evaluation_nodes": points,
            "evaluation_determinant": str(evaluation.det()),
            "output_weights_rows": [[str(weights[i, j]) for j in range(10)] for i in range(4)],
            "rank_one_term_formula": "epsilon^-3 * (sum_x weights[x,h] X_x) * F(epsilon*s_h,epsilon*t_h) * G(epsilon*s_h,epsilon*t_h)",
            "constant_support": constant_support,
            "flattening_lower_bound": 10, "checks": dict(counts)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("status", "border_rank", "checks")}, indent=2))

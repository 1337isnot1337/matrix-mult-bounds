"""Exact restrictions P_a -> M(a,2,a), valid for every integer a>=2.

All maps have entries 0, 1, -1.  Every coefficient is checked over Z.
These constructions do not improve the matrix multiplication exponent.
"""

from collections import Counter
from itertools import product
import argparse
import json
from pathlib import Path


def maps(a):
    if not isinstance(a, int) or a < 2:
        raise ValueError("a must be an integer at least two")
    first = {(p, q): (1, (q, p)) for p, q in product(range(a), repeat=2)}
    second = {}
    for y, j in product(range(a), range(2*a-1)):
        if y == 0:
            second[y, j] = (1, (j+1, 1) if j < a-1 else (j-a+1, 0))
        elif y == 1:
            second[y, j] = (1, (j, 1) if j < a else (j-a, 0))
        else:
            second[y, j] = (0, None)
    third = {}
    for z, v in product(range(2*a-1), range(a)):
        if z > a:
            third[z, v] = (0, None)
        elif z <= v:
            third[z, v] = ((-1)**(a-1-v), (0, z-v+a-1))
        else:
            third[z, v] = ((-1)**v, (1, z-v-1))
    return first, second, third


def coefficient_table(a):
    first, second, third = maps(a)
    coefficients = Counter()
    contribution_counts = Counter()
    zero_terms = 0
    for p, q, y, v in product(range(a), repeat=4):
        sa, target_a = first[p, q]
        sb, target_b = second[y, q+v]
        sc, target_c = third[p+y, v]
        coefficient = sa*sb*sc
        if not coefficient:
            zero_terms += 1
            continue
        key = (target_a, target_b, target_c)
        coefficients[key] += coefficient
        contribution_counts[key] += 1
    return coefficients, contribution_counts, zero_terms


def certificate(a):
    coefficients, contributions, zero_terms = coefficient_table(a)
    target = {((i, k), (i, j), (j, k)): 1
              for i, j, k in product(range(a), range(2), range(a))}
    if {key: value for key, value in coefficients.items() if value} != target:
        raise ArithmeticError("The full integer coefficient identity failed")
    # Check all entries, not only the prescribed support.
    checked = 0
    for target_a, target_b, target_c in product(product(range(a), repeat=2),
                                               product(range(a), range(2)),
                                               product(range(2), range(a))):
        key = (target_a, target_b, target_c)
        if coefficients[key] != target.get(key, 0):
            raise ArithmeticError("A target or off-support coefficient is wrong")
        checked += 1
    canceled = [key for key, value in coefficients.items() if not value]
    if (len(canceled) != a*a*(a-1)
            or any(contributions[key] != 2 for key in canceled)
            or any(contributions[key] != 1 for key in target)
            or zero_terms != a**4-2*a**3):
        raise ArithmeticError("Unexpected source-term or cancellation count")
    return {
        "a": a, "source": f"P_{a}", "target": f"M({a},2,{a})",
        "source_dimensions": [a*a, a*(2*a-1), a*(2*a-1)],
        "target_dimensions": [a*a, 2*a, 2*a],
        "source_terms_checked": a**4, "source_terms_mapping_to_zero": zero_terms,
        "nonzero_source_contributions": 2*a**3,
        "all_target_coefficient_positions_checked": checked,
        "target_terms": 2*a*a, "off_support_cancellation_pairs": len(canceled),
        "coefficient_ring": "Z", "valid_over_every_field": True,
        "restriction_constructed": True, "improves_omega": False,
    }


def multiply(left, right):
    a = len(left)
    if (a < 2 or len(right) != 2 or any(len(row) != 2 for row in left)
            or any(len(row) != a for row in right)):
        raise ValueError("Expected an a-by-2 matrix and a 2-by-a matrix, a>=2")
    _, second, third = maps(a)
    b = {source: coefficient*left[i][j]
         for source, (coefficient, target) in second.items() if coefficient
         for i, j in [target]}
    c = {source: coefficient*right[j][k]
         for source, (coefficient, target) in third.items() if coefficient
         for j, k in [target]}
    return [[sum(b.get((y, i+v), 0)*c.get((k+y, v), 0)
                 for y, v in product(range(a), repeat=2))
             for k in range(a)] for i in range(a)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", type=int, nargs="+", default=list(range(2, 9)))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    reports = [certificate(a) for a in args.sizes]
    if args.output:
        args.output.write_text(json.dumps(reports, indent=2)+"\n")
    print(json.dumps(reports, indent=2))

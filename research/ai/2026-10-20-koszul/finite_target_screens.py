"""Exact finite controls for the written finite-target screening arguments."""
import argparse
from fractions import Fraction
import json
from math import comb
from pathlib import Path


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total+1):
        for rest in compositions(total-first, length-1):
            yield (first,)+rest


def normalized_coefficients(a, b):
    m = a+b-1
    return [[Fraction(comb(a-1, i)*comb(b-1, j), m*comb(m-1, i+j))
             for j in range(b)] for i in range(a)]


def marginal_control(a, b):
    p = normalized_coefficients(a, b)
    rows = [sum(row) for row in p]
    columns = [sum(p[i][j] for i in range(a)) for j in range(b)]
    output = [sum(p[i][k-i] for i in range(a) if 0 <= k-i < b)
              for k in range(a+b-1)]
    assert rows == [Fraction(1, a)]*a
    assert columns == [Fraction(1, b)]*b
    assert output == [Fraction(1, a+b-1)]*(a+b-1)
    return {"a": a, "b": b, "marginals": [str(rows[0]), str(columns[0]),
                                          str(output[0])]}


def convolution(p, q):
    r = [Fraction(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return r


def convolution_controls(maximum_degree=5, denominator=3):
    count = 0
    for degree in range(1, maximum_degree+1):
        vectors = [tuple(Fraction(x, denominator) for x in c)
                   for c in compositions(denominator, degree+1)]
        m = 2*degree+1
        for p in vectors:
            for q in vectors:
                r = convolution(p, q)
                assert r[degree]**2 >= 4*r[0]*r[-1]
                variation = sum(abs(x-Fraction(1, m)) for x in r)/2
                assert variation >= Fraction(1, 3*m)
                count += 1
    return {"maximum_degree": maximum_degree, "probability_denominator": denominator,
            "ordered_distribution_pairs": count, "all_passed": True}


def component_controls(maximum_size=6, types=4):
    count = 0
    for l in range(1, maximum_size+1):
        for n in range(1, maximum_size+1):
            for rows in compositions(l, types):
                for columns in compositions(n, types):
                    products = [r*s for r, s in zip(rows, columns)]
                    missing = l*n-sum(products)
                    assert max(products) >= l*n-2*missing
                    count += 1
    return {"maximum_rows_and_columns": maximum_size, "word_types": types,
            "count_vector_pairs": count, "all_passed": True}


def square_capacity(n, output_dimension):
    return n*(3*n*n-2*output_dimension)


def report():
    marginal_records = [marginal_control(a, b)
                        for a in range(1, 17) for b in range(1, 17)]
    entropy_records = []
    for a in range(2, 17):
        m = 2*a-1
        denominator = 81*m*m
        old_lhs = 6**9*a**8*m**5
        old_rhs = (6*a-2)**12
        difference = old_rhs*(denominator+2)**9-old_lhs*denominator**9
        entropy_records.append({"a": a, "entropy_deficit": str(Fraction(2, 9*m*m)),
            "rational_factor": str(Fraction(denominator, denominator+2)),
            "old_coordinate_screen_excludes": old_lhs <= old_rhs,
            "new_coordinate_screen_excludes": difference >= 0,
            "integer_comparison_difference": difference})
    return {"status": "finite exact controls for unreviewed written proofs",
        "new_exponent_established": False, "independent_review": False,
        "uniform_marginal_records": marginal_records,
        "singleton_quantum_screen": {"source_value": 12544, "target_value": 11236,
            "target_excluded": False, "target_constructed": False},
        "convolution_controls": convolution_controls(),
        "entropy_screen_records": entropy_records,
        "component_controls": component_controls(),
        "laurent_output_screen": {"source_output_dimension": 12544,
            "source_group_order": 117649, "square_target_upper_bound": 93,
            "constructed": False,
            "records": [{"n": n, "capacity_lhs": square_capacity(n, 12544),
                         "excluded": square_capacity(n, 12544) > 117649}
                        for n in (49, 93, 94, 106, 112)]}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+"\n")
    print("Exact finite controls passed; the target degeneration remains unconstructed.")

"""Exact finite controls for the ordinary Hankel-symbol dimension bound.

The proof is in hankel_symbol_dimension.md.  These controls do not prove
a tensor construction, an asymptotic exclusion, or a smaller exponent.
Only the Python standard library is needed.
"""

from collections import Counter
from itertools import combinations, combinations_with_replacement, product
import json
from math import comb
from pathlib import Path


def rref(matrix, prime):
    a = [[int(x) % prime for x in row] for row in matrix]
    if not a:
        return a, []
    rows, columns = len(a), len(a[0])
    pivot_columns = []
    active = 0
    for column in range(columns):
        pivot = next((i for i in range(active, rows) if a[i][column]), None)
        if pivot is None:
            continue
        a[active], a[pivot] = a[pivot], a[active]
        inverse = pow(a[active][column], -1, prime)
        a[active] = [(x * inverse) % prime for x in a[active]]
        for i in range(rows):
            if i != active and a[i][column]:
                factor = a[i][column]
                a[i] = [(x - factor*y) % prime
                        for x, y in zip(a[i], a[active])]
        pivot_columns.append(column)
        active += 1
        if active == rows:
            break
    return a, pivot_columns


def rank(matrix, prime=101):
    return len(rref(matrix, prime)[1])


def nullspace(matrix, prime):
    reduced, pivots = rref(matrix, prime)
    columns = len(matrix[0])
    answer = []
    for free in range(columns):
        if free in pivots:
            continue
        vector = [0]*columns
        vector[free] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free] % prime
        answer.append(vector)
    return answer


def trim(polynomial):
    answer = list(polynomial)
    while len(answer) > 1 and not answer[-1]:
        answer.pop()
    return answer


def remainder(dividend, divisor, prime):
    a, b = trim(dividend), trim(divisor)
    if b == [0]:
        raise ZeroDivisionError("zero polynomial")
    inverse = pow(b[-1], -1, prime)
    while a != [0] and len(a) >= len(b):
        shift = len(a)-len(b)
        factor = a[-1]*inverse % prime
        for i, value in enumerate(b):
            a[shift+i] = (a[shift+i]-factor*value) % prime
        a = trim(a)
    return a


def gcd(left, right, prime):
    a, b = trim(left), trim(right)
    while b != [0]:
        a, b = b, remainder(a, b, prime)
    inverse = pow(a[-1], -1, prime)
    return [(x*inverse) % prime for x in a]


def kernel_scheme_degree(sequence, a, b, prime):
    """Recover the homogeneous gcd of the left Hankel kernel."""
    hankel = [[sequence[p+q] for q in range(b)] for p in range(a)]
    actual_rank = rank(hankel, prime)
    if not 0 < actual_rank < min(a, b):
        raise ValueError("this control requires a nonzero deficient Hankel rank")
    kernel = nullspace([list(row) for row in zip(*hankel)], prime)
    polynomials = [trim(v) for v in kernel]
    finite_gcd = polynomials[0]
    for polynomial in polynomials[1:]:
        finite_gcd = gcd(finite_gcd, polynomial, prime)
    infinity_order = min(a-len(polynomial) for polynomial in polynomials)
    degree = len(finite_gcd)-1+infinity_order
    # The homogeneous polynomial has this degree; the missing highest
    # coefficients encode its factor at infinity.
    q = finite_gcd+[0]*(degree+1-len(finite_gcd))
    d = a+b-2
    annihilates = all(sum(q[i]*sequence[k+i] for i in range(len(q))) % prime == 0
                      for k in range(d-degree+1))
    assert degree == actual_rank and annihilates
    return actual_rank, infinity_order


def binary_hankel_controls():
    answer = []
    for a, b in ((3, 4), (4, 5), (5, 6)):
        histogram = Counter()
        checked = infinity = 0
        for sequence in product(range(2), repeat=a+b-1):
            if not any(sequence):
                continue
            actual_rank = rank([[sequence[p+q] for q in range(b)]
                                for p in range(a)], 2)
            histogram[actual_rank] += 1
            if actual_rank < min(a, b):
                recovered, infinity_order = kernel_scheme_degree(sequence, a, b, 2)
                assert recovered == actual_rank
                checked += 1
                infinity += int(infinity_order > 0)
        answer.append({
            "a": a, "b": b, "field_prime": 2,
            "nonzero_sequences": 2**(a+b-1)-1,
            "rank_histogram": dict(sorted(histogram.items())),
            "kernel_gcd_and_annihilation_checks": checked,
            "kernel_gcd_with_infinity_factor": infinity,
        })
    return answer


POINTS = (0, 1, 2, None)


def jet(degree, point, order):
    if point is None:
        return [int(k == degree-order) for k in range(degree+1)]
    return [comb(k, order)*point**(k-order) if k >= order else 0
            for k in range(degree+1)]


def schemes(length):
    for indices in combinations_with_replacement(range(len(POINTS)), length):
        counts = tuple(indices.count(j) for j in range(len(POINTS)))
        yield counts


def scheme_jets(degree, scheme):
    return [jet(degree, point, order)
            for point, multiplicity in zip(POINTS, scheme)
            for order in range(multiplicity)]


def hermite_controls():
    counts = {}
    degree, prime = 9, 101
    for length in range(1, degree+2):
        checked = 0
        for scheme in schemes(length):
            rows = scheme_jets(degree, scheme)
            assert rank(rows, prime) == length
            checked += 1
        counts[length] = checked
    return {
        "degree": degree, "field_prime": prime,
        "points": [0, 1, 2, "infinity"],
        "schemes_by_length": counts,
        "total_schemes": sum(counts.values()),
        "all_jet_lists_have_full_rank": True,
    }


def pencil_controls():
    answer = []
    for a, b, r in ((4, 5, 2), (5, 6, 3)):
        d = a+b-2
        data = []
        for scheme in schemes(r):
            rows = scheme_jets(d, scheme)
            sequence = [sum(values) for values in zip(*rows)]
            assert rank([[sequence[p+q] for q in range(b)] for p in range(a)]) == r
            data.append((scheme, sequence))
        histogram = Counter()
        for (z0, h0), (z1, h1) in combinations(data, 2):
            union_length = sum(max(x, y) for x, y in zip(z0, z1))
            assert union_length > r
            summed = [x+y for x, y in zip(h0, h1)]
            summed_rank = rank([[summed[p+q] for q in range(b)] for p in range(a)])
            assert summed_rank > r
            histogram[summed_rank] += 1
        answer.append({
            "a": a, "b": b, "rank_limit": r, "field_prime": 101,
            "schemes": len(data), "distinct_scheme_pencils": sum(histogram.values()),
            "sum_rank_histogram": dict(sorted(histogram.items())),
            "every_distinct_scheme_pencil_has_a_member_above_rank_limit": True,
        })
    return answer


def allowed_ranks(a, b):
    if min(a, b) < 2:
        raise ValueError("a and b must be at least two")
    return [r for r in range(1, min(a, b)) if 3*r <= a+b-1]


def square_block_tests(a, b, sizes):
    """Necessary ordinary-map tests only; passing is not a construction."""
    sizes = tuple(int(n) for n in sizes)
    if not sizes or any(n < 1 for n in sizes):
        raise ValueError("positive square block sizes required")
    dimension = sum(n*n for n in sizes)
    source = a*b*(a+b-1)
    if dimension > source:
        raise ValueError("target already exceeds source leg dimension")
    loss = source-dimension
    tests = []
    for block, n in enumerate(sizes):
        for r in allowed_ranks(a, b):
            lifted_rank_upper = n+2*loss
            tests.append({
                "block_index": block, "block_size": n, "symbol_rank_limit": r,
                "block_dimension": n*n, "coefficient_dimension_limit": r*a*b,
                "lifted_rank_one_slice_upper_bound": lifted_rank_upper,
                "rank_threshold": (r+1)*a*b,
                "excludes_ordinary_restriction":
                    n*n > r*a*b and lifted_rank_upper < (r+1)*a*b,
            })
    return {
        "a": a, "b": b, "blocks": list(sizes), "source_leg_dimension": source,
        "target_leg_dimension": dimension, "loss_per_leg": loss,
        "tests": tests,
        "ordinary_restriction_excluded": any(t["excludes_ordinary_restriction"] for t in tests),
        "singular_degeneration_excluded": False,
    }


def variable_scheme_projection_control():
    # Two rational-function directions with recurrence f_(k+2)=x*f_k.
    # Multiplication by z^s supplies twelve independent C-valued slices.
    a, b, m = 5, 6, 10
    vectors = []
    for parity in (0, 1):
        for s in range(b):
            vector = [0]*(a*m*b)
            for j in range(a):
                vector[(j*m+2*j+parity)*b+s] = 1
            vectors.append(vector)
    projected = [[vector[(i*m+k)*b+s]
                  for k in (0, 1) for i in range(a) for s in range(b)]
                 for vector in vectors]
    original_rank = rank(vectors)
    projected_rank = rank(projected)
    assert original_rank == projected_rank == 12
    return {
        "a": a, "b": b, "variable_recurrence": "f[k+2]=x*f[k]",
        "symbol_span_dimension_over_C_x_z": 2,
        "selected_long_coordinates": [0, 1],
        "coefficient_space_dimension": original_rank,
        "projected_coefficient_rank_mod_101": projected_rank,
        "coefficient_dimension_bound": 2*a*b,
        "constant_scheme_claimed": False,
    }


def scheme_line_boundary_controls():
    """The fixed-scheme line condition cannot drop 3r<=m."""
    answer = []
    for r in (2, 3, 4, 5):
        a, b = r+r//2, r+(r+1)//2
        m = a+b-1
        assert m == 3*r-1 and r not in allowed_ranks(a, b)
        ranks = []
        for parameter in (0, 1, 2, None):
            sequence = [0]*m
            if parameter is None:
                sequence[2*r-1] = 1
            else:
                sequence[r-1], sequence[2*r-1] = 1, parameter
                # The annihilating polynomial is t^r-parameter.
                assert all(sequence[k+r] == parameter*sequence[k]
                           for k in range(m-r))
            value = rank([[sequence[p+q] for q in range(b)] for p in range(a)])
            assert value == r
            ranks.append(value)
        answer.append({
            "a": a, "b": b, "rank": r, "sequence_length": m,
            "three_r": 3*r,
            "pencil": f"delta[{r-1}]+c*delta[{2*r-1}]",
            "parameters": [0, 1, 2, "infinity"],
            "hankel_ranks_mod_101": ranks,
            "finite_parameter_annihilator": f"t^{r}-c",
            "support_scheme_varies": True,
        })
    return answer


def report():
    return {
        "claim": "Exact controls for ordinary Hankel-symbol dimension obstruction",
        "binary_hankel_controls": binary_hankel_controls(),
        "hermite_interpolation_controls": hermite_controls(),
        "bounded_rank_pencil_controls": pencil_controls(),
        "variable_scheme_coordinate_projection": variable_scheme_projection_control(),
        "fixed_scheme_line_boundary_counterexamples": scheme_line_boundary_controls(),
        "ordinary_target_tests": [
            square_block_tests(5, 5, (14,)),
            square_block_tests(5, 6, (16,)),
            square_block_tests(5, 6, (16, 4)),
            square_block_tests(5, 6, (16, 3, 2, 1, 1)),
            square_block_tests(5, 6, (15, 4, 2, 1, 1)),
            square_block_tests(7, 8, (25, 5)),
        ],
        "singular_exclusion_claimed": False,
        "new_exponent_established": False,
    }


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[3]
    destination = root/"results/anisotropic-constructions-2026-10-20/hankel-symbol-dimension-controls.json"
    result = report()
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))

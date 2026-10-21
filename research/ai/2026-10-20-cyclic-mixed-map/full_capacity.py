"""Finite integer controls for the all-power triangular-minor argument."""
from fractions import Fraction
from itertools import product
import json
from math import isqrt
import random


def add(left, right):
    return tuple(x+y for x, y in zip(left, right))


def subtract(left, right):
    return tuple(x-y for x, y in zip(left, right))


def slice_entry(f, row, column):
    j, p, long_row = row
    long_column, q, t = column
    return f.get((subtract(long_column, j), add(p, q), subtract(long_row, t)), 0)


def triangular_minor(a, r, f):
    grid = list(product(range(a), repeat=r))
    base = 2*a-1
    u = [base**i for i in range(r)]
    v = [base**(r+i) for i in range(r)]

    def dot(weights, point):
        return sum(w*x for w, x in zip(weights, point))

    k0 = next(k for (i, k, s), value in sorted(f.items()) if value)
    i0, s0 = max(((i, s) for (i, k, s), value in f.items() if k == k0 and value),
                 key=lambda pair: dot(u, pair[0])+dot(v, pair[1]))
    p0 = tuple(min(k, a-1) for k in k0)
    q0 = subtract(k0, p0)
    pairs = sorted(product(grid, repeat=2), key=lambda pair: dot(u, pair[0])-dot(v, pair[1]))
    eta = [dot(u, j)-dot(v, t) for j, t in pairs]
    if len(set(eta)) != len(eta):
        raise AssertionError("Ordering weights collide")
    rows = [(j, p0, add(t, s0)) for j, t in pairs]
    columns = [(add(j, i0), q0, t) for j, t in pairs]
    matrix = [[slice_entry(f, row, col) for col in columns] for row in rows]
    pivot = f[i0, k0, s0]
    for i in range(len(matrix)):
        assert matrix[i][i] == pivot
        assert all(matrix[i][j] == 0 for j in range(i+1, len(matrix)))
    return {"rows": rows, "columns": columns, "matrix": matrix, "pivot": pivot}


def corner_support(a, r):
    """Expand the corner slice directly in its original six short indices."""
    grid = list(product(range(a), repeat=r))
    zero = (0,)*r
    # i=s=0 and p+q=0 force p=q=0; H=j and L=t remain free.
    return [((j, zero, t), (j, zero, t)) for j, t in product(grid, repeat=2)]


def direct_sum_marginals(sizes):
    dimension = sum(n*n for n in sizes)
    marginals = [[Fraction(0) for _ in range(dimension)] for _ in range(3)]
    offset = 0
    mass = Fraction(0)
    for n in sizes:
        weight = Fraction(1, dimension*n)
        for i, j, k in product(range(n), repeat=3):
            for axis, index in enumerate((i*n+j, j*n+k, k*n+i)):
                marginals[axis][offset+index] += weight
            mass += weight
        offset += n*n
    assert mass == 1
    assert all(value == Fraction(1, dimension) for marginal in marginals for value in marginal)
    return dimension


def report():
    seed = 202610360
    rng = random.Random(seed)
    cases = []
    for a, r in ((2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (4, 1), (5, 1)):
        grid = list(product(range(a), repeat=r))
        for _ in range(16):
            long = tuple(rng.randrange(2*a-1) for _ in range(r))
            f = {(i, long, s): rng.choice((-1, 0, 1)) for i, s in product(grid, repeat=2)}
            f[grid[0], long, grid[0]] = 1
            result = triangular_minor(a, r, f)
            assert abs(result["pivot"]) == 1
        support = corner_support(a, r)
        assert len(support) == a**(2*r)
        assert len({row for row, _ in support}) == len(support)
        assert len({column for _, column in support}) == len(support)
        cases.append({"a": a, "power": r, "integer_slices": 16,
                      "minor_size": a**(2*r), "corner_rank": len(support)})
    examples = []
    for a, r in ((2, 2), (5, 1), (4, 2)):
        dimension = (a*a*(2*a-1))**r
        n = isqrt(dimension)
        assert n*n == dimension and a**(2*r) > n
        examples.append({"a": a, "power": r, "leg_dimension": dimension,
                         "excluded_square_size": n, "minimum_source_slice_rank": a**(2*r)})
    return {
        "seed": seed, "triangular_minor_controls": cases,
        "integer_slices_checked": 16*len(cases),
        "direct_sum_uniform_marginal_controls": [
            {"sizes": sizes, "leg_dimension": direct_sum_marginals(sizes)}
            for sizes in ([2, 2, 2], [3, 1, 1, 1], [10, 2, 2, 2])],
        "full_capacity_examples": examples,
        "all_size_statement_status": "written proof, unreviewed",
        "external_invariant_theory_verified_by_this_program": False,
        "smaller_targets_excluded": False,
        "new_exponent_established": False,
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))

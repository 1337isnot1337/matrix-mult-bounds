"""Exact torus character budgets, allowing unequal vertex weight widths.

This is an optional SymPy discovery enumerator. It factors every possible
small-deficit character polynomial and reconstructs all nonnegative factors.
The central-slice screen is a necessary condition for ordinary restrictions.
It is not a condition for arbitrary singular degenerations.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, product
import json
from pathlib import Path
import time

import sympy as sp


def source_character(a, b):
    result = [1]
    for length in (a, b, a+b-1):
        updated = [0] * (len(result)+length-1)
        for i, coefficient in enumerate(result):
            for j in range(length):
                updated[i+j] += coefficient
        result = updated
    return result


def profile(weights):
    return tuple(sorted(Counter(weights).items()))


def compatible(first, second, source):
    radius = (len(source)-1)//2
    actual = Counter()
    for i, a in first:
        for j, b in second:
            actual[i-j] += a*b
    return all(-radius <= k <= radius and c <= source[k+radius]
               for k, c in actual.items())


def factor_pairs(poly, first_dimension, second_dimension, radius):
    """All pairs with first minimum weight zero before common translation."""
    x = poly.gen
    _, factors = sp.factor_list(poly)
    choices = []
    for factor, multiplicity in factors:
        value = abs(int(factor.eval(1)))
        # Any x factor belongs to the reversed second character, since the
        # first character has nonzero constant coefficient by normalization.
        if factor.nth(0) == 0:
            choices.append((0,))
        else:
            choices.append(tuple(e for e in range(multiplicity+1)
                                 if first_dimension % (value**e) == 0))
    for exponents in product(*choices):
        selected = sp.Poly(1, x)
        for (factor, _), exponent in zip(factors, exponents):
            selected *= factor**exponent
        value = int(selected.eval(1))
        if not value or first_dimension % value:
            continue
        selected *= first_dimension//value
        quotient, remainder = sp.div(poly, selected)
        if remainder or int(quotient.eval(1)) != second_dimension:
            continue
        if any(c.q != 1 or c < 0 for c in selected.all_coeffs()+quotient.all_coeffs()):
            continue
        first = tuple((i, int(selected.nth(i)))
                      for i in range(selected.degree()+1) if selected.nth(i))
        second = tuple(sorted((radius-i, int(quotient.nth(i)))
                              for i in range(quotient.degree()+1) if quotient.nth(i)))
        shift = second[0][0]
        # A common translation leaves all matrix-leg weights unchanged.
        yield (tuple((i-shift, c) for i, c in first),
               tuple((i-shift, c) for i, c in second))


def central_minimum(a, b):
    """Minimum degree of the exact central tight support."""
    degrees = []
    for i in range(a):
        for s in range(b):
            degree = sum(1 for j in range(b) for p in range(a)
                         if 0 <= i+s-p < b and
                         0 <= i+j-(i+s-p) < a)
            degrees.append(degree)
    return min(degrees)


def central_screen(vertices, source_zero_dimension, source_minimum):
    vectors = list(map(dict, vertices))
    edges = ((0, 1, 2), (1, 2, 0), (2, 0, 1))
    dimensions = [sum(c*vectors[j].get(w, 0) for w, c in vectors[i].items())
                  for i, j, _ in edges]
    defects = [source_zero_dimension-d for d in dimensions]
    minima = [min((vectors[k].get(w, 0) for w, c in vectors[i].items()
                   if c*vectors[j].get(w, 0)), default=0)
              for i, j, k in edges]
    slacks = [minima[i]-source_minimum+sum(defects[j] for j in range(3) if j != i)
              for i in range(3)]
    return {"target_dimensions": dimensions,
            "source_kernel_dimensions": defects,
            "target_minimum_slice_ranks": minima,
            "minimum_rank_slacks": slacks, "passes": min(slacks) >= 0}


def pair_search(a, b, first_dimension, second_dimension):
    source = source_character(a, b)
    radius = (len(source)-1)//2
    deficit = sum(source)-first_dimension*second_dimension
    if deficit < 0:
        return {}, 0
    x = sp.Symbol("x")
    base = sp.Poly.from_list(list(reversed(source)), x)
    by_second = defaultdict(set)
    valid = 0
    started = time.monotonic()
    for case, positions in enumerate(combinations_with_replacement(range(len(source)), deficit)):
        delta = Counter(positions)
        if any(c > source[i] for i, c in delta.items()):
            continue
        valid += 1
        poly = base-sp.Poly(sum(c*x**i for i, c in delta.items()), x)
        for first, second in factor_pairs(poly, first_dimension, second_dimension, radius):
            if not compatible(first, second, source):
                raise ArithmeticError("Factor pair failed its original coefficient budget")
            by_second[second].add(first)
        if case % 1000 == 0:
            print("case", case, "pairs", sum(map(len, by_second.values())),
                  "seconds", time.monotonic()-started, flush=True)
    return by_second, valid


def search(a, b, first_dimension, second_dimension):
    """Repeated first vertex dimension: target (first, first, second)."""
    source = source_character(a, b)
    by_second, valid = pair_search(a, b, first_dimension, second_dimension)
    triples = []
    minimum = central_minimum(a, b)
    for third, neighbors in sorted(by_second.items()):
        ordered = sorted(neighbors)
        for i, first in enumerate(ordered):
            for second in ordered[i:]:
                if compatible(first, second, source):
                    vertices = (first, second, third)
                    triples.append({"vertex_profiles": vertices,
                                    "central_screen": central_screen(vertices, a*b, minimum)})
    return {"source_lengths": [a, b],
            "target_shape": [first_dimension, first_dimension, second_dimension],
            "source_weight_multiplicities": source,
            "valid_deficit_polynomials": valid,
            "compatible_vertex_pairs": sum(map(len, by_second.values())),
            "distinct_second_vertex_profiles": len(by_second),
            "compatible_triples": triples,
            "source_central_minimum_slice_rank": minimum,
            "triples_passing_central_rank_screen": sum(t["central_screen"]["passes"] for t in triples),
            "constructed": False, "new_exponent_established": False}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", nargs=2, type=int, default=(4, 5))
    parser.add_argument("--vertices", nargs=2, type=int, default=(12, 13))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = search(*args.source, *args.vertices)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print({k: v for k, v in result.items() if k != "compatible_triples"})

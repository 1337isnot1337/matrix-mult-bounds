"""Exact controls for cyclic convolution slices and an unconstructed target."""
import argparse
from collections import Counter
from itertools import product
import json
from math import isqrt
from pathlib import Path
import random


def coefficient(f, a, i, k, s):
    if not (0 <= i < a and 0 <= k < 2*a-1 and 0 <= s < a):
        return 0
    return f[(i*(2*a-1)+k)*a+s]


def slice_entry(f, a, row, column):
    j, p, long_row = row
    long_column, q, r = column
    return coefficient(f, a, long_column-j, p+q, long_row-r)


def triangular_minor(f, a):
    k = next(k for k in range(2*a-1)
             if any(coefficient(f, a, i, k, s) for i in range(a) for s in range(a)))
    i = max(i for i in range(a)
            if any(coefficient(f, a, i, k, s) for s in range(a)))
    s = max(s for s in range(a) if coefficient(f, a, i, k, s))
    p, q = min(k, a-1), max(0, k-a+1)
    rows = [(j, p, r+s) for j in range(a) for r in range(a)]
    columns = [(j+i, q, r) for j in range(a) for r in range(a)]
    pivot = coefficient(f, a, i, k, s)
    matrix = [[slice_entry(f, a, row, column) for column in columns] for row in rows]
    for row, (j, r) in enumerate(product(range(a), repeat=2)):
        for col, (jp, rp) in enumerate(product(range(a), repeat=2)):
            if jp > j or (jp == j and r > rp):
                assert matrix[row][col] == 0
        assert matrix[row][row] == pivot
    return {"pivot": pivot, "minor_size": a*a, "matrix": matrix}


def rank_f2(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length()-1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def binary_slice_controls():
    a = 2
    rows = list(product(range(a), range(a), range(2*a-1)))
    columns = list(product(range(2*a-1), range(a), range(a)))
    counts = Counter()
    minimum_slices = set()
    for encoded in range(1, 1 << 12):
        f = [(encoded >> i) & 1 for i in range(12)]
        bit_rows = [sum(slice_entry(f, a, row, col) << j
                        for j, col in enumerate(columns)) for row in rows]
        rank = rank_f2(bit_rows)
        assert rank >= 4
        counts[rank] += 1
        if rank == 4:
            minimum_slices.add(encoded)
        minor = triangular_minor(f, a)
        assert rank_f2([sum(x << j for j, x in enumerate(row))
                        for row in minor["matrix"]]) == 4
    factored_slices = set()
    vectors = ((1, 0), (0, 1), (1, 1))
    hankel_vectors = ((1, 0, 0), (0, 0, 1), (1, 1, 1))
    for u, v, h in product(vectors, vectors, hankel_vectors):
        f = [u[i]*h[k]*v[s] for i in range(a) for k in range(2*a-1) for s in range(a)]
        factored_slices.add(sum(x << j for j, x in enumerate(f)))
    assert minimum_slices == factored_slices
    return {"a": a, "field": "F2", "nonzero_slices": sum(counts.values()),
            "minimum_rank": min(counts),
            "minimum_rank_classification_matches": True,
            "minimum_rank_encoded_slices": sorted(minimum_slices),
            "rank_distribution": {str(k): counts[k] for k in sorted(counts)}}


def seeded_minor_controls():
    seed = 202610203
    rng = random.Random(seed)
    count = 0
    for a in range(3, 9):
        for _ in range(20):
            f = [rng.randrange(-2, 3) for _ in range(a*a*(2*a-1))]
            result = triangular_minor(f, a)
            assert result["pivot"] != 0
            count += 1
    return {"seed": seed, "a_min": 3, "a_max": 8,
            "integer_slices_checked": count, "all_passed": True}


def improving_frontier(a):
    d = a*a*(2*a-1)
    records = []
    for l in range(2, isqrt(d)+1):
        for h in range(l, isqrt(d)+1):
            for n in range(h, d//h+1):
                volume = l*h*n
                if 216*volume <= (6*a-2)**4:
                    continue
                gaps = [2*d-a*a-v*(l+h+n-v-1) for v in (l, h, n)]
                locus_excludes = a >= 2 and any(
                    gap == 0 and l+h+n-v-2 > 2*a-1
                    for gap, v in zip(gaps, (l, h, n)))
                records.append({"shape": [l, h, n], "volume": volume,
                                "constant_restriction_slacks": gaps,
                                "minimum_slice_rank_excluded": min(gaps) < 0,
                                "minimum_rank_locus_excluded": locus_excludes,
                                "constant_restriction_excluded": min(gaps) < 0 or locus_excludes})
    return {"a": a, "source_leg_dimension": d, "source_minimum_slice_rank": a*a,
            "improving_sorted_shapes": records}


def report():
    lhs, rhs = 237600**281, 22**1125
    assert lhs > rhs
    return {"new_exponent_established": False, "independent_review": False,
        "finite_target": {"source": "cyclic product of three C(4,4)",
            "source_leg_dimensions": [112]*3, "source_border_rank_upper_bound": 343,
            "target_shape": [10, 10, 11], "target_leg_dimensions": [100, 110, 110],
            "constructed": False, "constant_linear_restriction_excluded": True,
            "general_degeneration_excluded": False,
            "conditional_rational_exponent": "281/125",
            "integer_certificate": "237600**281 > 22**1125",
            "integer_certificate_passes": lhs > rhs},
        "binary_slice_controls": binary_slice_controls(),
        "integer_minor_controls": seeded_minor_controls(),
        "frontiers": [improving_frontier(a) for a in range(1, 7)]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+"\n")
    print("Exact slice controls passed; the conditional target remains unconstructed.")

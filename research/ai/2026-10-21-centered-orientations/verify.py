"""Exact controls for costed, shared-input partial-transpose aggregation.

Only standard-library arithmetic is used.  The all-size claims are proved in
README.md; finite coefficient and orbit controls are not asymptotic proofs.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import product
import json
from pathlib import Path


EVEN3 = ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0))


def encode(v, s):
    ans = 0
    for x in v:
        ans = s * ans + x
    return ans


def transpose_coordinates(p, q, mask):
    return (
        tuple(q[i] if mask[i] else p[i] for i in range(len(p))),
        tuple(p[i] if mask[i] else q[i] for i in range(len(p))),
    )


def controlled_tensor(s, code=EVEN3):
    d = len(code[0])
    n = s**d
    ans = {}
    for p in product(range(s), repeat=d):
        for q in product(range(s), repeat=d):
            a = n * encode(p, s) + encode(q, s)
            for k, mask in enumerate(code):
                r, c = transpose_coordinates(p, q, mask)
                ans[a, k*n + encode(r, s), k*n + encode(c, s)] = 1
    return ans


def aggregate_and_corrections(s, code=EVEN3):
    """Expand each term of the displayed aggregate and each rank-one correction.

    A correction group is keyed by its ordered pair of channel indices and
    by the B/C coordinates it fixes. Its A factor is the sum over precisely
    the omitted scalar coordinates.  We independently form the controlled
    tensor in controlled_tensor(), rather than deleting mixed aggregate keys.
    """
    d = len(code[0])
    n = s**d
    aggregate = Counter()
    groups = defaultdict(list)
    for p in product(range(s), repeat=d):
        for q in product(range(s), repeat=d):
            a = n * encode(p, s) + encode(q, s)
            rc = [transpose_coordinates(p, q, mask) for mask in code]
            for k in range(len(code)):
                for ell in range(len(code)):
                    b = k*n + encode(rc[k][0], s)
                    c = ell*n + encode(rc[ell][1], s)
                    aggregate[a, b, c] += 1
                    if k != ell:
                        groups[k, ell, b, c].append(a)
    corrected = Counter(aggregate)
    group_counts = Counter()
    for (k, ell, b, c), a_factor in groups.items():
        group_counts[k, ell] += 1
        distance = sum(x != y for x, y in zip(code[k], code[ell]))
        assert len(a_factor) == s**distance
        assert len(set(a_factor)) == len(a_factor)
        for a in a_factor:
            corrected[a, b, c] -= 1
    corrected = {key: val for key, val in corrected.items() if val}
    expected = controlled_tensor(s, code)
    assert corrected == expected
    for k, ell in group_counts:
        h = sum(x != y for x, y in zip(code[k], code[ell]))
        assert group_counts[k, ell] == s**(2*d-h)
    return {
        "s": s,
        "outer_dimension": n,
        "aggregate_rank_one_terms": n*n,
        "expanded_aggregate_coefficients": len(aggregate),
        "correction_rank_one_terms": len(groups),
        "surviving_nonzero_coefficients": len(expected),
        "all_expanded_coefficients_verified": True,
    }


def gram_certificate(s, code=EVEN3):
    """Check scalar Gram matrices, including vanishing off-diagonal entries."""
    t = controlled_tensor(s, code)
    n = s**len(code[0])
    dims = (n*n, len(code)*n, len(code)*n)
    marginals = []
    for leg, dim in enumerate(dims):
        # Distinct support triples never have the same complementary pair.
        # Thus no cross term appears in this flattening's Gram matrix.
        complementary_keys = set()
        counts = Counter()
        for key in t:
            other = tuple(key[i] for i in range(3) if i != leg)
            assert other not in complementary_keys
            complementary_keys.add(other)
            counts[key[leg]] += 1
        assert set(counts) == set(range(dim))
        assert len(set(counts.values())) == 1
        marginals.append(next(iter(counts.values())))
    assert marginals == [len(code), n, n]
    return {"s": s, "format": list(dims), "gram_scalars": marginals}


def orbit_repair_rank(s, code=EVEN3):
    """Rank of the first flattening of T_code minus same-orientation MM.

    The kernel consists of coefficient arrays fixed by every partial
    transpose.  Each orbit gives one independent fixed coefficient.
    """
    d = len(code[0])
    points = list(product(range(s), repeat=2*d))
    unseen = set(points)
    orbit_sizes = Counter()
    while unseen:
        x = next(iter(unseen))
        orbit, queue = {x}, [x]
        while queue:
            u = queue.pop()
            for mask in code:
                p, q = transpose_coordinates(u[:d], u[d:], mask)
                v = p + q
                if v not in orbit:
                    orbit.add(v)
                    queue.append(v)
        unseen.difference_update(orbit)
        orbit_sizes[len(orbit)] += 1
    rank = s**(2*d) - sum(orbit_sizes.values())
    if code == EVEN3:
        assert rank == 3 * (s**6 - s**4) // 4
    return {"s": s, "first_flattening_rank": rank,
            "fixed_space_dimension": sum(orbit_sizes.values()),
            "orbit_counts": dict(sorted(orbit_sizes.items()))}


def sparse_product(a, b):
    ans = Counter()
    by_row = defaultdict(list)
    for (i, j), val in b.items():
        by_row[i].append((j, val))
    for (i, k), val in a.items():
        for j, v in by_row.get(k, ()):
            ans[i, j] += val*v
    return {key: val for key, val in ans.items() if val}


def partial_transpose_matrix(a, s, mask):
    d = len(mask)

    def decode(k):
        v = []
        for _ in range(d):
            v.append(k % s)
            k //= s
        return tuple(reversed(v))

    ans = {}
    for (i, j), val in a.items():
        p, q = transpose_coordinates(decode(i), decode(j), mask)
        ans[encode(p, s), encode(q, s)] = val
    return ans


def multiplication_witness(s):
    """X=E01 tensor I tensor I and Y=E10 tensor I tensor I."""
    assert s >= 2
    x, y = {}, {}
    for i, j in product(range(s), repeat=2):
        x[encode((0, i, j), s), encode((1, i, j), s)] = 1
        y[encode((1, i, j), s), encode((0, i, j), s)] = 1
    xy = sparse_product(x, y)
    mask = (1, 0, 1)
    product_of_blocks = sparse_product(partial_transpose_matrix(x, s, mask),
                                      partial_transpose_matrix(y, s, mask))
    block_of_product = partial_transpose_matrix(xy, s, mask)
    residual = Counter(product_of_blocks)
    residual.subtract(block_of_product)
    residual = {key: val for key, val in residual.items() if val}
    assert len(residual) == 2*s*s
    assert set(residual.values()) == {-1, 1}
    return {"s": s, "mask": list(mask), "nonzero_residual_entries": len(residual),
            "sample": [list(key) + [val] for key, val in sorted(residual.items())[:4]]}


def factor_source_certificate(s):
    """Independent six-factor source D_s^{tensor 6} -> the K4 tensor.

    D_s=sum_i a_i(b_i c_*+b_* c_i).  Select B patterns that are K4
    stars, and complementary C patterns.  The selected support terms are
    exactly the four channels, with every coefficient equal to one.
    """
    n = s**3
    patterns = []
    for mask in EVEN3:
        patterns.append(tuple(i if not mask[i] else i+3 for i in range(3)))
    selected = {frozenset(p): k for k, p in enumerate(patterns)}
    selected_c = {frozenset(set(range(6)) - set(p)): k
                  for k, p in enumerate(patterns)}
    support = {}
    for indices in product(range(s), repeat=6):
        p, q = indices[:3], indices[3:]
        a = n*encode(p, s)+encode(q, s)
        for orient in product((0, 1), repeat=6):
            b_set = frozenset(i for i in range(6) if orient[i] == 0)
            c_set = frozenset(i for i in range(6) if orient[i] == 1)
            if b_set not in selected or c_set not in selected_c:
                continue
            k = selected[b_set]
            assert selected_c[c_set] == k
            r, c = transpose_coordinates(p, q, EVEN3[k])
            support[a, k*n+encode(r, s), k*n+encode(c, s)] = 1
    assert support == controlled_tensor(s)
    return {"s": s, "source_factors": 6, "source_terms_before_restriction": 64*s**6,
            "selected_nonzero_coefficients": len(support),
            "character_upper_bound": "(s^p_B+s^p_C)^6",
            "balanced_endpoint_coefficient": 64}


def certificate():
    return {
        "status": "exact finite controls for written all-size identities; no exponent improvement",
        "coefficients": [aggregate_and_corrections(s) for s in (2, 3, 4)],
        "exact_grams": [gram_certificate(s) for s in (2, 3, 4)],
        "literal_orientation_repair": [orbit_repair_rank(s) for s in (2, 3, 4)],
        "normalized_slice_algebra_witnesses": [multiplication_witness(s) for s in (2, 3, 4)],
        "separate_character_source": [factor_source_certificate(s) for s in (2, 3)],
        "Q_source_map_supplied": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(certificate(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    else:
        print(payload, end="")

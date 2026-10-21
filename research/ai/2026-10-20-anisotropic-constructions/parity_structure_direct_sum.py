"""Integral restrictions A(a,a) -> M(2a-2) direct sum M(a-2).

The construction is exact and applies to the full source, not its parity
degeneration.  It is a control family, not an exponent improvement.
"""

from itertools import product
import json
from pathlib import Path

import numpy as np

from parity_structure import apply_sparse, source_coordinates, source_tensor


def factor_maps(a):
    if a < 3:
        raise ValueError("a must be at least three")
    d = a-1
    u = np.zeros((2, a), dtype=np.int64)
    u[0, 0] = 1
    u[1, 0], u[1, d] = -1, 1
    v = np.zeros((d, a), dtype=np.int64)
    for j in range(1, d):
        v[j-1, j] = 1
    v[d-1, 0], v[d-1, d] = -1, 1
    r = np.zeros((2*d, 2*d+1), dtype=np.int64)
    for j in range(1, d):
        r[j-1, j] = r[j-1, j+d] = 1
        r[d+j-1, j+d] = 1
    r[d-1, d], r[d-1, 2*d] = 1, 2
    r[2*d-1, 2*d] = 1
    h = np.zeros(2*d+1, dtype=np.int64)
    h[0] = h[d] = h[2*d] = 1
    products = np.stack([np.convolve(x, y) for x, y in product(u, v)], axis=1)
    assert np.array_equal(r @ products, np.eye(2*d, dtype=np.int64))
    assert not np.any(h @ products)
    extended = np.column_stack((products, np.eye(2*d+1, dtype=np.int64)[:, 0]))
    inverse = np.vstack((r, h))
    assert np.array_equal(inverse @ extended, np.eye(2*d+1, dtype=np.int64))
    assert np.array_equal(extended @ inverse, np.eye(2*d+1, dtype=np.int64))
    hankel = np.array([[h[i+j] for j in range(a)] for i in range(a)])
    p = np.eye(a, dtype=np.int64)[1:d]
    q = p[::-1].copy()
    assert np.array_equal(p @ hankel @ q.T, np.eye(d-1, dtype=np.int64))
    assert not np.any(u @ hankel @ v.T)
    assert not np.any(u @ hankel @ q.T)
    return u, v, r, h, p, q


def restriction_maps(a=5, add_scalar=False):
    u, v, r, h, p, q = factor_maps(a)
    d, m = a-1, 2*a-1
    core, small = 2*d, d-1
    dimension = a*a*m
    target = core*core + small*small + int(add_scalar)
    maps = [np.zeros((target, dimension), dtype=np.int64) for _ in range(3)]
    coordinates = source_coordinates(a, a)
    for a1, b2, a2, b3 in product(range(2), range(d), range(2), range(d)):
        row = core*(d*a1+b2)+(d*a2+b3)
        for col, (i, t, s) in enumerate(coordinates[0]):
            maps[0][row, col] = u[a1, i]*r[d*a2+b2, t]*v[b3, s]
    for a2, b3, a3, b1 in product(range(2), range(d), range(2), range(d)):
        row = core*(d*a2+b3)+(d*a3+b1)
        for col, (j, k, t) in enumerate(coordinates[1]):
            maps[1][row, col] = v[b1, j]*u[a2, k]*r[d*a3+b3, t]
    for a3, b1, a1, b2 in product(range(2), range(d), range(2), range(d)):
        row = core*(d*a3+b1)+(d*a1+b2)
        for col, (t, j, k) in enumerate(coordinates[2]):
            maps[2][row, col] = r[d*a1+b1, t]*v[b2, j]*u[a3, k]

    offset = core*core
    for i, j in product(range(small), repeat=2):
        row = offset+small*i+j
        for col, (ii, t, ss) in enumerate(coordinates[0]):
            maps[0][row, col] = p[j, ii]*h[t]*q[i, ss]
    for j, k in product(range(small), repeat=2):
        row = offset+small*j+k
        for col, (jj, pp, t) in enumerate(coordinates[1]):
            maps[1][row, col] = q[j, jj]*p[k, pp]*h[t]
    for k, i in product(range(small), repeat=2):
        row = offset+small*k+i
        for col, (t, qq, rr) in enumerate(coordinates[2]):
            maps[2][row, col] = h[t]*q[k, qq]*p[i, rr]

    if add_scalar:
        for col, (i, t, s) in enumerate(coordinates[0]):
            maps[0][-1, col] = int(i == 0 and s == 0)*h[t]
        for col, (j, p0, t) in enumerate(coordinates[1]):
            maps[1][-1, col] = int(j == 0 and p0 == 0)*h[t]
        for col, (t, q0, r0) in enumerate(coordinates[2]):
            maps[2][-1, col] = int(q0 == 0 and r0 == 0)*h[t]
    return maps


def direct_sum_tensor(sizes):
    result = {}
    offset = 0
    for n in sizes:
        for i, j, k in product(range(n), repeat=3):
            result[offset+n*i+j, offset+n*j+k, offset+n*k+i] = 1
        offset += n*n
    return result


def verify(a=5):
    source = source_tensor(a, a)
    maps = restriction_maps(a)
    core, small = 2*a-2, a-2
    expected = direct_sum_tensor([core, small])
    actual = apply_sparse(source, maps)
    assert actual == expected

    # A tempting additional scalar is not independent: verify that failure
    # explicitly, so it cannot be mistaken for a larger direct-sum witness.
    extra_maps = restriction_maps(a, add_scalar=True)
    extra_actual = apply_sparse(source, extra_maps)
    extra_expected = direct_sum_tensor([core, small, 1])
    mixed = {point: value for point, value in extra_actual.items()
             if point not in extra_expected}
    wrong = {point: (extra_actual.get(point, 0), value)
             for point, value in extra_expected.items()
             if extra_actual.get(point, 0) != value}
    assert not wrong and mixed
    return {
        "claim": "Exact ordinary restriction of full A(a,a); no exponent improvement",
        "a": a, "source_format": [a*a*(2*a-1)]*3,
        "target_blocks": [core, small],
        "target_format": [core*core+small*small]*3,
        "source_terms": len(source), "target_terms": len(actual),
        "all_coefficients_verified_exactly": True,
        "map_nonzero_counts": [int(np.count_nonzero(x)) for x in maps],
        "map_entry_set": sorted({int(v) for x in maps for v in np.unique(x)}),
        "additional_scalar_is_not_a_direct_sum": True,
        "additional_scalar_mixed_term_count": len(mixed),
        "additional_scalar_first_mixed_term": [list(min(mixed)), mixed[min(mixed)]],
    }


if __name__ == "__main__":
    reports = [verify(a) for a in (3, 4, 5, 6)]
    destination = Path(__file__).with_name("parity_structure_direct_sum_certificate.json")
    destination.write_text(json.dumps(reports, indent=2)+"\n")
    aa, bb, cc = restriction_maps(5)
    u, v, r, h, p, q = factor_maps(5)
    np.savez_compressed(Path(__file__).with_name("parity_structure_direct_sum_maps.npz"),
                        A=aa, B=bb, C=cc, U=u, V=v, R=r, h=h, P=p, Q=q)
    print(json.dumps(reports, indent=2))

"""Integer controls for three fixed length-two long-coordinate spaces."""

from itertools import product
import json
from pathlib import Path

import numpy as np

from hankel_symbol_dimension import jet, rank


def long_plane(a, b, kind, points):
    if kind == "secant":
        if len(points) != 2 or points[0] == points[1]:
            raise ValueError("a secant needs two distinct points")
        long = np.array([jet(a+b-2, t, 0) for t in points], dtype=np.int64)
        left = np.array([jet(a-1, t, 0) for t in points], dtype=np.int64)
        right = np.array([jet(b-1, t, 0) for t in points], dtype=np.int64)
        core = np.zeros((2, 2, 2), dtype=np.int64)
        core[0, 0, 0] = core[1, 1, 1] = 1
    elif kind == "tangent":
        if len(points) != 1:
            raise ValueError("a tangent needs one point")
        t = points[0]
        long = np.array([jet(a+b-2, t, j) for j in (0, 1)], dtype=np.int64)
        left = np.array([jet(a-1, t, j) for j in (0, 1)], dtype=np.int64)
        right = np.array([jet(b-1, t, j) for j in (0, 1)], dtype=np.int64)
        core = np.zeros((2, 2, 2), dtype=np.int64)
        core[0, 0, 0] = core[1, 0, 1] = core[1, 1, 0] = 1
    else:
        raise ValueError("unknown plane kind")
    hankel = np.array([[[row[p+q] for q in range(b)] for p in range(a)]
                       for row in long], dtype=np.int64)
    separated = np.einsum("Aur,up,rq->Apq", core, left, right)
    assert np.array_equal(hankel, separated)
    return long, left, right, core, hankel


def factorization_control(a, b, specifications):
    data = [long_plane(a, b, *specification) for specification in specifications]
    (_, ux, vx, lx, hx), (_, uy, vy, ly, hy), (_, uz, vz, lz, hz) = data
    dimension = 2*a*b
    actual = np.einsum("Apq,Brs,Cij->AisBjpCqr", hx, hy, hz).reshape((dimension,)*3)
    small = np.einsum("Auv,Bwz,Ctl->AtzBluCvw", lx, ly, lz).reshape((8,)*3)
    ex, ey, ez = [np.zeros((dimension, 8), dtype=np.int64) for _ in range(3)]
    for alpha, i, s, t, z in product(range(2), range(a), range(b), range(2), range(2)):
        ex[(alpha*a+i)*b+s, (alpha*2+t)*2+z] = uz[t, i]*vy[z, s]
    for beta, j, p, ell, u in product(range(2), range(b), range(a), range(2), range(2)):
        ey[(beta*b+j)*a+p, (beta*2+ell)*2+u] = vz[ell, j]*ux[u, p]
    for gamma, q, r, v, w in product(range(2), range(b), range(a), range(2), range(2)):
        ez[(gamma*b+q)*a+r, (gamma*2+v)*2+w] = vx[v, q]*uy[w, r]
    reconstructed = np.einsum("xu,yv,zw,uvw->xyz", ex, ey, ez, small, optimize=True)
    assert np.array_equal(actual, reconstructed)
    leg_ranks = [rank(factor.tolist()) for factor in (ex, ey, ez)]
    core_ranks = [rank(np.moveaxis(small, leg, 0).reshape(8, -1).tolist())
                  for leg in range(3)]
    assert leg_ranks == core_ranks == [8, 8, 8]
    return {
        "a": a, "b": b,
        "long_planes": [{"kind": kind, "points": ["infinity" if p is None else p for p in points]}
                        for kind, points in specifications],
        "restricted_format": [dimension]*3, "factor_format": [8]*3,
        "integer_coefficients_compared": int(actual.size),
        "all_coefficients_match_integer_factorization": True,
        "factor_ranks_mod_101": leg_ranks, "core_flattening_ranks_mod_101": core_ranks,
    }


def equality_block_screen(a, b, n, total_dimension):
    source = a*b*(a+b-1)
    if n*n > total_dimension or total_dimension > source:
        raise ValueError("invalid target dimension")
    hypothesis = min(a, b) >= 3 and a+b-2 >= 5
    lifted_rank = n+2*(source-total_dimension)
    return {
        "a": a, "b": b, "block_size": n, "total_target_leg_dimension": total_dimension,
        "lemma_hypotheses_hold": hypothesis,
        "lifted_rank_one_slice_upper_bound": lifted_rank,
        "equality_threshold": 2*a*b,
        "ordinary_restriction_excluded": hypothesis and n*n > 8 and lifted_rank <= 2*a*b,
        "singular_degeneration_excluded": False,
    }


def report():
    secant = ("secant", (0, 1))
    endpoint_secant = ("secant", (0, None))
    zero = ("tangent", (0,))
    one = ("tangent", (1,))
    infinity = ("tangent", (None,))
    specifications = [
        (secant,)*3, (zero,)*3, (one,)*3, (infinity,)*3,
        (endpoint_secant, zero, one), (infinity, secant, zero),
    ]
    return {
        "claim": "Exact eight-coordinate factorization for three fixed length-two long spaces",
        "factorization_controls": [factorization_control(5, 6, row) for row in specifications],
        "ordinary_equality_tests": [
            equality_block_screen(5, 6, 4, 272),
            equality_block_screen(5, 6, 3, 271),
            equality_block_screen(5, 6, 2, 271),
            equality_block_screen(3, 3, 3, 45),
        ],
        "singular_exclusion_claimed": False, "new_exponent_established": False,
    }


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[3]
    destination = root/"results/anisotropic-constructions-2026-10-20/hankel-rank-two-controls.json"
    result = report()
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))

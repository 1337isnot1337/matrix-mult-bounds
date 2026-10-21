"""Standard-library integer controls for fixed length-two long spaces."""

from itertools import product
import json
from pathlib import Path

from hankel_symbol_dimension import jet, rank


def long_plane(a, b, kind, points):
    if kind == "secant":
        if len(points) != 2 or points[0] == points[1]:
            raise ValueError("a secant needs two distinct points")
        long = [jet(a+b-2, t, 0) for t in points]
        left = [jet(a-1, t, 0) for t in points]
        right = [jet(b-1, t, 0) for t in points]
        core = [[[0]*2 for _ in range(2)] for _ in range(2)]
        core[0][0][0] = core[1][1][1] = 1
    elif kind == "tangent":
        if len(points) != 1:
            raise ValueError("a tangent needs one point")
        t = points[0]
        long = [jet(a+b-2, t, j) for j in (0, 1)]
        left = [jet(a-1, t, j) for j in (0, 1)]
        right = [jet(b-1, t, j) for j in (0, 1)]
        core = [[[0]*2 for _ in range(2)] for _ in range(2)]
        core[0][0][0] = core[1][0][1] = core[1][1][0] = 1
    else:
        raise ValueError("unknown plane kind")
    hankel = [[[row[p+q] for q in range(b)] for p in range(a)]
              for row in long]
    for alpha, p, q in product(range(2), range(a), range(b)):
        separated = sum(core[alpha][u][v]*left[u][p]*right[v][q]
                        for u, v in product(range(2), repeat=2))
        assert hankel[alpha][p][q] == separated
    return long, left, right, core, hankel


def factorization_control(a, b, specifications):
    data = [long_plane(a, b, *specification) for specification in specifications]
    (_, ux, vx, lx, hx), (_, uy, vy, ly, hy), (_, uz, vz, lz, hz) = data
    dimension = 2*a*b
    # The three core indices have orders (alpha,t,z), (beta,ell,u),
    # and (gamma,v,w), respectively.  Keep all coefficients as Python
    # integers; neither a numerical package nor fixed-width arithmetic
    # is needed for this finite identity.
    coordinates = list(product(range(2), repeat=3))
    small = [[[lx[alpha][u][v]*ly[beta][w][z]*lz[gamma][t][ell]
               for gamma, v, w in coordinates]
              for beta, ell, u in coordinates]
             for alpha, t, z in coordinates]
    core_terms = [(u, v, w, small[u][v][w])
                  for u, v, w in product(range(8), repeat=3)
                  if small[u][v][w]]
    ex, ey, ez = [[[0]*8 for _ in range(dimension)] for _ in range(3)]
    for alpha, i, s, t, z in product(range(2), range(a), range(b), range(2), range(2)):
        ex[(alpha*a+i)*b+s][(alpha*2+t)*2+z] = uz[t][i]*vy[z][s]
    for beta, j, p, ell, u in product(range(2), range(b), range(a), range(2), range(2)):
        ey[(beta*b+j)*a+p][(beta*2+ell)*2+u] = vz[ell][j]*ux[u][p]
    for gamma, q, r, v, w in product(range(2), range(b), range(a), range(2), range(2)):
        ez[(gamma*b+q)*a+r][(gamma*2+v)*2+w] = vx[v][q]*uy[w][r]
    x_coordinates = list(product(range(2), range(a), range(b)))
    y_coordinates = list(product(range(2), range(b), range(a)))
    z_coordinates = y_coordinates
    compared = 0
    for x, (alpha, i, s) in enumerate(x_coordinates):
        for y, (beta, j, p) in enumerate(y_coordinates):
            # Contract the first two factors with the small core once,
            # then compare every coefficient on the complete third leg.
            partial = [0]*8
            for u, v, w, coefficient in core_terms:
                partial[w] += coefficient*ex[x][u]*ey[y][v]
            nonzero = [(w, value) for w, value in enumerate(partial) if value]
            for z, (gamma, q, r) in enumerate(z_coordinates):
                reconstructed = sum(value*ez[z][w] for w, value in nonzero)
                actual = hx[alpha][p][q]*hy[beta][r][s]*hz[gamma][i][j]
                assert reconstructed == actual
                compared += 1
    assert compared == dimension**3
    leg_ranks = [rank(factor) for factor in (ex, ey, ez)]
    core_flattenings = [
        [[small[u][v][w] for v, w in product(range(8), repeat=2)] for u in range(8)],
        [[small[u][v][w] for u, w in product(range(8), repeat=2)] for v in range(8)],
        [[small[u][v][w] for u, v in product(range(8), repeat=2)] for w in range(8)],
    ]
    core_ranks = [rank(flattening) for flattening in core_flattenings]
    assert leg_ranks == core_ranks == [8, 8, 8]
    return {
        "a": a, "b": b,
        "long_planes": [{"kind": kind, "points": ["infinity" if p is None else p for p in points]}
                        for kind, points in specifications],
        "restricted_format": [dimension]*3, "factor_format": [8]*3,
        "integer_coefficients_compared": compared,
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

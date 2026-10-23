"""Independent finite controls for the pinned divisor-cap proof review.

No code from the reviewed package is imported. These are finite controls,
not a proof of the all-size statement. Run from any working directory.
"""
from itertools import combinations, product
import json

import sympy as s


def biform(a, terms):
    """Read the literal coefficient rule, including zero output padding."""
    return s.Matrix([
        [terms.get((height-j, ell-r), 0)
         for height in range(2*a-1) for r in range(a)]
        for j in range(a) for ell in range(2*a-1)
    ])


def orbit_controls():
    records = []
    for a in range(2, 7):
        for d in range(1, a):
            if a % d:
                continue
            # Construct every orbit from every starting point, then deduplicate.
            # This differs from the reviewed package's unseen-set traversal.
            orbits = {tuple(sorted(((i+t*d) % a, (j+t*d) % a)
                                   for t in range(a//d)))
                      for i, j in product(range(a), repeat=2)}
            assert len(orbits) == a*d
            covered = [point for orbit in orbits for point in orbit]
            assert len(covered) == len(set(covered)) == a*a
            ranks = []
            for orbit in sorted(orbits):
                for first, second in combinations(orbit, 2):
                    # Unequal coefficients also check that a cancellation in a
                    # wrapped pair is not hidden by the all-one control.
                    actual = int(biform(a, {first: 1, second: -2}).to_DM().rank())
                    assert actual >= a*(a+d), (a, d, first, second, actual)
                    ranks.append(actual)
            records.append({"a": a, "d": d, "orbits": len(orbits),
                            "pairs": len(ranks), "minimum_pair_rank": min(ranks),
                            "required_rank": a*(a+d)})
    return records


def torus_controls():
    counts = []
    for a in range(2, 7):
        middle = 2*a-1
        weights = {i+a*k+a*middle*ell for i, k, ell in
                   product(range(a), range(middle), range(a))}
        assert weights == set(range(a*a*middle))
        checked = 0
        for i, k, ell in product(range(a), range(middle), range(a)):
            for j, b, r in product(range(a), repeat=3):
                c = k-b
                if not 0 <= c < a:
                    continue
                height, output = i+j, ell+r
                row_weight = -j+a*b+a*middle*output
                col_weight = height+a*c-a*middle*r
                assert row_weight+col_weight == i+a*k+a*middle*ell
                checked += 1
        counts.append({"a": a, "source_weights": len(weights),
                       "coefficient_identities": checked})
    return counts


def pole_control():
    t = s.Symbol("t", nonzero=True)
    b = s.Matrix([[1/t, 0, 1], [0, 1, 0]])
    d = s.Matrix([[t, 0], [0, 1], [0, 0]])
    z = s.Matrix([[2, 4], [3, 6]])
    kernel = s.Matrix([-t, 0, 1])
    w = kernel*s.Matrix([[1, 2]])
    y = d*z+w
    projection = s.eye(3)-d*b
    assert b*d == s.eye(2)
    assert s.simplify(b*y-z) == s.zeros(2)
    assert projection.rank() == 1
    assert s.simplify(projection*y-w) == s.zeros(3, 2)
    assert all(s.denom(s.cancel(x)) == 1 for x in y)
    assert w.subs(t, 0).rank() == 1

    # Make the projection itself polar while preserving BD=I and the
    # regularity of the particular Y, D, Z and W being specialized.
    b = s.Matrix([[1/t, 1/t, 0], [0, 0, 1]])
    d = s.Matrix([[t-1, 0], [1, 0], [0, 1]])
    w = s.Matrix([-1, 1, 0])*s.Matrix([[1, 2]])
    y = d*z+w
    projection = s.eye(3)-d*b
    assert s.simplify(b*d-s.eye(2)) == s.zeros(2)
    assert any(s.denom(s.cancel(x)) != 1 for x in projection)
    assert all(s.denom(s.cancel(x)) == 1 for x in y)
    assert s.simplify(b*y-z) == s.zeros(2)
    assert s.simplify(y-d*z-w) == s.zeros(3, 2)
    assert s.simplify(projection*y-w) == s.zeros(3, 2)
    assert projection.rank() == w.subs(t, 0).rank() == 1
    return {"regular_projection_case": True, "polar_projection_case": True,
            "regular_correction_rank_at_zero": 1,
            "scope": "Linear-algebra controls, not source degenerations"}


def boundary_controls():
    # The proof explicitly leaves this nondivisor pair outside its argument.
    actual = int(biform(5, {(0, 0): 1, (2, 2): 1}).to_DM().rank())
    assert actual == 34 < 5*(5+2)
    cutoffs = [c for c in range(11)
               if 10 > 4*2 and 11+2*2+c < 4*(4+2) and 4**2 > 3*2+c]
    assert cutoffs == list(range(9))
    return {"nondivisor_pair_rank": actual, "a4_excluded_coranks": cutoffs}


def audit():
    return {"scope": "Finite internal audit; no independent review or exponent gain",
            "torus": torus_controls(), "divisor_pairs": orbit_controls(),
            "laurent": pole_control(), "boundaries": boundary_controls()}


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))

"""Explicit scalar repairs saving one term in the one-dependency family.

For b>=2 and n=b+2, the product-oblique residual for Q(n,b) -> M(n-1,4,n-1)
has a rank-one decomposition with 4*(n-1)-1 terms. At n=6,b=4 this costs19.
The construction uses only integer coefficients and is valid over every
field. It is an upper bound, not an assertion that the tensor rank is19.
"""

from itertools import product


def _add(first, second, scale=1):
    result = dict(first)
    for key, value in second.items():
        updated = result.get(key, 0) + scale * value
        if updated:
            result[key] = updated
        else:
            result.pop(key, None)
    return result


def _record(a, b, c):
    return {"a": [[i, x] for i, x in sorted(a.items()) if x],
            "b": [[i, x] for i, x in sorted(b.items()) if x],
            "c": [[i, x] for i, x in sorted(c.items()) if x]}


def one_dependency_terms(n, b):
    """Seven core terms and 4*(r-2) other terms, r=n-1.

    Let s=b-1, the sole bad outer coordinate; its shift neighbor is zero.
    Write u=A_(s,0), v=A_(0,s), w=A_(s,s) and

      X=B_(s,0)-B_(0,1), Z=B_(s,2)-B_(0,3),
      a=B_(0,0), d=B_(0,1), y=B_(s,1),
      P=C_(0,0), Q=C_(2,0), R=C_(0,s)-C_(2,0),
      S=C_(1,s)-C_(3,0), T=C_(2,s).

    The core is
      u*(X*P+Z*Q) + v*(a*R+d*S)
        + w*(X*Q+Z*T+d*R+y*S+X*R).
    Its first and second binary-convolution parts each have rank at most
    three by the displayed Karatsuba terms below; w*X*R is the seventh.
    """
    if type(n) is not int or type(b) is not int or b < 2 or n != b + 2:
        raise ValueError("Require integer b>=2 and n=b+2.")
    r, s = n - 1, b - 1
    u, v, w = {r * s: 1}, {s: 1}, {r * s + s: 1}
    xx = {4 * s: 1, 1: -1}
    zz = {4 * s + 2: 1, 3: -1}
    aa, dd, yy = {0: 1}, {1: 1}, {4 * s + 1: 1}
    pp, qq = {0: 1}, {2 * r: 1}
    rr = {s: 1, 2 * r: -1}
    ss = {r + s: 1, 3 * r: -1}
    tt = {2 * r + s: 1}
    terms = [
        _record(_add(u, w), _add(xx, zz), qq),
        _record(u, xx, _add(pp, qq, -1)),
        _record(w, zz, _add(tt, qq, -1)),
        _record(_add(v, w), dd, _add(rr, ss)),
        _record(v, _add(aa, dd, -1), rr),
        _record(w, _add(yy, dd, -1), ss),
        _record(w, xx, rr),
    ]
    for j in range(r):
        if j in (0, s):
            continue
        terms.extend([
            _record({r * s + j: 1}, xx, {j: 1}),
            _record({r * s + j: 1}, zz, {2 * r + j: 1}),
            _record({r * j + s: 1}, {4 * j: 1}, rr),
            _record({r * j + s: 1}, {4 * j + 1: 1}, ss),
        ])
    if len(terms) != 4 * r - 1:
        raise ArithmeticError("The explicit Karatsuba term count changed.")
    return terms


def expand_terms(terms):
    """Replay all rank-one terms exactly in the standard target basis."""
    output = {}
    for term in terms:
        for (a, x), (b, y), (c, z) in product(
            term["a"], term["b"], term["c"]
        ):
            key = (a, b, c)
            output[key] = output.get(key, 0) + x * y * z
    return {key: value for key, value in output.items() if value}


def certificate(n, b, expected_residual):
    terms = one_dependency_terms(n, b)
    if expand_terms(terms) != expected_residual:
        raise ArithmeticError("The full Karatsuba scalar repair did not replay.")
    return {"rank_one_terms": terms,
            "scalar_rank_upper_bound": len(terms),
            "core_rank_one_terms": 7,
            "remaining_rank_one_terms": len(terms) - 7,
            "coefficient_field": "Z (identity remains valid over every field)",
            "complete_decomposition_replayed": True,
            "tensor_rank_optimality_claimed": False}

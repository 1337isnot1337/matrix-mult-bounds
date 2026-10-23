"""Exact finite controls for the formal channel-separation proof.

No discovery solver is imported. Polynomial keys are (X degree,Y degree,t
degree); negative t degrees are retained. Modular ranks are exact finite
specializations, not certificates for the general formal theorem.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def clean(p):
    return {e: c for e, c in p.items() if c}


def add(*polys):
    out = defaultdict(int)
    for p in polys:
        for e, c in p.items():
            out[e] += c
    return clean(out)


def scale(p, c):
    return clean({e: c * v for e, v in p.items()})


def mul(p, q):
    out = defaultdict(int)
    for a, x in p.items():
        for b, y in q.items():
            out[tuple(u + v for u, v in zip(a, b))] += x * y
    return clean(out)


def mono(c=1, x=0, y=0, t=0):
    return {(x, y, t): c} if c else {}


def shift(p, x=0, y=0, t=0):
    return mul(p, mono(x=x, y=y, t=t))


def evaluate(p, *, prime, tv, xv=1, yv=1):
    return sum(c * pow(xv, x, prime) * pow(yv, y, prime)
               * pow(tv, t, prime) for (x, y, t), c in p.items()) % prime


def rank_mod(rows, prime):
    basis = {}
    for original in rows:
        row = {j: x % prime for j, x in original.items() if x % prime}
        while row:
            pivot = min(row)
            if pivot not in basis:
                inv = pow(row[pivot], -1, prime)
                basis[pivot] = {j: x * inv % prime for j, x in row.items()}
                break
            factor = row[pivot]
            for j, x in basis[pivot].items():
                value = (row.get(j, 0) - factor * x) % prime
                if value:
                    row[j] = value
                else:
                    row.pop(j, None)
    return len(basis)


def determinant_two(a):
    return add(mul(a[0][0], a[1][1]), scale(mul(a[0][1], a[1][0]), -1))


def matrix_scale(a, p):
    return [[mul(x, p) for x in row] for row in a]


def matrix_add(a, b):
    return [[add(x, y) for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def contract(slices, weights):
    out = [[{}, {}], [{}, {}]]
    for a, w in zip(slices, weights):
        out = matrix_add(out, matrix_scale(a, w))
    return out


def matrix_flat_rows(slices, prime=101, tv=2):
    keys = sorted({(a, b, x, y) for sl in slices for a in range(2)
                   for b in range(2) for x, y, _ in sl[a][b]})
    index = {key: i for i, key in enumerate(keys)}
    rows = []
    for sl in slices:
        row = defaultdict(int)
        for a in range(2):
            for b in range(2):
                for (x, y, t), c in sl[a][b].items():
                    row[index[a, b, x, y]] += c * pow(tv, t, prime)
        rows.append(dict(row))
    return rows


def formal_controls():
    one, zero = mono(), {}
    identity = [[one, zero], [zero, one]]
    rank_one = [[mono(t=-1), one], [one, mono(t=1)]]
    assert not determinant_two(rank_one)
    raw_constant = [[{e: c for e, c in p.items() if e[2] == 0}
                     for p in row] for row in rank_one]
    assert determinant_two(raw_constant) == mono(-1)

    # A moving V=ker(w0+t*w1), with two-dimensional auxiliary image.
    # S(w)=(w0+t*w1)I+((X-t)w1+Y*w2)rank_one.
    # E(w)=((X-t)w1+Y*w2)(I-rank_one); S+E=M identically.
    x_minus_t = add(mono(x=1), mono(-1, t=1))
    y = mono(y=1)
    difference = matrix_add(identity, matrix_scale(rank_one, mono(-1)))
    source = [identity,
              matrix_add(matrix_scale(identity, mono(t=1)),
                         matrix_scale(rank_one, x_minus_t)),
              matrix_scale(rank_one, y)]
    auxiliary = [matrix_scale(identity, zero),
                 matrix_scale(difference, x_minus_t),
                 matrix_scale(difference, y)]
    target = [identity, matrix_scale(identity, mono(x=1)),
              matrix_scale(identity, y)]
    for s, e, m in zip(source, auxiliary, target):
        assert matrix_add(s, e) == m
    v1 = [mono(-1, t=1), one, zero]
    v2 = [zero, zero, one]
    assert not determinant_two(contract(source, v1))
    assert not determinant_two(contract(source, v2))
    assert not determinant_two(contract(source, [mono(-2, t=1), mono(2), mono(3)]))
    assert any(t < 0 for sl in source for row in sl for p in row for _, _, t in p)
    assert any(t < 0 for sl in auxiliary for row in sl for p in row for _, _, t in p)
    rank = rank_mod(matrix_flat_rows(auxiliary), 101)
    assert rank == 2

    # Dropping one auxiliary direction leaves v2 in its exact kernel.
    # The resulting source contraction is Y*I, violating low channel rank.
    smaller_aux = auxiliary[:2] + [matrix_scale(identity, zero)]
    modified_source = [matrix_add(m, matrix_scale(e, mono(-1)))
                       for m, e in zip(target, smaller_aux)]
    assert not any(contract(smaller_aux, v2)[a][b] for a in range(2) for b in range(2))
    assert determinant_two(contract(modified_source, v2)) == mono(y=2)

    # A leading rank drop is not a generic Laurent-field rank bound.
    generic_full = [[one, zero], [zero, mono(t=1)]]
    assert determinant_two(generic_full) == mono(t=1)
    return {
        "raw_constant_rank_increase": {"generic_rank": 1, "constant_rank": 2},
        "moving_subspace": "V(t)=ker(w0+t*w1)",
        "moving_subspace_dimension": 2,
        "genuine_poles_cancel_in_complete_total": True,
        "auxiliary_first_flattening_rank": rank,
        "auxiliary_rank_one_truncation_breaks_channel_hypothesis": True,
        "primitive_vector": {"input": ["-1", "t^-1", "0"],
                             "normalized": ["-t", "1", "0"],
                             "nonzero_constant": [0, 1, 0]},
        "leading_rank_only_countercontrol": {"generic_rank": 2, "leading_rank": 1},
    }


def coeff(tag, *indices):
    return (tag + sum((j + 2) * (x + 1) for j, x in enumerate(indices))) % 5 - 2


def b_coeff(case, y, alpha, k, col):
    c0 = coeff(1, y, alpha, k)
    c1 = coeff(3, alpha, k, y)
    if case["variable_b"]:
        return add(mono(c0, t=-1), mono(c1 * col, t=1))
    return add(mono(c0, t=-1), mono(c1))


def c_coeff(case, v, beta, u, col):
    c0 = coeff(2, v, beta, u)
    c1 = coeff(4, beta, u, v)
    if case["variable_c"]:
        return add(mono(c0, t=-1), mono(c1 * col * col))
    return add(mono(c0), mono(c1, t=2))


def b_targets(case, y, col):
    if col in case["exceptions_b"]:
        return [(j, a, add(mono(coeff(1, y, col, j, a), t=-2),
                            mono(coeff(2, a, j, y), t=1)))
                for j in range(case["r"]) for a in range(case["h"])]
    return [(col-k, a, b_coeff(case, y, a, k, col))
            for a in range(case["h"]) for k in range(-case["D"], case["D"]+1)
            if 0 <= col-k < case["r"]]


def c_targets(case, col, v):
    if col in case["exceptions_c"]:
        return [(i, b, add(mono(coeff(3, v, col, i, b), t=-1),
                            mono(coeff(4, b, i, v), t=2)))
                for i in range(case["l"]) for b in range(case["h"])]
    return [(col-u, b, c_coeff(case, v, b, u, col))
            for b in range(case["h"]) for u in range(-case["D"], case["D"]+1)
            if 0 <= col-u < case["l"]]


def native_slice(case, p, q):
    """Independent complete native source expansion, with actual cropping."""
    out = {}
    for y in range(case["m"]):
        for v in range(case["m"]):
            for j, a, bc in b_targets(case, y, q+v):
                for i, b, cc in c_targets(case, p+y, v):
                    key = a, b
                    out[key] = add(out.get(key, {}), shift(mul(bc, cc), x=j, y=i))
    return {k: v for k, v in out.items() if v}


def channel_factors(case, p, q):
    """The separate window/profile formula; no native-slice call."""
    h, m, D = case["h"], case["m"], case["D"]
    factors = []
    for j in range(2 if case["variable_b"] else 1):
        for s in range(2 if case["variable_c"] else 1):
            left, right = [{} for _ in range(h)], [{} for _ in range(h)]
            for alpha in range(h):
                for y in range(m):
                    for k in range(-D, D+1):
                        b0, b1 = coeff(1, y, alpha, k), coeff(3, alpha, k, y)
                        if case["variable_b"]:
                            hcoef = (add(mono(b0, t=-1), mono(q*b1, t=1))
                                     if j == 0 else mono(b1))
                        else:
                            hcoef = add(mono(b0, t=-1), mono(b1))
                        # Moving profile psi_1(z,t)=t*z^2.
                        psi = mono() if s == 0 else mono((p+y)**2, t=1)
                        left[alpha] = add(left[alpha], shift(mul(hcoef, psi), x=-k, y=y))
            for beta in range(h):
                for v in range(m):
                    # Moving common basis phi_1(v,t)=t*v.
                    phi = mono() if j == 0 else mono(v, t=1)
                    for u in range(-D, D+1):
                        c0, c1 = coeff(2, v, beta, u), coeff(4, beta, u, v)
                        if case["variable_c"]:
                            gamma = mono(c0 if s == 0 else c1, t=-1)
                        else:
                            gamma = add(mono(c0), mono(c1, t=2))
                        right[beta] = add(right[beta], shift(mul(phi, gamma), x=v, y=-u))
            factors.append((left, right))
    return factors


def factored_slice(case, p, q):
    out = {}
    for left, right in channel_factors(case, p, q):
        for a, lc in enumerate(left):
            for b, rc in enumerate(right):
                out[a, b] = add(out.get((a, b), {}), shift(mul(lc, rc), x=q, y=p))
    return {k: v for k, v in out.items() if v}


def good_indices(case):
    n, m, D = case["n"], case["m"], case["D"]
    ps = [p for p in range(n) if D <= p <= case["l"]-m-D
          and all(p+y not in case["exceptions_c"] for y in range(m))]
    qs = [q for q in range(n) if D <= q <= case["r"]-m-D
          and all(q+v not in case["exceptions_b"] for v in range(m))]
    return ps, qs


def lower_bounds(case):
    ps, qs = good_indices(case)
    n, m, D = case["n"], case["m"], case["D"]
    gb = max(0, case["r"]-m+1-2*D-m*len(case["exceptions_b"]))
    gc = max(0, case["l"]-m+1-2*D-m*len(case["exceptions_c"]))
    offset = case["l"]*case["r"]-n*n
    return max(0, offset+len(ps)*len(qs)), max(0, offset+gb*gc)


def first_map(case, p, q):
    # Deliberately nonseparable first-map mixing, including a pole.
    l, r = case["l"], case["r"]
    return [((p+q) % l, (p+2*q) % r, mono(1, t=-1)),
            ((2*p+q+1) % l, (p+q+1) % r, mono(-1, t=1))]


def full_residual_rank(case, prime, tv):
    n, m, h, l, r = (case[k] for k in ("n", "m", "h", "l", "r"))
    def col(i, j, a, b):
        return (((j*h+a)*h+b)*l+i)
    rows = [defaultdict(int) for _ in range(l*r)]
    for i in range(l):
        for j in range(r):
            for a in range(h):
                rows[i*r+j][col(i, j, a, a)] = 1
    bcache = {(y, s): [(j, a, evaluate(c, prime=prime, tv=tv))
                       for j, a, c in b_targets(case, y, s)]
              for y in range(m) for s in range(n+m-1)}
    ccache = {(s, v): [(i, b, evaluate(c, prime=prime, tv=tv))
                       for i, b, c in c_targets(case, s, v)]
              for v in range(m) for s in range(n+m-1)}
    for p in range(n):
        for q in range(n):
            native = defaultdict(int)
            for y in range(m):
                for v in range(m):
                    for j, a, bc in bcache[y, q+v]:
                        for i, b, cc in ccache[p+y, v]:
                            native[col(i, j, a, b)] += bc*cc
            for i, j, ac in first_map(case, p, q):
                aval = evaluate(ac, prime=prime, tv=tv)
                for k, val in native.items():
                    rows[i*r+j][k] -= aval*val
    return rank_mod(rows, prime)


def finite_case(case):
    ps, qs = good_indices(case)
    checked, negative = 0, 0
    for p in ps:
        for q in qs:
            direct = native_slice(case, p, q)
            symbolic = factored_slice(case, p, q)
            assert direct == symbolic, (case["name"], p, q)
            checked += sum(len(poly) for poly in direct.values())
            negative += sum(t < 0 for poly in direct.values() for _, _, t in poly)
    actual, count = lower_bounds(case)
    values = []
    for prime, tv in [(101, 2), (3, 2)]:
        rank = full_residual_rank(case, prime, tv)
        assert rank >= actual >= count
        values.append({"field_prime": prime, "t_value": tv,
                       "complete_residual_flattening_rank": rank})
    cap = (2 if case["variable_b"] else 1)*(2 if case["variable_c"] else 1)
    assert cap < case["h"]
    return {**case, "generic_channel_rank_cap": cap,
            "good_p_count": len(ps), "good_q_count": len(qs),
            "good_source_slices": len(ps)*len(qs),
            "exact_laurent_coefficient_checks": checked,
            "negative_power_coefficients_retained": negative,
            "kernel_dimension_lower_bound": actual,
            "exception_count_lower_bound": count,
            "finite_specializations": values}


CASES = [
    dict(name="two_toeplitz_with_poles", n=6, m=2, h=2, l=6, r=6, D=0,
         variable_b=False, variable_c=False, exceptions_b=[], exceptions_c=[]),
    dict(name="moving_window_near_full", n=8, m=3, h=3, l=7, r=7, D=0,
         variable_b=True, variable_c=False, exceptions_b=[], exceptions_c=[]),
    dict(name="two_variable_moving_profiles", n=7, m=5, h=5, l=7, r=7, D=0,
         variable_b=True, variable_c=True, exceptions_b=[], exceptions_c=[]),
    dict(name="nonlocal_column_exceptions", n=8, m=2, h=2, l=8, r=8, D=0,
         variable_b=False, variable_c=False, exceptions_b=[0], exceptions_c=[0]),
    dict(name="nonzero_bandwidth", n=8, m=2, h=2, l=8, r=8, D=1,
         variable_b=False, variable_c=False, exceptions_b=[], exceptions_c=[]),
]


def source_pins():
    record = json.loads((HERE / "sources.json").read_text())
    checked = []
    for row in record["local_dependencies"]:
        digest = hashlib.sha256((ROOT / row["path"]).read_bytes()).hexdigest()
        assert digest == row["sha256"], row["path"]
        checked.append({"path": row["path"], "sha256": digest})
    return checked


def certificate():
    return {"schema": "laurent-channel-barrier-controls-v1",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "independent_review": False, "lean_formalized": False,
            "source_pins": source_pins(),
            "formal_controls": formal_controls(),
            "finite_cases": [finite_case(case) for case in CASES],
            "scope": "Finite exact controls only; the all-size formal proof is in proof.md."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = certificate()
    encoded = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()

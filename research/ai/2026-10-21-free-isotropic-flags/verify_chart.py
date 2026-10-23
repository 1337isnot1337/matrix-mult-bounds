#!/usr/bin/env python3
"""Recovered exact certificate for the free C(7,15) -> matched T5 flag.

Standard library only. Binary seed values are NOT characteristic-zero maps.
An odd 45x45 Jacobian minor proves an exact 2-adic lift by Hensel's lemma.
The open conditions below are checked at the binary seed.
"""
import argparse
import json
from pathlib import Path

N = 13
F_BITS = 10717
U_BITS = [109, 114, 60, 83, 18]
MU_BITS = 5780
L_BITS = [1, 2050, 7656]
G_BITS = 2550
PIVOTS = [0,2,7,9,14,16,21,23,28,30,35,36,37,38,39,40,41,42,43,44,45,46,
          49,50,51,52,53,54,55,56,57,58,62,63,64,65,66,67,68,69,70,71,75,76,87]

def bits(x, n):
    return [(x >> i) & 1 for i in range(n)]

def seed():
    return (sum((bits(u, 7) for u in U_BITS), []) + bits(MU_BITS, 13)
            + bits(L_BITS[1], 13) + bits(L_BITS[2], 13)
            + bits(G_BITS, 13) + bits(F_BITS, 13))

def pmul(a, b, modulus):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % modulus
    return out

def evaluate(x, modulus):
    """All 45 integral equations evaluated modulo modulus."""
    us = [x[7*i:7*i+7] for i in range(5)]
    mu, ls, g = x[35:48], [[1], x[48:61], x[61:74]], x[74:87]
    f = x[87:100] + [1]
    def top(a):
        a = a[:]
        for k in range(len(a)-1, N-1, -1):
            c = a[k]
            for j in range(N):
                a[k-N+j] = (a[k-N+j] - c*f[j]) % modulus
        return a[N-1] if len(a) >= N else 0
    out = []
    for u in us:
        for j in range(3):
            for k in range(j, 3):
                p = pmul(pmul(pmul(mu, u, modulus), ls[j], modulus), ls[k], modulus)
                out.append(top(p))
    for u in us:
        for l in ls:
            p = pmul(pmul(pmul(mu, u, modulus), g, modulus), l, modulus)
            out.append(top(p))
    return out

def rank(rows):
    piv = {}
    for value in rows:
        while value:
            k = value.bit_length()-1
            if k in piv:
                value ^= piv[k]
            else:
                piv[k] = value
                break
    return len(piv)

def nullspace(rows, n):
    rows = rows[:]
    pivots, at = [], 0
    for col in range(n):
        index = next((i for i in range(at, len(rows)) if (rows[i] >> col) & 1), None)
        if index is None:
            continue
        rows[at], rows[index] = rows[index], rows[at]
        for i in range(len(rows)):
            if i != at and ((rows[i] >> col) & 1):
                rows[i] ^= rows[at]
        pivots.append(col)
        at += 1
    out = []
    for col in range(n):
        if col in pivots:
            continue
        value = 1 << col
        for i, p in enumerate(pivots):
            if (rows[i] >> col) & 1:
                value |= 1 << p
        out.append(value)
    return out

def solve_square(rows, rhs, n):
    aug = [r | (b << n) for r, b in zip(rows, rhs)]
    for col in range(n):
        index = next(i for i in range(col, n) if (aug[i] >> col) & 1)
        aug[col], aug[index] = aug[index], aug[col]
        for i in range(n):
            if i != col and ((aug[i] >> col) & 1):
                aug[i] ^= aug[col]
    return [(aug[i] >> n) & 1 for i in range(n)]

def raw_mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out

def raw_div(a, b):
    q = 0
    while a and a.bit_length() >= b.bit_length():
        k = a.bit_length() - b.bit_length()
        q ^= 1 << k
        a ^= b << k
    return q, a

def mul(a, b):
    return raw_div(raw_mul(a, b), F_BITS)[1]

def inverse(a):
    r0, r1, s0, s1 = F_BITS, a, 0, 1
    while r1:
        q, r = raw_div(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, s0 ^ raw_mul(q, s1)
    assert r0 == 1, "unit condition fails"
    return raw_div(s0, F_BITS)[1]

def tau(a):
    return (a >> 12) & 1

def trace_row(a):
    return sum(tau(mul(a, 1 << j)) << j for j in range(13))

def open_conditions():
    assert rank(U_BITS) == 5
    assert rank(U_BITS + [u << 1 for u in U_BITS]) == 8
    inverse(MU_BITS)
    invg = inverse(G_BITS)
    big_g = mul(MU_BITS, G_BITS)
    assert big_g == 1921
    assert rank(L_BITS + [G_BITS]) == 4
    ul = [mul(u, l) for u in U_BITS for l in L_BITS]
    assert rank(ul) == 9
    central = []
    weight = mul(MU_BITS, invg)
    for u in U_BITS:
        entries = [tau(mul(mul(mul(weight, u), L_BITS[j]), L_BITS[k]))
                   for j in range(3) for k in range(j, 3)]
        central.append(sum(x << i for i, x in enumerate(entries)))
    assert rank(central) == 5
    conics = nullspace(central, 6)
    assert len(conics) == 1 and conics[0] == 43
    aa, bb, cc, dd, ee, ff = bits(conics[0], 6)
    discriminant = 4*aa*dd*ff + bb*cc*ee - aa*ee*ee - dd*cc*cc - ff*bb*bb
    assert discriminant == 3

    k_basis = [mul(MU_BITS, l) for l in L_BITS] + [big_g]
    assert rank(k_basis) == 4
    assert all(tau(mul(x, y)) == 0 for x in k_basis for y in ul)
    k0 = nullspace([trace_row(u) for u in U_BITS], 13)
    assert len(k0) == 8
    span, outer_y = k_basis[:], []
    for v in k0:
        if rank(span + [v]) > len(span):
            span.append(v)
            outer_y.append(v)
    assert len(outer_y) == 4
    pencil = [[[tau(mul(mul(u, y), l)) for u in U_BITS] for y in outer_y]
              for l in L_BITS[1:]]
    sylvester = []
    for degree in range(5):
        for y in range(4):
            row = 0
            for power in range(4):
                for i in range(5):
                    value = 0
                    if degree == power:
                        value ^= pencil[0][y][i]
                    if degree == power + 1:
                        value ^= pencil[1][y][i]
                    row |= value << (5*power+i)
            sylvester.append(row)
    assert rank(sylvester) == 20
    # A degree-four kernel gives a direct basis certificate for the pencil,
    # without needing a classification theorem for matrix pencils.
    kernel_equations = []
    for degree in range(6):
        for y in range(4):
            row = 0
            for power in range(5):
                for i in range(5):
                    value = 0
                    if degree == power:
                        value ^= pencil[0][y][i]
                    if degree == power+1:
                        value ^= pencil[1][y][i]
                    row |= value << (5*power+i)
            kernel_equations.append(row)
    assert rank(kernel_equations) == 24
    vectors = nullspace(kernel_equations, 25)
    assert len(vectors) == 1
    coefficients = [(vectors[0] >> (5*k)) & 31 for k in range(5)]
    assert rank(coefficients) == 5
    a_rows = [sum(v << i for i,v in enumerate(row)) for row in pencil[0]]
    images = [sum(((row & vector).bit_count() & 1) << i
                  for i,row in enumerate(a_rows)) for vector in coefficients[1:]]
    assert rank(images) == 4
    h1 = [sum(((((u << k) >> 2) ^ ((u << k) >> 5)) & 1) << k for k in range(5))
          for u in U_BITS]
    assert rank(h1) == 5
    return {"shared_rank": 5, "rank_U_plus_tU": 8, "rank_UL": 9,
            "rank_L_plus_g": 4, "mu_times_g_bits": big_g,
            "central_shared_rank": 5, "central_conic_bits": 43,
            "primitive_conic_discriminant": discriminant,
            "outer_sylvester_rank": 20, "high_pair_shared_rank": 5,
            "outer_degree_four_equation_rank": 24,
            "outer_kernel_coefficient_vectors": coefficients,
            "outer_kernel_coefficient_rank": 5,
            "outer_normalizing_image_rank": 4}

def verify(lift_bits=12):
    x = seed()
    assert len(x) == 100
    base = evaluate(x, 4)
    assert len(base) == 45 and all(v % 2 == 0 for v in base)
    rows = [0] * 45
    for c in range(100):
        perturbed = x[:]
        perturbed[c] += 2
        values = evaluate(perturbed, 4)
        for i, (a, b) in enumerate(zip(values, base)):
            derivative = ((a-b) % 4) // 2
            rows[i] |= derivative << c
    minor = [sum(((row >> col) & 1) << i for i, col in enumerate(PIVOTS)) for row in rows]
    assert rank(rows) == 45
    assert rank([r & ((1 << 87)-1) for r in rows]) == 44
    assert rank(minor) == 45
    for level in range(1, lift_bits):
        values = evaluate(x, 1 << (level+1))
        assert all(v % (1 << level) == 0 for v in values)
        delta = solve_square(minor, [v >> level for v in values], 45)
        for c, value in zip(PIVOTS, delta):
            x[c] += (1 << level) * value
    assert not any(evaluate(x, 1 << lift_bits))
    return {"equations": 45, "variables": 100, "jacobian_rank_mod2": 45,
            "fixed_modulus_jacobian_rank_mod2": 44, "pivot_minor_rank_mod2": 45,
            "pivot_columns": PIVOTS, "finite_difference_checks": 4500,
            "hensel_replay_bits": lift_bits, "opens": open_conditions(),
            "claim": "Exact characteristic-zero existence via an odd Jacobian minor.",
            "scope": "Finite C(7,15) degeneration to five independently based convolution sectors; no exponent improvement."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--lift-bits", type=int, default=12)
    args = parser.parse_args()
    report = verify(args.lift_bits)
    data = json.dumps(report, indent=2) + "\n"
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data)
    print(data, end="")


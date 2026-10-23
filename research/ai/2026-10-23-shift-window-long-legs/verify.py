"""Exact finite controls for one variable-coefficient Q(n,m) long leg.

No third-party dependencies. The all-size theorem is proved in proof.md,
not by these tests. Arithmetic: F_101 throughout.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from math import comb
from pathlib import Path

P = 101


def bcoef(mode: str, degree: int, y: int, t: int, k: int, s: int) -> int:
    a = 3 + 5*y + 7*t + 2*k
    b = 1 + 2*y + 3*t + k
    c = 1 + y + 2*t
    if mode == "polynomial":
        return (a + b*s + (c*s*s if degree == 2 else 0)) % P
    if mode == "two_exponentials":
        return (a*pow(2, s, P) + b*pow(3, s, P)) % P
    if mode == "exp_linear":
        return ((a + b*s)*pow(2, s, P)) % P
    raise ValueError(mode)


def ccoef(v: int, u: int, ell: int) -> int:
    return (2 + 2*v + 7*u + 3*ell) % P


def recurrence(mode: str, degree: int) -> list[int]:
    if mode == "polynomial":
        r = degree + 1
        # (E - 1)^r annihilates polynomials of degree < r.
        return [(-1)**(r-j+1) * comb(r, j) % P for j in range(r)]
    if mode == "two_exponentials":
        return [-6 % P, 5]
    if mode == "exp_linear":
        return [-4 % P, 4]
    raise ValueError(mode)


def recurrence_windows(c: list[int], m: int) -> list[list[int]]:
    """phi[v][j]: common expansion of value at shift v from r initials."""
    r = len(c)
    assert 1 <= r < m
    phi = [[int(v == j) for j in range(r)] for v in range(r)]
    for v in range(r, m):
        phi.append([sum(c[i]*phi[v-r+i][j] for i in range(r)) % P
                    for j in range(r)])
    return phi


def b_terms(n: int, m: int, D: int, y: int, s: int,
            mode: str, degree: int, exceptions: frozenset[int]):
    if s in exceptions:
        return [((7*s + 3*y + t + 1) % n, t, (4+y+2*t) % P)
                for t in range(m)]
    return [(s-k,t,bcoef(mode,degree,y,t,k,s))
            for t in range(m) for k in range(-D,D+1) if 0 <= s-k < n]


def c_terms(n: int, m: int, D: int, z: int, v: int,
            exceptions: frozenset[int]):
    if z in exceptions:
        return [(u,(5*z+v+2*u+1) % n,(3+v+4*u) % P)
                for u in range(m)]
    return [(u,z-ell,ccoef(v,u,ell))
            for u in range(m) for ell in range(-D,D+1) if 0 <= z-ell < n]


def source_slice(n: int, m: int, D: int, p: int, q: int,
                 mode: str, degree: int, eb: frozenset[int], ec: frozenset[int]):
    out = defaultdict(int)
    for y in range(m):
        for v in range(m):
            for qp,t,b in b_terms(n,m,D,y,q+v,mode,degree,eb):
                for u,pp,c in c_terms(n,m,D,p+y,v,ec):
                    out[(t,u,qp,pp)] = (out[(t,u,qp,pp)] + b*c) % P
    return {key:val for key,val in out.items() if val}


def mul(a: dict, b: dict) -> dict:
    out = defaultdict(int)
    for (ax,ay),av in a.items():
        for (bx,by),bv in b.items():
            out[(ax+bx,ay+by)] = (out[(ax+bx,ay+by)] + av*bv) % P
    return {key:val for key,val in out.items() if val}


def predicted_slice(n: int, m: int, D: int, p: int, q: int,
                    mode: str, degree: int, phi: list[list[int]]) -> dict:
    r = len(phi[0])
    result = defaultdict(int)
    for j in range(r):
        for t in range(m):
            f = defaultdict(int)
            for y in range(m):
                for k in range(-D,D+1):
                    f[(-k,y)] = (f[(-k,y)] + bcoef(mode,degree,y,t,k,q+j)) % P
            for u in range(m):
                g = defaultdict(int)
                for v in range(m):
                    for ell in range(-D,D+1):
                        g[(v,-ell)] = (g[(v,-ell)] + phi[v][j]*ccoef(v,u,ell)) % P
                for (dx,dy),value in mul(f,g).items():
                    key = (t,u,q+dx,p+dy)
                    assert 0 <= key[2] < n and 0 <= key[3] < n
                    result[key] = (result[key] + value) % P
    return {key:val for key,val in result.items() if val}


def amap(n: int, p: int, q: int):
    return [(p,q,1),((2*p+q+1)%n,(p+3*q+2)%n,-1),
            ((p+q+1)%n,(2*q+1)%n,2)]


def rank_mod(rows, prime=P):
    pivots = {}
    for original in rows:
        row = {k:v%prime for k,v in original.items() if v%prime}
        while row:
            lead = min(row)
            if lead not in pivots:
                scale = pow(row[lead], -1, prime)
                pivots[lead] = {k:(v*scale)%prime for k,v in row.items() if v%prime}
                break
            coef = row[lead]
            for k,v in pivots[lead].items():
                new = (row.get(k,0)-coef*v)%prime
                if new:
                    row[k] = new
                else:
                    row.pop(k,None)
    return len(pivots)


def check(n: int, m: int, D: int, mode: str, degree: int,
          e_b=(), e_c=(), tamper_phi: bool=False) -> dict:
    L = m-1+D
    assert n > 2*L
    eb, ec = frozenset(e_b), frozenset(e_c)
    good_q = [q for q in range(L,n-L) if all(q+v not in eb for v in range(m))]
    good_p = [p for p in range(L,n-L) if all(p+y not in ec for y in range(m))]
    rec = recurrence(mode,degree)
    r = len(rec)
    assert r < m
    phi = recurrence_windows(rec,m)
    if tamper_phi:
        phi[-1][0] = (phi[-1][0] + 1) % P
    # Direct check of the common-shift-window premise, all channel/stencil indices.
    for q in good_q:
        for y in range(m):
            for t in range(m):
                for k in range(-D,D+1):
                    for v in range(m):
                        value = bcoef(mode,degree,y,t,k,q+v)
                        expanded = sum(phi[v][j]*bcoef(mode,degree,y,t,k,q+j)
                                       for j in range(r)) % P
                        assert value == expanded, (mode,n,m,D,q,y,t,k,v)
    # Independent direct tensor vs. rank-r Laurent-symbol expansion.
    for p in good_p:
        for q in good_q:
            actual = source_slice(n,m,D,p,q,mode,degree,eb,ec)
            expected = predicted_slice(n,m,D,p,q,mode,degree,phi)
            assert actual == expected, (mode,n,m,D,p,q)
    # Full residual A | B,C flattening, including exceptional maps and arbitrary A mixing.
    rows = [defaultdict(int) for _ in range(n*n)]
    def col(qp,t,u,pp):
        return ((qp*m+t)*(m*n)+(u*n+pp))
    for i in range(n):
        for h in range(n):
            for t in range(m):
                rows[i*n+h][col(h,t,t,i)] += 1
    for p in range(n):
        for q in range(n):
            src = source_slice(n,m,D,p,q,mode,degree,eb,ec)
            for i,h,a in amap(n,p,q):
                for (t,u,qp,pp),v in src.items():
                    rows[i*n+h][col(qp,t,u,pp)] -= a*v
    observed = rank_mod(rows)
    lower = len(good_q)*len(good_p)
    assert observed >= lower
    return {"n":n,"m":m,"D":D,"variable_mode":mode,"degree":degree,
            "window_rank_bound":r,"good_p":len(good_p),"good_q":len(good_q),
            "predicted_lower_bound":lower,"observed_residual_flattening_rank_F101":observed,
            "b_exceptional_columns":sorted(eb),"c_exceptional_columns":sorted(ec),
            "window_coefficients_checked":len(good_q)*m*m*(2*D+1)*m,
            "source_symbol_slices_checked":lower,"arbitrary_a_mixing":True}


def full_window_rank_control(m: int=3) -> bool:
    """Unrestricted bulk coefficients need not have a common proper shift span."""
    windows = []
    q = 1
    for y in range(m):
        windows.append({v: int((q+v-y) % m == 0) for v in range(m)})
    return rank_mod(windows) == m


def run() -> dict:
    cases = [
        (8,3,0,"polynomial",1),
        (10,4,0,"polynomial",2),
        (10,4,0,"two_exponentials",0),
        (12,3,0,"exp_linear",0,(4,),(5,)),
        (12,3,1,"polynomial",1),
    ]
    outcome = [check(*case) for case in cases]
    assert full_window_rank_control(3)
    assert bcoef("polynomial",2,1,0,0,1) != bcoef("polynomial",2,1,0,0,2)
    return {"status":"pass", "field":"F_101", "methods":"exact modular arithmetic",
            "cases":outcome, "full_window_rank_countercontrol":True,
            "scope":"Five finite controls only; the all-size statement depends on proof.md."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    report = json.dumps(run(),indent=2,sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(report,encoding="utf8")
    else:
        print(report)

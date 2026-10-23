#!/usr/bin/env python3
"""Independent characteristic-zero oracle: direct definition and SymPy QQ elimination."""
from __future__ import annotations

import json
from fractions import Fraction
from sympy import Matrix, Rational


def rank_by_definition(a, b, e, c, w):
    m = a + b - 1
    poly = {(0, s): Rational(v) for s, v in enumerate(c) if v}
    poly.update({(i, e): Rational(v) for i, v in enumerate(w) if v})
    rows = []
    for j in range(b):
        for L in range(m):
            rows.append([poly.get((H - j, L - r), 0)
                         for H in range(m) for r in range(a)])
    return Matrix(rows).rank()


def expected(a,b,e,w):
    d = len(w)-1
    while d > 0 and w[d] == 0:
        d -= 1
    return a*b + sum(min(b, d*((a+j)//e)) for j in range(e))


def run():
    # Includes non-monic coefficients, fractions, and nonconstant middle-free cases.
    checks=0
    for a in (2,3):
        for e in (2,3):
            for b in (e+1,e+3):
                for variant in (0,1,2):
                    c = [Rational(2,3)]
                    for k in range(1,e):
                        c.append([Rational(0),Rational(-1,2),Rational(3,5)][(k+variant)%3])
                    w = [Rational(1,7) if variant else Rational(0)]*a
                    w[0] = Rational(1,7)
                    w[min(a-1,variant)] = [Rational(2,5),Rational(-7,3),Rational(9,4)][variant]
                    r = rank_by_definition(a,b,e,c,w)
                    want=expected(a,b,e,w)
                    assert r==want,(a,b,e,variant,r,want)
                    checks += 1
    return {'result':'PASS','charzero_QQ_cases':checks,
            'oracle':'SymPy rational rank of full row-by-column coefficient matrix built from biform dict'}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))

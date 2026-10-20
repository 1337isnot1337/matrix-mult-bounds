"""Exact finite checks and symbolic identities for the scalar-profile theorem.

The general proof is in research_note.md. These tests are independent sanity
checks of the formulas; a finite grid is not an asymptotic proof.
Run: python verify_profile.py
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import json
import math
import time
import sympy as sp
from search_degenerations import profile, slopes


def main():
    start = time.perf_counter()
    n = 128
    h = slopes(4*n+1)
    counters = dict(symmetry=0, boundary=0, concavity=0, tripling=0,
                    rank_upper=0, diagonal_equality=0, replication=0)
    for a in range(1,n+1):
        assert profile(1,a,h)==a
        counters['boundary']+=1
        assert profile(a,a,h)==h[a]*Fraction(3*a-1,2)
        counters['diagonal_equality']+=1
        for b in range(1,n+1):
            p=profile(a,b,h)
            assert p==profile(b,a,h)
            counters['symmetry']+=1
            if b>=2:
                slack=2*p-profile(a,b-1,h)-profile(a,b+1,h)
                assert slack>=0
                counters['concavity']+=1
            assert profile(a,3*b+a-1,h)>=3*p
            counters['tripling']+=1
            assert p**3 <= (a+b-1)**4
            counters['rank_upper']+=1
    for a in range(1,33):
        for b in range(1,33):
            for m in range(1,9):
                assert profile(m*a,m*b,h)**3 >= m**4*profile(a,b,h)**3
                counters['replication']+=1
    a,b,q=sp.symbols('a b q')
    concavity=sp.factor(2*(a+(b-1)/2)-(3*b+1)/(3*b)*(a+b/2)-3*(b-1)/(3*b-2)*(a+(b-2)/2))
    assert sp.simplify(concavity-2*(a-b)/(3*b*(3*b-2)))==0
    tripling=sp.factor((3*a+1)*(a+2*q)*(2*a+q-1)-3*a*(a+2*q-1)*(2*a+q+1))
    assert sp.expand(tripling-2*(a-q)*(a-q+1))==0
    upper=sp.factor(27*a**3*(3*a+2)-(3*a+1)**3*(3*a-1))
    assert upper==6*a+1
    assert sp.factor((1+sp.Rational(1,3)/a)**3-(1+1/a)) == (9*a+1)/(27*a**3)
    report={'grid_max':n,'exact_checks':counters,'total_exact_grid_checks':sum(counters.values()),
            'symbolic_identities':{'concavity':str(concavity),'tripling':str(tripling),'cubic_upper':str(upper)},
            'diagonal_values':{str(a):{'exact':str(profile(a,a,h)),
                                      'ratio_to_a_4_over_3':float(profile(a,a,h))/(a**(4/3))}
                                for a in [1,2,3,10,100,128]},
            'diagonal_asymptotic_coefficient':3/(2*math.gamma(4/3)),
            'elapsed_seconds':time.perf_counter()-start,
            'status':'All checks passed. General validity rests on the algebraic proof, not this grid.'}
    path=Path(__file__).with_name('profile_checks.json')
    path.write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()

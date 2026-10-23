#!/usr/bin/env python3
"""Exact controls for the scalar shifted-block barrier; standard library only."""
import argparse
import json
from pathlib import Path

def rank_mod(matrix, prime):
    a = [[v % prime for v in row] for row in matrix]
    if not a:
        return 0
    at = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(at, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[at], a[pivot] = a[pivot], a[at]
        inv = pow(a[at][col], -1, prime)
        a[at] = [(v*inv) % prime for v in a[at]]
        for i in range(len(a)):
            if i != at and a[i][col]:
                c = a[i][col]
                a[i] = [(x-c*y) % prime for x, y in zip(a[i], a[at])]
        at += 1
    return at

def verify():
    checks = sums = 0
    for m in range(3, 21):
        degree = 2*m-1
        for d in range(degree+1):
            cat = [[int(i+j == m-1) for i in range(d+1)]
                   for j in range(degree-d+1)]
            expected = min(d+1, 2*m-d)
            for prime in (2, 101):
                assert rank_mod(cat, prime) == expected
                assert d+1-expected == max(2*d-2*m+1, 0)
                checks += 1
        for k in range(m-1):
            total = sum(max(2*r+2*k-2*m+3, 0) for r in range(m-1))
            assert total == k*k
            lhs = (m-1)*(k+1) - (k*k+m+k+1)
            assert lhs == k*(m-2-k)-2
            sums += 1
        assert max(k*(m-2-k) for k in range(m-1)) == (m-2)**2//4
    assert (checks, sums) == (828, 189)
    return {"literal_catalecticant_rank_checks": checks, "exact_sum_checks": sums,
            "fields": [2, 101], "m_range": [3, 20],
            "bound": "B >= m(m+1)/2 + floor((m-2)^2/4) - 2",
            "scope": "Scalar shifted input factors and full negative shifted moments in C(m+1,B); no exponent improvement."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    text = json.dumps(verify(), indent=2) + "\n"
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    print(text, end="")


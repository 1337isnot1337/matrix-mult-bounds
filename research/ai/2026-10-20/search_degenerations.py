"""Offline search for monomial convolution splittings that beat an exact profile.

Every candidate is scored with fractions and its target support is verified,
not inferred from a rounded numerical tensor fit. The displayed float ratio
is descriptive only and is never used to accept a violation.
This does not itself prove a new matrix-multiplication exponent.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
import random
import time
from pathlib import Path


def slopes(n: int) -> list[Fraction]:
    h = [Fraction(0), Fraction(1)]
    for k in range(1, n):
        h.append(h[-1] * Fraction(3*k+1, 3*k))
    return h


def profile(a: int, b: int, h: list[Fraction]) -> Fraction:
    a, b = sorted((a, b))
    return h[a] * Fraction(2*b+a-1, 2)


def components(wx: tuple[int, ...], wy: tuple[int, ...]):
    a, b = len(wx), len(wy)
    mins = [min(wx[i] + wy[k-i] for i in range(max(0,k-b+1), min(a-1,k)+1))
            for k in range(a+b-1)]
    terms = [(i,j,i+j) for i in range(a) for j in range(b)
             if wx[i]+wy[j] == mins[i+j]]
    parent = list(range(b+a+b-1))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i,j,k in terms:
        r,s = root(j), root(b+k)
        if r != s:
            parent[r] = s
    groups = {}
    for term in terms:
        groups.setdefault(root(term[1]), []).append(term)
    return list(groups.values()), [-v for v in mins]


def recognize(terms):
    """Check equality with a convolution support after axis reversals/reindexing.

    The largest axis must have length equal to the sum of the other lengths
    minus one. Order on each coordinate set, optionally reversed, identifies
    a prospective output index with the sum of the two input indices.
    """
    vals = [sorted({t[k] for t in terms}) for k in range(3)]
    dims = list(map(len, vals))
    for output in range(3):
        inputs = [i for i in range(3) if i != output]
        r,s = dims[inputs[0]], dims[inputs[1]]
        if dims[output] != r+s-1 or len(terms) != r*s:
            continue
        indexes = [{v:j for j,v in enumerate(axis)} for axis in vals]
        for flips in product((False,True), repeat=3):
            mapped = []
            for term in terms:
                ids = [indexes[k][term[k]] for k in range(3)]
                ids = [dims[k]-1-v if flips[k] else v for k,v in enumerate(ids)]
                mapped.append(tuple(ids))
            if all(t[output] == t[inputs[0]]+t[inputs[1]] for t in mapped):
                return {'kind':'convolution','a':r,'b':s,'output_axis':output,
                        'reversals':flips,'dimensions':dims}
    # A slice is a matching because the original support is i+j=k.
    d = max(max(Counter(t[k] for t in terms).values()) for k in range(3))
    return {'kind':'slice_lower_bound','a':1,'b':d,'dimensions':dims}


def inspect(wx, wy, hf, h):
    groups, wz = components(wx,wy)
    blocks = [recognize(g) for g in groups]
    target = sum((profile(q['a'],q['b'],h) for q in blocks), Fraction(0))
    source = profile(len(wx),len(wy),h)
    record = {'a':len(wx),'b':len(wy),'x_weights':wx,'y_weights':wy,'z_weights':wz,
              'blocks':blocks,'ratio_float':float(target/source),
              'source_exact':str(source),'target_exact':str(target),
              'violation_exact':target > source}
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['binary','ternary','random'], default='binary')
    parser.add_argument('--max-sum', type=int, default=12)
    parser.add_argument('--samples', type=int, default=20000)
    parser.add_argument('--seed', type=int, default=20261020)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    h = slopes(100)
    hf = [float(v) for v in h]
    rng = random.Random(args.seed)
    start = time.perf_counter()
    count = 0
    best = None
    best_nontrivial = None
    witnesses = []
    if args.mode == 'random':
        cases = ((tuple(rng.randint(-8,8) for _ in range(rng.randint(2,15))),
                  tuple(rng.randint(-8,8) for _ in range(rng.randint(2,15))))
                 for _ in range(args.samples))
    else:
        alphabet = range(2 if args.mode=='binary' else 3)
        # min=0 removes translations, without altering the zero-weight support.
        cases = ((wx,wy) for a in range(2,args.max_sum-1)
                 for b in range(a,args.max_sum-a+1)
                 for wx in product(alphabet,repeat=a) if min(wx)==0
                 for wy in product(alphabet,repeat=b) if min(wy)==0)
    for wx,wy in cases:
        rec = inspect(wx,wy,hf,h)
        count += 1
        if best is None or rec['ratio_float'] > best['ratio_float']:
            best = rec
        if len(rec['blocks']) > 1 and (best_nontrivial is None or rec['ratio_float'] > best_nontrivial['ratio_float']):
            best_nontrivial = rec
        if rec.get('violation_exact',False):
            witnesses.append(rec)
            break
    report = {'mode':args.mode,'max_sum':args.max_sum,'seed':args.seed,
              'cases_tested':count,'elapsed_seconds':time.perf_counter()-start,
              'best':best,'best_nontrivial':best_nontrivial,'exact_witnesses':witnesses,
              'scope':'Exact scoring of the specified finite integer-weight arrays only. Unrecognized blocks use a valid slice lower bound.'}
    args.output.write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))

if __name__ == '__main__':
    main()

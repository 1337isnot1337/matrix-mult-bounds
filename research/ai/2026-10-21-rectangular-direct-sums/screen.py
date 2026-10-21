"""Exact necessary tests for two ordinary rectangular matrix summands.

Passing is not a tensor construction. No floating-point acceptance tests.
Only the written polynomial/Hankel lemmas cited in the companion note are used.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
from itertools import permutations
import json
from math import isqrt
from pathlib import Path

SCALE = 10**6

@lru_cache(None)
def score_interval(volume, scale=SCALE):
    """Enclose (216*volume)**(3/4), scaled by scale."""
    if volume < 1 or scale < 1:
        raise ValueError('Positive volume and scale required')
    q = (216*volume)**3 * scale**4
    low = isqrt(isqrt(q))
    assert low**4 <= q < (low+1)**4
    return low, low if low**4 == q else low+1


def legs(shape):
    m, n, p = shape
    return (m*n, n*p, p*m)


def slice_minima(shape):
    m, n, p = shape
    return (p, m, n)


def rejection(a, b, shapes):
    """Return a witnessed necessary-condition failure, or None."""
    if min(a, b) < 2 or not shapes or any(min(s) < 1 for s in shapes):
        raise ValueError('Invalid source or target')
    ab = a*b
    size = ab*(a+b-1)
    dims = tuple(sum(legs(s)[i] for s in shapes) for i in range(3))
    if max(dims) > size:
        return 'dimension'
    losses = [2*size-sum(dims)+dims[i] for i in range(3)]
    levels = range(1, min(a-1, b-1, (a+b-1)//3)+1)
    boundary = (a+b)//3 if (a+b)%3 == 0 else None
    if boundary is not None and not (2 <= boundary < min(a,b)):
        boundary = None
    for s in shapes:
        ds, rs = legs(s), slice_minima(s)
        lifts = [rs[i]+losses[i] for i in range(3)]
        if min(lifts) < ab:
            return 'minimum slice rank'
        if s != (1,1,1) and max(lifts) < 2*ab:
            return 'three coherent factors'
        for i in range(3):
            for r in levels:
                if ds[i] > r*ab and lifts[i] < (r+1)*ab:
                    return 'Hankel symbol dimension'
            if (boundary is not None and ds[i] > max(boundary,4)*ab
                    and lifts[i] < (boundary+1)*ab):
                return 'boundary symbol dimension'
        # Use the existing equality refinement only in its original square,
        # equal-total-leg setting. Do not extend it silently to rectangles.
        if (len(set(dims)) == 1 and len(set(s)) == 1 and s[0] >= 3
                and min(a,b) >= 3 and a+b-1 >= 6 and lifts[0] == 2*ab):
            return 'square equality'
    if sum(s == (1,1,1) for s in shapes) >= 2 and max(2+x for x in losses) < 2*ab:
        return 'two scalar summands'
    return None


def sorted_shapes(size):
    return [(m,n,p) for m in range(1,isqrt(size)+1)
            for n in range(m,isqrt(size)+1) for p in range(n,size//n+1)]


def volume(s):
    return s[0]*s[1]*s[2]


def screen_source(a, b):
    size = a*b*(a+b-1)
    threshold = (3*(a+b)-2)**3*SCALE
    shapes = sorted(sorted_shapes(size), key=lambda s: (volume(s),s), reverse=True)
    records = [(s, volume(s), score_interval(volume(s))) for s in shapes]
    counts = {'normalized_shapes':len(shapes), 'first_volume_bound_pruned':0,
              'dimension_eligible_pairs':0, 'score_eligible_pairs':0, 'survivors':0}
    failures = {}
    survivors = []
    for first, v1, (l1,u1) in records:
        if 2*u1 <= threshold:
            break
        caps = [size-x for x in legs(first)]
        if min(caps) < 1:
            continue
        # v2 squared is the product of its three leg dimensions.
        vmax = min(v1,isqrt(caps[0]*caps[1]*caps[2]))
        if u1+score_interval(vmax)[1] <= threshold:
            counts['first_volume_bound_pruned'] += 1
            continue
        lo, hi = 1, vmax
        while lo < hi:
            mid=(lo+hi)//2
            if u1+score_interval(mid)[1] > threshold:
                hi=mid
            else:
                lo=mid+1
        min_volume=lo
        for m in range(1,min(caps[0],caps[2])+1):
            for n in range(1,caps[0]//m+1):
                pmax=min(caps[2]//m,caps[1]//n,v1//(m*n))
                counts['dimension_eligible_pairs'] += pmax
                pmin=(min_volume+m*n-1)//(m*n)
                for p in range(pmin,pmax+1):
                    oriented=(m,n,p)
                    l2,u2=score_interval(m*n*p)
                    if u1+u2 <= threshold:
                        continue
                    counts['score_eligible_pairs'] += 1
                    reason=rejection(a,b,[first,oriented])
                    assert reason != 'dimension'
                    if reason is not None:
                        failures[reason]=failures.get(reason,0)+1
                        continue
                    counts['survivors'] += 1
                    survivors.append({'shapes':[first,oriented],
                        'leg_dimensions':[sum(x) for x in zip(legs(first),legs(oriented))],
                        'score_interval_numerators':[l1+l2,u1+u2],
                        'strict_score_gain_certified':l1+l2 > threshold})
    return {'a':a,'b':b,'source_leg_dimension':size,
            'threshold_numerator':threshold,'denominator':SCALE,
            'counts':counts,'rejection_counts':failures,'surviving_targets':survivors,
            'status':'necessary tests only; no maps constructed'}

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('a',type=int)
    parser.add_argument('b',type=int)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    report=screen_source(args.a,args.b)
    out=json.dumps(report,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(out)
    print(json.dumps({k:v for k,v in report.items() if k!='surviving_targets'},indent=2))
    print('first survivors:',report['surviving_targets'][:3])

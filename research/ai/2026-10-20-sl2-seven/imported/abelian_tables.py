"""Exact canonical triple-product tables for a cyclic prime-order subgroup.

Independent translations put 0 in every set. If the first size is >=2,
simultaneous nonzero scaling puts 1 in the first set as well. The enumeration
is complete within that normalization, not a search over the whole group.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations


@lru_cache(None)
def normal_tables(p: int,a: int,b: int,c: int) -> tuple:
    if min(p,a,b,c)<1 or max(a,b,c)>p:
        raise ValueError('invalid cyclic subgroup or set size')
    if a*b*c>p:return ()
    base=(0,1) if a>=2 else (0,)
    rest=range(2,p) if a>=2 else range(1,p)
    mask=(1<<p)-1
    result=[]
    for extra in combinations(rest,a-len(base)):
        A=base+extra
        for other in combinations(range(1,p),b-1):
            B=(0,)+other
            sums={(x+y)%p for x in A for y in B}
            if len(sums)!=a*b:continue
            D=sum(1<<x for x in sums)
            allowed=[]
            for t in range(1,p):
                shifted=((D<<t)|(D>>(p-t)))&mask
                if not D&shifted:allowed.append(t)
            allowed_set=set(allowed)
            def complete(chosen,candidates):
                if len(chosen)==c-1:
                    result.append((A,B,(0,)+chosen));return
                need=c-1-len(chosen)
                for pos,x in enumerate(candidates):
                    if len(candidates)-pos<need:break
                    remaining=tuple(y for y in candidates[pos+1:] if (y-x)%p in allowed_set)
                    complete(chosen+(x,),remaining)
            complete((),tuple(allowed))
    return tuple(result)


def verify_table_entry(p,entry):
    A,B,C=entry
    return (all(0<=x<p for S in entry for x in S)
            and all(len(set(S))==len(S) for S in entry)
            and len({(a+b+c)%p for a in A for b in B for c in C})==len(A)*len(B)*len(C))

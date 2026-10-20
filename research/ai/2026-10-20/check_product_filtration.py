"""Test additional determinant-filtration inequalities against the exact model.

For C(a,b) tensor C(c,d), the associated graded has convolution blocks indexed
by i,j,k with i+j=k. Fixing any one block label gives matched sectors sharing
that leg, and hence a power-sum inequality for the symmetrized profile.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import time
from search_degenerations import profile,slopes


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-size',type=int,default=10)
    args=parser.parse_args()
    n=args.max_size
    h=slopes(2*n+1)
    p={(a,b):profile(a,b,h) for a in range(1,2*n+1) for b in range(1,2*n+1)}
    count=0
    sources=0
    best=Fraction(0)
    best_record=None
    nontrivial_best=Fraction(0)
    nontrivial_record=None
    violations=[]
    start=time.perf_counter()
    for a,b,c,d in product(range(1,n+1),repeat=4):
        sources+=1
        src=p[a,b]*p[c,d]
        aa=[a+c-1-2*i for i in range(min(a,c))]
        bb=[b+d-1-2*j for j in range(min(b,d))]
        targets=[]
        for i in range(len(aa)):
            targets.append(('X',i,[(aa[i],s) for s in bb]))
        for j in range(len(bb)):
            targets.append(('Y',j,[(r,bb[j]) for r in aa]))
        for k in range(len(aa)+len(bb)-1):
            targets.append(('Z',k,[(aa[i],bb[k-i]) for i in range(len(aa)) if 0<=k-i<len(bb)]))
        for shared,label,blocks in targets:
            count+=1
            dst=sum((p[r,s] for r,s in blocks),Fraction(0))
            ratio=dst/src
            rec={'source':[a,b,c,d],'shared_leg':shared,'label':label,
                 'blocks':blocks,'source_value':str(src),'target_value':str(dst),'ratio':str(ratio)}
            if ratio>best:
                best,best_record=ratio,rec
            if len(blocks)>1 and min(a,b,c,d)>1 and ratio>nontrivial_best:
                nontrivial_best,nontrivial_record=ratio,rec
            if dst>src:
                violations.append(rec)
    report={'max_size':n,'source_quadruples':sources,'exact_inequalities_checked':count,
            'violations':violations,'best':best_record,'best_nontrivial':nontrivial_record,
            'elapsed_seconds':time.perf_counter()-start,
            'scope':'Exact finite grid only; no general barrier for this additional inequality family is claimed.'}
    Path(__file__).with_name('product_filtration_checks.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()

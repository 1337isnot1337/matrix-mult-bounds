#!/usr/bin/env python3
"""Exact partial fat-point coefficient controls, using integers only."""
from __future__ import annotations
import argparse
import json
from pathlib import Path


def verify(m, extra=0):
    n=m*(m+1)//2
    b=n+extra
    r=b+m
    h=b-m-1
    assert m>=4 and extra>=0 and h>m
    exponents=[0,m]+[k for k in range(1,m) if k!=2]
    assert len(exponents)==m and len(set(exponents))==m
    y_exponents=[0,b-1,h]
    products={d+e for d in exponents for e in y_exponents}
    assert len(products)==3*m-1
    complement=[k for k in range(r) if k not in products]
    assert len(complement)==b-2*m+1
    pairs=[(a,degree-a) for degree in range(m) for a in range(degree+1)]
    low_pairs=[(0,0),(0,1),(1,0)]
    z=[]
    unused=iter(complement)
    for a,c in pairs:
        degree=a+c
        if degree==m-1:
            z.append({exponents[a]})
        elif degree==m-2:
            z.append({b-1+exponents[a],h+exponents[a+1]})
        else:
            z.append({next(unused)})
    count=target_terms=0
    for i,d in enumerate(exponents):
        for yi,(a,aa) in enumerate(low_pairs):
            position=d+y_exponents[yi]
            for zi,(c,cc) in enumerate(pairs):
                actual=int(position in z[zi])
                expected=int(a+aa+c+cc==m-1 and i==a+c)
                assert actual==expected,(m,i,yi,zi,actual,expected)
                count+=1
                target_terms+=expected
    # The high rows have disjoint supports except within each row.
    # Their supports are disjoint from the chosen lower rows as well.
    supports=[support for support in z]
    assert all(supports)
    assert all(not (supports[i]&supports[j]) for i in range(n) for j in range(i))
    return {
        'm':m,'B':b,'N':n,'source_output_dimension':r,
        'shared_exponents_in_target_index_order':exponents,
        'first_three_input_exponents':y_exponents,
        'product_space_dimension':len(products),
        'lower_output_annihilator_dimension':len(complement),
        'all_first_three_input_coefficients_checked':count,
        'nonzero_target_terms_checked':target_terms,
        'full_output_rank':n,
        'constructs_full_target':False,
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-m',type=int,default=16)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.max_m<4:parser.error('--max-m must be at least four')
    records=[verify(m,extra) for m in range(4,args.max_m+1) for extra in (0,1,m)]
    report={
        'status':'exact integer partial-construction controls passed',
        'scope':'All coefficients involving target input degrees zero and one only.',
        'constructs_full_target':False,'improves_omega':False,
        'arithmetic':'integers and finite sets',
        'coefficient_checks':sum(r['all_first_three_input_coefficients_checked'] for r in records),
        'records':records,
    }
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps({k:v for k,v in report.items() if k!='records'}))
    else:print(json.dumps(report,indent=2))


if __name__=='__main__':main()

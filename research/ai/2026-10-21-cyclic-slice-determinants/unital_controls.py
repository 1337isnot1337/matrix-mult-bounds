"""Exact rank-budget controls for the conditional all-order unit proof.

These finite matrices check the linear-algebra bounds. They are not tensor
maps and do not replace the all-order argument in unital_chart.md.
"""

import argparse
from fractions import Fraction
import json
from pathlib import Path


def rank(matrix):
    if not matrix:return 0
    A=[[Fraction(v) for v in row] for row in matrix]
    active=0
    for c in range(len(A[0])):
        pivot=next((i for i in range(active,len(A)) if A[i][c]),None)
        if pivot is None:continue
        A[active],A[pivot]=A[pivot],A[active]
        u=A[active][c];A[active]=[v/u for v in A[active]]
        for i in range(active+1,len(A)):
            if A[i][c]:
                f=A[i][c];A[i]=[x-f*y for x,y in zip(A[i],A[active])]
        active+=1
        if active==len(A):break
    return active


def multiply(A,B):
    return [[sum(x*y for x,y in zip(row,column)) for column in zip(*B)] for row in A]


def sharp_leading_matrix(d,k,h):
    if not 1<=h<=k<=d:raise ValueError('require 1<=h<=k<=d')
    N=d+3*k+2;R=N-k
    M=[[0]*N for unused in range(N)]
    L=[[int(i==j and j<h) for j in range(k)] for i in range(R)]
    for i in range(d):M[i][i]=1
    for i in range(h,k):M[R+i][d+i-h]=1
    for j in range(k):M[d+k-h+j][R+j]=1
    return {'d':d,'k':k,'h':h,'N':N,'R':R,'source_matrix':M,'leading_L':L}


def verify_leading(w):
    d,k,h,N,R=(w[key] for key in ['d','k','h','N','R'])
    M,L=w['source_matrix'],w['leading_L']
    if N!=d+3*k+2 or R!=N-k or not 1<=h<=k<=d:raise ValueError('incorrect rank-control dimensions')
    if len(M)!=N or any(len(row)!=N for row in M) or len(L)!=R or any(len(row)!=k for row in L):
        raise ValueError('incorrect block matrix format')
    X11=[row[:R] for row in M[:R]];X21=[row[:R] for row in M[R:]]
    if any(v for row in multiply(L,X21) for v in row):raise ValueError('leading pole does not cancel')
    if any(v for row in X11[d:] for v in row) or any(v for row in L[d:] for v in row):
        raise ValueError('top or leading image leaves V')
    if rank(L)!=h or rank(X11)!=d or rank(M)!=d+2*k-h:
        raise ValueError('claimed sharp rank is wrong')
    return {'d':d,'k':k,'h':h,'actual_rank':rank(M),'upper_bound':d+2*k-h}


def constant_image_control():
    R=12;coefficients=[];constant=[[0]*R for unused in range(R)]
    for j in range(6):
        L=[[0]*2 for unused in range(R)];H=[[0]*R for unused in range(2)]
        for c in range(2):
            index=2*j+c
            if index<11:L[index][c]=1;H[c][index]=1
        coefficients.append({'negative_order':j+1,'L':L,'H':H})
        value=multiply(L,H)
        constant=[[x+y for x,y in zip(row,other)] for row,other in zip(constant,value)]
    return {'coefficients':coefficients,'constant_coefficient':constant,
            'scope':'Singular Laurent product control; raw constant coefficient alone is not a limit.'}


def verify_constant(w):
    coefficients=w['coefficients'];constant=[[0]*12 for unused in range(12)];columns=[]
    if len(coefficients)!=6:raise ValueError('missing pole coefficient')
    for j,row in enumerate(coefficients):
        if row['negative_order']!=j+1:raise ValueError('incorrect pole order')
        L,H=row['L'],row['H']
        if len(L)!=12 or any(len(r)!=2 for r in L) or len(H)!=2 or any(len(r)!=12 for r in H):
            raise ValueError('incorrect principal-coefficient format')
        columns+=list(zip(*L))
        value=multiply(L,H)
        constant=[[x+y for x,y in zip(r,s)] for r,s in zip(constant,value)]
    if (constant!=w['constant_coefficient'] or rank(constant)!=11 or rank(columns)!=11
            or w['scope']!='Singular Laurent product control; raw constant coefficient alone is not a limit.'):
        raise ValueError('incorrect constant-image rank or scope')
    powers={}
    for left in coefficients:
        for right in coefficients:
            exponent=right['negative_order']-left['negative_order']
            value=multiply(left['L'],right['H'])
            old=powers.setdefault(exponent,[[0]*12 for unused in range(12)])
            powers[exponent]=[[x+y for x,y in zip(r,s)] for r,s in zip(old,value)]
    nonzero=[e for e,M in powers.items() if any(v for row in M for v in row)]
    generic=[[sum(M[i][j] for M in powers.values()) for j in range(12)] for i in range(12)]
    if min(nonzero)!=-5 or rank(powers[-5])!=1 or rank(generic)!=2:
        raise ValueError('singular product or its regularization does not replay')
    return {'principal_image_dimension':11,'raw_constant_coefficient_rank':11,
            'inner_dimension':2,'product_pole_order':5,'regularized_constant_rank':1,
            'remaining_negative_terms':True,'full_Laurent_map':False}


def a4_budget():
    return {'source_dimension':112,'source_minimum_first_slice_rank':16,
            'source_minimum_row_slice_rank':16,'target_first_dimension':100,
            'long_dimension':110,'codimension':2,'target_minimum_slice_rank':11,
            'first_pole_source_rank_ceiling':6,'regular_correction_rank_ceiling':2,
            'first_limit_dimension_ceiling':98,'ordinary_slice_floor':12,
            'requires_regular_full_rank_long_leg':True,
            'requires_regular_invertible_source_unit_lift':True,
            'all_finite_pole_orders_excluded_under_hypotheses':True,
            'conclusion':'All-order exclusion only under the written unit-chart hypotheses.',
            'improves_omega':False}


def report():
    return {'sharp_rank_witnesses':[sharp_leading_matrix(2,2,h) for h in (1,2)],
            'constant_image_control':constant_image_control(),'A4_budget':a4_budget(),
            'proof_status':'written; unreviewed','improves_omega':False}


def verify(report):
    if report.get('proof_status')!='written; unreviewed' or report.get('improves_omega') is not False:
        raise ValueError('incorrect mathematical status')
    witnesses=report['sharp_rank_witnesses']
    if [(w['d'],w['k'],w['h']) for w in witnesses]!=[(2,2,1),(2,2,2)]:
        raise ValueError('incorrect sharpness coverage')
    receipts=[verify_leading(w) for w in witnesses]
    control=verify_constant(report['constant_image_control'])
    if report['A4_budget']!=a4_budget():raise ValueError('incorrect dimensions or missing hypotheses')
    if not 16>3*2 or not 11>2:
        raise ArithmeticError('invalid pole or correction rank budget')
    if not 100>112-16+2 or not 16-4>11:
        raise ArithmeticError('invalid dimension or ordinary gap')
    return {'sharp_rank_controls':receipts,'constant_image_control':control,
            'excluded_all_finite_pole_orders_under_hypotheses':True,
            'all_A4_degenerations_excluded':False,'improves_omega':False}



if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    value=json.loads(args.verify.read_text()) if args.verify else report()
    receipt=verify(value)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(value,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

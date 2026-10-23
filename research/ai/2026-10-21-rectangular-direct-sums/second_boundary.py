"""Exact finite controls for the written second-boundary argument."""
from fractions import Fraction as F
from itertools import product
from math import prod, factorial
import json
import argparse
from pathlib import Path


def derivative_value(k,j,z):
    return 0 if k<j else factorial(k)//factorial(k-j)*z**(k-j)


def rank_mod(A,p=101):
    A=[[int(x)%p for x in row] for row in A];i=0
    for j in range(len(A[0])):
        t=next((t for t in range(i,len(A)) if A[t][j]),None)
        if t is None:continue
        A[i],A[t]=A[t],A[i];v=pow(A[i][j],-1,p);A[i]=[(x*v)%p for x in A[i]]
        for t in range(i+1,len(A)):
            c=A[t][j];A[t]=[(x-c*y)%p for x,y in zip(A[t],A[i])]
        i+=1
        if i==len(A):break
    return i


def partitions(n,minimum=1):
    if n==0:
        yield []
    for k in range(minimum,n+1):
        for tail in partitions(n-k,k):yield [k]+tail


def verify_rank(r):
    m=3*r-2;points=list(range(1,r+1));relations=[]
    for degree in (0,1):
        rel=[]
        for z in points:
            others=[w for w in points if w!=z]
            g=F(1,prod((z-w)**3 for w in others))
            L1=sum((F(3,z-w) for w in others),F(0))
            L2=-sum((F(3,(z-w)**2) for w in others),F(0))
            gp=-L1*g;gpp=(L1*L1-L2)*g
            P=1 if degree==0 else z;Pp=degree
            rel.extend([(P*gpp+2*Pp*gp)/2,Pp*g+P*gp,P*g/2])
        for k in range(m):
            assert sum(rel[3*i+j]*derivative_value(k,j,z)
                       for i,z in enumerate(points) for j in range(3))==0
        relations.append(rel)
    assert relations[0][2]*relations[1][5]!=relations[0][5]*relations[1][2]
    jets=[[derivative_value(k,j,z) for z in points for j in range(3)] for k in range(m)]
    assert rank_mod(jets)==m
    lower=[[derivative_value(k,j,z) for z in points for j in range(2)] for k in range(m)]
    assert rank_mod(lower)==2*r
    nonreduced=0
    for parts in partitions(r):
        rho=len(parts)
        if rho==r:continue
        columns=[(i+1,j) for i,e in enumerate(parts) for j in range(e+2)]
        assert len(columns)==r+2*rho<=m
        A=[[derivative_value(k,j,z) for z,j in columns] for k in range(m)]
        assert rank_mod(A)==len(columns)
        nonreduced+=1
    return {'r':r,'length':m,'residue_relations':2,'full_jet_rank':m,
            'lower_jet_rank':2*r,'nonreduced_partitions_checked':nonreduced}


def verify_pencils():
    accepted=0
    for A in product((-1,0,1),repeat=3):
        for B in product((-1,0,1),repeat=3):
            det=lambda z:(A[0]+z*B[0])*(A[2]+z*B[2])-(A[1]+z*B[1])**2
            if any(det(z) for z in (0,1,2)):continue
            assert all(A[i]*B[j]==A[j]*B[i] for i in range(3) for j in range(3))
            accepted+=1
    # Two samples do not suffice: diag(1-z,z).
    assert (1-0)*0==0 and (1-1)*1==0 and (1-2)*2!=0
    return accepted


def exclusion(a,b,shapes,D):
    if (a+b+1)%3:return None
    r=(a+b+1)//3
    if not 3<=r<min(a,b):return None
    N=a*b*(a+b-1)
    for j,(m,n,p) in enumerate(shapes):
        for i,(d,t) in enumerate(zip((m*n,n*p,p*m),(p,m,n))):
            lift=t+2*N-sum(D)+D[i]
            if d>max(r,4)*a*b and lift<(r+1)*a*b:
                return {'block':j,'leg':i,'rank':r,'lift_upper':lift,
                        'next_rank_threshold':(r+1)*a*b,
                        'parameter_dimension':d,'image_cap':max(r,4)*a*b}
    return None

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    report={'rank_controls':[verify_rank(r) for r in range(3,9)],
            'rank_one_symmetric_pencils_verified':verify_pencils(),
            'status':'finite controls; general proof written and unreviewed'}
    args.output.write_text(json.dumps(report,indent=2)+'\n');print(report)

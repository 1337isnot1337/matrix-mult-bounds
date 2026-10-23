#!/usr/bin/env python3
"""Construct an explicit rational C(5,10) degeneration to T4.

SymPy is required only for this constructor. The saved witness can be
verified separately with Python's standard-library Fraction arithmetic.
"""
import sympy as s
from math import gcd
from functools import reduce
import random,json
from pathlib import Path

t=s.symbols('t')

def primitive(v):
    den=s.ilcm(*[x.q for x in v])
    ints=[int(x*den) for x in v]
    g=reduce(gcd,ints,0)
    return s.Matrix([x//g for x in ints])

def conv(a,b,length=None):
    c=[s.S.Zero]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c if length is None else c+[s.S.Zero]*(length-len(c))

def contraction(a,z,B=10):
    return s.Matrix([[sum(a[i,d]*z[j+d] for d in range(5)) for j in range(B)] for i in range(4)])

def solve_columns(mat,target):
    pivots=mat.rref()[1]
    chosen=mat[:,pivots]
    coeff=chosen.gauss_jordan_solve(target)[0]
    out=s.zeros(mat.cols,target.cols)
    for k,p in enumerate(pivots):out[p,:]=coeff[k,:]
    assert mat*out==target
    return out

def construct(seed):
    rng=random.Random(seed)
    # Constant monomial hyperplane missing t^2; change target shared basis later.
    A=s.Matrix([[int(i==d) for i in range(5)] for d in (0,4,1,3)])
    h=[s.Integer(rng.choice([-1,0,1])) for _ in range(6)];h[-1]=1
    w0=[s.Integer(rng.choice([-1,0,1])) for _ in range(10)];w0[0]=1
    oldlow=s.Matrix([w0,conv(h,list(A[1,:])),conv(h,list(A[0,:]))])
    P=s.Matrix([conv(list(A[i,:]),list(oldlow[j,:])) for i in range(4) for j in range(3)])
    if P.rank()!=11:return None,'first rank'
    E=[primitive(v) for v in P.nullspace()]
    assert len(E)==3
    z0=E[0]+E[1]+E[2]
    z1,z2=E[:2]
    F=contraction(A,z0)
    if F.rank()!=4:return None,'z0 rank'
    W=oldlow
    mids=[]
    for v in F.nullspace():
        v=primitive(v).T
        if W.col_join(v).rank()>W.rows:
            W=W.col_join(v);mids.append(list(v))
    if len(mids)!=3:return None,'middle quotient'
    M=s.Matrix(mids)
    L0=M*contraction(A,z1).T
    L1=M*contraction(A,z2).T
    pencil=L1-t*L0
    kernel=[s.expand((-1)**i*pencil[:,[j for j in range(4) if j!=i]].det()) for i in range(4)]
    common=s.gcd_list(kernel)
    kernel=[s.cancel(v/common) for v in kernel]
    if max(s.degree(v,t) for v in kernel if v)!=3:return None,'minimal index'
    C=s.Matrix([[s.expand(v).coeff(t,j) for j in range(4)] for v in kernel])
    if C.det()==0:return None,'cofactor basis'
    flat=primitive(list(C))
    C=s.Matrix(4,4,list(flat))
    D=L0*C[:,:3]
    assert L0*C==D.row_join(s.zeros(3,1))
    assert L1*C==s.zeros(3,1).row_join(D)
    if D.det()==0:return None,'pencil left basis'
    Anew=C.T*A
    Mnew=D.inv()*M
    old_coeff=(C.T).inv()
    old_u0=list(old_coeff[0,:]);old_u1=list(old_coeff[1,:])
    compatibility=s.Matrix([[old_u0[i],old_u1[i],-old_u0[i+1],-old_u1[i+1]] for i in range(3)])
    possibilities=compatibility.nullspace()
    if not possibilities:return None,'low relation'
    solution=primitive(possibilities[0])
    aa,bb,cc,dd=solution
    if aa*dd-bb*cc==0:return None,'low basis determinant'
    u=aa*A[0,:]+bb*A[1,:]
    v=cc*A[0,:]+dd*A[1,:]
    low=s.Matrix([w0,conv(h,list(v)),conv(h,list(u))])
    Fnew=contraction(Anew,z0)
    top=solve_columns(Fnew,s.eye(4)).T
    Y=low.col_join(Mnew).col_join(top)
    assert Y.rank()==10
    Plow=s.Matrix([conv(list(Anew[i,:]),list(low[j,:])) for i in range(4) for j in range(3)])
    pairs=[(a,d-a) for d in range(4) for a in range(d+1)]
    target=s.Matrix([[int(sum(pairs[j])+sum(pairs[z])==3 and i==pairs[j][0]+pairs[z][0]) for z in range(3,10)] for i in range(4) for j in range(3)])
    Ztop=solve_columns(Plow,target).T
    Z=s.Matrix([list(z0),list(z1),list(z2)]).col_join(Ztop)
    assert Z.rank()==10
    weightsY=[max(0,a+b-1) for a,b in pairs]
    weightsZ=[-max(0,3-a-b-1) for a,b in pairs]
    zero=negative=positive=0
    remainder=[]
    for i in range(4):
        for j in range(10):
            poly=conv(list(Anew[i,:]),list(Y[j,:]))
            for k in range(10):
                coeff=sum(x*y for x,y in zip(poly,Z[k,:]))
                exponent=weightsY[j]+weightsZ[k]
                desired=int(sum(pairs[j])+sum(pairs[k])==3 and i==pairs[j][0]+pairs[k][0])
                if exponent<0:
                    assert coeff==0,('negative',i,j,k,coeff);negative+=1
                elif exponent==0:
                    assert coeff==desired,('constant',i,j,k,coeff,desired);zero+=1
                elif coeff:
                    remainder.append([i,j,k,exponent,str(coeff)]);positive+=1
    return {'status':'exact rational full-tensor coefficient identity verified','seed':seed,
            'source':'C(5,10)','target':'T4','a_map':[[str(x) for x in Anew.row(i)] for i in range(4)],
            'y':[[str(x) for x in Y.row(i)] for i in range(10)],
            'z':[[str(x) for x in Z.row(i)] for i in range(10)],
            'y_weights':weightsY,'z_weights':weightsZ,
            'negative_coefficients_checked':negative,'constant_coefficients_checked':zero,
            'nonzero_positive_remainder_terms':positive,'remainder':remainder,
            'initial_h':[str(x) for x in h],'initial_w0':[str(x) for x in w0],
            'source_shared_hyperplane_missing_monomial':2,
            'improves_omega':False},None

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,default=0)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result,error=construct(args.seed)
    if result is None:
        raise SystemExit(json.dumps({'seed':args.seed,'rejected':error}))
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({k:v for k,v in result.items() if k not in ('a_map','y','z','remainder')}))
    else:print(json.dumps(result,indent=2))

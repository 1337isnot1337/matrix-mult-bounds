#!/usr/bin/env python3
"""Exact constructive probe for independently based m5 sectors with slack."""
import sympy as s
from math import gcd
from functools import reduce
import argparse,random,json
from pathlib import Path
t=s.symbols('t')

def prim(v):
    den=s.ilcm(*[x.q for x in v]);v=[int(x*den) for x in v]
    g=reduce(gcd,v,0)
    return s.Matrix([x//g for x in v])

def solvecols(M,T):
    piv=M.rref()[1];C=M[:,piv];x=C.gauss_jordan_solve(T)[0]
    out=s.zeros(M.cols,T.cols)
    for i,p in enumerate(piv):out[p,:]=x[i,:]
    assert M*out==T
    return out

def attempt(seed):
    rng=random.Random(seed)
    m=5;B=20;N=15;H=14;R=25
    A=s.Matrix([[int(i==d) for i in range(6)] for d in [0,1,3,4,5]])
    F=s.Matrix([[rng.choice([-1,0,1]) for _ in range(6)] for __ in range(3)])
    if F.rank()!=3 or F[0,5]==0 or F[0,2]==0:return None,'F'
    moment=[s.Integer(rng.choice([-1,0,1])) for _ in range(2*H)]+[s.S.Zero]*(2*B+m-1-2*H)
    moment[2*H-1]=1
    Uforms=[s.Matrix([[sum(A[i,d]*moment[j+k+d] for d in range(6)) for k in range(B)] for j in range(B)]) for i in range(m)]
    low=s.zeros(3,B);low[:,H:H+6]=F
    Fl=s.Matrix.vstack(*[low*M for M in Uforms])
    if Fl.rank()!=11:return None,'UF rank'
    # A basis of the three-dimensional quotient of the common annihilator.
    rev=[moment[2*H-1-i] for i in range(H)]
    inv=[s.S.One]+[s.S.Zero]*(H-1)
    for n in range(1,H):inv[n]=-sum(rev[k]*inv[n-k] for k in range(1,n+1))
    mid=s.Matrix([[s.S.Zero]*i+inv[:H-i]+[s.S.Zero]*(B-H) for i in range(3)])
    assert Fl*mid.T==s.zeros(15,3)
    central=[mid*M*mid.T for M in Uforms]
    assert all(K[i,j]==K[0,i+j] if i+j<3 else K[i,j]==K[i+j-2,2] for K in central for i in range(3) for j in range(3))
    Hmid=s.Matrix([[K[0,0],K[0,1],K[0,2],K[1,2],K[2,2]] for K in central])
    if Hmid.det()==0:return None,'central rank'
    F0=s.Matrix.vstack(*[low[0,:]*M for M in Uforms])
    if F0.rank()!=5:return None,'F0'
    W=s.Matrix.vstack(*[prim(v).T for v in Fl.nullspace()])
    assert W.rows==9
    reps=[]
    for v in F0.nullspace():
        row=prim(v).T
        if W.col_join(row).rank()>W.rows:
            W=W.col_join(row);reps.append(list(row))
    assert len(reps)==6
    reps=s.Matrix(reps)
    good=None
    for trial in range(10):
        mixing=s.Matrix([[rng.choice([-1,0,1]) for _ in range(6)] for __ in range(4)])
        M=mixing*reps
        L0=s.Matrix.hstack(*[M*Ui*low[1,:].T for Ui in Uforms])
        L1=s.Matrix.hstack(*[M*Ui*low[2,:].T for Ui in Uforms])
        P=L1-t*L0
        kernel=[s.expand((-1)**i*P[:,[j for j in range(5) if j!=i]].det()) for i in range(5)]
        if all(v==0 for v in kernel):continue
        div=s.gcd_list(kernel);kernel=[s.cancel(v/div) for v in kernel]
        if max(s.degree(v,t) for v in kernel if v)!=4:continue
        C=s.Matrix([[s.expand(v).coeff(t,j) for j in range(5)] for v in kernel])
        if C.det()==0:continue
        C=s.Matrix(5,5,list(prim(list(C))))
        D=L0*C[:,:4]
        if D.det()==0:continue
        assert L0*C==D.row_join(s.zeros(4,1))
        assert L1*C==s.zeros(4,1).row_join(D)
        good=(D.inv()*M,C.inv().T);break
    if good is None:return None,'high pencil'
    high,Hpair=good
    top=solvecols(F0,s.eye(5)).T
    Y=low.col_join(mid).col_join(high).col_join(top)
    assert Y.rank()==N
    Z=s.Matrix([[sum(Y[y,j]*moment[j+k] for j in range(B)) for k in range(R)] for y in range(N)])
    assert Z.rank()==N
    blocks=[s.eye(5),Hpair,Hmid,Hpair,s.eye(5)]
    pairs=[(a,p-a) for p in range(5) for a in range(p+1)]
    checked=0
    for i,Ui in enumerate(Uforms):
        coeff=Y*Ui*Y.T
        for j,(a,b) in enumerate(pairs):
            for k,(c,d) in enumerate(pairs):
                e=a+b+c+d-4
                if e<=0:
                    want=blocks[a+b][i,a+c] if e==0 else s.S.Zero
                    assert coeff[j,k]==want,(seed,i,j,k,coeff[j,k],want)
                    checked+=1
    return {'status':'exact independent-sector finite degeneration verified','source':'C(6,20)','target':'m5 degree sectors with separate invertible shared maps',
            'seed':seed,'a_map':[[str(x) for x in A.row(i)] for i in range(5)],
            'y':[[str(x) for x in Y.row(i)] for i in range(N)],
            'z':[[str(x) for x in Z.row(i)] for i in range(N)],
            'shared_sector_maps':[[[str(x) for x in block.row(i)] for i in range(5)] for block in blocks],
            'y_degree_weights':[-2,-1,0,1,2],'z_degree_weights':[-2,-1,0,1,2],
            'nonpositive_coefficients_checked':checked,'shared_sector_determinants':[str(M.det()) for M in blocks],
            'F':[[str(x) for x in F.row(i)] for i in range(3)],'moment_sequence':[str(x) for x in moment],
            'improves_omega':False},None

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,default=2)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result,error=attempt(args.seed)
    if result is None:
        raise RuntimeError(f'Seed {args.seed} rejected: {error}')
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
                     ['a_map','y','z','shared_sector_maps','moment_sequence','F']}))

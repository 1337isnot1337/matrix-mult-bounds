"""Exact finite controls for the all-field affine-z biform rank proof."""
import json
import random
from itertools import product


def trim(a):
    a=list(a)
    while a and a[-1] == 0: a.pop()
    return a


def rem(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b])
    while len(a)>=len(b):
        q=a[-1]*pow(b[-1],-1,p)%p
        t=len(a)-len(b)
        for j,x in enumerate(b): a[t+j]=(a[t+j]-q*x)%p
        a=trim(a)
    return a


def primitive_degree(u,v,p):
    u=trim([x%p for x in u]);v=trim([x%p for x in v])
    if not u or not v: return 0
    x,y=u,v
    while y: x,y=y,rem(x,y,p)
    return max(len(u)-len(x),len(v)-len(x))


def matrix(a,b,u,v,p):
    m=a+b-1
    out=[[0]*(a*m) for _ in range(b*m)]
    for j in range(b):
        for L in range(m):
            for H in range(m):
                i=H-j
                for r in range(a):
                    s=L-r
                    if s==0 and 0<=i<len(u):out[j*m+L][H*a+r]=u[i]%p
                    if s==1 and 0<=i<len(v):out[j*m+L][H*a+r]=v[i]%p
    return out


def rank(rows,p):
    A=[row[:] for row in rows];n=len(A);m=len(A[0]);k=0
    for j in range(m):
        t=next((i for i in range(k,n) if A[i][j]),None)
        if t is None:continue
        A[k],A[t]=A[t],A[k]
        inv=pow(A[k][j],-1,p)
        for h in range(j,m):A[k][h]=A[k][h]*inv%p
        for i in range(k+1,n):
            c=A[i][j]
            if c:
                for h in range(j,m):A[i][h]=(A[i][h]-c*A[k][h])%p
        k+=1
        if k==n:break
    return k


def check(a,b,u,v,p):
    if not any(u) and not any(v):return False
    d=primitive_degree(u,v,p)
    predicted=a*b+min(b,a*d)
    got=rank(matrix(a,b,u,v,p),p)
    if got!=predicted:
        raise AssertionError((a,b,u,v,p,d,got,predicted))
    return True


def verify():
    counts={'exhaustive':0,'seeded':0,'spectrum':0}
    for p in (2,3):
        for a in (2,3):
            for b in range(a,7):
                vecs=[v for v in product(range(p),repeat=a) if any(v)]
                for u in vecs:
                    for v in vecs:
                        if check(a,b,u,v,p):counts['exhaustive']+=1
    rng=random.Random(20261023)
    for p in (2,3,5,7,101):
        for a in range(2,6):
            for b in range(a,11):
                for _ in range(20):
                    u=[rng.randrange(p) for _ in range(a)]
                    v=[rng.randrange(p) for _ in range(a)]
                    if check(a,b,u,v,p):counts['seeded']+=1
            for b in range(a,12):
                for d in range(a):
                    if check(a,b,[1],[0]*d+[1],p):counts['spectrum']+=1
    return {'status':'pass','seed':20261023,**counts,
            'scope':'finite checks; written proof gives all-field theorem; no exponent claim'}

if __name__=='__main__':print(json.dumps(verify(),indent=2,sort_keys=True))

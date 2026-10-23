"""Independent rational upper / modular lower exact rank certificates.

Term placement does not import verify.py. A full modular-rank minor is
not exported, but rank equality modulo a prime supplies a rational lower
bound, while rational polynomial null vectors supply the opposite bound.
"""
from fractions import Fraction as Q
from random import Random
import json

P=1000003


def coefficient_matrix(a,b,alpha,v,gamma):
    m=a+b-1
    R=[[0]*(a*m) for _ in range(b*m)]
    for i,j,c in [(0,0,alpha),(0,2,gamma)]+[(k,1,w) for k,w in enumerate(v) if w]:
        for rowx in range(b):
            H=rowx+i
            for r in range(a):
                L=r+j
                R[rowx*m+L][H*a+r]+=c
    return R


def modular_rank(A):
    a=[list(map(lambda z:int(z)%P,row)) for row in A]
    h=0
    for c in range(len(a[0])):
        pivot=next((i for i in range(h,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[h],a[pivot]=a[pivot],a[h]
        x=pow(a[h][c],-1,P)
        a[h]=[(z*x)%P for z in a[h]]
        for i in range(len(a)):
            if i!=h and a[i][c]:
                t=a[i][c]
                a[i]=[(z-t*w)%P for z,w in zip(a[i],a[h])]
        h+=1
        if h==len(a):break
    return h


def polyadd(u,v):
    a=[Q(0)]*max(len(u),len(v))
    for i,x in enumerate(u):a[i]+=x
    for i,x in enumerate(v):a[i]+=x
    while a and a[-1]==0:a.pop()
    return a


def poly_mul(u,v):
    if not u or not v:return []
    a=[Q(0)]*(len(u)+len(v)-1)
    for i,x in enumerate(u):
        for j,y in enumerate(v):a[i+j]+=x*y
    while a and a[-1]==0:a.pop()
    return a


def scale(u,c):
    return [x*c for x in u]


def central_basis_vector(a,alpha,v,gamma,leg,degree):
    center=a//2 if a%2==0 else (a+1)//2
    rows=[[] for _ in range(a+2)]
    rows[center+leg]=[Q(0)]*degree+[Q(1)]
    for i in range(center-1,-1,-1):
        rows[i]=scale(polyadd(poly_mul(v,rows[i+1]),scale(rows[i+2],gamma)),-Q(1,alpha))
    for i in range(center,a):
        rows[i+2]=scale(polyadd(scale(rows[i],alpha),poly_mul(v,rows[i+1])),-Q(1,gamma))
    return rows


def verify():
    rng=Random(292929)
    checks=vectors=0
    for a in range(2,8):
        for b in range(3,9):
            alpha=rng.choice([-3,-2,-1,1,2,3])
            gamma=rng.choice([-3,-2,-1,1,2,3])
            v=[Q(rng.randrange(-2,3)) for _ in range(a)]
            d=max([i for i,c in enumerate(v) if c] or [0])
            target=a*b+min(b,((a+1)//2)*d)+min(b,(a//2)*d)
            R=coefficient_matrix(a,b,alpha,v,gamma)
            assert modular_rank(R)==target,(a,b,'modular rank')
            k=0
            for leg,limit in enumerate((b-((a+1)//2)*d,b-(a//2)*d)):
                for degree in range(max(0,limit)):
                    rows=central_basis_vector(a,alpha,v,gamma,leg,degree)
                    assert all(len(z)<=b for z in rows)
                    m=a+b-1
                    for H in range(m):
                        for r in range(a):
                            summed=sum((rows[L][j] if j<len(rows[L]) else Q(0))*R[j*m+L][H*a+r] for L in range(a+2) for j in range(b))
                            assert summed==0,(a,b,H,r)
                    vectors+=1;k+=1
            assert k==(a+2)*b-target
            checks+=1
    return {'status':'pass','field':'Q','independent_terms':checks,'exact_rational_kernel_vectors':vectors,'modular_prime':P,'seed':292929}

if __name__=='__main__':print(json.dumps(verify(),indent=2))

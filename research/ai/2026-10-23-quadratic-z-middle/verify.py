"""Exact all-field polynomial-middle quadratic-z source-slice rank controls.

Standalone standard-library verifier. The source matrix is constructed literally.
"""
from itertools import product
from random import Random
import json


def rank_mod(matrix, p):
    A = [[v % p for v in row] for row in matrix]
    if not A:
        return 0
    nr, nc = len(A), len(A[0])
    piv = 0
    for c in range(nc):
        r = next((j for j in range(piv, nr) if A[j][c]), None)
        if r is None:
            continue
        A[piv], A[r] = A[r], A[piv]
        v = pow(A[piv][c], -1, p)
        A[piv][c:] = [x * v % p for x in A[piv][c:]]
        for j in range(piv + 1, nr):
            w = A[j][c]
            if w:
                A[j][c:] = [(x - w * y) % p for x, y in zip(A[j][c:], A[piv][c:])]
        piv += 1
        if piv == nr:
            break
    return piv


def source_matrix(a, b, alpha, middle, gamma, p):
    m = a + b - 1
    rows = [[0] * (a * m) for _ in range(b * m)]
    for j in range(b):
        for L in range(m):
            row = rows[j * m + L]
            for H in range(m):
                i = H-j
                for r in range(a):
                    s = L-r
                    c = alpha if (s == 0 and i == 0) else \
                        (middle[i] if s == 1 and 0 <= i < len(middle) else \
                         (gamma if s == 2 and i == 0 else 0))
                    row[H*a+r] = c % p
    return rows


def prediction(a, b, middle):
    d = len(middle) - 1
    while d >= 0 and middle[d] == 0:
        d -= 1
    if d < 0:
        d = 0
    return (a + 2) * b - max(0, b - ((a + 1) // 2) * d) - max(0, b - (a // 2) * d)


def trim(xs):
    xs=list(xs)
    while xs and xs[-1] == 0:
        xs.pop()
    return xs

def polyadd(*xs, p):
    n = max(map(len, xs), default=0)
    return trim([sum(x[i] if i < len(x) else 0 for x in xs) % p for i in range(n)])


def mul(a, b, p):
    if not a or not b:
        return []
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] = (out[i+j] + x*y)%p
    return trim(out)


def central_solution(a, alpha, middle, gamma, h, k, p):
    """From the central consecutive pair, solve the recursion both ways."""
    center = a // 2 if a % 2 == 0 else (a+1)//2
    v = [[] for _ in range(a+2)]
    v[center],v[center+1] = h,k
    for i in range(center-1,-1,-1):
        v[i] = polyadd(mul(middle, v[i+1], p), [(gamma*x)%p for x in v[i+2]],p=p)
        v[i] = trim([(-pow(alpha,-1,p)*x)%p for x in v[i]])
    for i in range(center,a):
        v[i+2] = polyadd([(alpha*x)%p for x in v[i]], mul(middle,v[i+1],p),p=p)
        v[i+2] = trim([(-pow(gamma,-1,p)*x)%p for x in v[i+2]])
    return v


def kernel_basis(a,b,alpha,middle,gamma,p):
    d = len(middle) -1
    while d >= 0 and middle[d] == 0:
        d -= 1
    d = max(0,d)
    limits = (b - ((a+1)//2)*d, b - (a//2)*d)
    for leg, lim in enumerate(limits):
        for k in range(max(0,lim)):
            h = [0]*k+[1] if leg == 0 else []
            v = [0]*k+[1] if leg == 1 else []
            yield central_solution(a,alpha,middle,gamma,h,v,p)


def check_case(a,b,alpha,middle,gamma,p,check_basis=True):
    assert a >= 2 and b >= 3 and len(middle) <= a and alpha%p and gamma%p
    expected=prediction(a,b,middle)
    R=source_matrix(a,b,alpha,middle,gamma,p)
    observed=rank_mod(R,p)
    assert observed==expected, (a,b,p,alpha,middle,gamma,observed,expected)
    if check_basis:
        basis=list(kernel_basis(a,b,alpha,middle,gamma,p))
        assert len(basis)==b*(a+2)-expected
        m=a+b-1
        for v in basis:
            assert all(len(poly)<=b for poly in v)
            for H in range(m):
                for r in range(a):
                    c = sum((v[L][j] if j<len(v[L]) else 0)*R[j*m+L][H*a+r] for L in range(a+2) for j in range(b))%p
                    assert c==0, (a,b,p,H,r)
        flat=[]
        for v in basis:
            flat.append([v[L][j] if j<len(v[L]) else 0 for j in range(b) for L in range(a+2)])
        assert rank_mod(flat,p)==len(basis)
    return len(R), len(R[0])


def verify():
    rng=Random(20261023)
    count={'exhaustive':0,'seeded':0,'basis_vectors':0,'spectrum':0}
    # Exhaust all polynomial middle coefficients over small fields, including zero,
    # with arbitrary nonzero constant outer coefficients.
    for p in (2,3):
        for a in range(2,5):
            for b in range(3,7):
                for middle in product(range(p),repeat=a):
                    alpha=1
                    gamma=1 if p==2 else 2
                    check_case(a,b,alpha,list(middle),gamma,p,check_basis=True)
                    count['exhaustive']+=1
    for p in (2,3,5,7,101):
        for a in range(2,8):
            for b in range(3,11):
                for rep in range(4):
                    alpha=rng.randrange(1,p)
                    gamma=rng.randrange(1,p)
                    middle=[rng.randrange(p) for _ in range(a)]
                    check_case(a,b,alpha,middle,gamma,p,check_basis=False)
                    count['seeded']+=1
            for d in range(a):
                b=3+a
                middle=[0]*d+[1]
                check_case(a,b,1,middle,1,p,check_basis=True)
                count['spectrum']+=1
                count['basis_vectors']+=len(list(kernel_basis(a,b,1,middle,1,p)))
    return {'status':'pass','fixed_seed':20261023,**count,'scope':'finite matrix and kernel controls; no asymptotic or exponent claim'}

if __name__=='__main__':
    print(json.dumps(verify(),sort_keys=True,indent=2))

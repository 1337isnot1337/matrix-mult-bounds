"""All-field universal rank witnesses for two equal-degree quadratic biforms.

The proof is an integer minor of determinant +/-1 (lower rank bound in
any characteristic), together with independent integral left-null vectors
(upper bound over every field). No modular-rank heuristic is used.
"""
from pathlib import Path
import json

WITNESS = Path(__file__).with_name('certificate_equal_degrees.json')


def source_matrix(a, b, u, v, w):
    m = a+b-1
    R = [[0]*(a*m) for _ in range(b*m)]
    for z_index, p in enumerate((u, v, w)):
        for x_index, c in enumerate(p):
            if not c:
                continue
            for j in range(b):
                for r in range(a):
                    R[j*m + r + z_index][(j+x_index)*a+r] += c
    return R


def det_bareiss(M):
    A=[row[:] for row in M]
    n=len(A)
    if not n:return 1
    assert all(len(row)==n for row in A)
    prev=1
    sign=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:
            A[pivot],A[k]=A[k],A[pivot]
            sign=-sign
        akk=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                t=A[i][j]*akk-A[i][k]*A[k][j]
                assert t%prev == 0, (i,j,k,t,prev)
                A[i][j]=t//prev
            A[i][k]=0
        prev=akk
    return sign*A[-1][-1]


def rank_mod(M,p):
    A=[[int(v)%p for v in row] for row in M]
    n=len(A);m=len(A[0]);h=0
    for j in range(m):
        pivot=next((i for i in range(h,n) if A[i][j]),None)
        if pivot is None:continue
        A[pivot],A[h]=A[h],A[pivot]
        inverse=pow(A[h][j],-1,p)
        A[h][j:]=[(v*inverse)%p for v in A[h][j:]]
        for i in range(h+1,n):
            t=A[i][j]
            if t:A[i][j:]=[(v-t*w)%p for v,w in zip(A[i][j:],A[h][j:])]
        h+=1
        if h==n:break
    return h


def check_certificate(entry,a=4,b=3):
    coeff=entry['coefficients']
    u,v,w=(coeff[x] for x in ('u','v','w'))
    R=source_matrix(a,b,u,v,w)
    m=a+b-1
    assert len(R)==b*m and len(R[0])==a*m
    rank=entry['claimed_rank']
    rows,columns=entry['rows'],entry['columns']
    assert len(rows)==len(columns)==rank
    assert len(set(rows))==rank and len(set(columns))==rank
    assert all(0<=x<len(R) for x in rows)
    assert all(0<=x<len(R[0]) for x in columns)
    minor=[[R[i][j] for j in columns] for i in rows]
    assert det_bareiss(minor)==entry['determinant']
    assert abs(entry['determinant'])==1
    basis=entry['kernel']
    assert len(basis)==len(R)-rank
    assert all(len(v)==len(R) for v in basis)
    coords=entry['independence_columns']
    assert len(coords)==len(basis) and len(set(coords))==len(coords)
    assert abs(det_bareiss([[u[c] for c in coords] for u in basis]))==1
    for vec in basis:
        for col in range(len(R[0])):
            assert sum(vec[row]*R[row][col] for row in range(len(R)))==0
    assert [len(u)-1,len(v)-1,len(w)-1]==[0,1,1]
    assert u==[1]  # unit primitive gcd, in every field
    for p in (2,3,5,101):assert rank_mod(R,p)==rank
    return rank


def verify():
    witness=json.loads(WITNESS.read_text())
    assert witness['a']==4 and witness['b']==3
    ranks={case['name']:check_certificate(case,witness['a'],witness['b']) for case in witness['cases']}
    assert ranks=={'factorable':15,'nonfactorable':16}
    return {'status':'pass','field_scope':'every field','certificates':len(ranks),'sizes':'18x24', 'ranks':ranks,'signed_unit_minors':True,'integral_kernel_vectors':5}

if __name__=='__main__':print(json.dumps(verify(),indent=2,sort_keys=True))

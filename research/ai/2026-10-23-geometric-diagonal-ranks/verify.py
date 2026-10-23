#!/usr/bin/env python3
"""Independent exact controls for the geometric diagonal-source rank theorem.

The theorem is proved in proof.md. These finite controls are not a proof.
All arithmetic in the acceptance calculations is over small prime fields.
"""
import argparse
import json
from pathlib import Path


def rank_mod(rows, prime):
    a = [[x % prime for x in row] for row in rows]
    if not a:
        return 0
    pivot = 0
    for col in range(len(a[0])):
        i = next((j for j in range(pivot, len(a)) if a[j][col]), None)
        if i is None:
            continue
        a[pivot], a[i] = a[i], a[pivot]
        inv = pow(a[pivot][col], -1, prime)
        a[pivot] = [v * inv % prime for v in a[pivot]]
        for j in range(pivot + 1, len(a)):
            factor = a[j][col]
            if factor:
                a[j] = [(x-factor*y) % prime for x, y in zip(a[j], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def geometric_coeff(k, degree, scalar, ratio, prime):
    return scalar * pow(ratio, k, prime) % prime if 0 <= k <= degree else 0


def toeplitz(size, degree, left, scalar, ratio, prime):
    return [[geometric_coeff(left + v - u, degree, scalar, ratio, prime)
             for v in range(size)] for u in range(size)]


def full_source(size, degree, scalar, ratio, prime):
    """Reconstruct the literal coefficient tensor without Toeplitz blocks."""
    n = size * (2*size-1)
    out = [[0]*n for _ in range(n)]
    for j in range(size):
        for low in range(2*size-1):
            for high in range(2*size-1):
                k = high-j
                if 0 <= k <= degree:
                    right = low-k
                    if 0 <= right < size:
                        out[j*(2*size-1)+low][high*size+right] = (
                            scalar * pow(ratio,k,prime) % prime)
    return out


def index_block(size, degree, index, scalar, ratio, prime):
    indices = range(max(0, index-2*size+2), min(size-1,index)+1)
    return [[geometric_coeff(index-u-v,degree,scalar,ratio,prime)
             for v in indices] for u in indices]


def residue_sets(size, degree, left):
    m=degree+1
    right=degree-left
    killed_left=set(range(right+1,m))
    killed_right={(size-m+i)%m for i in range(right)}
    free=sorted(set(range(m))-killed_left-killed_right)
    return killed_left, killed_right, free


def kernel_basis(size, degree, left, ratio, prime):
    _,_,free=residue_sets(size,degree,left)
    root=free[0]
    m=degree+1
    return [[(int(i%m==j)-int(i%m==root))*pow(ratio,-i,prime)%prime
             for i in range(size)] for j in free[1:]]


def verify():
    counts={key:0 for key in ('toeplitz_ranks','kernel_vectors',
        'individual_nullities','conserved_index_blocks','literal_full_matrices')}
    for a in range(2,14):
        for d in range(1,a):
            m=d+1
            q=a%m
            predicted_defect=(q-1)*(m-q) if q else 0
            for prime in (2,3,5,7,11):
                for ratio in (1,) if prime==2 else (1,2):
                    scalar=1 if prime==2 else prime-1
                    total_defect=0
                    for left in range(1,m):
                        t=toeplitz(a,d,left,scalar,ratio,prime)
                        killed_l,killed_r,free=residue_sets(a,d,left)
                        defect=len(free)-1
                        formula=(min(left,d-left,q-1,m-q) if q else 0)
                        assert defect==len(killed_l & killed_r)==formula
                        basis=kernel_basis(a,d,left,ratio,prime)
                        assert len(basis)==defect
                        assert rank_mod(basis,prime)==defect
                        for v in basis:
                            assert all(sum(x*y for x,y in zip(row,v))%prime==0
                                       for row in t)
                            counts['kernel_vectors']+=1
                        assert a-rank_mod(t,prime)==defect
                        counts['toeplitz_ranks']+=1
                        counts['individual_nullities']+=1
                        total_defect+=defect
                    assert total_defect==predicted_defect
                    if a<=10 and prime in (2,3,5):
                        blocks=[index_block(a,d,s,scalar,ratio,prime)
                                for s in range(3*a-2)]
                        assert sum(rank_mod(b,prime) for b in blocks)==a*a+a*d-predicted_defect
                        counts['conserved_index_blocks']+=1
                    if a<=6 and prime in (2,3,5):
                        assert rank_mod(full_source(a,d,scalar,ratio,prime),prime)==(
                            a*a+a*d-predicted_defect)
                        counts['literal_full_matrices']+=1
    return {'result':'PASS','counts':counts,
            'scope':'bounded exact finite controls over F2,F3,F5,F7,F11; '
                    'proof over every field is separate'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    report=json.dumps(verify(),sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(report,encoding='utf-8')
    print(report,end='')


if __name__=='__main__':
    main()

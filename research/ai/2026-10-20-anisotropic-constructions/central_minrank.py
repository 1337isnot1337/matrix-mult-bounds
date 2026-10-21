"""Exact central-block triangular minors for cyclic convolution sources.

This verifies the coefficient identity behind the written minimum-rank proof.
It does not turn a finite search into an arbitrary-degeneration exclusion.
"""
from itertools import product


def central_entry(f, a, b, row, column):
    """Row=(j,p), column=(q,r), first-leg slice f=(i,s)."""
    j, p = row
    q, r = column
    i, s = q+r-j, j+p-r
    return f[i*b+s] if 0 <= i < a and 0 <= s < b else 0


def central_minor(f, a, b):
    if not 1 <= a <= b or len(f) != a*b:
        raise ValueError("The stated convention requires 1<=a<=b and ab coefficients")
    if not any(f):
        raise ValueError("The zero slice has no nonzero minor")
    degree = next(k for k in range(a+b-1)
                  if any(f[i*b+k-i] for i in range(a)
                         if 0 <= k-i < b))
    i0 = max(i for i in range(a)
             if 0 <= degree-i < b and f[i*b+degree-i])
    s0 = degree-i0
    p0 = min(s0, a-1)
    shift = s0-p0
    q0 = i0+shift
    rows = [(r+shift, p0) for r in range(a)]
    columns = [(q0, r) for r in range(a)]
    if not (0 <= q0 < b and 0 <= shift <= b-a):
        raise ArithmeticError("Constructed coordinates leave the source")
    matrix = [[central_entry(f,a,b,row,col) for col in columns]
              for row in rows]
    pivot = f[i0*b+s0]
    for r in range(a):
        if matrix[r][r] != pivot or any(matrix[r][s] for s in range(r+1,a)):
            raise ArithmeticError("Claimed minor is not triangular with the stated pivot")
    return matrix, pivot


def source_matrix(f, a, b):
    return [[central_entry(f,a,b,row,column)
             for column in product(range(b),range(a))]
            for row in product(range(b),range(a))]


def rank_mod_two(matrix):
    basis = {}
    for row in matrix:
        word = sum((int(value)&1)<<j for j,value in enumerate(row))
        while word:
            pivot = word.bit_length()-1
            if pivot in basis:
                word ^= basis[pivot]
            else:
                basis[pivot] = word
                break
    return len(basis)


def controls():
    records = []
    for a,b in ((1,3),(2,2),(2,3),(3,3)):
        histogram = {}
        for bits in range(1,1<<(a*b)):
            f = [(bits>>j)&1 for j in range(a*b)]
            central_minor(f,a,b)
            rank = rank_mod_two(source_matrix(f,a,b))
            if rank < a:
                raise ArithmeticError("A finite slice contradicts the proven minor")
            histogram[rank] = histogram.get(rank,0)+1
        corner = [1]+[0]*(a*b-1)
        if rank_mod_two(source_matrix(corner,a,b)) != a:
            raise ArithmeticError("The corner does not attain the claimed minimum")
        records.append({"a":a,"b":b,"nonzero_slices":(1<<(a*b))-1,
                        "rank_histogram":histogram})
    return records


if __name__ == "__main__":
    import json
    print(json.dumps(controls(),indent=2,sort_keys=True))

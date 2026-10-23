"""Exact finite acceptance checks for rank-two slices of Q(n,b).
Requires only the Python standard library; no archived sources are modified.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

def field_rank(matrix, p):
    if not matrix:
        return 0
    a = [[int(x) % p for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank][col:] = [(z * inv) % p for z in a[rank][col:]]
        for row in range(rank + 1, rows):
            factor = a[row][col]
            if factor:
                a[row][col:] = [
                    (x - factor * y) % p
                    for x, y in zip(a[row][col:], a[rank][col:])
                ]
        rank += 1
        if rank == rows:
            break
    return rank

def gf2_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            top = row.bit_length() - 1
            if top in pivots:
                row ^= pivots[top]
            else:
                pivots[top] = row
                break
    return len(pivots)

def source_matrix(coeff, b):
    """Literal Q(n,b) first slice; Y[p,q] is zero outside [0,n)^2."""
    n = len(coeff)
    N = n + b - 1
    return [
        [
            coeff[w - y][z - v]
            if 0 <= w - y < n and 0 <= z - v < n
            else 0
            for w in range(N) for v in range(b)
        ]
        for y in range(b) for z in range(N)
    ]

def factorized_matrix(terms, n, b):
    """Independent pair-of-Toeplitz-matrices tensor calculation."""
    N = n + b - 1
    output = [[0] * (N * b) for _ in range(b * N)]
    for f, g in terms:
        assert len(f) == len(g) == n
        A = [[f[w - y] if 0 <= w - y < n else 0
              for w in range(N)] for y in range(b)]
        B = [[g[z - v] if 0 <= z - v < n else 0
              for v in range(b)] for z in range(N)]
        for y in range(b):
            for z in range(N):
                row = output[y * N + z]
                for w in range(N):
                    if A[y][w]:
                        for v in range(b):
                            row[w * b + v] += A[y][w] * B[z][v]
    return output

def pencil_pair_block(e, d):
    """Map U_i(z) -> U_i(z)+z*U_(i+1)(z), degrees <d."""
    matrix = [[0] * ((e + 1) * d) for _ in range(e * (d + 1))]
    for i in range(e):
        for j in range(d):
            matrix[i * (d + 1) + j][i * d + j] += 1
            matrix[i * (d + 1) + j + 1][(i + 1) * d + j] += 1
    return matrix

def gf2_source_rank(mask, n, b):
    N = n + b - 1
    rows = []
    for y in range(b):
        for z in range(N):
            bits = 0
            for w in range(N):
                if 0 <= w - y < n:
                    for v in range(b):
                        if 0 <= z - v < n and ((mask >> ((w-y)*n+z-v)) & 1):
                            bits |= 1 << (w*b+v)
            rows.append(bits)
    return gf2_rank(rows)

def rank_two_census(n, b):
    """Exhaust GF2 matrices, retaining only those of matrix rank two."""
    distribution = Counter()
    for mask in range(1, 1 << (n * n)):
        yrows = [sum(((mask >> (i*n+j)) & 1) << j for j in range(n))
                 for i in range(n)]
        if gf2_rank(yrows) != 2:
            continue
        source_rank = gf2_source_rank(mask, n, b)
        assert source_rank >= b * (b + 1), (n, b, mask, source_rank)
        distribution[source_rank] += 1
    return {'n': n, 'b': b,
            'rank_two_matrices': sum(distribution.values()),
            'ranks': {str(k): distribution[k] for k in sorted(distribution)}}

def verify():
    blocks = 0
    for e in range(1, 9):
        for d in range(1, 9):
            mat = pencil_pair_block(e, d)
            exact = e*d + min(e, d)
            for p in (2, 101):
                got = field_rank(mat, p)
                assert got == exact, (e, d, p, got, exact)
                blocks += 1
    monomials = 0
    for b in range(1, 9):
        n = 2
        f0, f1 = (1, 0), (0, 1)
        terms = [(f0, f0), (f1, f1)]
        Y = [[1, 0], [0, 1]]
        source = source_matrix(Y, b)
        from_pencils = factorized_matrix(terms, n, b)
        assert source == from_pencils, b
        for p in (2, 101):
            got = field_rank(source, p)
            assert got == b*(b+1), (b, p, got)
            monomials += 1
    exhaustive = [rank_two_census(n, b)
                  for n,b in ((2,2), (2,3), (2,4),
                              (3,2), (3,3), (3,4), (4,2))]
    return {
        'status': 'exact finite controls; written proof not independently reviewed',
        'block_rank_checks': blocks,
        'block_index_range': [1, 8],
        'tested_prime_fields': [2, 101],
        'equality_controls': monomials,
        'source_factorization_matches': 8,
        'rank_two_gf2_censuses': exhaustive,
        'logical_scope': 'finite tests do not establish the all-n all-field theorem'
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    parser.add_argument('--check-certificate', type=Path)
    args = parser.parse_args()
    actual = verify()
    if args.check_certificate:
        saved = json.loads(args.check_certificate.read_text(encoding='utf-8'))
        assert actual == saved, 'the saved finite receipt does not replay'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(actual, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps(actual, sort_keys=True))

if __name__ == '__main__':
    main()

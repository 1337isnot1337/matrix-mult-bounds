"""Discovery only: literal crossed coefficient matrices over a prime field."""
import json
from math import comb


def rank_mod(rows, p=1000003):
    rows = [[v % p for v in row] for row in rows]
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, p)
        rows[rank] = [v*inv % p for v in rows[rank]]
        for i in range(rank+1, len(rows)):
            if rows[i][col]:
                c = rows[i][col]
                rows[i] = [(x-c*y) % p for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def matrix(a, b, degree):
    width = a+b-1
    return [[comb(degree, h-j) if 0 <= h-j <= degree and h-j+ell-r == degree else 0
             for h in range(width) for r in range(a)]
            for j in range(b) for ell in range(width)]


if __name__ == '__main__':
    cases = []
    for a in range(2, 7):
        for b in range(a, a+3):
            for degree in range(1, a):
                rank = rank_mod(matrix(a, b, degree))
                cases.append(dict(a=a, b=b, degree=degree, rank=rank, excess=rank-a*b))
    print(json.dumps(dict(prime=1000003, scope='finite modular discovery, not proof', cases=cases), indent=2))

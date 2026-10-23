"""Independent exact finite checks for the all-field contraction-strata proof.

No NumPy, SymPy or imported PR147 code. The theorem itself is proved in
proof.md; these are bounded acceptance controls and not a general proof.
"""
import argparse
import json
import random
from fractions import Fraction
from pathlib import Path


def tensor(k):
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a nonnegative integer")
    # A: u,v,w,h[0:k],z[0:k]
    # B: X,Z,a,eta,y,x[0],y[0],...
    # C: P,Q,R,S,T,p[0],q[0],...
    terms = [
        (0, 0, 0, 1), (0, 1, 1, 1),
        (1, 2, 2, 1), (1, 3, 3, 1),
        (2, 0, 1, 1), (2, 1, 4, 1),
        (2, 3, 2, 1), (2, 4, 3, 1), (2, 0, 2, 1),
    ]
    for j in range(k):
        terms += [
            (3 + j, 0, 5 + 2*j, 1),
            (3 + j, 1, 6 + 2*j, 1),
            (3 + k + j, 5 + 2*j, 2, 1),
            (3 + k + j, 6 + 2*j, 3, 1),
        ]
    return (3 + 2*k, 5 + 2*k, 5 + 2*k), terms


def modular_rank(rows, prime):
    """Exact Gaussian elimination modulo a prime, including p=2."""
    if not rows:
        return 0
    a = [[v % prime for v in row] for row in rows]
    m, n = len(a), len(a[0])
    r = 0
    for j in range(n):
        h = next((i for i in range(r, m) if a[i][j]), None)
        if h is None:
            continue
        a[h], a[r] = a[r], a[h]
        inverse = pow(a[r][j], -1, prime)
        a[r][j:] = [(t * inverse) % prime for t in a[r][j:]]
        for i in range(r + 1, m):
            factor = a[i][j]
            if factor:
                a[i][j:] = [(v-factor*w) % prime
                            for v,w in zip(a[i][j:], a[r][j:])]
        r += 1
        if r == m:
            break
    return r



def rational_rank(rows):
    """Exact elimination over Q, independent of the modular routine."""
    if not rows:
        return 0
    a = [[Fraction(z) for z in row] for row in rows]
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank,m) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank],a[pivot] = a[pivot],a[rank]
        leading = a[rank][col]
        a[rank][col:] = [z / leading for z in a[rank][col:]]
        for j in range(rank+1,m):
            factor = a[j][col]
            if factor:
                a[j][col:] = [x-factor*y for x,y in
                                  zip(a[j][col:],a[rank][col:])]
        rank += 1
        if rank == m:
            break
    return rank

def literal_slice(k, leg, coefficients, prime=None):
    dims, terms = tensor(k)
    if leg not in (0,1,2) or len(coefficients) != dims[leg]:
        raise ValueError("Invalid leg or coefficient length")
    others = [i for i in range(3) if i != leg]
    mat = [[0] * dims[others[1]] for _ in range(dims[others[0]])]
    for i,j,h,weight in terms:
        item = (i,j,h)
        row, col = (item[z] for z in others)
        mat[row][col] += weight * coefficients[item[leg]]
    return rational_rank(mat) if prime is None else modular_rank(mat,prime)


def pair_rank(rows, prime=None):
    if not rows:
        return 0
    a = [(x % prime, y % prime) if prime is not None else (x,y)
         for x,y in rows]
    if all(not x and not y for x,y in a):
        return 0
    for x,y in a:
        if not x and not y:
            continue
        if any(((x * v - y * u) % prime if prime is not None
                else x*v-y*u) for u,v in a):
            return 2
        return 1
    raise AssertionError("Unreachable")


def expected_rank(k, leg, coeff, prime=None):
    z = [x % prime if prime is not None else x for x in coeff]
    if leg == 0:
        if not any(z):
            return 0
        top = bool(z[0] or any(z[3:3+k]))
        bottom = bool(z[1] or any(z[3+k:]))
        if not z[2] and top != bottom:
            return 2
        return 4
    if leg == 1:
        pairs = [(z[2], z[3])] + [
            (z[5+2*j], z[6+2*j]) for j in range(k)]
        if z[0] or z[1]:
            return k+2+pair_rank(pairs, prime)
        return pair_rank(pairs[:1] + [(z[3], z[4])] + pairs[1:], prime)
    if leg == 2:
        pairs = [(z[0], z[1])] + [
            (z[5+2*j], z[6+2*j]) for j in range(k)]
        if z[2] or z[3]:
            return k+2+pair_rank(pairs, prime)
        return pair_rank(pairs[:1] + [(z[1], z[4])] + pairs[1:], prime)
    raise ValueError("Invalid leg")


def verify(exhaustive_k=3, seed=20261023):
    rng = random.Random(seed)
    checks = 0
    census = []
    for k in range(exhaustive_k + 1):
        dims, terms = tensor(k)
        if len(terms) != 9+4*k or dims != (3+2*k,5+2*k,5+2*k):
            raise AssertionError("Source format changed")
        sizes = []
        for leg, dimension in enumerate(dims):
            hist = {}
            for mask in range(1 << dimension):
                coeff = [(mask >> i) & 1 for i in range(dimension)]
                literal = literal_slice(k,leg,coeff,2)
                expected = expected_rank(k,leg,coeff,2)
                if literal != expected:
                    raise AssertionError(
                        (k,leg,mask,literal,expected))
                hist[literal] = hist.get(literal,0)+1
                checks += 1
            sizes.append(hist)
        census.append({"k":k,"dims":dims,
                       "GF2_census":[dict(sorted(x.items())) for x in sizes]})
    odd_checks = 0
    for prime in (3,5,101):
        for k in (0,1,2,3,5):
            dims, _ = tensor(k)
            for leg, dimension in enumerate(dims):
                for trial in range(48):
                    coeff = [rng.randrange(-100,101) for _ in range(dimension)]
                    if trial < dimension:
                        coeff = [int(i == trial) for i in range(dimension)]
                    literal = literal_slice(k,leg,coeff,prime)
                    expected = expected_rank(k,leg,coeff,prime)
                    if literal != expected:
                        raise AssertionError(
                            (k,leg,prime,trial,literal,expected))
                    odd_checks += 1
    rational_checks = 0
    for k in (0,1,2,3,5):
        dims, _ = tensor(k)
        for leg, dimension in enumerate(dims):
            for trial in range(32):
                coeff = [rng.randrange(-7,8) for _ in range(dimension)]
                literal = literal_slice(k,leg,coeff)
                expected = expected_rank(k,leg,coeff)
                if literal != expected:
                    raise AssertionError((k,leg,"Q",trial,literal,expected))
                rational_checks += 1
    return {
        "rational_checks": rational_checks,
        "theorem": "exact all-field A,B,C contraction-rank formulas",
        "status": "finite acceptance for written proof, not independent review",
        "exhaustive_GF2_checks": checks,
        "odd_prime_checks": odd_checks,
        "GF2_census": census,
        "tested_primes": [2,3,5,101],
        "improves_omega": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    ns = parser.parse_args()
    receipt = verify()
    if ns.output:
        ns.output.parent.mkdir(parents=True, exist_ok=True)
        ns.output.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "binary_checks":receipt["exhaustive_GF2_checks"],
        "odd_prime_checks":receipt["odd_prime_checks"],
        "rational_checks":receipt["rational_checks"],
        "dimensions":[entry["dims"] for entry in receipt["GF2_census"]],
    }))


if __name__ == "__main__":
    main()

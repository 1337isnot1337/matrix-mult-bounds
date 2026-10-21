"""The order-125 Heisenberg group and its exact conditional target gate."""
from itertools import product
from math import isqrt
from pathlib import Path
import sys

RESEARCH = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RESEARCH/'2026-10-20-sl2-seven/imported'))


def require_odd_prime(p):
    if p < 3 or p % 2 == 0 or any(p % d == 0 for d in range(3, isqrt(p)+1, 2)):
        raise ValueError('an odd prime is required')


def group(p=5):
    require_odd_prime(p)
    elements = list(product(range(p), repeat=3))
    index = {g: i for i, g in enumerate(elements)}
    table = [[index[(a+x) % p, (b+y) % p, (c+z+a*y) % p]
              for x, y, z in elements] for a, b, c in elements]
    return {'name': f'Heisenberg({p})', 'identity': 0, 'p': p,
            'matrices': elements, 'mul': table,
            'inv': [index[-a % p, -b % p, (-c+a*b) % p] for a, b, c in elements]}


def two_coset_sets(G):
    p, M, inv = G['p'], G['mul'], G['inv']
    subgroups = set()
    for g, (a, b, c) in enumerate(G['matrices']):
        if a == b == 0:
            continue
        powers = [0]
        for _ in range(p-1):
            powers.append(M[powers[-1]][g])
        if len(set(powers)) != p or M[powers[-1]][g] != 0:
            raise ArithmeticError('expected a noncentral order-p subgroup')
        subgroups.add(tuple(sorted(powers)))
    candidates = set()
    for L in sorted(subgroups):
        for coset in sorted({tuple(sorted(M[g][l] for l in L)) for g in range(p**3)}):
            g = min(coset)
            if set(coset) == set(L) or {M[M[g][l]][inv[g]] for l in L} == set(L):
                continue
            candidates.add(tuple(sorted(set(L) | set(coset))))
    return sorted(candidates), len(subgroups)


def quotients(G, S):
    return {G['mul'][g][G['inv'][h]] for g in S for h in S if g != h}


def source_gate(p=5, shape=(10, 10, 10)):
    require_odd_prime(p)
    sys.path.insert(0, str(RESEARCH/'2026-10-20-sl2-seven'))
    sys.path.insert(0, str(RESEARCH/'2026-10-20-group-potentials'))
    from source_certificate import exponent_gate
    from rank_locus_obstruction import screen
    degrees = [1]*(p*p)+[p]*(p-1)
    return {'group': f'Heisenberg({p})', 'order': p**3, 'complex_degrees': degrees,
            'shape': list(shape), 'conditional_gate': exponent_gate(degrees, shape=shape),
            'rank_locus_screen': screen(degrees, list(shape)),
            'degree_derivation': 'Explicit p^2 linear characters and p-1 irreducible '
                'p-dimensional shift/phase representations; proof in source_proof.md.',
            'degeneration_constructed': False, 'exponent_improvement': False}

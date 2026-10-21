"""Independent finite controls for the all-prime averaging argument and seven projections."""
from itertools import permutations, product
import json
from pathlib import Path
import sys

from source import group, RESEARCH
from projection_orbits import derive
sys.path.insert(0, str(RESEARCH/'2026-10-20-group-potentials'))
from stream_potentials import support


def subgroup_controls(p):
    G = group(p)
    M, inv = G['mul'], G['inv']
    unique = {}
    for g, (a, b, c) in enumerate(G['matrices']):
        if a == b == 0:
            continue
        powers = [0]
        for _ in range(p-1):
            powers.append(M[powers[-1]][g])
        unique.setdefault(tuple(sorted(powers)), g)
    rows = []
    half = pow(2, -1, p)
    for points, g in sorted(unique.items()):
        a, b, c = G['matrices'][g]
        rows.append((points, a, b, (c-half*a*b) % p))
    checked = tpp = conjugations = 0
    for L, a, b, h in rows:
        for g, (x, y, c) in enumerate(G['matrices']):
            aa, bb, cc = G['matrices'][M[M[g][unique[L]]][inv[g]]]
            if aa != a or bb != b or (cc-half*aa*bb-h-x*b+y*a) % p:
                raise ValueError('conjugation does not have the predicted central slope')
            conjugations += 1
    for L, a, b, h in rows:
        for K, x, y, k in rows:
            determinant = (a*y-b*x) % p
            if not determinant:
                continue
            determinant_inverse = pow(determinant, -1, p)
            for J, u, v, j in rows:
                if not (a*v-b*u) % p or not (x*v-y*u) % p:
                    continue
                alpha = (-u*y+x*v)*determinant_inverse % p
                beta = (-a*v+u*b)*determinant_inverse % p
                A = half*alpha*beta*determinant % p
                if not alpha or not beta or not A:
                    raise ValueError('quadratic coefficient unexpectedly vanished')
                predicted = (alpha*h+beta*k+j) % p == 0
                actual = not any(M[s][t] in J for s in L for t in K if s or t)
                if predicted != actual:
                    raise ValueError('subgroup TPP disagrees with the quadratic criterion')
                checked += 1
                tpp += actual
    return {'prime': p, 'noncentral_cyclic_subgroups': len(rows),
            'pairwise_distinct_direction_triples_checked': checked,
            'ordinary_TPP_triples': tpp, 'central_conjugations_checked': conjugations}


def projection_control():
    # A binary matrix with margins two is an even-cycle bipartite graph;
    # alternating the cycles decomposes it into two disjoint permutations.
    configurations = set()
    for first in permutations(range(5)):
        for second in permutations(range(5)):
            if any(a == b for a, b in zip(first, second)):
                continue
            configurations.add(tuple(sorted(5*r+c for r in range(5)
                                             for c in (first[r], second[r]))))
    report = derive()
    union = set()
    for row in report['affine_coordinate_orbits']:
        S = row['representative']
        orbit = set()
        for a, c in product(range(1, 5), repeat=2):
            for b, d in product(range(5), repeat=2):
                transformed = tuple(sorted(5*((a*(q//5)+b) % 5)+(c*(q % 5)+d) % 5 for q in S))
                orbit.add(transformed)
                orbit.add(tuple(sorted(5*(q % 5)+q//5 for q in transformed)))
        if len(orbit) != row['size'] or union & orbit:
            raise ValueError('wrong or overlapping affine coordinate orbit')
        union |= orbit
    if union != configurations or len(configurations) != report['row_and_column_sum_two_sets']:
        raise ValueError('seven representatives do not cover the independent enumeration')
    return {'independently_enumerated_projections': len(configurations),
            'affine_coordinate_classes': len(report['affine_coordinate_orbits'])}


def averaging_control(path):
    G = group()
    sets = json.loads(path.with_suffix('.cuts.jsonl').read_text().splitlines()[0])['sets']
    terms = set(support(G, sets))
    stabilizers = [[g for g in range(125) if {G['mul'][s][g] for s in row} == set(row)]
                   for row in sets]
    checks = 0
    positions = [(0, 5), (1, 2), (3, 4)]
    for f, H in enumerate(stabilizers):
        indices = {g: i for i, g in enumerate(sets[f])}
        for h in H:
            permutation = [indices[G['mul'][g][h]] for g in sets[f]]
            for vertices in terms:
                transformed = list(vertices)
                for position in positions[f]:
                    transformed[position] = permutation[transformed[position]]
                if tuple(transformed) not in terms:
                    raise ValueError('right stabilizer did not preserve exact group support')
                checks += 1
    return {'right_stabilizer_orders': list(map(len, stabilizers)),
            'group_support_terms': len(terms), 'transformed_support_terms_checked': checks}


def all_controls():
    root = Path(__file__).resolve().parents[3]
    return {'subgroups': [subgroup_controls(p) for p in (3, 5, 7)],
            'projected_supports': projection_control(),
            'averaging': averaging_control(root/'results/heisenberg-five-2026-10-20/two-coset.json'),
            'proof_status': 'Finite controls for written all-prime proof; no independent review.',
            'exponent_improvement': False}


if __name__ == '__main__':
    print(json.dumps(all_controls(), indent=2))

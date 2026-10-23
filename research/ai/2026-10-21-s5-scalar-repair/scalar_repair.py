"""Exact scalar-monomial repair witnesses for coordinate group contractions."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'2026-10-21-s5-split'))
from s5_source import ROOT
from group_exact import pair_map, verify_farkas


def terms(G, sets):
    X, Y, Z = [pair_map(G, sets[f], sets[(f+1) % 3]) for f in range(3)]
    for x, (s, t) in X.items():
        for y, (tt, u) in Y.items():
            z = G['inv'][G['mul'][x][y]]
            if z in Z:
                uu, ss = Z[z]
                yield (s, t, tt, u, uu, ss)


def weight(shape, potentials, vertices):
    n, m, p = shape
    s, t, tt, u, uu, ss = vertices
    return (potentials[s]-potentials[ss]+potentials[n+tt]-potentials[n+t]
            +potentials[n+m+uu]-potentials[n+m+u])


def intended(vertices):
    s, t, tt, u, uu, ss = vertices
    return (s, t, u) == (ss, tt, uu)


def verify_repair(G, sets, potentials, corrections):
    if (len(sets) != 3 or any(not S or len(set(S)) != len(S)
            or any(type(g) is not int or not 0 <= g < len(G['mul']) for g in S) for S in sets)):
        raise ValueError('three nonempty coordinate vertex sets required')
    shape = list(map(len, sets))
    if len(potentials) != sum(shape) or any(type(w) is not int for w in potentials):
        raise ValueError('one integer potential per vertex required')
    removed = {tuple(v) for v in corrections}
    if len(removed) != len(corrections) or any(len(v) != 6 or any(type(i) is not int for i in v)
                                            for v in removed):
        raise ValueError('distinct monomial corrections required')
    found, intended_count, extras, positive, negative = set(), 0, 0, [], 0
    for v in terms(G, sets):
        w = weight(shape, potentials, v)
        if intended(v):
            if w or v in removed:
                raise ValueError('intended coefficient was changed')
            intended_count += 1
            continue
        extras += 1
        if v in removed:
            found.add(v)
            negative += w < 0
        elif w <= 0:
            raise ValueError('uncorrected nonpositive extra term')
        else:
            positive.append(w)
    if found != removed or intended_count != shape[0]*shape[1]*shape[2]:
        raise ValueError('correction outside the actual extra support')
    return {'shape': shape, 'intended_terms': intended_count, 'extra_monomials': extras,
            'scalar_corrections': len(removed), 'corrected_negative_terms': negative,
            'surviving_extra_terms': len(positive),
            'minimum_surviving_weight': min(positive) if positive else None,
            'verified': True, 'exponent_improvement': False}


def verify_disjoint_circuits(G, sets, circuits):
    # Pair injectivity also ensures each extra potential row identifies a
    # unique monomial: an extra must differ on both indices in every family.
    for f in range(3):
        pair_map(G, sets[f], sets[(f+1) % 3])
    shape = list(map(len, sets))
    seen = set()
    for circuit in circuits:
        rows = []
        for raw in circuit['vertices']:
            v = tuple(raw)
            if len(v) != 6 or intended(v) or v in seen:
                raise ValueError('circuit monomials must be extra and disjoint')
            s, t, tt, u, uu, ss = v
            if any(type(i) is not int or not 0 <= i < shape[f] for f, i in
                   [(0,s),(1,t),(1,tt),(2,u),(2,uu),(0,ss)]):
                raise ValueError('invalid circuit vertex')
            x = G['mul'][G['inv'][sets[0][s]]][sets[1][t]]
            y = G['mul'][G['inv'][sets[1][tt]]][sets[2][u]]
            z = G['mul'][G['inv'][sets[2][uu]]][sets[0][ss]]
            if G['mul'][G['mul'][x][y]][z] != 0:
                raise ValueError('circuit monomial is outside the group support')
            row = [0]*sum(shape)
            for f, i, a in [(0,s,1),(0,ss,-1),(1,tt,1),(1,t,-1),(2,uu,1),(2,u,-1)]:
                row[sum(shape[:f])+i] += a
            rows.append({'row': row})
            seen.add(v)
        if not verify_farkas(rows, list(range(len(rows))), circuit['weights']):
            raise ValueError('not an exact positive dependence')
    return {'disjoint_circuits': len(circuits), 'distinct_monomials': len(seen),
            'monomial_correction_lower_bound': len(circuits),
            'scope': 'Individual scalar-monomial cancellation only; arbitrary rank-one corrections remain open.'}


def verify_coordinate_packing(G, sets, circuits, leg):
    if leg not in (0, 1, 2):
        raise ValueError('a target tensor leg is required')
    receipt = verify_disjoint_circuits(G, sets, circuits)
    seen = set()
    for circuit in circuits:
        coordinates = {tuple(v[2*leg:2*leg+2]) for v in circuit['vertices']}
        if seen & coordinates or sorted(coordinates) != [tuple(v) for v in circuit['output_coordinates']]:
            raise ValueError('circuit coordinate sets must be exact and disjoint')
        seen.update(coordinates)
    return {'coordinate_leg': leg, 'disjoint_circuits': len(circuits),
            'distinct_monomials': receipt['distinct_monomials'], 'distinct_coordinates': len(seen),
            'auxiliary_rank_lower_bound': len(circuits),
            'scope': 'Arbitrary Laurent correction tensors to these fixed coordinate group maps with integer vertex weights; general group input mixing remains open.'}


def control():
    points = [(a, b) for b in range(3) for a in range(3)]
    G = {'name': 'C3 x C3', 'mul': [[(a+c) % 3+3*((b+d) % 3) for c, d in points]
                                  for a, b in points],
         'inv': [(-a) % 3+3*((-b) % 3) for a, b in points]}
    sets, potentials = [[0, 1], [0, 3], [0, 4]], [0, 1, 0, 0, 0, 0]
    corrections = [list(v) for v in terms(G, sets) if not intended(v)
                   and weight([2,2,2], potentials, v) <= 0]
    receipt = verify_repair(G, sets, potentials, corrections)
    if (receipt['intended_terms'], receipt['extra_monomials'], receipt['scalar_corrections'],
            receipt['corrected_negative_terms'], receipt['minimum_surviving_weight']) != (8,2,1,1,1):
        raise ArithmeticError('incorrect Laurent correction control')
    return G, {'group': G['name'], 'sets': sets, 'potentials': potentials,
               'corrections': corrections, 'verification': receipt}

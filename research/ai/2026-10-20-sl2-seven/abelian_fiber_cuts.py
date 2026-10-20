"""Necessary abelian fiber clauses for the SL(2,7) projection search."""
from itertools import combinations, product


def cyclic_subgroups(G, Q):
    n = len(Q['representatives'])
    subgroups = set()
    for generator in range(1, n):
        powers, x = [], 0
        while x not in powers:
            powers.append(x)
            x = Q['mul'][x][generator]
        if x != 0:
            raise ArithmeticError('quotient is not a group')
        if len(powers) in (3, 4, 7):
            subgroups.add(tuple(sorted(powers)))
    records = []
    for H in sorted(subgroups, key=lambda h: (len(h), h)):
        m = len(H)
        preimage = [g for g in range(len(G['mul'])) if Q['projection'][g] in H]
        if len(preimage) != 2*m or any(G['mul'][g][h] != G['mul'][h][g]
                                     for g in preimage for h in preimage):
            raise ArithmeticError('preimage is not abelian of the stated order')
        cyclic = False
        for generator in preimage:
            x, powers = 0, set()
            while x not in powers:
                powers.add(x)
                x = G['mul'][x][generator]
            cyclic |= len(powers) == 2*m
        if not cyclic:
            raise ArithmeticError('cyclic preimage required')
        cosets = sorted({tuple(sorted(Q['mul'][h][g] for h in H)) for g in range(n)})
        if len(cosets)*m != n or len(set().union(*map(set, cosets))) != n:
            raise ArithmeticError('incorrect coset partition')
        classes = sorted({min(h, Q['inv'][h]) for h in H if h})
        records.append({'subgroup': H, 'cosets': cosets, 'classes': classes,
                        'preimage_order': 2*m})
    return records


def append_cuts(records, pool, members, owners, clauses):
    before = len(clauses)
    counts = {3: 0, 4: 0, 7: 0}
    for record in records:
        m = len(record['subgroup'])
        counts[m] += 1
        if m == 4:
            # Three center-free two-point fibers cannot tile C8.
            for choices in product(record['classes'], repeat=3):
                clauses.append([-owners[f][choices[f]] for f in range(3)])
            continue
        thresholds = (3,) if m == 3 else (2, 3, 4, 5)
        flags = [{k: pool.id(('maximum-fiber', tuple(record['subgroup']), f, k))
                  for k in thresholds} for f in range(3)]
        for f in range(3):
            for k in thresholds:
                if k == 2:
                    for c in record['classes']:
                        clauses.append([-owners[f][c], flags[f][k]])
                else:
                    for coset in record['cosets']:
                        for points in combinations(coset, k):
                            clauses.append([-members[f][p] for p in points]+[flags[f][k]])
                if k-1 in flags[f]:
                    clauses.append([-flags[f][k], flags[f][k-1]])
        for f, h in combinations(range(3), 2):
            for k, ell in product(thresholds, repeat=2):
                if k*ell > 2*m:
                    clauses.append([-flags[f][k], -flags[h][ell]])
        for ks in product(thresholds, repeat=3):
            if ks[0]*ks[1]*ks[2] > 2*m:
                clauses.append([-flags[f][ks[f]] for f in range(3)])
    return {'cyclic_subgroup_counts': counts, 'additional_clauses': len(clauses)-before}

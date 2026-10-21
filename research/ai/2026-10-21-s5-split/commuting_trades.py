"""Existing necessary commuting trades, generated in the actual central cover."""
from itertools import combinations, permutations


def templates(G):
    M, inv = G['mul'], G['inv']
    output = set()
    # The sampler uses sections of the central quotient. Its internal
    # differences therefore never belong to the central fiber over identity.
    for x in range(4, 480):
        for y in range(4, 480):
            z = M[x][y]
            if z < 4 or z != M[y][x]:
                continue
            a, b, c = (min(q, inv[q]) for q in (x, y, z))
            for f, h, k in permutations(range(3)):
                row = [0]*3
                row[f], row[h], row[k] = c, a, b
                output.add(tuple(row))
    return sorted(output)


def owner_sets(G, sets):
    return [{min(G['mul'][g][G['inv'][h]], G['inv'][G['mul'][g][G['inv'][h]]])
             for g, h in combinations(S, 2)} for S in sets]


def violations(G, sets, rows=None):
    owners = owner_sets(G, sets)
    return sum(all(row[f] in owners[f] for f in range(3))
               for row in (templates(G) if rows is None else rows))

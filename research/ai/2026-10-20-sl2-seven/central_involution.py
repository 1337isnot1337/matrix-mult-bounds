"""Exact central-involution pruning for coordinate-potential constructions."""


def forced_center_pair_exclusions(G, shape):
    table, inverses = G['mul'], G['inv']
    n = len(table)
    involutions = [z for z in range(1, n) if inverses[z] == z
                   and all(table[z][g] == table[g][z] for g in range(n))]
    exclusions = []
    for z in involutions:
        pairs = [(g, table[z][g]) for g in range(n) if g < table[z][g]]
        for f in range(3):
            product = shape[(f+1) % 3]*shape[(f+2) % 3]
            if 2*product > n:
                exclusions.append({'set': f, 'central_involution': z,
                                   'quotient_order': n//2,
                                   'other_pair_count': product, 'pairs': pairs})
    return exclusions


def opposite_trade(G, s0, s1, t0, t1, u0, u1):
    """Check both six-vertex group equations and their cancelling rows."""
    table, inv = G['mul'], G['inv']
    vertices = [(s0, t0, t1, u1, u0, s1),
                (s1, t1, t0, u0, u1, s0)]
    rows = []
    for s, t, tt, u, uu, ss in vertices:
        labels = [table[inv[s]][t], table[inv[tt]][u], table[inv[uu]][ss]]
        if table[table[labels[0]][labels[1]]][labels[2]] != 0:
            raise ValueError('not a supported extra group term')
        if (s, t, u) == (ss, tt, uu):
            raise ValueError('term is intended')
        row = {}
        for vertex, sign in [((0, s), 1), ((0, ss), -1),
                             ((1, tt), 1), ((1, t), -1),
                             ((2, uu), 1), ((2, u), -1)]:
            row[vertex] = row.get(vertex, 0)+sign
        rows.append(row)
    keys = set(rows[0]) | set(rows[1])
    if any(rows[0].get(k, 0)+rows[1].get(k, 0) for k in keys):
        raise ArithmeticError('potential rows do not cancel')
    return vertices

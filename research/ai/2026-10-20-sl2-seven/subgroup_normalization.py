"""Finite order-48 subgroup and its conjugation/inversion coverage."""


def octahedral_certificate(G):
    matrices = G['matrices']
    index = {x: i for i, x in enumerate(matrices)}
    generators = [index[x] for x in [(0, 1, 6, 0), (2, 3, 3, 5),
                                    (3, 1, 0, 5), (3, 6, 3, 4)]]
    table, inv = G['mul'], G['inv']
    H, pending = {0}, [0]
    while pending:
        x = pending.pop()
        for y in generators:
            z = table[x][y]
            if z not in H:
                H.add(z)
                pending.append(z)
    if len(H) != 48 or any(table[x][y] not in H for x in H for y in H):
        raise ArithmeticError('incorrect order-48 subgroup')
    members = sorted(H)
    remaining, anchors, witnesses = H-{0}, [], []
    while remaining:
        q = min(remaining)
        orbit = {table[table[g][x]][inv[g]]
                 for g in members for x in (q, inv[q])}
        anchor = min(orbit)
        anchors.append(anchor)
        for x in sorted(orbit):
            for reverse in (False, True):
                actual = inv[x] if reverse else x
                conjugator = next((g for g in members
                                   if table[table[g][actual]][inv[g]] == anchor), None)
                if conjugator is not None:
                    witnesses.append({'quotient': x, 'reverse_pair': reverse,
                                      'conjugator': conjugator, 'anchor': anchor})
                    break
            else:
                raise ArithmeticError('missing subgroup quotient normalization')
        remaining.difference_update(orbit)
    if len(witnesses) != 47:
        raise ArithmeticError('incorrect subgroup orbit coverage')
    return {'name': 'order-48 subgroup', 'order': 48, 'index': 7,
            'generators': generators, 'members': members, 'anchors': anchors,
            'witnesses': witnesses}


def verify_certificate(G, certificate):
    table, inv = G['mul'], G['inv']
    H = set(certificate['members'])
    if (len(H) != 48 or 0 not in H or
            any(inv[x] not in H for x in H) or
            any(table[x][y] not in H for x in H for y in H)):
        return False
    witnesses = certificate['witnesses']
    if sorted(w['quotient'] for w in witnesses) != sorted(H-{0}):
        return False
    for w in witnesses:
        q, g = w['quotient'], w['conjugator']
        if g not in H or w['anchor'] not in certificate['anchors']:
            return False
        q = inv[q] if w['reverse_pair'] else q
        if table[table[g][q]][inv[g]] != w['anchor']:
            return False
    return True

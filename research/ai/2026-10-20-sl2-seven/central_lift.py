"""Exact quotient and parity conditions for lifting three projected sets.

No SAT, linear-programming or numerical dependency. A consistent parity
system certifies pair-map injectivity only, not a tensor degeneration.
"""
from itertools import combinations


def quotient(G, z):
    table, inv = G['mul'], G['inv']
    n = len(table)
    if z == 0 or inv[z] != z or any(table[z][g] != table[g][z] for g in range(n)):
        raise ValueError('central involution required')
    reps = sorted({min(g, table[z][g]) for g in range(n)})
    index = {g: i for i, g in enumerate(reps)}
    projection = [index[min(g, table[z][g])] for g in range(n)]
    bits = [int(g != reps[projection[g]]) for g in range(n)]
    inverses = [projection[inv[g]] for g in reps]
    qtable = [[projection[table[g][h]] for h in reps] for g in reps]
    classes = sorted({min(g, inverses[g]) for g in range(1, len(reps))})
    fibers = {c: set() for c in classes}
    for g in range(n):
        if projection[g]:
            c = min(projection[g], inverses[projection[g]])
            fibers[c].add(min(g, inv[g]))
    fibers = {c: sorted(v) for c, v in fibers.items()}
    if any(len(v) not in (1, 2) for v in fibers.values()):
        raise ArithmeticError('unexpected inverse-class fiber')
    pairs = {}
    for u, v in combinations(range(len(reps)), 2):
        g = table[reps[u]][inv[reps[v]]]
        c = min(projection[g], inverses[projection[g]])
        pairs[u, v] = (c, fibers[c].index(min(g, inv[g])))
    return {'z': z, 'representatives': reps, 'projection': projection,
            'bits': bits, 'mul': qtable, 'inv': inverses,
            'classes': classes, 'fibers': fibers, 'pairs': pairs}


def lift_system(Q, sets):
    """Conditional parity rows, with point supports for valid conflict cuts."""
    if any(len(set(s)) != len(s) or 0 not in s for s in sets):
        raise ValueError('distinct projected points including identity required')
    variables, variable_index, rows = [], {}, []

    def variable(label):
        if label not in variable_index:
            variable_index[label] = len(variables)
            variables.append(label)
        return variable_index[label]

    def add(labels, rhs, support):
        mask = 0
        for label in labels:
            mask ^= 1 << variable(label)
        rows.append({'mask': mask, 'rhs': rhs, 'support': sorted(set(support))})

    for f, points in enumerate(sets):
        for p in points:
            variable(('sign', f, p))
        add([('sign', f, 0)], 0, [(f, 0)])
    pairs = [{c: [] for c in Q['classes']} for _ in sets]
    for f, points in enumerate(sets):
        for u, v in combinations(sorted(points), 2):
            c, offset = Q['pairs'][u, v]
            pairs[f][c].append((u, v, offset))
    for c in Q['classes']:
        users = [f for f in range(3) if pairs[f][c]]
        capacity = len(Q['fibers'][c])
        if len(users) > capacity:
            raise ValueError('projected inverse-class capacity exceeded')
        if len(users) != 2:
            continue
        first, second = users
        witnesses = {f: [(f, x) for x in pairs[f][c][0][:2]] for f in users}
        add([('owner', first, c), ('owner', second, c)], 1,
            witnesses[first]+witnesses[second])
        for f, other in [(first, second), (second, first)]:
            for u, v, offset in pairs[f][c]:
                add([('sign', f, u), ('sign', f, v), ('owner', f, c)], offset,
                    [(f, u), (f, v)]+witnesses[other])
    return {'variables': variables, 'rows': rows}


def verify_circuit(rows, indices):
    if not indices or len(set(indices)) != len(indices):
        return False
    mask, rhs = 0, 0
    for i in indices:
        if not isinstance(i, int) or not 0 <= i < len(rows):
            return False
        mask ^= rows[i]['mask']
        rhs ^= rows[i]['rhs']
    return mask == 0 and rhs == 1


def eliminate(system):
    basis = {}
    for i, row in enumerate(system['rows']):
        mask, rhs, provenance = row['mask'], row['rhs'], 1 << i
        while mask:
            pivot = mask.bit_length()-1
            if pivot not in basis:
                basis[pivot] = (mask, rhs, provenance)
                break
            old_mask, old_rhs, old_provenance = basis[pivot]
            mask ^= old_mask
            rhs ^= old_rhs
            provenance ^= old_provenance
        if not mask and rhs:
            circuit = [j for j in range(len(system['rows'])) if provenance >> j & 1]
            if not verify_circuit(system['rows'], circuit):
                raise ArithmeticError('invalid parity circuit')
            return {'consistent': False, 'circuit': circuit}
    assignment = 0
    for pivot in sorted(basis):
        mask, rhs, _ = basis[pivot]
        bit = rhs ^ ((mask & assignment).bit_count() % 2)
        assignment |= bit << pivot
    if any(((row['mask'] & assignment).bit_count() % 2) != row['rhs']
           for row in system['rows']):
        raise ArithmeticError('invalid particular parity solution')
    return {'consistent': True, 'assignment': assignment,
            'rank': len(basis), 'nullity': len(system['variables'])-len(basis)}


def lifted_sets(G, Q, system, assignment, sets):
    lookup = {v: i for i, v in enumerate(system['variables'])}
    return [[G['mul'][Q['z']][Q['representatives'][p]]
             if assignment >> lookup['sign', f, p] & 1
             else Q['representatives'][p] for p in points]
            for f, points in enumerate(sets)]

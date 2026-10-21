"""Verified finite conjugation and equal-leg canonicalization for S5 x C2."""
from s5_source import data, control
from group_exact import verify_witness


def lex_geq(left, right, variable, add_clause, label):
    """Require the first Boolean vector to be lexicographically >= the second."""
    if len(left) != len(right):
        raise ValueError('equal comparison lengths required')
    previous = None
    for i, (a, b) in enumerate(zip(left, right)):
        guard = [] if previous is None else [-previous]
        add_clause(guard+[a, -b])
        if i+1 == len(left):
            break
        equal = variable(('lex-prefix', label, i))
        add_clause(guard+[-a, -b, equal])
        add_clause(guard+[a, b, equal])
        add_clause([-equal, -a, b])
        add_clause([-equal, a, -b])
        if previous is not None:
            add_clause([-equal, previous])
        previous = equal


def actions(G, Q, receipt):
    H = receipt['subgroup_members']
    return sorted({tuple(Q['projection'][G['mul'][G['mul'][g][2*q]][G['inv'][g]]]
                         for q in range(120)) for g in H})


def append(G, Q, receipt, members, variable, add_clause):
    order = receipt['projected_subgroup']+sorted(set(range(120))-set(receipt['projected_subgroup']))
    permutations = actions(G, Q, receipt)
    for j, permutation in enumerate(permutations):
        if permutation == tuple(range(120)):
            continue
        inverse = [0]*120
        for q, image in enumerate(permutation):
            inverse[image] = q
        lex_geq([members[0][q] for q in order], [members[0][inverse[q]] for q in order],
                variable, add_clause, ('common-conjugation', j))
    lex_geq([members[1][q] for q in order], [members[2][q] for q in order],
            variable, add_clause, 'equal-last-legs')
    return {'common_subgroup_conjugations': len(permutations),
            'first_leg_order': 'normalization-subgroup points first, presence preferred',
            'equal_last_legs_ordered': True}


def canonical_control():
    G, Q, receipt = data()
    known = control()['witness']
    order = receipt['projected_subgroup']+sorted(set(range(120))-set(receipt['projected_subgroup']))
    best = None
    for g in receipt['subgroup_members']:
        sets = [[G['mul'][G['mul'][g][x]][G['inv'][g]] for x in row] for row in known['sets']]
        potentials = [known['potentials'][3*f:3*f+3] for f in range(3)]
        for swapped in (False, True):
            candidate = [sets[0], sets[2], sets[1]] if swapped else sets
            weights = [-v for f in (0, 2, 1) for v in potentials[f]] if swapped else known['potentials']
            key = tuple(int(q in {Q['projection'][x] for x in row}) for row in candidate for q in order)
            if best is None or key > best[0]:
                best = key, candidate, weights
    _, sets, potentials = best
    return {'group': G['name'], 'witness': {'sets': sets, 'potentials': potentials,
              'verification': verify_witness(G, sets, potentials)},
            'normalization': 'Joint maximum under common H conjugations and equal-leg swap',
            'exponent_improvement': False}

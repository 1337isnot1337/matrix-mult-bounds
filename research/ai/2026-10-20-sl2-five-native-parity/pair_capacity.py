"""Exact projected-pair capacity witnesses for a central cover of degree two."""
from itertools import combinations


def triple_patterns(Q):
    """Partition all projected triples by independent right translation."""
    patterns = {}
    for points in combinations(range(len(Q['representatives'])), 3):
        canonical = min(tuple(sorted(Q['mul'][p][Q['inv'][anchor]] for p in points))
                        for anchor in points)
        patterns.setdefault(canonical, []).append(points)
    return patterns


def append_patterns(Q, solver, members, top):
    """Compile all degree-two pair capacities with shared pattern flags."""
    patterns = triple_patterns(Q)
    clauses = 0
    for pattern, triples in patterns.items():
        flags = []
        for f in range(3):
            top += 1
            flags.append(top)
            for points in triples:
                solver.add_clause([-members[f][p] for p in points]+[top])
                clauses += 1
        for first, second in combinations(flags, 2):
            solver.add_clause([-first, -second])
            clauses += 1
    return top, {'triple_patterns': len(patterns),
                 'covered_triples': sum(map(len, patterns.values())),
                 'pattern_flags': 3*len(patterns), 'clauses': clauses}


def violations(Q, sets):
    """Three pairs above one quotient cannot inject into its two lifts.

    Return one minimal witness per overflowing projected label. Points of
    each input set are distinct, so the three edges use three points per leg.
    This criterion is necessary and independent of the central sign choices.
    """
    output = []
    for f, h in combinations(range(3), 2):
        fibers = {}
        for s in sets[f]:
            for t in sets[h]:
                q = Q['mul'][Q['inv'][s]][t]
                fibers.setdefault(q, []).append((s, t))
        for q, edges in sorted(fibers.items()):
            if len(edges) > 2:
                output.append({'type': 'exact-pair-capacity', 'legs': [f, h],
                               'label': q, 'edges': edges[:3]})
    return output


def verify(Q, record):
    f, h = record['legs']
    edges = record['edges']
    n = len(Q['representatives'])
    if not (0 <= f < h < 3 and len(edges) == 3
            and len({s for s, t in edges}) == 3
            and len({t for s, t in edges}) == 3):
        raise ValueError('capacity witness needs three distinct edges on two legs')
    if any(not (0 <= s < n and 0 <= t < n)
           or Q['mul'][Q['inv'][s]][t] != record['label'] for s, t in edges):
        raise ValueError('capacity witness has a wrong projected label')
    return sorted({(f, s) for s, t in edges} | {(h, t) for s, t in edges})

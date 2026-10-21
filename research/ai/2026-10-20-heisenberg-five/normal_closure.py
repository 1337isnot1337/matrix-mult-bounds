"""Exact finite normal-count and affine-incidence closure for Heisenberg(5)."""
from itertools import combinations_with_replacement, product
import json
from math import isqrt
from pathlib import Path
import sys

from source import RESEARCH
sys.path.insert(0, str(RESEARCH/'2026-10-20-normal-coset-koszul'))
from rectangular_certificate import rotate, rectangular_score
sys.path.insert(0, str(RESEARCH/'2026-10-20-group-potentials'))
from rank_locus_obstruction import profile, screen, gate_9_fourths


def patterns(total):
    rows = sorted(row for row in product(range(5), repeat=5) if sum(row) == total
                  and row == min(rotate(row, s) for s in range(5)))
    seen = set()
    for row in rows:
        orbit = {rotate(row, s) for s in range(5)}
        if seen & orbit:
            raise ArithmeticError('overlapping cyclic count classes')
        seen |= orbit
    coefficients = [1]
    for _ in range(5):
        updated = [0]*(len(coefficients)+4)
        for i, value in enumerate(coefficients):
            for j in range(5):
                updated[i+j] += value
        coefficients = updated
    if len(seen) != coefficients[total]:
        raise ArithmeticError('cyclic count classes do not cover all bounded compositions')
    return rows, len(seen)


def maximum_score(a, b, c):
    """Exact maximum at most 50, or an already valid larger obstruction."""
    best = 0
    for s in range(5):
        bb = rotate(b, s)
        for t in range(5):
            cc = rotate(c, t)
            best = max(best, rectangular_score(a, bb, cc),
                       rectangular_score(a, cc, bb), rectangular_score(bb, cc, a))
            if best > 50:
                return best
    return best


def derive():
    A, number9 = patterns(9)
    B, number10 = patterns(10)
    C, number11 = patterns(11)
    balanced = (2,)*5
    allowed_pairs, product_pairs = [], 0
    for i, a in enumerate(B):
        for j in range(i, len(B)):
            b = B[j]
            if 2*max(a)*max(b) > 25:
                continue
            product_pairs += 1
            # The balanced block makes one relative shift redundant.
            value = max(max(rectangular_score(balanced, a, rotate(b, s)),
                            rectangular_score(balanced, rotate(b, s), a),
                            rectangular_score(a, rotate(b, s), balanced)) for s in range(5))
            if value <= 50:
                allowed_pairs.append({'first': a, 'second': b, 'maximum_score': value})
    types = {tuple(sorted(row)) for record in allowed_pairs
             for row in (record['first'], record['second'])}
    if types != {(0, 0, 2, 4, 4), (0, 1, 3, 3, 3)}:
        raise ArithmeticError('balanced normal-count classification changed')
    pair_counts = [sum(v*(v-1)//2 for v in row)
                   for row in ((2,)*5, (0, 0, 2, 4, 4), (0, 1, 3, 3, 3))]
    if any(v % 4 != 1 for v in pair_counts) or (10*9//2) % 4 == 6 % 4:
        raise ArithmeticError('affine-incidence residue contradiction failed')
    allowed_triples, product_triples = [], 0
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            for k, c in enumerate(C):
                if max(a)*max(b)*max(c) > 25:
                    continue
                product_triples += 1
                value = maximum_score(a, b, c)
                if value <= 50:
                    if b != balanced:
                        raise ArithmeticError('unequal survivor has a nonbalanced middle family')
                    allowed_triples.append({'indices': [i, j, k], 'maximum_score': value})
    degrees = [1]*25+[5]*4
    ranks = profile(degrees)
    frontier = []
    for b in range(2, isqrt(125)+1):
        for c in range(b, 125//b+1):
            for a in range(2, b+1):
                if gate_9_fourths(degrees, [a, b, c]):
                    frontier.append(screen(degrees, [a, b, c], ranks))
    survivors = [row['shape'] for row in frontier if not row['excluded']]
    if survivors != [[10, 10, 10], [9, 10, 11], [10, 10, 11]]:
        raise ArithmeticError('uncovered source-cost frontier')
    return {'source': 'Heisenberg(5)', 'abelian_normal_order': 25, 'quotient_order': 5,
        'fiber_cap': 4, 'composition_counts': [number9, number10, number11],
        'cyclic_count_classes': [len(A), len(B), len(C)],
        'balanced_unordered_class_pairs': len(B)*(len(B)+1)//2,
        'balanced_pairs_passing_product': product_pairs,
        'balanced_surviving_pairs': allowed_pairs,
        'line_pair_counts': pair_counts, 'affine_directions': 6,
        'ten_point_unordered_pairs': 45, 'incidence_residue_modulus': 4,
        'unequal_ordered_class_triples': len(A)*len(B)*len(C),
        'unequal_triples_passing_product': product_triples,
        'unequal_surviving_triples': allowed_triples,
        'unequal_middle_family_forced_balanced': True,
        'source_cost_frontier': frontier, 'rank_locus_survivors': survivors,
        'status': 'proof-written-unreviewed', 'exponent_improvement': False,
        'scope': 'All single matrix targets from Heisenberg(5) through injective '
                 'coordinate pair maps and strict vertex potentials that pass the usual '
                 'degree-sum gate at an exponent in [2,9/4]. General complex tensor '
                 'degenerations and joint extraction are not excluded.'}


def replay(path):
    report = json.loads(path.read_text())
    expected = json.loads(json.dumps(derive()))
    if report != expected:
        raise ValueError('normal-count closure report differs from exact enumeration')
    return {'cyclic_count_classes': report['cyclic_count_classes'],
            'balanced_pairs_checked': report['balanced_unordered_class_pairs'],
            'unequal_triples_checked': report['unequal_ordered_class_triples'],
            'single_target_source_cost_frontier_closed': True,
            'scope': report['scope'], 'exponent_improvement': False}


if __name__ == '__main__':
    print(json.dumps(derive(), indent=2))

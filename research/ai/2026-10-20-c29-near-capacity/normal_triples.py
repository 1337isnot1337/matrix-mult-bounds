"""Exact classification of three-point unique-sum triples in C29.

Primary set-sum enumeration uses five affine templates for the first set.
An independent bit-mask loop tests all 126^3 translation-class triples.
"""
import argparse
from itertools import combinations, product
import json
from pathlib import Path

P = 29


def translation_canonical(points):
    return min(tuple(sorted((x-t) % P for x in points)) for t in points)


def affine_canonical(points):
    return min(translation_canonical([(s*x) % P for x in points])
               for s in range(1,P))


def classes():
    return sorted({translation_canonical((0,a,b))
                   for a,b in combinations(range(1,P),2)})


def is_progression(points):
    return any((2*b-a-c) % P == 0 for a,b,c in
               [(points[0],points[1],points[2]),
                (points[1],points[0],points[2]),
                (points[0],points[2],points[1])])


def primary():
    representatives = classes()
    templates = sorted({affine_canonical(A) for A in representatives})
    survivors = []
    pairs = tested = 0
    for A in templates:
        for B in representatives:
            pairs += 1
            AB = {(a+b) % P for a,b in product(A,B)}
            if len(AB) != 9:
                continue
            for C in representatives:
                tested += 1
                if len({(x+c) % P for x,c in product(AB,C)}) == 27:
                    survivors.append([list(A),list(B),list(C)])
    return {'translation_classes':len(representatives),
            'first_affine_templates':[list(x) for x in templates],
            'pairs_checked':pairs, 'sum_triples_checked_after_pair_injection':tested,
            'surviving_normalized_triples':survivors,
            'all_surviving_sets_are_progressions':all(is_progression(A)
                                                     for row in survivors for A in row)}


def independent():
    # Construct translation classes directly from all 3,654 actual subsets,
    # using all 29 cyclic rotations of their bit masks. Avoid the primary
    # canonicalization and its affine-template reduction entirely.
    mask_limit = (1 << P)-1

    def rotate(mask, shift):
        return ((mask << shift) | (mask >> (P-shift))) & mask_limit

    raw = set()
    subsets = 0
    for points in combinations(range(P),3):
        subsets += 1
        mask = sum(1 << x for x in points)
        raw.add(min(rotate(mask,t) for t in range(P)))
    representatives = [[j for j in range(P) if mask & (1 << j)] for mask in sorted(raw)]
    tested = positive = 0
    normalized = set()
    for A in representatives:
        for B in representatives:
            pair = [(a+b) % P for a in A for b in B]
            if len(set(pair)) != 9:
                # All 126 C choices fail without needing their masks.
                tested += len(representatives)
                continue
            mask = sum(1 << v for v in pair)
            shifts = [rotate(mask,c) for c in range(P)]
            for C in representatives:
                tested += 1
                a,b,c = (shifts[v] for v in C)
                if a & b or b & c or c & a:
                    continue
                positive += 1
                if not all(is_progression(x) for x in [A,B,C]):
                    raise ArithmeticError('non-progression sum triple found')
                candidates = []
                for scalar in range(1,P):
                    mapped = tuple(translation_canonical([(scalar*v) % P for v in row])
                                   for row in [A,B,C])
                    candidates.append(mapped)
                normalized.add(min(candidates))
    return {'actual_subsets_used_to_build_classes':subsets,
            'translation_classes':len(representatives),
            'class_triples_covered':tested,
            'positive_translation_class_triples':positive,
            'normalized_triples':[[list(x) for x in row] for row in sorted(normalized)],
            'all_positive_sets_are_progressions':True}


def report():
    first, second = primary(), independent()
    if first['surviving_normalized_triples'] != second['normalized_triples']:
        raise ArithmeticError('independent normalized lists disagree')
    if not first['all_surviving_sets_are_progressions']:
        raise ArithmeticError('arithmetic-progression statement fails')
    return {'claim':'AI-GROUP-C29-SUM-008', 'prime':P, 'primary':first,
            'independent':second, 'status':'exact finite classification; proof-written-unreviewed',
            'scope':'Three three-point subsets of C29 only; no group target is constructed.',
            'improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

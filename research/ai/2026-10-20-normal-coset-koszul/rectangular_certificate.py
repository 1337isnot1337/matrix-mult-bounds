"""Standard-library replay of the complete size-nineteen F8 count cover.

The binary byte stream gives a leg and two cyclic shifts for every triangle
not covered by pair averaging. Every byte is checked mathematically.
"""
import argparse
from collections import Counter
import hashlib
from itertools import product
import json
from math import comb
from pathlib import Path


def rotate(row,shift):
    return row[shift:]+row[:shift]


def patterns():
    return sorted(row for row in product(range(5),repeat=7)
                  if sum(row)==19 and row==min(rotate(row,s) for s in range(7)))


def verify_pattern_coverage(rows):
    # Independent coefficient recurrence counts every bounded composition.
    coefficients = [1]
    for _ in range(7):
        following = [0]*(len(coefficients)+4)
        for i,n in enumerate(coefficients):
            for value in range(5):
                following[i+value] += n
        coefficients = following
    orbit = set()
    for row in rows:
        if len(row)!=7 or sum(row)!=19 or any(v not in range(5) for v in row):
            raise ValueError('invalid fiber-count pattern')
        rotations = {rotate(row,s) for s in range(7)}
        if len(rotations)!=7 or orbit.intersection(rotations):
            raise ValueError('overlapping or incomplete cyclic normalization')
        orbit.update(rotations)
    if len(orbit)!=coefficients[19]:
        raise ValueError('cyclic classes do not cover all bounded compositions')
    return len(orbit)


def pair_weight(a,b):
    return sum(3*min(x,y)-int(x==y==1) for x,y in zip(a,b))


def rectangular_score(a,b,c):
    return sum(z*(3*min(x,y)-int(x==y==1)) for x,y,z in zip(a,b,c))


def replay(data):
    rows = patterns()
    actual_patterns = verify_pattern_coverage(rows)
    n = len(rows)
    bad = [0]*n
    histogram = Counter()
    for i,a in enumerate(rows):
        if pair_weight(a,a)<48:
            raise ArithmeticError('repeated pattern is not covered by averaging')
        for j in range(i+1,n):
            value = max(pair_weight(a,rotate(rows[j],s)) for s in range(7))
            histogram[value] += 1
            if value<48:
                bad[i] |= 1 << j
                bad[j] |= 1 << i
    count = 0
    ranks = Counter()
    for i in range(n):
        neighbors = bad[i] & ~((1 << (i+1))-1)
        while neighbors:
            bit = neighbors & -neighbors
            neighbors ^= bit
            j = bit.bit_length()-1
            common = bad[i] & bad[j] & ~((1 << (j+1))-1)
            while common:
                bit = common & -common
                common ^= bit
                k = bit.bit_length()-1
                if count>=len(data) or data[count]>=147:
                    raise ValueError('missing or invalid alignment byte')
                leg,shifts = divmod(data[count],49)
                shift_b,shift_c = divmod(shifts,7)
                a,b,c = rows[i],rotate(rows[j],shift_b),rotate(rows[k],shift_c)
                args = [(a,b,c),(a,c,b),(b,c,a)][leg]
                value = rectangular_score(*args)
                if value<=128:
                    raise ValueError('alignment does not obstruct a rank-64 source')
                ranks[value] += 1
                count += 1
    if count!=len(data):
        raise ValueError('unused alignment bytes')
    if not (18**9<700**4 and 78**4<7**9 and 700<7+9*78):
        raise ArithmeticError('balanced source gate separator failed')
    return {'claim':'AI-GROUP-F8-RECTANGULAR-013',
            'source_normal_subgroup':'C2^6','quotient':'C7','target_shape':[19]*3,
            'bounded_compositions_covered':actual_patterns,'cyclic_classes':n,
            'class_triples_mod_family_permutation':comb(n+2,3),
            'pair_maximum_weight_histogram':{str(k):v for k,v in sorted(histogram.items())},
            'pairs_not_covered_by_averaging':sum(b.bit_count() for b in bad)//2,
            'explicit_triangles_checked':count,
            'triples_covered_by_pair_averaging':comb(n+2,3)-count,
            'explicit_rank_histogram':{str(k):v for k,v in sorted(ranks.items())},
            'minimum_explicit_rank':min(ranks),
            'source_Koszul_rank_at_most':128,
            'witness_bytes':len(data),'witness_sha256':hashlib.sha256(data).hexdigest(),
            'balanced_gate_separator':{'target_18_ninth_power':18**9,
                                       'separator_fourth_power':700**4,
                                       'root_lower_fourth_power':78**4,
                                       'source_root_radicand':7**9,
                                       'source_cost_lower':7+9*78},
            'status':'proof-written-unreviewed','improves_omega':False,
            'scope':'All size-nineteen normal-fiber count patterns after the '
                    'F2^6 four-point cap, for the injective-pair-map construction '
                    'with strict vertex potentials. General complex degenerations remain open.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--witness',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = replay(args.witness.read_bytes())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

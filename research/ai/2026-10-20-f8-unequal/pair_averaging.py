"""Complete seven-slice averaging certificate for the (16,16,26) frame.

Only standard-library exact arithmetic is used. The input pencil report is
replayed before its ranks are used; no discovery solver is trusted.
"""
import argparse
from collections import Counter
from itertools import product
import json
from pathlib import Path

from koszul_tables import verify


def rotate(row,shift):
    return row[shift:]+row[:shift]


def classes(total):
    return sorted(row for row in product(range(5),repeat=7)
                  if sum(row)==total and row==min(rotate(row,s) for s in range(7)))


def coverage(rows,total):
    # Independent bounded-composition recurrence checks cyclic normalization.
    coefficients = [1]
    for _ in range(7):
        following = [0]*(len(coefficients)+4)
        for i,n in enumerate(coefficients):
            for v in range(5):
                following[i+v] += n
        coefficients = following
    seen = set()
    for row in rows:
        if len(row)!=7 or sum(row)!=total or any(type(v) is not int or not 0<=v<=4 for v in row):
            raise ValueError('invalid count pattern')
        orbit = {rotate(row,s) for s in range(7)}
        if seen.intersection(orbit):
            raise ValueError('duplicate cyclic orbit')
        seen.update(orbit)
    if len(seen)!=coefficients[total]:
        raise ValueError('incomplete count coverage')
    return len(seen)


def rank_tables(pencils):
    verify(pencils)
    tables = {p:[[0]*5 for _ in range(5)] for p in [2,3]}
    for row in pencils['records']:
        tables[row['p']][row['a']][row['b']] = row['rank_lower_bound']
    return tables


def replay(pencils):
    tables = rank_tables(pencils)
    table = tables[3]
    if any(table[a][b]!=table[b][a] for a,b in product(range(5),repeat=2)):
        raise ValueError('pair permutation requires a symmetric certified table')
    rows = classes(16)
    n_patterns = coverage(rows,16)
    histogram = Counter()
    sharp_pair = None
    minimum = None
    for i,a in enumerate(rows):
        for b in rows[i:]:
            weight = max(sum(table[x][y] for x,y in zip(a,rotate(b,s))) for s in range(7))
            histogram[weight] += 1
            if minimum is None or weight<minimum:
                minimum,sharp_pair = weight,[list(a),list(b)]
            if 26*weight <= 7*64*20:
                raise ValueError('pair is not excluded by seven-slice averaging')
    return {'shape':[16,16,26], 'fiber_bound':4, 'quotient_order':7,
            'bounded_count_patterns':n_patterns, 'cyclic_classes':len(rows),
            'unordered_pairs_with_repetition':sum(histogram.values()),
            'maximum_pair_weight_histogram':{str(k):histogram[k] for k in sorted(histogram)},
            'minimum_maximum_pair_weight':minimum,'sharp_pair':sharp_pair,
            'koszul_power':3,'slice_dimension':7,'rank_one_contribution':20,
            'source_koszul_rank_ceiling':1280,
            'target_averaged_rank_lower_bound':{'numerator':26*minimum,'denominator':7},
            'scope':'Injective pair maps and strict vertex potentials in a group with normal C2^6 and quotient C7. No general tensor-degeneration exclusion.',
            'status':'written proof with complete finite certificate; unreviewed',
            'improves_omega':False}


def count_receipt(pencils,counts):
    tables = rank_tables(pencils)
    tables[1] = [[3*min(a,b)-int(a==b==1) if a*b else 0
                  for b in range(5)] for a in range(5)]
    if len(counts)!=3 or any(len(row)!=7 or any(type(v) is not int or not 0<=v<=4 for v in row) for row in counts):
        raise ValueError('three bounded seven-entry count arrays required')
    levels = []
    for p,divisor in [(1,2),(2,6),(3,20)]:
        best = max(sum(z*tables[p][x][y] for x,y,z in
                       zip(counts[leg],rotate(counts[(leg+1)%3],j),rotate(counts[(leg+2)%3],k)))
                   for leg,j,k in product(range(3),range(7),range(7)))
        levels.append({'p':p,'maximum_certified_rank':best,'source_ceiling':64*divisor,
                       'excluded':best>64*divisor})
    capacities = [[sum(x*y for x,y in zip(counts[f],rotate(counts[g],s))) for s in range(7)]
                  for f,g in [(0,1),(1,2),(2,0)]]
    return {'fiber_counts':counts,'shape':list(map(sum,counts)),
            'pair_capacity_values':capacities,'pair_capacity_passes':max(map(max,capacities))<=64,
            'koszul_levels':levels,
            'scope':'Necessary count conditions only. No directions, offsets, pair maps or strict potential constructed.',
            'improves_omega':False}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pencils',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = replay(json.loads(args.pencils.read_text()))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

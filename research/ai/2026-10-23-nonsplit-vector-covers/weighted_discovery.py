"""Exact bounded weight search combining saved coordinate cover and degree."""
import argparse
from collections import Counter
from itertools import product
import json
from math import comb, gcd
from pathlib import Path
from functools import reduce


def multiply(left, right):
    out = [0]*(len(left)+len(right)-1)
    for a, x in enumerate(left):
        for b, y in enumerate(right):
            out[a+b] += x*y
    return out


def cutoffs(counts, maximum):
    cumulative = [0]
    for count in counts:
        cumulative.append(cumulative[-1]+count)
    target = maximum-2
    best = None
    for a in range(-1, target//3+1):
        for b in range(a, (target-a)//2+1):
            c = target-a-b
            cost = sum(cumulative[min(cut+1, len(counts))] for cut in (a,b,c))
            if best is None or cost < best[0]:
                best = cost, (a,b,c)
    return best


def run(source, limit):
    degrees = source['basis_degrees']
    selected = [set(leg) & set(range(88)) for leg in source['covers'][0]['selected_coordinates']]
    if not selected[0] == selected[1] == selected[2] or len(selected[0]) != 22:
        raise ValueError('expected the same 22-coordinate principal cover on all legs')
    rows = []
    for j in range(4):
        best = None
        checked = 0
        ps = [(s,q) for s in range(limit+1) for q in range(limit+1) if s+q] if j else [(0,0)]
        for s,q in ps:
            hist = Counter(s*degrees[a]+q*int(a not in selected[0]) for a in range(88))
            principal = [hist.get(k,0) for k in range(max(hist)+1)]
            powered = [1]
            for _ in range(j):
                powered = multiply(powered,principal)
            for a,b in product(range(1,limit+1) if j<3 else [0], range(1,limit+1)):
                if reduce(gcd,(s,q,a,b)) != 1:
                    continue
                counts = powered
                for _ in range(3-j):
                    counts = multiply(counts,[16]+[0]*(a-1)+[16])
                for _ in range(3):
                    counts = multiply(counts,[1]+[0]*(b-1)+[1])
                maximum = j*(8*s+2*q)+(3-j)*a+3*b
                cost,cuts = cutoffs(counts,maximum)
                checked += 1
                if best is None or cost < best['per_word_slices']:
                    best = {'weights':{'principal_degree':s,'principal_unselected':q,
                                       'matrix_central':a,'extra_C2':b},
                            'maximum_total_degree':maximum,'cutoffs':cuts,
                            'per_word_slices':cost,'degree_counts':counts}
        rows.append({'principal_factors':j,'word_multiplicity':comb(3,j),
                     'weight_vectors_checked':checked,'best':best})
    return {'status':'exact-bounded-weight-search', 'weight_limit':limit, 'rows':rows,
            'slice_upper_bound':sum(row['word_multiplicity']*row['best']['per_word_slices'] for row in rows),
            'optimality_certified':False,'exponent_improvement':False}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-certificate',type=Path,required=True)
    parser.add_argument('--limit',type=int,default=6)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    report=run(json.loads(args.source_certificate.read_text()),args.limit)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    for row in report['rows']:
        print(row['principal_factors'], row['weight_vectors_checked'],
              row['best']['weights'], row['best']['per_word_slices'])
    print('total',report['slice_upper_bound'])

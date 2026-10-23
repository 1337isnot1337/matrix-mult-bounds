"""Explicit rectangular Koszul pencils for small normal-coset matrix blocks.

Discovery uses deterministic small integer matrices. Acceptance recomputes
matrix rank modulo a prime; it is a lower bound over C, not a generic-rank
claim. Rank-one contribution is binomial(d-1,p) for d first-leg slices.
"""
import argparse
from itertools import combinations,product
import json
from math import comb
from pathlib import Path
import random
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'2026-10-20-normal-coset-koszul'))
from certificate import rank_mod


def koszul_matrix(slices,p):
    d = len(slices)
    if not slices or not 0<=p<d:
        raise ValueError('nonempty slices and 0<=p<d required')
    if not slices[0] or not slices[0][0]:
        raise ValueError('nonempty rectangular slices required')
    a,b = len(slices[0]),len(slices[0][0])
    if any(len(X)!=a or any(len(row)!=b for row in X) for X in slices):
        raise ValueError('consistent nonempty rectangular slices required')
    if any(type(value) is not int for X in slices for row in X for value in row):
        raise ValueError('integer coefficients required')
    inputs = list(combinations(range(d),p))
    outputs = {row:i for i,row in enumerate(combinations(range(d),p+1))}
    matrix = [[0]*(len(inputs)*b) for _ in range(len(outputs)*a)]
    for j,I in enumerate(inputs):
        for t,X in enumerate(slices):
            if t in I:
                continue
            J = tuple(sorted((*I,t)))
            sign = -1 if sum(i<t for i in I)%2 else 1
            k = outputs[J]
            for u,v in product(range(a),range(b)):
                matrix[k*a+u][j*b+v] += sign*X[u][v]
    return matrix


def discover(maximum=4,attempts=3):
    records = []
    for p in [2,3]:
        d = 2*p+1
        for a,b in product(range(1,maximum+1),repeat=2):
            best = None
            for attempt in range(attempts):
                seed = 20261020+10000*p+100*a+10*b+attempt
                rng = random.Random(seed)
                slices = [[[rng.randrange(-2,3) for _ in range(b)]
                           for _ in range(a)] for _ in range(d)]
                matrix = koszul_matrix(slices,p)
                rank = rank_mod(matrix,101)
                if best is None or rank>best['rank_lower_bound']:
                    best = {'a':a,'b':b,'p':p,'slice_dimension':d,
                            'rank_one_contribution':comb(d-1,p),'seed':seed,
                            'integer_slices':slices,'rank_lower_bound':rank,
                            'matrix_format':[len(matrix),len(matrix[0])],'modulus':101}
                if rank==comb(d,p)*min(a,b):
                    break
            records.append(best)
    return {'source_normal_subgroup_order':64,'maximum_matrix_side':maximum,
            'discovery_attempts_per_case':attempts,'records':records,
            'scope':__doc__,'improves_omega':False}


def verify(report):
    if report['source_normal_subgroup_order']!=64:
        raise ValueError('wrong normal subgroup order')
    keys = set()
    for row in report['records']:
        a,b,p = row['a'],row['b'],row['p']
        if any(type(value) is not int or value<1 for value in [a,b,p]):
            raise ValueError('positive integer pencil dimensions required')
        key = a,b,p
        if key in keys:
            raise ValueError('duplicate pencil case')
        keys.add(key)
        slices = row['integer_slices']
        if row['slice_dimension']!=2*p+1 or len(slices)!=2*p+1 or any(len(X)!=a or any(len(line)!=b for line in X) for X in slices):
            raise ValueError('pencil shape mismatch')
        if row['rank_one_contribution']!=comb(2*p,p):
            raise ValueError('wrong rank-one divisor')
        matrix = koszul_matrix(slices,p)
        if [len(matrix),len(matrix[0])]!=row['matrix_format']:
            raise ValueError('wrong Koszul matrix shape')
        if rank_mod(matrix,row['modulus'])!=row['rank_lower_bound']:
            raise ValueError('unverified rank lower bound')
    maximum = report['maximum_matrix_side']
    if keys!={(a,b,p) for a,b in product(range(1,maximum+1),repeat=2) for p in [2,3]}:
        raise ValueError('incomplete pencil table')
    return {'pencils_replayed':len(keys),'rank_semantics':'Exact modular lower bounds over C',
            'improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = discover()
    receipt = verify(result)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(receipt))
    for p in [2,3]:
        print('p',p,[[next(r['rank_lower_bound'] for r in result['records']
                           if (r['a'],r['b'],r['p'])==(a,b,p)) for b in range(1,5)] for a in range(1,5)])

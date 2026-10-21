"""All size-ten fiber patterns after the C29 three-point classification.

Normal-fiber directions and pair-quotient translations are exact necessary
tests. Offsets are independent in each pair quotient; surviving triples are
not global group constructions or positive-potential witnesses.
"""
import argparse
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path

from cyclic_packing import options, pack
from normal_triples import primary, is_progression

P = 29
SCALARS = (1,12,28,17)


def step(points):
    if not is_progression(points):
        raise ValueError('arithmetic progression required')
    for center in points:
        distances = {(v-center) % P for v in points if v != center}
        if len(distances) == 2:
            d = min(distances)
            if distances == {d,(-d) % P}:
                return min(d,P-d)
    raise ArithmeticError('progression center not found')


def points(kind):
    size,d = kind
    return (0,) if size == 1 else ((0,d) if size == 2 else tuple(sorted((0,d,P-d))))


@lru_cache(None)
def unique(kinds):
    value = {0}
    size = 1
    for kind in kinds:
        row = points(kind)
        size *= len(row)
        value = {(x+y) % P for x in value for y in row}
    return len(value) == size


def family_domains(base, family):
    other = tuple((3,d) for f,d in enumerate(base) if f != family)
    d3 = [d for d in range(1,15) if unique(((3,d),*other))]
    d2 = [d for d in range(1,15) if unique(((2,d),*other))]
    result = []
    # Identity is an independently selected largest fiber in every family.
    for second in range(1,4):
        short = [a for a in range(1,4) if a != second]
        for direction,e,f in product(d3,d2,d2):
            row = [None]*4
            row[0],row[second] = (3,base[family]),(3,direction)
            row[short[0]],row[short[1]] = (2,e),(2,f)
            result.append(tuple(row))
    for last in range(1,4):
        large = [a for a in range(1,4) if a != last]
        for e,f in product(d3,repeat=2):
            row = [None]*4
            row[0],row[last] = (3,base[family]),(1,0)
            row[large[0]],row[large[1]] = (3,e),(3,f)
            result.append(tuple(row))
    if len(set(result)) != len(result):
        raise ArithmeticError('duplicated family pattern')
    return result


@lru_cache(None)
def pair_orbits(left, right, scalar):
    values = {(pow(scalar,-1,P)*(y-x)) % P for x,y in product(points(left),points(right))}
    if len(values) != left[0]*right[0]:
        return None
    return tuple(options(sorted(values),P))


@lru_cache(None)
def quotient_pack(rows):
    return pack(rows,P)


def pair_compatible(left, right, other_base):
    if any(not unique((a,b,(3,other_base))) for a,b in product(left,right)):
        return False,'normal-with-third-base'
    for q in SCALARS:
        rows = []
        for i,a in enumerate(SCALARS):
            j = SCALARS.index(a*q % P)
            orbit = pair_orbits(left[i],right[j],a)
            if orbit is None:
                return False,'normal-pair-collision'
            rows.append(orbit)
        # Feasibility does not depend on the order of the four mask domains.
        result = quotient_pack(tuple(sorted(rows)))
        if not result['satisfiable']:
            return False,f'quotient-{q}'
    return True,'passes'


def run(base_limit=None):
    unique.cache_clear()
    pair_orbits.cache_clear()
    quotient_pack.cache_clear()
    normalized = primary()['surviving_normalized_triples']
    bases = sorted({tuple(step(row) for row in triple) for triple in normalized})
    if base_limit is not None:
        bases = bases[:base_limit]
    records = []
    for base in bases:
        domains = [family_domains(base,f) for f in range(3)]
        edges = []
        pair_stats = []
        for f,g in [(0,1),(1,2),(2,0)]:
            h = 3-f-g
            compatible = set()
            reasons = {}
            for i,left in enumerate(domains[f]):
                for j,right in enumerate(domains[g]):
                    answer,reason = pair_compatible(left,right,base[h])
                    reasons[reason] = reasons.get(reason,0)+1
                    if answer:
                        compatible.add((i,j))
            edges.append(compatible)
            pair_stats.append({'families':[f,g], 'domain_pairs':len(domains[f])*len(domains[g]),
                               'outcomes':reasons,'compatible_pairs':len(compatible)})
        survivors = []
        normal_failures = 0
        triangles = 0
        third_by_second = {}
        for j,k in edges[1]:
            third_by_second.setdefault(j,[]).append(k)
        for i,j in sorted(edges[0]):
            for k in sorted(third_by_second.get(j,[])):
                if (k,i) not in edges[2]:
                    continue
                triangles += 1
                cells = [domains[0][i],domains[1][j],domains[2][k]]
                if any(not unique(row) for row in product(*cells)):
                    normal_failures += 1
                    continue
                survivors.append({'family_indices':[i,j,k], 'cells':cells})
        records.append({'base_directions':base,'family_domain_sizes':list(map(len,domains)),
                        'pair_statistics':pair_stats,'pair_compatible_triangles':triangles,
                        'rejected_by_full_normal_triples':normal_failures,'survivors':survivors})
    return {'group':'C29:C4','shape':[10]*3,'records':records,
            'bases_covered':len(bases),'local_survivors':sum(len(x['survivors']) for x in records),
            'distinct_quotient_packing_problems':quotient_pack.cache_info().currsize,
            'scope':__doc__,'improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-limit',type=int)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = run(args.base_limit)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'records'},indent=2))

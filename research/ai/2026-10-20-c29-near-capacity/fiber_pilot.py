"""Finite C29:C4 local pilot: opposite large fibers, constant AP directions.

Three-point fibers lie over 1,-1 and use directions 1,3,9. Two-point fibers
lie over the other two scalar cosets and share a direction within a family.
Offsets are relaxed independently in every pair quotient. A local survivor
is not a global construction or a positive-potential witness.
"""
import argparse
from itertools import product
import json
from pathlib import Path

from cyclic_packing import options, pack

P = 29
SCALARS = [1,12,28,17]
STEPS = [1,3,9]


def normal_options():
    large = [{(-d) % P,0,d} for d in STEPS]
    domains = []
    for f in range(3):
        pair = {0}
        for g in range(3):
            if f != g:
                pair = {(a+b) % P for a,b in product(pair,large[g])}
        differences = {(a-b) % P for a,b in product(pair,pair)}
        domains.append([d for d in range(1,15) if d not in differences])
    return large,domains


def run():
    large,domains = normal_options()
    candidates = normal_pass = nodes = 0
    failures = {}
    survivors = []
    for short in product(*domains):
        candidates += 1
        point_types = [[large[f],{0,short[f]}] for f in range(3)]
        if any(len({(a+b+c) % P for a,b,c in product(*row)}) !=
               len(row[0])*len(row[1])*len(row[2])
               for row in product(*point_types)):
            continue
        normal_pass += 1
        cells = [{a:(large[f] if a in [1,28] else {0,short[f]})
                  for a in SCALARS} for f in range(3)]
        receipts = []
        for f,g in [(0,1),(1,2),(2,0)]:
            for q in SCALARS:
                rows = []
                for a in SCALARS:
                    b = a*q % P
                    points = {(pow(a,-1,P)*(y-x)) % P
                              for x,y in product(cells[f][a],cells[g][b])}
                    if len(points) != len(cells[f][a])*len(cells[g][b]):
                        raise ArithmeticError('unexpected pair collision')
                    rows.append(options(sorted(points),P))
                result = pack(rows,P)
                nodes += result['search_nodes']
                if not result['satisfiable']:
                    key = f'{f},{g},q={q}'
                    failures[key] = failures.get(key,0)+1
                    break
                receipts.append({'pair':[f,g],'quotient':q,
                                 'selected_masks':result['selected_masks']})
            else:
                continue
            break
        else:
            survivors.append({'short_directions':list(short),'pair_packings':receipts})
    return {'group':'C29:C4','shape':[10]*3,'large_scalars':[1,28],
            'large_directions':STEPS,'short_direction_domains':domains,
            'short_direction_choices_checked':candidates,
            'normal_triple_choices_passing':normal_pass,
            'first_pair_failures':failures,'survivors':survivors,
            'search_nodes':nodes,'scope':__doc__,'improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'survivors'},indent=2))

"""Seeded search for compatible polynomial-flag weight chambers.

This samples integer weights. It does not enumerate the real hyperplane
arrangement or prove the selected chamber minimizes any count.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random


POINTS = [(a, d-a) for d in range(4) for a in range(d+1)]


def inspect(eta, beta):
    wy = [eta[a+b]-beta*a for a,b in POINTS]
    wz = [-eta[3-c-d]-beta*c for c,d in POINTS]
    if len(set(wy)) != 10 or len(set(wz)) != 10:
        return None
    ry = {v:j for j,v in enumerate(sorted(wy))}
    rz = {v:j for j,v in enumerate(sorted(wz))}
    degrees_y = [9-ry[w] for w in wy]
    pivots_z = [rz[w] for w in wz]
    constraints, forced, pivot_targets = [], [], []
    for p in range(4):
        for y,(a,b) in enumerate(POINTS):
            for z,(c,d) in enumerate(POINTS):
                weight = beta*p+wy[y]+wz[z]
                if weight > 0:
                    continue
                wanted = int(p == a+c and a+b+c+d == 3)
                delta = 3-p+degrees_y[y]-pivots_z[z]
                if delta < 0:
                    if wanted:
                        return None
                    forced.append((p,y,z))
                elif delta == 0 and not wanted:
                    return None
                else:
                    constraints.append((p,y,z,wanted))
                    if delta == 0:
                        pivot_targets.append((p,y,z))
    key = (tuple(degrees_y),tuple(pivots_z),tuple(constraints))
    summary = {'eta':eta,'equations':len(constraints),
               'zeros':sum(not row[3] for row in constraints),
               'orders':[degrees_y,pivots_z],'delta0':len(pivot_targets),
               'identically_zero_nonpositive_entries':len(forced)}
    return key, summary


def search(seed=829191, samples=20000, bound=900, beta=100):
    rng = random.Random(seed)
    patterns = {}
    survivors = 0
    for _ in range(samples):
        eta = [0]+[rng.randint(-bound,bound) for _ in range(3)]
        item = inspect(eta,beta)
        if item is None:
            continue
        survivors += 1
        key,summary = item
        patterns.setdefault(key,summary)
    ordered = sorted(patterns.values(),key=lambda r:r['equations'])
    histogram = Counter(r['equations'] for r in ordered)
    return {'seed':seed,'samples':samples,'offset_bound':bound,'beta':beta,
            'survivors':survivors,'distinct_coefficient_patterns':len(patterns),
            'pattern_count_by_equations':dict(sorted(histogram.items())),
            'best_patterns':ordered[:20],
            'scope':'Seeded integer sample; no exhaustive chamber or optimality claim.',
            'exact_solution_found':False,'improves_omega':False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,default=829191)
    parser.add_argument('--samples',type=int,default=20000)
    parser.add_argument('--bound',type=int,default=900)
    parser.add_argument('--beta',type=int,default=100)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = search(args.seed,args.samples,args.bound,args.beta)
    result['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print({key:value for key,value in result.items() if key!='best_patterns'})


if __name__ == '__main__':
    main()

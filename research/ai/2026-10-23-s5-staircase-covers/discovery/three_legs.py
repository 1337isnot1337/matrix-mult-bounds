"""Independent Python continuation with three unequal monotone legs, r=1."""
import argparse
from itertools import accumulate, combinations_with_replacement
import importlib.util
import json
from math import comb
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('prior_staircase', PACKAGE/'staircases.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)


def run(j):
    maximum, k = 6*j, 6-j
    counts = [16**(3-j)*comb(k, e) for e in range(k+1)]
    prefix = [0]+list(accumulate(prior.principal_counts(j)))
    firsts = []
    for ascending in combinations_with_replacement(range(-1, maximum+1), k+1):
        f = ascending[::-1]
        firsts.append((sum(c*prefix[v+1] for c, v in zip(counts, f)), f))
    firsts.sort()
    best = prefix[-1]*sum(counts)
    witness = [[-1]*(k+1), [-1]*(k+1), [maximum]*(k+1)]
    evaluated = 0
    for a, (first_cost, first) in enumerate(firsts):
        if 2*first_cost >= best:
            break
        for second_cost, second in firsts[a:]:
            initial = first_cost+second_cost
            if initial >= best:
                break
            evaluated += 1
            pair_minimum = [2*maximum+1]*(k+1)
            for u, x in enumerate(first):
                if x == maximum:
                    continue
                for v in range(k-u+1):
                    y = second[v]
                    if y < maximum and x+y < pair_minimum[u+v]:
                        pair_minimum[u+v] = x+y
            for t in range(1, k+1):
                pair_minimum[t] = min(pair_minimum[t], pair_minimum[t-1])
            third = [max(-1, maximum-2-pair_minimum[k-c]) for c in range(k+1)]
            cost = initial + sum(c*prefix[v+1] for c, v in zip(counts, third))
            if cost < best:
                best, witness = cost, [list(first), list(second), third]
    return {'principal_factors': j, 'central_factors': k, 'staircases': len(firsts),
            'unordered_pair_universe': len(firsts)*(len(firsts)+1)//2,
            'evaluated_pairs': evaluated, 'cost': best, 'cutoffs': witness}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for j in range(4):
        row = run(j)
        rows.append(row)
        args.output.write_text(json.dumps({'scope': 'r=1, three monotone legs, bidegree majorant',
                                          'completed_rows': rows, 'complete': len(rows)==4}, indent=2)+'\n')
        print(json.dumps(row), flush=True)

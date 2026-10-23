"""Replay the declared forty-case degree-one additive-cost discovery pilot."""

import argparse
import importlib.util
import json
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('additive_degree_controls', PACKAGE/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def cases():
    x, z = v.X, v.Z
    for n in range(3, 7):
        for r in range(2, n):
            for kind in ['separated', 'mixed']:
                c = [x+z if kind == 'separated' else 1+x*z]
                c += [(j+1)*x+(j-1)*z for j in range(1, r-1)]
                for seed in [0, r-1]:
                    f = [0]*(2*n-1)
                    f[seed] = 1
                    for k in range(len(f)-r):
                        f[k+r] = v.sp.expand(sum(c[j]*f[k+j] for j in range(r-1)))
                    yield n, r, kind, seed, f


def report():
    rows = []
    for n, r, kind, seed, f in cases():
        name = f'n{n}-r{r}-{kind}-seed{seed}'
        literal = v.control(name, f, n, n, r, 1, 1)
        bound = n*n*r+2*n*(n-r)
        rows.append({'n': n, 'r': r, 'kind': kind, 'seed': seed,
                     'full_slice_rank': literal['full_slice_rank'],
                     'inner_ranks': literal['literal_inner_ranks'],
                     'primitive_degrees': literal['primitive_degrees'],
                     'candidate_additive_bound': bound,
                     'candidate_gap': literal['full_slice_rank']-bound})
    return {'cases': rows, 'complete_declared_cases': 40,
            'violations': sum(row['candidate_gap'] < 0 for row in rows),
            'minimum_observed_gap': min(row['candidate_gap'] for row in rows),
            'general_additive_inequality_proved': False,
            'independent_review': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = json.dumps(report(), indent=2)+'\n'
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end='')

"""Related order-48 direct-product discovery control; optional SAT dependencies."""
import argparse
from itertools import combinations
from pathlib import Path
import sys

from source_data import SEVEN, central_projection
sys.path.insert(0, str(SEVEN/'imported'))
from group_exact import group
import search


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=120)
    args = parser.parse_args()
    B = group(3)
    G = {'name': 'SL(2,3) x C2', 'identity': 0,
         'matrices': [(g, b) for g in B['matrices'] for b in (0, 1)],
         'mul': [[2*B['mul'][g//2][h//2]+((g & 1) ^ (h & 1))
                  for h in range(48)] for g in range(48)],
         'inv': [2*B['inv'][g//2]+(g & 1) for g in range(48)]}
    center = [z for z in range(48) if all(G['mul'][z][g] == G['mul'][g][z]
                                         for g in range(48))]
    orbits = sorted({tuple(sorted(G['mul'][z][g] for z in center)) for g in range(48)})
    Q = central_projection(G, {'central_orbits': orbits})
    original = search.build_solver

    def build(source, shape, seed, engine):
        solver, members, metadata = original(source, shape, seed, engine)
        if len(center) != 4 or any(n <= 24 for n in (36, 42, 42)):
            raise ArithmeticError('central-pair bound premise failed')
        for row in members:
            for orbit in orbits:
                for g, h in combinations(orbit, 2):
                    solver.add_clause([-row[g], -row[h]])
        metadata['central_orbits'] = len(orbits)
        metadata['projected_inverse_class_lift_sizes'] = sorted(
            map(len, Q['inverse_class_lifts'].values()))
        return solver, members, metadata

    search.group = lambda _p=5: G
    search.build_solver = build
    search.run([6, 6, 7], args.seconds, 20260367, args.output,
               max_models=1000, engine='cadical195')


if __name__ == '__main__':
    main()

"""Arbitrary central colors over two parallel projected lines in Heisenberg(5)."""
import argparse
from itertools import product
import json
from pathlib import Path
import sys

from source import group, RESEARCH
sys.path.insert(0, str(RESEARCH/'2026-10-20-sl2-seven/imported'))
from pysat.card import CardEnc
import search


def projected_line_pairs():
    lines = {tuple(sorted({(t*a % 5, t*b % 5) for t in range(5)}))
             for a, b in product(range(5), repeat=2) if (a, b) != (0, 0)}
    sets = set()
    for L in lines:
        for x, y in product(range(5), repeat=2):
            other = {(x+a) % 5*5+(y+b) % 5 for a, b in L}
            first = {5*a+b for a, b in L}
            if not first & other:
                sets.add(tuple(sorted(first | other)))
    if len(sets) != 24:
        raise ArithmeticError('expected 24 normalized line pairs')
    return sorted(sets)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=300)
    args = parser.parse_args()
    G = group()
    projections = projected_line_pairs()
    first = tuple(sorted(5*a+b for a in range(5) for b in (0, 1)))
    original = search.build_solver

    def build(source, shape, seed, engine):
        solver, members, metadata = original(source, shape, seed, engine)
        top = metadata['variables']
        for q in first:
            solver.add_clause([members[0][5*q+c] for c in range(5)])
        for f in (1, 2):
            flags = []
            for projected in projections:
                top += 1
                flag = top
                flags.append(flag)
                for q in projected:
                    solver.add_clause([-flag]+[members[f][5*q+c] for c in range(5)])
            card = CardEnc.equals(flags, 1, top_id=top)
            solver.append_formula(card.clauses)
            top = card.nv
        metadata['first_projection'] = first
        metadata['other_projection_options'] = len(projections)
        metadata['central_colors_per_point'] = 5
        metadata['variables_with_projection_selectors'] = top
        return solver, members, metadata

    search.group = lambda _p=5: G
    search.build_solver = build
    search.run([10]*3, args.seconds, 20260510, args.output, 1000, engine='cadical195')


if __name__ == '__main__':
    main()

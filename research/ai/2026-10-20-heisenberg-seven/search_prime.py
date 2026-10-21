"""Heisenberg(7) construction search beyond the closed full-coset family."""
import argparse
from itertools import combinations
import json
from pathlib import Path
import sys

FIVE = Path(__file__).resolve().parents[1]/'2026-10-20-heisenberg-five'
sys.path.insert(0, str(FIVE))
from source import group, source_gate, RESEARCH
sys.path.insert(0, str(RESEARCH/'2026-10-20-sl2-seven/imported'))
from pysat.card import CardEnc
import search


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--first-size', type=int, choices=(16, 17), default=16)
    args = parser.parse_args()
    p = 7
    G = group(p)
    shape = [16, 16, 17] if args.first_size == 16 else [17, 16, 16]
    directions = [(1, k) for k in range(p)]+[(0, 1)]
    fibers = [[sorted(q for q in range(p*p)
                      if (a*(q % p)-b*(q//p)) % p == k) for k in range(p)]
              for a, b in directions]
    original = search.build_solver

    def build(source, sizes, seed, engine):
        solver, members, metadata = original(source, sizes, seed, engine)
        top = metadata['variables']
        presence = []
        for f in range(3):
            row = []
            for q in range(p*p):
                top += 1
                variable = top
                row.append(variable)
                colors = [members[f][p*q+c] for c in range(p)]
                solver.add_clause([-variable]+colors)
                for v in colors:
                    solver.add_clause([-v, variable])
                for v, w in combinations(colors, 2):
                    solver.add_clause([-v, -w])
            card = CardEnc.equals(row, sizes[f], top_id=top)
            solver.append_formula(card.clauses)
            top = card.nv
            presence.append(row)
        for d in range(p+1):
            flags = []
            for f in range(3):
                row = {}
                for threshold in (4, 5):
                    top += 1
                    row[threshold] = top
                    for fiber in fibers[d]:
                        for chosen in combinations(fiber, threshold):
                            solver.add_clause([-presence[f][q] for q in chosen]+[top])
                for fiber in fibers[d]:
                    for chosen in combinations(fiber, 6):
                        solver.add_clause([-presence[f][q] for q in chosen])
                flags.append(row)
            solver.add_clause([-flags[f][4] for f in range(3)])
            for f in range(3):
                for h in range(3):
                    if f != h:
                        solver.add_clause([-flags[f][5], -flags[h][4]])
        # At least one family has maximum three in >=3 of the eight normal
        # directions. A common GL2 automorphism sends three of them to
        # horizontal, vertical, diagonal. Both possible first sizes are run.
        for a, b in ((1, 0), (0, 1), (1, 1)):
            for k in range(p):
                fiber = [q for q in range(p*p) if (a*(q % p)-b*(q//p)) % p == k]
                for chosen in combinations(fiber, 4):
                    solver.add_clause([-presence[0][q] for q in chosen])
        # The central shear c -> c+u*a+v*b can make two independent selected
        # first points have central height zero. Require zero-height points
        # on at least two distinct lines through the origin.
        zero_lines = []
        for a, b in directions:
            top += 1
            flag = top
            zero_lines.append(flag)
            solver.add_clause([-flag]+[members[0][p*(p*((t*a) % p)+(t*b) % p)]
                                       for t in range(1, p)])
        card = CardEnc.atleast(zero_lines, 2, top_id=top)
        solver.append_formula(card.clauses)
        metadata.update(projected_points=p*p, central_colors=p,
            abelian_fiber_directions=p+1, normal_fiber_cap=5,
            first_three_direction_cap=3, central_shear_zero_lines=2,
            variables_after_normalization=card.nv,
            normalization_status='written derivation; unreviewed')
        return solver, members, metadata

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.with_name('source-gate.json').write_text(
        json.dumps(source_gate(p, (16, 16, 17)), indent=2)+'\n')
    search.group = lambda _p=5: G
    search.build_solver = build
    search.run(shape, args.seconds, 20260700+args.first_size, args.output,
               max_models=1000, engine='cadical195')


if __name__ == '__main__':
    main()
